"""Check the checked-in method identity and absence of private publication links."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import tarfile
import zipfile

ROOT=Path(__file__).resolve().parents[1]
FORBIDDEN=re.compile(rb'-agents|#agents|requirements_skill_dir|@shared_requirements_method@',re.I)


def inspect(name,data):
    if FORBIDDEN.search(data):raise ValueError('Private tooling reference in '+name)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--published',type=Path);args=parser.parse_args()
    directory=ROOT/'tools/method';marker=json.loads((directory/'.method-package.json').read_text())
    for name,expected in marker['files'].items():
        path=directory/name
        if path.is_symlink() or not path.resolve().is_relative_to(directory.resolve()):raise ValueError('Unsafe method file: '+name)
        data=path.read_bytes()
        if hashlib.sha256(data).hexdigest()!=expected:raise ValueError('Method file differs from imported package: '+name)
        inspect(name,data)
    for path in (ROOT/'docs').rglob('*.rst'):
        if '_build' not in path.parts:
            inspect(str(path.relative_to(ROOT)),path.read_bytes())
    if args.published:
        directory=args.published
        for path in directory.rglob('*'):
            if not path.is_file():continue
            data=path.read_bytes();inspect(str(path),data)
            if zipfile.is_zipfile(path):
                with zipfile.ZipFile(path) as archive:
                    for name in archive.namelist():inspect(str(path)+'!'+name,archive.read(name))
            elif path.name.endswith(('.tar.gz','.tgz')):
                with tarfile.open(path) as archive:
                    for entry in archive:
                        if entry.isfile():inspect(str(path)+'!'+entry.name,archive.extractfile(entry).read())
    print('Method package/publication checks passed')


if __name__=='__main__':main()
