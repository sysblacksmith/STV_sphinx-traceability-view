"""Publication rejects mismatched versions, tampered bytes and altered source."""
import hashlib
import importlib.util
from pathlib import Path
import tarfile
from io import BytesIO
import zipfile
import pytest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('release_publication', ROOT/'scripts/release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


def fixture(tmp_path, monkeypatch):
    source = tmp_path/'source'
    package = source/'src/sphinx_traceability_view'
    package.mkdir(parents=True)
    (package/'_version.py').write_text('__version__ = "1.1.0"\n')
    (source/'PYPI.rst').write_text('Public description\n')
    (source/'pyproject.toml').write_text('[project]\n')
    monkeypatch.setattr(release, 'ROOT', source)
    out = tmp_path/'dist'; out.mkdir()
    wheel, sdist = release.names('1.1.0')
    metadata = b'Name: sphinx-traceability-view\nVersion: 1.1.0\nDescription-Content-Type: text/x-rst\n\nPublic description\n'
    with zipfile.ZipFile(out/wheel, 'w') as archive:
        archive.writestr('sphinx_traceability_view-1.1.0.dist-info/METADATA', metadata)
        archive.writestr('sphinx_traceability_view/_version.py', (package/'_version.py').read_bytes())
    with tarfile.open(out/sdist, 'w:gz') as archive:
        for name in ['PKG-INFO', 'PYPI.rst', 'pyproject.toml', 'src/sphinx_traceability_view/_version.py']:
            data = metadata if name == 'PKG-INFO' else (source/name).read_bytes()
            member = tarfile.TarInfo('sphinx_traceability_view-1.1.0/'+name);member.size=len(data)
            archive.addfile(member, BytesIO(data))
    checksums(out)
    return source, out


def checksums(out):
    (out/'SHA256SUMS').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n'
                                           for p in sorted(out.iterdir()) if p.name != 'SHA256SUMS'))


def test_qualified_assets_match_source_and_reject_tampering(tmp_path, monkeypatch):
    source, out = fixture(tmp_path, monkeypatch)
    assert len(release.validate_artifacts(out, 'v1.1.0')) == 2
    with pytest.raises(ValueError, match='tag must match'):
        release.validate_artifacts(out, 'v1.0.0')
    wheel = next(out.glob('*.whl'))
    wheel.write_bytes(wheel.read_bytes()+b'altered')
    with pytest.raises(ValueError, match='checksum mismatch'):
        release.validate_artifacts(out, 'v1.1.0')


def test_valid_checksums_do_not_accept_different_runtime_source(tmp_path, monkeypatch):
    source, out = fixture(tmp_path, monkeypatch)
    (source/'src/sphinx_traceability_view/_version.py').write_text('__version__ = "1.1.0"\n# changed code\n')
    with pytest.raises(ValueError, match='differs from tagged source'):
        release.validate_artifacts(out, 'v1.1.0')


def test_checksum_paths_and_duplicates_are_rejected(tmp_path, monkeypatch):
    source, out = fixture(tmp_path, monkeypatch)
    checks = out/'SHA256SUMS'
    original = checks.read_text()
    for text in [original+original, '0'*64+'  ../escape.whl\n']:
        checks.write_text(text)
        with pytest.raises(ValueError, match='checksum entry'):
            release.validate_artifacts(out, 'v1.1.0')
