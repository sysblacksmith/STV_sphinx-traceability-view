PR013 position-stability proof of concept
================================================================================

:need:`STV_PR_013` records the owner-authorized PoC. This record preserves
analysis and limited smoke evidence; broader V-cycle documentation is deferred
until the owner confirms the interaction. Nothing is committed or released.

Reproduction and candidate behavior
--------------------------------------------------------------------------------

The original bundled UI moved P by 656 layout pixels (about 357 screen pixels)
and Q by -328 layout pixels (about -510 screen pixels) when P's group expanded.
The same failure was reproduced in Firefox over file and HTTP. The fresh full-
scene layout, bottom-up recentering and normalization did not retain old slots.

The draft layout now receives the last committed geometry and the activated
node for group/root toggles. Surviving primary horizontal slots and the activated
band are retained; new nodes use free positions. Bands above/below can move when
extra height is necessary. Existing test lanes remain separate. New branches
may extend left or above zero; Reset viewport fits their complete bounds.
Initial views, seed/overview changes and page changes use a fresh full layout.

Both transports now record **0 px** movement for every surviving node across
P expand, Q expand, P collapse and P re-expand. All **25 JavaScript tests** pass,
including three new provisional geometry cases. **Six Firefox cases** pass:
the two new transport cases plus existing offline-exploration and alternate-model
checks over both transports. The persistent demo's Reset viewport also fits all
eight nodes after expansion. The screenshot was visually inspected.

Owner review instructions
--------------------------------------------------------------------------------

Open the local ``docs/_build/pr013-poc/html/index.html`` in a browser. Expand P,
then Q, collapse P and open it again. Watch both parent boxes and already-visible
children. Use pan/zoom or Reset viewport to inspect new branches without automatic
recentering. The normal project demo is also rebuilt with this candidate bundle.

Confirm or refine this behavior before updating requirements, architecture,
interface/state documentation, canonical case specifications and review records.
In particular, :need:`STV_SWR_056` currently requires parent centering from visible
children. The PoC prioritizes existing positions when that competes with keeping
parents centered. Fresh layouts retain their centering behavior. Its historical
passed field is evidence for the previous baseline, not qualification of this
provisional interactive policy. Full formal impact/verification remains pending.
No full release/capacity/packaging run or concept acceptance is claimed.

Retained attempts and evidence
--------------------------------------------------------------------------------

The first fixture attempt had a Python selector quoting error; the next used
short IDs without configuring the fixture regex. Both setup failures remain
separate from the true before-fix reproduction. A direct standalone fixture build
also lacked the source import path; rebuilding with the existing fixture helper
passed. An initial Node command was issued from the repository root and collected
zero tests; it is not counted. The retained Node report is the actual frontend run.

* :download:`Baseline, exact scope, commands and final source hashes <verification.json>`
* :download:`Initial fixture collection failure <fixture-initial.log>`
* :download:`Initial fixture ID failure <fixture-ids.log>`
* :download:`True before-fix reproduction <before.log>`
* :download:`Before-fix JUnit <before.xml>`
* :download:`Before file measurements <before/file.json>`
* :download:`Before HTTP measurements <before/http.json>`
* :download:`First PoC browser pass <after.log>`
* :download:`First PoC JUnit <after.xml>`
* :download:`Component regression JUnit <node.xml>`
* :download:`Final browser regression log <browser-final.log>`
* :download:`Final browser regression JUnit <browser-final.xml>`
* :download:`Final file measurements <final/file.json>`
* :download:`Final HTTP measurements <final/http.json>`
* :download:`Viewport fit check <reset-viewport.json>`
* :download:`Persistent demo build <demo-build.log>`
* :download:`Initial demo import error <demo-build-initial.log>`
* :download:`PoC screenshot after Reset viewport <poc-demo.png>`

Actual project demo and structural checks
--------------------------------------------------------------------------------

The rebuilt normal project demo also passed a file-URL smoke check: expanding
``derives_from`` and ``allocated_to`` for ``STV_SWR_001``, then collapsing the
upward link, kept its world and screen coordinates unchanged and produced no
layout failure. This is additional manual smoke evidence, not a complete graph
or requirement qualification. The normal clean-publication build passed with
warnings treated as errors, and the shared existing requirement/test/evidence
graph validates. New PoC-only tests await formal allocation after owner confirmation.

* :download:`Actual project interaction observations <project-demo.json>`
* :download:`Project documentation build <documentation.log>`

Arrow regression reported during owner review
--------------------------------------------------------------------------------

The owner approved the direction of the stable-position interaction but reported
missing/truncated arrows in Firefox. This was caused by the PoC's negative graph
coordinates: routes remained logically valid while extending outside the SVG
viewport. The observed project scene had two of five routes outside it. A live
SVG-only bounds correction restored those exact missing segments without moving
nodes. The renderer now explicitly positions and sizes a viewBox containing all
node corners and route points, including negative coordinates, with marker padding.

The four arrow-coverage cases exercise downward negative X and upward negative Y
over file and HTTP. They require all points inside the viewBox and projected
endpoints aligned with actual DOM box boundaries, while preserving old node
positions. Alongside the two position cases, all six pass. The initial upward
fixture had no negative route points (even when tall boxes extended upward), so
its precondition failures are not counted as a reproduced clipping bug. The
corrected fixture reveals a further ancestor and exercises actual negative Y
routes. All raw attempts remain retained below. The 27 final component cases
include SVG bounds and existing stability/route tests. Adjacent browser regressions
are retained separately; no release qualification is claimed.

* :download:`Arrow correction source identities and commands <arrows/verification.json>`
* :download:`Original project route/viewport observations <arrows/firefox-before.json>`
* :download:`Original clipped lines <arrows/firefox-before.png>`
* :download:`SVG-only live probe restores lines <arrows/firefox-viewport-probe.png>`
* :download:`Before route-coverage JUnit <arrows/before.xml>`
* :download:`Before route-coverage log <arrows/before.log>`
* :download:`First corrected-renderer attempt with incomplete upward fixture <arrows/first-after.xml>`
* :download:`First corrected-renderer log <arrows/first-after.log>`
* :download:`Final route/stability browser JUnit <arrows/after.xml>`
* :download:`Final route/stability browser log <arrows/after.log>`
* :download:`Final component JUnit <arrows/node-final.xml>`
* :download:`Downward file route observations <arrows/final/file-down-arrows.json>`
* :download:`Upward file route observations <arrows/final/file-up-arrows.json>`
* :download:`Downward HTTP route observations <arrows/final/http-down-arrows.json>`
* :download:`Upward HTTP route observations <arrows/final/http-up-arrows.json>`

The final corrected embedded demo reproduces the same formerly clipped project
scene with two negative-coordinate routes and zero points outside its explicit
viewBox. Its screenshot is byte-identical to the earlier SVG-only diagnostic
render, confirming that the permanent renderer restores the same complete lines.
All four adjacent file/HTTP offline/alternate-model cases pass with the final
bounds implementation. The final scoped total is 27 component and ten browser
cases across the route/stability and adjacent reports; full qualification and
owner confirmation remain separate.

* :download:`Corrected embedded-demo route observations <arrows/firefox-after.json>`
* :download:`Corrected embedded-demo screenshot <arrows/firefox-after.png>`
* :download:`Adjacent browser JUnit <arrows/adjacent.xml>`
* :download:`Adjacent browser log <arrows/adjacent.log>`

Natural numeric order for initial seed rows
--------------------------------------------------------------------------------

The owner requested ID order after the corrected PoC interaction looked good.
ELK's incidental ordering of disconnected initial nodes is now replaced by
natural numeric comparison when no relationship edges are expanded. This covers
initial explicit-seed and project-entry rows; each row keeps semantic rank.
Expanded navigation retains its stable positions rather than re-sorting nodes.

The component case checks shuffled IDs in both modes and preserves their order
and coordinates after expansion. The file/HTTP browser cases use authored
``REQ_20 REQ_10 REQ_3 REQ_2 REQ_1`` and require visible left-to-right order
``REQ_1 REQ_2 REQ_3 REQ_10 REQ_20``, followed by unchanged old coordinates.

* :download:`Ordering source identity and commands <ordering/verification.json>`
* :download:`Component results <ordering/node.xml>`
* :download:`Ordering browser JUnit <ordering/browser.xml>`
* :download:`Ordering browser log <ordering/browser.log>`
* :download:`File ordering observation <ordering/file-numeric-order.json>`
* :download:`HTTP ordering observation <ordering/http-numeric-order.json>`
