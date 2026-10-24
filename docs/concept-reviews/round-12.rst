Round 12: Persistent per-view details
======================================

Scope, authority and baseline
------------------------------

2026-10-24. Reviewer: Codex. Owner: project owner. Input revision
``740c35ce234ec26b16c76a0b77463b273f84863c`` plus the owner-authored CR014.
The owner requested the complete V-cycle, then explicitly chose reuse without
age refresh, independent per-view stacks and persistence across graph replacement.
The additional instruction makes the capacity author-configurable, default 10.
These decisions authorize the precise amendment and scoped internal review/
acceptance followed by implementation; no commit or release is authorized.

Inventory and requirements
---------------------------

Current requirements/elements, interfaces, plans, technology/manifests, ADRs,
Draw.io/SVG views, case/execution records and source/review registers form the
context. Changed paths are :need:`STV_SHR_057`, :need:`STV_SWR_033`,
:need:`STV_SWR_050`, :need:`STV_SWR_057`, :need:`STV_SWR_063`,
:need:`STV_SWR_064`, :need:`STV_SWR_065`. Retained parents include
:need:`STV_SHR_015`, :need:`STV_SHR_033`, :need:`STV_SHR_034`,
:need:`STV_SYS_002`, :need:`STV_SYS_006`. Ownership stays with existing
:need:`STV_SWE_INSPECT`, :need:`STV_SWE_RENDER`, :need:`STV_SWE_MODEL` and
:need:`STV_SWE_DIRECTIVE`; no artificial component/system requirement.

New designs: :need:`STV_TC_SW_049`, :need:`STV_TC_SW_050`,
:need:`STV_TC_SY_063`, :need:`STV_TC_SY_064`. Existing hover, safe content,
keyboard, seed and retry designs require semantic re-review where explicit
Escape formerly dismissed a panel. Hover-Escape remains unchanged. Historical
executions remain evidence of their own revision, not new runtime passes.

Findings and design decisions
------------------------------

* **STV_R12_001:** A singleton overlay cannot meet persistent capacity while
  retaining hover cancellation. Separate lifecycles; share only safe transport
  and restored content. ADR 010 partially supersedes prior inspection policy.
* **STV_R12_002:** Age/scope/replacement were unspecified. Owner answers define
  per-view Need-ID reuse, FIFO and preservation; no graph-state mutation/storage.
* **STV_R12_003:** Capacity is configurable, not hard-coded at ten. Validate a
  positive exact JS integer in the build; publish an additive optional field.
* **STV_R12_004:** Layout, focus and async ownership can regress on commit/evict.
  Native responsive dock, live trigger lookup, no focus on completion and
  entry-identity guards fix these contracts; Reset uses current viewport size.

Semantic review: SYS 002 legitimately refines author validation in build-side
MODEL/DIRECTIVE. Browser-local collection and presentation use justified direct
SHR paths and existing inspector/renderer containment. Unchanged full-content,
offline/remote-media, hidden-object, clipping and graph/capacity contracts remain
constraints. The four substantive cases cover normal/negative/boundary/recovery
behavior, including actual default/override limits and late results. No new
library, service, later occurrence-mode delivery, reader capacity UI or session
persistence is introduced. Unrelated PRSA and release gates remain excluded.

Review gate
-------------

The scoped clean concept is accepted under the recorded delegation. Accepted:
:need:`STV_SWR_033`, :need:`STV_SWR_050`, :need:`STV_SWR_057`,
:need:`STV_SWR_063`, :need:`STV_SWR_064`, :need:`STV_SWR_065`, the four new
case designs above and :ref:`STV_ADR_010`. :need:`STV_SHR_057` records explicit
owner decisions, including the additional configurable-capacity instruction.
At this concept gate cases were not_run and implementation verification was
not assessed; subsequent runtime results are recorded separately below.

All four concept findings are closed by the concrete contracts and case designs.
The first build exposed a duplicated review toctree entry; it was removed and
the warnings-as-errors rebuild passed. Complete --require-test-coverage validation
passed (57 SHR, 10 SYS, 65 SWR, 114 cases, 606 executions). New persistent, revised
hover, software and retained system SVGs were inspected standalone and in their
HTML embeddings. Routes/arrowheads and labels are readable; a long entry arrow
label was split before export. No missing core policy or in-scope blocker remains.

Accepted ordinary documents cover the changed interfaces, implementation and
verification plans, state-machine table and diagram pairs, dependency placement
clarification and author/demo guidance. The
:download:`concept-gate inventory <round-12-inventory.json>` identifies content;
unchanged context preserves prior review/draft states. Old explicit-Escape
procedures must be reconciled during implementation, with original hover-Escape
assertions retained and actual regressions rerun. Runtime outcomes are a separate
gate; this acceptance does not publish or qualify a release.

Implementation feedback review
--------------------------------

The implementation retains the accepted component boundaries and contracts.
Shared content transport/restoration moved into ``inspect/content.js``; the
collection and persistent DOM managers stay inside INSPECT. RENDER owns dock
wiring, trigger refresh and current-size Reset. MODEL/DIRECTIVE own capacity
validation and graph serialization. No new dependency was introduced.

**STV_R12_005 (closed):** Ordinary navigation can suspend a page in the browser's
back-forward cache. Explicit ``pagehide`` clearing is needed to honor document
navigation clearing even in that case. The state table and editable persistent
Draw.io/SVG pair now include this action; the renderer clears without focus
restoration. This refines the accepted document-local lifetime, with no new owner
policy. The actual event handler is exercised in both publishing modes.

Historical explicit-Escape test procedures were revised to assert preservation
and use their Close control. Original hover-Escape assertions remain. Runtime
verification and source/artifact identities are in
:doc:`../test-execution/cr014-details/index`.

Final runtime and documentation gate
---------------------------------------

All 156 distinct executable checks pass, including corrected targeted usability
reruns, clean installed-wheel/source-archive checks and the rebuilt capacity
fixture. The normal warnings-as-errors documentation build and complete shared
traceability/evidence validation pass with 114 canonical cases and 717 execution
records. Strict mapping has no unmapped active requirement or unknown ID.
Fresh persistent SVG and embedded page were visually inspected after pagehide
feedback export. The :download:`completion inventory <round-12-completion.json>`
records the reconciled artifacts. No in-scope design or implementation finding
remains open; no release or publication is authorized by these local results.
