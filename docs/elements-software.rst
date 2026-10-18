Software elements
=================

Software module responsibilities and containment within the product system elements.

.. swe:: Extension lifecycle and directives
   :id: STV_SWE_DIRECTIVE
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Registers the extension, parses directives, records source locations, resolves optional seed lists, validates initial capacity and handles package compatibility. Source: src/sphinx_traceability_view/__init__.py and directives.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

.. swe:: Host model normalization
   :id: STV_SWE_MODEL
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Validates supplemental mappings against host definitions; resolves colors, labels, acceptance values and stakeholder entry roles. Source: model.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

.. swe:: Graph adapter and indexes
   :id: STV_SWE_GRAPH
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Reads the completed Needs collection and constructs canonical objects, links, incoming/outgoing indexes, missing-target records and project-name/stakeholder entry metadata. Source: graph.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

.. swe:: Rendered detail extraction
   :id: STV_SWE_DETAIL_BUILD
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Uses Beautiful Soup 4.13.5 with html.parser to capture full host-rendered Need HTML, adjusts portable links/assets and isolates fragments for overlay use. Source: details.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

.. swe:: Static bundle emission
   :id: STV_SWE_BUNDLE
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Packages esbuild-built local runtime assets and writes deterministic graph manifests, lazy per-object detail scripts and packaged runtime assets with relative output paths and rebuild dependencies. Source: bundle.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

.. swe:: Exploration state engine
   :id: STV_SWE_STATE
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Pure transition and visibility logic; immutable input graph, independent view state, capacity checks, persistent seed sets, independent project-page exploration and later occurrence projection. Source: frontend/src/state.js. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

.. swe:: Semantic rank layout
   :id: STV_SWE_LAYOUT
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Uses ELK.js 0.10.0 for ordering suggestions then STV projection to rank by model levels with a separate synthetic project-root band, places tests to the right and routes edges including cycles without changing semantic graph data. Source: frontend/src/layout.js. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

.. swe:: Accessible view and viewport
   :id: STV_SWE_RENDER
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Renders SVG connections and HTML controls/nodes, owns project-root presentation/paging, focus, keyboard operation, status styling and D3 zoom 3.0.0/selection 3.0.0 for view-local pan/zoom. Source: frontend/src/view.js and packaged static/stv.css. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

.. swe:: Detail overlay and original links
   :id: STV_SWE_INSPECT
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Uses Floating UI DOM 1.7.4 to position final rendered fragments in bounded scrollable overlays and retains original-object new-tab links for real Needs, excluding artificial project roots. Source: frontend/src/inspect.js. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.
