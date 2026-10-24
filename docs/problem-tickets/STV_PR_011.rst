STV_PR_011: Incremental output retains obsolete published data
==============================================================

.. problem_report:: Incremental output retains obsolete published data
   :id: STV_PR_011
   :status: fixed
   :basis: observed
   :evidence: docs/problem-tickets/STV_PR_011.rst
   :priority: unassigned
   :verification_state: partial

   **Source and authority:** Audit PRSA-005 identified 31 graph scripts in
   incremental output versus one in a clean build. The owner authorized the
   next fix after committing PRSA-004; baseline ``d9b7408``. This is local
   publication preparation, not deployment or a new release.

   **Cause and expected outcome:** Content-addressed asset emission updates
   current references but does not remove old graph/detail assets, HTML pages
   or downloads. Reusing that tree for publication exposes obsolete files.
   A publication tree must contain only one fresh successful build's output.
   Preserve usable existing output if the build or promotion fails.

   **Fix:** Use an isolated fresh HTML stage and separate doctree directory.
   Generate a relative-path SHA-256/size manifest, retain prior output outside
   the publication tree, and promote successful output with rollback on a failed
   rename. Validate resolved paths before moving directories. The PowerShell
   entry point preserves dependency checks and propagates helper failures.
   See :doc:`../internal-interfaces` and the README publication instructions.

   **Traceability:** Existing distribution obligations :need:`STV_SYS_009`
   and :need:`STV_SWR_042`. The maintainer build scripts own this boundary;
   no extension component allocation, requirement meaning, runtime version,
   graph state, event or timer changes.

   **Checks and review:** :doc:`../test-execution/prsa-005-fix/index` retains
   real Sphinx rebuild/removal, failed-build preservation and injected promotion
   failure/rollback results, plus the actual project output inventory. Old output
   remains local evidence outside ``html``; this does not recall earlier copies.
   Changed build workflow/interface and new case designs await owner review.
   Prior concept acceptance and requirement verification are unchanged.

   **Disposition:** Fixed with three passing scoped integration cases. Owner
   review of the publication workflow/interface and case designs remains pending;
   a release/deployment decision is separate from these development checks.
