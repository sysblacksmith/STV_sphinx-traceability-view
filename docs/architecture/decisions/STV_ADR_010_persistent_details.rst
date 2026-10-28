.. _STV_ADR_010:

STV_ADR_010: Separate persistent details from hover inspection
==============================================================

Status: **accepted**. Date: 2026-10-24. Owner: project owner through scoped
review in :doc:`../../concept-reviews/round-12`.
Supersedes: partially :ref:`STV_ADR_003` for the shared explicit/hover inspection
lifecycle. Superseded by: partially :ref:`STV_ADR_012` for opt-in browser serialization
and reload restoration only. Other graph/exploration decisions remain.

Decision and ownership
-----------------------

:ref:`STV_CR_014` and the owner's three explicit answers/configuration request
are refined by :need:`STV_SHR_057`, :need:`STV_SWR_063`, :need:`STV_SWR_064`,
:need:`STV_SWR_065` and the revised :need:`STV_SWR_050` / :need:`STV_SWR_057`.
INSPECT owns a per-view insertion-ordered Need-ID collection and entry lifetimes;
RENDER owns its responsive dock, Close all and wiring. MODEL/DIRECTIVE validate
and publish the positive author limit, default 10, as graph.details_limit.

Keep Floating UI for transient hover. Persistent boxes use native CSS layout,
scrolling and nonmodal labelled regions. A shared content module owns cached
classic-script transport and safe fragment/ID/URL restoration, but each panel
gets independent DOM and async identity. Copied Need metadata uses a scoped
keyboard-accessible disclosure controller, initially folded; canonical artifact-ID
header links retain source-page navigation. No new dependency or network service.
Guard every deferred completion against the same still-live entry. Reuse focuses
without reinsertion; close/reopen creates a fresh entry. Keep age independent
of focus. Collection removal invalidates late completions without discarding
shared transport cache. Close failed entries and reopen to retry.

Graph changes close hover only. Persistent focus survives commits; live trigger
associations are refreshed after node control replacement. Closing restores the
current trigger or Close all. Explicit open/reuse reveals its Close control;
async body completion does not focus. Close all is per-view and remains usable
when empty. Escape affects hover only. Reset recomputes fit using current graph
viewport dimensions, avoiding a stale fit after dock width changes.

Alternatives and consequences
------------------------------

One shared panel cannot preserve hover dismissal while retaining explicit boxes.
A page-global stack violates the owner's independent-view choice. Duplicate
boxes, focus-based LRU and clearing on reseed contradict explicit decisions.
A fixed overlay obscures graph content; a native responsive dock reserves space
and moves below the graph on narrow containers. The dock targets 720 px,
reserving graph space beside it only above a 1120 px container width. Reading long content uses both
bounded box and stack scrolling. Opening the dock can reduce graph width; graph
world positions/transform are preserved until the reader requests Reset.

The original CR014 decision did not serialize the collection into Needs, URL,
local storage or sessions, and navigation/reload created a fresh page. This
portion is superseded by :ref:`STV_ADR_012` only when the reader opts into
remembering the view; the default remains fresh-page behavior. Configuration is author-side, not a
reader capacity control. No later occurrence-mode delivery or release is implied.

Handover and verification
---------------------------

:need:`STV_TC_SW_049`, :need:`STV_TC_SW_050`, :need:`STV_TC_SY_063` and
:need:`STV_TC_SY_064` cover collection/configuration, real file/HTTP presentation,
focus, races and safe shared content. Re-review old explicit-Escape test designs
against the new Close policy while retaining unchanged hover-Escape assertions.
Update coordinated state tables and adjacent Draw.io/SVG diagrams before delivery.
