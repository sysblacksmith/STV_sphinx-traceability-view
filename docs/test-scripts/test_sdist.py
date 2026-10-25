"""Check the actual source archive boundary and a wheel rebuilt from that archive."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tarfile
import zipfile
from email.parser import BytesParser
import pytest

ROOT=Path(__file__).parents[2]


@pytest.mark.requirements('STV_SYS_009','STV_SWR_042','STV_SWR_046')
def test_sdist_excludes_local_evidence_and_rebuilds_wheel(tmp_path):
    source=tmp_path/'source';source.mkdir()
    for name in ('src','frontend'):
        shutil.copytree(ROOT/name,source/name,ignore=shutil.ignore_patterns('node_modules','__pycache__','*.pyc'))
    for name in ('pyproject.toml','hatch_build.py','README.rst','PYPI.rst','LICENSE','requirements-tooling.txt','requirements-docs.txt','conftest.py','.gitignore'):
        shutil.copyfile(ROOT/name,source/name)
    # The checked-in VCS negation and nested negation must not widen the tar.
    payloads=('docs/test-execution/private/probe.log','docs/_build/probe.log',
              '_security-audits/probe.txt','.venv/probe.txt','frontend/node_modules/probe.js',
              'src/sphinx_traceability_view/__pycache__/probe.pyc')
    for name in payloads:
        path=source/name;path.parent.mkdir(parents=True,exist_ok=True);path.write_text('STV_LOCAL_ONLY_SENTINEL')
    nested=source/'docs/test-execution/.gitignore';nested.write_text('!**/*.log\n')
    output=tmp_path/'dist'
    result=subprocess.run([sys.executable,'-m','build','--no-isolation','--outdir',str(output),str(source)],capture_output=True,text=True)
    assert result.returncode==0,result.stdout+result.stderr
    sdist=next(output.glob('*.tar.gz'))
    with tarfile.open(sdist,'r:gz') as archive:
        members={m.name.split('/',1)[1]:archive.extractfile(m).read() for m in archive.getmembers() if m.isfile()}
    assert not any(name in members for name in payloads)
    assert not any(n.startswith(('docs/test-execution/','docs/_build/','_security-audits/','.venv/','frontend/node_modules/')) for n in members)
    assert not any(b'STV_LOCAL_ONLY_SENTINEL' in data for data in members.values())
    for name in ('pyproject.toml','hatch_build.py','LICENSE','README.rst','PYPI.rst','requirements-tooling.txt',
                 'src/sphinx_traceability_view/_version.py','src/sphinx_traceability_view/static/stv.js',
                 'src/sphinx_traceability_view/static/vendor/ELK-INVENTORY.json',
                 'frontend/src/render/index.js','frontend/build.js','frontend/package.json','frontend/package-lock.json',
                 'frontend/legal/elk-inventory.json'):
        assert name in members,name
    # `build` above builds the wheel from the produced source archive, not the checkout.
    with zipfile.ZipFile(next(output.glob('*.whl'))) as wheel:
        metadata = BytesParser().parsebytes(wheel.read(next(n for n in wheel.namelist() if n.endswith('.dist-info/METADATA'))))
        assert metadata['Description-Content-Type'] == 'text/x-rst'
        assert metadata.get_payload().strip() == members['PYPI.rst'].decode('utf-8').strip()
        for name in ('stv.js','LICENSE.txt','THIRD_PARTY_NOTICES.txt','vendor/ELK-SOURCE.txt','vendor/ELK-INVENTORY.json'):
            path='sphinx_traceability_view/static/'+name
            assert wheel.read(path)==members['src/'+path]
    retained=os.environ.get('STV_SDIST_RECORD')
    if retained:
        import hashlib,json
        record=Path(retained);record.mkdir(parents=True,exist_ok=True)
        (record/'members.json').write_text(json.dumps(sorted(members),indent=2),encoding='utf-8')
        (record/'artifacts.json').write_text(json.dumps([{ 'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in output.iterdir()],indent=2),encoding='utf-8')
