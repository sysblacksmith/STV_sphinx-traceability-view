.. _STV_CR_016:

STV_CR_016: Save the visible view as SVG
=============================================================

.. change_request:: Save the visible view as SVG
   :id: STV_CR_016
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_016_save-current-view-as-svg.rst
   :priority: unassigned
   :verification_state: partial

   **Owner request, 2026-10-25 (language-corrected):** Add a Save as SVG button
   that saves the current view, including any opened detailed information, into
   an SVG file for which the user can choose the location.

   **Owner clarification, 2026-10-25:** Export only the currently visible area,
   rather than the complete expanded graph and all off-screen card content.
   Source: owner conversation and clarification reply.

   **Baseline:** Available local revision
   ``633bee2a1fb569f5366bdf6a93ec96ed9fbcb04d``. This adds a new output capability;
   no existing export requirement or accepted obligation is replaced.

   **Stakeholder amendment:** :need:`STV_SHR_059` requests a per-view Save as SVG
   control, visible-area capture and reader-selected save location. Include the
   visible graph at its current pan/zoom and the visible portions of open detail
   information, preserving current attribute-folding and scroll states. Do not
   unfold attributes or include graph/card content outside the captured area.
   Capturing a transient tooltip and retaining it while the save control receives
   focus need explicit design assessment, not an implicit promise that a tooltip
   survives its normal dismissal conditions.

   **Retained constraints:** :need:`STV_SHR_015`, :need:`STV_SHR_017`,
   :need:`STV_SHR_018`, :need:`STV_SHR_033`, :need:`STV_SHR_034`,
   :need:`STV_SHR_038`, :need:`STV_SHR_039`, :need:`STV_SHR_040` and
   :need:`STV_SHR_057` retain content, offline/static hosting, accessibility,
   isolation, viewport and persistence obligations. Export must not fetch
   unavailable remote resources or disclose hidden Needs. It does not change
   the live graph, card collection or rendering state.

   **Pending impact analysis:** Assess :need:`STV_SYS_003`,
   :need:`STV_SYS_006`, :need:`STV_SYS_007`, :need:`STV_SWR_015`,
   :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_033`,
   :need:`STV_SWR_039`, :need:`STV_SWR_040`, :need:`STV_SWR_049`,
   :need:`STV_SWR_063`, :need:`STV_SWR_064` and :need:`STV_SWE_RENDER`.
   Reconcile clipping/composition, typography, local media, safe serialization,
   standalone SVG readability, keyboard activation and cancel/failure behavior.
   Assess technology/license implications before selecting an export library.
   See :doc:`/internal-interfaces`, :doc:`/technology-stack`,
   :doc:`/architecture-decisions` and :doc:`/verification-plan`.

   **Open feasibility/scope points:** Browser and OS download policies may not
   permit an application-controlled location picker, especially under file URLs
   or mobile browsers. The requested location choice is retained as intent;
   silently substituting a fixed download folder is not an approved exception.
   Decide supported save interactions and any platform exception with the owner
   before concept acceptance. Toolbar inclusion and transient-tooltip capture
   semantics also remain explicit refinement questions. No implementation
   mechanism, browser API, raster-only substitute or new platform qualification
   is selected by this CR.

   **Stakeholder-stage intake history (before owner approval):** exact requirement
   approval and downstream refinement are pending. No internal requirements,
   ADRs, cases, code or verification states have been changed. Actual checks
   and limitations are consolidated in :doc:`/maturity`.

   **Current decision:** The owner accepted this CR and its exact stakeholder
   requirement on 2026-10-25 and requested concept creation. Concept design,
   current readiness and actual checks are centralized in :doc:`/maturity`;
   earlier intake-stage pending-work statements above describe the prior stage.

   **Owner save clarification, 2026-10-25:** Use browser-managed Save As with
   documented settings, including enabling a location prompt when downloads
   otherwise go to a default directory. An application-controlled folder picker
   is not required. This resolves the location-feasibility choice, not runtime
   verification.
