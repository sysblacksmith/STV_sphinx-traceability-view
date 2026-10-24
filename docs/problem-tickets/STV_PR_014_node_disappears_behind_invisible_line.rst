STV_PR_014: Mark the visible graph boundary with a grey line
================================================================

.. problem_report:: Mark the visible graph boundary with a grey line
   :id: STV_PR_014
   :status: fixed
   :tags: usability, viewport
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_014_node_disappears_behind_invisible_line.rst
   :priority: unassigned
   :verification_state: passed

   **Reporter/date:** Project owner, 2026-10-24.

   **Reported problem:** A node appears partially hidden behind an invisible
   boundary, making it unclear where the graph's visible region ends.

   **Observed evidence:** The annotated screenshot shows the upper part of the
   project/root node clipped near the area below the view controls and visible
   node count. A red ellipse and callout identify the boundary. The screenshot
   shows 17 visible nodes; this is contextual evidence, not an established
   condition required to trigger the problem.

   **Expected behavior (language-corrected from the slide):** Display a thin
   grey line separating the region in which nodes are visible from the region
   in which they are not. The line should make the actual clipping boundary
   apparent to the reader.

   **Reproduction and environment:** Exact steps, browser, operating system,
   product revision and viewport dimensions were not supplied. The supplied screenshot is the original presentation evidence; independent
   reproduction details and environment are recorded below.

   **Original report and attachments:** The intake identifies slide 1 of
   ``PR_node_disappears_behind_invisible_line.pptx`` as the originating source.
   Only the normalized RST and exported PNG were supplied in this repository;
   the PNG is sufficient evidence. Language was corrected without changing intent.

   .. figure:: STV_PR_014_node_disappears_behind_invisible_line.png
      :alt: Annotated graph screenshot highlighting a partially clipped root node and requesting a thin grey separator at the visibility boundary.
      :width: 100%

      Owner-provided screenshot and annotation showing the unmarked boundary.

   **Proposed resolution criteria:**

   * A thin grey separator marks the boundary identified in the screenshot.
   * Its position matches the actual boundary where graph nodes become clipped,
     including after viewport resizing and graph pan/zoom operations.
   * The separator does not obscure node content or intercept graph controls.
   * Existing graph navigation, clipping and interaction behavior remain intact;
     this report requests a visible boundary marker, not removal of clipping.

   **Affected area:** Graph viewport rendering and the boundary adjoining the
   control region. Rendering responsibility: :need:`STV_SWE_RENDER`. Confirmed requirement and interface links are recorded in the analysis below.

   **Analysis and fix plan:** ``.stv-viewport`` establishes clipping with
   ``overflow: hidden``. Its parent has an outer border, but this inner edge
   below the controls/status has no marker. Graph movement can therefore hide
   part of a node behind a boundary with the same background as the controls.

   1. Reproduce partial clipping in Firefox over file/HTTP before changing CSS.
   2. Add one thin grey top border on the viewport container, outside the
      transformed scene; keep its content height 975 px under either host box
      sizing policy. Add no overlay, event handler or clipping-policy change.
   3. Model the exact owner-requested outcome, review its design/test coverage,
      rebuild packaged assets and test clipping, resizing, pan/zoom, keyboard
      expansion and independent views. Check installed asset delivery.
   4. Rebuild the project demo and validate documentation/evidence paths before
      closing this report. No release or commit is authorized.

   **Requirement/design path:** :need:`STV_SHR_056` -> :need:`STV_SWR_062` ->
   :need:`STV_SWE_RENDER`, with :need:`STV_TC_SY_062` verification.
   :doc:`../concept-reviews/round-11` records scoped review and
   :doc:`../test-execution/pr014-boundary/index` retains actual attempts.
   This is a software-local presentation refinement, not a new system boundary.

   **Reproduction:** Firefox 158.0.1 on Windows 11 reproduced partial node clipping
   in both file/HTTP fixtures. The actual overflow edge has no border (0 px,
   style none); hit tests and screenshots are retained in the development record.

   **Disposition:** Fixed and development-verified. The native grey viewport
   border is implemented and packaged; 10 targeted Firefox variants and all
   60 non-browser checks passed. Before-fix failures remain retained. The normal
   demo is rebuilt; full capacity/release qualification is outside this
   presentation-only increment. Historical release records and unrelated
   requirements are unchanged.
