Round 9: Stable navigation concept and implementation handover
======================================================================

Scope, authority and baseline
-------------------------------------

Date: 2026-10-24. Reviewer: Codex; decision owner: project owner.
Input commit: ``4ad8fcefdf95ee6987478a9d632d5f33624aa673``; clean worktree.
The owner approved the PR013 PoC ("i love it") after Firefox arrows and numeric
ordering were corrected, then explicitly invoked concept-creation,
concept-review and concept-implementation to finalize that fix. This delegates
review and acceptance of clean internal concept/test artifacts in this scope,
and authorizes implementation; it does not authorize a commit or release.
The approved behavior is the revision evidence for :need:`STV_SHR_052`,
:need:`STV_SHR_054` and :need:`STV_SHR_055`, rather than inferred approval from
a passing build. The historical centering baseline remains in round 6.

Inventory and boundary
------------------------------

Review context comprises all current requirement, element, architecture,
interface, dependency, ADR, test, implementation/verification and source/review
artifacts. The machine-readable inventory records hashes and distinguishes
changed scope from retained context. Current documents were read together with
their affected dependency neighborhood. Historical executions are evidence of
their own revisions, never new candidate passes.

Changed scope: :need:`STV_SHR_052`, :need:`STV_SHR_054`, :need:`STV_SHR_055`,
:need:`STV_SWR_056`, :need:`STV_SWR_058`, :need:`STV_SWR_059`,
:need:`STV_SWR_060`; owners :need:`STV_SWE_LAYOUT` / :need:`STV_SWE_RENDER`;
:ref:`STV_ADR_008` and partial supersession of :ref:`STV_ADR_006`;
:need:`STV_TC_SW_043`, :need:`STV_TC_SW_044`, :need:`STV_TC_SW_045`,
:need:`STV_TC_SY_058`, :need:`STV_TC_SY_059`, :need:`STV_TC_SY_060`.
Fresh-centering cases :need:`STV_TC_SW_010` / :need:`STV_TC_SW_011` retain
valid designs. Existing route, test-lane, shared-identity, capacity, transactional
failure, focus, viewport and independent-view contracts remain constraints.

The separate artifact vertical-target CR, occurrence-mode later scope, hosted
PRSA-006 work and unrelated draft security case designs are excluded from new
acceptance, not declared resolved. No system requirement, component, dependency,
serialization format, state transition or timer is added.

Review findings and closure criteria
--------------------------------------------

* **STV_R9_001, conflicting centering policy:** The accepted centering text
  applied to every computation and contradicted the owner-approved stable
  behavior. Fresh versus incremental policies now have explicit precedence,
  amendment evidence and reciprocal partial ADR supersession. Recheck all
  references in architecture, interfaces, implementation/state and demo prose.
* **STV_R9_002, incomplete geometry contract:** The prototype snapshot and
  negative-origin SVG behavior were absent from the design. Contracts now name
  last-successful per-view ownership, token/failure retention, stable slots,
  reranked tests, band-height exceptions and equal CSS/viewBox origins.
* **STV_R9_003, provisional tests:** PoC selectors lacked requirement metadata
  and modeled case coverage. Six substantive designs now cover the changed
  criteria, including root/rank/capacity/negative-boundary cases. Required gates
  are source metadata, full-case implementation, real outcomes and traceability.

Semantic assessment
---------------------------

The directly derived software obligations refine local browser outcomes without
an artificial system layer. Layout owns ordering/placement and final routing;
render owns committed snapshots, focus, transform and SVG presentation. Existing
containment in the browser system element stays valid. Stability takes precedence
over renewed centering, not over collision safety or semantic rank. A shared
test can change median rank, so its relocation is explicit and testable.

Case designs distinguish ordinary slots from shared-test rank exceptions and
simple stationary bands from vertical growth. Unit coverage is complemented by
actual Firefox world/screen/CTM assertions on both transports. Fresh centering,
stale failures and other-view state have their existing complementary tests.
Empty SVG bounds and 200-node geometry cover relevant boundaries. No successful
build or low-level pass is treated as full parent verification.

* **STV_R9_004, visual contract:** The existing software view omitted geometry
  feedback from rendering to layout. Its new separate upward arrow now names
  previous geometry and activated key, while the state diagram's layout action
  distinguishes fresh placement/stable slots. Editable sources and exported
  SVGs are kept adjacent; inspect both standalone and embedded after export.

Review decision and checks
----------------------------------

The scoped concept is accepted under the recorded delegation after semantic,
structural and visual review. Accepted internal requirements are
:need:`STV_SWR_056`, :need:`STV_SWR_058`, :need:`STV_SWR_059`,
:need:`STV_SWR_060`; the six new cases above are accepted as designs, with
``last_result: not_run`` at this gate. :ref:`STV_ADR_008` is accepted and the
partial supersession link on :ref:`STV_ADR_006` preserves its other decisions.
Stakeholder revision evidence is the owner's explicit PoC approval, as recorded
above. All four review findings are closed for the concept; executable
implementation and real outcomes remain the next gate, not inferred passes.

Accepted ordinary-document changes are the software/state diagram pairs,
:doc:`../architecture-software`, :doc:`../elements-software`,
:doc:`../internal-interfaces`, :doc:`../implementation-plan`,
:doc:`../state-machine`, :doc:`../technology-stack`,
:doc:`../verification-plan` and :doc:`../demo`. The unchanged system diagram
and accepted baseline remain context, not newly accepted unseen content.

Checks: the first build exposed two short heading underlines; both were
corrected and warnings-as-errors builds passed. Full shared test-coverage
validation passed (55 SHR, 10 SYS, 60 SWR, 105 cases). Standalone and embedded
system/software/state pictures were inspected; feedback and geometry arrows
use separate ports and readable labels. The linked-graph and failure/state
contracts agree. The first export failed through a PowerShell symbolic-link
PSScriptRoot resolution; invoking the actual shared script with explicit
ProjectRoot succeeded, without changing shared tooling.

The :download:`artifact inventory <round-9-inventory.json>` records the
reviewed content identities and retained-context boundary. The scoped handover
has no unresolved concept blocker. Implementation starts from these contracts,
adds requirement metadata and boundary assertions, rebuilds the bundle, executes
component/Firefox/packaging checks and records development outcomes separately.
No release qualification or publication is implied.

Implementation feedback and re-review
-------------------------------------

**STV_R9_005, placeholder visibility assumption (closed):** Two adjacent browser
cases failed because a newly discovered missing-target box was partly outside
the retained viewport; its ID remained in the DOM. Re-reviewed
:need:`STV_TC_SY_003` / :need:`STV_TC_SY_012` now explicitly Reset viewport,
assert unchanged world geometry and then require visible ID, missing status,
noninteractive placeholder and detail failure/retry. Both real retests passed.
This resolves the test/design assumption without altering the product or
weakening missing-target requirements. Failed reports and new attempts are
retained. The updated case designs are reaffirmed accepted under the same
scope delegation; this widens only the affected dependency neighborhood.

The six new designs are implemented, requirement-tagged and have 21 actual
passing focused outcomes. The state-machine token/failure case also asserts
that rejected work retains the same committed geometry snapshot. Semantic
recheck found no new policy decision; ordinary and test-rank exceptions remain
consistent with the accepted concept. Final capacity/document checks and the
current inventory are linked through the development record.

**STV_R9_006, grouped execution timestamps (closed):** The first final graph
check rejected multiple subtest records with the same latest completion time
for one modeled procedure. The current unissued development record now has
one aggregate execution per complete new canonical case, with all actual
subtest selectors/outcomes retained in its mapping and JUnit evidence. No test
time was invented and no historical issued execution was changed. Existing
failed/retest attempts remain separate. Recheck the full graph after rebuilding.

Final disposition
------------------

The implementation feedback re-review is complete: all six findings are closed,
the scoped accepted concept has no unresolved blocker, and 111 distinct tests
have latest passing outcomes. Final warnings-as-errors documentation and complete
test-coverage validation passed after correcting execution aggregation (55 SHR,
10 SYS, 60 SWR, 105 cases, 600 executions). Strict executable mapping covers all
70 system/software requirements without unknown IDs. Per-requirement verification
updates are confined to the revised centering and new navigation/order paths;
unrelated verification/acceptance states are preserved.

The :download:`final worktree inventory <round-9-final-inventory.json>` captures
current content after implementation feedback and execution links. The original
inventory preserves concept-gate hashes. Finalizing :need:`STV_PR_013` does not
resolve unrelated draft security reviews, hosted gates or qualify a release.
