Problem 4: Delay hover details
==============================

.. problem_report:: Delay hover details
   :id: STV_PR_004
   :status: fixed
   :tags: usability_draft
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_004.rst; docs/change-requests/STV_CR_003_usability-problems.rst
   :priority: unassigned
   :verification_state: partial

   Reported by: project owner. Date: 2026-10-18.

   **Requested behavior**

   Show details after approximately one second of continuous hover.

   **Original report**

   .. code-block:: text

      the details tool tip triggers too fast. please adapt the mvp to show the details only after around 1 second of hover over

   **Analysis and disposition**

   See :doc:`/change-requests/STV_CR_003_usability-problems` for requirements, design,
   source changes and smoke-test evidence.

   **Diagnosis and fix**

   Node entry opened details immediately. A cancellable 1000ms hover timer now delays opening; explicit Details activation remains immediate.

   Affected artifacts: :need:`STV_SHR_015`, :need:`STV_SYS_006`, :need:`STV_SWR_050`.
   Source: ``frontend/src/inspect/inspect.js; frontend/src/render/view.js``.

   **Verification and handover**

   Smoke check: ``docs/test-scripts/test_browser.py::test_usability_smoke`` passed on 2026-10-18; commands and limits are recorded in :doc:`/change-requests/STV_CR_003_usability-problems`.
   The fix is implemented as a draft. Owner review, full regression and release
   approval remain pending; partial verification does not accept linked requirements.

   Lifecycle: received and analyzed on 2026-10-18; fixed in the draft increment
   with smoke evidence on 2026-10-18. Reopen to analyzed if the issue recurs.
