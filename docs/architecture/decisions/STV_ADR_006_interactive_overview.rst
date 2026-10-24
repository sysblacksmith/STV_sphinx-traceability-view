.. _STV_ADR_006:

STV_ADR_006: Centered layout and interactive overview
==========================================================================================

Status: **accepted**. Date: 2026-10-18. Scope: software architecture.
Decision owner: project owner through delegated concept review; see
:doc:`../../concept-reviews/round-6`.
Supersedes: partially
:ref:`STV_ADR_005` for page size, initial root expansion and runtime seed
mutability. Superseded by: none.

Related requirements: :need:`STV_SHR_003`, :need:`STV_SHR_047`,
:need:`STV_SHR_052`, :need:`STV_SHR_053`, :need:`STV_SWR_003`,
:need:`STV_SWR_051`, :need:`STV_SWR_052`, :need:`STV_SWR_056`,
:need:`STV_SWR_057`. Affected elements: :need:`STV_SWE_LAYOUT`,
:need:`STV_SWE_STATE`, :need:`STV_SWE_RENDER`.

Context
------------------------------------------------------------------------------------------

The owner requested an inspectable MVP with centered parents, five-item
overview pages and runtime seed selection. Existing graph data already carries
all published IDs/titles; component boundaries and offline delivery suffice.

Decision
------------------------------------------------------------------------------------------

Initialize project mode with its first page of five entries open. Keep ordinary
trace expansion collapsed and preserve independent page exploration on paging.
Use a per-view local picker over the immutable published graph; a confirmed
exact ID replaces that view's seeds and exploration after capacity/layout
validation. Project overview explicitly starts a fresh first-page overview.
Keep author-supplied multi-seed syntax and source validation unchanged.

After ELK ordering and semantic projection, move parent boxes toward the
midpoint of visible lower-level child spans. Resolve same-band collisions
deterministically before recomputing test lanes and final routes. Interpret
parent/child by semantic rank, independent of edge authorship. Ignore same-rank
and test-role connections for centering; keep shared children single nodes.

Rationale
------------------------------------------------------------------------------------------

Five entries provide immediate useful content and leave capacity for exploration.
Local search reuses authoritative published data without a new backend or
rebuild. Transactional replacement preserves the committed view on errors.
Collision constraints preserve readability where exact centering is impossible.

Consequences and constraints
------------------------------------------------------------------------------------------

Selection discards only its view's prior exploration; it does not edit Needs,
RST defaults or another instance. Search suggestions may be bounded with total
match information; direct exact-ID entry remains possible. This decision replaces ADR 005's page size, initial root expansion and
runtime seed immutability choices; its unaffected decisions remain applicable.

Alternatives considered
------------------------------------------------------------------------------------------

Viewport-centered parents ignore child geometry. Duplicating shared children
breaks shared identity. Adding a selected seed preserves unrelated exploration
against the confirmed replacement intent. Rebuilding RST for every selection
does not provide the requested reader workflow. None is selected.

Verification and handover
------------------------------------------------------------------------------------------

Use focused geometry/state and Firefox file/HTTP cases from
:doc:`../../verification-plan`. Concept acceptance is recorded in :doc:`../../concept-reviews/round-6`.
Full release qualification remains separate; see
:doc:`../../change-requests/STV_CR_006_centered-layout-and-interactive-seeds`.
