.. _STV_CR_010:

STV_CR_010: Consolidate system and software test specifications
===============================================================

.. change_request:: STV_CR_010: Consolidate system and software test specifications
   :id: STV_CR_010
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_010_consolidated-test-specifications.rst
   :priority: unassigned
   :verification_state: not_assessed

   .. rubric:: Owner request and provenance

   Date: 2026-10-24. Source: project owner prompt in this conversation.

   **Language-corrected owner request:** Consolidate the test specifications into
   one system-test document and one software-test document, adapt the shared
   agents guidance accordingly, and provide commit messages for both repositories.

   .. rubric:: Organization and preserved semantics

   :doc:`../test-cases/system-tests` contains the 45 system cases;
   :doc:`../test-cases/software-tests` contains the 38 software cases. Each case
   remains a separate ``test_case`` Need with its existing ID, content, review
   state, requirement links, latest result and execution links. Only the file
   organization changes. Canonical links should target Need IDs, not an
   individual source filename. Archived execution records and review identities
   remain historical.

   This supersedes the per-case-file packaging introduced in
   :doc:`STV_CR_009_requirement-filenames-and-test-levels`, retaining its test-level
   classification. Case source paths now use ``test-cases/system-tests.rst`` or
   ``test-cases/software-tests.rst`` with the canonical case ID as section evidence.
   This consolidation does not change executable tests or verification claims.

   .. rubric:: Validation

   The before/after exported Needs comparison confirms unchanged contents and
   canonical metadata for all 83 cases, including requirement/execution links,
   review status, latest result and verification state. Counts remain 45 system
   and 38 software cases. Sphinx warnings-as-errors, shared traceability with
   required test coverage, all eight skill validators and whitespace checks pass.
   Executable procedures are unchanged; this is not a new runtime test execution.
