.. _STV_ADR_012:

STV_ADR_012: Browser-local opt-in view snapshots
================================================

Status: **accepted**. Date: 2026-10-28. Type/scope: software persistence. Decision owner: project owner through
CR019 concept-review delegation. Supersedes: partially :ref:`STV_ADR_010` only
for its unconditional no-serialization/reload-clearing policy. Superseded by: none.

Decision
--------

Use the browser Web Storage localStorage API, synchronous guarded getItem,
setItem and removeItem, with versioned JSON and independent view keys. STATE
validates data against the current published graph; RENDER owns UI/wiring,
LAYOUT owns validated placement and INSPECT owns ordered card reopening.
See :need:`STV_SWR_073`, :need:`STV_SWR_074`, :need:`STV_SWR_075` and
:doc:`../../internal-interfaces`. No dependency, account or server is added.

Alternatives and consequences
-----------------------------

Cookies send state to the server and impose small payload limits. Session storage
would not meet browser-restart retention. IndexedDB offers asynchronous storage
but adds transactions for a bounded 200-node snapshot. Native localStorage is
sufficient; reads/writes can throw and must remain recoverable. Store identifiers,
exploration, geometry and transform only, never rendered HTML or hidden content.
Storage is local and may be cleared by the user/browser. file URL support varies;
unsupported storage produces an explanation while offline exploration works.

Platform evidence: Web Storage API and Window.localStorage documentation:
https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage .
Product-specific validation, isolation and recovery remain STV responsibilities.
Real browser file/HTTP feasibility and failure injection are implementation gates.

Verification
------------

:need:`STV_TC_SW_056` and :need:`STV_TC_SY_070` define snapshot and real-host
criteria. No runtime result is implied by this decision.

Affected components: :need:`STV_SWE_STATE`, :need:`STV_SWE_RENDER`,
:need:`STV_SWE_LAYOUT`, :need:`STV_SWE_INSPECT`. Scoped review and acceptance
are recorded in :doc:`../../concept-reviews/round-16`.
