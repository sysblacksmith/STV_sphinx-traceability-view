.. _STV_ADR_005:

STV_ADR_005: Optional seed sets and paged project entry
================================================================================

Status: **accepted**. Date: 2026-10-18. Scope: software architecture.
Decision owner: project owner, through delegated concept review.
Supersedes: :ref:`STV_ADR_003` partially, for single-root initialization and
reachability assumptions. Superseded by: none. Its transactional engine,
semantic rank, viewport, inspection and later-mode isolation choices remain
applicable. This extends :ref:`STV_ADR_001` and :ref:`STV_ADR_002` without changing
their deployment or local-bundle decisions.

Related requirements: :need:`STV_SHR_047`, :need:`STV_SHR_048`,
:need:`STV_SYS_001`, :need:`STV_SWR_001`, :need:`STV_SWR_014`,
:need:`STV_SWR_025`, :need:`STV_SWR_043`, :need:`STV_SWR_051`, :need:`STV_SWR_052`.
Affected elements: :need:`STV_SWE_DIRECTIVE`, :need:`STV_SWE_MODEL`,
:need:`STV_SWE_GRAPH`, :need:`STV_SWE_STATE`, :need:`STV_SWE_LAYOUT`,
:need:`STV_SWE_RENDER`, :need:`STV_SWE_INSPECT`.

Context
---------

The accepted stakeholder amendment permits no seeds and multiple seeds.
Large stakeholder sets exceed the existing 200-node cap if opened together;
the owner selected paging of project-root links. The single-root visibility
assumption must therefore change while ordinary trace navigation remains intact.

Decision
----------

Use an optional whitespace-separated argument list. Deduplicate in first-seen
order; no IDs means project mode, invalid explicit IDs fail and more than 200
distinct explicit IDs fails before publication. Explicit mode has no artificial
root. Project mode derives its label from Sphinx project configuration and
entry types from the model's explicit stakeholder role. Represent its node and
edges with tagged synthetic identities outside the host Need graph.

Page sorted stakeholder IDs in fixed groups of 50, preserving independent
exploration state for each page. Keep inactive pages out of rooted visibility;
apply cap and layout checks before atomic page commit. Use one separate root
band above configured levels and no fabricated Need status/details/link.
Detailed parser, model, state, rendering and failure contracts are specified in
:doc:`../../internal-interfaces` and :doc:`../../implementation-plan`.

Rationale
-----------

The optional positional list preserves existing single-ID syntax. Fifty entries
leave capacity for 149 further nodes plus the project root. Paging makes every
stakeholder entry accessible without weakening the global cap; independent
page state avoids silently discarding exploration when readers change page.
Explicit roles preserve replacement-model semantics without hard-coded types.

Logical components and interfaces
----------------------------------

Reuse the existing DIRECTIVE/MODEL/GRAPH/BUNDLE build pipeline and
STATE/LAYOUT/RENDER/INSPECT runtime. Payload metadata grows; component
connections, packaging and selected dependency versions remain unchanged.
No new library, service, host schema type or authoritative relationship is added.

Consequences and constraints
-----------------------------

The root is not a Need and needs distinct rendering/inspection behavior.
Root-page edges do not alter authored backlinks or ordinary all-or-nothing
group expansion. Explicit seeds are never silently truncated. Paging may store
more expansion keys than are currently visible, but only the selected page
participates in layout/cap counting. This does not promise bounded total graph
memory or introduce numeric performance budgets.

Alternatives considered
-------------------------

Rejecting oversized root expansion was declined by the owner. Showing all
stakeholders would violate the cap. Treating the root as a fabricated Need
would pollute host identity/status/link semantics. Repeated directives or a
new multi-ID option add syntax without preserving the simple existing call.
