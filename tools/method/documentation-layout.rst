Shared project documentation layout
===================================

This is the authoritative layout reference for engineering projects. Use
its structure for new projects unless the owner chooses another layout.
Preserve an existing project’s established structure; migrate it only
when the owner authorizes that change. The shared method owns data-model
and lifecycle semantics. Keep folder and filename policy here rather
than duplicating it in individual skills.

Use this layout for new reconstructed documentation unless the user
requests another structure or the existing project has an established
one. Preserve project-specific scope, titles and decisions. Use the
landing template and replace its three ``{{...}}`` project placeholders;
keep generated requirements and evidence in the project, in the project.

Target directory tree and initialization
----------------------------------------

Paths below are relative to the project root. ``docs/`` is the default
Sphinx source root; preserve an explicitly selected alternative. The
tree describes locations, not a requirement to fabricate artifacts.

.. code:: text

   project/
   |-- README.rst                         Project setup and usage
   |-- docs/
   |   |-- conf.py                        Shared model and rendering configuration
   |   |-- index.rst                      Chapter navigation
   |   |-- requirements-stakeholder.rst                Stakeholder requirements
   |   |-- requirements-system.rst                     System requirements or explicit gap
   |   |-- requirements-software.rst                   Software requirements or explicit gap
   |   |-- architecture-system.rst         System architecture view or gap
   |   |-- elements-system.rst             System elements or gap
   |   |-- architecture-software.rst       Software architecture view or gap
   |   |-- elements-software.rst           Software elements or gap
   |   |-- architecture-decisions.rst      ADR index (first Architecture entry)
   |   |-- state-machine.rst               Behavioral state machines
   |   |-- technology-stack.rst            Selected dependencies and toolchain
   |   |-- architecture/
   |   |   |-- decisions/                 Stable project ADR records
   |   |   `-- diagrams/                  Adjacent editable Draw.io/SVG pairs
   |   |-- change-requests/
   |   |   |-- index.rst
   |   |   `-- <PROJECT>_CR_001_<slug>.rst  Initial owner request; append in order
   |   |-- problem-tickets/
   |   |   |-- index.rst
   |   |   |-- report.rst.template
   |   |   `-- <PROJECT>_PR_001_<slug>.rst Ticket; adjacent prefixed attachments
   |   |-- test-cases/
   |   |   |-- index.rst
   |   |   |-- system-tests.rst           Integrated system test specifications
   |   |   `-- software-tests.rst         Software component test specifications
   |   |-- test-scripts/
   |   |   |-- index.rst
   |   |   |-- test_*.py                  Cross-component/system Python checks
   |   |   `-- fixtures/                  Test inputs; exclude RST from discovery
   |   |-- test-execution/                 Retained release execution evidence
   |   |-- concept-reviews/                Historical review rounds
   |   |-- project-metrics.rst             Nine status charts under Scope management
   |   |-- maturity.rst                    Central readiness and review history
   |   |-- review.rst                      Scope decisions and review register
   |   |-- sources.rst                     Source provenance
   |   `-- method.rst                      Local versioned method wrapper
   `-- scripts/                            Project tooling and shared tool links

During stakeholder elicitation, initialize configuration, navigation,
the requirement/architecture scaffold and explicit downstream gaps,
maturity/review/source records, the local Methods wrapper, and all four
sibling record folders with their indexes. Capture the actual initial
owner prompt in the first change request immediately; start further
records for substantive requests or coherent clarifications. Do not
invent tickets, test cases, executable tests, architecture decisions or
acceptance to populate the scaffold. Empty directories need not be
committed until they contain real files; the four record indexes keep
their locations present from the start.

Concept creation adds interface contracts, implementation/verification
plans and technology selections when authored. Implementation fills
executable scripts and fixtures; release validation adds execution
records. Use language-appropriate source/build layouts for product code
and frontend tests rather than imposing Python on every project. Keep
test-source naming references discoverable from the script index.

Chapter groups and ordering
---------------------------

1. **Scope management:** ``change-requests/index`` (**Change
   Requests**), ``problem-tickets/index`` (**Problem Tickets**),
   ``project-metrics`` (**Project Metrics**).
2. **Requirements:** ``requirements-stakeholder``,
   ``requirements-system``, ``requirements-software``.
3. **Architecture:** ``architecture-decisions``,
   ``architecture-system``, ``elements-system``,
   ``architecture-software``, ``elements-software``, ``state-machine``,
   ``technology-stack``, ``traceability``.
4. **Verification and Validation:** ``verification-plan``,
   ``test-cases/index``, ``test-scripts/index``, ``test-coverage``,
   ``test-execution/index``.
5. **Miscellaneous:** ``internal-interfaces``, ``implementation-plan``,
   ``review``, ``maturity``, ``sources``.
6. **Utilities:** ``method``, whose visible chapter title is
   **Methods**.

Use separate system/software element pages. The architecture views are
titled **Architecture View for System** and **Architecture View for
Software** and embed the project’s internal SVGs at 100% content width.
Author architecture pictures in Draw.io, retain editable .drawio sources
directly beside their same-basename .svg exports in the same directory,
and export SVG only. Follow the central method’s architecture-diagram
authoring rules, including portable links from element boxes to their
Need records and interactive HTML embedding that preserves those links.
Build these views from evidenced architecture; if diagrams do not exist,
create them from inspected evidence or explicitly record the gap. Never
invent components to fill a template. Blank lines must separate toctree
options from entries.

Title ``state-machine.rst`` **Behavioral state machines**. Place it
directly after the software element page and before the technology
stack, following the Architecture order above. Keep the title and
navigation stable across phases; early scaffolds state the
behavioral-design gap without inventing states or transitions.
Implementation maintains the actual behavior under the shared method.
Use the state-machine starter and technology-stack starter for explicit
initial gaps.

The **Architecture Design Decisions** page
(``architecture-decisions.rst``) indexes project ADRs stored under
``architecture/decisions/`` and includes them in a toctree. Follow the
shared method for their content, evidence, lifecycle and supersession
links. Include historical records as well as current decisions; if none
are available, record the gap without inventing decisions.

The Methods chapter includes the complete local method.rst from the
imported package. Preserve Docutils include dependency tracking. Updates
are explicit imports; the build never reads another repository.

When concept creation adds the technology stack, list it directly in the
root Architecture toctree, not under the ADR index. Interface contracts
and implementation plans belong directly in the root Miscellaneous
toctree. Verification plans, test-case and executable-script indexes,
coverage and execution records belong in the separate top-level
**Verification and Validation** group, in the order above. Keep
maturity/readiness history in Miscellaneous and the nine generated
status charts in Project Metrics under Scope management; link
verification evidence without duplicating its navigation. Add these
entries when their pages are authored; stakeholder-only scaffolds may
keep these future entries absent until that phase. The ADR index
contains ADRs rather than acting as a general supporting-document
folder.

Central maturity and review history
-----------------------------------

Initialize ``maturity.rst`` from the maturity template and
``project-metrics.rst`` from the metrics template alongside the landing
page. Follow the central method: current maturity/readiness history
lives in Miscellaneous, while generated charts live in Project Metrics
under Scope management; each concept-review round has a separate linked
RST file with explicit assessed Need/document links. Keep the artifact’s
canonical status and design in its source; keep dated
maturity/review/lifecycle history centrally. Do not create review-only
changes to otherwise unchanged artifacts.

Local rendering code and style
------------------------------

Import status_charts and traceability_model from tools/method/tooling.
Use tools/method/static as a local Sphinx static asset path, with
wide-layout.css in html_css_files. Enable sphinx_needs, sphinx_rtd_theme
and status_charts plus need_controls and method_version by default. All tooling and assets are checked into the consuming
project.

The ``need_controls`` extension adds **Collapse all** and **Expand all** on
pages containing Sphinx-Needs objects. They hide/show only collapsible metadata,
preserving titles, bodies and individual controls. Copied detail cards are excluded.
Unsupported host markup disables the buttons with an explanation. Where STV
already provides page controls, the shared script reuses that group.
Include ``need_controls`` in ``extensions`` with the local tooling directory on
``sys.path``; the extension registers its JavaScript and CSS automatically.
Keep ``tools/method/static`` in ``html_static_path``. This requires no Node build
or STV installation and works with local HTML files.

Preserve any required project extensions or static assets. Start with
the tested dependency pins. The default theme is Read the Docs with the
content width limit removed. On desktop, all four chart rows use the
same three-column grid: three requirement charts, then two
architecture-element charts, then two test-case charts and two
scope-management charts; each two-card row leaves the rightmost column
empty. On narrow screens the cards stack. Never generate a fake third
architecture chart to fill the grid.

Dashboard semantics
-------------------

Use ``.. status-pie:: TYPE`` with ``shr``, ``sysr``, ``swr``, ``syse``,
``swe``, ``test_case``, ``problem_report`` or ``change_request``. Place
nine generated charts on ``project-metrics.rst``, titled **Project
Metrics**, under Scope management: three requirement cards, two element
cards, then two test-case maturity cards and two scope-management status
cards. For the test-case charts use ``:tag: test_system`` and
``:tag: test_software``, respectively, selecting canonical ``test_case``
Needs by exact tag membership. Include a ``need_count`` total with the
same type/tag predicate on each card. Do not infer populations from
requirement links or execution outcomes. The landing page provides
stable chapter navigation instead of duplicated maturity prose or
counts.

The shared extension reads actual Sphinx-Needs items and the status enum
from the shared model’s type-specific status mapping, rather than
hard-coding status filters in each landing page. Requirement, element
and test-case review states are draft, reviewed and accepted (gold,
blue, green). Problem reports and change requests use their independent
lifecycles defined below.

All legends always show state, count and percentage, including
zero-count states. Percentages within the pies are 15 pt bold and
displayed only for slices of at least 5%; legends are 16 pt before
display scaling. All nine charts have the same figure size and card
width. Empty categories display a no-data message rather than fabricated
proportions. Status means artifact review or record lifecycle, not
verification pass/fail.

Following STV_CR_015, the shared stylesheet displays all pie charts at
80% of the previous linear dimensions, preserving aspect ratio,
grid/card layout and responsive limits. This includes the Problem
Tickets chart and both new test-case charts relative to the former
maturity-chart baseline. Keep the 6.4 x 5.8 inch rendering canvas;
changing the canvas alone does not establish browser display size.
Compare actual width and height at matching viewport/layout conditions,
including narrow screens; check readable legends and no
clipping/overlap. Imported renderer/style updates affect consumers on
rebuild; adding the two cards to an existing project’s metrics page
requires updating its project source within the authorized scope. Do not
change canonical statuses, coverage, execution history or acceptance
claims to populate charts.

Validation
----------

Build HTML with warnings as errors and run the shared graph validator.
Check all nine charts against exported type/status counts and exact
test-case tags, including mixed categories, zero-count legends and empty
categories. Check the independent problem-report lifecycle as well.
Verify the generated navigation follows the chapter groups above,
internal SVGs are embedded, and the Methods chapter contains the master
text and tables. Confirm both the renderer and CSS resolve to local
imported files. Imported method updates must appear after rebuilding;
never edit generated SVG charts, HTML, JSON or CSV by hand.

Local Draw.io export tooling
----------------------------

Use tooling/export-architecture.ps1 and
tooling/normalize-diagram-links.py from the imported package. Pass
-ProjectRoot explicitly. Keep adjacent .drawio/.svg pairs. The wrapper
exports SVG using Draw.io and restores portable source links. Run the
normalizer with –diagram-dir PATH and optionally –published-dir HTML for
target validation. No symbolic links to another checkout are needed.

User problem intake folder
--------------------------

Initialize ``problem-tickets/`` immediately below the Sphinx source
directory from the folder template. Include its index under Scope
management as **Problem Tickets**, and copy the adjacent
``report.rst.template`` starter without instantiating a fake issue.
Users hand over reports and attachments here; the problem solver returns
analysis and fix evidence into the same stable records. Use
``problem_report`` Needs with new/analyzed/fixed states. Keep the
existing seven review-status charts; the report index adds its own
``status-pie:: problem_report`` chart and all-status table. Never mix
report states into review chart legends. Reports are outside
requirement/allocation coverage and use body Need/doc links.

Record folders and chronological filenames
------------------------------------------

Initialize ``change-requests/``, ``problem-tickets/``, ``test-cases/``
and ``test-scripts/`` directly below the Sphinx source root during
stakeholder elicitation. Include their index pages in the documentation
navigation; create empty indexes rather than invented records or tests.
Cross-component/system test scripts use ``docs/test-scripts/`` by
default, adjacent to the test-case specifications; component unit tests
belong inside their owning component directories. Configure test
collection across both locations, package exclusions and Sphinx fixture
exclusions accordingly. Keep language-specific test tooling with its
components and list plain-text source paths in the script index.

Change-request filenames use ``<PROJECT>_CR_001_<slug>.rst``,
incremented in originating-request order. The initial owner prompt
starts the sequence during elicitation, before an accepted baseline
exists. Save each subsequent substantive owner request or coherent
clarification as the next record, with date/provenance,
language-corrected prompt text, scope, affected Need links and actual
decisions. Distinguish initial requests from post-baseline amendments;
creating a request record does not imply acceptance. Never fabricate
inaccessible prompt text or attribute later refinements to the original
prompt. Preserve IDs/numbers after assignment; append new records
without renumbering history.

Problem-ticket filenames begin with their stable ``problem_report`` Need
IDs and include a short descriptive suffix as specified below, with
adjacent attachments named using the same ID prefix. Retain
``problem_report``, test-case and execution semantics and typed
relations; folder names do not introduce new Need types. Use stable
``<PROJECT>_TC_SY_001`` and ``<PROJECT>_TC_SW_001`` Need IDs with
independent category counters across the corresponding system/software
documents, following the central method; do not require a file per case.
Keep archived execution logs, hashes and original selectors unchanged
during migrations, and record the old-to-new path mapping.

New ticket filenames use ``<PROJECT>_PR_001_<slug>.rst``, for example
``STV_PR_014_invisible-viewport-boundary.rst``. Use a short lowercase,
hyphen-separated description as for change requests. The canonical Need
ID stays ``STV_PR_014``, and attachments keep that stable ID prefix.
Preserve existing filenames unless a migration is explicitly requested.

Migration of existing projects
------------------------------

An established layout is not an instruction to rename a project
automatically. Obtain owner authorization for structural migrations;
reuse authorization already given for the requested move. Preserve
canonical Need IDs, typed relations and assigned record numbers.
Determine original request order from source evidence and history;
disclose uncertain ordering instead of inventing timestamps. For
imported records assign numbers once, then never renumber existing
requests merely because an older request is later recovered.

Update current document links, evidence paths, selectors, attachment
paths, pytest configuration, fixture-root calculations, build/package
configuration and generators together. Preserve archived execution logs,
historical hashes and original selectors; record the old-to-new mapping.
Build Sphinx with warnings as errors, validate traceability/evidence and
run checks affected by the path changes. Do not claim prior review
hashes or test results validate changed artifacts automatically.

Architecture-owned source components
------------------------------------

Each software architecture element has a clearly named implementation
directory with its source code, colocated unit tests (normally
``tests/``) and a short boundary README. Use the element’s canonical ID
suffix or a matching stable name so ownership is apparent without
hyperlinks. Record the convention in the element description and keep
names consistent across architecture, source and tests. Keep public
entry-point shims and generated delivery assets explicitly owned rather
than inventing architectural elements for incidental files.

Use language-native source roots, for example
``src/<package>/<component>/`` and ``frontend/src/<component>/``; do not
force separate toolchains into a single package. If an element spans
implementation roots, make ownership explicit or refine the
architectural boundary. Detailed design may be added within the owning
component later; do not fabricate design or unit-test evidence during
elicitation. Integration, browser, installation and release checks
remain under the system test-script location. Configure test collection
and traceability hooks to include all locations. Exclude unit tests and
development-only boundary files from runtime packages where appropriate,
and verify the actual package contents and clean installation.

System and software test specifications
---------------------------------------

Initialize ``test-cases/system-tests.rst`` and
``test-cases/software-tests.rst`` during elicitation, linked through
``test-cases/index.rst`` under Verification and Validation. Start with
explicit empty documents; append real canonical ``test_case`` Needs as
they are authored. Default to one document per verification level, with
an ID-prefixed section for each case. Canonical identity and execution
links belong to the Need ID, not the filename. Split into
component/feature documents later only when size warrants it or the
owner requests it; preserve IDs and navigation when doing so.

Classify by the boundary actually exercised: system cases check the
integrated product through its public interfaces, including applicable
host, browser and installation behavior; software cases check individual
components or internal software integration. A test’s linked requirement
prefixes alone do not determine its level. Preserve legitimate
cross-level ``verifies`` links without duplicating the case or inferring
requirement verification. Use the common ``tags`` field (``test_system``
or ``test_software``) for separately filtered overviews; do not add a
competing test type or status enum. Planned/manual cases follow their
intended verification boundary and remain unexecuted until real evidence
exists.

Plain-text source ownership in published documentation
------------------------------------------------------

Describe implementation and unit-test ownership through naming
conventions and plain repository-relative text, such as
``src/<package>/<component>/tests/``. Do not create local filesystem
links, ``file://`` URLs or Sphinx ``:download:`` links to implementation
code, unit-test sources or component READMEs. Apply this to element
descriptions, source inventories, state-machine ownership and coverage
generators so regenerated pages preserve the convention. Local checkout
paths are not publication locations.

Keep ordinary published documentation/Need cross-references and
canonical repository/release URLs. Deliberately published verification
evidence attachments are separate from implementation-source navigation;
preserve their established publication and historical-evidence policy.
Check generated pages as well as authoring sources for unwanted
source-download links.

Ticket chapter titles
~~~~~~~~~~~~~~~~~~~~~

Use the stable report ID in every problem-ticket chapter title, for
example ``PRJ_PR_001: Facing edge ports``, rather than
``Problem 1: ...``. The ID must match the filename’s ID prefix and
``problem_report`` Need ID; keep the Need’s human-readable title. In
``report.rst.template``, replace ``REPORT_ID`` consistently and
calculate ``REPORT_CHAPTER_UNDERLINE`` for the complete ID-prefixed
heading. Set ``REPORT_FILENAME`` to the actual filename including its
slug and ``.rst`` suffix so evidence paths resolve correctly. Preserve
IDs, existing record paths and historical evidence when changing
navigation/titles.

Scope-management metrics and change-request status
--------------------------------------------------

Metrics contains nine charts: the seven requirement/element/test-case
charts plus a **Scope management status** subsection with problem
tickets and change requests. Use ``status-pie:: problem_report`` and
``status-pie:: change_request``, with matching ``need_count`` predicates
for the same canonical types. Problem states remain new/analyzed/fixed;
CR states are draft/accepted/implemented. Both types are real
Sphinx-Needs records with the common metadata defined in the shared
method, outside mandatory requirement allocation/coverage.

Use one ``.. change_request::`` per existing CR file; preserve stable
IDs and filenames and retain legacy document labels on migration. Its
body preserves the complete originating request and context; use rubrics
instead of nested section headings. Do not infer lifecycle states from
prose or passing tests. Do not create duplicate ordinary-document status
fields or an Unclassified Need state. Empty populations render the
no-data message and zero count. Add a CR needtable to the Change
Requests index. The adjacent ``change-requests/request.rst.template`` is
a non-instantiated starter. CR colors use gold for Draft, blue for
Accepted and green for Implemented. Keep nine charts at the shared 80%
linear display size with responsive rows. Tagged chart populations use
distinct safe SVG filenames.

The ``method_version`` extension renders the version immediately before Purpose
and limits from the imported ``.method-package.json`` at build time. It tracks
the manifest as a build dependency and rejects missing or invalid versions.
