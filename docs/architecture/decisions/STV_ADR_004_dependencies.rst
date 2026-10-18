.. _STV_ADR_004:

STV_ADR_004: Concrete dependency and delivery stack
=======================================================

Status: **proposed**. Date: 2026-10-18. Scope: solution/software architecture.
Decision owner: project owner; acceptance evidence: none yet.
Supersedes: none. Superseded by: none. This refines the still-proposed
:ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

Related requirements: :need:`STV_SYS_003`, :need:`STV_SYS_005`,
:need:`STV_SYS_006`, :need:`STV_SYS_009`, :need:`STV_SWR_015`,
:need:`STV_SWR_033`, :need:`STV_SWR_039`, :need:`STV_SWR_040`.
Affected elements: :need:`STV_SWE_DETAIL_BUILD`, :need:`STV_SWE_BUNDLE`,
:need:`STV_SWE_LAYOUT`, :need:`STV_SWE_RENDER`, :need:`STV_SWE_INSPECT`.

Context
-----------

The owner requested an implementation-ready concept after finding the initial
proposal insufficiently specific about external libraries and tools. The
accepted baseline requires semantic levels, cycles, native keyboard interaction,
full rendered details, offline file URLs and installed Firefox on Windows.
The initial custom-layout proposal lacked a technology comparison.

Decision
------------

Select ELK.js 0.10.0 for ordering suggestions, D3 zoom 3.0.0 and selection 3.0.0
for viewport interactions, Floating UI DOM 1.7.4 for panel placement and
Beautiful Soup 4.13.5 with html.parser for final rendered Need extraction.
STV owns semantic projection, state, final edge routing, accessible controls
and panel lifecycle. Library algorithms do not replace domain requirements.

Use esbuild 0.25.12 to create a bundled IIFE without runtime workers or module
requests, Hatchling 1.27.0/build 1.3.0 to package prebuilt assets, pytest 8.4.2
and Node's native test runner for unit/integration checks, and Selenium 4.35.0
with release Firefox/geckodriver for browser verification. Exact browser/driver
versions are recorded per release rather than declared permanently supported.

Detailed roles, licenses, selected manifests and sources are in
:doc:`../../technology-stack`; implementation contracts are in
:doc:`../../implementation-plan` and :doc:`../../verification-plan`.

Rationale
-------------

Existing libraries handle general graph ordering, viewport gestures, overlay
geometry and HTML parsing. STV keeps semantic constraints and accessible DOM
interactions explicit. This avoids replacing the hard hierarchy with force
layout or treating a canvas graph as automatically keyboard accessible.
Selenium verifies the installed release Firefox rather than a patched browser.

Logical components and interfaces
-------------------------------------

Beautiful Soup is confined to :need:`STV_SWE_DETAIL_BUILD`. ELK is isolated by
the :need:`STV_SWE_LAYOUT` adapter. D3 belongs to :need:`STV_SWE_RENDER` and
Floating UI to :need:`STV_SWE_INSPECT`. Browser libraries are built into the
wheel's local assets through :need:`STV_SWE_BUNDLE`. Host projects require
Python dependencies only; Node remains a maintainer tool.

Consequences and constraints
--------------------------------

ELK's y coordinates and routes cannot be trusted after semantic projection;
STV recomputes them under its hard constraints. The measured minified library
bundle is approximately 1.5 MB, before graph data. Full Need bodies load from
local per-object scripts on demand. Include dependency notices and the selected
ELK source/license redistribution materials. Python transitive hashes are
captured when assembling the first implementation environment.

Alternatives considered
---------------------------

* Entirely custom graph ordering: not selected because a general solver already
  provides useful ordering and cycle handling; only domain constraints remain custom.
* ELK output used unchanged: rejected because topology-derived layers do not
  guarantee semantic hierarchy or right-side test placement.
* Cytoscape/canvas-first rendering: not selected because HTML controls and rich
  details would still require an accessible DOM representation and synchronization.
* React: not selected; the isolated views do not need a framework lifecycle.
* Playwright Firefox for release verification: not selected because it uses a
  patched Firefox rather than the required installed release browser.
* lxml: not selected; html.parser meets the initial extraction use case without
  a native parser dependency.

Open design questions
-------------------------

No library selection is left open for MVP implementation. Validation tasks
remain: real browser execution, final geometry, incremental-build coherence
and the measured large-project cost. External objects without local full rendering use the owner-confirmed
metadata/link fallback. Hidden objects and incident links are excluded by owner decision. Static widget content is sufficient for MVP details; widget-specific
JavaScript remains on the original page by owner agreement;
they must not be reported as full offline-detail parity without evidence.
Owner: implementation team; release exceptions require project-owner review.

Decision history
--------------------

2026-10-18: Proposed concrete versions, boundaries and verification plan in
response to the owner's implementation-ready concept request. Verified npm
resolution, cyclic ELK layout and IIFE bundling in a temporary environment;
these smoke checks do not establish product acceptance.

2026-10-18: Owner confirmed external metadata/link fallback without downloading
or caching pages as sufficient for the MVP. Other decisions remain proposed.

2026-10-18: Owner confirmed host-hidden Need exclusion and hidden-seed
rejection; filtering precedes published graph/detail generation.

2026-10-18: Owner confirmed static third-party widget content as sufficient
for MVP details, deferring widget-specific JavaScript behavior.

2026-10-18: Owner deferred project license selection and agreed to set
performance budgets after first MVP measurements. No numeric budget or project
license is assigned; library decisions remain proposed.
