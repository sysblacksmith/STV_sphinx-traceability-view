PR013 final development verification
=====================================

Scope and identity
-------------------

Date: 2026-10-24, Windows 11, Python 3.13.17, Node 24.21.0, Firefox 158.0.1,
geckodriver 0.37.1. Input commit ``4ad8fcefdf95ee6987478a9d632d5f33624aa673``
plus the recorded dirty worktree. The owner approved the PoC and requested
concept creation, review and implementation; :doc:`../../concept-reviews/round-9`
records acceptance. This is development verification, not a release candidate.
Historical PoC attempts remain in :doc:`../pr013-poc/index`.

* :download:`Build/package identity <build-identity.json>`
* :download:`Initial source hashes <source-hashes.json>`
* :download:`Final source hashes and test-only difference <source-hashes-final.json>`
* :download:`Exact commands and report timestamps <commands.json>`
* :download:`Machine-readable summary <summary.json>`

Results and interpretation
--------------------------

111 distinct tests have latest passing outcomes: 31 Node component cases and
80 pytest cases (42 non-browser and 38 Firefox, including two capacity variants).
There are no latest failures/errors/skips. This combines complementary selections
against the same product bytes, not historical release candidates.

The initial adjacent browser run had two failed missing-target text assertions.
Stable navigation placed the newly discovered box partly outside the retained
viewport. The ID was present in the DOM. The revised accepted procedure asserts
identity, explicitly Reset viewport, verifies unchanged world geometry and then
requires visible identity plus detail failure/retry recovery. Both retests pass.
Only that test function changed after the initial suites; product bytes and the
other test functions did not change. Failed attempts are retained below.

All new case designs have actual executions: :need:`STV_TC_SW_043`,
:need:`STV_TC_SW_044`, :need:`STV_TC_SW_045`, :need:`STV_TC_SY_058`,
:need:`STV_TC_SY_059`, :need:`STV_TC_SY_060`. Geometry assertions cover
shared-test reranking, either anchor role, root collapse/reopen, growing earlier
bands and 200 nodes. Firefox checks measure world/screen stability, focus,
negative x/y route coverage, endpoint alignment, Reset and initial numeric order.
The async harness verifies committed snapshot identity survives rejected work.
Existing fresh-centering, alternate-model, paging/picker, inspection and
independent-view checks passed as complementary regression gates.

* :download:`Frontend component report <node.xml>`
* :download:`Full non-browser report <python.xml>`
* :download:`Focused Firefox report <focused-browser.xml>`
* :download:`Adjacent Firefox first attempt, including failures <adjacent-browser.xml>`
* :download:`Placeholder procedure retest <missing-recheck.xml>`
* :download:`Capacity report <capacity.xml>`
* :download:`Adjacent failure diagnostics <adjacent-browser.log>`
* :download:`Placeholder retest log <missing-recheck.log>`

Capacity, packaging and concept checks
--------------------------------------

The newly rebuilt fixture contains 30,000 Needs / 90,000 authored edges. Three
runs per transport reach exactly 200 visible nodes, reject overflow without
committing, exercise uncached/cached details and collapse. Measured maxima were
223 ms/file and 230 ms/HTTP for expansions; these observations are not new
performance guarantees. The isolated wheel host imports the installed development
package with Node absent from PATH. The source archive excludes local evidence
and rebuilds the wheel with identical shipped static assets.

* :download:`Fixture metrics <benchmark-metrics.json>`
* :download:`Browser measurements <capacity-browser.json>`
* :download:`Clean installed consumer identity <consumer/identity.txt>`
* :download:`Consumer build log <consumer/build.log>`
* :download:`Source archive member inventory <sdist/members.json>`
* :download:`Rebuilt archive checksums <sdist/artifacts.json>`
* :download:`Package build log <package-build.log>`

Warnings-as-errors documentation, full test-coverage traceability and strict
bidirectional executable mapping passed. The final graph contains 105 canonical
cases and 600 historical/current execution records; all 70 system/software
requirements have executable mappings. Standalone
and embedded system/software/state diagrams were visually inspected. Separate
feedback and geometry arrows are readable; link checks verify 2/9/11 portable
Need targets. The initial short-heading warnings and symbolic-link export
preflight failure are retained with successful rechecks. An initial root-level
Node build invocation also failed before the correct frontend invocation; no
product test result is attributed to that preflight.

* :download:`Initial concept build warnings <concept-build.log>`
* :download:`Successful concept build <accepted-concept-build.log>`
* :download:`Initial export preflight <diagram-export.log>`
* :download:`Successful shared export <diagram-export-recheck.log>`
* :download:`Published diagram link check <diagram-links.log>`
* :download:`Executable mapping check <executable-coverage.log>`

Canonical case execution records
---------------------------------

.. toctree::
   :maxdepth: 1

   cases

* :download:`Case-result mapping <case-results.json>`

No tag, GitHub release, deployment or commit is created. Unrelated security
review/hosted gates and later occurrence-mode requirements retain their prior
states. The complete next release must be explicitly started and qualified.

Final checks
-------------

* :download:`Successful final documentation build <completion-build.log>`
* :download:`Initial aggregation diagnostic <traceability-final.log>`
* :download:`Successful corrected graph check <traceability-final-recheck.log>`
* :download:`Final traceability paths <traceability-final.csv>`
* :download:`Final requirement-to-case paths <test-coverage-final.csv>`

The first final graph check found ambiguous latest timestamps when several
runner subtests were modeled as separate executions of one canonical procedure.
The corrected unissued record has one aggregate execution per complete new case;
every actual subtest selector/result remains in the mapping and runner reports.
No per-subtest time or result is invented. Failed/retested placeholder attempts
remain separate history. No previously issued execution record was changed.
