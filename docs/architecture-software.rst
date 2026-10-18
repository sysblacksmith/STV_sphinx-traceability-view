Architecture View for Software
==============================

Proposed component design; file mappings are listed in :doc:`elements-software`.

.. raw:: html

   <object type="image/svg+xml" data="software-architecture.svg" style="width:100%;height:auto;aspect-ratio:1140/780" aria-label="Interactive architecture diagram with links to Need objects">
     <a href="software-architecture.svg">Open linked architecture diagram</a>
   </object>

Build sequence
--------------

1. Register the directive, namespaced configuration and static assets through
   the Sphinx extension setup entry point.
2. Parse invocations into serializable placeholders with source locations.
   Do not resolve forward-referenced IDs during parsing.
3. After the host has resolved Needs, normalize configuration and snapshot the
   complete project graph, including generated incoming indexes.
4. During HTML writing, capture final host-rendered Need fragments across all
   pages. Before reporting completion, emit the details bundle and data script.
   Handler ordering must be verified against the pinned host toolchain.
5. Invalidate generated data when source Needs, mappings or rendered details
   change. The MVP supports serial builds; parallel-safety flags must remain
   false until merge/purge behavior has dedicated checks.

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

Use an internal rank-based layout: horizontal slots within ordered rank bands,
a right-side test lane, and SVG edges behind HTML node controls. Compute ranks
from semantic mappings, not graph depth. Cycles can cross rank bands without
changing their semantic order. Place shared test nodes beyond the rightmost
associated artifact. This gives a deterministic starting point; crossing and
spacing quality require prototype assessment rather than a claim of optimality.

Fixed node summary: complete ID and title visually clamped to two lines, with
full title in details. This is a proposed implementation choice, not an edit to
the accepted stakeholder baseline. Details use a focusable, dismissible overlay
with constrained height/width and scrolling. Expansion controls must not bubble
activation into the new-tab object link. A tooltip-to-overlay pointer transition
must not dismiss it. Pan gestures must not activate node links.

Interfaces and verification
---------------------------

See :doc:`internal-interfaces`, :ref:`STV_ADR_002` and :ref:`STV_ADR_003`.
Unit checks target graph normalization, state transitions and geometry
invariants. Host integration fixtures cover build lifecycle, links and full
Need content. Browser checks cover file/HTTP behavior, keyboard focus and
pointer interactions on Firefox/Windows. None have been executed for a runtime
implementation: the product is not yet implemented.

Diagram source: ``architecture/diagrams/software-architecture.drawio``.
Edit in Draw.io and export SVG; element boxes link to their Need records.
