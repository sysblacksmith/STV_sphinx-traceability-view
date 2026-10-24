"""Development regression checks only; never invokes release qualification."""
from pathlib import Path
from datetime import datetime, timezone
import os,subprocess,sys,json,runpy,hashlib
ROOT=Path(__file__).resolve().parents[3]
record=Path(__file__).resolve().parent
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',STV_GECKODRIVER='C:/Users/fragg/.cache/selenium/geckodriver/win64/0.37.1/geckodriver.exe',REQUIREMENTS_SKILL_DIR=str(ROOT.parent/'-agents/skills/reverse-engineer-requirements'))
version=runpy.run_path(str(ROOT/'src/sphinx_traceability_view/_version.py'))['__version__']
out=ROOT/'docs/_build/maintenance-dist'
env['STV_WHEEL']=str(out/f'sphinx_traceability_view-{version}-py3-none-any.whl')
env['STV_CONSUMER_RECORD']=str(record/'consumer')
env['STV_PATH_RECORD']=str(record/'regression-paths')
env['STV_SCREENSHOTS']=str(record/'screenshots')
steps=[('development-package',[sys.executable,'-B','-m','build','--no-isolation','--outdir',str(out)]),('regression',[sys.executable,'-B','-m','pytest','-q','-p','no:cacheprovider','--ignore=docs/test-scripts/test_capacity.py','--junitxml='+str(record/'regression.xml'),'--requirement-map='+str(record/'test-map.json')]),('node-regression',['node','--test','--test-reporter=junit','frontend/src/*/tests/*.test.js'])]
entries=[]
for name,cmd in steps:
 start=datetime.now(timezone.utc).isoformat();print(name,flush=True)
 with (record/(name+'.log')).open('w',encoding='utf-8') as log:code=subprocess.run(cmd,cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT).returncode
 entries.append({'suite':name,'command':cmd,'started':start,'finished':datetime.now(timezone.utc).isoformat(),'returncode':code,'log':name+'.log'})
 (record/'commands.json').write_text(json.dumps(entries,indent=2),encoding='utf-8');print(name,code,flush=True)
 if name=='development-package' and code:break
raise SystemExit(int(any(x['returncode'] for x in entries)))
