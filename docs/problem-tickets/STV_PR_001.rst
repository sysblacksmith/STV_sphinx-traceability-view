Problem 1: Facing edge ports
============================

.. problem_report:: Facing edge ports
   :id: STV_PR_001
   :status: fixed
   :tags: usability_draft
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_001.rst; docs/change-requests/STV_CR_003_usability-problems.rst
   :priority: unassigned
   :verification_state: partial

   Reported by: project owner. Date: 2026-10-18.

   **Requested behavior**

   Links to objects above a node leave its top edge and enter the bottom edge of the parent. The reported example is STV_SWR_001 to STV_SYS_001.

   **Original report**

   .. code-block:: text

      The arrows in the view are routed around the boxes (see STV_PR_001.png). This is unneceesaryily complex. the link to elements above the box shall start on the boxes top and not bottom. Furthermore the links shall end at the bottom of the parent box (STV_SYS_001) and not on its top. This avoids unnesessary edges in the arrows.

   **Evidence**

   .. image:: STV_PR_001.png
      :alt: Original screenshot illustrating problem 1
      :width: 100%

   **Analysis and disposition**

   See :doc:`/change-requests/STV_CR_003_usability-problems` for requirements, design,
   source changes and smoke-test evidence.

   **Diagnosis and fix**

   The router used a bottom exit and top entry even for upward links. Facing ports now follow the relative box positions.

   Affected artifacts: :need:`STV_SHR_050`, :need:`STV_SWR_053`.
   Source: ``frontend/src/layout/layout.js``.

   **Verification and handover**

   Smoke check: ``node --test test/layout.test.js`` passed on 2026-10-18; commands and limits are recorded in :doc:`/change-requests/STV_CR_003_usability-problems`.
   The fix is implemented as a draft. Owner review, full regression and release
   approval remain pending; partial verification does not accept linked requirements.

   Lifecycle: received and analyzed on 2026-10-18; fixed in the draft increment
   with smoke evidence on 2026-10-18. Reopen to analyzed if the issue recurs.
