STV_PR_009: Build and test environments contain advisory-matched dependencies
=============================================================================

.. problem_report:: Build and test environments contain advisory-matched dependencies
   :id: STV_PR_009
   :status: fixed
   :basis: observed
   :evidence: docs/problem-tickets/STV_PR_009.rst
   :priority: unassigned
   :verification_state: partial

   **Source:** PRSA-003, public-release audit dated 2026-10-24. Baseline
   ``4b1199e`` plus the authorized PRSA-002 working-tree fix. Remediation is
   authorized; new release preparation and publication are not authorized.

   **Cause and owner scope:** The audit identified certifi, Pillow, pytest, pip and setuptools versions
   matched by published advisories. The owner approved refreshing tooling and
   the offline wheelhouse on 2026-10-24, together with the historical licensing
   fix. Old environment logs remain truthful evidence.

   **Disposition design:** Recreate the two existing environment paths using
   project-local Python 3.13.17. Preserve old environments as inactive local
   evidence. Maintain common pip/setuptools/certifi pins in one requirements
   file, pin patched Pillow in docs and pytest in implementation tooling.
   Documentation/test tooling now requires Python 3.11+; base package runtime
   remains Python 3.10+. Resolve the offline wheelhouse with both actual Python
   interpreters, including version-marker and Windows ABI differences. Bootstrap
   isolated consumers using patched offline tooling before package installation.

   **Compatibility:** :need:`STV_SYS_009`, :need:`STV_SWR_042` and
   :need:`STV_SWR_046` remain unchanged. Newer maintainer tooling is separate
   from the extension runtime contract. Browser dependencies and state-machine
   behavior are unchanged. Historical Guava JVM API advisory matches are not
   treated as browser vulnerabilities; their absent filesystem APIs remain the
   audit's recorded non-applicability rationale.

   **Checks and current review:** :doc:`../test-execution/prsa-001-003-fix/index`
   retains actual results, source/package identities and initial failed attempts.
   Interface/tooling and new verification case designs await owner review;
   prior concept acceptance and requirement verification are not promoted.

   **Current disposition:** Fixed for the authorized technical remediation scope.
   The 84-case development regression and independent Python 3.10 offline host
   pass; supplement/archive checks and final documentation validation are linked
   above. Owner review remains pending; no release qualification is claimed.
