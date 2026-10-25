.. _STV_ADR_011:

STV_ADR_011: Separate exploration, page metadata and SVG capture
================================================================================

Status: **proposed**. Date: 2026-10-25. Decision owner: project owner.
Supersedes: none. Superseded by: none.

Context
-------

The accepted :need:`STV_CR_015` through :need:`STV_CR_018` add navigation reset,
SVG output, independent detail typography and page-wide host metadata controls.
Their stakeholder obligations are :need:`STV_SHR_058`, :need:`STV_SHR_059`,
:need:`STV_SHR_060` and :need:`STV_SHR_061`. The owner permits browser-managed
Save As with documented location-prompt settings. Existing shared identity,
offline content policy and persistent-card lifecycle remain applicable.

Decision
--------

STATE owns collapse-all as a new atomic transition, clearing all expansion
sets/page caches while retaining current seed IDs or restoring the initial
project overview. RENDER requests a fresh fit and invalidates pending layouts;
INSPECT preserves persistent cards. No seed parser/schema change is needed.

MODEL/DIRECTIVE publish independent author font scales, both 0.7 by default.
INSPECT scales computed unscaled typography once per clone; original host Need
tables and ordinary graph node typography are unchanged. Page metadata controls
belong to RENDER's separate page controller, delivered by DIRECTIVE even on pages
without a view. They never traverse copied detail subtrees. Host per-Need click
handlers remain authoritative: bulk commands activate only controls whose
actual row visibility differs from the requested state, then synchronize ARIA.

EXPORT is a cohesive tenth software component contained in
:need:`STV_SE_BROWSER`. Its inputs are the committed view presentation,
read-only visible INSPECT regions and immutable local resource records. It
creates a standalone SVG with an XHTML foreignObject snapshot, explicit computed
styles, crop/scroll wrappers and retained vector graph SVG. XMLSerializer escapes
text/attributes; no executable scripts, controls or graph datasets are serialized.
The download is a native Blob/object-URL HTML-anchor operation. The file is a
browser-viewable SVG, not a promise of native editable objects in every vector
editor. No export library, canvas rasterization or runtime service is added.

DETAIL_BUILD/BUNDLE collect output-contained resources at build finalization.
They embed validated local image/font bytes, including resources needed by safe
copied HTML styles, in content-addressed classic-script records. Remote media
retains the existing unavailable indication; missing required local media makes
export fail visibly. EXPORT never uses fetch/XHR or reads browser-local files.
The exact resource and capture interfaces are in :doc:`../../internal-interfaces`.

Alternatives and trade-offs
---------------------------

* Full-graph export contradicts the owner's visible-area choice.
* A required showSaveFilePicker API does not meet retained Firefox availability;
  browser download prompts are the approved cross-browser location mechanism.
* html-to-image/dom-to-image style libraries also depend on DOM cloning and
  foreignObject, and commonly resolve fonts/images asynchronously. A narrow
  product-owned serializer can reuse STV's safe resource boundary, avoid runtime
  fetches and capture committed revision/scroll state explicitly. This choice
  carries responsibility for computed-style, clipping and pseudo-element tests.
* A screenshot/canvas-only image inside SVG loses vector text/edges and introduces
  image-origin constraints. A pure SVG reimplementation of arbitrary host HTML
  would duplicate browser text/table layout and is substantially broader.
* Invoking a global host toggle unconditionally would invert mixed initial
  states and may affect copied details. Explicit per-table targets preserve
  local scope and existing individual behavior.

Evidence, consequences and validation
-------------------------------------

The existing frontend lock remains authoritative; no new third-party dependency
or license obligation is introduced. Native API compatibility follows the retained
Firefox desktop policy, with additional mobile testing optional rather than
inferred from the owner's earlier demo smoke tests.

Primary API references checked 2026-10-25:
`foreignObject <https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/foreignObject>`_,
`XMLSerializer <https://developer.mozilla.org/en-US/docs/Web/API/XMLSerializer/serializeToString>`_,
`object URLs <https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL_static>`_
and `HTML download behavior <https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#download>`_.
`Mozilla's picker tracking issue <https://bugzilla.mozilla.org/show_bug.cgi?id=1930240>`_
documents the Firefox picker gap. API availability alone does not prove snapshot
fidelity; the feasibility probe and remaining implementation checks are recorded
centrally in :doc:`../../maturity`.

The canonical cases :need:`STV_TC_SY_066` through :need:`STV_TC_SY_069` and
:need:`STV_TC_SW_051` through :need:`STV_TC_SW_055` cover this increment.
No existing accepted ADR is superseded: topology and interfaces are extended,
while previously accepted exploration, layout and card lifecycle choices remain.
