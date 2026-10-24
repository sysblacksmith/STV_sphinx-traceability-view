Round 10: CR_013 classified evidence rows
===========================================

Scope and authority
---------------------

2026-10-24. Reviewer: Codex. Owner: project owner. Input commit
``0cecafb4836ab252d9e30e4553ab901cbd8660b7`` plus owner-authored untracked
CR_013 RST/SVG; the earlier PPTX remains backup evidence. Canonical remote:
https://github.com/sysforger/STV_sphinx-traceability-view.
The owner explicitly requested concept creation, review and implementation of
CR_013 and then chose "Keep unclassified records in a fallback row". This
is authority to implement the specified row amendment and delegated acceptance
of clean internal design/tests. It is not publication, commit or release authority.
The stakeholder revision records that instruction and preserves prior rounds.

Inventory and review boundary
------------------------------

Current requirements, test designs/executions, system/software elements,
architecture/Draw.io exports, interfaces, dependency manifests, state machines,
implementation/verification plans and source/review registers form the context.
The scoped inventory identifies changed/accepted content separately from prior
accepted or still-draft context; a hash alone is not evidence of review.
Unrelated PRSA gates, later occurrence mode, arbitrary manual positioning and
new release qualification are excluded without declaring them resolved.

Changed requirement paths: :need:`STV_SHR_012`, :need:`STV_SHR_054`,
:need:`STV_SYS_005`, :need:`STV_SWR_012`, :need:`STV_SWR_037`,
:need:`STV_SWR_055`, :need:`STV_SWR_058`, :need:`STV_SWR_061`.
Retained context includes :need:`STV_SHR_009`, :need:`STV_SHR_010`,
:need:`STV_SHR_011`, :need:`STV_SHR_014`, :need:`STV_SYS_002`,
:need:`STV_SWR_014`, :need:`STV_SWR_056`, :need:`STV_SWR_059`,
:need:`STV_SWR_060`. Component owners remain :need:`STV_SWE_MODEL`,
:need:`STV_SWE_GRAPH`, :need:`STV_SWE_LAYOUT`, :need:`STV_SWE_RENDER`.
Test designs: :need:`STV_TC_SW_046`, :need:`STV_TC_SW_047`,
:need:`STV_TC_SW_048`, :need:`STV_TC_SY_061`; prior legacy and PR013 cases
remain regression context, with their historical executions preserved.

Findings and design resolutions
--------------------------------

* **STV_R10_001 (requirements conflict):** Mandatory right-side tests contradict
  nine target rows. Revised requirements distinguish classified ordinary rows
  from an explicitly configured compatibility role; ADR 009 partially supersedes
  ADR 008's test-lane assumptions while retaining stable navigation.
* **STV_R10_002 (classification ownership):** Neighbor/ID inference would move
  shared tests or depend on naming. Configurable tag mapping and complete-graph
  one-hop owner mapping resolve placement at build time, with additive object
  fields consumed by both layout and control ordering. No duplicate host types.
* **STV_R10_003 (exception policy):** Strict failure was proposed; the owner
  selected fallback retention. A common labelled fallback below software
  architecture and above problems handles ambiguous/missing records. Invalid
  configuration remains an error. Hidden owners cannot leak or reclassify nodes.
* **STV_R10_004 (test completeness):** Four concrete designs cover model paths,
  actual classification/hidden/mixed-owner cases, layout/control/stability and
  Firefox file/HTTP entry from software/cases/executions. Legacy regression and
  clean installed distribution are separate gates, not inferred passes.

Semantic and feasibility assessment
------------------------------------

SYS 005 retains the observable row boundary; SWR 012/037 own browser projection.
SWR 061 derives from SYS 002 and SHR 012, allocated to build-side MODEL/GRAPH,
which already own normalization/snapshot publication. Existing containment is
consistent for actual system parents. No artificial component or system
requirement is introduced. The unchanged stack supports Python dictionary/set
classification and JS resolved-level lookup. Indexed two-pass resolution avoids
per-execution whole-graph scans; cyclic/chained data links use fallback under the one-hop contract, rather than
recursively guessing classifications.

Designs distinguish missing classification data (retained fallback) from invalid
configuration (actionable build error), specify row alignment versus child-span
centering, and retain transactional scene/geometry ownership. No new browser
state or timer is needed. The build snapshot action and software flow labels
are refined in editable diagrams, preserving routes and component boundaries.

Review decision and handover
-----------------------------

The clean scoped concept is accepted under the owner's recorded delegation.
Accepted internal requirements: :need:`STV_SYS_005`, :need:`STV_SWR_012`,
:need:`STV_SWR_037`, :need:`STV_SWR_055`, :need:`STV_SWR_058`,
:need:`STV_SWR_061`. Stakeholder revision :need:`STV_SHR_012` and the
classified/legacy clarification of :need:`STV_SHR_054` cite the explicit owner
CR_013 implementation instruction and fallback decision, not inferred approval
from a build. ADR 009 is accepted; ADR 008's reciprocal partial supersession
preserves all stable-navigation policy.

The four new cases above are accepted as designs, still not_run with no
fabricated executions. Changed ordinary documents (interfaces, architecture,
state actions, implementation/verification plans, technology and demo guidance)
and the software/state Draw.io/SVG pairs are accepted against the
:download:`concept-gate inventory <round-10-inventory.json>`. Unchanged context
retains its own prior accepted/draft states; no blanket reacceptance is claimed.

All four findings are closed for concept scope. Initial Sphinx validation
exposed an ADR entry appended outside the toctree; it was moved into the index
and the warnings-as-errors rebuild passed. Complete --require-test-coverage
validation passed: 55 SHR, 10 SYS, 61 SWR, 109 cases, 600 executions. CSV paths
were exported and reviewed for the revised paths. System/software/state SVGs
and their embedded pages were visually inspected at reading scale; routes,
arrowheads and labels are readable. No new boundary or missing core policy
remains. Runtime evidence is explicitly not assessed at this gate.

Implementation handover: apply the model selectors and two-pass graph contract,
share resolved-level lookup between layout and controls, label fallback nodes,
configure the project's nine rows, and execute the four new procedures plus
legacy, PR013, packaging and capacity regression gates. No release is authorized.

Implementation feedback re-review
----------------------------------

**STV_R10_005 (closed):** A malformed data link to another owner-derived record
must not bypass the owner's fallback policy. Such chains/cycles now use fallback
(or the documented strict mode when fallback is absent), with no recursive
inference. Invalid classifier configuration still fails early. Updated graph
cases cover cycles, hidden/mixed owners and input order. The same scoped design
is reaffirmed; no stakeholder outcome or default model changes.

A large graph case additionally resolves 30,000 classified case/execution records
and 15,000 owner links. It asserts actual boundary assignments without inventing
a performance budget. The revised SW_047 design is reaffirmed under the same
review delegation; runtime outcome remains dependent on the actual runner report.

Final implementation disposition
---------------------------------

The scoped implementation and feedback re-review are complete. Four accepted
canonical procedures now have actual passing aggregate executions. The full
134-test development selection passed, including 30,000-record classification,
real Firefox file/HTTP nine-row navigation, legacy/PR013 regression, clean
installed packaging and rebuilt browser capacity. The five review findings are
closed; no unresolved design/implementation blocker remains in CR_013.
Verification-state updates are limited to the revised eight requirement paths.
The normal embedded project demo uses the classified model and owner-selected
fallback. Final publication/evidence validation is retained in
:doc:`../test-execution/cr013-rows/index`; no release qualification is inferred.

The :download:`final inventory <round-10-final-inventory.json>` records current
content after source ownership, fallback clarification and execution links.
The original inventory preserves the concept-gate baseline. Unchanged context
and unrelated draft security artifacts retain their earlier acceptance states.

Final checks passed: warnings-as-errors Sphinx; full --require-test-coverage
validation with 55 SHR, 10 SYS, 61 SWR, 109 cases and 604 executions; 134
executable tests mapped without unknown IDs; 2/9/11 published diagram links.
No acceptance-blocking finding remains in the scoped final inventory.
