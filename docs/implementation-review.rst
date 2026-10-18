Implementation criterion review and operating limits
=====================================================

Scope and authority
-------------------

The owner requested implementation of the accepted STV concept on 2026-10-18.
Input was clean revision ``30aaba98776ecbe648558d278a985691d81bccb4``, with
the round-3 starting-node amendment already accepted. The delivered scope is
the initial shared-identity MVP: every system requirement and every software
requirement except the four explicitly later occurrence-mode requirements
(:need:`STV_SWR_019`, :need:`STV_SWR_021`, :need:`STV_SWR_022`,
:need:`STV_SWR_023`). Touch and additional platforms remain deferred.

The assessment below identifies observable assertions at the appropriate
boundary. Results are separate: :doc:`test-execution/index` retains actual
candidate identities, per-case outcomes, commands, packages and measurements;
:doc:`test-coverage` provides the complete individual SYS/SWR inventory and
executable sources. A mapping or this review prose does not replace an executed
result. Current maturity and verification dispositions remain in :doc:`maturity`
and the canonical Need fields.

System criterion assessment
---------------------------

.. list-table:: System-level executable assertions
   :header-rows: 1
   :widths: 18 45 37

   * - Requirement
     - Observable criterion exercised
     - Executable cases
   * - :need:`STV_SYS_001`
     - Real HTML build resolves cross-page explicit seeds and independent
       seedless views; mixed unknown/hidden seeds fail at invocation location.
     - ``test_cross_page_bundle``, ``test_invalid_seed_source_location``,
       ``test_project_paging``
   * - :need:`STV_SYS_002`
     - Two authored schemas retain host labels and placement; invalid mapping
       reports its entry path and invocation location before view generation.
     - ``test_alternate_host_schema_external_metadata_and_parts``,
       ``test_invalid_mapping_has_entry_path_and_location``
   * - :need:`STV_SYS_003`
     - Generated output explores and loads rich local details under file and
       nested static HTTP URLs with external HTTP/HTTPS blocked by proxy.
     - ``test_offline_exploration``,
       ``test_alternate_model_geometry_details_and_external``
   * - :need:`STV_SYS_004`
     - Actual host traces traverse in both directions; hidden references are
       filtered; host broken-link failure coexists with a usable missing node.
     - ``test_alternate_model_geometry_details_and_external``,
       ``test_missing_placeholder_and_detail_error``,
       ``test_host_owns_broken_trace_failure``
   * - :need:`STV_SYS_005`
     - Software-seeded expansion reveals higher declared levels above it;
       the added hardware rank and right-side shared test retain geometry.
     - ``test_alternate_model_geometry_details_and_external`` plus
       ``frontend/test/layout.test.js`` invariant assertions
   * - :need:`STV_SYS_006`
     - Hover/keyboard details preserve host metadata, rich body, tables,
       local images and namespaced IDREFs; external metadata and unavailable
       bodies are explicit; original links and remote-media fallbacks work.
     - ``test_offline_exploration``,
       ``test_alternate_model_geometry_details_and_external``
   * - :need:`STV_SYS_007`
     - Exploration and viewport changes in one view leave the other view's
       revision and transform unchanged. Async completion does not reclaim
       focus from a control outside the view.
     - ``test_offline_exploration``,
       ``test_async_layout_failure_and_stale_completion``
   * - :need:`STV_SYS_008`
     - The real 30,000-Need/90,000-edge build loads and explores to exactly
       200 visible nodes; another complete group is rejected without changing
       the committed revision. Measurements repeat under file and HTTP URLs.
     - ``test_large_project_at_visible_capacity`` plus exact 199/200/201
       and project-root counting cases in ``frontend/test/state.test.js``
   * - :need:`STV_SYS_009`
     - A wheel installs offline into a fresh Python 3.10 host and builds the
       fixture with Node absent from PATH; import resolves inside that host.
     - ``test_clean_wheel_host``
   * - :need:`STV_SYS_010`
     - Interaction workflows use the installed stable Firefox desktop binary
       on Windows, including pointer, keyboard, pan/zoom, paging and recovery.
     - ``tests/test_browser.py`` and ``tests/test_capacity.py``;
       exact binary/platform versions and headless mode are retained per run

Software criteria and transition review
---------------------------------------

The individual acceptance criteria are reproduced beside their executable
cases in :doc:`test-coverage`. Source review checks the same component seams:

* Directive/model/graph checks cover optional distinct seed lists, exact initial
  capacity, source locations, host-normalized labels, replacement type/rank
  mappings, stable palette fallback, accepted-status overrides, parts,
  external original URLs and hidden filtering before indexing/serialization.
* Pure state cases assert complete-group expansion, both trace directions
  beyond three hops, diamonds, self-loops, isolated cycles, multiple roots,
  descendant restoration, page boundaries and independent page expansion sets.
  Rejected candidates retain the original state object.
* Layout checks assert declared rank order, nonoverlapping finite rectangles,
  shared test placement, ports and routes that avoid node interiors. Browser
  cases inspect actual rendered boxes; measurements exercise real 200-node
  scenes rather than replacing ELK with a mock.
* Detail and browser cases cover static host markup, local images, data images,
  srcset/CSS/media rewriting, remote fallback links, executable URL rejection,
  DOM ID/IDREF isolation, external-body fallback and static third-party widgets.
  Prototype-like IDs and script-closing text are data in classic registration
  scripts. Normal author prose is not treated as a hidden relationship field.
* Browser cases cover two-line title clamping, complete wrapped IDs, empty and
  reviewed status borders, nonempty directional controls, missing-object text,
  whole-card original links, hover travel, bounded/scrollable panels, keyboard
  dismissal, native focus panning, pointer drag/wheel zoom and independent views.
* Controlled layout completions exercise initial failure/retry, late-result
  discard, subsequent failure without commit, and focus ownership. Missing
  detail assets show an error and recover after the asset is restored.
* Host/build cases exercise content hashes across incremental/no-op rebuilds,
  hidden-object removal, finalization failure and preservation of a prior fatal
  exception. Packaging cases inspect included assets/notices and the installed
  artifact, not a source-only import.

The behavioral transition/source/test mapping and editable published diagram
are in :doc:`state-machine`. No later occurrence mode or selector is shipped.

Integration decisions within the accepted contracts
---------------------------------------------------

Sphinx-Needs 8.2.0 unconditionally registers unused GitHub service types during
environment preparation. STV captures the author's type schema before that
injection, then includes any additional type actually used by host objects.
Complete mapping validation therefore covers the authored schema and actual
service data, without demanding mappings for unused injected service types or
mutating the host schema. Host-normalized relationship defaults remain
authoritative. This resolves the default five-type preset against the real
host seam without changing the accepted architecture or adding another model.

Graph/detail publication uses content identities, null-prototype JSON data
dictionaries and safe classic scripts. Runtime/CSS URLs also carry their asset
digest. Current manifests reference only current fragments; obsolete output
files can remain on disk after incremental builds. Distribute a clean output
tree when changing visibility; STV cannot revoke older published copies.

Operating limits and deferred decisions
------------------------------------------------------------

* Windows Firefox's local file loader needs short physical output paths. A
  detail filename contains two full SHA-256 digests; keep the complete physical
  asset path below the loader's Windows path-length limit. File workflows use
  short fixture roots, including the large-project copy.
* Supported release verification uses installed stable Firefox on Windows in
  headless automation. Touch, other browsers/platforms and occurrence mode are
  outside the initial scope.
* Remote embedded resources are not fetched or cached. Details provide static
  unavailable-resource indications and explicit links; full widget interaction
  remains available on the original documentation page.
* Performance measurements have no owner-agreed numeric latency/memory budgets
  yet. The hard 200-node limit is independently asserted. Recorded browser
  memory is the sum of process-tree working sets and can count shared pages
  more than once; it is not a private-memory or peak-allocation measurement.
* The project license remains an owner decision before external distribution.
  Internal implementation/testing does not assign one. Dependency notices and
  the selected unmodified ELK bundle/source reference are included in the wheel.

Record integrity
----------------

Intermediate release attempts remain available even when their executable
cases passed: source/test changes during review invalidate their frozen-input
claim. Their source-stability outcomes are preserved. Only the final stable
candidate can support the delivered verification disposition. The first report's
empty infrastructure Need label has a separately identified publication erratum;
its original report and XML/JSON have not been overwritten.

v0.2.0 criterion assessment
------------------------------------------------------------------------------------------

The owner accepted the centered-layout/seed-selection concept in
:doc:`concept-reviews/round-6` and invoked release-test against pre-release
revision ``bee5a15fed8e0b89a21b9cced09d7a1e67bb3c40``.
The original assessment above remains historical. The delivered scope now covers
all ten system and 53 initial-release software requirements. The four
occurrence-mode requirements remain explicitly deferred and not_assessed.

The amendment's criterion review adds the following observable evidence to the
existing system/software assessment:

* :need:`STV_SWR_003`, :need:`STV_SWR_051` and :need:`STV_SWR_052`:
  real seeded/seedless builds, initial project plus at most five entries,
  complete 201-entry/41-page traversal, empty projects, exact capacity counting,
  independent page memory and hidden-object filtering.
* :need:`STV_SWR_050`, :need:`STV_SWR_053`, :need:`STV_SWR_054` and
  :need:`STV_SWR_055`: measured hover versus explicit activation, real Escape
  outside view focus, cancellation, facing ports and safe obstacle/self-loop
  routes, computed 975px viewports, and stable semantic control ordering with
  replacement mappings. File/HTTP workflows exercise real pointer and keyboard
  behavior as well as the pure state/geometry checks.
* :need:`STV_SWR_056`: exact five-child and project centering, shared-parent
  collision avoidance, retained identity, independent noncompeting parents,
  deterministic cycles/isolated nodes/variable heights, test lanes and final
  routes. The release review found that averaging collision displacement across
  the whole band moved an unrelated parent by 109.33px. Local least-displacement
  pooling fixes that defect within the accepted layout contract; the new
  regression would fail the previous implementation. Component boundaries,
  state transitions and ADR decisions are unaffected.
* :need:`STV_SWR_057`: ID/title matching and result bounds, pointer and keyboard
  confirmation, typing/Escape, exact trimmed IDs, invalid/hidden/case-mismatched
  IDs, empty catalogs, repeated replacement, overview reset, independent seeded
  and seedless views, retained focus, and failed/stale layout preservation.
  ``tests/test_release_seeds.py`` extends the MVP smoke cases with these
  real file/HTTP paths; Node checks cover pure catalog and transition invariants.

A test synchronization defect was also corrected: the original-object workflow
asserted a newly opened tab's URL while Firefox still reported about:blank.
The test now waits for the expected URL and actual Need element, preserving and
strengthening the original criterion. The failed release attempt and separate
diagnostics remain retained; isolated passes did not substitute for full
qualification.

Final outcomes and artifact identities are in
:doc:`test-execution/0.2.0-final/index`. Canonical verification is promoted only
against the full passing candidate and this criterion review; acceptance remains
independent. Browser/platform, occurrence-mode, widget-interaction, numeric
performance-budget and external-distribution licensing limits above still apply.
