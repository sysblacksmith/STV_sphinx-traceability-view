PR015 detail acceptance corrections: development verification
===============================================================

Input commit ``740c35ce234ec26b16c76a0b77463b273f84863c`` plus the prior dirty
CR014 implementation. :need:`STV_PR_015` retains the acceptance findings;
:doc:`../../concept-reviews/round-13` records the scoped technical review.
No commit or release is performed. Owner acceptance retest remains pending.

Before/after and criterion review
-----------------------------------

The real Sphinx/Firefox baseline fails in both file and HTTP modes: dock width
360 px, metadata initially shown, no local toggle handler, and a header-ID URL
pointing at a namespaced clone in the view page. The after-fix variants pass:
720 px dock, folded initial metadata with pointer/Space/Enter toggling and ARIA
state, independent hover/persistent copies, preserved reuse state, and an actual
new tab at the source page/Need element. Ordinary copied-body anchors retain
local namespace behavior. At 1050 px, the dock is below the graph and bounded
to available width/720 px; the 1120 px breakpoint reserves useful graph space.

The shared content controller executes no host/widget script. Existing safe
URL/media policies remain. The adjacent alternate-model procedure explicitly
opens metadata before asserting its contents; this preserves the underlying
availability check under the requested folded default. Collection age, limit,
races, hover timing and original-object navigation remain regression constraints.

All 127 distinct selected checks pass: 72 Python unit/host/package checks,
36 Node components and 19 Firefox variants (eight persistent/metadata plus eleven
adjacent). Three host builds appear in both Python and focused reports. The
fresh wheel/source distribution passes clean installed-consumer and boundary/
rebuild checks. Capacity and full release qualification are not rerun; earlier
results are historical. No version or dependency change is made.

* :download:`Failing baseline <before.xml>` and :download:`diagnostics <before.log>`
* :download:`Persistent/acceptance result <focused.xml>`
* :download:`Adjacent rich-content/hover/transport/path result <adjacent.xml>`
* :download:`Python/package result <python.xml>`
* :download:`Frontend component result <node.xml>`
* :download:`Source/artifact identity <identity.json>`
* :download:`Exact commands/environment <commands.json>`
* :download:`Installed consumer identity <consumer/identity.txt>`
* :download:`Source archive inventory <sdist/members.json>`
* :download:`Rendered metadata and independent copies <visual/file.png>`
* :download:`Observed width, fold and link values <visual/file.json>`
* :download:`Draw.io export/link checks <diagrams.log>`

Canonical executions
-----------------------

.. toctree::
   :maxdepth: 1

   cases

* :download:`Exact result mapping <case-results.json>`

Each execution is a complete canonical procedure, aggregating real runner
variants. Timestamps are report completion times, not invented per-subtest
finish times. The before-fix failure is retained separately; passing executions
do not accept unrelated draft case designs. Environment: Windows 11, Python
3.13.17, Firefox 158.0.1 and geckodriver 0.37.1; browser requests outside loopback
are blocked.


Final rendered and publication review
---------------------------------------

The new metadata diagram and its normal HTML embedding were visually inspected;
labels, both arrow routes and Need links are readable. The actual project demo
was inspected with folded and expanded metadata. Its dock measures 720 px and
its header ID points at the original stakeholder document/Need, not demo.html.
A refined two-protocol repeat adds explicit arrow-icon and unique-ID assertions;
both pass. This repeats existing distinct cases without increasing the 127-case
selection. Product code is unchanged across the successful suites.

Warnings-as-errors Sphinx and complete shared evidence validation pass. Strict
mapping covers 75 system/software requirements and 158 executable cases with no
unknown IDs or unmapped active requirement. The evidence graph includes 115
canonical cases and 805 execution records; deferred/unselected cases retain their
prior states. These development gates do not qualify a release.

* :download:`Refined icon/ID report <metadata-recheck.xml>`
* :download:`Normal demo, metadata folded <normal-demo-folded.png>`
* :download:`Normal demo, metadata expanded <normal-demo-expanded.png>`
* :download:`Normal demo measurements/URLs <normal-demo.json>`
* :download:`Initial folded wide fixture <visual-final/file-folded-wide.png>`
* :download:`Independent narrow boxes <visual-final/file.png>`
* :download:`Metadata state diagram <metadata-diagram.png>`
* :download:`Normal HTML diagram embedding <metadata-embedded.png>`
* :download:`Normal documentation build <normal-build.log>`
* :download:`Strict executable mapping <coverage.log>`
* :download:`Shared evidence validation <traceability.log>`
* :download:`Requirement paths <traceability.csv>`
* :download:`Requirement-to-case paths <test-coverage.csv>`


Pane-frame acceptance follow-up
---------------------------------

The owner supplied a screenshot of the invisible side-pane boundary and shadowed
first-card edge. The open pane now has a 1 CSS-pixel solid #999 frame on all four
sides, inside its existing 720 px width. Its top and 976 px outer height align
with the graph's 975 px client area plus top border. Eight-pixel inset padding
and shadow-free cards give the first card a clean top edge. Narrow layouts keep
the existing 60vh cap and below-graph position. Hidden panes render no frame.

All ten selected Firefox file/HTTP variants pass: four persistence/navigation,
two async-race, two metadata/pane-frame and two viewport-boundary variants. The
extended presentation procedure checks all four borders, exact alignment, inset
and absence of card shadows. Product changes are CSS-only; no state transition
or diagram topology changes. Earlier broad regressions remain historical, not a
new full release result. Source and packaged CSS hashes match.

* :download:`Pane-frame regression report <pane-frame/results.xml>`
* :download:`Runner log <pane-frame/results.log>`
* :download:`Follow-up source/environment identity <pane-frame/identity.json>`


The actual normal demo was visually inspected with two open boxes. The frame
makes the clipping boundary visible from top to bottom, aligns with the graph
separator and leaves a clean inset around the first box. Normal Sphinx and
complete shared evidence validation pass (115 canonical cases, 809 executions).

* :download:`Framed normal demo <pane-frame/normal-demo.png>`
* :download:`Actual demo measurements <pane-frame/normal-demo.json>`
* :download:`Follow-up documentation build <pane-frame/build.log>`
* :download:`Follow-up evidence validation <pane-frame/traceability.log>`
