Problem 12: Limited automated validation and artifact provenance
================================================================================

.. problem_report:: Limited automated validation and artifact provenance
   :id: STV_PR_012
   :status: analyzed
   :basis: observed
   :evidence: docs/problem-tickets/STV_PR_012.rst
   :priority: unassigned
   :verification_state: partial

   **Source and authority:** Audit PRSA-006, optional release hardening. The owner
   authorized proceeding after committing PRSA-005; baseline ``31fd1b5``.
   Scope: prepare automated validation/provenance and review available branch
   protections. No commit, push, release or remote settings change is performed.

   **Cause and implementation:** The audited main branch has no automated checks
   or enforced protection. New pinned workflows and ``scripts/ci.py`` provide
   read-only development validation, actual archive checksums and a manual main-
   branch candidate provenance path. The attestation job alone has write/OIDC
   permissions and executes no repository code. ``scripts/check-workflows.py``
   rejects privilege/trigger/pin drift. See :doc:`../ci-and-provenance`.

   **Traceability:** Existing distribution obligations :need:`STV_SYS_009` and
   :need:`STV_SWR_042`. These are maintainer controls; runtime behavior,
   requirement meanings and extension state-machine/allocation are unchanged.

   **Limits and remaining disposition:** Partially remediated, not closed.
   Current GitHub plan/visibility denies rulesets; protection details are denied
   to this integration. The proposed profile is unapplied. Hosted CI/attestation
   has not run, and no cryptographic provenance is claimed from local metadata.
   The full project docs/shared-method check remains local because that shared
   repository is private. Browser/capacity qualification remains separate.

   **Verification and owner review:** :doc:`../test-execution/prsa-006-fix/index`
   retains actual local commands/results and source/action identities. New
   workflow/policy/protection designs and cases await owner review. Preserve
   the original optional-hardening audit classification; do not promote release
   readiness or requirement verification from these scoped checks.
