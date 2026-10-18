Architecture View for Software
==============================

Component responsibilities and interfaces; file mappings are listed in
:doc:`elements-software`.

.. raw:: html

   <object type="image/svg+xml" data="software-architecture.svg" style="width:100%;height:auto;aspect-ratio:1302/1152" aria-label="Interactive architecture diagram with links to Need objects">
     <a href="software-architecture.svg">Open linked architecture diagram</a>
   </object>

Build sequence
--------------

The exact hook priorities, failure ownership and incremental-build policy are
fixed in :doc:`implementation-plan`. Read the resolved NeedsView at write-started
priority 800; extract final rendered HTML with Beautiful Soup at build-finished
priority 900. Emit content-addressed details and the final manifest, then
patch STV-owned script/root attributes in view pages to the completed identity. Keep
the initial serial-build safety flags false. Source and type mappings remain
host-owned; no duplicate model registry is introduced.

Browser sequence
----------------

Initialize immutable graph data once per page and separate state per root.
A command proposes a candidate expansion set, computes seed-rooted visibility,
checks the 200-occurrence cap, and commits only on success. Layout receives the
visible graph and model ranks. Rendering and inspection consume its positions
without changing graph identities. Zoom and pan affect a per-view transform.

In shared mode, identity is the Need ID. Expansion keys are
``(Need ID, relation name, direction)``. Visible edges have canonical
``(source ID, relation name, target ID)`` identities; opposite-direction
navigation must not duplicate an authored edge. Rooted reachability removes
unreachable cycles after collapse. Visiting a cycle is distinct from recursively
unfolding it.

Later occurrence mode uses path-specific keys and terminal ancestor references.
Its projection/restore logic is isolated in the state component. Navigation in
shared mode after merging independently edited copies remains a later-release
review question; the MVP does not silently select a policy.

Layout and rendering
--------------------

Use ELK.js 0.10.0 for ordering suggestions, then STV's authoritative semantic
projection and final edge routing. Use D3 zoom/selection for view-local pan/zoom,
Floating UI DOM for overlay placement, and native HTML controls over SVG edges.
The complete algorithm and module APIs are specified in :doc:`implementation-plan`.
Do not use generic solver layers as semantic ranks or retain its edge paths
after moving nodes. See :ref:`STV_ADR_004` for the dependency decision.

Fixed node summary: complete ID and title visually clamped to two lines, with
full title in details. This is a fixed implementation choice, not an edit to
the accepted stakeholder baseline. Details use a focusable, dismissible overlay
with constrained height/width and scrolling. Expansion controls must not bubble
activation into the new-tab object link. A tooltip-to-overlay pointer transition
must not dismiss it. Pan gestures must not activate node links.

Interfaces and verification
---------------------------

See :doc:`internal-interfaces`, :doc:`technology-stack`,
:doc:`implementation-plan`, :doc:`verification-plan` and :ref:`STV_ADR_004`.
Unit checks target graph normalization, state transitions and geometry
invariants. Host integration fixtures cover build lifecycle, links and full
Need content. Browser checks cover file/HTTP behavior, keyboard focus and
pointer interactions on Firefox/Windows. None have been executed for a runtime
implementation: the product is not yet implemented.

Diagram source: ``architecture/diagrams/software-architecture.drawio``.
Edit in Draw.io and export SVG; element boxes link to their Need records.
