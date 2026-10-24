.. _STV_CR_014:

STV_CR_014: Persistent artifact details on the right side
=============================================================

Owner request
-----------------

Date: 2026-10-24. Status: implemented and development-verified; no release started.

**Language-corrected owner request:** When the user clicks an artifact's Details
button, display its details on the right-hand side of the screen instead of
directly over the node. Keep the details box open until the user clicks its
Close control. Stack additional details boxes vertically. Allow at most ten
open details boxes; when another box opens at that limit, automatically close
the first-opened box. Preserve the existing hover-tooltip behavior.

Source: project owner's request in this conversation.

Requested behavior
----------------------

* Explicit activation of an artifact's Details button opens a persistent details
  box in a region on the right-hand side of the screen, separate from the
  node-anchored hover tooltip.
* Multiple details boxes form a vertical stack in that right-side region.
  Each box identifies its artifact and has its own Close control.
* A details box remains open when the pointer leaves the artifact or box,
  another artifact is inspected, or the user interacts with the graph.
  Its normal dismissal is its own Close control.
* At most ten details boxes may be open simultaneously. Opening an additional
  box when ten are open automatically closes the oldest still-open box and
  adds the new box. Age means opening order, not last focus or interaction.
* Closing one box leaves the other boxes open. Capacity eviction is the
  explicit exception to remaining open until the user closes a box.
* A Close all details button shall be available in the same row as the other
  control buttons like e.g. Pan Down or Reset viewport. This button shall be 
  right aligned so it shows above the opened details boxes.
* Hover tooltips retain their existing content, delay, positioning, scrolling
  and dismissal behavior. Hovering does not create a persistent details box,
  occupy one of its ten slots or evict an existing box.

Acceptance criteria
-----------------------

1. Activating Details for artifact A immediately opens an identifiable box on
   the right side of the screen, rather than a details overlay at A's node.
2. Moving the pointer away, hovering another node, panning, zooming or expanding
   and collapsing graph relationships does not dismiss an open details box.
3. Opening Details for artifacts A, B and C displays three vertically stacked
   boxes. Closing B leaves A and C open with their artifact associations intact.
4. Opening ten distinct artifacts' details keeps all ten boxes open. Opening
   an eleventh closes the first-opened box and leaves the other nine plus the
   new box open. Repeating this operation evicts the next-oldest open box.
5. Interacting with or focusing an older box does not change eviction order.
   Closing a box manually frees a slot; opening a replacement at that point
   does not evict any other box.
6. Existing hover-tooltip regression scenarios still pass, including the
   approximately one-second hover delay, brief pointer crossings, movement
   into a tooltip, scrolling long content and viewport-edge containment.
   A hover tooltip can appear without changing the persistent-box collection.
7. Keyboard users can open, reach, read, scroll and close persistent details
   boxes with visible focus, preserving the existing accessibility obligations.

Affected requirements and concept work
------------------------------------------

* :need:`STV_SHR_015`: distinguish immediate explicit Details activation from
  unchanged transient hover inspection. Retain existing content and external/
  offline fallback rules for the detail information.
* :need:`STV_SHR_033`: preserve hover-tooltip readability and scrolling; define
  corresponding usable scrolling for long persistent boxes and the stack.
* :need:`STV_SHR_034`: retain keyboard access and visible focus for the new
  details region and its individual Close controls.
* :need:`STV_SWE_RENDER`: refine details-region placement, vertical stacking,
  box identity, focus management and dismissal controls. Assess state ownership
  and lifecycle contracts for the ten-box collection and oldest-first eviction.
* :doc:`/internal-interfaces` and :doc:`/verification-plan`: separate hover
  state from persistent details state and add placement, persistence, capacity,
  eviction, independent-close and tooltip-regression coverage.

These are impact references for later refinement. This request does not change
canonical requirements, their acceptance states or implementation code.

Owner decisions and configuration amendment
---------------------------------------------

The owner selected reuse/focus without refreshing eviction age, independent
per-view stacks and retention across seed/overview/page changes, including when
an artifact is no longer visible. New boxes append at the bottom. Escape remains
hover-only; normal document navigation/reload clears the in-memory collection.
The owner additionally requested a configurable capacity: conf.py setting
traceability_view_details_limit defaults to 10 and applies independently per view.

The dock is a responsive 360 px right column, moving below the graph for view
containers at or below 760 px. Individual boxes and the stack scroll. Close
restores the live trigger when present, otherwise the view's Close all control;
new/reused boxes focus their own Close control. These routine design choices
preserve the explicit owner decisions and keyboard usability.

Implementation handover
-------------------------

Follow :ref:`STV_ADR_010` and :doc:`/concept-reviews/round-12` for the reconciled
concept and test designs. Shared detail content/transport remains safe and
offline; hover and persistent lifecycle ownership are separated. No new release
or commit is authorized.

Implementation and verification: :doc:`../test-execution/cr014-details/index`.
