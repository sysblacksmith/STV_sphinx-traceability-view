"""Verify retained archive fingerprints and the unchanged complete supplement."""
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
started = datetime.now(timezone.utc).isoformat()
spec = importlib.util.spec_from_file_location('historical', ROOT/'scripts/historical-licenses.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
inventory = module.inventory()
known = {item['sha256'] for item in json.loads((ROOT/'docs/licensing/historical/artifacts.json').read_text())['artifacts']}
cleanup = json.loads((ROOT/'docs/test-execution/build-cleanup-2026-10-26/preservation-manifest.json').read_text())
preserved = cleanup['preserved']
known.add(cleanup['archive_sha256'])
known.update(item['sha256'] for item in preserved if item['original'].endswith(('.whl', '.tar.gz')))
for path in (ROOT/'docs/test-execution').rglob('*SHA256SUMS*'):
    if path.is_file():
        for line in path.read_text().splitlines():
            digest = line.split()[0] if line.split() else ''
            if len(digest) == 64:
                known.add(digest)
for item in inventory:
    assert item['sha256'] in known, item['locations']
comparisons = []
for source, target in [('LICENSE','LICENSE.txt'), ('src/sphinx_traceability_view/static/THIRD_PARTY_NOTICES.txt','THIRD_PARTY_NOTICES.txt'), ('src/sphinx_traceability_view/static/vendor/ELK-SOURCE.txt','ELK-SOURCE.txt'), ('frontend/legal/elk-inventory.json','ELK-INVENTORY.json')]:
    current = (ROOT/source).read_bytes()
    retained = (ROOT/'docs/licensing/historical'/target).read_bytes()
    assert current.replace(b'\r\n', b'\n') == retained.replace(b'\r\n', b'\n'), target
    comparisons.append(dict(source=source, retained=target, identical_bytes=current==retained, identical_text=True, sha256=hashlib.sha256(current).hexdigest()))
(HERE/'historical-check.json').write_text(json.dumps(dict(started=started, finished=datetime.now(timezone.utc).isoformat(), result='passed', archives=inventory, supplement=comparisons, basis='Fresh Git and retained archive scan; audited ELK fingerprint; known retained checksums; complete supplement with only CRLF/LF normalization'), indent=2)+'\n')
print(len(inventory), 'archive identities and complete historical supplements verified')
