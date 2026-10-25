Round 15: CR015-018 controls and SVG concept
================================================================================

Authority and baseline
----------------------

Date: 2026-10-25. Reviewer: Codex. Decision owner: project owner through explicit
conversation delegation: "Review and accept clean artifacts on my behalf."
The owner first requested a side branch and commit, then invoked concept-review.
The prepared input is commit ``2e1eace`` on ``concept-cr015-018``; parent main
is ``8dbbe79``. Review corrections and acceptance are subsequent branch changes.
The versioned method is engineering-method 1.0.0, schema 1, identified by
``tools/method/.method-package.json``. No new method or requirement type is used.

The owner previously accepted :need:`STV_CR_015`, :need:`STV_CR_016`,
:need:`STV_CR_017`, :need:`STV_CR_018` and :need:`STV_SHR_058`,
:need:`STV_SHR_059`, :need:`STV_SHR_060`, :need:`STV_SHR_061`. Save-location
choice uses browser-managed Save As with documented prompt settings. These
stakeholder decisions are input evidence, not this reviewer's new approval.

Inventory and scope
-------------------

``round-15-inventory.json`` records SHA-256 identities of the reviewed final
source set, configured model/manifests and every exported current Need, with
explicit increment/baseline/history dispositions. It includes the full current
concept inventory, not only changed files. Retained unmodified requirement,
case and ADR decisions rely on their existing review records; they are not
bulk reaccepted or claimed as new full-product runtime evidence here. Historical
execution payloads and rounds 1-14 remain immutable evidence. Later occurrence
mode retains its existing deferral and statuses; this round does not accept it.

The substantive review covers all four input obligations, every new derivation,
allocation/containment and verifies path, the changed component contracts and
their relevant baseline neighborhood. Assessed ordinary documents are
:doc:`../requirements-stakeholder`, :doc:`../requirements-system`,
:doc:`../requirements-software`, :doc:`../elements-system`,
:doc:`../elements-software`, :doc:`../architecture-system`,
:doc:`../architecture-software`, :doc:`../state-machine`,
:doc:`../internal-interfaces`, :doc:`../technology-stack`,
:doc:`../implementation-plan`, :doc:`../verification-plan`,
:doc:`../traceability`, :doc:`../review`, :doc:`../sources` and
:doc:`../maturity`, with their navigation/configuration/build/manifest context.
The current ADR chain was checked for retained/superseded scope; this increment
accepts :ref:`STV_ADR_011` without superseding earlier accepted choices.

Findings, corrections and closure
---------------------------------

Each finding was initially acceptance-blocking for its dependent path. Owner for
correction/recheck: Codex under delegated review. All are resolved on 2026-10-25;
their original observations are retained here, not erased by the corrections.

**STV_REVIEW_015_001 — host activation and mixed state.** The original interface
said to invoke a per-Need control, but installed Sphinx-Needs 8.2.0 attaches its
handler to nested arrow spans. A wrapper click can do nothing, and blindly
toggling mixed rows cannot guarantee a bulk target state. Native individual
clicks also did not own the new ARIA synchronization. Affected:
:need:`STV_SWR_069`, :need:`STV_SWE_RENDER`, :need:`STV_TC_SW_054`,
:need:`STV_TC_SY_069`, ADR011 and the metadata interface. Resolution: explicitly
activate the displayed host icon only for uniformly opposite states, normalize
mixed rows, and add synchronization-only post-host handling plus keyboard
forwarding. Installed ``sphinx_needs_collapse.js`` was inspected: its handler is
``$(this).find("span.needs.collapsed, span.needs.visible").click(...)``.
Closure: requirements, interface, ADR and both tests agree on one handler action,
mixed-state normalization and subsequent individual row/icon/ARIA consistency.

**STV_REVIEW_015_002 — initialization order.** DOM-ready alone does not express
that the host jQuery collapse handlers exist, especially with late rootless
page initialization. Same affected page-control path as finding 001. Resolution:
window-load plus jQuery-ready gates, already-complete handling and readable
disabled state for missing prerequisites; no second visibility toggle handler.
Closure: both before/after-load fixtures and rootless pages are explicit in
:need:`STV_TC_SW_054`; the page controller cannot enable prematurely.

**STV_REVIEW_015_003 — capture readiness and empty crop.** The original capture
contract lacked a result for a wholly off-screen workspace and could leave an
implementer to wait for fonts then capture a later DOM revision. Affected:
:need:`STV_SWR_070`, :need:`STV_SWR_071`, :need:`STV_TC_SW_053`,
:need:`STV_TC_SY_067` and the EXPORT interface. Resolution: reject zero-area
capture readably without scrolling/downloading; resource/font readiness is a
retryable preparation condition, failure is visible, and capture never waits
asynchronously then rereads live DOM. Closure: negative/recovery procedures and
expected outcomes now state these paths, while immutable one-task capture holds.

**STV_REVIEW_015_004 — metadata diagram margins.** The retained metadata picture
had insufficient space around its upper transition label in standalone rendering.
This is a visual-quality correction, not a changed metadata lifecycle. Resolution:
add a transparent diagram-bounds frame in detail-metadata.drawio and re-export
through installed Draw.io. Closure: re-inspect standalone/embedded rendering and
the retained linked target. The prior round-13 source/hash remains historical;
this round identifies the corrected picture rather than rewriting that review.

**STV_REVIEW_015_005 — review navigation.** Round 14 was linked from maturity but
missing from the concept-review toctree. Resolution: add its existing page and
this round to that index without changing its content. Closure: strict Sphinx
navigation/reference build succeeds and historical round content is unchanged.

Semantic traceability and test-case review
------------------------------------------

* :need:`STV_SHR_058` channels to :need:`STV_SWR_066`, allocated to
  :need:`STV_SWE_STATE` and :need:`STV_SWE_RENDER`. :need:`STV_TC_SW_051`
  checks pure state/cache/revision behavior and :need:`STV_TC_SY_066` the actual
  independent-view/card/focus lifecycle. Current roots, cleared page history,
  cycles, project-entry exceptions and transactional failure are covered. Global
  collapse is a fresh navigation command, consistent with the retained fresh
  scene exception in :need:`STV_SHR_054` and :ref:`STV_ADR_008`, not a change
  to stable ordinary group/root toggles. :need:`STV_SHR_003`,
  :need:`STV_SHR_047`, :need:`STV_SHR_048` and :need:`STV_SHR_053` retain
  initialization/seed authority; :need:`STV_SHR_057` retains card lifetime.
* :need:`STV_SHR_059` derives through :need:`STV_SYS_011` to
  :need:`STV_SWR_070`, :need:`STV_SWR_071`, :need:`STV_SWR_072`.
  :need:`STV_SWE_DETAIL_BUILD` and :need:`STV_SWE_BUNDLE` own output-local
  bytes and content identity; :need:`STV_SWE_EXPORT` owns capture/XML/resources/
  download; RENDER owns activation and presentation geometry. Each software
  allocation is inside an actual parent-system allocation, BUILD or BROWSER.
  :need:`STV_TC_SW_053` reviews capture/serialization/save lifecycle,
  :need:`STV_TC_SW_055` resource safety/identity and :need:`STV_TC_SY_067`
  complete offline visible-area/save fidelity. Their procedures cover normal,
  negative, capacity, cancellation, recovery, viewport, font and resource paths.
  :need:`STV_SYS_003`, :need:`STV_SYS_006`, :need:`STV_SYS_007`,
  :need:`STV_SHR_017`, :need:`STV_SHR_018`, :need:`STV_SHR_033`,
  :need:`STV_SHR_038`, :need:`STV_SHR_039`, :need:`STV_SHR_040` and
  :need:`STV_SHR_043` retain offline, inspection, isolation, viewport and capacity
  constraints. Explicit export failure for unavailable/unsafe resources does not
  waive any live-detail behavior or silently offer a broken successful file.
* :need:`STV_SHR_060` channels to :need:`STV_SWR_067` and
  :need:`STV_SWR_068`. :need:`STV_SWE_MODEL` validates;
  :need:`STV_SWE_DIRECTIVE` serializes author settings;
  :need:`STV_SWE_INSPECT` and RENDER apply independent once-only presentation
  scales. :need:`STV_TC_SW_052` covers input/default/legacy/identity and DOM
  sizing; :need:`STV_TC_SY_068` full readable content, reuse, delayed fonts,
  scrolling, browser zoom and unaffected source/node typography. Existing
  :need:`STV_SHR_015`, :need:`STV_SHR_033`, :need:`STV_SHR_034` and
  :need:`STV_SHR_057` are retained constraints, not weakened by text reduction.
* :need:`STV_SHR_061` channels to :need:`STV_SWR_069`; RENDER owns page-local
  DOM actions and DIRECTIVE delivery on pages without graph roots. Both cases
  SW054/SY069 cover mixed states, outside-viewport objects, multiple types,
  individual operation afterward, absent/unsupported metadata, keyboard/ARIA
  and exclusion of copied detail/view subtrees. Page metadata is a local browser
  presentation obligation without a new external system service; this justifies
  channeling, as for navigation reset and font settings. All allocated software
  components retain their proper BUILD/BROWSER containment.

The nine new cases have concrete tools/fixtures, procedures and observable
criteria and are accepted as designs. They remain ``last_result: not_run``
without execution links. Existing case/execution ownership, timestamps and latest
results are checked by the full validator; no historical result or requirement
verification flag is promoted. Semantic review does not infer correctness from
the link graph alone. Ordinary graph/keyboard/offline/detail baseline cases stay
in implementation regression scope; this review does not rerun the released
product qualification or claim fresh all-product test execution.

Architecture, feasibility and visual review
-------------------------------------------

The full current diagrams and their containing pages were rendered in installed
headless Firefox: system-architecture, software-architecture, state-machine,
persistent-details, detail-metadata and view-export, plus architecture-system,
architecture-software and state-machine HTML. Exported SVGs and their embedded
views were inspected for connector identity, arrowheads, labels and reading scale.
The margin issue above was corrected; no remaining ambiguous connector or
unrelated-box crossing blocks the reviewed paths. Embedded objects retain direct
SVG fallback links and adjacent editable Draw.io sources. The new companion
export view extends rather than falsifies the retained nine-component core.

The architecture has explicit data/state/error ownership, output-root resource
containment, inert XML composition, local classic-script transport and no runtime
fetch/service. Installed manifests retain pinned dependencies and existing legal
inputs; no dependency or lock change is introduced by a new native-API module.
Primary API evidence and the earlier standalone foreignObject fixture support
technology feasibility, not arbitrary host-content fidelity. Full integrated
resource/style export remains the first implementation gate, with explicit tests
rather than an unresolved technology choice. The safe imported SVG allowlist and
readable failure policy are explicit; vector-editor portability and mandatory
filesystem pickers are outside the accepted scope.

Acceptance and remaining work
------------------------------

After closure and final checks, delegated acceptance covers exactly:
:need:`STV_SYS_011`; :need:`STV_SWR_066` through :need:`STV_SWR_072`;
the eight component revisions DIRECTIVE, MODEL, DETAIL_BUILD, BUNDLE, STATE,
RENDER, INSPECT and EXPORT; all nine test-case designs listed above; ADR011;
and the inventoried ordinary concept documents/pictures for this increment.
These are 25 modeled internal/case artifacts plus one ADR, not a new acceptance
of every historical/current Need in the repository. The exact final identities
and individual dispositions are in ``round-15-inventory.json``.

Verification remains not_assessed, new cases remain not_run, product code is
unchanged, and the CRs stay accepted rather than implemented. Implementation
starts only with separate authority. Use the accepted :doc:`../implementation-plan`
and canonical case IDs as handover; offline SVG first-slice fidelity, packaging,
full regressions and release qualification are execution gates, not open concept
findings. Full-graph export, later occurrence mode, native vector-editor editing
and new mobile/touch qualification retain their explicit exclusions/deferrals.

Final commands and results are consolidated in :doc:`../maturity`.
