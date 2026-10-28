.. _STV_CR_019:

STV_CR_019: Remember current view across page reloads
===================================================

.. change_request:: Remember current view across page reloads
   :id: STV_CR_019
   :status: draft
   :basis: owner
   :evidence: docs/change-requests/STV_CR_019_remember-current-view.rst
   :priority: unassigned
   :verification_state: unverified

   **Owner request, 2026-10-28:** Add a checkbox that the user can enable to
   retain the currently shown STV view across page reloads.

   **Owner clarification:** The view includes the currently visible nodes,
   open detail cards, and the currently visible graph area including zoom.
   Source: owner conversation and clarification reply on 2026-10-28.

   **Requested behavior:** Add an opt-in checkbox, provisionally labelled
   "Remember my current view". Enabling it captures the current view and keeps
   the saved state updated as the view changes. Reloading restores that state
   and the enabled preference. Disabling it clears the saved state for its
   scope and stops persistence, without changing the current display; later
   reloads use normal startup behavior.

   **State to retain:** The displayed graph node set and expansion/collapse
   state needed to reconstruct it; the open detail cards; and viewport
   position/pan and zoom. Interpret visible nodes as the displayed graph set,
   including nodes outside the viewport. Retain layout information where
   necessary to restore the same visible area.

   **Proposed browser integration:** Use browser local storage for the
   preference and a versioned snapshot; cookies are not required. Scope state
   to the documentation/project, page and individual STV view. Persistence is
   local to a browser profile and site, without cross-device synchronization.
   Restore after graph data and layout are ready, avoiding initialization
   that resets the restored viewport.

   **Proposed acceptance criteria:**

   * Reload with persistence enabled restores the displayed nodes, open
     detail cards, viewport position and zoom.
   * View changes while enabled become the state restored on the next reload.
   * The checkbox remains enabled after reload.
   * Disabling clears saved state for its scope without changing the current
     display; later reloads use normal startup behavior.
   * Separate pages and multiple STV views retain independent state.
   * Missing, stale, incompatible or corrupt snapshots fall back safely;
     removed nodes and cards are tolerated.
   * Storage unavailability or quota failures do not break graph interaction
     or falsely indicate successful persistence.
   * The checkbox supports keyboard activation, a clear label and visible focus.

   **Pending impact analysis:** Review graph state, expansion, layout,
   viewport and persistent detail-card interfaces, including
   :need:`STV_CR_014`. Define storage schema, scope, update timing and restore
   order. Assess documentation changes, concurrent tabs, viewport size changes
   and precedence of explicit URL/navigation state. Retain static/offline use
   where browser storage is available; assess file:// separately because
   storage behavior varies by browser. Derive traceable requirements and
   verification cases before implementation.

   **Current decision:** Recorded as a draft change request. Requirement
   refinement, implementation, verification and release approval remain pending.
