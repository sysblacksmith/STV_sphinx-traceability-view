Select separate occurrences
===========================

.. test_case:: Select separate occurrences
   :id: STV_TC_OCC_019
   :status: accepted
   :tags: release_later
   :basis: documented
   :evidence: docs/stakeholder.rst; docs/software.rst
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_019, STV_SWR_019
   :last_result: not_run

   **Level/environment:** Planned browser acceptance, Windows/Firefox,
   file and nested static HTTP output, network blocked.

   **Preconditions/inputs:** Future occurrence-mode implementation; two
   parents sharing one child with two disjoint nonempty relationship groups.

   **Procedure:** Open a two-parent graph sharing one child. Select separate-occurrence mode, then shared mode.

   **Expected outcomes:** Separate mode shows two child occurrences; shared mode shows one. The selector and visible mode agree.

   Repeat with a cycle and a missing target to verify termination and visible
   placeholder identity. Start at 199 visible occurrences and request two more:
   the transition must be rejected atomically with the node-limit explanation.
   A transition to exactly 200 succeeds. Attempt a mode switch producing 201:
   retain mode, graph and exploration state and explain the limit.

   **Execution/evidence:** No executable implementation exists in v0.2.0.
   Retain per-case results, candidate identity and file/HTTP screenshots when
   the future release implements this scope; no execution record is invented.
