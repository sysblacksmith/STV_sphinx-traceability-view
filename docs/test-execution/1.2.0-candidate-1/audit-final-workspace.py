"""Check the final published evidence, artifacts and retained environments."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
assessment = json.loads((HERE/'verification-assessment.json').read_text())
for name, expected in json.loads((HERE/'source-hashes.json').read_text()).items():
    path = ROOT/name
    if hashlib.sha256(path.read_bytes()).hexdigest() == expected:
        continue
    assert name in assessment['unchanged_criteria_sha256'], name
    text = re.sub(r'(?m)^   :verification_state: [a-z_]+$', '   :verification_state: <assessed>', path.read_text())
    assert hashlib.sha256(text.encode()).hexdigest() == assessment['unchanged_criteria_sha256'][name], name
html = ROOT/'docs/_build/html'
text = BeautifulSoup((html/'index.html').read_text(encoding='utf-8'), 'html.parser').get_text(' ', strip=True)
assert 'STV version: 1.2.0' in text
for page, filename, field, expected in [('qualification.html', 'final-validation.json', 'passed', True), ('cleanup-review.html', 'cleanup-receipt.json', 'removed_bytes', 594419602)]:
    path = html/'test-execution'/HERE.name/page
    document = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    assert 'retained in the engineering checkout' in document.get_text()
    assert not any(link['href'].endswith('/'+filename) for link in document.select('a[href]'))
    retained = json.loads((HERE/filename).read_text())
    assert retained[field] == expected, filename
for path in (HERE/'artifacts').glob('*'):
    if path.name == 'SHA256SUMS':
        continue
    assert path.read_bytes() == (ROOT/'dist'/path.name).read_bytes()
assert sorted(path.name for path in (ROOT/'docs/_build').iterdir()) == ['html']
pip_checks = []
for directory in ('.venv', '.venv-implementation'):
    completed = subprocess.run([str(ROOT/directory/'Scripts/python.exe'), '-m', 'pip', 'check'], capture_output=True, text=True)
    assert completed.returncode == 0, completed.stdout+completed.stderr
    pip_checks.append(dict(environment=directory, returncode=completed.returncode, output=completed.stdout.strip()))
attempts = json.loads((HERE/'supplemental-attempts.json').read_text())
assert all(next(item for item in reversed(attempts) if item['suite'] == name)['returncode'] == 0 for name in ('documentation', 'traceability', 'diagram-links', 'published-method', 'publication-inputs'))
record = dict(recorded_at=datetime.now(timezone.utc).isoformat(), passed=True, source_stability='All candidate source/build/test inputs unchanged except assessed verification metadata; criterion hashes match', evidence_publication='Public summaries retain checkout-only evidence notices; successful local gate/receipt records verified', audit_harness_corrections='Initial audit assumed a generic Project version label and public raw downloads; corrected to the actual STV version label and established checkout-only evidence publication policy, without product changes', remaining_build_entries=['html'], pip_checks=pip_checks, disposition='Local qualification complete; awaiting owner release decision and hosted gates; no commit/tag/publication performed')
(HERE/'final-workspace-audit.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
