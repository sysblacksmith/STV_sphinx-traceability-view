"""Retain final local gates after evidence/verification metadata consolidation."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
result=json.loads((HERE/'results.json').read_text(encoding='utf-8'))
assert result['outcomes']=={'passed':229,'failed':0,'error':0,'skipped':0}
assert all(a['returncode']==0 for a in result['attempts'] if a['suite']!='documentation')
sources=json.loads((HERE/'source-hashes.json').read_text(encoding='utf-8'))
changes=[]
allowed={'docs/requirements-stakeholder.rst','docs/requirements-system.rst','docs/requirements-software.rst'}
for name,expected in sources.items():
    current=(ROOT/name).read_bytes()
    if hashlib.sha256(current).hexdigest()==expected:continue
    assert name in allowed,'Unexpected tested-input change: '+name
    before=subprocess.check_output(['git','show',result['revision']+':'+name],cwd=ROOT).replace(b'\r\n',b'\n')
    strip=lambda data:re.sub(rb':verification_state: [a-z_]+',b':verification_state: <assessed>',data.replace(b'\r\n',b'\n'))
    assert strip(before)==strip(current),'Requirement criteria changed after qualification: '+name
    changes.append({'path':name,'change':'verification_state metadata only','sha256':hashlib.sha256(current).hexdigest()})
counter=len(list(HERE.glob('final-commands-*.json')))+1
record={'scope':'Local release qualification; successful hosted checks remain required before merge/publication',
        'passed':False,'started':datetime.now(timezone.utc).isoformat(),'test_revision':result['revision'],
        'outcomes':result['outcomes'],'post_run_source_changes':changes,'commands':[],
        'artifact_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (HERE/'artifacts').iterdir() if p.suffix in ['.whl','.gz']}}
tools='tools/method/tooling/'
commands=[('coverage',[sys.executable,'scripts/check-coverage.py','--strict']),
 ('method-package',[sys.executable,'scripts/check-method-package.py']),
 ('documentation',[sys.executable,'scripts/build_docs.py','docs']),
 ('traceability',[sys.executable,tools+'validate_traceability.py','docs/_build/html/needs.json','--version','1.1','--repo-root',str(ROOT),'--require-test-coverage','--csv',str(HERE/'final-traceability.csv'),'--test-csv',str(HERE/'final-test-traceability.csv')]),
 ('diagram-links',[sys.executable,tools+'normalize-diagram-links.py','--diagram-dir','docs/architecture/diagrams','--published-dir','docs/_build/html']),
 ('published-method',[sys.executable,'scripts/check-method-package.py','--published','docs/_build/html']),
 ('exact-publication-inputs',[sys.executable,'-c',"import runpy; from pathlib import Path; runpy.run_path('scripts/release.py')['validate_artifacts'](Path('docs/test-execution/1.1.0-candidate-4/artifacts'),'v1.1.0')"])]
for name,command in commands:
    entry={'suite':name,'command':command,'started':datetime.now(timezone.utc).isoformat(),'log':f'final-{counter}-{name}.log'}
    with (HERE/entry['log']).open('wb') as output:
        run=subprocess.run(command,cwd=ROOT,stdout=output,stderr=subprocess.STDOUT)
    entry.update(returncode=run.returncode,finished=datetime.now(timezone.utc).isoformat());record['commands'].append(entry)
    record['finished']=entry['finished']
    (HERE/f'final-commands-{counter}.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    (HERE/'final-validation.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(name,run.returncode,flush=True)
    if run.returncode:sys.exit(run.returncode)
record['passed']=True
record['resolved_original_documentation_failure']='Missing evidence toctree entries corrected; see final documentation command and retained original log'
(HERE/f'final-commands-{counter}.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
(HERE/'final-validation.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'outcomes':result['outcomes'],'post_run_source_changes':changes},indent=2))
