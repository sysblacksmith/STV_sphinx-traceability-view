STV_PR_002: Direct readable routes
==================================

.. problem_report:: Direct readable routes
   :id: STV_PR_002
   :status: fixed
   :tags: usability_draft
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_002.rst; docs/change-requests/STV_CR_003_usability-problems.rst
   :priority: unassigned
   :verification_state: partial

   Reported by: project owner. Date: 2026-10-18.

   **Requested behavior**

   Connections use direct paths where clear of other boxes, avoiding unnecessary bends and the far-right detour.

   **Original report**

   .. code-block:: text

      the arrows in the view are routed with unnecessary edges which makes the picture hard to read (see STV_PR_002.png). Please route on direct pathes to establish better readability

   **Evidence**

   .. image:: STV_PR_002.png
      :alt: Original screenshot illustrating problem 2
      :width: 100%

   **Analysis and disposition**

   See :doc:`/change-requests/STV_CR_003_usability-problems` for requirements, design,
   source changes and smoke-test evidence.

   **Diagnosis and fix**

   Every link used an outer corridor. Clear segments now connect facing ports directly; blocked paths retain obstacle-avoiding detours.

   Affected artifacts: :need:`STV_SHR_050`, :need:`STV_SWR_053`.
   Source: ``frontend/src/layout/layout.js``.

   **Verification and handover**

   Smoke check: ``node --test test/layout.test.js`` passed on 2026-10-18; commands and limits are recorded in :doc:`/change-requests/STV_CR_003_usability-problems`.
   The fix is implemented as a draft. Owner review, full regression and release
   approval remain pending; partial verification does not accept linked requirements.

   Lifecycle: received and analyzed on 2026-10-18; fixed in the draft increment
   with smoke evidence on 2026-10-18. Reopen to analyzed if the issue recurs.
