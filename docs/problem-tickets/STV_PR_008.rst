STV_PR_008: Historical distributions omit complete license materials
====================================================================

.. problem_report:: Historical distributions omit complete license materials
   :id: STV_PR_008
   :status: fixed
   :basis: observed
   :evidence: docs/problem-tickets/STV_PR_008.rst
   :priority: unassigned
   :verification_state: partial

   **Source:** PRSA-001, public-release audit dated 2026-10-24. Baseline
   ``4b1199e`` plus the authorized PRSA-002 working-tree fix. Remediation is
   authorized; new release preparation and publication are not authorized.

   **Cause and owner scope:** The former GitHub releases and retained historical archives predate complete
   MIT / compiled-dependency notice packaging. Adding notices to current builds
   did not supply them with old archive bytes. The owner removed the Releases
   and explicitly authorized resolving the remaining finding on 2026-10-24.

   **Disposition design:** Preserve archive hashes, source/test evidence and Git
   history. Supply complete project/third-party licensing and corresponding
   source references with an explicit historical scope and SHA-256 inventory.
   Retire old binary download roles and quarantine generated download copies.
   See :doc:`../licensing/historical/index`. Affected existing distribution
   obligations: :need:`STV_SYS_009`, :need:`STV_SWR_042` and :need:`STV_SWR_046`.

   **Limits:** Supplied notices do not change historical bytes or recall earlier
   downloads. Removed hosted source archives remain uninspected and are not
   republished. No Git refs or historical objects are rewritten. The supplement
   is an engineering remediation and does not assert a legal opinion.

   **Checks and current review:** :doc:`../test-execution/prsa-001-003-fix/index`
   retains actual results, source/package identities and initial failed attempts.
   Interface/tooling and new verification case designs await owner review;
   prior concept acceptance and requirement verification are not promoted.

   **Current disposition:** Fixed for the authorized technical remediation scope.
   The 84-case development regression and independent Python 3.10 offline host
   pass; supplement/archive checks and final documentation validation are linked
   above. Owner review remains pending; no release qualification is claimed.
