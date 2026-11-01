"""Run named final-candidate gates, retaining every attempt separately."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
env = dict(os.environ, STV_GECKODRIVER=str(Path.home() / '.cache/selenium/geckodriver/win64/0.37.1/geckodriver.exe'))
tools = 'tools/method/tooling/'
commands = {
    'documentation': [sys.executable, 'scripts/build_docs.py', 'docs'],
    'coverage': [sys.executable, 'scripts/check-coverage.py', '--strict'],
    'traceability': [sys.executable, tools+'validate_traceability.py', 'docs/_build/html/needs.json', '--version', '1.2', '--repo-root', str(ROOT), '--require-test-coverage', '--csv', str(HERE/'final-traceability.csv'), '--test-csv', str(HERE/'final-test-traceability.csv')],
    'diagram-links': [sys.executable, tools+'normalize-diagram-links.py', '--diagram-dir', 'docs/architecture/diagrams', '--published-dir', 'docs/_build/html'],
    'published-method': [sys.executable, 'scripts/check-method-package.py', '--published', 'docs/_build/html'],
    'publication-inputs': [sys.executable, 'scripts/release.py', 'check', '--directory', str(HERE/'artifacts'), '--tag', 'v1.2.0'],
    'export-capacity': [sys.executable, str(HERE/'export-capacity.py')],
    'hover-export': [sys.executable, str(HERE/'check-hover-export.py')],
}
path = HERE/'supplemental-attempts.json'
attempts = json.loads(path.read_text()) if path.exists() else []
for name in sys.argv[1:]:
    number = 1 + sum(item['suite'] == name for item in attempts)
    entry = dict(suite=name, command=commands[name], cwd=str(ROOT), started=datetime.now(timezone.utc).isoformat(), log=f'supplement-{name}-{number}.log')
    with (HERE/entry['log']).open('wb') as output:
        result = subprocess.run(commands[name], cwd=ROOT, env=env, stdout=output, stderr=subprocess.STDOUT)
    entry.update(returncode=result.returncode, finished=datetime.now(timezone.utc).isoformat())
    attempts.append(entry)
    path.write_text(json.dumps(attempts, indent=2)+'\n')
    print(name, result.returncode, flush=True)
    if result.returncode:
        sys.exit(result.returncode)
