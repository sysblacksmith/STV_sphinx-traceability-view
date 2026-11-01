"""Execute only the owner's reviewed path list after qualification finishes."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
assert json.loads((HERE/'final-validation.json').read_text())['passed']
assert json.loads((HERE/'results.json').read_text())['finished']
inventory = json.loads((HERE/'workspace-inventory.json').read_text())
targets = inventory['proposed']
for item in targets:
    path = ROOT/item['path']
    assert path.resolve().is_relative_to(ROOT) and path.resolve() != ROOT
    assert not path.is_symlink()
    assert path != ROOT/'docs/_build/html'
    assert path.is_relative_to(ROOT/'docs/_build') or path.name in ('__pycache__', '.pytest_cache')
preserved = []
for source_name, destination_name in [
    ('docs/_build/test-map.json', 'executable-test-map.json'),
    ('docs/_build/release-benchmark/1.2.0-candidate-1/metrics.json', 'capacity-build.json'),
    ('docs/_build/release-benchmark/1.2.0-candidate-1/build.log', 'capacity-host.log'),
]:
    source, destination = ROOT/source_name, HERE/destination_name
    if destination.exists():
        assert source.read_bytes() == destination.read_bytes()
    else:
        shutil.copyfile(source, destination)
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    assert digest == hashlib.sha256(destination.read_bytes()).hexdigest()
    preserved.append(dict(original=source_name, retained=destination.relative_to(ROOT).as_posix(), sha256=digest))
runtime = ROOT/'docs/_build/release-runtime310/1.2.0-candidate-1-retry/Scripts/python.exe'
(HERE/'runtime310-environment.txt').write_bytes(subprocess.check_output([str(runtime), '-m', 'pip', 'freeze']))
wheel_hashes = {path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in (ROOT/'docs/_build/wheelhouse').glob('*.whl')}
(HERE/'supplement-runtime-wheel-hashes.json').write_text(json.dumps(wheel_hashes, indent=2)+'\n')
def snapshot(directory):
    return {path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in directory.rglob('*') if path.is_file() and '__pycache__' not in path.parts}
html_before = snapshot(ROOT/'docs/_build/html')
dist_before = snapshot(ROOT/'dist')
evidence_before = snapshot(HERE)
record = dict(started=datetime.now(timezone.utc).isoformat(), authorization='Owner approved the explicit cleanup-review.rst / workspace-inventory.json list on 2026-11-01, after tests finish', preserved=preserved, removed=[], failed=[], retained=['docs/_build/html', 'all dist files', 'all canonical evidence', 'source and tests', 'normal development environments and frontend dependencies'])
for item in targets:
    path = ROOT/item['path']
    if not path.exists():
        continue
    size = path.stat().st_size if path.is_file() else sum(child.stat().st_size for child in path.rglob('*') if child.is_file())
    try:
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
        record['removed'].append(dict(path=item['path'], bytes=size))
    except OSError as error:
        record['failed'].append(dict(path=item['path'], error=str(error)))
assert html_before == snapshot(ROOT/'docs/_build/html')
assert dist_before == snapshot(ROOT/'dist')
assert evidence_before == snapshot(HERE)
record.update(finished=datetime.now(timezone.utc).isoformat(), removed_bytes=sum(item['bytes'] for item in record['removed']), current_html_files_verified=len(html_before), distribution_files_verified=len(dist_before), canonical_evidence_files_verified=len(evidence_before), remaining_build_entries=sorted(path.name for path in (ROOT/'docs/_build').iterdir()), git_status=subprocess.check_output(['git', 'status', '--short', '--ignored'], cwd=ROOT, text=True))
(HERE/'cleanup-receipt.json').write_text(json.dumps(record, indent=2)+'\n')
page = HERE/'cleanup-review.rst'
text = page.read_text().replace('Nothing was deleted.', 'No pre-existing output had been deleted when this proposal was issued.').replace('Nothing has been deleted.', 'No approved cleanup had been performed when this proposal was issued.')
text += '\nCleanup execution\n-----------------\n\n'
text += f"The owner approved this exact list after testing on 2026-11-01. Removed **{record['removed_bytes']/1048576:.2f} MiB** from {len(record['removed'])} listed paths. "
text += f"There were {len(record['failed'])} failed removals. The current {len(html_before)} HTML files, {len(dist_before)} distribution files and {len(evidence_before)} canonical evidence files were verified unchanged by SHA-256. "
text += 'Only current HTML remains under ``docs/_build``. Task-created raw SVG duplicates were separately retained in a verified lossless archive. The normal development environments remain usable; future capacity/offline tests must regenerate the host and reprovision the wheelhouse.\n\n'
text += '* :download:`Cleanup receipt, preservation hashes and final inventory <cleanup-receipt.json>`\n'
text += '* :download:`Minimum-runtime dependency versions <runtime310-environment.txt>`\n'
text += '* :download:`Supplemental runtime wheel hashes <supplement-runtime-wheel-hashes.json>`\n'
page.write_text(text)
assert not record['failed'], record['failed']
print(json.dumps({key:record[key] for key in ('removed_bytes', 'current_html_files_verified', 'distribution_files_verified', 'remaining_build_entries')}, indent=2))
