Internal interfaces and model contract
======================================

This is the concrete MVP software design contract, not an implemented API.
Use :doc:`implementation-plan` for lifecycle/module behavior and
:doc:`technology-stack` for selected dependencies.
Related decisions: :ref:`STV_ADR_001`, :ref:`STV_ADR_002` and :ref:`STV_ADR_005`.

Author interface
----------------

Proposed package name: ``sphinx-traceability-view``; import name:
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
additional nodes until the view's selected seeds change in the RST source.
Instance identity is generated from source document and invocation index.
No project node is added for explicit seeds, and no edges are opened initially.

Capture Docutils arguments with required_arguments=0, optional_arguments=1,
final_argument_whitespace=True; split the single captured argument on
whitespace. An omitted argument is equivalent to an empty seed list.

The host's ``needs_types`` and ``needs_links`` remain authoritative. A single
supplemental ``traceability_view_model`` configuration value contains ordered
levels, a mapping from host type names to level names or a test role, and an
optional accepted-status set. Example, using this project's host types::

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

A host test type uses ``{"role": "test"}`` instead of ``level``. It must already
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
include expand/collapse group, open/close details, zoom and pan; the later
selector adds mode projection. Graph state is separate from viewport state.
A rejected cap transition cannot partially update graph, mode, page or focus.
Seed mode retains every distinct supplied seed as a visibility root. Project
mode retains its synthetic root and follows only the current stakeholder entry
page when expanded. Each page owns an independent expansion-key set; inactive
pages contribute neither visible nodes nor traversal roots. Page size is 50,
with IDs sorted lexicographically. Previous/Next selects an adjacent valid page,
restores its saved valid exploration state, then uses normal cap/layout checks
before atomic commit. Page zero starts collapsed; first root expansion opens
its first 50 entries. Root collapse retains the page index and page state but
hides every descendant. Empty lists have no root expansion or page controls.

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
