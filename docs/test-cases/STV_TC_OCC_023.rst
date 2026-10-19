Merge shared expansion sets
===========================

.. test_case:: Merge shared expansion sets
   :id: STV_TC_OCC_023
   :status: accepted
   :tags: release_later
   :basis: documented
   :evidence: docs/stakeholder.rst; docs/software.rst
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_023, STV_SWR_023
   :last_result: not_run

   **Level/environment:** Planned browser acceptance, Windows/Firefox,
   file and nested static HTTP output, network blocked.

   **Preconditions/inputs:** Future occurrence-mode implementation; two
   parents sharing one child with two disjoint nonempty relationship groups.

   **Procedure:** In separate mode expand disjoint groups on two copies. Switch to shared mode.

   **Expected outcomes:** One shared object remains with the union of both expanded groups and no duplicate canonical edges.

   Repeat with a cycle and a missing target to verify termination and visible
   placeholder identity. Start at 199 visible occurrences and request two more:
   the transition must be rejected atomically with the node-limit explanation.
   A transition to exactly 200 succeeds. Attempt a mode switch producing 201:
   retain mode, graph and exploration state and explain the limit.

   **Execution/evidence:** No executable implementation exists in v0.2.0.
   Retain per-case results, candidate identity and file/HTTP screenshots when
   the future release implements this scope; no execution record is invented.
