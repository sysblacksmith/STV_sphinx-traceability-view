v0.2.0 final release validation
==========================================================================================

Disposition and candidate
------------------------------------------------------------------------------------------

Validation passed; the candidate is ready for the owner's release decision.
This is verification evidence, not a commit, tag or publication. Before external
distribution, the owner must still resolve the recorded project-license decision.

Final execution: :doc:`../0.2.0-candidate-5/index`.
UTC interval: 2026-10-18T20:40:04.137930+00:00 to 2026-10-18T20:46:49.932074+00:00.
Baseline Git revision: ``bee5a15fed8e0b89a21b9cced09d7a1e67bb3c40``, plus the
recorded uncommitted layout/test/runner corrections. Source/test identity:
``3129fab28bbb196691acd6326a03a689f9a5c25997bf03d61950f29e9570eb29``.
Wheel: ``sphinx_traceability_view-0.2.0-py3-none-any.whl``; SHA-256:
``ac1a23625c104ca26768856b1c00675c042fe62a0685bac7967a57f52f0ef6e5``.

All required executable suites passed: **76 passed, zero failed, zero errors,
zero skipped** (58 Python/browser cases and 18 JavaScript cases). The run
includes Windows Firefox 158.0, file and nested static-HTTP
workflows with external requests blocked, Python 3.10.9, pinned Sphinx/Needs,
Node v24.21.0, isolated offline wheel installation with Node absent,
coverage, Sphinx warnings-as-errors, traceability and published diagram links.
Exact commands, environment, per-case requirement mappings, logs, tested wheel
and screenshots remain in the candidate execution.

The final wheel's 11 package files were compared byte-for-byte with the tested
source/assets; no mismatch was found. :download:`Wheel/source check <wheel-source-check.json>`.
Candidate 5 reused only candidate 4's host-built capacity fixture after proving
identical wheel, fixture inputs, Python, dependency hashes and runtime JavaScript.
Every browser capacity test was rerun; no previous browser result substituted
for a final test. The reuse proof and benchmark path are retained in candidate 5.

Criteria, corrections and history
------------------------------------------------------------------------------------------

:doc:`/implementation-review` records the criterion assessment, with
:doc:`/test-coverage` providing executable mappings for every delivered system/
software requirement. Ten system and 53 software requirements are now verified
passed. :need:`STV_SWR_019`, :need:`STV_SWR_021`, :need:`STV_SWR_022` and
:need:`STV_SWR_023` remain not_assessed and outside the delivered scope.
Stakeholder/element verification and all acceptance statuses are preserved.
Verification-only source changes after execution are identified separately;
they do not alter the tested product or tests.

* :doc:`../0.2.0-candidate-1/index`: historical failed execution retained.
* :doc:`../0.2.0-candidate-2/index`: 68 executable tests passed, but later
  criterion review exposed missing coverage for independent-parent centering.
* :doc:`../0.2.0-candidate-3/index`: interrupted after that defect was reproduced;
  partial logs and identities remain, without a complete-suite pass claim.
* :doc:`../0.2.0-candidate-4/index`: 75 passed, one failed. Its traceback shows
  the test asserted a new tab's URL while Firefox still reported about:blank.
  The test now waits for both the destination URL and actual Need element.
* :doc:`../0.2.0-candidate-5/index`: the complete corrected selection passed.
  This is the only final qualification result.

The layout correction pools only conflicting desired positions and minimizes
their displacement. An unrelated parent previously shifted 109.33px now stays
exactly over its child; shared competing parents retain their separation and
local balance. Regression coverage also checks cycles, isolated nodes,
variable heights, test lanes and deterministic geometry. No dependency,
component boundary, state transition or accepted stakeholder intent changed.

Expanded file/HTTP tests cover pointer and keyboard seed confirmation, hidden/
invalid/exact IDs, empty catalogs, repeat replacement, independent views,
overview reset and failed/stale layout preservation. A diagnostic test initially
used WebDriver clear(), which left hidden suggestion DOM unrefreshed; real
Ctrl+A/Backspace events corrected the test. Its failed report and six-case
retest remain retained. Four isolated HTTP diagnostics passed before the full
failure traceback identified the new-tab race; they were never counted as a
release pass.

* :download:`Initial seed diagnostic failure <seed-preflight-1.xml>`
* :download:`Corrected seed diagnostic: six passed <seed-preflight-2.xml>`
* :download:`HTTP diagnostic <http-diagnostic.xml>`
* :download:`HTTP repetition 1 <http-repeat-1.xml>`
* :download:`HTTP repetition 2 <http-repeat-2.xml>`
* :download:`HTTP repetition 3 <http-repeat-3.xml>`

Capacity and operating scope
------------------------------------------------------------------------------------------

The real 30,000-Need/90,000-edge host build passed in
309.590 seconds. It produced 34897944 graph
bytes, 147393890 detail bytes and 415474937 total
published bytes. Browser measurements repeated three times per transport,
expanded to exactly 200 visible nodes and verified atomic rejection beyond
the hard cap, collapse and first/cached detail loading.

.. list-table:: Final repeated browser measurements
   :header-rows: 1

   * - Transport
     - Startup median / max (ms)
     - Expansion median / max (ms)
     - Working set median / max (MiB)
   * - file
     - 552.3 / 559.2
     - 87.0 / 232.0
     - 1749.5 / 1769.2
   * - http
     - 591.9 / 612.9
     - 76.5 / 200.0
     - 1613.2 / 1642.3

Memory is the sum of Firefox process-tree working sets; shared pages may be
counted more than once. It is neither private memory nor peak allocation.
Fixture copying/cleanup is test preparation, outside the interaction timings.
No owner-agreed numeric latency/memory budget exists, so measurements are
reported without claiming a threshold pass. The 200-node cap is independently
verified. Occurrence mode, touch, other browsers/platforms and widget-specific
JavaScript parity remain deferred; remote resources retain static fallbacks.

Publication closure
------------------------------------------------------------------------------------------

After the verification-only edits, the full warnings-as-errors Sphinx rebuild,
shared traceability validation, all source/published diagram links and strict
coverage checks passed. Coverage reports 67 requirements and 76 executable
cases, with no unmapped active IDs or unknown references. A fresh Firefox
publication check passed (one case, 16 deselected); this repeats the publication
case after documentation edits and is not added to the 76-case qualification total.

Only canonical verification metadata differs from the candidate's frozen
source/test inventory. All tested product, test and runner files remain unchanged;
the tested wheel checksum still matches. No acceptance status was changed.

* :download:`Closure checks and verification identities <closure.json>`
* :download:`Final publication JUnit report <publication.xml>`
