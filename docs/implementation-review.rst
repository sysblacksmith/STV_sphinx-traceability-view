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
       ``frontend/src/layout/tests/layout.test.js`` invariant assertions
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
       and project-root counting cases in ``frontend/src/state/tests/state.test.js``
   * - :need:`STV_SYS_009`
     - A wheel installs offline into a fresh Python 3.10 host and builds the
       fixture with Node absent from PATH; import resolves inside that host.
     - ``test_clean_wheel_host``
   * - :need:`STV_SYS_010`
     - Interaction workflows use the installed stable Firefox desktop binary
       on Windows, including pointer, keyboard, pan/zoom, paging and recovery.
     - ``docs/test-scripts/test_browser.py`` and ``docs/test-scripts/test_capacity.py``;
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
  ``docs/test-scripts/test_release_seeds.py`` extends the MVP smoke cases with these
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

CR014 development criterion review
------------------------------------

:doc:`test-execution/cr014-details/index` records the implemented persistent
collection and author capacity setting against round 12. The new software and
system cases pass normal, boundary, negative and asynchronous recovery paths.
Hover timing/cancellation and safe URL/content transport regressions pass;
explicit-Escape procedures now assert persistent preservation and use Close.
Seed/page replacement, keyboard focus, narrow/wide docking and current-width
Reset pass with the default ten and overridden three-box collections. Shared
loading tests cover one-slot eviction, out-of-order completion, retry and clear.
The repeated capacity, clean-wheel and source-archive checks pass. These results
support the changed requirements' verification fields, without changing unrelated
partial/deferred verification or constituting release approval.


PR015 detail acceptance correction review
-------------------------------------------

The owner's findings are resolved within existing INSPECT/RENDER boundaries;
:doc:`test-execution/pr015-details/index` retains the actual failing baseline,
127 distinct passing selected checks and refined icon/ID repeat. The 720 px dock
and 1120 px responsive boundary preserve usable graph space. Metadata defaults
folded; pointer, Enter and Space update only its copied table with consistent
icons and ARIA state. New boxes reset disclosure, reuse retains it. The artifact
ID opens its real source Need; local body fragments retain their namespace.
The actual normal demo and metadata state diagram/HTML embedding were visually
reviewed. No arbitrary host/widget script is initialized and adjacent safe
transport/offline/race/hover/package checks pass. Owner acceptance retest is
pending; no release qualification or new capacity result is claimed.

CR015-018 development implementation, 2026-10-25
--------------------------------------------------------------------------------

Input: accepted concept commit ``2c4236a`` on ``concept-cr015-018``, including
round 15 and the four owner-approved stakeholder amendments. Implementation is
an uncommitted development worktree, not a new release or deployed publication.
No dependency/version change is introduced. Development distributions remain
version 1.0.0 in an isolated directory; existing release assets are not replaced.

Delivered behavior
~~~~~~~~~~~~~~~~~~

* :need:`STV_SHR_058` / :need:`STV_SWR_066`: atomic Collapse all nodes keeps
  current roots, clears all page restoration caches, fits a fresh committed
  scene and preserves persistent cards. Layout retry repeats the rejected command.
* :need:`STV_SHR_059` / :need:`STV_SYS_011` / :need:`STV_SWR_070`,
  :need:`STV_SWR_071`, :need:`STV_SWR_072`: inert visible-area SVG capture,
  local resource/font records, preserved crop/background/scroll layout and actual
  browser downloads. Errors retain the live view. Imported active SVG and
  outside-output paths fail; unreferenced images do not enter resource records.
* :need:`STV_SHR_060` / :need:`STV_SWR_067`, :need:`STV_SWR_068`: independent
  author font scales default to 0.7, including loading/error wrappers and later
  inserted content. Baseline restoration and two-phase measurement avoid nested
  or repeated scaling, with no duplicated accessible measurement card.
* :need:`STV_SHR_061` / :need:`STV_SWR_069`: page-wide metadata controls on
  rootless and graph pages, preserving body/title, copied details and native
  individual operation. Unsupported encodings or absent host handlers produce
  disabled explanatory controls rather than partial success.

Implementation source and transition ownership are in :doc:`elements-software`
and :doc:`state-machine`. Author settings and browser save-location guidance
are in :doc:`getting-started`. The interface changes bind the accepted design
into actual function signatures and equivalent synchronous pre-paint measurement;
no stakeholder behavior, component boundary or accepted ADR choice was weakened.

Executable coverage and actual developer checks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Canonical design to executable checks
   :header-rows: 1
   :widths: 25 75

   * - Canonical cases
     - Executable selection
   * - :need:`STV_TC_SW_051`, :need:`STV_TC_SY_066`
     - ``frontend/src/state/tests/collapse-all.test.js`` and retained state/cap
       tests; ``test_collapse_all_keeps_current_roots_and_open_details``.
   * - :need:`STV_TC_SW_052`, :need:`STV_TC_SY_068`
     - ``model/tests/test_font_scale.py``, ``inspect/tests/typography.test.js``;
       ``test_font_scales_are_independent_and_applied_once`` measures both actual
       hover and persistent sizes under default, baseline and separate overrides.
   * - :need:`STV_TC_SW_053`, :need:`STV_TC_SW_055`, :need:`STV_TC_SY_067`
     - ``export/tests/*.test.js``, ``detail_build/tests/test_export_resources.py``;
       ``test_standalone_svg_visible_details`` covers file/HTTP, one/ten cards,
       empty-crop recovery, real temporary-folder downloads, background and visible
       reopened card positions after the original output directory is unavailable.
   * - :need:`STV_TC_SW_054`, :need:`STV_TC_SY_069`
     - ``render/tests/page-metadata.test.js`` and the ``test_page_*`` functions
       in ``docs/test-scripts/test_view_controls.py`` cover native individual
       operation, rootless pages and explicit unsupported/missing-handler failures.

Actual check sets are separate developer runs, not a manufactured aggregate
release execution:

* Complete frontend selection: **42 passed**.
* Complete non-browser selection excluding the separate capacity benchmark:
  **87 passed**. Its package check uses the development wheel.
* Broad Firefox selection excluding the separate capacity benchmark:
  **57 passed** before the final export/page edge refinements.
* Later delivered-scope/persistent-detail selection: **30 passed**.
* Final SVG/reset/font feature selection after crop/scroll corrections:
  **9 passed**; page-only refinements are rechecked separately on the final build.
* Clean offline wheel host without Node: **passed**, with required runtime/legal
  assets and no component tests in the runtime wheel. Final package hashes and
  source/test identity are retained in ignored developer build output.

Commands use ``.venv-implementation/Scripts/python.exe`` with installed Firefox
158.0.1 and geckodriver 0.37.1 for browser checks. For example::

   node --test src/*/tests/*.test.js
   .venv-implementation/Scripts/python.exe -m pytest -m "not browser" --ignore=docs/test-scripts/test_capacity.py -q
   .venv-implementation/Scripts/python.exe -m pytest docs/test-scripts/test_view_controls.py -q
   .venv-implementation/Scripts/python.exe scripts/check-coverage.py --strict

Run the Node command from ``frontend``. Set STV_GECKODRIVER to the installed driver
and STV_WHEEL to the new wheel for consumer checks. Browser fixture downloads are
confined to automatically cleaned temporary folders. Early identified fixture
SVGs were moved out of Downloads into ignored build output.

Developer logs/JUnit, packages, source/test identity and visual examples are under
``docs/_build/cr015-018*``. They are transient local evidence, not committed release
records. The real generated demo and an exported standalone SVG were inspected
in Firefox. Visual checks exposed inherited-background and off-screen flow-layout
issues; the implementation now captures a backdrop and empty flow placeholders,
and browser checks assert visible reopened content rather than text presence only.

Verification boundary and handover
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The four CRs are implemented. New requirement verification is conservatively
``partial``: these development checks do not constitute execution of every full
canonical case procedure, native Save As dialog qualification, the separate
30,000/90,000 capacity benchmark or a release qualification. The nine canonical
case designs remain accepted/not_run until their complete procedures are recorded;
no test_execution or historical release result was fabricated or overwritten.
Existing passing release claims retain their original candidate identities.

The development wheel/source archive are in
``docs/_build/cr015-018/distributions``. To replace the same version in a local
consumer, use pip with ``--force-reinstall --no-deps`` and the explicit wheel path
in that consumer's environment. Readers need no Node or runtime service.
User inspection and separately authorized release-test work remain before any
new release/publication claim. Implementation changes have not been committed,
pushed or deployed by this invocation.

Final local verification identity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Source/test SHA-256: ``0d79572952f63638efd7b433a6515370af15865cae2f2b7b38d65e2250fe0a50``.
The complete input file hashes and archive hashes are in
``docs/_build/cr015-018/source-identity.json``. The wheel's packaged stv.js was
compared byte-for-byte with the final rebuilt asset; runtime tests are excluded.

Final page-control retest: four passes, including explicit missing-host and
body-target refusal and collision-safe ARIA row references. Final export retest:
four passes (file/HTTP, one/ten cards), including actual temporary-folder file
bytes, visible reopened content, and plaintext-password exclusion. Final resource
and font validation selection: fourteen passes, including UTF-8/UTF-16 entity
rejection. These supersede only their affected earlier developer checks; they
are not combined into a fictitious release run.

Source whitespace checks exclude generated stv.js, whose vendored raw string
literals legitimately retain trailing spaces; the generated bytes are not trimmed.
Strict documentation, graph/evidence/test coverage and published diagram checks
are recorded in :doc:`maturity`. No additional implementation commit was made.

CR019 remembered views
----------------------

STATE snapshot/storage validation, RENDER checkbox/mount/D3 wiring, LAYOUT
position/band restoration and INSPECT focus-free ordered reopening implement
:need:`STV_SWR_073`, :need:`STV_SWR_074`, :need:`STV_SWR_075`.
:doc:`test-execution/cr019-development/index` retains the exact source/test
identities and development evidence. Current maturity and qualification limits
are centralized in :doc:`maturity`; concept acceptance is in
:doc:`concept-reviews/round-16`.
