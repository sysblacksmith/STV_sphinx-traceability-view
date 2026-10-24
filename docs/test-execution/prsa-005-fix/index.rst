PRSA-005 clean documentation publication verification
================================================================================

The owner authorized :need:`STV_PR_011` after committing PRSA-004. The normal
PowerShell entry point now builds an inventoried fresh HTML tree using
``scripts/build_docs.py``. No release, deployment, tag or commit is performed.

Scope and failure handling
--------------------------------------------------------------------------------

A new Sphinx build uses a fresh stage and separate doctree cache. Success writes
``_stv-publication.json`` and replaces ``docs/_build/html``. Prior HTML remains
in a sibling directory outside the publication tree; failed stages/caches remain
local diagnostics. Only ``html`` may be published. A failed Sphinx build leaves
published output unchanged; a failed promotion restores the previous tree.
No recursive deletion or Git-history change occurs. Resolved move targets are
checked to stay directly within the intended build directory.

The three real-Sphinx integration cases cover obsolete graph/page/download
removal, complete manifest hashes, failed-build preservation and failed-promotion
rollback. The initial attempt failed because pytest's import path was absent in
Sphinx subprocesses; an autouse fixture now supplies the local extension path.
The first passing attempt and final metadata-synchronized run are both retained.
The existing normal project tree had 34 graph assets before this remediation.
The actual PowerShell-wrapper rebuild and final inventory are retained below.

Review and limits
--------------------------------------------------------------------------------

The revised build workflow/interface and three new case designs await owner
review. Requirement verification and prior concept acceptance are not promoted.
Runtime assets, graph behavior and version are unchanged. Full release, capacity
and browser qualification are not rerun for this maintainer-script change.
Direct incremental Sphinx commands do not provide the publication guarantee.
Previously distributed output is not revoked. PRSA-006 remains outside scope.

Retained evidence
--------------------------------------------------------------------------------

* :download:`Initial fixture failures <fixture-initial.xml>`
* :download:`Initial fixture log <fixture-initial.log>`
* :download:`First passing attempt <first-pass.xml>`
* :download:`First passing log <first-pass.log>`
* :download:`Final regression JUnit <pytest.xml>`
* :download:`Final regression log <pytest.log>`
* :download:`Original project graph inventory <before-publication.json>`
* :download:`Obsolete-file removal observations <observations/clean-rebuild.json>`
* :download:`Failed-build preservation <observations/failed-build.json>`
* :download:`Promotion rollback <observations/failed-promotion.json>`

Final regression results
--------------------------------------------------------------------------------

All three integration cases pass. Their initial fixture setup failures and first
passes remain historical and are not counted as additional distinct cases.
Final source identity, exact commands and environment are retained below.

* :download:`Source hashes and invocation <verification.json>`
* :download:`Case-result mapping <case-results.json>`

.. toctree::
   :maxdepth: 1

   cases

PowerShell entry-point correction
--------------------------------------------------------------------------------

The first real wrapper invocation failed before Sphinx: Windows PowerShell
removed nested double quotes in the existing Python-version precheck, producing
a Python syntax error. The corrected assertion uses single quotes within the
Python expression. That failure left the publication untouched; its log is
retained separately. This correction is required for the normal entry point to
reach the new publication helper.

* :download:`Initial wrapper quoting error <project-build-initial.log>`

Actual project publication
--------------------------------------------------------------------------------

The normal PowerShell entry point succeeded with warnings treated as errors.
The HTML tree now contains one current graph asset instead of the 34 retained
before the fix. Every manifest entry's size and SHA-256 matched the actual file;
there are no unlisted files other than the manifest itself and no public doctree
cache. Prior output was preserved outside ``html``. The successful wrapper's
summary prints both the publication and retained-output locations.

* :download:`Successful project wrapper build <project-build.log>`
* :download:`Project publication inventory checks <project-publication.json>`

Documentation and traceability checks
--------------------------------------------------------------------------------

Strict executable coverage reports 67 requirements and 90 executable cases,
with no unmapped active requirements or unknown IDs. The shared validator passes
complete requirement-to-test coverage and repository-relative evidence checks.
The normal project wrapper build passed with warnings treated as errors.
The project-publication observation above identifies that first successful
wrapper run; later documentation handover edits receive their own fresh build.

* :download:`Successful traceability validation <traceability.log>`

Commands from the repository root (``<shared-skill>`` is the configured shared
reverse-engineer-requirements skill):

.. code-block:: text

   .venv-implementation/Scripts/python.exe scripts/check-coverage.py --strict
   powershell -NoProfile -ExecutionPolicy Bypass -File build-docs.ps1
   .venv-implementation/Scripts/python.exe <shared-skill>/scripts/validate_traceability.py docs/_build/html/needs.json --version 1.0 --repo-root . --require-test-coverage
