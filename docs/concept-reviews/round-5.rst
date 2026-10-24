Concept review round 5: centered-layout and seed-picker MVP
==========================================================================================

Authority and boundary
------------------------------------------------------------------------------------------

Date: 2026-10-18. Reviewer: Codex concept-review agent. The owner requested
clarification followed by autonomous concept/implementation work on an MVP for
inspection. This review supports that provisional implementation scope only;
it grants neither formal stakeholder/concept acceptance nor release approval.
The input is the uncommitted amendment after round 4 and the retained failed
``0.2.0-candidate-1``; historical round-4 identities are not rewritten.
Owner intent and exceptions are recorded in
:doc:`/change-requests/STV_CR_006_centered-layout-and-interactive-seeds`.

Assessed dependency neighborhood
------------------------------------------------------------------------------------------

Changed stakeholder drafts: :need:`STV_SHR_003`, :need:`STV_SHR_047`,
:need:`STV_SHR_052`, :need:`STV_SHR_053`. Software drafts:
:need:`STV_SWR_003`, :need:`STV_SWR_051`, :need:`STV_SWR_052`,
:need:`STV_SWR_056`, :need:`STV_SWR_057`. Retained constraints:
:need:`STV_SHR_002`, :need:`STV_SHR_025`, :need:`STV_SHR_034`,
:need:`STV_SHR_043`, :need:`STV_SHR_044`, :need:`STV_SHR_048`,
:need:`STV_SYS_001`, :need:`STV_SYS_008`, :need:`STV_SWR_038`,
:need:`STV_SWR_043`, :need:`STV_SWR_044`, :need:`STV_SWR_048`.
Existing owners remain :need:`STV_SWE_STATE`, :need:`STV_SWE_LAYOUT`,
:need:`STV_SWE_RENDER` within :need:`STV_SE_BROWSER`.

Reviewed contracts: :doc:`/internal-interfaces`, :doc:`/architecture-software`,
:doc:`/implementation-plan`, :doc:`/state-machine`,
:doc:`/verification-plan` and proposed :ref:`STV_ADR_006`, alongside the
unchanged boundaries of :ref:`STV_ADR_001` and :ref:`STV_ADR_002` and historical
initialization/page decisions in :ref:`STV_ADR_005`.

Semantic and feasibility review
------------------------------------------------------------------------------------------

Direct derivation of SWR 056/057 from SHR 052/053 is justified: horizontal
placement and per-view selection are browser-local refinements. No new system
obligation, host schema, dependency, runtime service or payload is introduced.
The original directive continues to validate author defaults; runtime selection
operates only on the already published non-hidden graph. System-level model,
distribution, visibility and capacity contracts remain applicable.

The open five-entry overview is an explicit exception to initial trace collapse;
ordinary traces remain closed. The synthetic project node still counts toward
capacity and has no Need status/details/link. Paging preserves independent page
memory, while explicit overview/reseed intentionally replaces it. Selection is
confirmed and transactional, with independent instance ownership, cap validation,
layout request tokens and failure preservation. ID/title suggestions cannot
expose host-hidden objects because filtering precedes graph serialization.

Centering uses semantic ranks rather than authored arrow direction. Processing
visible child spans, resolving competing positions, retaining shared nodes and
recomputing routes preserves the existing layout invariants. Exact centering is
conditional on collision constraints; cycles cannot recursively unfold through
this bounded geometry pass. Existing libraries and component boundaries suffice.

Disposition and remaining evidence
------------------------------------------------------------------------------------------

No unresolved essential design choice blocks the authorized prototype. The
draft design is suitable for implementation and focused verification under the
owner's existing MVP authority. Current Needs remain draft/not_assessed;
ADR 006 remains proposed and ADR 005's acceptance history is preserved.
Actual Node/browser checks and exported state-diagram visual/link checks are
recorded in :doc:`/change-requests/STV_CR_006_centered-layout-and-interactive-seeds`.
Owner inspection remains pending. Full release qualification, formal baseline
acceptance, tagging and publication remain outside this round's disposition.
