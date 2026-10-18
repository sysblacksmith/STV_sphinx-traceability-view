Internal interfaces and model contract
======================================

This is a proposed software design contract, not an implemented API.
Related decisions: :ref:`STV_ADR_001` and :ref:`STV_ADR_002`.

Author interface
----------------

Proposed package name: ``sphinx-traceability-view``; import name:
``sphinx_traceability_view``. Neither name's registry availability has been
verified. Enable the module in the host's Sphinx extensions list.

Proposed invocation::

   .. traceability-view:: MY_NEED_ID

The required argument is the seed ID. Instance identity is generated from the
source document and invocation index, not provided by an extra author option.

The host's ``needs_types`` and ``needs_links`` remain authoritative. A single
supplemental ``traceability_view_model`` configuration value contains ordered
levels, a mapping from host type names to level names or a test role, and an
optional accepted-status set. Example, using this project's host types::

   traceability_view_model = {
       "levels": ["stakeholder", "system", "system_arch", "software", "software_arch"],
       "types": {
           "shr": {"level": "stakeholder"},
           "sysr": {"level": "system"},
           "syse": {"level": "system_arch"},
           "swr": {"level": "software"},
           "swe": {"level": "software_arch"},
       },
       "accepted_statuses": ["accepted"],
   }

A host test type uses ``{"role": "test"}`` instead of ``level``. It must already
exist in the host schema. The five default levels/mappings are a supplied
preset for this method, not a restriction on other projects. Replacement models
provide explicit mappings for their host types. No separate title, tooltip or
palette settings are proposed. Missing colors use a built-in stable palette.
Missing/empty status never counts as accepted, even if present in the override.

Validation checks unique ordered levels, known host types, one placement per
type, known referenced level, complete host-type mapping and valid acceptance
values. Relationship types and incoming/outgoing labels come from the host;
there is no duplicated relation registry. Missing incoming labels and host
special cases are adapter feasibility checks, not grounds to invent labels
silently. The supplemental mapping must not mutate the host schema.

Build-to-browser contract
-------------------------

A versioned immutable payload contains:

* schema version and build content identity;
* normalized levels, type placement/color, accepted statuses and relation labels;
* objects keyed by Need ID: title, type, status, document/anchor and detail key;
* canonical outgoing edges and indexed incoming/outgoing target groups;
* unresolved target records preserving the referenced ID;
* a registry of final rendered detail fragments keyed by resolved Need ID.

Per-view seeds and identities remain page-local. Emit one shared project data
asset per build rather than embedding the full graph in every view. Classic
script assignment to a private namespaced registry permits loading from disk;
do not rely on file-origin fetch or ES-module requests. Include only project
content already published by the host, not hidden Need internals. Serialize
strings safely for their HTML/JavaScript context, including closing-script
sequences, and avoid evaluating Need text as code.

Detail fragments are derived from the host's final HTML, not reconstructed from
raw Need dictionaries. Rebase relative links and media to work on the embedding
page, namespace duplicated HTML IDs and update fragment references, preserve
original documentation anchors for navigation, and exclude executable scripts
from copied fragments. Exact adaptation of interactive third-party extensions
must be assessed in the vertical slice; do not claim arbitrary widget fidelity.

State interface
---------------

Input: immutable graph/model, current view state and a command. Output: either
new state plus visible graph, or unchanged state plus a diagnostic. Commands
include expand/collapse group, open/close details, zoom and pan; the later
selector adds mode projection. Graph state is separate from viewport state.
A rejected cap transition cannot partially update either graph or mode.

Capacity and performance
------------------------

Build adjacency in O(N + E); runtime expansion uses indexed groups and considers
only candidate visible nodes for rendering. The entire project graph/detail
payload can still be large: this design does not claim bounded memory or load
time independent of N. Measure a proposed 30,000-object/90,000-edge fixture and
200 visible nodes in the prototype, recording payload size, startup and
interaction timings. These are proposed measurements, not accepted performance
thresholds; budgets remain open.
