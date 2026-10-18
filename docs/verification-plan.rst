Implementation verification plan
====================================

This plan is ready for implementation; it records intended checks, not passed
runtime results. Requirement verification states remain ``not_assessed``.

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
     - Required seed, forward references, alternate host names, extra ranks, accepted-state override, missing colors, invalid required mappings.
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
The extension's own missing seed/model errors have separate fixtures; do not
accept a generic traceback in place of source-located diagnostics.

Add a third-party widget fixture checking static content preservation, absence
of copied script execution and the original-page link (STV_SWR_049).

Add a host-hidden fixture that asserts absence of hidden IDs, edges and details
from generated product data, plus a hidden-seed error case (STV_SWR_048).

No product code exists yet, so the test module names in the handover are tasks,
not executable commands claimed to pass today. Once implemented, the project
test entry points must expose Python tests, Node tests, browser tests and wheel
smoke tests with nonzero exit codes propagated.

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
