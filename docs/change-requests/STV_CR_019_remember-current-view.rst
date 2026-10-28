.. _STV_CR_019:

STV_CR_019: Remember current view across page reloads
===================================================

.. change_request:: Remember current view across page reloads
   :id: STV_CR_019
   :status: draft
   :basis: owner
   :evidence: docs/change-requests/STV_CR_019_remember-current-view.rst
   :priority: unassigned
   :verification_state: not_assessed

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

   **Stakeholder amendment for owner review, 2026-10-28:**
   :need:`STV_SHR_003` is revised to apply collapsed startup only when not
   restoring an opted-in saved view. :need:`STV_SHR_057` replaces unconditional
   reload clearing with the same opt-in exception. New :need:`STV_SHR_062`
   defines the checkbox lifecycle, :need:`STV_SHR_063` the restored state,
   :need:`STV_SHR_064` isolation/local retention, and :need:`STV_SHR_065`
   safe recovery. All six revisions are draft pending exact owner approval.

   **Working proposals requiring alignment:** Retain graph node placement and
   card order, but not card-internal scroll/fold state, page scroll, transient
   hover or keyboard focus. Persist through browser restarts. Separate tabs
   keep their live state; the last successful save wins on a later reload.
   Browser-local storage remains a design proposal, not a mandated API.
   A reduced card limit keeps the newest entries. Invalid starting contexts
   or over-capacity restored graphs fall back to normal startup. Direct-file
   persistence depends on browser storage support, without weakening the
   existing offline exploration requirement.

   **Baseline and pending contracts:** PR #6 is based on main revision
   ``3c2647f56898efce1e1b59b261af30f0f905cf61``. Current internal revisions
   remain historical accepted inputs, not reconciled designs for this increment.
   Assess :need:`STV_SYS_007`, :need:`STV_SYS_008`,
   :need:`STV_SWR_003`, :need:`STV_SWR_038`, :need:`STV_SWR_043`,
   :need:`STV_SWR_048`, :need:`STV_SWR_052`, :need:`STV_SWR_057`,
   :need:`STV_SWR_058`, :need:`STV_SWR_059`,
   :need:`STV_SWR_063` through :need:`STV_SWR_065`;
   serialization, initialization, reachability/collapse, layout/focus,
   detail restoration and capacity checks require downstream review.
   Existing :need:`STV_SHR_017`, :need:`STV_SHR_018`,
   :need:`STV_SHR_034`, :need:`STV_SHR_043`, :need:`STV_SHR_044`,
   :need:`STV_SHR_052` and :need:`STV_SHR_054` constraints remain applicable;
   fresh-placement wording needs reconciliation with saved placement at the
   concept stage. No hidden Need can be restored from browser state.

   **Current phase and review:** The owner invoked stakeholder elicitation and
   manage-change to align this CR and accept the stakeholder requirements only.
   Exact proposed wording has not yet been approved. No internal refinement,
   concept acceptance or product implementation is performed in this scope.
   Prior acceptance and verification history remains in :doc:`/maturity`.

   **Validation:** Authoring checks confirm six draft stakeholder revisions,
   unique stakeholder IDs, unchanged other stakeholder records and use of the
   existing configured Need model. The globbed CR index includes this file.
   Sphinx and the traceability validator have not been run in this session;
   downstream derivation and verification coverage for new SHRs remain pending.
   No runtime checks or acceptance evidence are claimed.
