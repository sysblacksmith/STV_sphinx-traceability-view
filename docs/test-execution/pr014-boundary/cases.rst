PR014 canonical executions
============================

Completion times are enclosing report times, not per-subtest finish times.
The complete procedure comprises file and HTTP variants; raw outcomes are retained.

.. test_execution:: STV_TC_SY_062 before fix
   :id: STV_TE_67ADF36ED5EF6CB3
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr014-boundary/before.xml
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T18:22:10.614549+00:00

   **Case:** :need:`STV_TC_SY_062`. Both file/HTTP variants reproduce partial
   clipping and fail on the absent border (0 px, style none). Actual node hit
   tests confirm the unmarked clip edge. :download:`Before report <before.xml>`.

.. test_execution:: STV_TC_SY_062 after fix
   :id: STV_TE_13CB015D758DFB0E
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr014-boundary/after.xml
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T18:25:59.308004+00:00

   **Case:** :need:`STV_TC_SY_062`. Both file/HTTP variants pass the complete
   procedure, including border-box host sizing, resizing and keyboard controls.
   Eight adjacent usability/offline/arrow variants also passed, retained in
   :download:`actual runner report <after.xml>`.
