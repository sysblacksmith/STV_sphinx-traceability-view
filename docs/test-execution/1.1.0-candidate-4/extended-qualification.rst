Extended qualification assessment
=================================

Software baseline: ``41e57ed``. Final executable test baseline:
``3b32d6be34a8a5c3bea1f118e4b24cb919901a28``. The complete candidate-4 selection passed all
229 automated cases. Its wheel and source archive match candidates 2 and 3
byte for byte. The assessment below combines the final full run, applicable
unchanged maximum-size/hover supplements and owner native/zoom observations.
Final strict documentation and hosted gates remain separate from acceptance
and publication; see :doc:`qualification`.

Criterion assessment
--------------------

The following is a semantic assessment of the accepted CR015-018 procedures,
not a claim that collecting a test establishes verification. Final full-run results cover these criteria; only scoped verification states
are updated, preserving independent acceptance statuses.

.. list-table:: Extended accepted procedures
   :header-rows: 1
   :widths: 15 45 40

   * - Cases
     - Criteria exercised
     - Evidence
   * - :need:`STV_TC_SY_066`, :need:`STV_TC_SW_051`
     - Current interactive/multiple seeds; hidden-artifact cards; independent
       views; empty/three/twelve-entry overview; page restoration; repeated
       pointer/keyboard resets; stale layout, failure/retry; cyclic/shared
       traversal, fresh state collections, input immutability and 200-node cap.
     - Extended control/reseed tests and the two Node command-sequence cases;
       baseline state, capacity and reset integration tests.
   * - :need:`STV_TC_SY_067`, :need:`STV_TC_SW_053`
     - Visible crop, scroll, negative scene origins, overflow, inline SVG
       definitions/pseudo/text escaping; immutable capture; pointer cancellation,
       outside release/blur, keyboard freshness; one-flight ownership;
       serializer/resource/font failures and retry; safe names, MIME, leases.
       Reopened text geometry is checked within one CSS pixel.
     - Extended snapshot/event/download tests; baseline four standalone SVG
       file/HTTP variants; maximum-size 200-node/ten-card supplements at both
       widths; visible-hover supplement retained beside this assessment.
   * - :need:`STV_TC_SY_068`, :need:`STV_TC_SW_052`
     - Default .7, independent .8/.6, legacy 1.0 fallback; nested px/em/rem
       hierarchy; newly inserted children and asynchronous rendered details;
       reuse/close/reopen, resize, keyboard scrolling, unchanged host/node text;
       invalid setting errors and independent graph identity invalidation.
     - Extended font/build tests, existing invalid-value component matrix and
       owner browser-zoom observation below. Valid WOFF2 readiness/embedding and
       controlled pending/failed-font refusal are separate checks.
   * - :need:`STV_TC_SY_069`, :need:`STV_TC_SW_054`
     - Actual host controls, mixed rows, repeated initialization/explicit states,
       Enter/Space, exactly one native handler, synchronized ARIA; removed table;
       copied graph/detail tables excluded; no-Needs/no-metadata pages;
       before-load normal initialization and after-load scheduling;
       unsupported markup and missing jQuery fail closed.
     - Extended host/page-scope tests and baseline page-controller, unsupported
       markup, missing-dependency and copied-metadata tests.
   * - :need:`STV_TC_SW_055`
     - Relative/encoded/Unicode local paths, real symlink escape, no outside
       content read; nested SVG/CSS cycles, active SVG rejection, missing and
       malformed resources; srcset/currentSrc, selected fonts, deterministic
       script-safe records; valid local PNG/SVG/WOFF2 self-contained snapshots.
     - Extended resource/browser tests and baseline resource/URL sanitization
       tests. External HTTP/HTTPS is blocked for browser qualification.

Owner-observed native behavior
------------------------------

The owner reported Firefox **158.0.1 (64-bit)**: "looks all good" in response
to checking 125% and 150% browser zoom, card/tooltip readability and keyboard
scrolling. Recorded at 2026-10-25T21:54:43+00:00. This is owner observation,
not agent-operated native browser UI or an automated screenshot comparison.

The earlier native Save As/folder selection and cancellation observation, and
the two verified saved SVGs, remain in
:download:`candidate-2 native evidence <../1.1.0-candidate-2/native-save-as.json>`.
Exact artifact equality makes that observation applicable to candidate 3.

Retained corrections and scope
------------------------------

All failed supplemental attempts remain under candidate 2. Reset fault
injection originally changed a Selenium script variable rather than the page
window; explicit ``window`` properties corrected the harness. Snapshot probes
initially ran before fonts were ready or placed an image outside the crop.
Font hover probes suffered pointer departure/occlusion after reopening a dock;
closing the dock, refitting and placing the native pointer stabilized them.
These were test-fixture corrections; no product code changed.

The real-hover supplement passes on file and HTTP. Each reopened SVG retains
all 25 fully visible source words inside the workspace/screen crop, after the
live hover was removed between pointer-down and click. Source and reopened
screenshots were inspected. Earlier attempts selected the project root (which
has no inspector), then incorrectly expected text lying outside the export
crop. Both failed logs are retained; the final comparison measures the actual
crop and never changes the product's crop contract.

* :download:`Hover supplement source <../1.1.0-candidate-3/check-hover-export.py>`
* :download:`Hover results and hashes <../1.1.0-candidate-3/hover-export.json>`
* :download:`Final hover log <../1.1.0-candidate-3/hover-export-final.log>`
* :download:`Source screenshot <../1.1.0-candidate-3/hover-before-file.png>`
* :download:`Reopened screenshot <../1.1.0-candidate-3/hover-reopened-file.png>`
* :download:`File-transport SVG <../1.1.0-candidate-3/hover-export-file.svg>`
* :download:`HTTP-transport SVG <../1.1.0-candidate-3/hover-export-http.svg>`

Linux/macOS, other browser/version combinations, mobile/touch optimization and
universal vector-editor rendering are not included in the Windows/Firefox
release qualification. Occurrence mode remains explicitly deferred. Prior
mobile/Edge smoke observations do not establish qualification of those targets.
The first live Trusted Publishing and Pages deployment remain publication-time
checks; workflow policy/artifact validation cannot prove a live deployment.

No cleanup was performed. The optional
:doc:`cleanup proposal <cleanup-review>` remains
pending explicit path-specific approval; all distributions and evidence remain.
