Problem 5: Order relationship controls by vertical direction
================================================================================

.. problem_report:: Order relationship controls by vertical direction
   :id: STV_PR_005
   :status: fixed
   :tags: usability_draft
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_005.rst
   :priority: unassigned
   :verification_state: partial

   **Reporter/date:** Project owner, 2026-10-18.

   **Report, spelling and capitalization corrected:** The order of the buttons
   used to expand and collapse links is not intuitive. Buttons that open links
   to parents above the node shall appear at the top, and buttons that open
   links to children below the node shall appear at the bottom.

   **Source:** Converted from the owner's ``docs/problem-tickets/STV_PR_005.txt``.
   Corrections preserve the requested behavior; reproduction/environment
   details beyond the existing MVP were not supplied.

   **Diagnosis:** Rendering iterated outgoing groups before incoming groups,
   preserving relation insertion order. Authorship direction does not indicate
   whether targets appear above or below the node.

   **Disposition:** Use configured semantic levels to place wholly upward groups
   first, neutral groups next and wholly downward groups last. Mixed-direction,
   same-level, test-lane and unresolved targets are neutral. Preserve host order
   within each category and retain one control per relation/direction group.
   Ordering applies before expansion and remains identical for collapse controls.

   **Affected artifacts:** :need:`STV_SHR_051`, :need:`STV_SWR_055`,
   :need:`STV_SWE_RENDER`. See :doc:`/change-requests/STV_CR_005_control-order`.

   **Implementation:** ``frontend/src/groups.js`` and ``frontend/src/view.js``.
   No system responsibility, architecture boundary or behavioral transition
   changes. Verification and remaining review are recorded in the change record.

   **Checks:** Two ordering tests and the Firefox expansion/collapse smoke test
   passed on 2026-10-18. The Sphinx build and traceability validation passed.
   Received, analyzed and fixed as a draft on that date. Full regression,
   owner review and release approval remain pending; requirement acceptance
   and complete verification are not implied by this fixed disposition.
