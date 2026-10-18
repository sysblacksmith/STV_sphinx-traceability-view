Implementation concept and handover
=======================================

This page fixes the MVP implementation approach. Start implementation from the
accepted stakeholder baseline, draft internal specification and the concrete
choices in :doc:`technology-stack`. No additional library-selection phase is
needed. ADRs remain proposed until reviewed; runtime acceptance is a later gate.

Product boundary and source layout
--------------------------------------

The distribution is ``sphinx-traceability-view`` with import name
``sphinx_traceability_view``. Build a wheel for installation in other projects;
registry publication is outside the implementation task. Initial builder
support is Sphinx's ``html`` builder. Fail clearly if a view is used with an
unsupported builder rather than silently producing an empty view.

Create the following product files; these are responsibilities, not existing
implementation claims::

   pyproject.toml                       # Hatchling; includes built assets
   src/sphinx_traceability_view/
       __init__.py                     # setup, dependency and hook registration
       directives.py                   # placeholder node and RST directive
       model.py                        # normalized supplemental host model
       graph.py                        # pinned NeedsView adapter and adjacency
       details.py                      # Beautiful Soup final-HTML extraction
       bundle.py                       # stable data/detail scripts and manifest
       static/stv.js                   # generated IIFE, included in wheel/sdist
       static/stv.css                  # scoped styles
       static/THIRD_PARTY_NOTICES.txt
   frontend/
       package.json                    # copy selected architecture manifest
       package-lock.json               # copy verified lock
       build.js                        # esbuild plus notice generation
       src/state.js                    # pure graph commands and reachability
       src/layout.js                   # ELK adapter plus semantic projection
       src/view.js                     # HTML controls, SVG edges and D3 zoom
       src/inspect.js                  # Floating UI and accessible detail panel
       src/index.js                    # bundle registry and instance startup
       test/*.test.js                  # Node's built-in test runner
   tests/
       test_model.py
       test_graph.py
       test_details.py
       test_build.py
       test_browser.py
       fixtures/minimal/               # actual Sphinx host project
       fixtures/alternate_model/
       fixtures/broken_links/
       fixtures/rich_details/

Use JavaScript modules with JSDoc types in source, compiled to a classic IIFE
for the browser. No TypeScript compiler or frontend framework is needed.
Do not load ``frontend/`` or ``node_modules`` from generated documentation.

The initial pyproject contract is ``requires-python = '>=3.10'`` with runtime
dependencies ``Sphinx==8.1.3``, ``sphinx-needs==8.2.0`` and
``beautifulsoup4==4.13.5``. Use ``hatchling.build`` with
``hatchling==1.27.0`` in build-system.requires. Include the
``src/sphinx_traceability_view`` package, prebuilt static files and required
third-party redistribution materials in wheel/sdist. The maintainer release
command builds JS before invoking ``python -m build``; ordinary Python package
builds consume those checked/package-ready artifacts and fail if they are
missing. Runtime distribution metadata must not require pytest, Selenium,
Node, esbuild or Draw.io.

Component interfaces
------------------------

Implement these seams so host/version adaptation and browser libraries remain
replaceable without a second application-state implementation:

.. list-table:: Module contracts
   :header-rows: 1
   :widths: 22 40 38

   * - Component
     - Input
     - Output / error contract
   * - model.normalize
     - Host type/link definitions and supplemental mapping
     - Immutable normalized model or entry-located model error.
   * - graph.snapshot
     - Resolved NeedsView, model and builder URI resolver
     - Objects, canonical edges and two directional indexes; missing targets retained.
   * - details.extract
     - Final output pages and object locations
     - Rendered fragments plus portable resource/anchor references; explicit unavailable-body records.
   * - bundle.emit
     - Snapshot, fragments, packaged assets and output root
     - Coherent graph/detail scripts and versioned manifest; no partially published manifest.
   * - state.transition
     - Immutable graph, current state and structured command
     - Candidate visible graph/new state or unchanged state with diagnostic.
   * - layout.compute
     - Candidate visible graph, normalized ranks and measured boxes
     - Promise of final boxes, edge polylines and bounds; stale revision results discarded.
   * - view.render
     - Root, committed state, geometry and command dispatcher
     - Updated semantic DOM/SVG with retained focus; no graph mutation.
   * - inspect.open / close
     - Need ID, trigger, view identity and detail-loader promise
     - Local rendered panel, Floating UI cleanup and keyboard focus restoration.

Sphinx lifecycle contract
-----------------------------

``setup(app)`` calls ``app.setup_extension('sphinx_needs')``, registers the
directive/node and ``traceability_view_model`` with rebuild scope ``env``.
Advertise ``parallel_read_safe=False`` and ``parallel_write_safe=False`` for
the initial release; parallel support is not assumed from serialized data.

1. **builder-inited:** Validate the HTML builder, arrange local JS/CSS assets
   and reset transient build data. The directive records invocations as plain
   serializable values in the environment; its HTML visitor emits the view root
   with seed and instance attributes, never the full graph.
2. **env-purge-doc:** Remove invocations belonging to a reread/deleted document.
   **env-get-outdated:** conservatively return all existing documents for MVP
   builds with views. This deliberately favors coherent final fragments over
   fine-grained caching. No-op builds still regenerate bundle manifests.
3. **write-started, priority 800:** Read
   ``SphinxNeedsData(app.env).get_needs_view()`` after host postprocessing
   (registered at the default priority in installed 8.2.0). Normalize the
   host model, resolve seeds across documents, construct canonical graph and
   incoming indexes. Use ``builder.get_target_uri(docname)`` and original
   anchors for original-object locations. Validate before any view is emitted.
4. **html-page-context:** Include graph and runtime scripts only on pages with
   view roots, using relative builder URLs. Detail fragments have per-object
   script URLs from the manifest. Scripts are classic scripts with ordered
   loading, never ES modules or runtime fetch requests.
5. **build-finished, priority 900:** Parse final HTML pages listed by the graph,
   produce detail fragments and bundle files, even when host dangling-link
   warnings made the final exit code nonzero, provided final pages exist.
   On a fatal earlier exception, leave it intact and do not claim a valid new
   bundle. Host data locks are released at priority 9999 in pinned 8.2.0.
   STV must not suppress host diagnostics or replace their failure status.

Build output is not published until Sphinx exits. Thus pages can reference
files emitted at build-finished without a runtime race in the finished bundle.
Write outputs through sibling temporary files and rename only when complete.
Regenerate graph and detail manifests together to prevent stale seed/link data.
Keep output paths under the builder output root; never delete unrelated files.

Final rendered details and offline loading
----------------------------------------------

Parse each distinct original output page once with
``BeautifulSoup(html, 'html.parser')``. Locate the exact element by Need ID,
not a CSS selector assembled from an unescaped ID, and retain the complete
outer Need element. The current host emits ``table.need`` with the Need ID;
do not constrain extraction to a table tag, so another host layout can use a
different element with the same anchor.

Write one small classic-script file per resolved Need detail under
``_static/stv/details/<sha256-of-id>.js``. The graph manifest includes its
relative path and original-page location. Each file registers the rendered
fragment in ``globalThis.__STV_DATA__.details``. Load it on first inspection
by adding a script element; cache the resulting promise per ID. This works
without fetching an HTML page or loading all rich Need bodies at startup.
Files are generated locally at build time and require no network service.

Encode registration data with JSON, escaping ``<``, U+2028 and U+2029 and
never using Need text as executable source. A fragment is trusted published
host content, not an authorization to copy executable scripts: remove script
elements, inline event attributes and executable URL schemes. Preserve
displayed text, tables, links, images and host metadata. This is not a general
untrusted-HTML sanitizer. The owner agreed that static rendered widget text,
images and non-executable markup are sufficient for MVP details; widget-specific
JavaScript remains on the original page (STV_SWR_049). Do not execute copied
widget scripts or claim snapshots of content that exists only after script execution.

Store local resource/link targets in output-root-relative form with their
query/fragment preserved. At insertion, resolve them against the embedding
page's known documentation root. Use ``urllib.parse`` and path components;
handle href, src, srcset, poster and SVG href attributes. Do not rewrite http,
https, mailto, data-image or telephone links as local paths. Reject executable
schemes. Prefix cloned DOM IDs using view ID and inspection sequence and
update same-fragment links and IDREF attributes such as ``for`` and
``aria-labelledby``. Original-object links retain original IDs on the original
page. Details have a loading/error message if a local asset is unavailable.

When an existing object has no locally rendered body (for example an external
Need), show all locally available host metadata and its original link with an
explicit external/unavailable-body indication. Do not fetch external content
during an offline build or pretend that its full body is present. For external Needs this metadata/link fallback was explicitly confirmed as
sufficient for the MVP by the owner; see :need:`STV_SWR_047`. Full-body parity
applies to locally rendered Needs. Host-hidden Needs and all their incident links are excluded before graph or
detail serialization; a hidden starting ID fails with source location. Never
turn a filtered hidden target into a missing-object placeholder.

Graph and state contracts
-----------------------------

The serialized schema version is integer ``1``. Reject unknown major schema
versions in the runtime with a visible diagnostic. Use sorted IDs and canonical
edge triples for deterministic output. Treat labels and IDs as data; DOM text
uses textContent rather than HTML interpolation. Build one index in O(N + E).

``GraphSnapshot`` includes normalized model, objects by ID, canonical edge
triples, directional adjacency and detail script locations. Need parts follow
their host full IDs when present in link targets; resolve them through the host
part collection and original anchor rather than incorrectly marking them
missing. Detail inspection of a part points to its published containing object
and part anchor; part-specific full rendering needs a fixture.

``ViewState`` holds seed, expanded group keys, revision and viewport transform.
Group keys are structured triples ``[objectId, relationName, direction]``;
use nested maps/sets or JSON tuple encoding, not delimiter concatenation that
can collide with an ID. Canonical edge identity uses the same tuple principle.

Filter hidden objects and their incident links before building directional
indexes, degree counts or detail manifests. The initial state has one shared node. Expanding proposes an added group key;
collapsing proposes its removal. Run breadth-first reachability from the seed,
following only expanded groups owned by reached nodes. Retain previously
expanded descendant keys while hidden so a reopened branch can restore them,
but never treat those keys or disconnected cycles as visibility roots.
Stop candidate counting at 201 nodes and reject without commit. Controls and
text labels are not nodes; each missing-target placeholder is a node.

An edge becomes visible when its relationship group is open in either traversal
direction. Deduplicate by authored source/type/target. Missing targets have no
invented expansion controls. Keep their ID and show them in the source object's
band because they have no known type; this is placeholder placement, not a
silent mapping for a real host artifact type.

After a valid candidate graph is obtained, perform layout before committing its
rendered revision. A per-view monotonically increasing request token discards
late asynchronous ELK results. Show a busy indication during the transition;
retain the previous view on layout failure and announce the error. Later
occurrence projection remains behind the state interface and is not implemented
in the MVP.

Layout algorithm and library boundary
-----------------------------------------

ELK performs general ordering; STV enforces the domain rules explicitly:

1. Measure node boxes with width 280 CSS pixels, two title lines and dynamically
   sized relationship controls. Full IDs wrap rather than being truncated.
   Build the visible ELK graph with actual width/height and the canonical
   edges. Run layered layout with DOWN direction and fixed random seed 1.
2. Sort each semantic rank's nodes by their suggested ELK x coordinate, with
   Need ID as the stable tie-breaker. Ignore ELK's y coordinates and edge
   routes after this step. This is intentional: ELK graph-theoretic layers do
   not substitute for the host's semantic level order.
3. Assign ordered horizontal rank bands using measured maximum heights and
   at least 80-pixel inter-band gaps; place nodes with 48-pixel horizontal
   separation. Empty semantic levels may keep an empty band so upward
   expansion does not invert level order. Reordering within a band is allowed.
4. Put resolved test nodes in a separate lane at least 96 pixels beyond the
   rightmost ordinary artifact. Assign a shared test to the median rank of its
   connected artifacts, breaking ties upward; an unconnected test seed uses
   the first band. Stack tests within each band and increase its height to
   avoid overlap. Every shared test remains right of all associated artifacts.
5. Route final SVG edges from measured ports through empty inter-band corridors
   and numbered outer lanes beyond all nodes. Backward edges and cycles retain
   authored arrow direction; same-band links use the gap below that band.
   Reserve separate lanes for self-links. Recompute routes after semantic
   projection rather than drawing stale ELK paths through moved nodes.
6. Assert finite coordinates, nonoverlapping node rectangles, rank order,
   correct test-side placement and edge endpoints on their owning nodes.
   Geometry failure keeps the previous view and produces a diagnostic.

Initial constants are internal design values, not new public configuration.
They can be tuned by prototype evidence without changing the stakeholder
baseline. This MVP routing favors correctness over minimum crossings; a
claim of optimal layout is explicitly outside the acceptance criteria.

Rendering, viewport and inspection
--------------------------------------

An outer view root contains a toolbar, live status region and clipped viewport.
Inside it, one transformed scene contains an SVG edge layer and positioned HTML
nodes. D3 zoom applies the same x/y/scale transform to both layers. Restrict
pointer panning to background drags; wheel zoom applies only within the active
view. Toolbar plus/minus and arrow controls call the same D3 transform API for
keyboard use. Keep transforms per instance. A keyboard-focused node must be
panned into view, not merely focused off-screen.

Each node has an original-object anchor with ``target=_blank`` and
``rel=noopener noreferrer`` plus separate relationship buttons and a Details
button. Buttons expose aria-expanded and meaningful directional names. Stable
DOM keys preserve focus after relayout; if the focused node disappears, return
focus to the collapsing control or nearest surviving ancestor, then the toolbar.

Hover and keyboard Details open the same nonmodal detail panel. Floating UI
positions it relative to the node using offset/flip/shift/size; use fixed
positioning and available viewport dimensions. Keep it open while either trigger
or panel is hovered/focused, with a short dismissal grace period for pointer
travel. Escape or Close dismisses it and restores keyboard focus. Include
aria-controls/labeling; do not assign role=tooltip to a panel containing
interactive links and scrolling controls. Clean up autoUpdate listeners on
close and reposition after view zoom/pan.

Use full host type colors; unknown colors get a deterministic palette ordered
by sorted host type names. Missing/empty status always produces a red border,
even if the accepted-status override contains empty text. Placeholder styling
uses explicit missing-object text, not color alone. No mode selector is displayed
until separate-occurrence mode is actually implemented.

Implementation sequence and completion gates
------------------------------------------------

1. **Package and host seam:** create the package, build assets from the selected
   lock, build a wheel, install it into an independent fixture, and resolve two
   cross-page seed directives. Gate: unknown/missing seeds and invalid mappings
   fail at the correct source location.
2. **Static data and full details:** implement host graph extraction, classic
   script registry and lazy detail scripts. Gate: source metadata/body parity,
   ID/link/media rewriting and successful file-URL operation before continuing.
3. **Shared exploration:** implement state, capacity, ELK projection, nodes,
   edges and styling. Gate: diamonds, cycles, reverse links, placeholder targets
   and exact 200-node atomic rejection checks.
4. **Complete MVP interactions:** add Floating UI panel behavior, D3 viewport,
   keyboard focus and independent instances. Gate: real stable Firefox/Windows
   passes the workflows under file and static HTTP URLs.
5. **Release artifact:** verify clean-wheel install with no Node installed in
   the host, incremental/deletion builds, included notices and large-project
   measurements. Use :doc:`verification-plan` for evidence and exit conditions.

Do not implement later occurrence mode, broaden supported platforms or change
accepted requirements as incidental work. Do not mark internal requirements
passed because a documentation build or a library smoke test succeeds.
