Round 14: Owner acceptance for v1.0.0
===============================================

Authority and boundary
-----------------------

On 2026-10-24 the owner explicitly approved readiness items 1 and 2 and requested
a v1.0.0 release. :ref:`release-1-0-0-authority` records the instruction and explicit
deferral of runner improvements and hosted hardening. Input baseline:
``9d3b793``. Prior execution histories and acceptance decisions remain intact.

Accepted scope
----------------

* PRSA-001/003: historical licensing supplement and patched maintainer tooling,
  offline Python 3.10 bootstrap/install design and clean consumer policy;
  :need:`STV_PR_008`, :need:`STV_PR_009`, :doc:`../licensing/historical/index`,
  :doc:`../technology-stack`, :doc:`../test-execution/prsa-001-003-fix/index`.
* PRSA-002: authored transport-marker stripping and output-local restoration
  contract; :need:`STV_PR_007`, :doc:`../internal-interfaces`,
  :doc:`../test-execution/prsa-002-fix/index`.
* PRSA-004: source archive allowlist and actual-archive regression design;
  :need:`STV_PR_010`, :doc:`../test-execution/prsa-004-fix/index`.
* PRSA-005: staged clean publication, manifest, failed-build preservation and
  rollback contracts; :need:`STV_PR_011`,
  :doc:`../test-execution/prsa-005-fix/index`.
* PR015: final details width/frame, initially folded interactive metadata and
  original-object header navigation; :need:`STV_PR_015`,
  :doc:`round-13`, :doc:`../test-execution/pr015-details/index`.

The accepted test designs are :need:`STV_TC_SY_038`,
:need:`STV_TC_SY_047`, :need:`STV_TC_SY_048`, :need:`STV_TC_SY_049`,
:need:`STV_TC_SY_050`, :need:`STV_TC_SY_051`, :need:`STV_TC_SY_052`,
:need:`STV_TC_SY_053`, :need:`STV_TC_SY_054`, :need:`STV_TC_SW_040`,
:need:`STV_TC_SW_041` and :need:`STV_TC_SW_042`.
The already accepted PR015 design :need:`STV_TC_SY_065` is owner-approved.

The owner closes the pending acceptance conditions on these existing reviewed
artifacts. No new manual observation, legal opinion, execution result or
requirement verification is inferred from this decision. The prior failures
and successful development evidence remain in their original records.

Exclusions and release gates
-----------------------------

:need:`STV_PR_012` remains analyzed and partially verified. Hosted workflow,
attestation/protection activation and their draft cases are not accepted by
this scoped decision. The release runner remains unchanged. Full current
candidate qualification, artifact identity and final documentation validation
are separate release gates; the canceled candidate remains historical.

The owner subsequently clarified that remaining security findings are
nonblocking deferrals for v1.0.0 and that release labels must not depend on
repository visibility. The release is named v1.0.0; no visibility setting is
changed. Deferral does not manufacture hosted execution or close PRSA-006.
