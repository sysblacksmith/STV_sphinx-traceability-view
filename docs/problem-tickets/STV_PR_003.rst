STV_PR_003: Increase view height
================================

.. problem_report:: Increase view height
   :id: STV_PR_003
   :status: fixed
   :tags: usability_draft
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_003.rst; docs/change-requests/STV_CR_003_usability-problems.rst
   :priority: unassigned
   :verification_state: partial

   Reported by: project owner. Date: 2026-10-18.

   **Requested behavior**

   Increase the standard viewport height by a factor of 1.5 so three expanded levels have more room.

   **Original report**

   .. code-block:: text

      the views height is not sufficent, as soon as three Levels of elemnts are opened in Standard view, the user has to zoom out. please increase the height by factor 1.5

   **Analysis and disposition**

   See :doc:`/change-requests/STV_CR_003_usability-problems` for requirements, design,
   source changes and smoke-test evidence.

   **Diagnosis and fix**

   The standard viewport was fixed at 650px. The stylesheet now provides 975px, a factor of 1.5.

   Affected artifacts: :need:`STV_SHR_049`, :need:`STV_SWR_054`.
   Source: ``src/sphinx_traceability_view/static/stv.css``.

   **Verification and handover**

   Smoke check: ``docs/test-scripts/test_browser.py::test_usability_smoke`` passed on 2026-10-18; commands and limits are recorded in :doc:`/change-requests/STV_CR_003_usability-problems`.
   The fix is implemented as a draft. Owner review, full regression and release
   approval remain pending; partial verification does not accept linked requirements.

   Lifecycle: received and analyzed on 2026-10-18; fixed in the draft increment
   with smoke evidence on 2026-10-18. Reopen to analyzed if the issue recurs.
