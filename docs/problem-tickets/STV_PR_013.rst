STV_PR_013: Keep node positions stable during relationship expansion
================================================================================

.. problem_report:: Keep node positions stable during relationship expansion
   :id: STV_PR_013
   :status: analyzed
   :tags: usability_draft
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_013.rst
   :priority: unassigned
   :verification_state: partial

   **Reporter/date:** Project owner, 2026-10-24. Baseline ``a445aa6``.

   **Reported problem (language-corrected):** When relationships for a node are
   expanded, nodes on the same level, including the activated node, shift
   positions. This is annoying and makes navigating the tree difficult.

   **Owner authority and sequence:** Analyze the issue, prepare and smoke-test
   a proof-of-concept fix, then let the owner confirm it. Only after confirmation
   should the requirements/design/verification documentation be revised from
   top to bottom. This authorizes draft code and a reviewable demo, not concept
   acceptance, a commit or release preparation.

   **Diagnosis and actual reproduction:** Layout recomputes ELK ordering,
   bottom-up parent centering and graph normalization for every visible-set
   change. The renderer does not supply the last committed geometry or the
   activated node. Firefox reproduced P moving about 357 screen pixels and Q
   about -510 screen pixels on the first expansion, over both file and HTTP.

   **Provisional fix:** For group/root toggles, retain surviving primary slots
   and the clicked band, allocate new nodes into free space and create vertical
   room above/below as needed. Keep the shared test lane separate; allow negative
   branch coordinates and fit their bounds on explicit Reset viewport. Keep
   normal fresh layout for initialization/reseeding/overview/page changes. Restore
   focus without native scrolling. The shipped browser bundle is rebuilt.

   **Ownership and provisional impact:** :need:`STV_SWE_LAYOUT` and
   :need:`STV_SWE_RENDER`; ``frontend/src/layout/layout.js``, the provisional
   ``stability.js`` helper and ``frontend/src/render/view.js``. Existing
   :need:`STV_SWR_056` / :need:`STV_SHR_052` parent-centering intent needs explicit
   reconciliation with stable interactive positions after owner confirmation.
   :need:`STV_SWR_053` safe routing, shared identity, test-lane constraints and
   view independence remain relevant. Requirement meanings/statuses, accepted
   ADRs and verification claims are not rewritten in this PoC increment.

   **Smoke evidence and demo:** :doc:`../test-execution/pr013-poc/index` retains
   actual before/after measurements and attempts. Twenty-five component tests
   and six Firefox transport/adjacent interaction cases pass. Surviving nodes
   move 0 px in the measured four-toggle sequence. Reset viewport fits all demo
   nodes, and the resulting screenshot was inspected. Review the local
   ``docs/_build/pr013-poc/html/index.html`` or the rebuilt normal project demo.

   **Current disposition:** Analyzed; a tested PoC is ready for owner confirmation.
   Broad regression, complex rank-changing test scenarios, capacity, packaging,
   formal case allocation and the full documentation/acceptance update remain
   pending. Moving other semantic bands is permitted when additional height is
   needed; this is not a guarantee that every node in every band never moves.

   **Owner feedback and PoC correction:** The owner likes the stable-position
   behavior but reported missing/truncated arrows in Firefox, with a screenshot.
   This is a regression introduced by the PoC, not a separate routing diagnosis:
   new negative coordinates lay outside the SVG's zero-origin viewport. Logical
   route endpoints remained correct, but Firefox clipped their visible segments.
   An explicit SVG viewBox and matching positioned viewport now cover every node
   and route point, with marker padding. This changes no node coordinates.
   Bounds are accumulated incrementally rather than spreading large route arrays.

   The same Firefox scene restored the missing segments when only SVG bounds
   changed. New downward/upward route-coverage checks verify negative points,
   complete viewport containment, endpoint-to-box alignment and unchanged node
   positions over file/HTTP. See the arrow follow-up in the existing PoC evidence
   record. The corrected bundle and both review demos are rebuilt; owner review
   remains pending before the full documentation/baseline update.

   **Initial ID order refinement:** After confirming the corrected interaction
   looks good, the owner requested numeric left-to-right order for seeded
   requirements. Unexpanded seed and project-entry rows now use natural ID
   sorting (for example, ``REQ_2`` before ``REQ_10``), rather than ELK's incidental
   component order. Expanded navigation still preserves existing positions.
   Fresh expanded scenes retain their routing/centering ordering; this refinement
   does not continuously reshuffle discovered nodes. The ordering evidence is
   retained with the same PoC pending full baseline documentation refinement.
