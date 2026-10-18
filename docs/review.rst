Review and scope decisions
==========================

Resolved stakeholder questions
------------------------------

All decisions below were clarified with the project owner on 2026-10-18.
The project owner accepted requirements STV_SHR_001 through STV_SHR_046 as
stakeholder baseline v1 on 2026-10-18; see :doc:`sources`. Acceptance records
agreement to the requirements, not implementation or successful verification.

* **Resolved ? navigation:** Explore incoming and outgoing relationships from
  any displayed object, with separate model-labeled controls for each direction
  (:need:`STV_SHR_013`, :need:`STV_SHR_035`). Empty types have no controls;
  isolated nodes show "No related objects" (:need:`STV_SHR_029`).
* **Resolved ? model integration:** Reuse the host project's Sphinx-Needs type
  and relationship definitions, supplemented by replaceable layout and
  accepted-status mappings. Additional ordered levels are allowed; invalid
  required mappings fail the build (:need:`STV_SHR_014`, :need:`STV_SHR_032`,
  :need:`STV_SHR_036`, :need:`STV_SHR_037`, :need:`STV_SHR_045`).
* **Resolved ? inspection:** Nodes show ID and shortened title. Hover details
  contain all information displayed by the full Need object, without field
  selection settings. Long tooltips stay within the window and remain open
  while hovered, with scrolling. Node activation opens the original object in
  a new tab (:need:`STV_SHR_008`, :need:`STV_SHR_015`, :need:`STV_SHR_016`,
  :need:`STV_SHR_033`).
* **Resolved ? deployment:** Generated documentation works offline from disk
  and on static hosting without an application server
  (:need:`STV_SHR_017`, :need:`STV_SHR_018`).
* **Resolved ? shared objects:** One shared node is the default. Independent
  separate occurrences and mode switching are retained as later-scope features.
  Switching preserves exploration state; shared mode displays the union of
  expanded traces (:need:`STV_SHR_019` through :need:`STV_SHR_023`).
* **Resolved ? cycles and collapse:** Cycles close through a connection or
  reference without endless repetition. Collapsing a branch retains objects
  reachable through other open paths (:need:`STV_SHR_024`, :need:`STV_SHR_025`).
* **Resolved ? invalid starting ID:** Omitted and unknown IDs fail the build
  with an error identifying the invocation (:need:`STV_SHR_026`).
* **Resolved ? broken traces:** The host build validates and fails broken
  traces; the extension still renders valid data and marked missing-target
  placeholders containing the target ID (:need:`STV_SHR_027`, :need:`STV_SHR_028`).
* **Resolved ? type colors:** Reuse host type colors, with a built-in default
  scheme for omitted colors (:need:`STV_SHR_030`).
* **Resolved ? acceptance styling:** Red node borders mark states outside the
  model-defined accepted values, defaulting to ``accepted``. Missing and empty
  statuses count as not accepted (:need:`STV_SHR_031`, :need:`STV_SHR_032`).
* **Resolved ? test placement:** Test cases appear to the right of artifacts.
  A shared test node is to the right of all connected artifacts; later separate
  occurrences appear beside their respective artifacts (:need:`STV_SHR_012`).
* **Resolved ? interaction scope:** Keyboard operation with visible focus,
  independent views per page, zoom and pan are required initially
  (:need:`STV_SHR_034`, :need:`STV_SHR_038` through :need:`STV_SHR_040`).
* **Resolved ? compatibility:** Firefox desktop on Windows; Python 3.10+,
  Sphinx 8.1.3 and Sphinx-Needs 8.2.0 initially
  (:need:`STV_SHR_041`, :need:`STV_SHR_042`).
* **Resolved ? capacity:** Projects may contain tens of thousands of Needs.
  Each view permits at most 200 visible occurrences, including duplicates and
  placeholders. An expansion or mode switch exceeding the cap leaves the view
  unchanged with an explanation (:need:`STV_SHR_043`, :need:`STV_SHR_044`).
* **Resolved ? distribution:** Deliver a reusable, installable Sphinx extension
  for use in other documentation projects (:need:`STV_SHR_046`).
* **Resolved ? configuration scope:** Avoid separate settings for every visual
  detail; fixed node contents and full-object tooltips need no field-selection
  configuration. This preserves the explicitly agreed model mappings.

Agreed MVP scope
----------------

Start with shared-node mode only. Embed a seeded view in RST, navigate in both
directions, preserve model-defined artifact levels, inspect objects and produce
self-contained HTML for Firefox on Windows. Reuse host model definitions with
additional layout and acceptance mappings. Include type/status styling,
independent views, keyboard operation, zoom, pan and the capacity constraints.
Deliver the extension as a reusable installable package.

The ``release_initial`` and ``release_later`` tags record release allocation
independently of priority and review status. Requirements involving both modes
apply to the shared-node workflow initially; their separate-occurrence and
switching clauses apply when the later mode is delivered.

Deferred features ? scope resolved
----------------------------------

* Separate-occurrence mode, its selector, independent occurrence expansion and
  cross-mode state preservation/combination: later scope
  (:need:`STV_SHR_019`, :need:`STV_SHR_021`, :need:`STV_SHR_022`,
  :need:`STV_SHR_023`). No later release number is assigned.
* Touch interaction, including alternatives to hover: deferred beyond the MVP.
* Other browsers, Linux and macOS: deferred beyond the MVP.
* Other Sphinx and Sphinx-Needs versions: deferred beyond the MVP.

Remaining refinement ? not blockers for design
----------------------------------------------

Detailed elicitation is paused at the owner's request. Resolve these through
architecture work, prototype feedback and later requirement refinement:

* Model input mechanism and precise required mapping schema.
* Fixed title-shortening rule.
* Behavior of links to documentation outside an offline bundle.
* Exact large-project benchmark, relationship density and response-time targets.
* Later-mode behavior when shared-mode navigation changes saved independent
  occurrence states.
* Additional accessibility criteria beyond the agreed keyboard workflow.

Working assumptions ? not confirmed obligations
-----------------------------------------------

* Exploration is read-only; editing Needs is outside the current draft.
* Unrevealed ancestors need not be displayed automatically.

Method and coverage
-------------------

Stakeholder baseline v1 remains accepted. The internal specification now adds
10 draft system requirements, 46 draft software requirements and proposed
architecture allocations. These establish structural traceability, not product
implementation or successful verification. All three ADRs remain proposed.
The host model may contain test-case and other types beyond the five types used
by this project's requirements documentation. Their visualization uses the
agreed model integration; no extension of the shared documentation method is
implied. No high-level scope questions remain blocking design.

Internal design review gaps
---------------------------

The design is documented in :doc:`architecture-system`,
:doc:`architecture-software` and :doc:`internal-interfaces`. Open prototype tasks:

* Demonstrate final-rendered Need extraction and URL/ID/media rebasing across
  documents on the pinned toolchain. Full host rendering, rather than raw field
  reconstruction, is essential to STV_SHR_015.
* Verify local classic-script loading and the overlay workflow from file URLs
  in Firefox/Windows. Static-only operation is designed, not yet demonstrated.
* Measure the proposed 30,000-Need/90,000-edge fixture; agreed numeric latency
  and memory budgets are still absent. Payload size grows with project size.
* Evaluate layout quality with mixed ranks, direct channeling, cycles and
  shared tests. Geometry and keyboard checks need implementation fixtures.
* Verify Python 3.10 and record exact release verification environments.
* Validate incremental regeneration, purge behavior and dependency ordering.
  Do not claim parallel build safety until it has dedicated validation.
* Review and accept internal requirements and ADRs separately. Their current
  draft/proposed state must not inherit stakeholder acceptance.

First vertical slice: install the package in a separate fixture, embed two
seeded views, follow a cross-page relationship in both directions, inspect its
full details, and verify local-file operation before adding the remaining MVP
interactions. Later occurrence mode remains deferred.

Revision history
----------------

- 2026-10-18: Added draft internal requirements, proposed system/software
  elements, architecture diagrams, interfaces and three proposed ADRs.

- 2026-10-18: Project owner accepted STV_SHR_001 through STV_SHR_046 as
  stakeholder requirements baseline v1. All priorities remain unassigned and
  verification states remain not_assessed.

- 2026-10-18: Reconciled all clarified topics as resolved, separated deferred
  scope from remaining refinement, confirmed the shared-node MVP, host-model
  reuse and reusable extension delivery.

- 2026-10-18: Extended STV_SHR_044 to blocked mode switches and recorded the
  owner's request to pause detailed elicitation in favor of high-level MVP scope.

- 2026-10-18: Refined STV_SHR_043 to count duplicate occurrences and
  missing-target placeholders toward the 200-node limit.

- 2026-10-18: Added STV_SHR_044 for atomic rejection of expansions exceeding
  the node limit, with an explanatory message.

- 2026-10-18: Added STV_SHR_043 for projects with tens of thousands of Needs
  and a maximum of 200 visible nodes per view.

- 2026-10-18: Added STV_SHR_042 for the agreed initial documentation toolchain.

- 2026-10-18: Restricted STV_SHR_041's initial platform scope to Windows and
  deferred Linux and macOS support.

- 2026-10-18: Added STV_SHR_041 for Firefox desktop as the sole initial browser
  target; deferred support for other browsers.

- 2026-10-18: Added STV_SHR_039 and STV_SHR_040 for initial-release zoom and pan,
  and extended keyboard-operation coverage to include them.

- 2026-10-18: Added STV_SHR_038 for multiple independent views per page,
  explicitly allocated to the initial release.

- 2026-10-18: Added STV_SHR_037 for extensible model-defined artifact levels
  and identified the previously specified hierarchy as the default.

- 2026-10-18: Added STV_SHR_036 for build-time rejection of invalid or incomplete
  input models, preserving explicitly agreed defaults.

- 2026-10-18: Refined STV_SHR_012 for test cases linked to multiple artifacts
  in both display modes.

- 2026-10-18: Refined STV_SHR_031 to treat missing or empty status values as
  not accepted.

- 2026-10-18: Refined STV_SHR_030 to use a built-in default color scheme for
  artifact types lacking configured colors.

- 2026-10-18: Refined STV_SHR_030 to reuse host Sphinx-Needs type colors rather
  than introducing another palette configuration.

- 2026-10-18: Added STV_SHR_035 for separate model-labeled incoming and outgoing
  expansion and collapse controls.

- 2026-10-18: Recorded touch support as a deferred feature beyond the initial
  release, without assigning a later release.

- 2026-10-18: Added STV_SHR_034 for keyboard-only operation and visible focus.

- 2026-10-18: Added STV_SHR_033 for bounded, persistent-on-hover, scrollable
  tooltips.

- 2026-10-18: Refined STV_SHR_015 to show all full-object information in the
  tooltip without configurable field selection; recorded the preference to
  limit configuration.

- 2026-10-18: Added STV_SHR_032 and refined STV_SHR_031 for model-defined
  accepted-status values, defaulting to accepted.

- 2026-10-18: Added STV_SHR_031 after confirming that status highlighting
  applies to node borders.

- 2026-10-18: Refined STV_SHR_008 to fixed ID/title node contents, added
  STV_SHR_030 for artifact-type backgrounds, and recorded the status-color
  clarification needed.

- 2026-10-18: Extended STV_SHR_026 to reject omitted starting IDs as well as
  unknown IDs.

- 2026-10-18: Added STV_SHR_029 for nodes without relationships and controls
  for nonempty relationship types only.

- 2026-10-18: Added STV_SHR_028 for missing-target placeholders.

- 2026-10-18: Added STV_SHR_027 to separate host broken-trace validation from
  extension rendering.

- 2026-10-18: Added STV_SHR_026 to reject unknown starting IDs at build time.

- 2026-10-18: Added STV_SHR_025 for retaining objects reached through other open
  paths when a branch is collapsed.

- 2026-10-18: Added STV_SHR_024 for finite cycle presentation in both display modes.

- 2026-10-18: Added STV_SHR_022 and STV_SHR_023 for independent occurrence
  expansion and the union of expanded traces when switching to shared mode.

- 2026-10-18: Added STV_SHR_021 to make the expected preservation of expansion
  state explicit when switching display modes.

- 2026-10-18: Added STV_SHR_020 for the confirmed shared-node default.

- 2026-10-18: Added STV_SHR_019 for selecting shared-object presentation in the
  view itself.

- 2026-10-18: Added STV_SHR_017 and STV_SHR_018 for offline use and static hosting
  without an application server.

- 2026-10-18: Refined STV_SHR_008 to cover node summaries and added STV_SHR_015
  and STV_SHR_016 for hover details and opening original objects in new tabs.

- 2026-10-18: Added STV_SHR_014 for a configurable, replaceable input data model.

- 2026-10-18: Added STV_SHR_013 for explicitly confirmed bidirectional navigation
  and resolved the directionality question.

- 2026-10-18: Initial draft from the project owner's description. Created stable
  IDs STV_SHR_001 through STV_SHR_012. All requirements remain drafts; priorities
  and release allocations remain unassigned.

- 2026-10-18: Converted the initial Markdown draft into canonical RST Needs, preserving all 12 IDs; added the shared-method documentation structure.

