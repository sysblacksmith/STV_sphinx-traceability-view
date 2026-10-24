Inspect details from a nested Windows checkout
================================================================================

.. test_case:: Inspect details from a nested Windows checkout
   :id: STV_TC_WINDOWS_PATH
   :status: accepted
   :tags: known_issue
   :basis: documented
   :evidence: docs/problem-tickets/STV_PR_006.rst
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SHR_018, STV_SYS_003, STV_SYS_006, STV_SWR_015, STV_SWR_017, STV_SWR_018
   :last_result: not_run

   **Level/environment:** Windows browser system acceptance; stable Firefox
   with recorded version, direct file URLs and nested static HTTP hosting.
   This planned regression preserves :need:`STV_PR_006` and is not part of the
   currently implemented executable suite. No fresh result is inferred from
   the report's earlier diagnostic evidence.

   **Preconditions/inputs:** A nested checkout reproducing the report's old
   generated detail paths beyond 260 characters, an existing generated local
   detail asset and a requirement with published rich content. Include a root
   documentation page and a page below the output root. Record actual absolute
   asset-path lengths and browser/Windows versions. Preserve the old scheme's
   failure evidence before testing an authorized correction.

   **Procedure:** Build the exact candidate; open each page via file URL and
   activate the requirement's Details control by pointer and keyboard. Compare
   the displayed title, metadata and body with the original published object.
   Check script-load/network errors. Repeat from a nested static HTTP prefix.
   Remove one generated detail asset in an isolated fixture copy, activate its
   control, restore it and exercise retry. Inspect shared-fragment registration
   and graph references using two objects with identical detail fragments.

   **Expected outcomes:** Existing detail assets load and show the correct
   content in both transports and page depths, without the generic unavailable
   message or unexpected script-load errors. Identical fragments retain shared
   content identity and correct references. A genuinely missing asset produces
   the accessible unavailable indication; retry after restoration succeeds.
   Record the supported path boundary explicitly; do not claim arbitrary-depth
   Windows paths work merely because filenames were shortened.

   **Evidence:** Candidate/test identity, build and browser logs, measured path
   lengths, before/after screenshots and the retained missing-asset/retry result.
   Product correction and executable implementation remain outside the current
   documentation-only increment. ``not_run`` is a known qualification gap.
