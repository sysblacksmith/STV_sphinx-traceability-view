.. _STV_ADR_003:

STV_ADR_003: Transactional exploration and semantic rank layout
===============================================================

Status: **accepted**. Date: 2026-10-18. Scope: software architecture.
Decision owner: project owner.
Supersedes: none. Superseded by: none.

Related specifications and elements: :need:`STV_SYS_005`, :need:`STV_SYS_007`, :need:`STV_SYS_008`, :need:`STV_SWR_024`, :need:`STV_SWR_034`.

Context
-------

Exploration must handle cycles, shared nodes, independent views, a hard node cap and semantic ranks independent of the seed.

Decision
--------

Propose a pure state transition engine, seed-rooted reachability, pre-commit cap checks, ELK ordering followed by STV semantic rank projection/final routing, D3 viewport controls, Floating UI detail positioning and HTML controls over SVG edges. Use shared identity initially and add path occurrences later.

Rationale
---------

Separating state, geometry and presentation makes cap and reachability rules directly testable. HTML controls support keyboard access; custom layout still needs geometry and usability validation.

Logical components and interfaces
---------------------------------

:need:`STV_SWE_STATE` emits visible graph data to :need:`STV_SWE_LAYOUT`; :need:`STV_SWE_RENDER` handles controls and viewport while :need:`STV_SWE_INSPECT` handles details.

Consequences and constraints
----------------------------

No persistence across reloads is proposed. Zoom/pan remain view-local. A two-line title clamp is an internal fixed presentation choice. Later-mode state edits still need a reviewed policy.

Alternatives considered
-----------------------

A naive tree recursively duplicates cycles and obscures shared dependencies. A generic force layout does not guarantee semantic levels. ELK.js is selected for ordering; authoritative rank and test constraints remain in STV. Dependency trade-offs are recorded in :ref:`STV_ADR_004`.
