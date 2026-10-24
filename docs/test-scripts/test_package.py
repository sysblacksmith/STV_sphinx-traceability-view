"""Verify the distributable in an isolated Python host, without Node on PATH."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
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
        for asset in ('stv.js','stv.css','THIRD_PARTY_NOTICES.txt','vendor/elk.bundled.js'):
            assert f'sphinx_traceability_view/static/{asset}' in names
        metadata=archive.read(next(name for name in names if name.endswith('.dist-info/METADATA'))).decode()
        assert not any('Requires-Dist: '+name in metadata for name in ('pytest','selenium','esbuild'))
    with tempfile.TemporaryDirectory(prefix='stv-wheel-') as directory:
        root=Path(directory);envpath=root/'env'
        assert root.resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
        subprocess.run([sys.executable,'-m','venv',str(envpath)],check=True,capture_output=True)
        python=envpath/'Scripts/python.exe'
        result=subprocess.run([str(python),'-m','pip','install','--no-index','--find-links',str(wheelhouse),str(wheel)],capture_output=True,text=True)
        assert result.returncode==0,result.stdout+result.stderr
        source=root/'source';shutil.copytree(ROOT/'docs/test-scripts/fixtures/minimal',source)
        env=dict(os.environ);env.pop('PYTHONPATH',None)
        env['PATH']=str(envpath/'Scripts')+os.pathsep+str(Path(os.environ['SystemRoot'])/'System32')
        result=subprocess.run([str(python),'-m','sphinx','-b','html','-W',str(source),str(root/'html')],env=env,cwd=root,capture_output=True,text=True)
        assert result.returncode==0,result.stdout+result.stderr
        assert 'STV_PENDING' not in (root/'html/index.html').read_text(encoding='utf-8')
        probe=subprocess.run([str(python),'-c','import sphinx_traceability_view as s;print(s.__file__)'],env=env,cwd=root,capture_output=True,text=True,check=True)
        assert str(envpath).lower() in probe.stdout.lower()
        retained=os.environ.get('STV_CONSUMER_RECORD')
        if retained:
            destination=Path(retained);destination.mkdir(parents=True,exist_ok=True)
            (destination/'build.log').write_text(result.stdout+result.stderr,encoding='utf-8')
            frozen=subprocess.run([str(python),'-m','pip','freeze'],capture_output=True,text=True,check=True)
            (destination/'environment.txt').write_text(frozen.stdout,encoding='utf-8')
            (destination/'identity.txt').write_text(probe.stdout+'\nPATH='+env['PATH']+'\n',encoding='utf-8')
