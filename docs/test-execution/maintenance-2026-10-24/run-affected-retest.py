from pathlib import Path
from datetime import datetime,timezone
import json,os,subprocess,sys
root=Path.cwd();r=root/'docs/test-execution/maintenance-2026-10-24';env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',STV_GECKODRIVER='C:/Users/fragg/.cache/selenium/geckodriver/win64/0.37.1/geckodriver.exe',STV_WHEEL=str(root/'docs/_build/maintenance-dist-2/sphinx_traceability_view-1.0.0.dev0-py3-none-any.whl'),STV_CONSUMER_RECORD=str(r/'consumer-final'),STV_PATH_RECORD=str(r/'paths-final'))
steps=[('development-package-2',[sys.executable,'-B','-m','build','--no-isolation','--outdir','docs/_build/maintenance-dist-2']),('affected-retest',[sys.executable,'-B','-m','pytest','-q','-p','no:cacheprovider','src/sphinx_traceability_view/directive/tests','docs/test-scripts/test_package.py','docs/test-scripts/test_windows_paths.py','docs/test-scripts/test_legal_guard.py','--junitxml='+str(r/'affected-retest.xml')])]
entries=json.loads((r/'commands.json').read_text())
for name,cmd in steps:
 start=datetime.now(timezone.utc).isoformat();print(name,flush=True)
 with (r/(name+'.log')).open('w',encoding='utf-8') as log:code=subprocess.run(cmd,env=env,stdout=log,stderr=subprocess.STDOUT).returncode
 entries.append(dict(suite=name,command=cmd,started=start,finished=datetime.now(timezone.utc).isoformat(),returncode=code,log=name+'.log'));(r/'commands.json').write_text(json.dumps(entries,indent=2));print(name,code,flush=True)
 if code:raise SystemExit(code)
