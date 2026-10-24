Per-case packaging remediation results
================================================================================

Actual JUnit outcomes with report-file completion timestamps (UTC).
The initial failure demonstrates the old archive boundary. Later passes do
not imply owner acceptance or full release qualification. See :doc:`index`.

.. test_execution:: docs/test-scripts/test_sdist.py::test_sdist_excludes_local_evidence_and_rebuilds_wheel
   :id: STV_TE_053E27C9576BC49A
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-004-fix/before.xml :: docs/test-scripts/test_sdist.py::test_sdist_excludes_local_evidence_and_rebuilds_wheel
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T14:39:54.392761+00:00

   **Case:** :need:`STV_TC_SDIST_BOUNDARY`.

   **Evidence:** :download:`before.xml <before.xml>`. Exact commands,
   source identities, actual archive members and limits are retained in :doc:`index`.

.. test_execution:: docs/test-scripts/test_sdist.py::test_sdist_excludes_local_evidence_and_rebuilds_wheel
   :id: STV_TE_3F0DEB05F990600D
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-004-fix/after.xml :: docs/test-scripts/test_sdist.py::test_sdist_excludes_local_evidence_and_rebuilds_wheel
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T14:40:25.945287+00:00

   **Case:** :need:`STV_TC_SDIST_BOUNDARY`.

   **Evidence:** :download:`after.xml <after.xml>`. Exact commands,
   source identities, actual archive members and limits are retained in :doc:`index`.

.. test_execution:: docs/test-scripts/test_package.py::test_clean_wheel_host
   :id: STV_TE_8C0DFF558A66DCA0
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-004-fix/package.xml :: docs/test-scripts/test_package.py::test_clean_wheel_host
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T14:41:42.683929+00:00

   **Case:** :need:`STV_TC_F988267D01C9`.

   **Evidence:** :download:`package.xml <package.xml>`. Exact commands,
   source identities, actual archive members and limits are retained in :doc:`index`.
