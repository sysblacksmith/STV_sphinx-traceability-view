CR019 scoped concept review, round 16
=====================================

Authority and scope
-------------------

On 2026-10-28 the project owner explicitly accepted the exact stakeholder
amendment in PR #6 and invoked concept creation, concept review and concept
implementation. This delegates acceptance of clean concept artifacts for
:need:`STV_CR_019`; no release or deployment is authorized. Input revision:
``ae0c0b5a5af6a03e13fd3ef4911888bfaa66442e`` plus this recorded increment.
The reviewer is the Codex assistant applying the owner's invoked engineering workflow skills.
Historical rounds and results retain their original identities.

Inventory and semantic review
-----------------------------

Accepted stakeholder inputs are :need:`STV_SHR_003`, :need:`STV_SHR_057`,
:need:`STV_SHR_062`, :need:`STV_SHR_063`, :need:`STV_SHR_064` and
:need:`STV_SHR_065`. Existing visibility, capacity, keyboard, offline and static
hosting requirements remain unchanged. The increment reuses existing browser
components and dependencies; no artificial system requirement/service is added.

* :need:`STV_SWR_073` channels opt-in lifecycle, isolation and storage failures
  into STATE/RENDER with an explicit no-system-boundary rationale.
* :need:`STV_SWR_074` channels startup/exploration/recovery into current-graph
  validation; rooted reachability and the existing cap remain authoritative.
* :need:`STV_SWR_075` covers placement, card age and viewport restoration;
  RENDER/LAYOUT/INSPECT ownership remains within STV_SE_BROWSER.
* Revised :need:`STV_SWR_003` and :need:`STV_SWR_063` reconcile the startup and
  detail lifecycle with the owner-accepted exception, preserving stable IDs.
* :need:`STV_SWE_STATE`, :need:`STV_SWE_RENDER`, :need:`STV_SWE_LAYOUT` and
  :need:`STV_SWE_INSPECT` describe the expanded responsibilities and source maps.
* :need:`STV_TC_SW_056` covers schema, current-data authority, limits and storage
  failure handling. :need:`STV_TC_SY_070` covers real reload, scope, card FIFO,
  viewport and failure/race behavior. Their procedures/expected outcomes were
  read against every changed requirement, not inferred from nonempty links.

Ordinary artifact scope: :doc:`../internal-interfaces`,
:doc:`../architecture-software`, :doc:`../implementation-plan`,
:doc:`../verification-plan`, :doc:`../technology-stack`,
:doc:`../state-machine` and :ref:`STV_ADR_012`. :ref:`STV_ADR_010` is partially
superseded only for no-serialization/reload clearing; its other decisions remain.
The existing system context, runtime dependencies, build hooks, host filtering,
public graph schema, export architecture and unrelated diagrams are retained.
Their interfaces were checked for the affected startup/storage/detail paths.
Exact accepted source identities are in ``round-16-inventory.json`` alongside
this record, without changing historical review hashes.

Findings and resolutions
------------------------

* **STV_REVIEW_16_001, resolved:** Unconditional collapsed startup and reload
  clearing contradicted persistence. The owner accepted the exact SHR exceptions;
  SWR003/SWR063 now carry the corresponding clauses. Closure: no unconditional
  startup obligation overrides a compatible opted-in snapshot.
* **STV_REVIEW_16_002, resolved:** Saved positions alone omit stable-navigation
  band offsets. Snapshot geometry includes band tops; current dimensions, ranks
  and topology gate reuse. Invalid geometry retries fresh validated layout.
  Closure: post-reload navigation retains the existing stable-slot contract.
* **STV_REVIEW_16_003, resolved:** A pagehide card cleanup could overwrite a
  saved collection with an empty one. Enabled remembering suppresses pagehide clearing/writing; unchecked views retain ordinary cleanup.
  Closure: saved cards survive reload and back/forward cache lifecycle.
* **STV_REVIEW_16_004, resolved:** The enable connector shared the startup
  connector junction in the first export. Distinct ports/waypoints separate the
  flows. Draw.io 32.6.1 exports the adjacent SVG; standalone and embedded Firefox
  rendering are inspected for labels, arrows, unrelated-box crossings and links.
* **STV_REVIEW_16_005, resolved:** First implementation wiring incorrectly
  attached a D3 end listener to a DOM listener return value, preventing mount.
  The listener now belongs to D3; real mount/reload tests exercise that boundary.
  This failure was corrected rather than treated as a passing feasibility check.

Decision and checks
-------------------

The five internal requirement revisions, four component revisions, two new case
designs, ADR012, scoped ADR010 supersession and ordinary artifacts above are
accepted after substantive method, semantic, architecture/lifecycle, coverage,
consistency and feasibility review under the owner's delegation. No stakeholder
wording is changed by this review. Ordinary documents have no invented status.

Strict Sphinx/publication and full graph/evidence validation with
``--require-test-coverage``, trace/test CSV exports passed on the concept
increment. The executable inventory contains no unmapped active SYS/SWR IDs.
The new diagram source/export links and standalone/embedded rendering were
checked. Primary platform API behavior is exercised by real Firefox file/HTTP
snapshot tests, distinct from concept acceptance. Case designs remain not_run
until formal execution records are created; development runs do not fabricate
execution Needs. Requirement verification is not advanced by this decision.

Implementation handover
-----------------------

Use :doc:`../implementation-plan` and :doc:`../verification-plan` with the
versioned protocol in :doc:`../internal-interfaces`. The owner already authorized
implementation. Windows desktop qualification, release publication and later
occurrence mode remain separate; this development environment is Linux with
Firefox 159.0, Python 3.12 and Node 24.19.0. Actual implementation results and
remaining verification limits are recorded centrally in :doc:`../maturity`.
