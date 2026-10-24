.. _STV_CR_001:

Initial project request: traceability exploration
=================================================

.. change_request:: Initial project request: traceability exploration
   :id: STV_CR_001
   :status: implemented
   :basis: documented
   :evidence: docs/change-requests/STV_CR_001_initial-project-request.rst
   :priority: unassigned
   :verification_state: not_assessed

   .. rubric:: Origin and provenance

   Original request date: 2026-10-18, as recorded in :doc:`../sources`.
   This retrospective record was created on 2026-10-24 at the owner's request.
   It records the project-starting need, not an amendment to an existing baseline.

   The full original prompt is unavailable in the conversation context used to
   create this record. The following is a reconstruction from the initial source
   register and its derived stakeholder requirements, not an exact quotation or
   a recovered transcript. Spelling and grammar are normalized. The original
   prompt is still needed to confirm its wording and scope. Later clarifications
   are not attributed to the initial request.

   .. rubric:: Reconstructed initial request

   Provide an interactive traceability view embedded in an RST page, starting
   from a specified Sphinx-Needs object ID. Initially show the starting object
   with its traced relationships collapsed. Offer a plus-sign control for each
   relationship type to reveal related objects, allow further exploration from
   those objects, and allow opened relationships to be collapsed again. Readers
   should be able to inspect objects discovered during exploration.

   Preserve the artifact hierarchy: stakeholder requirements above system
   requirements, system architecture between system and software requirements,
   and software architecture below software requirements. Display related test
   cases to the right of their associated artifacts.

   .. rubric:: Traceability and subsequent changes

   The initial interpretation is represented by :need:`STV_SHR_001`,
   :need:`STV_SHR_002`, :need:`STV_SHR_003`, :need:`STV_SHR_004`,
   :need:`STV_SHR_005`, :need:`STV_SHR_006`, :need:`STV_SHR_007`,
   :need:`STV_SHR_008`, :need:`STV_SHR_009`, :need:`STV_SHR_010`,
   :need:`STV_SHR_011` and :need:`STV_SHR_012`. These canonical records include
   later refinements; they are not a verbatim copy of the first prompt.

   Later clarifications are recorded in :doc:`../sources`; starting-node changes
   are recorded in :doc:`STV_CR_002_starting-nodes`. Current acceptance and verification
   remain in :doc:`../maturity`. This record changes no requirements or statuses.
