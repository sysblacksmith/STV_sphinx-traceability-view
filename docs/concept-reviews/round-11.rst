Round 11: PR014 visible viewport boundary
==========================================

Scope and authority
---------------------

2026-10-24. Reviewer: Codex. Owner: project owner. Baseline
``baf629a7d0c927f20658801f114235abc8f3edb5`` plus the new PR014 RST/PNG.
The owner explicitly requested analysis, fix planning and implementation through
the whole V-cycle using the respective skills. The report explicitly requests a
thin grey marker without removing clipping; that is the stakeholder intent for
:need:`STV_SHR_056`. This authorizes scoped concept review/acceptance and
implementation, not a commit, release or new behavior beyond that marker.

Analysis and plan
-------------------

:need:`STV_PR_014` identifies the actual ``.stv-viewport`` overflow edge; the
outer widget border does not mark that internal boundary. Add a native top
border outside the transformed scene, retaining 975 px content height and all
input semantics. The plan is in the same problem report. Correct the supplied
attachment/evidence paths and provenance without inventing a missing PPTX.

:need:`STV_SWR_062` refines :need:`STV_SHR_056`, allocated to
:need:`STV_SWE_RENDER`; no artificial system requirement is needed. The concrete
case :need:`STV_TC_SY_062` checks rendered clipping, resizing, host sizing and
controls rather than merely matching CSS source. Existing viewport/zoom/focus,
independent-view and packaging obligations remain unchanged regression context.

Findings and review gates
--------------------------

* **STV_R11_001:** Intake figure/evidence paths name files not supplied under
  those names. Use the actual adjacent PNG and repository-relative report path;
  distinguish reported PPTX provenance from files supplied here.
* **STV_R11_002:** An unqualified top border under a host border-box rule could
  reduce the existing usable height. Explicit content-box sizing plus actual
  975 px client-area checks preserves the accepted viewport contract.
* **STV_R11_003:** A scene-level line would move with pan/zoom, while an overlay
  could obscure content or intercept input. Use the native viewport border;
  verify its clip/pointer boundary and fixed position in the actual browser.

Current concept context includes the existing requirements/elements, diagrams,
interfaces, stack and plans, canonical cases/executions and review/source records.
Changes are limited to the two requirement paths, one case, viewport contract
and relevant plan/demo/state-neutral prose. No library, component boundary,
serialization, layout algorithm, state transition or timer changes. Accepted ADRs
and unchanged diagrams retain their prior reviews; no diagram-only edits or new
ADR are justified for a native CSS border. Unrelated PRSA and release gates are
excluded from this scope without declaring them resolved.

Review decision
-----------------

Accepted under the scoped whole-V-cycle delegation: :need:`STV_SWR_062` and
:need:`STV_TC_SY_062`; stakeholder :need:`STV_SHR_056` records the exact grey-line
outcome explicitly requested in PR014 and authorized for implementation. No
broader stakeholder revision is inferred. The case retains its actual failed
baseline attempt; acceptance of its design does not imply an implementation pass.

All three findings are closed for the concept: attachment paths are corrected,
content-box sizing preserves the accepted client height, and a native container
border avoids transform/overlay ownership errors. Browser reproduction confirms
actual clipping with a 0 px/style-none edge over file/HTTP. The warnings-as-errors
concept build and full --require-test-coverage validator passed: 56 SHR, 10 SYS,
62 SWR, 110 cases, 605 executions. The direct SHR-to-SWR channel and the case's
verifies/executed-by paths are semantically appropriate; no unrelated tooltip or
system requirement was linked merely to fill the graph.

Accepted ordinary-document changes are the interface/implementation/verification
marker contract and state-neutral/demo guidance. The inventory records all
current concept context and scoped identities. Existing architecture/state SVG
hashes match round 10's reviewed files; their standalone/embedded visual evidence
is retained there. This CSS-only change does not export or change a diagram,
state action or transition, so no new diagram acceptance is claimed.

Implementation handover: add the viewport top border and explicit sizing,
regenerate packaged CSS, execute the exact clipping/resizing/control procedure
and adjacent usability/offline/arrow checks, verify installed asset delivery,
and rebuild/validate the real project demo. Full capacity/release suites are not
required for unchanged layout/data algorithms and are not claimed as rerun.

Implementation and re-review
-----------------------------

The implementation matches the accepted native-border contract. Actual file/HTTP
checks now pass clipping hit tests, neutral 1 px marker, responsive flow/width,
975 px client height under a border-box theme, keyboard controls and independent
views. Negative-arrow and usability regressions passed. All 60 non-browser
checks passed, including clean package consumption and source archive rebuilding;
the changed packaged CSS matches the tested source asset. The complete selected
development outcome is 70 passes, zero latest failures/errors/skips. The expected
before-fix failures remain linked to the same canonical case.

All three scoped findings are closed. New requirement verification is justified
by its complete browser criterion, not concept acceptance. No state/diagram,
algorithm or dependency change occurred. Final documentation/evidence validation
and inventory reconcile the scoped changes; unrelated accepted/draft artifacts
retain their existing states. Full release/capacity qualification is not claimed.

Final disposition
-------------------

:need:`STV_PR_014` is fixed. Final warnings-as-errors Sphinx, full evidence/
--require-test-coverage validation and strict executable mapping passed with no
scoped blocker. The owner-requested outcome is delivered through the accepted
requirement/design/case path and real before/after execution. The
:download:`concept-gate inventory <round-11-inventory.json>` and
:download:`final inventory <round-11-final-inventory.json>` distinguish reviewed
scope from preserved context. No unrelated artifact is newly accepted, no prior
execution is rewritten and no commit/tag/release is created.
