"""Exercise the Python 3.10 runtime independently of newer maintainer tooling."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

root=Path(__file__).resolve().parents[3]
record=Path(__file__).resolve().parent
parser=argparse.ArgumentParser();parser.add_argument('--python310',required=True);args=parser.parse_args()
envpath=root/'docs/_build/runtime310-prsa003'
subprocess.run([args.python310,'-m','venv',str(envpath)],check=True)
python=envpath/'Scripts/python.exe'
wheel=root/'docs/_build/prsa003-dist/sphinx_traceability_view-1.0.0.dev0-py3-none-any.whl'
wheelhouse=root/'docs/_build/wheelhouse'
commands=[[str(python),'-m','pip','install','--no-index','--find-links',str(wheelhouse),'-r',str(root/'requirements-tooling.txt')],
          [str(python),'-m','pip','install','--no-index','--find-links',str(wheelhouse),str(wheel)],
          [str(python),'-m','pip','check']]
source=root/'docs/_build/runtime310-source';shutil.copytree(root/'docs/test-scripts/fixtures/minimal',source,dirs_exist_ok=True)
env=dict(os.environ);env.pop('PYTHONPATH',None);env['PATH']=str(envpath/'Scripts')+os.pathsep+str(Path(os.environ['SystemRoot'])/'System32')
commands += [[str(python),'-m','sphinx','-W','-b','html',str(source),str(root/'docs/_build/runtime310-html')],
             [str(python),'-c','import sys,importlib.metadata as m,sphinx_traceability_view as s; assert sys.version_info[:2]==(3,10); assert m.version("certifi")=="2026.10.23"; assert m.version("pip")=="26.2.2"; assert m.version("setuptools")=="84.2.1"; print(sys.version);print(s.__file__);print(s.__version__);print("certifi",m.version("certifi"))']]
results=[]
for command in commands:
    result=subprocess.run(command,cwd=envpath,env=env,text=True,capture_output=True)
    results.append({'command':command,'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    (record/'runtime310.json').write_text(json.dumps({'wheel_sha256':hashlib.sha256(wheel.read_bytes()).hexdigest(),'checks':results},indent=2),encoding='utf-8')
    assert result.returncode==0,result.stdout+result.stderr
assert (root/'docs/_build/runtime310-html/_static/stv/vendor/ELK-INVENTORY.json').is_file()
assert str(envpath).lower() in results[-1]['stdout'].lower()
print('Python 3.10 offline bootstrap, dependency check, installed extension identity and Sphinx host: passed.')
