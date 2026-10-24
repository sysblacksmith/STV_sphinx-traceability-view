PR013 canonical development case executions
============================================================

Timestamps are report-file completion times in UTC, not per-test end times.
Source/package identities and exact commands are retained in :doc:`index`.
These development results do not qualify a release.

.. test_execution:: test_missing_placeholder_and_detail_error[file] (adjacent-browser.xml)
   :id: STV_TE_6AA25FA7CA5F5192
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/adjacent-browser.xml :: test_missing_placeholder_and_detail_error[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T17:14:42.322167+00:00

   **Case:** :need:`STV_TC_SY_003`. The first attempt predates the explicit-fit
   test adaptation. Product geometry is unchanged; the retest brings discovered
   content into view before asserting visible identity and detail recovery.
   :download:`Actual runner report <adjacent-browser.xml>`.

.. test_execution:: test_missing_placeholder_and_detail_error[http] (adjacent-browser.xml)
   :id: STV_TE_F9FF69F5AF8B80F1
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/adjacent-browser.xml :: test_missing_placeholder_and_detail_error[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T17:14:42.322167+00:00

   **Case:** :need:`STV_TC_SY_012`. The first attempt predates the explicit-fit
   test adaptation. Product geometry is unchanged; the retest brings discovered
   content into view before asserting visible identity and detail recovery.
   :download:`Actual runner report <adjacent-browser.xml>`.

.. test_execution:: test_missing_placeholder_and_detail_error[file] (missing-recheck.xml)
   :id: STV_TE_CECBFB91BF01D342
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/missing-recheck.xml :: test_missing_placeholder_and_detail_error[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:15:51.973207+00:00

   **Case:** :need:`STV_TC_SY_003`. The first attempt predates the explicit-fit
   test adaptation. Product geometry is unchanged; the retest brings discovered
   content into view before asserting visible identity and detail recovery.
   :download:`Actual runner report <missing-recheck.xml>`.

.. test_execution:: test_missing_placeholder_and_detail_error[http] (missing-recheck.xml)
   :id: STV_TE_64C890A655FDC0CE
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/missing-recheck.xml :: test_missing_placeholder_and_detail_error[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:15:51.973207+00:00

   **Case:** :need:`STV_TC_SY_012`. The first attempt predates the explicit-fit
   test adaptation. Product geometry is unchanged; the retest brings discovered
   content into view before asserting visible identity and detail recovery.
   :download:`Actual runner report <missing-recheck.xml>`.

.. test_execution:: STV_SWR_056: competing parents do not displace a separate centered parent
   :id: STV_TE_112EF87FDDCC77C1
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/node.xml :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: competing parents do not displace a separate centered parent
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:06:59.766358+00:00

   **Case:** :need:`STV_TC_SW_011`; :download:`actual report <node.xml>`.
   Development source/package identities and commands are retained in :doc:`index`.

.. test_execution:: STV_SWR_053: clear facing ports and fan-in avoid outer detours
   :id: STV_TE_E9D48EE5D838F9F2
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/node.xml :: frontend/src/layout/tests/layout.test.js :: STV_SWR_053: clear facing ports and fan-in avoid outer detours
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:06:59.766358+00:00

   **Case:** :need:`STV_TC_SW_010`; :download:`actual report <node.xml>`.
   Development source/package identities and commands are retained in :doc:`index`.

.. test_execution:: test_large_project_at_visible_capacity[file]
   :id: STV_TE_FC0887B66F8AAE1A
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/capacity.xml :: docs/test-scripts/test_capacity.py::test_large_project_at_visible_capacity[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:18:27.167481+00:00

   **Case:** :need:`STV_TC_SY_017`; :download:`actual report <capacity.xml>`.
   Development source/package identities and commands are retained in :doc:`index`.

.. test_execution:: test_large_project_at_visible_capacity[http]
   :id: STV_TE_1B0FA04DA16E3401
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/capacity.xml :: docs/test-scripts/test_capacity.py::test_large_project_at_visible_capacity[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:18:27.167481+00:00

   **Case:** :need:`STV_TC_SY_035`; :download:`actual report <capacity.xml>`.
   Development source/package identities and commands are retained in :doc:`index`.

.. test_execution:: STV_TC_SW_043 complete procedure
   :id: STV_TE_5D39F79D9C4AC4CD
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/node.xml
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:06:59.766358+00:00

   **Case:** :need:`STV_TC_SW_043`. One execution of the complete modeled procedure,
   comprising 6 actual runner subtests. Every subtest passed; none was
   skipped. Timestamp is the enclosing report completion time, not fabricated
   per-subtest timing. Full selectors/outcomes remain in
   :download:`case-results.json <case-results.json>` and
   :download:`node.xml <node.xml>`.

.. test_execution:: STV_TC_SW_044 complete procedure
   :id: STV_TE_9660E9FDD3E534BF
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/node.xml
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:06:59.766358+00:00

   **Case:** :need:`STV_TC_SW_044`. One execution of the complete modeled procedure,
   comprising 2 actual runner subtests. Every subtest passed; none was
   skipped. Timestamp is the enclosing report completion time, not fabricated
   per-subtest timing. Full selectors/outcomes remain in
   :download:`case-results.json <case-results.json>` and
   :download:`node.xml <node.xml>`.

.. test_execution:: STV_TC_SW_045 complete procedure
   :id: STV_TE_4ADD571D9D48391C
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/node.xml
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:06:59.766358+00:00

   **Case:** :need:`STV_TC_SW_045`. One execution of the complete modeled procedure,
   comprising 1 actual runner subtests. Every subtest passed; none was
   skipped. Timestamp is the enclosing report completion time, not fabricated
   per-subtest timing. Full selectors/outcomes remain in
   :download:`case-results.json <case-results.json>` and
   :download:`node.xml <node.xml>`.

.. test_execution:: STV_TC_SY_058 complete procedure
   :id: STV_TE_BFC00DA35F1B2273
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/focused-browser.xml
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:09:51.186986+00:00

   **Case:** :need:`STV_TC_SY_058`. One execution of the complete modeled procedure,
   comprising 6 actual runner subtests. Every subtest passed; none was
   skipped. Timestamp is the enclosing report completion time, not fabricated
   per-subtest timing. Full selectors/outcomes remain in
   :download:`case-results.json <case-results.json>` and
   :download:`focused-browser.xml <focused-browser.xml>`.

.. test_execution:: STV_TC_SY_059 complete procedure
   :id: STV_TE_E018DFA57A2EB582
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/focused-browser.xml
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:09:51.186986+00:00

   **Case:** :need:`STV_TC_SY_059`. One execution of the complete modeled procedure,
   comprising 4 actual runner subtests. Every subtest passed; none was
   skipped. Timestamp is the enclosing report completion time, not fabricated
   per-subtest timing. Full selectors/outcomes remain in
   :download:`case-results.json <case-results.json>` and
   :download:`focused-browser.xml <focused-browser.xml>`.

.. test_execution:: STV_TC_SY_060 complete procedure
   :id: STV_TE_873F1D2F001CA837
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/pr013-final/focused-browser.xml
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T17:09:51.186986+00:00

   **Case:** :need:`STV_TC_SY_060`. One execution of the complete modeled procedure,
   comprising 2 actual runner subtests. Every subtest passed; none was
   skipped. Timestamp is the enclosing report completion time, not fabricated
   per-subtest timing. Full selectors/outcomes remain in
   :download:`case-results.json <case-results.json>` and
   :download:`focused-browser.xml <focused-browser.xml>`.
