"""Fresh offline Python 3.10 consumer of the exact final candidate wheel."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
host=ROOT/'docs/_build/release-runtime310'/HERE.name
python=host/'Scripts/python.exe'
commands=[('create-runtime310',[str(Path.home()/'AppData/Local/Programs/Python/Python310/python.exe'),'-m','venv',str(host)]),
 ('install-runtime310',[str(python),'-m','pip','install','--no-index','--find-links',str(ROOT/'docs/_build/wheelhouse'),'-r',str(ROOT/'requirements-tooling.txt'),str(HERE/'artifacts/sphinx_traceability_view-1.1.0-py3-none-any.whl')]),
 ('runtime310-host',[str(python),str(ROOT/'scripts/ci.py'),'runtime']),
 ('runtime310-clean-build',[str(python),'-m','sphinx','-W','-b','html',str(ROOT/'docs/test-scripts/fixtures/minimal'),str(host/'fresh-host')]),
 ('runtime310-version',[str(python),'-c','import sys;print(sys.version)'])]
attempts=[];env=dict(os.environ);env.pop('PYTHONPATH',None)
for suite,command in commands:
    start=datetime.now(timezone.utc).isoformat()
    with (HERE/(suite+'.log')).open('wb') as output:
        result=subprocess.run(command,cwd=ROOT,env=env,stdout=output,stderr=subprocess.STDOUT)
    attempts.append({'suite':suite,'command':command,'started':start,'finished':datetime.now(timezone.utc).isoformat(),'returncode':result.returncode,'log':suite+'.log'})
    (HERE/'supplement-commands.json').write_text(json.dumps(attempts,indent=2)+'\n',encoding='utf-8')
    print(suite,result.returncode,flush=True)
    if result.returncode:sys.exit(result.returncode)
