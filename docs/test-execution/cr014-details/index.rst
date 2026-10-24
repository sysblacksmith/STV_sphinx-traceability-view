CR014 persistent details: development verification
====================================================

Input commit ``740c35ce234ec26b16c76a0b77463b273f84863c`` plus the owner's CR014
and explicit answers on reuse, per-view scope, preservation and configurable
capacity. The accepted concept is :doc:`../../concept-reviews/round-12`.
This record covers a development increment, without starting a release.

Implemented and reviewed criteria
-----------------------------------

Explicit Details now opens an independent per-view dock, beside a wide graph
and below a narrow graph. Need-ID reuse preserves insertion age. The author
setting ``traceability_view_details_limit`` defaults to 10; positive exact
integers are validated before publication. FIFO eviction, manual Close, Close
all, independent views and late completion identity are implemented. Existing
safe content/cache restoration is shared with transient hover. Graph commits
refresh trigger associations without clearing boxes. Reset uses current size;
pagehide clears without focus restoration, including back-forward cache suspension.

Requirements :need:`STV_SWR_033`, :need:`STV_SWR_050`, :need:`STV_SWR_057`,
:need:`STV_SWR_063`, :need:`STV_SWR_064`, :need:`STV_SWR_065` and
:need:`STV_SHR_057` pass this criterion review and actual checks. The new cases
are :need:`STV_TC_SW_049`, :need:`STV_TC_SW_050`, :need:`STV_TC_SY_063` and
:need:`STV_TC_SY_064`. Acceptance and runtime verification remain separate.
Unrelated deferred occurrence-mode and historical distribution/CI-runtime
procedures were not newly executed; their earlier evidence remains historical.

Actual outcomes
------------------

All 156 distinct executable cases pass: 72 Python unit/host/package checks,
36 Node component checks and 48 Firefox browser variants. The browser total
includes six new persistent variants, two capacity variants and 40 existing
regressions; two usability variants passed on their targeted corrected rerun.
The focused report also repeats three already-passing configuration builds.
The one-box boundary uses the real persistent manager; real Sphinx fixtures
serialize default/1/3 and Firefox enforces default 10 and override 3 in file/HTTP.

The rebuilt 30,000-record fixture passes at 200 visible nodes in three runs per
protocol, including rejection at the limit and first/cached details. No numeric
performance budget or release qualification is inferred. The fresh wheel and
source archive pass boundary, clean installed-consumer and rebuild checks.
Windows 11, Python 3.13.17, Firefox 158.0.1, geckodriver 0.37.1; browser external
requests are blocked. There is no new dependency or version change.

* :download:`Python/package report <python.xml>`
* :download:`Node report <node.xml>`
* :download:`Persistent/configuration report <focused-final.xml>`
* :download:`Existing browser report <browser-regression.xml>`
* :download:`Usability corrected rerun <usability-recheck.xml>`
* :download:`Capacity report <capacity.xml>` and :download:`measurements <capacity-metrics.json>`
* :download:`Source/package identity <identity.json>`
* :download:`Commands and phase notes <commands.json>`
* :download:`Strict executable mapping <coverage.log>`
* :download:`Clean installed consumer <consumer/identity.txt>`
* :download:`Source archive inventory <sdist/members.json>`

Rendered and failure review
-----------------------------

Wide and narrow screenshots were visually inspected; controls and rich content
are readable, the dock scrolls independently and no modal graph overlay remains.
The revised hover/persistent Draw.io/SVG lifecycles are synchronized with the
source. The pending diagram's pagehide label was re-exported after feedback.

* :download:`Wide dock <visual/3-file-wide.png>`
* :download:`Narrow readable box <visual-final/3-file.png>`
* :download:`Geometry/order evidence <visual/3-file.json>`
* :download:`Diagram export/link checks <diagrams.log>`
* :download:`Concept build <concept-build.log>` and :download:`concept validation <concept-traceability.log>`

The initial focused collection error was an escaped-string defect in the new
harness test, before any procedure ran. Two subsequent focused attempts failed
on off-screen pointer placement and a narrow theme column correctly selecting
the below-graph dock. The fixture now explicitly exercises wide and narrow
containers. The full existing browser run found two toolbar pointer actions
outside the screen after the new below-graph interaction. Scrolling the graph
back into view resolves those test assumptions; both complete usability
procedures pass, with original hover timing/cancellation assertions retained.
No product behavior was weakened to make those assertions pass.

* :download:`Collection diagnostic <first-focused.log>`
* :download:`First focused report <focused.xml>`
* :download:`Theme/placement attempt <focused-recheck.xml>`
* :download:`Corrected layout report <focused-layout.xml>`
* :download:`Readable screenshot repeat <visual.xml>`

Canonical executions
-----------------------

.. toctree::
   :maxdepth: 1

   cases

* :download:`Exact runner-to-case mapping <case-results.json>`

Each execution is one complete canonical procedure. Failed fixture attempts are
preserved separately. Timestamps use actual enclosing report completion times;
subtest finish timestamps are not invented. Unchanged case designs retain their
review states; a passing execution does not accept a draft design.

Final documentation checks
-----------------------------

The normal warnings-as-errors documentation build and shared evidence validation
pass: 57 stakeholder, 10 system and 65 software requirements; 114 canonical cases
and 717 actual execution records. Strict mapping covers 75 system/software
requirements and 156 executable cases with no unknown or unmapped active IDs.
The refreshed persistent lifecycle was visually inspected standalone and in the
normal HTML embedding. The normal embedded demo uses the rebuilt browser assets.

* :download:`Normal documentation build <final-build.log>`
* :download:`Final evidence validation <traceability.log>`
* :download:`Requirement paths <traceability.csv>`
* :download:`Requirement-to-case paths <test-coverage.csv>`
* :download:`Final executable mapping <coverage-final.log>`
* :download:`Fresh standalone lifecycle <persistent-diagram.png>`
* :download:`Fresh normal-page embedding <persistent-embedded.png>`
