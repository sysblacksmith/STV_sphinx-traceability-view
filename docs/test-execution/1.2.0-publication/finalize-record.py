"""Preserve publication evidence and tear down only this task's staging data."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT=Path.cwd()
STAGE=ROOT/'docs/_build/release-publication'
RECORD=ROOT/'docs/test-execution/1.2.0-publication'
receipt=json.loads((RECORD/'publication-verification.json').read_text())
assert receipt['workflow_conclusion']=='success' and receipt['pypi_hashes_match']
preserved=[]
paths=sorted(path for path in STAGE.iterdir() if path.is_file())+[ROOT/'docs/_build/release-1.2.0-publication.json']
for source in paths:
    target=RECORD/('github-release.json' if source.name=='release-1.2.0-publication.json' else 'release-notes.md.txt' if source.name=='release-notes.md' else source.name)
    assert not target.exists(),target
    shutil.copyfile(source,target)
    digest=hashlib.sha256(source.read_bytes()).hexdigest()
    assert digest==hashlib.sha256(target.read_bytes()).hexdigest()
    preserved.append(dict(original=source.relative_to(ROOT).as_posix(),retained=target.relative_to(ROOT).as_posix(),bytes=source.stat().st_size,sha256=digest))
dist={path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in (ROOT/'dist').rglob('*') if path.is_file()}
html={path.relative_to(ROOT).as_posix():hashlib.sha256(path.read_bytes()).hexdigest() for path in (ROOT/'docs/_build/html').rglob('*') if path.is_file()}
assert STAGE.resolve().parent==(ROOT/'docs/_build').resolve()
shutil.rmtree(STAGE)
(ROOT/'docs/_build/release-1.2.0-publication.json').unlink()
assert all(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==value for name,value in {**dist,**html}.items())
cleanup=dict(recorded_at=datetime.now(timezone.utc).isoformat(),scope='Normal teardown of newly created task-owned publication staging only; pre-existing workspace output preserved',preserved=preserved,remaining_build_entries=sorted(path.name for path in (ROOT/'docs/_build').iterdir()),distribution_files_verified=len(dist),html_files_verified=len(html),removed_bytes=sum(item['bytes'] for item in preserved),git_status=subprocess.check_output(['git','status','--short'],text=True))
(RECORD/'cleanup-review.json').write_text(json.dumps(cleanup,indent=2)+'\n')
title='STV 1.2.0 published'
text=f'''{title}
{'='*len(title)}

The owner authorized release creation and tagging on 2026-11-01 after committing
the qualified candidate. PR #11 passed hosted core/minimum-runtime validation
and merged. Annotated tag ``v1.2.0`` identifies release commit
``{receipt['commit']}``, whose tree matches qualified commit ``1362c25``.

GitHub Release was published at ``{receipt['published_at']}``.
All three hosted publication jobs passed: exact-asset build/validation, PyPI
Trusted Publishing and Pages deployment. Public GitHub assets and PyPI wheel/
source hashes match the qualified artifacts. The documentation reports 1.2.0
and serves the exact qualified runtime bundle. No qualified archive was rebuilt
or replaced. Issued qualification and failed-attempt history remain unchanged.

* `GitHub release <{receipt['release']}>`_
* `PyPI 1.2.0 <{receipt['pypi']}>`_
* `Documentation <{receipt['documentation']}>`_
* `Hosted publication <{receipt['workflow']}>`_
* `Release PR <https://github.com/sysblacksmith/STV_sphinx-traceability-view/pull/11>`_

Post-release workspace review
-----------------------------

The task-created publication staging scripts/notes and receipt were preserved
with verified SHA-256 hashes before normal temporary-data teardown. All
distributions, original evidence, development environments and current HTML
remain. Only ``docs/_build/html`` remains under the build directory. The normal
Python caches recreated by validation are retained; no broader cleanup occurred.
The earlier owner-approved 566.88 MiB cleanup is retained in the candidate record.

This post-publication documentation/evidence update is an uncommitted local
follow-up; the published tag and artifacts are unchanged. No development-version
bump or additional deployment is included.

Evidence
--------

* :download:`Public hashes, tag and deployment verification <publication-verification.json>`
* :download:`Publication job results <workflow-jobs.json>`
* :download:`GitHub creation/upload receipt <github-release.json>`
* :download:`Post-release cleanup and preservation manifest <cleanup-review.json>`
* :download:`Published release description <release-notes.md.txt>`
'''
(RECORD/'index.rst').write_text(text)
index=ROOT/'docs/test-execution/index.rst'
content=index.read_text()
assert '   1.2.0-publication/index' not in content
index.write_text(content+'   1.2.0-publication/index\n')
maturity=ROOT/'docs/maturity.rst'
content=maturity.read_text()
anchor='1.2.0 release qualification, 2026-11-01'
entry='''1.2.0 released, 2026-11-01
---------------------------

The owner authorized publishing after committing the qualified baseline.
PR #11 passed hosted validation and merged. Annotated ``v1.2.0`` identifies
``c75dbbe84481bf0c319daf09151b6330d6f99c9d``. GitHub release, PyPI Trusted
Publishing and Pages deployment completed successfully. Public distribution
hashes and the deployed 1.2.0 runtime match the qualified artifacts.

:doc:`test-execution/1.2.0-publication/index` retains the publication receipts,
public verification and completed post-release workspace review. Prior
qualification/failed-attempt records remain unchanged. The post-publication
documentation follow-up is local and does not move the issued tag.

'''
assert anchor in content
maturity.write_text(content.replace(anchor,entry+anchor,1))
print(json.dumps(dict(record=str(RECORD),remaining_build_entries=cleanup['remaining_build_entries'],distribution_files_verified=len(dist),html_files_verified=len(html)),indent=2))
