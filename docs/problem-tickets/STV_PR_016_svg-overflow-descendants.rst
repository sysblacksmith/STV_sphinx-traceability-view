STV_PR_016: SVG export omits visible graph overflow
===================================================

.. problem_report:: SVG export omits visible graph overflow
   :id: STV_PR_016
   :status: fixed
   :basis: observed
   :evidence: docs/test-execution/1.1.0-candidate-1/narrow-diagnostic.log; docs/test-execution/1.1.0-candidate-1/export-capacity.py
   :priority: unassigned
   :verification_state: passed

   **Reporter/date:** Agent release qualification, 2026-10-25.

   **Observation:** A live 200-node view contains visible graph labels, while
   the saved SVG contains no graph node elements. Wide exports retained visible
   detail cards; a narrower export could contain only background/viewport styles.

   **Expected:** :need:`STV_SYS_011`, :need:`STV_SWR_070` and :need:`STV_SWR_071`
   require a static snapshot of the actual visible graph and details.

   **Cause:** EXPORT pruned a non-intersecting positioned scene by its own box.
   Negative-position descendants can overflow that box into the visible crop.
   The parent's bounds alone do not establish that its subtree is invisible.

   **Fix scope:** Preserve traversal through overflow-visible containers;
   retain clipping at actual clipping/scroll containers and off-screen leaf/flow
   handling. This is a state-neutral snapshot correction, not a requirement,
   architecture or behavioral-state change. EXPORT ownership and the existing
   accepted interfaces remain authoritative.

   **Verification:** Add real reopened-SVG assertions for visible graph labels,
   rerun the maximum-size supplement and qualify a fresh candidate. Candidate 1's
   196-check result remains historical; its artifacts must not be published.
   Earlier supplementary assertion/layout mistakes and their diagnostic attempts
   remain in that record rather than being reclassified as product passes.

   **Observed fix evidence:** Software baseline ``41e57ed``; the rejected
   runtime fails the overflow regression and the corrected runtime passes all
   four existing export variants. Fresh candidate-2 full selection: 196 passes;
   four maximum-size exports also pass and were visually inspected. See
   :doc:`../test-execution/1.1.0-candidate-2/qualification`.
