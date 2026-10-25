.. _STV_CR_017:

STV_CR_017: Smaller configurable detail text
=============================================================

.. change_request:: Smaller configurable detail text
   :id: STV_CR_017
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_017_configurable-detail-font-size.rst
   :priority: unassigned
   :verification_state: partial

   **Owner request, 2026-10-25 (language-corrected):** Reduce the font size of
   detail cards, both tooltips and side cards, to approximately 70% and make
   their font sizes configurable. Source: project owner conversation.

   **Baseline:** Available local revision
   ``633bee2a1fb569f5366bdf6a93ec96ed9fbcb04d``; current rendered detail typography
   is the comparison baseline. This means approximately 70% of the previous
   size, not a reduction by 70%.

   **Stakeholder amendment:** :need:`STV_SHR_060` adds a smaller default and
   configurable font sizing for both transient hover details and persistent side
   cards. It supplements the content/readability obligations of
   :need:`STV_SHR_015`, :need:`STV_SHR_033` and :need:`STV_SHR_057` without
   removing information, changing ordinary graph labels or changing the host
   Need page typography.

   **Retained constraints:** Keyboard operation, visible focus, scrolling,
   viewport containment, full locally available detail content and offline
   behavior remain applicable. Reduced text must not disable browser zoom or
   alter the persistent-card limit and eviction rules. SVG capture under
   :need:`STV_SHR_059` must reflect the effective detail typography.

   **Pending impact analysis:** Assess :need:`STV_SYS_006`,
   :need:`STV_SWR_015`, :need:`STV_SWR_033`, :need:`STV_SWR_034`,
   :need:`STV_SWR_064` and :need:`STV_SWE_RENDER`; trace configuration through
   authoring validation, serialization and both detail presentation paths.
   Reconcile relative sizing of nested headings/tables/code, containment and
   the existing explicit size declarations. See :doc:`/internal-interfaces`,
   :doc:`/getting-started`, :doc:`/implementation-plan` and
   :doc:`/verification-plan`. No configuration name, units, numeric range or
   default pixel size is selected at stakeholder stage.

   **Disclosed review assumptions:** Configuration is provisionally interpreted
   as author configuration, consistent with the existing Sphinx configuration
   surface, rather than a new reader settings panel. Whether tooltip and side
   card sizes share one setting or have independent settings remains open;
   both surfaces must be configurable. Approximately 70% is the requested
   visual target; measurable tolerances belong in the reviewed refinement.

   **Stakeholder-stage intake history (before owner approval):** owner review of
   :need:`STV_SHR_060` is pending. No existing accepted requirement is rewritten,
   no prior test result verifies the new typography, and no implementation or
   internal refinement has occurred. Checks are consolidated in :doc:`/maturity`.

   **Current decision:** The owner accepted this CR and its exact stakeholder
   requirement on 2026-10-25 and requested concept creation. Concept design,
   current readiness and actual checks are centralized in :doc:`/maturity`;
   earlier intake-stage pending-work statements above describe the prior stage.
