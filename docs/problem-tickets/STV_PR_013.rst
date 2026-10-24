STV_PR_013: Keep node positions stable during relationship expansion
====================================================================

.. problem_report:: Keep node positions stable during relationship expansion
   :id: STV_PR_013
   :status: fixed
   :tags: usability, release_initial
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_013.rst
   :priority: unassigned
   :verification_state: passed

   **Reporter/date:** Project owner, 2026-10-24. Original baseline ``a445aa6``.

   **Reported problem (language-corrected):** Expanding a node's relationships
   shifts its same-level peers and the activated node, making navigation hard.

   **Cause and reproduction:** Fresh ELK ordering, parent centering and origin
   normalization ran on every toggle without committed geometry. Firefox measured
   P moving about 357 screen px and Q about -510 screen px on first expansion
   over both file and HTTP. :doc:`../test-execution/pr013-poc/index` preserves
   before/after measurements, failed attempts and owner-review screenshots.

   **Owner decisions:** The owner requested a PoC before broad documentation,
   liked stable navigation, reported missing arrows in Firefox, then approved
   the corrected arrows and requested natural numeric seed ordering. After
   approving the PoC ("i love it"), the owner explicitly requested concept
   creation, review and implementation to finalize the fix. No release or
   commit is authorized by that instruction.

   **Design and ownership:** :ref:`STV_ADR_008` partially supersedes repeated
   centering in :ref:`STV_ADR_006`. Fresh layouts retain
   :need:`STV_SHR_052` / :need:`STV_SWR_056`; group/root commands follow
   :need:`STV_SHR_054` / :need:`STV_SWR_058`. :need:`STV_SWE_LAYOUT` owns
   nearest free slots, clicked-band anchoring and shared-test reranking.
   :need:`STV_SWE_RENDER` owns per-view committed snapshots, transactional
   retention, focus, transforms and :need:`STV_SWR_059` SVG bounds. Initial
   numeric order follows :need:`STV_SHR_055` / :need:`STV_SWR_060`.

   **Arrow regression:** The PoC introduced valid negative graph coordinates
   outside a zero-origin SVG viewport. Logical ports were correct but Firefox
   clipped segments. Matching positioned SVG/viewBox origins now include every
   route/node extent with padding; final routes remain governed by
   :need:`STV_SWR_053`. No coordinate shift is used to disguise the clipping.

   **Accepted limits:** Surviving ordinary horizontal slots and the clicked
   band remain stable. Other bands may move vertically for changed height;
   shared tests may change their median associated rank. Collapsed gaps can
   remain until fresh initialization/reseed/overview/page placement. Reset
   viewport changes the transform only. This is not global frozen geometry.

   **Concept and verification:** :doc:`../concept-reviews/round-9` records
   scoped acceptance, semantic coverage and diagram review.
   :doc:`../test-execution/pr013-final/index` records final development checks
   and canonical cases. The final development run has 111 distinct latest passing tests, including
   component, Firefox file/HTTP, 200-node capacity and clean-package checks.
   The two placeholder visibility test failures and corrected retests remain
   recorded; product geometry did not change during those retests.
   Historical candidate results
   do not qualify the current code. Full release qualification remains separate.
