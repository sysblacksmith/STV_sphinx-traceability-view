"""Execute retained historical licensing and current minimum-runtime case evidence."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
started = datetime.now(timezone.utc).isoformat()
spec = importlib.util.spec_from_file_location('historical', ROOT/'scripts/historical-licenses.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
current = module.inventory()
retained = {i['sha256']: i for i in json.loads((ROOT/'docs/licensing/historical/artifacts.json').read_text())['artifacts']}
new_release = {hashlib.sha256(p.read_bytes()).hexdigest() for p in (RECORD/'artifacts').iterdir()}
historical = []
for item in current:
    if item['sha256'] in new_release:
        continue  # Exact current release artifacts are not historical distributions.
    assert item['sha256'] in retained, item['locations']
    assert item['elk_sha256'] == retained[item['sha256']]['elk_sha256']
    historical.append(item)
assert historical
for source, destination in [('LICENSE','LICENSE.txt'),
    ('src/sphinx_traceability_view/static/THIRD_PARTY_NOTICES.txt','THIRD_PARTY_NOTICES.txt'),
    ('src/sphinx_traceability_view/static/vendor/ELK-SOURCE.txt','ELK-SOURCE.txt'),
    ('frontend/legal/elk-inventory.json','ELK-INVENTORY.json')]:
    assert (ROOT/source).read_bytes() == (ROOT/'docs/licensing/historical'/destination).read_bytes()
result = dict(started=started, finished=datetime.now(timezone.utc).isoformat(), result='passed',
    historical=historical, excluded_current_release_hashes=sorted(new_release),
    policy='Preserve all original archive and Git bytes; compare available historical copies with the accepted frozen inventory and complete supplement.')
(RECORD/'historical-check.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(f'{len(historical)} distinct historical archives and complete supplement verified; current release excluded by exact digest.')
