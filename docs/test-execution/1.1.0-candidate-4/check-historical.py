from pathlib import Path
from datetime import datetime,timezone
import importlib.util,json,hashlib
root=Path.cwd();r=root/'docs/test-execution/1.1.0-candidate-4';started=datetime.now(timezone.utc).isoformat()
spec=importlib.util.spec_from_file_location('historical',root/'scripts/historical-licenses.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
current=h.inventory();known={i['sha256'] for i in json.loads((root/'docs/licensing/historical/artifacts.json').read_text())['artifacts']}
known.update(line.split()[0] for line in (root/'docs/test-execution/1.0.0-candidate-2/SHA256SUMS.txt').read_text().splitlines())
known.update(line.split()[0] for line in (root/'docs/test-execution/1.1.0-candidate-1/artifacts/SHA256SUMS').read_text().splitlines())
assert __import__('json').loads((root/'docs/test-execution/1.1.0-candidate-1/disposition.json').read_text())['state']=='rejected'
new={hashlib.sha256(p.read_bytes()).hexdigest() for p in (r/'artifacts').iterdir() if p.suffix in ['.whl','.gz']}
for i in current:assert i['sha256'] in known|new,i['locations']
for a,b in [('LICENSE','LICENSE.txt'),('src/sphinx_traceability_view/static/THIRD_PARTY_NOTICES.txt','THIRD_PARTY_NOTICES.txt'),('src/sphinx_traceability_view/static/vendor/ELK-SOURCE.txt','ELK-SOURCE.txt'),('frontend/legal/elk-inventory.json','ELK-INVENTORY.json')]:assert (root/a).read_bytes()==(root/'docs/licensing/historical'/b).read_bytes()
result=dict(started=started,finished=datetime.now(timezone.utc).isoformat(),result='passed',historical=current,current_candidate_hashes=sorted(new),basis='Existing frozen historical inventory, unchanged issued 1.0.0 SHA256SUMS and explicitly rejected candidate-1 checksums; fresh Git/archive inspection checks ELK fingerprints and complete supplements.')
(r/'historical-check.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(len(current),'archive identities and complete licensing supplements verified')

