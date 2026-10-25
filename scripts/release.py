"""Validate and stage exact release assets; never upload or create a release."""
import argparse
from email.parser import BytesParser
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import runpy
import subprocess
import sys
import tarfile
from urllib.request import urlopen
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def version():
    return runpy.run_path(str(ROOT / 'src/sphinx_traceability_view/_version.py'))['__version__']


def validate_tag(tag):
    value = version()
    if not re.fullmatch(r'\d+\.\d+\.\d+', value) or tag != 'v' + value:
        raise ValueError('A final vMAJOR.MINOR.PATCH tag must match the package version')
    return value


def names(value):
    stem = 'sphinx_traceability_view-' + value
    return (stem + '-py3-none-any.whl', stem + '.tar.gz')


def validate_artifacts(directory, tag):
    value = validate_tag(tag)
    wheel_name, source_name = names(value)
    expected_names = {wheel_name, source_name}
    lines = (directory / 'SHA256SUMS').read_text(encoding='utf-8').splitlines()
    sums = {}
    for line in lines:
        match = re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)', line)
        if not match or match[2] in sums:
            raise ValueError('Invalid or duplicate release checksum entry')
        sums[match[2]] = match[1]
    if set(sums) != expected_names:
        raise ValueError('Checksums must identify exactly the wheel and source archive')
    for name, digest in sums.items():
        if hashlib.sha256((directory / name).read_bytes()).hexdigest() != digest:
            raise ValueError('Release checksum mismatch: ' + name)

    description = (ROOT / 'PYPI.rst').read_text(encoding='utf-8').strip()

    def metadata(data):
        message = BytesParser().parsebytes(data)
        if (message['Name'] != 'sphinx-traceability-view' or message['Version'] != value
                or message['Description-Content-Type'] != 'text/x-rst'
                or message.get_payload().replace('\r\n', '\n').strip() != description):
            raise ValueError('Release package metadata differs from the tagged source')

    def source_bytes(name, data):
        path = PurePosixPath(name)
        if path.is_absolute() or '..' in path.parts or '\\' in name:
            raise ValueError('Unsafe archive path')
        local = ROOT.joinpath(*path.parts)
        if not local.is_file():
            raise ValueError('Release archive differs from tagged source: ' + name)
        current = local.read_bytes()
        text = path.suffix in {'.py', '.rst', '.toml', '.json', '.txt', '.css'} or (
            path.suffix == '.js' and 'static' not in path.parts)
        if text:
            # Git may use CRLF for source text; packaged browser binaries remain exact.
            current, data = current.replace(b'\r\n', b'\n'), data.replace(b'\r\n', b'\n')
        if current != data:
            raise ValueError('Release archive differs from tagged source: ' + name)

    with zipfile.ZipFile(directory / wheel_name) as archive:
        members = archive.namelist()
        meta = [n for n in members if n.endswith('.dist-info/METADATA')]
        if len(meta) != 1:
            raise ValueError('Expected one wheel metadata record')
        metadata(archive.read(meta[0]))
        package_files = {n for n in members if n.startswith('sphinx_traceability_view/')}
        expected = {p.relative_to(ROOT / 'src').as_posix()
                    for p in (ROOT / 'src/sphinx_traceability_view').rglob('*')
                    if p.is_file() and not {'tests', '__pycache__'} & set(p.parts)
                    and p.name != 'README.rst' and p.suffix not in ('.pyc', '.pyo')}
        if package_files != expected:
            raise ValueError('Wheel runtime inventory differs from tagged source')
        for name in package_files:
            source_bytes('src/' + name, archive.read(name))

    with tarfile.open(directory / source_name) as archive:
        seen = set()
        for member in archive.getmembers():
            if member.isdir():
                continue
            if not member.isfile():
                raise ValueError('Source archive must not contain links')
            prefix, separator, relative = member.name.partition('/')
            if prefix != 'sphinx_traceability_view-' + value or not separator or relative in seen:
                raise ValueError('Unexpected or duplicate source archive member')
            seen.add(relative)
            data = archive.extractfile(member).read()
            if relative == 'PKG-INFO':
                metadata(data)
            else:
                source_bytes(relative, data)
        if not {'PKG-INFO', 'PYPI.rst', 'pyproject.toml', 'src/sphinx_traceability_view/_version.py'} <= seen:
            raise ValueError('Source archive is incomplete')
    return sums


def prepare(event, destination):
    release = event['release']
    if release['draft'] or release['prerelease'] or event['repository']['full_name'] != 'sysblacksmith/STV_sphinx-traceability-view':
        raise ValueError('Only a final public project release may publish')
    tag = release['tag_name']
    value = validate_tag(tag)
    subprocess.run(['git', 'merge-base', '--is-ancestor', 'HEAD', 'origin/main'], cwd=ROOT, check=True)
    tagged = subprocess.check_output(['git', 'rev-parse', tag + '^{commit}'], cwd=ROOT, text=True).strip()
    head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    if head != tagged:
        raise ValueError('Checkout must identify the release tag exactly')
    wanted = set(names(value)) | {'SHA256SUMS'}
    assets = [a for a in release['assets'] if a['name'] in wanted]
    if len(assets) != 3 or {a['name'] for a in assets} != wanted:
        raise ValueError('Attach the qualified wheel, sdist and SHA256SUMS before publishing')
    incoming = destination / 'incoming'
    incoming.mkdir(parents=True, exist_ok=False)
    for asset in assets:
        url = asset['browser_download_url']
        prefix = 'https://github.com/sysblacksmith/STV_sphinx-traceability-view/releases/download/'
        if not url.startswith(prefix) or asset['size'] > 100_000_000:
            raise ValueError('Unexpected release asset URL or size')
        with urlopen(url, timeout=60) as response:
            data = response.read(100_000_001)
        if len(data) != asset['size']:
            raise ValueError('Incomplete or oversized release download')
        (incoming / asset['name']).write_bytes(data)
    sums = validate_artifacts(incoming, tag)
    subprocess.run([sys.executable, '-m', 'twine', 'check', '--strict',
                    *[str(incoming / n) for n in sorted(sums)]], check=True)
    packages = destination / 'packages'
    packages.mkdir()
    for name in sums:
        (incoming / name).rename(packages / name)
    (destination / 'SHA256SUMS').write_bytes(''.join(
        digest + '  packages/' + name + '\n' for name, digest in sorted(sums.items())).encode())
    # Do not include staging or downloaded checksum files in the publishing artifact.
    (incoming / 'SHA256SUMS').unlink()
    incoming.rmdir()


def validate_docs():
    subprocess.run([sys.executable, 'tools/method/tooling/validate_traceability.py',
                    'docs/_build/html/needs.json', '--version', '.'.join(version().split('.')[:2]),
                    '--repo-root', '.', '--require-test-coverage'], cwd=ROOT, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['prepare', 'check', 'validate-docs'])
    parser.add_argument('--directory', type=Path, default=ROOT / 'docs/_build/release-publish')
    parser.add_argument('--tag')
    args = parser.parse_args()
    if args.command == 'prepare':
        prepare(json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text(encoding='utf-8')), args.directory)
    elif args.command == 'check':
        validate_artifacts(args.directory, args.tag)
    else:
        validate_docs()


if __name__ == '__main__':
    main()
