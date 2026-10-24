PRSA-006 CI and provenance preparation
================================================================================

The owner authorized :need:`STV_PR_012` after committing PRSA-005, baseline
``31fd1b5``. Local workflow/code preparation is complete; the finding remains
**partially remediated**, because hosted checks, attestation generation and the
chosen repository protections have not been activated/confirmed. No commit,
push, workflow dispatch, release, visibility or remote settings change occurred.

Design and service limits
--------------------------------------------------------------------------------

:doc:`../../ci-and-provenance` describes read-only Windows validation, a separate
Python 3.10 runtime job, manual main-only candidate builds, LF checksum files,
and public-main-only OIDC attestation isolated from repository-code execution.
All six top-level action references are pinned to official full commit hashes;
the upstream attestation wrapper's nested attest action is also commit-pinned.
Action definitions and release-tag identities were retrieved from upstream.
Workflow syntax/expressions pass checksum-verified actionlint 1.7.12.

The main branch remains unprotected. GitHub ruleset access returns 403 with an
upgrade-or-public requirement; detailed protection access is denied to the
integration. The concrete protection JSON is an unapplied owner-review proposal.
The private shared-method repository is not exposed to Actions with a new token;
full engineering documentation/traceability remains a local check. Browser and
capacity qualification remain separate from these automated development checks.

Actual local results and retained failures
--------------------------------------------------------------------------------

The shared CI driver passed **42 non-browser Python cases and 22 JavaScript
cases**. It regenerated browser assets without drift, built the sdist/wheel,
provisioned the offline wheelhouse, ran installed-wheel and source-archive checks,
and wrote checksums/source metadata. A first driver attempt passed 40 Python
cases before the two new policy/checksum cases were added; it remains historical.

The new checksum case initially exposed CRLF output rejected by GNU sha256sum.
Checksum output now writes explicit LF bytes. Positive verification, deliberate
byte tampering and ambiguous-wheel rejection pass. Workflow negative cases pass;
a final targeted retest also covers missing attestation jobs and altered subjects.
That targeted policy refinement is recorded separately from the full driver run.

The exact runtime subcommand passed with the new development wheel installed
on Python 3.10: installed module identity/version, pip check and Sphinx fixture
build all passed. No hosted Windows/Ubuntu Actions run or cryptographic attestation
has been executed; local metadata is not presented as signed provenance.
The 26 browser cases were deselected; two capacity cases were excluded by file.

Review and remaining owner steps
--------------------------------------------------------------------------------

Workflow/policy/protection designs and three new case designs await owner review.
Requirement verification and prior concept acceptance are unchanged. To complete
remote hardening, commit/push the reviewed workflows, observe successful hosted
checks, arrange public visibility or an eligible plan, review/apply the proposed
protections with the actual check names, then manually generate and verify
provenance for a separately approved future candidate. No first release is started.

Evidence
--------------------------------------------------------------------------------

* :download:`GitHub visibility/protection observations <github-state.json>`
* :download:`Official action release pins <action-pins.json>`
* :download:`Verified actionlint provenance <actionlint-provenance.json>`
* :download:`Actionlint result (zero exit) <actionlint.log>`
* :download:`First local driver log <local-ci-first.log>`
* :download:`Final local driver log <local-ci.log>`
* :download:`Final driver Python JUnit <pytest.xml>`
* :download:`Final driver JavaScript JUnit <node.xml>`
* :download:`Resolved implementation environment <environment.txt>`
* :download:`Initial checksum regression failure <checksum-initial.xml>`
* :download:`Initial checksum error log <checksum-initial.log>`
* :download:`Final targeted security JUnit <security.xml>`
* :download:`Final targeted security log <security.log>`
* :download:`Earlier targeted pass <security-first-pass.xml>`
* :download:`Python 3.10 wheel installation <runtime-install.log>`
* :download:`Actual installed-runtime check <runtime.log>`
* :download:`Development archive checksums <SHA256SUMS>`
* :download:`Unsigned local source/build metadata <build-info.json>`

Canonical results and identities
--------------------------------------------------------------------------------

The latest local outcome is passed for 64 distinct pytest/Node cases plus the
standalone installed-runtime case. Earlier attempts and targeted reruns remain
separate history, not additional distinct cases. The last targeted security
retest follows the final policy refinements; the complete driver run predates
those refinements as recorded in the source identity note.

* :download:`Final source identities and exact commands <verification.json>`
* :download:`Pre-refinement CI source snapshot <ci-source-hashes.json>`
* :download:`Per-case mapping <case-results.json>`

.. toctree::
   :maxdepth: 1

   cases

Final local documentation and traceability
--------------------------------------------------------------------------------

The normal clean-publication PowerShell build passed with warnings treated as
errors. Strict executable coverage reports 67 requirements and 92 executable
cases, with no unmapped active requirements or unknown IDs. The shared validator
passes complete requirement-to-test coverage and repository-relative evidence
checks. These local checks do not establish hosted CI success, an attestation,
remote protection activation, owner acceptance or release readiness.

* :download:`Successful project documentation build <documentation.log>`
* :download:`Successful traceability validation <traceability.log>`

Commands (``<shared-skill>`` is the configured reverse-engineer-requirements skill):

.. code-block:: text

   powershell -NoProfile -ExecutionPolicy Bypass -File build-docs.ps1
   .venv-implementation/Scripts/python.exe scripts/check-coverage.py --strict
   .venv-implementation/Scripts/python.exe <shared-skill>/scripts/validate_traceability.py docs/_build/html/needs.json --version 1.0 --repo-root . --require-test-coverage
