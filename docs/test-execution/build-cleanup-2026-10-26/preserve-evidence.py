"""Preserve unique evidence before owner-authorized build-output removal.

Copies only; deletion is performed separately with validated PowerShell paths.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import zipfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BUILD=ROOT/'docs/_build'
assert BUILD.resolve()==BUILD and (BUILD/'html').is_dir()
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

known={}
for parent in [ROOT/'docs/test-execution',ROOT/'dist']:
    for path in parent.rglob('*'):
        if path.is_file() and not path.is_symlink() and not path.is_relative_to(HERE):
            known.setdefault(sha(path),path.relative_to(ROOT).as_posix())
html={p.relative_to(BUILD/'html').as_posix():sha(p) for p in (BUILD/'html').rglob('*') if p.is_file()}
entries=[];excluded=[];selected=[];source_bytes=0
for parent,dirs,names in os.walk(BUILD,followlinks=False):
    current=Path(parent);relative=current.relative_to(BUILD)
    if current==BUILD/'html':dirs[:]=[];continue
    if current.name in {'.git','node_modules','__pycache__','wheelhouse','browser-tools','ci-tools'} or 'pyvenv.cfg' in names or current==BUILD/'pr3-clean-checkout':
        excluded.append({'path':current.relative_to(ROOT).as_posix(),'reason':'Recreatable environment, dependency/tool cache, or clean checkout'});dirs[:]=[];continue
    if '_static' in dirs and ('index.html' in names or 'objects.inv' in names):
        excluded.append({'path':current.relative_to(ROOT).as_posix(),'reason':'Generated HTML host; inputs/generators are retained'});dirs[:]=[];continue
    for name in names:
        path=current/name
        if path.is_symlink():raise RuntimeError('Review redirected file before cleanup: '+str(path))
        if name in {'native-session-finished'}:continue
        own_distribution=name.startswith(('sphinx_traceability_view-','sphinx-traceability-view-')) and name.endswith(('.whl','.tar.gz'))
        if not own_distribution and path.suffix.lower() in {'.pyc','.pyo','.exe','.dll','.pyd','.jar'}:continue
        digest=sha(path);row={'original':path.relative_to(ROOT).as_posix(),'bytes':path.stat().st_size,'sha256':digest}
        source_bytes+=row['bytes']
        if digest in known:row['retained']=known[digest]
        elif own_distribution:
            destination=ROOT/'dist/retained-build-artifacts'/digest[:16]/name
            destination.parent.mkdir(parents=True,exist_ok=True)
            if destination.exists():assert sha(destination)==digest
            else:shutil.copyfile(path,destination)
            assert sha(destination)==digest
            row['retained']=destination.relative_to(ROOT).as_posix();known[digest]=row['retained']
        else:
            member=path.relative_to(BUILD).as_posix()
            selected.append((path,member,digest))
            row['retained']='retained-evidence.zip::'+member;known[digest]=row['retained']
        entries.append(row)
archive=HERE/'retained-evidence.zip'
assert not archive.exists(),'Do not replace an existing preservation archive'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as output:
    for path,member,digest in selected:
        assert sha(path)==digest;output.write(path,member)
with zipfile.ZipFile(archive) as saved:
    assert saved.testzip() is None
    for path,member,digest in selected:assert hashlib.sha256(saved.read(member)).hexdigest()==digest
manifest={'recorded_at':datetime.now(timezone.utc).isoformat(),'authorization':'Owner requested removing everything under docs/_build except current HTML after preserving unique evidence.',
          'preserved':entries,'excluded_generated_roots':excluded,'html_sha256':html,'archive_sha256':sha(archive),'archive_bytes':archive.stat().st_size,
          'rebuild':'Use the maintained build/release runners; recreate temporary environments and download pinned dependencies as needed. Old fixture-reuse paths are historical provenance, not live dependencies.'}
(HERE/'preservation-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'evidence_files_accounted_for':len(entries),'unique_archive_members':len(selected),'archive_mib':round(archive.stat().st_size/1024**2,2),'current_html_files':len(html)},indent=2))
