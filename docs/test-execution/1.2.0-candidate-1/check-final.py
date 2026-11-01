"""Verify final evidence gates and unchanged tested inputs after metadata updates."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
result = json.loads((HERE/'results.json').read_text())
assert not any(result['outcomes'][state] for state in ('failed', 'error', 'skipped'))
assert all(item['returncode'] == 0 for item in result['attempts'] if item['suite'] != 'documentation')
assessment = json.loads((HERE/'verification-assessment.json').read_text())
changes = []
for name, expected in json.loads((HERE/'source-hashes.json').read_text()).items():
    data = (ROOT/name).read_bytes()
    if hashlib.sha256(data).hexdigest() == expected:
        continue
    assert name in assessment['unchanged_criteria_sha256'], name
    normalized = re.sub(r'(?m)^   :verification_state: [a-z_]+$', '   :verification_state: <assessed>', (ROOT/name).read_text())
    assert hashlib.sha256(normalized.encode()).hexdigest() == assessment['unchanged_criteria_sha256'][name], name
    changes.append(dict(path=name, change='verification metadata only', sha256=hashlib.sha256(data).hexdigest()))
record = dict(started=datetime.now(timezone.utc).isoformat(), passed=False, candidate=HERE.name, outcomes=result['outcomes'], source_identity=result['source_identity'], post_run_changes=changes, commands=[])
attempt = 1 + len(list(HERE.glob('final-validation-*.json')))
tools = 'tools/method/tooling/'
commands = [
    ('coverage', [sys.executable, 'scripts/check-coverage.py', '--strict']),
    ('method-package', [sys.executable, 'scripts/check-method-package.py']),
    ('documentation', [sys.executable, 'scripts/build_docs.py', 'docs']),
    ('traceability', [sys.executable, tools+'validate_traceability.py', 'docs/_build/html/needs.json', '--version', '1.2', '--repo-root', str(ROOT), '--require-test-coverage', '--csv', str(HERE/'final-traceability.csv'), '--test-csv', str(HERE/'final-test-traceability.csv')]),
    ('diagram-links', [sys.executable, tools+'normalize-diagram-links.py', '--diagram-dir', 'docs/architecture/diagrams', '--published-dir', 'docs/_build/html']),
    ('published-method', [sys.executable, 'scripts/check-method-package.py', '--published', 'docs/_build/html']),
    ('publication-inputs', [sys.executable, 'scripts/release.py', 'check', '--directory', str(HERE/'artifacts'), '--tag', 'v1.2.0']),
]
for name, command in commands:
    entry = dict(suite=name, command=command, started=datetime.now(timezone.utc).isoformat(), log=f'final-{attempt}-{name}.log')
    with (HERE/entry['log']).open('wb') as output:
        completed = subprocess.run(command, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT)
    entry.update(returncode=completed.returncode, finished=datetime.now(timezone.utc).isoformat())
    record['commands'].append(entry)
    record['finished'] = entry['finished']
    (HERE/f'final-validation-{attempt}.json').write_text(json.dumps(record, indent=2)+'\n')
    (HERE/'final-validation.json').write_text(json.dumps(record, indent=2)+'\n')
    print(name, completed.returncode, flush=True)
    if completed.returncode:
        sys.exit(completed.returncode)
record['passed'] = True
record['scope'] = 'Local qualification passed; awaiting owner release decision and successful hosted gates. No publication asserted.'
(HERE/f'final-validation-{attempt}.json').write_text(json.dumps(record, indent=2)+'\n')
(HERE/'final-validation.json').write_text(json.dumps(record, indent=2)+'\n')
print('Final local qualification gates passed', flush=True)
