"""Run the final documentation/evidence gates and retain exact command receipts."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
SHARED = ROOT.parent/'-agents/skills/reverse-engineer-requirements'
SOURCE = Path(os.environ.get('STV_RELEASE_SOURCE_ROOT', ROOT)).resolve()
commands = []

def run(name, args):
    entry = dict(suite=name, command=list(map(str,args)), started=datetime.now(timezone.utc).isoformat())
    with (RECORD/(name+'.log')).open('w',encoding='utf-8') as stream:
        result = subprocess.run(entry['command'],cwd=ROOT,stdout=stream,stderr=subprocess.STDOUT)
    entry.update(returncode=result.returncode,finished=datetime.now(timezone.utc).isoformat())
    commands.append(entry)
    (RECORD/'final-validation.json').write_text(json.dumps(dict(passed=all(c['returncode']==0 for c in commands),commands=commands),indent=2),encoding='utf-8')
    print(name+': '+str(result.returncode),flush=True)
    assert result.returncode == 0, name

run('final-documentation',[sys.executable,SOURCE/'scripts/build_docs.py',SOURCE/'docs'])
run('final-traceability',[sys.executable,SHARED/'scripts/validate_traceability.py',
    SOURCE/'docs/_build/html/needs.json','--version','1.0','--repo-root',SOURCE,'--require-test-coverage',
    '--test-csv',RECORD/'final-test-traceability.csv','--csv',RECORD/'final-traceability.csv'])
run('final-diagram-links',[sys.executable,SHARED/'scripts/normalize-diagram-links.py',
    '--diagram-dir',SOURCE/'docs/architecture/diagrams','--published-dir',SOURCE/'docs/_build/html'])
run('final-diff-check',['git','diff','--check'])
manifest = json.loads((SOURCE/'docs/_build/html/_stv-publication.json').read_text())['files']
for name, info in manifest.items():
    data = (SOURCE/'docs/_build/html'/name).read_bytes()
    assert len(data)==info['bytes'] and hashlib.sha256(data).hexdigest()==info['sha256'], name
receipt=json.loads((RECORD/'final-validation.json').read_text())
receipt.update(publication_manifest_files=len(manifest),publication_manifest_verified=True,
    final_checked_at=datetime.now(timezone.utc).isoformat())
(RECORD/'final-validation.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
paths = []
for directory in ('src','frontend/src','scripts','docs'):
    for parent, directories, files in os.walk(SOURCE/directory):
        directories[:] = [d for d in directories if d not in {'__pycache__','node_modules','_build','test-execution'}]
        paths.extend(p for name in files if (p := Path(parent)/name).is_file() and not p.is_symlink())
(RECORD/'final-source-document-hashes.json').write_text(json.dumps({p.relative_to(SOURCE).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},indent=2),encoding='utf-8')
print(f'All final gates passed; {len(manifest)} publication files matched their size/hash manifest.')
