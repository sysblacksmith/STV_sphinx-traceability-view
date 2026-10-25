Internal interfaces and model contract
======================================

This is the MVP software design contract. Usability amendments are tracked
in :doc:`change-requests/STV_CR_003_usability-problems`. Executed implementation
evidence and remaining verification gaps are linked from :doc:`maturity`.
Use :doc:`implementation-plan` for lifecycle/module behavior and
:doc:`technology-stack` for selected dependencies.
Related decisions: :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_005`.

Implementation ownership follows :doc:`elements-software`: every software
element maps to its matching component directory, source filenames and colocated
unit tests. :ref:`STV_ADR_007` defines the organization; the interfaces below
retain their behavior across the source move.

Author interface
----------------

Distribution name: ``sphinx-traceability-view``; import name:
``sphinx_traceability_view``. Neither name's registry availability has been
verified. Enable the module in the host's Sphinx extensions list.

Invocations::

   .. traceability-view::

   .. traceability-view:: MY_NEED_ID

   .. traceability-view:: NEED_A NEED_B NEED_C

The argument is optional: zero IDs selects project-root mode; otherwise parse
the whitespace-separated list, preserving the first occurrence of each ID.
Commas are not separators. Each token must resolve after host collection,
including supported visible Need parts. Unknown/hidden tokens fail the whole
invocation with source location. More than 200 distinct explicit seeds is an
invocation-located capacity error. Exactly 200 is valid but leaves no room for
additional nodes until runtime selection replaces that view's seed set or its
author changes the RST defaults.
Instance identity is generated from source document and invocation index.
No project node is added for explicit seeds, and no edges are opened initially.

Capture Docutils arguments with required_arguments=0, optional_arguments=1,
final_argument_whitespace=True; split the single captured argument on
whitespace. An omitted argument is equivalent to an empty seed list.

The host's ``needs_types`` and ``needs_links`` remain authoritative. A single
supplemental ``traceability_view_model`` configuration value contains ordered
levels, a mapping from host type names to level names or a test role, and an
optional accepted-status set. Example for a five-type host::

   traceability_view_model = {
       "levels": ["stakeholder", "system", "system_arch", "software", "software_arch"],
       "types": {
           "shr": {"level": "stakeholder", "role": "stakeholder"},
           "sysr": {"level": "system"},
           "syse": {"level": "system_arch"},
           "swr": {"level": "software"},
           "swe": {"level": "software_arch"},
       },
       "accepted_statuses": ["accepted"],
   }

The optional role ``stakeholder`` accompanies a normal level placement and
identifies project-root entry types without fixed host names. The default
preset marks ``shr`` this way; replacement models mark their corresponding
types explicitly. Multiple stakeholder types are supported. Missing stakeholder
designation is an entry-located model error only when project-root mode is used;
zero matching visible Needs is valid. Project-root entry lists exclude parts.

An explicitly selected legacy test type uses ``{"role": "test"}`` instead of
``level``; classified evidence uses the selectors specified below. It must already
exist in the host schema. The five default levels/mappings are a supplied
preset for this method, not a restriction on other projects. Replacement models
provide explicit mappings for their host types. No separate title, tooltip or
palette settings are proposed. Missing colors use a built-in stable palette.
Missing/empty status never counts as accepted, even if present in the override.

Validation checks unique ordered levels, known host types, one placement per
type, known referenced level, complete host-type mapping and valid acceptance
values. Relationship types and incoming/outgoing labels come from the host;
there is no duplicated relation registry. Missing incoming/outgoing labels use the host
configuration defaults, not independently invented wording. If a required
directional label is still absent after normalization, report an entry-specific
model error before writing views. The supplemental mapping must not mutate the host schema.

Build-to-browser contract
-------------------------

A versioned immutable payload contains:

* schema version and build content identity;
* host Sphinx project name and sorted top-level stakeholder IDs;
* normalized levels, type placement/color, accepted statuses and relation labels;
* objects keyed by Need ID: title, type, status, document/anchor and detail key;
* canonical outgoing edges and indexed incoming/outgoing target groups;
* unresolved target records preserving the referenced ID;
* per-object local detail-script locations and a lazily populated registry of
  final rendered fragments keyed by resolved Need ID.

Per-view initialization is page-local: ``{mode: "seeds", seed_ids: [...]}``
or ``{mode: "project", seed_ids: []}``, plus the instance identity. The manifest
contains the project name from ``app.config.project`` as escaped text, not HTML.
The synthetic root is a presentation record, not an entry in the Need registry.
Use tagged identities ``["need", id]`` and ``["project", viewId]`` so host IDs
cannot collide with the artificial root. Synthetic entry edges and controls
are separate from canonical authored relationship triples and relation indexes.

Per-view seeds and identities remain page-local. Emit one shared project graph
asset per build rather than embedding the full graph in every view. Emit details
as local per-object scripts and load them on first inspection, caching by build identity and ID. Classic
script assignment to a private namespaced registry permits loading from disk;
do not rely on file-origin fetch or ES-module requests. Include only project
content already published by the host, not hidden Need internals. Serialize
strings safely for their HTML/JavaScript context, including closing-script
sequences, and avoid evaluating Need text as code.

Detail fragments are derived from the host's final HTML, not reconstructed from
raw Need dictionaries. Rebase relative links and media to work on the embedding
page, namespace duplicated HTML IDs and update fragment references, preserve
original documentation anchors for navigation, and exclude executable scripts
from copied fragments. Third-party widgets preserve their static rendered content in MVP details;
widget-specific JavaScript remains on the original page by owner agreement
(STV_SWR_049).

State interface
---------------

Input: immutable graph/model, current view state and a command. Output: either
new state plus visible graph, or unchanged state plus a diagnostic. Commands
include expand/collapse group, replace seed, project overview, open/close
details, zoom and pan; the later
selector adds mode projection. Graph state is separate from viewport state.
A rejected cap transition cannot partially update graph, mode, page or focus.
Seed mode retains every distinct supplied seed as a visibility root until an
explicit runtime seed or overview replacement succeeds. Project
mode retains its synthetic root and follows only the current stakeholder entry
page when expanded. Each page owns an independent expansion-key set; inactive
pages contribute neither visible nodes nor traversal roots. Page size is five,
with IDs sorted lexicographically. Previous/Next selects an adjacent valid page,
restores its saved valid exploration state, then uses normal cap/layout checks
before atomic commit. Project mode initially opens page zero and at most five
entries. Root collapse retains the page index and page state but
hides every descendant. Empty lists have no root expansion or page controls.

Every view includes a labelled picker over its immutable published object
catalog. Case-insensitive substring matching searches IDs and titles; show
at most ten suggestions with the total and a refine-search hint. Confirmation
of a suggestion or case-sensitive exact trimmed ID proposes fresh seed mode.
Unconfirmed typing and invalid/hidden IDs cannot change graph state. Keyboard
Up/Down selects a suggestion; Enter confirms; Escape dismisses suggestions.
Project overview proposes fresh project mode with page zero open. Both commands
clear previous expansions/page memory only on successful capacity/layout commit,
reset that view's viewport and close transient hover details and retain persistent boxes. Preserve picker focus and
other instances. Failed/stale transitions preserve the committed scene/state.
No runtime graph fetching, source edit or rebuild is involved.

Capacity and performance
------------------------

Build adjacency in O(N + E); runtime expansion uses indexed groups and considers
only candidate visible nodes for rendering. The entire project graph/detail
payload can still be large: this design does not claim bounded memory or load
time independent of N. Measure a proposed 30,000-object/90,000-edge fixture and
200 visible nodes in the prototype, recording payload size, startup and
interaction timings. These are proposed measurements, not accepted performance
thresholds; budgets remain open.

Reviewed publication identity: content-addressed graph and detail scripts with
build-keyed registries prevent stale browser cache entries crossing revisions.


Remote embedded resource contract
---------------------------------

Uncached remote embedded media uses an unavailable-offline indication and
an explicit original-resource link.
Preserve local bundled media. Do not download remote media automatically at
build time or request it when a detail panel opens. During extraction, replace
remote image/srcset, audio/video/source/poster, iframe/object/embed and SVG
resource references with a static placeholder and explicit link. Remove remote
CSS imports and url() dependencies from copied styles; retain the affected
resource URLs as explicit links. Resolve relative references against the
original page before classifying them, including protocol-relative URLs.
Local resources and permitted data images remain usable; ordinary external
navigation links remain explicit reader actions. Do not copy remote stylesheets
or active embedded documents into details. This policy refines STV_SWR_015/017
and the explicitly amended STV_SHR_015; it does not require a media cache.

Layout and inspection contract
------------------------------

Relationship controls use configured target levels to order wholly upward
groups first, neutral groups next and wholly downward groups last. Mixed,
same-level, test-role and unresolved groups are neutral. Stable ties preserve
host order. The ordering helper preserves group identity and expansion state.

Direct unobstructed routes use facing box edges; blocked routes retain outer
corridors and canonical arrow direction. The viewport is 975 CSS pixels high.
Inspection owns one pending 1000 ms hover timer per view; node departure,
Escape, scene commit and viewport movement cancel it. Explicit Details
activation bypasses it. Moving onto the Details button retains the node timer.
Escape is observed even when keyboard focus is outside the hovered view.

Detail asset path contract
--------------------------

Each transformed detail fragment uses its full SHA-256 content digest as the
filename, ``_static/stv/details/<content-hash>.js``. Objects with identical
fragments share one immutable asset. The manifest retains per-object identity
and references its digest and URL; fragment registration remains keyed by that
same full digest. No digest is truncated. Windows file-URL consumers still need
an output root short enough that the complete asset path fits their browser's
path support; arbitrary-depth output roots are not promised.

Detail transport marker ownership
---------------------------------

``data-stv-*`` attributes are reserved for the detail extractor. Remove all
such attributes from authored HTML before generating transport markers from
validated ordinary attributes. The inspector independently restores only
output-local relative paths or permitted raster data images; it rejects active
schemes, remote/absolute paths, traversal and escaped separators. Ordinary
external navigation links remain explicit reader actions. CSS transport accepts
canonical quoted local ``url()`` values and rejects imports and escaped syntax.
This closes :need:`STV_PR_007` within :need:`STV_SWR_015`, :need:`STV_SWR_017`
and :need:`STV_SWR_018`. Graph state, events and timers are unchanged.

Local documentation publication
--------------------------------------------------------------------------------

``build-docs.ps1`` delegates to ``scripts/build_docs.py`` after dependency checks.
The helper builds into a new sibling staging directory with a separate Sphinx
doctree cache. Only a successful warnings-as-errors build is promoted to
``docs/_build/html``. Existing output is retained in a sibling previous-output
directory; failed promotion attempts restore it. No recursive deletion occurs.
Resolved rename targets must be direct children of the source's build directory;
redirected HTML output paths are rejected before moving existing output.

``_stv-publication.json`` inventories every staged publication file by relative
path, byte count and SHA-256. It excludes its own entry and contains no local
absolute paths. Only ``html`` is the publication tree; retained prior/failed
builds and doctrees outside it are local diagnostics. This prevents carryover
of obsolete graph/detail scripts, pages and downloads. It does not revoke
already copied output or add automatic deployment. Direct incremental Sphinx
commands remain suitable for development but are not the publication workflow.
This maintenance boundary refines :need:`STV_PR_011`; extension graph state,
timers and runtime behavior are unchanged, so no state diagram changes apply.

Committed geometry and navigation layout
-----------------------------------------

``layout.compute(graph, visible, measuredBoxes, context={})`` returns final
``nodes``, ``edges``, ``ranks``, ``bandTops``, horizontal origin ``x``, ``width``
and ``height``. Node/rank/band maps are transient per-view layout data.
``context={previous, anchor}`` is supplied only for group/root commands, using
the last successful scene and the structured Need key or synthetic project key.
The renderer never replaces this snapshot on a rejected/stale computation.

Fresh placement follows :need:`STV_SWR_056` and :need:`STV_SWR_060`.
Incremental placement follows :need:`STV_SWR_058`: preserve ordinary x slots,
anchor the clicked band, retain same-rank test offsets, append reranked/new tests
and open vertical space only where measured band heights require it. Ordinary
ranks are immutable model levels; a legacy test-role node's median connected rank may change.
The anchor's position wins over renewed centering; other bands may move in y.
No-op/rejected commands preserve the committed snapshot. Explicit Reset viewport
changes only D3's transform. Focus restoration uses ``preventScroll``.

``render/edge-viewport.js`` computes bounds from all node corners and route
points with 24 px padding. SVG CSS left/top equals viewBox x/y; width/height
match viewBox extents. Thus negative-world paths remain aligned to HTML nodes.
The existing request-token, rollback and independent-view contracts remain.
See :ref:`STV_ADR_008`. No component boundary, event, state or timer is added. The software view names
the committed-geometry feedback and the state view refines the layout action.

Classified test evidence placement
-----------------------------------

:ref:`STV_ADR_009` adds two mutually exclusive type placements to the existing
fixed level and legacy test role. ``levels_by_tag`` maps nonempty host tag names
to configured levels. ``level_from`` contains ``relation``, ``direction``
(incoming/outgoing) and a ``levels`` owner-level-to-target-level map. Its owners
must have fixed/tag placement; chained owner-derived data links are not inferred
and use fallback (or a Need-located strict error if fallback is absent).
``fallback_level`` is optional on either classifier and names a configured row.
Malformed selectors, unknown levels/relations and invalid chaining fail model
validation with a field path. No host type/tag/relation names are hard-coded.

GRAPH first excludes hidden records and resolves all fixed/tag placements, then
uses indexed published relations to resolve one-hop owner placements. Exactly
one resulting level is required: no selected tags, conflicting tag levels,
missing owners, unresolved owners or mixed owner levels choose the configured
fallback, or fail with Need ID if no fallback exists. Same-class multiple owners
are unambiguous. A fallback owner propagates fallback, rather than upgrading an
execution to a known class based on only one of its other owners. Hidden owner
identities are never published or included in diagnostics. Parts follow their
published metadata and the same rules. No derived backlink is required.

Schema 1 gains additive ``object.level`` and ``object.placement_fallback`` fields
for classified records only. Fixed types and legacy-role graphs remain readable
without them. Layout and directional controls use resolved level before fixed
type level. Classified rows use ordinary same-row/top alignment and stable slots;
only ``role: test`` retains the legacy lane. RENDER labels fallback nodes
``Unclassified test evidence`` without disabling links/details/navigation.
The synthetic root, cap, request tokens, world-coordinate SVG, focus and view
independence contracts remain unchanged. Empty configured rows retain spacing.

The project's model declares the nine CR_013 levels followed by unclassified
and problem rows. Test cases use test_system/test_software tags; executions use
incoming executed_by owners. Generic authors can select different names, fixed
levels or legacy role; the default five-type preset is unchanged.

Viewport clipping marker
--------------------------

:need:`STV_SWR_062` places a 1 px solid grey top border on ``.stv-viewport``,
not on ``.stv-scene``. The viewport owns overflow clipping and stays in normal
flow after toolbar/status. Explicit content-box sizing retains 975 px client
height under host themes. The border is outside the content clip area; no
pseudo-element, overlay, handler, timer or extra focus target is introduced.

Persistent detail collection contract
--------------------------------------

``traceability_view_details_limit = 10`` in conf.py is a positive safe integer;
MODEL validates it, DIRECTIVE publishes optional ``graph.details_limit`` before
BUNDLE emission. Missing fields in older graphs use 10. This presentation
setting is separate from the host type/relationship mapping; authors need not
replace that model to configure capacity.

INSPECT separates hover from persistent entries. ``content.js`` owns cached
classic-script transport and safe fragment/URL/IDREF restoration. ``inspect.js``
keeps Floating UI hover timers and dismissal. ``collection.js`` is an ordered
per-view Need-ID map; ``persistent.js`` owns labelled entry DOM, loading/error,
current-entry completion guards, reuse/FIFO/close/all and trigger associations.
RENDER owns the dock and right-aligned Close all, refreshes live trigger links
after node-control replacement and computes Reset against current viewport size.

A new ID is created once, oldest live entry is evicted if full, then the new
entry is appended. Reuse leaves order intact. Closed/reopened IDs get a new
entry identity; old completions cannot insert. Transport cache survives entry
removal. Entry errors remain readable; close/reopen retries transport failures.
Graph/seed/overview/page commits and Escape affect hover only, not the collection.
Document pagehide clears entries without focus restoration, including cache
suspension; navigation/reload drops page-local state. No storage or graph mutation.

The dock is 720 px beside graph containers wider than 1120 px. Below that
threshold it follows the graph, aligned right and bounded to the available width
and 720 px, retaining usable graph space.
Stack height is bounded and scrollable; boxes have bounded own scrolling and
unique namespaced body IDs. Open/reuse focuses/reveals its Close control; async
content never focuses. Close resolves a fresh visible node trigger, else the
view's Close all. The empty Close all remains focusable. Native layout reserves
graph space; it does not overlay nodes. Graph coordinates/D3 transform are not
changed merely by opening/closing a box; explicit Reset uses the new dimensions.


Copied Need metadata controls
-------------------------------

``inspect/content.js`` initializes only copied ``.needs_collapse`` controls.
Decode their host row-class list before replacing the control ID; resolve rows
within the same containing Need table. Generate unique control/row IDs, keep
button role, tabindex, aria-expanded and aria-controls in sync, and start folded.
Click, Enter and Space toggle those rows and the host right/down icons together.
Each new fragment owns its handlers; reuse preserves current state. No host
jQuery/document-ready callback or arbitrary widget script is executed. Unknown
controls without matching rows are hidden, rather than left as dead arrows.

Artifact-ID header anchors under ``.needs-id`` retain their restored canonical
source URL and open with noopener/noreferrer in a new tab. They are excluded
from copied-body fragment rebasing. Other same-document anchors keep namespaced
local destinations; other restored links/resources retain the safe URL policy.


Detail pane boundary
-----------------------

RENDER gives the visible stack a 1 px solid #999 border inside its 720 px
border-box width. Its side-by-side outer height is 976 px, matching the graph's
975 px client area plus top border. Keep 8 px inner padding and no persistent
card shadow so the pane top/separator remain crisp. The narrow container's
existing 60vh maximum still bounds the below-graph stack. Hidden stacks do not
render the frame. No exploration or inspection state transition changes.

CR015-018 command and presentation contracts
--------------------------------------------

RENDER dispatches ``{type: 'collapse-all'}`` to STATE. STATE computes
``initial(current.mode === 'seeds' ? current.seeds : [])``, sets revision to
current revision plus one, and returns the ordinary validated visibility result.
This clears expanded groups and all page restoration caches, sets project page
zero/rootOpen true, and never changes the persistent collection. RENDER cancels
old layout generations and closes transient hover using its normal graph-commit
policy. A successful fresh layout fits the current viewport. Pending layout
failure retains the committed view and permits retry; no partial reset is shown.
The existing occurrence-mode deferral remains; no unimplemented mode is enabled.

``traceability_view_tooltip_font_scale`` and
``traceability_view_details_font_scale`` are independent finite positive numbers,
not booleans, with new-build default 0.7. MODEL validates; DIRECTIVE publishes
schema-1 additive ``graph.presentation = {tooltip_font_scale, details_font_scale}``.
Missing fields in old bundles default to 1.0. Both values participate in bundle
identity. No user data model replacement or reader settings panel is required.

INSPECT measures each newly restored fragment in its actual presentation style
context at scale 1.0 before changing any font styles. Capture computed CSS-pixel
sizes for the complete descendant tree, then apply each captured size times the
presentation scale in a second pass. This avoids nested multiplication and
preserves existing explicit heading/table/code sizes. The visible panel wrapper's
own heading/link text uses the same baseline rule. Measure synchronously in the actual restored presentation before the next
paint, never creating a second accessible live card. Restore retained baselines
before measuring newly inserted descendants, then apply all sizes in a second
pass; initial loading/error wrappers use the same rule. Delayed fonts must finish before measurement, or
re-measure from the retained unscaled baseline after font readiness. Reuse never
rescales already scaled values. Fragment disposal releases its measurement state.
This is presentation-local; no source-page or graph label CSS is changed.

``render/page-metadata.js`` initializes at DOMContentLoaded (or immediately when
already ready), selecting original ``table.need`` elements outside ``.stv-view``
and all ``.stv-detail``/persistent-copy subtrees. DIRECTIVE includes the existing
local runtime on every HTML page with rendered Needs, even with zero STV roots;
initialization is idempotent and does not require a graph transport. DIRECTIVE
finalization scans completed host HTML for rendered Need tables and injects one
STV-owned local runtime/CSS reference using output-relative URLs when absent.
It does not inject a graph script merely for page controls. RENDER index.js
initializes the page controller before looking for a data-stv-root script; if
no view roots exist it returns without dereferencing a missing script. Place one
labelled control group before the first host Need, with real button elements.
No Needs means no group; Needs without disclosures show disabled buttons with
an explanation. Discover host disclosure controls only in their closest owning
Need table and derive target rows using the host's encoded class list. The pinned Sphinx-Needs 8.2.0 handler is attached to the nested
``span.needs.collapsed`` and ``span.needs.visible`` icons, not their
``.needs_collapse`` wrapper. For uniformly folded/open rows whose state differs
from the requested target, activate the currently displayed nested icon once,
then reconcile actual rows/icons/ARIA. For already matching rows do nothing.
For mixed rows within one disclosure normalize the identified rows and its two
icons directly to the target instead of inverting their mixed states.
A shared synchronization routine derives aria-expanded, aria-controls and label
from row visibility. A post-host delegated icon-click listener invokes only that
synchronization routine, never a second toggle; this keeps ARIA correct after
subsequent individual native clicks. Give the wrapper role/button tabindex and
map Enter/Space to the currently displayed host icon once, with preventDefault.
Bulk buttons remain real native buttons. Do not attach a competing individual
visibility-toggle handler to the host wrapper.

Enable page controls only after window load and a registered jQuery ready
callback, including already-complete document cases; host collapse handlers are
then installed. Missing pinned host prerequisites or unsupported encodings leave
a readable disabled group, not a partial/global toggle. Custom markup without
collapsible metadata retains the defined no-attributes explanation. Copied
INSPECT controls retain their separate existing initialization and lifecycle.

Visible-area capture and resource contract
-------------------------------------------

``EXPORT.capture(workspace, {base, resources, regions})``
returns an immutable snapshot descriptor or a typed capture error. A crop with
zero width/height produces "No visible view area to export" and no download;
never fabricate a minimum-size canvas or scroll the page automatically. Capture
requires completed local resource registration and document.fonts readiness.
Pending resources/fonts expose a retryable preparation state; failed required
resources/fonts expose an error while graph interaction remains available.
Capture does not asynchronously wait for fonts and then read newer live DOM.
RENDER exposes
only its last committed presentation. Busy/failed layout blocks export with a
retry instruction rather than mixing pending geometry and committed DOM.

Capture reads geometry, computed styles, all scroll offsets and DOM synchronously
in one task. The crop is the intersection of the workspace rectangle with the
browser visual viewport (layout viewport fallback), in CSS pixels. Toolbar,
status, other views and content outside this crop are excluded. Narrow layouts
include only the screen-visible part of the below-graph dock. The outer SVG uses
this crop as width/height and viewBox; workspace/tooltip positions are translated
relative to its top-left. Each overflow ancestor becomes an explicit clipping
wrapper. Normalize scroll containers into fixed-size overflow-hidden wrappers
with inner content translated by captured negative scroll offsets. Preserve the
D3 transform and existing nested SVG viewBox/origins; never refit for export.

A pointer activation snapshots on primary pointerdown before toolbar focus can
dismiss a visible tooltip; click completes serialization/save. Cancelled pointer
activation discards the descriptor. Keyboard activation captures the state at
activation; it does not recreate a tooltip already dismissed by normal focus.
An INSPECT region is included only if it belongs to this view and intersects
the crop. Frozen descriptors contain no live nodes or callbacks. Future graph,
font, viewport or card changes cannot alter an in-progress snapshot. Read-only
snapshotting does not close cards, update their age or move focus.

``EXPORT.serialize(snapshot)`` constructs namespaced SVG with
XHTML foreignObject, computed inline style and nested graph SVG. It materializes
visible ::before/::after textual decoration, replacing control icons with their
captured inert appearance. Freeze animation/transition state. Discard handlers,
scripts, forms, embedded executable widgets, graph/transport attributes and
nonvisual accessibility-control markup. Already safe detail content remains the
source; export adds a second inert-output boundary. Do not serialize document
head, style sheets or arbitrary host scripts. Rewrite fragment IDs/references
within the snapshot. The effective workspace ancestor background is captured
as an SVG backdrop. Original style elements are omitted after computed-style
capture; only selected embedded font-face rules are emitted. Ordinary external navigation links may remain explicit
links; automatic resource loading is restricted to embedded validated data.
Non-intersecting positioned/SVG subtrees are omitted. Off-screen flow boxes
become empty, nonvisual geometry placeholders, preserving scroll positions and
flex/grid gaps without their text, resources or identities. Clipping remains
authoritative for partial text/media intersections. SVG is a visual crop, not a promise to redact every
character beyond the visible portion of a partly clipped text node.

DETAIL_BUILD finalization walks safe local media/CSS dependencies used by detail
fragments and STV styles. Resolve and symlink-check every file beneath the output
root before reading. Validate MIME by content, retain approved raster data,
sanitize local SVG to inert namespaced markup (no scripts, event handlers,
foreign executable content or unresolved external dependencies), and collect
local font bytes needed for @font-face. Reject cycles/unresolvable references
with an explicit resource error. Never traverse outside output or download
HTTP resources. Existing unavailable remote-media placeholders remain visible.
Build records map canonical output-relative paths to MIME/base64/digest or a
readable failure record. Keep large resource maps in separate content-addressed
classic scripts, registered as immutable data using the existing escaped-JSON
transport; the graph points to their identity/URL. Load the local record script
before enabling Save; keep graph exploration usable if it fails. Include only
resources selected by the visible capture (including currentSrc for srcset),
not the entire resource map, in the saved SVG. Font fallback with no bundled
webfont uses the captured system-font family and carries no external request.

The resulting XML must parse before a download is offered. Required visible
resource/style failures abort with a readable message; do not silently replace
previously available local content or report success with broken images. No
runtime fetch/XHR, arbitrary file access or original-page dependency is permitted.
No export change relaxes the existing detail URL/sanitization policies.

``EXPORT.saveSVG(svgText, viewId)`` uses Blob type
``image/svg+xml;charset=utf-8``, URL.createObjectURL and a temporary HTML anchor
with download. Default name is ``stv-<safe-view-id>.svg``; allow only safe filename
characters and bound the generated component to 80 characters. There is one
in-flight operation per view. Remove the anchor after activation; revoke its URL
after 60 seconds or pagehide, whichever is first. A pending URL registry supports
several successive completed downloads without early revocation. The 60-second
lease is a cleanup policy to verify with the target browser, not proof of disk
save completion. Generation errors release immediately and allow retry.

Location/name choice is browser/OS owned. User guidance explains enabling
"Always ask you where to save files" in Firefox (or the equivalent browser
setting). STV cannot force the native dialog or observe a cancelled/completed
download. Its status says "SVG download requested", never "file saved". Automatic
folder mode remains usable but does not claim a location prompt. The accepted
owner clarification permits this documented browser-managed behavior.

Local SVG validation uses the standard-library XML parser with DTD/entity
constructs rejected before parsing. Accept only the SVG namespace and static
svg/g/defs/path/rect/circle/ellipse/line/polyline/polygon/text/tspan/use/image,
clipPath/mask/marker/pattern/linearGradient/radialGradient/stop/title/desc/style
nodes. Reject animation, scripts, event attributes, foreignObject and unknown
namespaces in imported resources; EXPORT's own controlled foreignObject wrapper
is a different boundary. SVG use/href and paint/filter references must resolve
to a local fragment or an embedded validated raster dependency; unresolved or
external references produce a typed resource failure. Reject CSS imports and
external URL references; embed accepted local font-face records explicitly.
Validate all references again after rewriting. Unsupported local SVG remains
viewable in the source documentation but export reports its unsupported resource
rather than claiming a complete standalone snapshot. Extending the allowlist is
a reviewed compatibility change with corresponding security/fidelity fixtures.

Host bulk actions reject disclosures targeting title/head or content/body rows.
Missing host handlers or unsupported row encodings disable the page-wide pair
with a readable explanation rather than applying a partial change.
