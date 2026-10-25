Post-release build cleanup, 2026-10-26
======================================

The owner explicitly requested removing everything under ``docs/_build`` except
the current HTML site, after preserving unique evidence, and updating the shared
release-test skill to use that policy. This is a workspace cleanup record, not a
new product qualification or a change to the issued 1.1.0 release.

Outcome
--------

Only ``docs/_build/html/`` remains. All 2,030 HTML-tree files match their original
SHA-256 hashes. The cleanup removed 158 top-level temporary entries containing
1,956,503,430 bytes, including consumer environments, dependency/tool caches,
generated previews and loose working files. Previous backup/benchmark cleanup
receipts are preserved through the manifest below.

Unique diagnostics, reports, raw SVG exports, screenshots and reproductions are
retained in a compressed evidence archive. The manifest accounts for 2,650 files:
it maps original paths to an existing identical canonical copy, a retained
distribution, or an archive member. All mapped hashes and the archive were
verified after deletion. Generated sites, dependency caches and environments
were not transferred wholesale into permanent evidence.

Project distribution copies are retained under ``dist/``; unique older development
builds use hash-separated ``dist/retained-build-artifacts/`` directories to avoid
replacing same-named files. Preservation does not qualify those development
artifacts for publication. Issued artifacts and prior execution records remain
unchanged.

Both main virtual environments depended on a Python runtime formerly stored in
``_build/tooling``. The post-cleanup check exposed that dependency. The exact
preserved Python 3.13.17 package was restored under
``.venv-implementation/.base-python/`` and both environments' references were
repaired. Python/Sphinx imports and dependency checks pass in both environments.
The shared skill now requires checking such dependencies before cleanup.

Future builds
--------------

The maintained source, benchmark generators, dependency pins and development
environments remain. Fresh isolated checks may need dependency downloads and
environment creation again. Capacity hosts can be regenerated; historical
``--reuse-capacity-from`` directories are no longer available. Paths recorded in
issued logs remain historical provenance, not live storage requirements.

The shared release-test skill now defaults to current HTML only in ``_build``
after testing/release. Required evidence is retained outside it, active consumers
are checked, and existing explicit cleanup authorization is honored without
repeated approval rounds. The skill passed its validator. The current HTML was
preserved rather than rebuilt for this cleanup record.

Evidence
---------

* :download:`Preservation manifest <preservation-manifest.json>`
* :download:`Unique retained evidence <retained-evidence.zip>`
* :download:`Deletion scope and sizes <deletion-targets.json>`
* :download:`Deletion receipt <deletion-receipt.json>`
* :download:`Post-cleanup verification <verification.json>`
* :download:`Runtime relocation <runtime-relocation.json>`
