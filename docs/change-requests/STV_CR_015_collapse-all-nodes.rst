.. _STV_CR_015:

STV_CR_015: Collapse all graph relationships
=============================================================

.. change_request:: Collapse all graph relationships
   :id: STV_CR_015
   :status: accepted
   :basis: owner
   :evidence: docs/change-requests/STV_CR_015_collapse-all-nodes.rst
   :priority: unassigned
   :verification_state: not_assessed

   **Owner request, 2026-10-25 (language-corrected):** Add a Collapse all nodes
   button that returns to the initial seed without any opened links.

   **Owner clarification, 2026-10-25:** Keep the current starting objects,
   including an interactively selected starting object; do not restore the
   author's original seeds. Source: owner conversation and clarification reply.

   **Baseline:** Available local revision
   ``633bee2a1fb569f5366bdf6a93ec96ed9fbcb04d``; accepted navigation obligations
   remain historical baseline evidence. Remote publication is not a new product
   verification baseline.

   **Stakeholder amendment:** :need:`STV_SHR_058` adds one view-local command
   to clear every ordinary expanded relationship and retain the current starting
   objects. It supplements :need:`STV_SHR_003`, :need:`STV_SHR_007`,
   :need:`STV_SHR_048` and :need:`STV_SHR_053`; their existing obligations are
   not replaced. The artificial project entry retains the initial overview
   behavior in :need:`STV_SHR_047`. No graph-wide expand command is requested.

   **Retained constraints:** Shared identity, hidden-object exclusion, node
   capacity, keyboard operation and independent views remain applicable
   (:need:`STV_SHR_020`, :need:`STV_SHR_025`, :need:`STV_SHR_034`,
   :need:`STV_SHR_038`, :need:`STV_SHR_043`). Persistent cards survive graph
   collapse under :need:`STV_SHR_057`; this command is distinct from Close all
   details and Reset viewport. Viewport positioning after collapse is pending
   concept refinement, without weakening retained navigation obligations.

   **Pending impact analysis:** Reconcile :need:`STV_SYS_007`,
   :need:`STV_SWR_003`, :need:`STV_SWR_007`, :need:`STV_SWR_025`,
   :need:`STV_SWR_038`, :need:`STV_SWR_052`, :need:`STV_SWR_057` and
   :need:`STV_SWR_063`; assess state ownership in :need:`STV_SWE_STATE` and
   controls in :need:`STV_SWE_RENDER`. Cover active seed identity, project
   entry paging, reachability/cycles, visibility/capacity accounting, subsequent
   expansion, keyboard focus and future occurrence-mode restoration. The reset
   must not leave expansions that reappear unexpectedly after later navigation.
   Parsing/serialization changes are not assumed necessary. See
   :doc:`/state-machine`, :doc:`/internal-interfaces`,
   :doc:`/implementation-plan` and :doc:`/verification-plan`.

   **Stakeholder-stage intake history (before owner approval):** Owner approval of
   the exact requirement is pending; internal requirements, design, ADRs, test
   cases and code have not been revised. Seedless initial overview behavior is
   retained rather than interpreted as an instruction to remove its entry links.
   No implementation, acceptance or runtime result is claimed. Consolidated
   checks and downstream readiness are recorded in :doc:`/maturity`.

   **Current decision:** The owner accepted this CR and its exact stakeholder
   requirement on 2026-10-25 and requested concept creation. Concept design,
   current readiness and actual checks are centralized in :doc:`/maturity`;
   earlier intake-stage pending-work statements above describe the prior stage.
