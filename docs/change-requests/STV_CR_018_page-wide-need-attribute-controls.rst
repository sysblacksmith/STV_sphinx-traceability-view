.. _STV_CR_018:

STV_CR_018: Page-wide Need attribute controls
=============================================================

.. change_request:: Page-wide Need attribute controls
   :id: STV_CR_018
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_018_page-wide-need-attribute-controls.rst
   :priority: unassigned
   :verification_state: partial

   **Owner request, 2026-10-25 (language-corrected):** Add Collapse all and Expand
   all buttons to each page containing Sphinx-Needs elements, to collapse or
   unfold their detailed attributes.

   **Owner clarification, 2026-10-25:** Each documentation page is intended,
   with page-wide controls; this is not a request for buttons on every STV side
   card. Source: owner conversation and clarification reply. The original
   wording used "side" and "extend"; these are normalized to the confirmed
   meaning "page" and "expand".

   **Baseline:** Available local revision
   ``633bee2a1fb569f5366bdf6a93ec96ed9fbcb04d``. Existing individual Need metadata
   toggles remain usable. This adds page-wide host-document behavior rather than
   replacing graph relationship controls or persistent-card Close all.

   **Stakeholder amendment:** :need:`STV_SHR_061` adds Collapse all and Expand
   all on each page with rendered Sphinx-Needs elements. Each action controls
   the detailed attributes of all those elements on that page, including
   attributes initially outside the viewport. Body content, titles, IDs and
   original-object navigation remain available. Individual folding remains
   available after a bulk operation.

   **Retained constraints:** Keyboard activation and visible focus,
   offline/static hosting and host-hidden exclusions remain applicable
   (:need:`STV_SHR_017`, :need:`STV_SHR_018`, :need:`STV_SHR_034`). No graph
   expansion, seed changes, card closing or modification of authored Need data
   is requested. Page-wide controls do not operate on copied STV tooltip or
   side-card attributes; those remain independently inspectable.

   **Pending impact analysis:** Assess :need:`STV_SYS_003`,
   :need:`STV_SYS_006`, :need:`STV_SWR_015`, :need:`STV_SWR_017`,
   :need:`STV_SWR_034`, :need:`STV_SWR_049` and :need:`STV_SWE_RENDER`.
   Establish responsibility for page-level controls separately from view-local
   controls, preserving host/theme compatibility, individual metadata toggles,
   multiple Need types, absent metadata and mixed initial fold states. Assess
   pages containing both rendered Needs and several STV views, safe DOM scope
   and copied-detail isolation. See :doc:`/internal-interfaces`,
   :doc:`/architecture-software` and :doc:`/verification-plan`.

   **Stakeholder-stage intake history (before owner approval):** Exact requirement
   approval, internal refinement, coverage design and implementation remain
   pending. No particular host/theme DOM implementation or universal third-party
   widget expansion is promised. No existing acceptance or runtime result is
   extended by this record. Actual checks are consolidated in :doc:`/maturity`.

   **Current decision:** The owner accepted this CR and its exact stakeholder
   requirement on 2026-10-25 and requested concept creation. Concept design,
   current readiness and actual checks are centralized in :doc:`/maturity`;
   earlier intake-stage pending-work statements above describe the prior stage.
