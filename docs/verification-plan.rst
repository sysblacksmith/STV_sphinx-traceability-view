Implementation verification plan
====================================

Planned checks, execution environments, fixtures and release gates.

Canonical test and execution records
--------------------------------------------------------------------------------

The :doc:`test-cases/index` contains the concept's concrete verification
procedures and explicit requirement links. The executable inventory in
:doc:`test-coverage` supplements those modeled cases. Case design acceptance
does not imply execution; unexecuted cases use ``last_result: not_run``.

The case index separates :doc:`test-cases/system-tests` from
:doc:`test-cases/software-tests`. System cases exercise the integrated Sphinx,
browser or installation boundary; software cases exercise isolated components.
Requirement links can span levels and are preserved independently of the
classification. Case IDs are stable across these directory moves.

For each actual attempt, retain one ``test_execution`` Need per executable
case in the release execution folder. Link it from its test case using
``executed_by`` and record timestamp with timezone, actual result, candidate,
test/environment identity and JUnit/log evidence. Synchronize ``last_result``
with the latest linked attempt without overwriting earlier records. Suite
results and criterion-level verification remain separate assessments.

Run structural coverage validation with ``--require-test-coverage`` and export
the requirement/test/execution matrix using ``--test-csv``. Planned
occurrence-mode coverage is retained for all later requirements, but those
cases have no delivered executable or passing execution claim. The release
must separately assess execution coverage of the delivered scope.

Execution environments
--------------------------

Use pytest for Python/integration/browser checks and Node's native test runner
for JavaScript state/layout checks. Use a separate implementation environment
from the current documentation-only environment; the selected direct pins and
npm lock are in ``docs/architecture/implementation``. No browser driver or Node
runtime is required by documentation readers or wheel consumers.

Release-browser checks use Selenium, stable Firefox and a compatible explicit
geckodriver on Windows. Provision binaries before the test run. Record binary
versions and paths, Windows version, Python version and installed STV wheel
hash in the result. Verify the minimum Python 3.10 build environment and the
developer environment separately. Do not substitute a patched browser for the
release-browser result.

.. list-table:: Required test groups
   :header-rows: 1
   :widths: 15 45 40

   * - Group
     - Behavior and fixture
     - Requirement coverage
   * - Host/model
     - Zero/one/multiple seeds, duplicate IDs, forward references, alternate host names, extra ranks, accepted-state override, missing colors, invalid required mappings.
     - STV_SWR_001, 002, 014, 026, 030, 032, 036, 037, 042, 045, 046.
   * - Graph/state
     - Chain, diamond, self-loop, A-B-C-A, reverse traversal, collapsed isolated cycle, exact 199/200/201 bounds and dangling targets.
     - STV_SWR_003 through 007, 013, 020, 024, 025, 027 through 029, 043, 044.
   * - Geometry
     - Mixed semantic ranks, reverse edges, direct channeling, tests shared across ranks, long IDs, variable group heights and added hardware rank.
     - STV_SWR_008 through 012, 037; assert nonoverlap and authoritative ranks, not an exact screenshot of solver coordinates.
   * - Rich details
     - Custom metadata, formatted body, tables, images, nested pages, relative and fragment links, srcset, duplicate DOM IDs and part references.
     - STV_SWR_015, 016, 017, 018, 033; compare displayed data and links to the original published object.
   * - Browser
     - Hover travel/scroll, keyboard open/dismiss, original new-tab link, click versus drag, zoom/pan, visible focus, two independent views and errors announced.
     - STV_SWR_004, 008, 016, 028, 029, 031, 033 through 035, 038 through 041.
   * - Packaging
     - Install wheel in independent host; include scripts/styles/licenses; build with Node unavailable; changed/deleted Need and changed mapping rebuild coherently.
     - STV_SWR_001, 015, 017, 018, 026, 027, 042, 045, 046.

Run each browser workflow from a file URL and from ``http.server`` mounted
under a nested documentation path. For offline checks, pre-provision binaries,
disable external networking in the test environment and ensure no CDN/API
requests are needed. WebDriver uses its local control channel, which is not a
product runtime network dependency. Local classic detail scripts must load from
disk. Test external documentation links separately: an unavailable external
destination is not falsely presented as locally cached content.

Host failure ownership
--------------------------

Configure the broken-link fixture with the host's dangling-link warning policy
and warnings-as-errors. Assert a nonzero build result owned by host validation
while valid graph data and a missing-target placeholder are still generated.
The extension's own invalid explicit-seed/model errors have separate fixtures; do not
accept a generic traceback in place of source-located diagnostics.

Add a third-party widget fixture checking static content preservation, absence
of copied script execution and the original-page link (STV_SWR_049).

Add a host-hidden fixture that asserts absence of hidden IDs, edges and details
from generated product data, plus a hidden-seed error case (STV_SWR_048).

Executable cases are indexed in :doc:`test-coverage`. The project test entry
points expose Python tests, Node tests, browser tests and clean-wheel checks
with nonzero exit codes propagated. Passing executions and criterion-level gaps
are recorded centrally from :doc:`maturity`; planned checks below do not claim
results by themselves.

Capacity measurements
-------------------------

Use a deterministic synthetic project with 30,000 Needs, 90,000 canonical edges,
cycles, shared tests and long details. Build the real host fixture, not merely
an in-memory graph, and use 200 visible nodes for interaction measurements.
Record build duration, graph/detail/JS byte sizes, startup, expansion/layout,
collapse, first/cached detail-open time and browser memory on a named machine.
Repeat enough to report median and maximum values with fixture seed/version.
The 200-node cap is an acceptance requirement; these fixture numbers are an
engineering benchmark, not newly accepted maximum project sizes or latency
budgets. Slow results must be reviewed before release rather than hidden by
claiming an unspecified performance pass.

Release exit criteria
-------------------------

* All MVP requirement acceptance checks have recorded results and evidence.
* File and HTTP workflows pass on recorded Firefox/Windows versions.
* Python 3.10 and pinned Sphinx integration work from an installed wheel.
* No later-mode behavior is falsely advertised as delivered.
* The agreed external-body fallback passes STV_SWR_047 and hidden-object
  exclusion passes STV_SWR_048. Static third-party widget content
  and original-page navigation pass STV_SWR_049; widget-specific JavaScript
  parity is not required for the MVP;
  do not claim complete STV_SHR_015 coverage otherwise.
* Graph validation, warnings-as-errors Sphinx build and published diagram-link
  checks pass. These checks supplement product tests rather than replace them.
* Notices, locked dependencies and wheel contents are reviewed; no unselected
  library or required runtime service has been introduced.
* Before external distribution, the owner resolves the deferred project license
  decision. Internal implementation and verification do not assign a license.

The owner agreed on 2026-10-18 to measure the first MVP before setting
response-time and memory budgets. Present measurements for agreement of the
budgets; no numeric thresholds are assigned now. The 200-visible-node limit
remains a hard acceptance criterion.

Concept review additions
--------------------------

Verify STV_SWR_050 explicitly: hover and keyboard activation open equivalent
object details, keyboard scrolling/dismissal work and original-link activation
is independent. Hidden-object tests include generated relationship references
inside copied detail fragments, inherited hidden parts and filtered counts.
Verify the external_url branch never passes a null external docname to the
builder URI resolver. Test host-default relation labels and invalid missing labels.

Run a cached-browser two-build fixture changing a Need body and making another
Need hidden: the finalized view page references the new graph identity and new
fragment hashes, no STV placeholder remains, and no current manifest references
obsolete or hidden details. Assert no generated view page is presented as
finalized if bundle generation fails. Do not claim revocation of previously
distributed copies; publish a clean output tree.

The remote-media fixtures below check the no-external-request contract;
the external-original-page link remains a separate explicit reader action.


Remote-media fallback fixtures
-------------------------------

For STV_SWR_015/017, exercise remote img/srcset, SVG references, video/poster,
iframe/object/embed, protocol-relative URLs and CSS url()/imports in copied
details. Assert that opening details makes no automatic remote requests and
shows an unavailable-offline indication with the correct explicit resource
link. Verify local bundled and permitted data images still render. Repeat under
file URLs with networking disabled and static HTTP hosting. These are planned
implementation checks, not passed runtime results.


Starting-node amendment checks
-------------------------------

Cover STV_SHR_003/025/026/047/048 and STV_SWR_001/003/007/014/025/026/043/051/052:

* Parse zero, one, multiple whitespace-separated and repeated IDs; preserve
  first occurrence order. Unknown/hidden tokens fail alone or among valid IDs.
  Exactly 200 distinct seeds succeed; 201 fail with source location. A supported
  visible Need part remains selectable. Two directives keep independent modes.
* Verify the host project name, including markup-like text, is displayed as
  text. A real Need ID equal to an internal root label cannot collide with
  tagged synthetic identity. The root has no original link, detail load or red
  unaccepted-Need border; normal Need presentation remains unchanged.
* Replace stakeholder type names and use multiple stakeholder types. Missing
  designation fails only for seedless invocations; zero visible stakeholder
  Needs is valid. Exclude hidden Needs and parts from entry lists.
* For 0/1/5/6/10/11/199/200/201 stakeholder Needs, verify deterministic pages of five,
  total counts, page bounds and every entry available exactly once. Check
  keyboard/mouse paging, focus retention, empty-state text, independent saved
  page exploration, collapse/reopen, stale layout results and layout errors.
* Verify ordinary trace expansion still rejects complete oversized groups
  atomically; project pages do not introduce partial authored-edge expansion.
  Cross-page trace targets are ordinary shared nodes, not extra visibility
  roots. Collapse preserves every explicit seed and root-reachable shared path;
  inactive pages and disconnected cycles do not retain visible nodes.
* Assert root-above-level geometry, unchanged semantic ranks, independent views
  and the hard 200-node count including the project node. Test file and static
  HTTP deployment offline with the existing Firefox/Windows release workflow.

These are implementation checks to be executed later, not passing runtime
results established by this documentation update.

Centered-layout and picker MVP checks
-------------------------------------

For :need:`STV_SWR_056`, verify exact centering of one parent over five children,
reverse-authored lower/upper relationships, synthetic root entries, competing
parents, shared children, isolated nodes and cycles. Assert finite nonoverlapping
boxes, semantic ranks, right-side test placement, retained shared identity and
final routes avoiding all box interiors after centering.

For :need:`STV_SWR_057`, verify case-insensitive ID/title substring matching,
ten-result bounds with total/refine information, exact case-sensitive ID entry,
keyboard Up/Down/Enter/Escape and pointer confirmation. Exercise originally
seeded and seedless views, invalid/hidden/unmatched/empty input, empty catalogs,
repeated replacement, independent views and return to first open overview.
Typing alone must preserve state. Failed/stale layout must preserve the prior
scene, viewport and exploration; success resets only that view's expansions,
page memory and viewport with usable focus. Test Firefox file and HTTP output
with external requests blocked. Confirm hidden IDs/titles never enter matches.

The MVP increment used focused Node and browser smoke checks. Owner inspection
and concept acceptance are complete; see :doc:`concept-reviews/round-6`.
Full release qualification remains a separate execution gate; the retained
failed release candidate remains historical evidence.

Historical draft smoke scope
----------------------------------------

For the owner-requested draft increment, execute layout geometry smoke cases
and ``test_usability_smoke`` under Firefox file URLs. Check facing ports,
clear fan-in, obstacle detours, 975px computed viewport height, delayed hover,
departure/Escape cancellation and immediate explicit Details access. Build
Sphinx with warnings as errors and validate traceability. Full regression,
capacity, clean-install packaging and release qualification remain deferred
until owner review; preserve existing suites and historical release evidence.

Before the centered-layout/picker amendment, the owner authorized v0.2.0 full
qualification, superseding the original smoke-only limit. That execution is
retained; the new MVP inspection gate is now closed. For full qualification,
run the complete Python and Node suites, file and static-HTTP Firefox workflows,
30,000-object/90,000-edge capacity measurements, isolated consumer wheel build,
documentation/traceability and diagram-publication checks. Retain a consolidated
versioned execution record including actual failures/retests and candidate hashes.

For :need:`STV_SWR_055`, ``frontend/src/render/tests/groups.test.js`` checks semantic target
ordering, stable ties, mixed/same-level/test/missing targets, graph immutability
and replacement mappings. ``test_control_order_smoke`` checks the rendered
upward/downward controls and their retained order/state after expansion.
