Problem 7: Authored detail transport attributes bypass resource policy
======================================================================

.. problem_report:: Authored detail transport attributes bypass resource policy
   :id: STV_PR_007
   :status: fixed
   :basis: observed
   :evidence: docs/problem-tickets/STV_PR_007.rst
   :priority: unassigned
   :verification_state: partial

   **Source and authority:** Public-release audit finding PRSA-002, 2026-10-24.
   The owner requested verification of removed GitHub releases, followed by a
   fix for this finding. Further findings require individual proposal approval.
   Baseline: ``4b1199e`` plus the separately approved audit-output ignore rule.

   **Observed/expected:** An inert authored ``data-stv-href`` containing a
   JavaScript URL became an executable link when the detail inspector restored
   it; an inert authored ``data-stv-src`` became an automatic resource request.
   The audit reproduced a harmless browser marker and loopback request. Copied
   details must preserve static rich content without activating these values.
   This requires control of authored Need HTML; it is not evidence of an
   unauthenticated remote injection path.

   **Cause:** The extractor sanitized ordinary attributes but trusted the
   reserved transport namespace. The browser restored markers without applying
   the local-resource policy. Affected components: :need:`STV_SWE_DETAIL_BUILD`
   and :need:`STV_SWE_INSPECT`; existing obligations :need:`STV_SWR_015`,
   :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_049`.

   **Implementation:** Strip authored transport markers before generating fresh
   ones. Independently validate restored URLs, srcset and CSS in the inspector.
   Rebuild the shipped browser bundle. See :doc:`../internal-interfaces` for
   the reserved namespace and resource contract. No requirement meaning,
   architecture allocation or state-machine transition changes.

   **Regression and review:** :doc:`../test-execution/prsa-002-fix/index`
   records actual commands, outcomes and verification limits. New tests and
   the refined interface contract await owner review; implementation authority
   does not imply concept acceptance or release qualification.

   **Disposition:** Fixed with scoped regression verification: 33 cases passed.
   Owner review of the interface refinement and new test designs remains pending;
   full release qualification remains separate. See the linked execution record.
