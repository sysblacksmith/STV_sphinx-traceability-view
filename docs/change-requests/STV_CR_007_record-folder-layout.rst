STV_CR_007: Record folder layout
================================

.. change_request:: STV_CR_007: Record folder layout
   :id: STV_CR_007
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_007_record-folder-layout.rst
   :priority: unassigned
   :verification_state: not_assessed

   .. rubric:: Owner request and provenance

   Date: 2026-10-24. Source: project owner prompt in this conversation.

   **Language-corrected owner prompt:**

   Rename the tests folder to test-scripts so it appears beside test-cases. Rename
   requirement-changes to change-requests and give its records distinct prefixes
   in original request order. Rename problems to problem-tickets and give those
   records clear prefixes too. Update all relations and references so the
   documentation still builds. Adapt the shared data model and skills in the historical tooling repository
   so new projects initialize this structure during stakeholder elicitation and
   create change-request files from the initial user prompts.

   .. rubric:: Implementation and historical mapping

   Executable Python sources are now under ``docs/test-scripts/``, adjacent to
   ``docs/test-cases/``. Current paths and selectors are updated. Canonical Need
   IDs, typed relations and requirement acceptance/verification states are retained.
   Shared scaffolds initialize all four indexes; request and ticket filenames use
   project prefixes. Request numbers follow the originating request sequence;
   records added in the same historical commit follow their documented workflow.
   The initial request remains explicitly reconstructed rather than quoted.

   This refactor changes paths, not Need identities or historical execution results.
   Archived execution logs, source hashes and selectors retain their original paths.
   Current test-case selectors and source evidence point to the relocated scripts.

   * ``tests/`` became ``docs/test-scripts/``.
   * ``docs/problems/problem_N.rst`` became
     ``docs/problem-tickets/STV_PR_NNN.rst``; adjacent images follow the same ID.

   * ``requirement-changes/initial-project-request`` became
     ``change-requests/STV_CR_001_initial-project-request``.
   * ``requirement-changes/starting-nodes`` became
     ``change-requests/STV_CR_002_starting-nodes``.
   * ``requirement-changes/usability-problems`` became
     ``change-requests/STV_CR_003_usability-problems``.
   * ``requirement-changes/problem-report-handover`` became
     ``change-requests/STV_CR_004_problem-report-handover``.
   * ``requirement-changes/control-order`` became
     ``change-requests/STV_CR_005_control-order``.
   * ``requirement-changes/centered-layout-and-interactive-seeds`` became
     ``change-requests/STV_CR_006_centered-layout-and-interactive-seeds``.


   .. rubric:: Checks

   * Relocated Python suite excluding browser tests: 33 passed.
   * Frontend Node suite: 18 passed.
   * Strict coverage: 67 requirements, 76 executable cases, no active gaps or
     unknown requirement IDs.
   * Shared validator regression suite: 18 passed.
   * Browser smoke checks: two setup errors before product interaction; Firefox
     closed unexpectedly or discarded its browsing context. No browser pass is
     claimed for this refactor.

   These checks do not update historical release results or verification states.



.. note::

   Publication copy: private tooling locations are omitted. The unchanged original
   is retained under engineering-history/pre-portable-method in the checkout.
