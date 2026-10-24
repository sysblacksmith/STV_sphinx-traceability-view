STV_PR_015: Correct detail readability, metadata controls and artifact-ID links
================================================================================

.. problem_report:: Correct detail readability, metadata controls and artifact-ID links
   :id: STV_PR_015
   :status: fixed
   :tags: usability, persistent_details
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_015_detail-presentation.rst
   :priority: unassigned
   :verification_state: passed

   **Reporter/date:** Project owner, 2026-10-24, acceptance findings in this
   conversation. Language corrected without changing meaning.

   **Reported/expected:** Make the detail views twice as wide. Secondary
   attributes such as status and tags must start folded. The existing arrow
   must fold/unfold them; it currently does nothing. The artifact-ID link in
   copied details must lead to the actual artifact, rather than this same view.
   Other working links must keep working.

   **Input:** Commit ``740c35ce234ec26b16c76a0b77463b273f84863c`` plus the current
   uncommitted CR014 implementation and the owner's acceptance findings.

   **Diagnosis:** RENDER fixes the dock at 360 px. The lazy copied content misses
   Sphinx-Needs' document-ready metadata handler, so its show-state and inert
   spans survive extraction. INSPECT rebases the header self-link to the copied
   Need ID, turning original navigation into an in-box jump. The real Firefox
   file/HTTP baseline reproduces these findings.

   **Resolution:** Target a 720 px dock; place it below graph containers at or
   below 1120 px, bounded by available width. INSPECT initializes only copied
   metadata controls with folded defaults, per-table state and pointer/Enter/
   Space activation, unique IDs and ARIA state. Reuse preserves local state.
   Keep canonical header-ID URLs and open them in a new tab; ordinary local
   body fragments remain namespaced. Existing sanitization stays in force.

   **Affected V-cycle:** :need:`STV_SHR_057`, :need:`STV_SWR_064`,
   :need:`STV_SWR_016`, :need:`STV_SWR_018`; owners :need:`STV_SWE_INSPECT`
   and :need:`STV_SWE_RENDER`. New regression :need:`STV_TC_SY_065`.
   Design review: :doc:`../concept-reviews/round-13`. State transitions:
   :doc:`../state-machine` (Copied metadata disclosure).

   **Actual result:** Both baseline variants fail; all 127 distinct selected
   checks pass after the correction, including file/HTTP acceptance, existing
   persistence/races, adjacent rich-content/hover/security/nested-path checks,
   frontend units and clean wheel/source-package checks. Full capacity and
   release qualification were not repeated. Evidence and phase identity:
   :doc:`../test-execution/pr015-details/index`.

   **Disposition:** Fixed and development-verified. Owner acceptance retest is
   pending; no commit, release or external publication is implied.


Pane boundary acceptance follow-up
-------------------------------------

The owner supplied an annotated screenshot showing the unmarked side-pane edge,
the graph disappearing behind it and a shadowed gap at the first card. Requested
resolution: a thin grey outline around the pane whenever it is open. The frame
now marks all four edges, aligns with the graph's top/full height and retains
padding around shadow-free cards. This is a state-neutral CSS refinement of
:need:`STV_SWR_064`; verification extends :need:`STV_TC_SY_065` and reruns the
existing viewport-boundary and persistent browser procedures. See the follow-up
results in :doc:`../test-execution/pr015-details/index`.
