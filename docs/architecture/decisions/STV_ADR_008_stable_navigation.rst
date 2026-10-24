.. _STV_ADR_008:

STV_ADR_008: Stable navigation after fresh placement
============================================================

Status: **accepted**. Date: 2026-10-24. Scope: browser layout and rendering.
Decision owner: project owner through the scoped review recorded in
:doc:`../../concept-reviews/round-9`.
Supersedes: partially :ref:`STV_ADR_006` for repeated parent recentering on
relationship/root toggles. Superseded by: partially :ref:`STV_ADR_009`
for classified test evidence; legacy-role and navigation decisions remain.

Context and requirement paths
-------------------------------------

The owner approved the :need:`STV_PR_013` prototype after correcting Firefox
arrow clipping and initial ID order. Reapplying collision-aware centering after
every toggle moves the activated node and its peers. The refined centering
scope is :need:`STV_SHR_052` / :need:`STV_SWR_056`; stable navigation is
:need:`STV_SHR_054` / :need:`STV_SWR_058` / :need:`STV_SWR_059`, and fresh
numeric ordering is :need:`STV_SHR_055` / :need:`STV_SWR_060`.
Owners remain :need:`STV_SWE_LAYOUT` and :need:`STV_SWE_RENDER`.

Decision and algorithm
------------------------------

Keep ELK.js 0.10.0 as an ordering proposal, semantic bands and custom safe
routing. Fresh initialization/seed/overview/page scenes use collision-aware
parent centering; edge-free ordinary rows use full-ID natural numeric ordering.
For group/root commands pass previous committed geometry and the activated key
into layout. Preserve surviving ordinary horizontal slots, anchor its band,
allocate new slots near fresh proposals translated toward the anchor and retain
surviving test-lane x. Preserve same-rank test offsets; append newcomers and
reranked shared tests, then make vertical room above/below the clicked band.
The complete deterministic constants and exceptions are in
:doc:`../../internal-interfaces` and :doc:`../../implementation-plan`.

Recompute and validate all routes after final placement. Negative x/y are valid;
the renderer covers every route/node with padded SVG bounds and matches the CSS
origin to its viewBox. Commit geometry only with the current request's accepted
scene. Failures/stale completions retain the last committed state and geometry.
Reset viewport fits committed node bounds without relayout; restore focus with
preventScroll. Geometry is per-view transient state, never serialized into Needs.

Alternatives and consequences
-------------------------------------

ELK incremental hints alone cannot enforce the semantic/test-lane invariants.
Translating the entire recomputed graph preserves only one anchor and still moves
its peers. Keeping every old x/y unconditionally cannot accommodate taller bands
or reranked shared tests. Recenter-on-every-toggle reproduces the reported defect.
The selected projection deliberately sacrifices renewed exact centering and can
leave gaps after collapse; fresh navigation starts compact the scene. No manual
dragging, persistent saved layout, optimal crossings or arbitrary rank changes
of ordinary Needs are introduced. The separate artifact vertical-target CR is
outside this decision. No dependency, component boundary, schema or event transition changes. The
software view depicts the geometry feedback; the state view names stable slots.

Verification and handover
---------------------------------

Use :need:`STV_TC_SW_043`, :need:`STV_TC_SW_044`, :need:`STV_TC_SW_045`,
:need:`STV_TC_SY_058`, :need:`STV_TC_SY_059`, :need:`STV_TC_SY_060` and
existing fresh-centering/transactional/viewport cases. Review test designs before
execution. Development evidence belongs to
:doc:`../../test-execution/pr013-final/index`; a new release requires separate
owner instruction and complete release qualification.
