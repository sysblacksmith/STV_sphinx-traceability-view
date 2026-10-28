"""Verify the distributable in an isolated Python host, without Node on PATH."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
import tarfile
import json
import hashlib
from email.parser import Parser
import pytest

ROOT=Path(__file__).parents[2]


@pytest.mark.requirements('STV_SYS_009','STV_SWR_042','STV_SWR_046')
def test_clean_wheel_host():
    wheels=[Path(os.environ['STV_WHEEL'])] if os.environ.get('STV_WHEEL') else sorted((ROOT/'dist').glob('*.whl'))
    assert wheels,'Build the wheel before packaging verification'
    wheel=wheels[-1]
    wheelhouse=ROOT/'docs/_build/wheelhouse'
    assert wheelhouse.is_dir(),'Provision the runtime wheelhouse before offline packaging verification'
    with zipfile.ZipFile(wheel) as archive:
        names=archive.namelist()
        assert not any("/tests/" in name for name in names), "Unit tests must not ship in the runtime wheel"
        for asset in ('stv.js','stv.css','LICENSE.txt','THIRD_PARTY_NOTICES.txt','vendor/elk.bundled.js','vendor/ELK-SOURCE.txt','vendor/ELK-INVENTORY.json'):
            assert f'sphinx_traceability_view/static/{asset}' in names
        packaged_inventory=json.loads(archive.read('sphinx_traceability_view/static/vendor/ELK-INVENTORY.json'))
        assert hashlib.sha256(archive.read('sphinx_traceability_view/static/vendor/elk.bundled.js')).hexdigest()==packaged_inventory['elkjs']['sha256']
        metadata=archive.read(next(name for name in names if name.endswith('.dist-info/METADATA'))).decode()
        parsed_metadata = Parser().parsestr(metadata)
        description = (ROOT / 'PYPI.rst').read_text(encoding='utf-8')
        assert parsed_metadata['Description-Content-Type'] == 'text/x-rst'
        assert parsed_metadata.get_payload().strip() == description.strip()
        assert set(parsed_metadata.get_all('Project-URL')) == {
            'Documentation, https://sysblacksmith.github.io/STV_sphinx-traceability-view/',
            'Source, https://github.com/sysblacksmith/STV_sphinx-traceability-view',
            'Issues, https://github.com/sysblacksmith/STV_sphinx-traceability-view/issues',
        }
        assert not any('Requires-Dist: '+name in metadata for name in ('pytest','selenium','esbuild'))
        assert 'License-Expression: MIT AND ISC AND BSD-3-Clause AND Apache-2.0 AND EPL-1.0 AND EPL-2.0' in metadata
        assert 'Copyright (c) 2026 Henning Heikes' in archive.read('sphinx_traceability_view/static/LICENSE.txt').decode()
        license_members=[name for name in names if '.dist-info/licenses/' in name]
        assert any(name.endswith('/LICENSE') for name in license_members)
        assert any(name.endswith('/THIRD_PARTY_NOTICES.txt') for name in license_members)
        assert any(name.endswith('/ELK-SOURCE.txt') for name in license_members)
    source_archive=wheel.parent/(wheel.name.split('-py3-')[0]+'.tar.gz')
    with tarfile.open(source_archive,'r:gz') as archive:
        names=archive.getnames()
        assert any(name.endswith('/LICENSE') for name in names)
        readme = next(name for name in names if name.endswith('/PYPI.rst'))
        assert archive.extractfile(readme).read().decode('utf-8').strip() == description.strip()
        package_info = Parser().parsestr(archive.extractfile(next(name for name in names if name.endswith('/PKG-INFO'))).read().decode('utf-8'))
        assert package_info['Description-Content-Type'] == 'text/x-rst'
        assert package_info.get_payload().strip() == description.strip()
        assert any(name.endswith('/static/THIRD_PARTY_NOTICES.txt') for name in names)
        assert any(name.endswith('/static/vendor/ELK-SOURCE.txt') for name in names)

    with tempfile.TemporaryDirectory(prefix='stv-wheel-') as directory:
        root=Path(directory);envpath=root/'env'
        assert root.resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
        subprocess.run([sys.executable,'-m','venv',str(envpath)],check=True,capture_output=True)
        python=envpath/('Scripts/python.exe' if os.name=='nt' else 'bin/python')
        bootstrap=subprocess.run([str(python),'-m','pip','install','--no-index','--find-links',str(wheelhouse),'-r',str(ROOT/'requirements-tooling.txt')],capture_output=True,text=True)
        assert bootstrap.returncode==0,bootstrap.stdout+bootstrap.stderr
        result=subprocess.run([str(python),'-m','pip','install','--no-index','--find-links',str(wheelhouse),str(wheel)],capture_output=True,text=True)
        assert result.returncode==0,result.stdout+result.stderr
        source=root/'source';shutil.copytree(ROOT/'docs/test-scripts/fixtures/minimal',source)
        env=dict(os.environ);env.pop('PYTHONPATH',None)
        env['PATH']=str(python.parent)+(os.pathsep+str(Path(os.environ['SystemRoot'])/'System32') if os.name=='nt' else '')
        result=subprocess.run([str(python),'-m','sphinx','-b','html','-W',str(source),str(root/'html')],env=env,cwd=root,capture_output=True,text=True)
        assert result.returncode==0,result.stdout+result.stderr
        assert 'STV_PENDING' not in (root/'html/index.html').read_text(encoding='utf-8')
        static=root/'html/_static/stv'
        assert (static/'LICENSE.txt').read_bytes()==(ROOT/'LICENSE').read_bytes()
        assert 'https://github.com/kieler/elkjs/tree/0.10.0' in (static/'vendor/ELK-SOURCE.txt').read_text(encoding='utf-8')
        notices=(static/'THIRD_PARTY_NOTICES.txt').read_text(encoding='utf-8')
        assert 'Eclipse Public License' in notices
        assert 'Apache License' in notices
        assert 'EMF-GWT common/ecore' in notices
        inventory=json.loads((static/'vendor/ELK-INVENTORY.json').read_text())
        assert inventory==packaged_inventory
        assert {x['license'] for x in inventory['compiled_dependencies']} >= {'Apache-2.0','EPL-1.0','EPL-2.0','MIT'}
        assert 'https://github.com/eclipse-elk/elk/tree/v0.10.0' in notices

        probe=subprocess.run([str(python),'-c','import sphinx_traceability_view as s;from importlib.metadata import version;assert s.__version__==version("sphinx-traceability-view");print(s.__file__);print(s.__version__)'],env=env,cwd=root,capture_output=True,text=True,check=True)
        assert str(envpath).lower() in probe.stdout.lower()
        retained=os.environ.get('STV_CONSUMER_RECORD')
        if retained:
            destination=Path(retained);destination.mkdir(parents=True,exist_ok=True)
            (destination/'build.log').write_text(result.stdout+result.stderr,encoding='utf-8')
            frozen=subprocess.run([str(python),'-m','pip','freeze'],capture_output=True,text=True,check=True)
            (destination/'environment.txt').write_text(frozen.stdout,encoding='utf-8')
            (destination/'identity.txt').write_text(probe.stdout+'\nPATH='+env['PATH']+'\n',encoding='utf-8')
