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

   Registers the extension, parses directives, records source locations, resolves optional seed lists, validates initial capacity and handles package compatibility. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

   **Component directory:** ``src/sphinx_traceability_view/directive``. The folder name is the
   lowercase suffix of ``STV_SWE_DIRECTIVE``.

   **Implementation:** ``lifecycle.py``; ``directives.py``; ``__init__.py``.

   The public setup/version shims in ``src/sphinx_traceability_view/__init__.py``
   and ``src/sphinx_traceability_view/_version.py`` belong to this component.

   **Unit tests:** ``tests/test_lifecycle.py``.

   **Boundary:** ``README.rst``.

.. swe:: Host model normalization
   :id: STV_SWE_MODEL
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Validates supplemental mappings against host definitions; resolves colors, labels, acceptance values and stakeholder entry roles. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

   **Component directory:** ``src/sphinx_traceability_view/model``. The folder name is the
   lowercase suffix of ``STV_SWE_MODEL``.

   **Implementation:** ``__init__.py``.

   **Unit tests:** ``tests/test_model.py``.

   **Boundary:** ``README.rst``.

.. swe:: Graph adapter and indexes
   :id: STV_SWE_GRAPH
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Reads the completed Needs collection and constructs canonical objects, links, incoming/outgoing indexes, missing-target records and project-name/stakeholder entry metadata. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

   **Component directory:** ``src/sphinx_traceability_view/graph``. The folder name is the
   lowercase suffix of ``STV_SWE_GRAPH``.

   **Implementation:** ``__init__.py``.

   **Unit tests:** ``tests/test_graph.py``.

   **Boundary:** ``README.rst``.

.. swe:: Rendered detail extraction
   :id: STV_SWE_DETAIL_BUILD
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Uses Beautiful Soup 4.13.5 with html.parser to capture full host-rendered Need HTML, adjusts portable links/assets and isolates fragments for overlay use. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

   **Component directory:** ``src/sphinx_traceability_view/detail_build``. The folder name is the
   lowercase suffix of ``STV_SWE_DETAIL_BUILD``.

   **Implementation:** ``__init__.py``.

   **Unit tests:** ``tests/test_details.py``.

   **Boundary:** ``README.rst``.

.. swe:: Static bundle emission
   :id: STV_SWE_BUNDLE
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BUILD

   Packages esbuild-built local runtime assets and writes deterministic graph manifests, lazy per-object detail scripts and packaged runtime assets with relative output paths and rebuild dependencies. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

   **Component directory:** ``src/sphinx_traceability_view/bundle``. The folder name is the
   lowercase suffix of ``STV_SWE_BUNDLE``.

   **Implementation:** ``__init__.py``.

   **Unit tests:** ``tests/test_bundle.py``.

   **Boundary:** ``README.rst``.

   Maintainer delivery helpers ``frontend/build.js`` and ``frontend/legal/``
   own audited npm/compiled-library notices and generated package assets for
   this delivery boundary; they introduce no additional runtime element.

.. swe:: Exploration state engine
   :id: STV_SWE_STATE
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Pure transition and visibility logic; immutable input graph, independent view state, capacity checks, persistent seed sets, independent project-page exploration and later occurrence projection. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

   **Component directory:** ``frontend/src/state``. The folder name is the
   lowercase suffix of ``STV_SWE_STATE``.

   **Implementation:** ``state.js``.

   **Unit tests:** ``tests/state.test.js``.

   **Boundary:** ``README.rst``.

.. swe:: Semantic rank layout
   :id: STV_SWE_LAYOUT
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Uses ELK.js 0.10.0 for ordering suggestions then STV projection to rank by model levels with a separate synthetic project-root band, places tests to the right and routes edges including cycles without changing semantic graph data. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

   **Component directory:** ``frontend/src/layout``. The folder name is the
   lowercase suffix of ``STV_SWE_LAYOUT``.

   **Implementation:** ``layout.js``; ``stability.js``.

   Owns fresh placement and committed-slot stabilization; see :ref:`STV_ADR_008`.

   **Unit tests:** ``tests/layout.test.js``; ``tests/stability.test.js``.

   **Boundary:** ``README.rst``.

.. swe:: Accessible view and viewport
   :id: STV_SWE_RENDER
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Renders SVG connections and HTML controls/nodes, owns project-root presentation/paging, relationship-control ordering, focus, keyboard operation, status styling and D3 zoom 3.0.0/selection 3.0.0 for view-local pan/zoom. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

   **Component directory:** ``frontend/src/render``. The folder name is the
   lowercase suffix of ``STV_SWE_RENDER``.

   **Implementation:** ``index.js``; ``view.js``; ``groups.js``; ``seeds.js``; ``edge-viewport.js``; ``stv.css``.

   **Unit tests:** ``tests/groups.test.js``; ``tests/seeds.test.js``; ``tests/edge-viewport.test.js``.

   **Boundary:** ``README.rst``.

.. swe:: Detail overlay and original links
   :id: STV_SWE_INSPECT
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :part_of: STV_SE_BROWSER

   Uses Floating UI DOM 1.7.4 to position final rendered fragments in bounded scrollable overlays and retains original-object new-tab links for real Needs, excluding artificial project roots. See :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003` and :ref:`STV_ADR_004`.

   **Component directory:** ``frontend/src/inspect``. The folder name is the
   lowercase suffix of ``STV_SWE_INSPECT``.

   **Implementation:** ``inspect.js``.

   **Unit tests:** ``tests/inspect.test.js``.

   **Boundary:** ``README.rst``.
