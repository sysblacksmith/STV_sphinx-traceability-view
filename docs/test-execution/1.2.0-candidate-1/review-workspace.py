"""Inventory generated output; no deletion or inferred cleanup permission."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
items = []
for path in sorted((ROOT/'docs/_build').iterdir()):
    if path.name == 'html':
        continue
    files = [path] if path.is_file() else [item for item in path.rglob('*') if item.is_file()]
    items.append(dict(path=path.relative_to(ROOT).as_posix(), bytes=sum(item.stat().st_size for item in files), files=len(files), reason='Reproducible release working output; canonical reports and distributions retained separately', consequence='Recreate capacity host, offline wheelhouse or temporary consumer as needed'))
for directory in ('src', 'docs/test-scripts', 'scripts', 'tools/method/tooling'):
    for path in sorted((ROOT/directory).rglob('__pycache__')):
        items.append(dict(path=path.relative_to(ROOT).as_posix(), bytes=sum(item.stat().st_size for item in path.rglob('*') if item.is_file()), reason='Regenerated Python bytecode cache', consequence='Python recreates it on next import'))
for path in (ROOT/'.pytest_cache', ROOT/'__pycache__', ROOT/'docs/__pycache__', HERE/'__pycache__'):
    if path.exists():
        items.append(dict(path=path.relative_to(ROOT).as_posix(), bytes=sum(item.stat().st_size for item in path.rglob('*') if item.is_file()), reason='Regenerated test/Python cache', consequence='Recreated by subsequent tests/imports'))
for config in (ROOT/'.venv/pyvenv.cfg', ROOT/'.venv-implementation/pyvenv.cfg'):
    assert 'docs\\_build' not in config.read_text() and 'docs/_build' not in config.read_text(), config
record = dict(recorded_at=datetime.now(timezone.utc).isoformat(), proposed=items, total_bytes=sum(item['bytes'] for item in items), retained=['docs/_build/html', 'dist (all current and historical distributions)', 'docs/test-execution (all evidence)', '.venv', '.venv-implementation', 'frontend/node_modules', 'next_steps.rst', 'original problem attachments', '_security-audits'], deleted=[], runtime_dependencies='Both development environment base interpreters remain outside _build', git_status=subprocess.check_output(['git', 'status', '--short', '--ignored'], cwd=ROOT, text=True))
(HERE/'workspace-inventory.json').write_text(json.dumps(record, indent=2)+'\n')
title = 'Workspace cleanup review'
lines = [title, '='*len(title), '', 'Nothing has been deleted. This is a concrete optional cleanup proposal after', 'all active qualification consumers finish. Post-release review remains due', 'when publication completes. All distributions, evidence and normal development', 'environments/dependencies are retained. Both Python environments use a base', 'interpreter outside disposable build output.', '', '.. list-table:: Reproducible output eligible for cleanup', '   :header-rows: 1', '', '   * - Project-relative path', '     - MiB', '     - Rebuild consequence']
for item in items:
    lines += ['   * - ``'+item['path']+'``', f"     - {item['bytes']/1048576:.2f}", '     - '+item['consequence']]
lines += ['', f"Total proposed space: **{record['total_bytes']/1048576:.2f} MiB**.", '', 'Retained: current HTML, all of ``dist/``, canonical execution records,', 'source/test inputs, original problem attachments, ``next_steps.rst``, security', 'audit records, normal virtual environments and frontend dependencies.', '', '* :download:`Full inventory and Git status <workspace-inventory.json>`', '']
(HERE/'cleanup-review.rst').write_text('\n'.join(lines))
print(json.dumps(dict(total_bytes=record['total_bytes'], paths=len(items)), indent=2))
