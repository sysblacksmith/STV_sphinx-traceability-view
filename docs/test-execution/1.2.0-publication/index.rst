STV 1.2.0 published
===================

The owner authorized release creation and tagging on 2026-11-01 after committing
the qualified candidate. PR #11 passed hosted core/minimum-runtime validation
and merged. Annotated tag ``v1.2.0`` identifies release commit
``c75dbbe84481bf0c319daf09151b6330d6f99c9d``, whose tree matches qualified commit ``1362c25``.

GitHub Release was published at ``2026-11-01T14:32:34Z``.
All three hosted publication jobs passed: exact-asset build/validation, PyPI
Trusted Publishing and Pages deployment. Public GitHub assets and PyPI wheel/
source hashes match the qualified artifacts. The documentation reports 1.2.0
and serves the exact qualified runtime bundle. No qualified archive was rebuilt
or replaced. Issued qualification and failed-attempt history remain unchanged.

* `GitHub release <https://github.com/sysblacksmith/STV_sphinx-traceability-view/releases/tag/v1.2.0>`_
* `PyPI 1.2.0 <https://pypi.org/project/sphinx-traceability-view/1.2.0/>`_
* `Documentation <https://sysblacksmith.github.io/STV_sphinx-traceability-view/>`_
* `Hosted publication <https://github.com/sysblacksmith/STV_sphinx-traceability-view/actions/runs/41316712011>`_
* `Release PR <https://github.com/sysblacksmith/STV_sphinx-traceability-view/pull/11>`_

Post-release workspace review
-----------------------------

The task-created publication staging scripts/notes and receipt were preserved
with verified SHA-256 hashes before normal temporary-data teardown. All
distributions, original evidence, development environments and current HTML
remain. Only ``docs/_build/html`` remains under the build directory. The normal
Python caches recreated by validation are retained; no broader cleanup occurred.
The earlier owner-approved 566.88 MiB cleanup is retained in the candidate record.

This record documents the completed publication and workspace review. The
published tag and artifacts remain unchanged; subsequent development uses its
own version and commits.

Evidence
--------

* :download:`Public hashes, tag and deployment verification <publication-verification.json>`
* :download:`Publication job results <workflow-jobs.json>`
* :download:`GitHub creation/upload receipt <github-release.json>`
* :download:`Post-release cleanup and preservation manifest <cleanup-review.json>`
* :download:`Published release description <release-notes.md.txt>`
