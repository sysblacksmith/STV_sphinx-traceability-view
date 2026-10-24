Per-case publication maintenance executions
================================================================================

Timestamps are actual JUnit report-file completion times (UTC). Initial fixture
setup failures do not reproduce the stale-output defect; removal and rollback
are demonstrated by the passing real-Sphinx cases. See :doc:`index`.

.. test_execution:: docs/test-scripts/test_publication.py::test_clean_publication_removes_obsolete_assets
   :id: STV_TE_D5D5C30CB3605726
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-005-fix/fixture-initial.xml :: docs/test-scripts/test_publication.py::test_clean_publication_removes_obsolete_assets
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T14:48:49.902075+00:00

   **Case:** :need:`STV_TC_PUBLICATION_CLEAN`.

   **Evidence:** :download:`fixture-initial.xml <fixture-initial.xml>`. See :doc:`index`
   for setup corrections, final source identity, exact commands and scope.

.. test_execution:: docs/test-scripts/test_publication.py::test_failed_build_preserves_published_tree
   :id: STV_TE_04F65BAA6CDB685B
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-005-fix/fixture-initial.xml :: docs/test-scripts/test_publication.py::test_failed_build_preserves_published_tree
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T14:48:49.902075+00:00

   **Case:** :need:`STV_TC_PUBLICATION_FAIL`.

   **Evidence:** :download:`fixture-initial.xml <fixture-initial.xml>`. See :doc:`index`
   for setup corrections, final source identity, exact commands and scope.

.. test_execution:: docs/test-scripts/test_publication.py::test_failed_promotion_restores_previous_tree
   :id: STV_TE_257F51CA54DE5456
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-005-fix/fixture-initial.xml :: docs/test-scripts/test_publication.py::test_failed_promotion_restores_previous_tree
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T14:48:49.902075+00:00

   **Case:** :need:`STV_TC_PUBLICATION_ROLLBACK`.

   **Evidence:** :download:`fixture-initial.xml <fixture-initial.xml>`. See :doc:`index`
   for setup corrections, final source identity, exact commands and scope.

.. test_execution:: docs/test-scripts/test_publication.py::test_clean_publication_removes_obsolete_assets
   :id: STV_TE_00DF8B8564A416AA
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-005-fix/first-pass.xml :: docs/test-scripts/test_publication.py::test_clean_publication_removes_obsolete_assets
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T14:49:40.932303+00:00

   **Case:** :need:`STV_TC_PUBLICATION_CLEAN`.

   **Evidence:** :download:`first-pass.xml <first-pass.xml>`. See :doc:`index`
   for setup corrections, final source identity, exact commands and scope.

.. test_execution:: docs/test-scripts/test_publication.py::test_failed_build_preserves_published_tree
   :id: STV_TE_057BEBB8A33EC7E4
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-005-fix/first-pass.xml :: docs/test-scripts/test_publication.py::test_failed_build_preserves_published_tree
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T14:49:40.932303+00:00

   **Case:** :need:`STV_TC_PUBLICATION_FAIL`.

   **Evidence:** :download:`first-pass.xml <first-pass.xml>`. See :doc:`index`
   for setup corrections, final source identity, exact commands and scope.

.. test_execution:: docs/test-scripts/test_publication.py::test_failed_promotion_restores_previous_tree
   :id: STV_TE_D90868BD589779C5
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-005-fix/first-pass.xml :: docs/test-scripts/test_publication.py::test_failed_promotion_restores_previous_tree
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T14:49:40.932303+00:00

   **Case:** :need:`STV_TC_PUBLICATION_ROLLBACK`.

   **Evidence:** :download:`first-pass.xml <first-pass.xml>`. See :doc:`index`
   for setup corrections, final source identity, exact commands and scope.

.. test_execution:: docs/test-scripts/test_publication.py::test_clean_publication_removes_obsolete_assets
   :id: STV_TE_0BA0673DB0572C62
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-005-fix/pytest.xml :: docs/test-scripts/test_publication.py::test_clean_publication_removes_obsolete_assets
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T14:52:25.019713+00:00

   **Case:** :need:`STV_TC_PUBLICATION_CLEAN`.

   **Evidence:** :download:`pytest.xml <pytest.xml>`. See :doc:`index`
   for setup corrections, final source identity, exact commands and scope.

.. test_execution:: docs/test-scripts/test_publication.py::test_failed_build_preserves_published_tree
   :id: STV_TE_4B16C75492B3457D
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-005-fix/pytest.xml :: docs/test-scripts/test_publication.py::test_failed_build_preserves_published_tree
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T14:52:25.019713+00:00

   **Case:** :need:`STV_TC_PUBLICATION_FAIL`.

   **Evidence:** :download:`pytest.xml <pytest.xml>`. See :doc:`index`
   for setup corrections, final source identity, exact commands and scope.

.. test_execution:: docs/test-scripts/test_publication.py::test_failed_promotion_restores_previous_tree
   :id: STV_TE_E0C20537B8E451DF
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/prsa-005-fix/pytest.xml :: docs/test-scripts/test_publication.py::test_failed_promotion_restores_previous_tree
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T14:52:25.019713+00:00

   **Case:** :need:`STV_TC_PUBLICATION_ROLLBACK`.

   **Evidence:** :download:`pytest.xml <pytest.xml>`. See :doc:`index`
   for setup corrections, final source identity, exact commands and scope.
