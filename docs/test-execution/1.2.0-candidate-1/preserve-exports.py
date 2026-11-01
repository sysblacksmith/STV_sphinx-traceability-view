"""Compress task-created raw SVG evidence with verified hashes before teardown."""
import hashlib
import json
from pathlib import Path
import zipfile

HERE = Path(__file__).resolve().parent
paths = sorted((HERE/'export-capacity').glob('*.svg')) + sorted(HERE.glob('hover-export-*.svg'))
assert len(paths) == 6
target = HERE/'retained-exports.zip'
assert not target.exists()
manifest = []
with zipfile.ZipFile(target, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
    for path in paths:
        assert path.resolve().is_relative_to(HERE)
        data = path.read_bytes()
        name = path.relative_to(HERE).as_posix()
        archive.writestr(name, data)
        manifest.append(dict(original='docs/test-execution/'+HERE.name+'/'+name, member=name, bytes=len(data), sha256=hashlib.sha256(data).hexdigest()))
with zipfile.ZipFile(target) as archive:
    for item in manifest:
        assert hashlib.sha256(archive.read(item['member'])).hexdigest() == item['sha256']
record = dict(archive=target.name, archive_sha256=hashlib.sha256(target.read_bytes()).hexdigest(), archive_bytes=target.stat().st_size, files=manifest, purpose='Exact raw SVG observations retained with lossless compression; original paths in issued supplemental metrics remain provenance')
(HERE/'export-preservation.json').write_text(json.dumps(record, indent=2)+'\n')
for path in paths:
    path.unlink()  # Only this task's verified, newly created duplicate raw outputs.
print(json.dumps(record, indent=2))
