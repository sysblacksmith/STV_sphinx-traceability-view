Software elements
=================

All source mappings below are proposed file responsibilities, not existing code
evidence. Containment follows the two product system elements.

.. swe:: Extension lifecycle and directives
   :id: STV_SWE_DIRECTIVE
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Registers the extension, parses directives, records source locations, resolves seeds and handles package compatibility. Proposed source: src/sphinx_traceability_view/__init__.py and directives.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

.. swe:: Host model normalization
   :id: STV_SWE_MODEL
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Validates supplemental mappings against host definitions; resolves colors, labels and acceptance values. Proposed source: model.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

.. swe:: Graph adapter and indexes
   :id: STV_SWE_GRAPH
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Reads the completed Needs collection and constructs canonical objects, links, incoming/outgoing indexes and missing-target records. Proposed source: graph.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

.. swe:: Rendered detail extraction
   :id: STV_SWE_DETAIL_BUILD
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Captures full host-rendered Need HTML, adjusts portable links/assets and isolates fragments for overlay use. Proposed source: details.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

.. swe:: Static bundle emission
   :id: STV_SWE_BUNDLE
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Writes deterministic local data scripts, details and packaged runtime assets with relative output paths and rebuild dependencies. Proposed source: bundle.py. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

.. swe:: Exploration state engine
   :id: STV_SWE_STATE
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Pure transition and visibility logic; immutable input graph, independent view state, capacity checks and later occurrence projection. Proposed source: static/state.js. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

.. swe:: Semantic rank layout
   :id: STV_SWE_LAYOUT
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Ranks by model levels, places tests to the right and routes edges including cycles without changing semantic graph data. Proposed source: static/layout.js. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

.. swe:: Accessible view and viewport
   :id: STV_SWE_RENDER
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Renders SVG connections and HTML controls/nodes, owns focus, keyboard operation, status styling and view-local pan/zoom. Proposed source: static/view.js and view.css. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

.. swe:: Detail overlay and original links
   :id: STV_SWE_INSPECT
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Displays final rendered fragments in bounded scrollable overlays and retains original-object new-tab links. Proposed source: static/inspect.js. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.

