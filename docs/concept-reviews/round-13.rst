Round 13: Detail acceptance corrections
=========================================

Scope and authority
----------------------

The owner's acceptance findings and instruction to continue authorize the
correction of CR014's detail presentation. :need:`STV_PR_015` preserves the
request and cause mapping. This scoped technical review continues the existing
CR014 concept-review/implementation delegation; it does not claim the owner's
acceptance retest. Input is commit ``740c35ce234ec26b16c76a0b77463b273f84863c``
plus the prior uncommitted CR014 worktree and the retained correction identity.

No stakeholder intent, capacity, collection policy, deployment interface or
architecture allocation changes. :need:`STV_SWR_064` refines exact presentation
and disclosure/navigation behavior inside INSPECT/RENDER. Its metadata remains
available on demand under :need:`STV_SWR_015`; the third-party-widget script
exclusion is preserved. This is owned Need metadata behavior, not execution of
arbitrary host widget JavaScript. Source-page navigation continues existing
safe local URL/original-object obligations.

Findings and disposition
--------------------------

* **R13_001 closed:** 360 px gives insufficient reading width. A 720 px target
  doubles the dock; a 1120 px breakpoint leaves useful graph space, with a
  right-aligned, bounded below-graph dock in narrower containers.
* **R13_002 closed:** Document-ready host scripts cannot initialize lazy clones.
  The shared content restorer owns per-copy folded/expanded state and accessible
  pointer/keyboard events, with no global handler or collection mutation.
* **R13_003 closed:** Universal fragment rebasing localizes the artifact ID.
  Header-ID anchors keep canonical source URLs/new-tab behavior; ordinary body
  anchors retain namespace mapping. Actual new-tab navigation is tested.

:need:`STV_TC_SY_065` is accepted as a concrete real-host regression design.
Existing alternate-model procedures now explicitly expand metadata before
checking it; their metadata-availability criterion is retained. Changed internal
interfaces, ADR010 clarification, SWR064 refinement and metadata transition table/
Draw.io/SVG pair are consistent with the implementation and owning boundaries.
The component design introduces no dependency or changed collection/graph state.

Verification
---------------

The two-protocol baseline fails. After the fixes, all 127 distinct selected
executables pass: 72 Python unit/host/package, 36 Node component and 19 Firefox
variants (eight persistent/metadata and eleven adjacent). The focused report
also repeats three already-covered host builds. Capacity and full release
qualification are not claimed. Runtime results, exact commands and source/
artifact identity are in :doc:`../test-execution/pr015-details/index`.

The scoped concept corrections and test design are accepted under the existing
delegation. Final publication/link checks and visual review are recorded in the
same execution record; owner acceptance retest remains pending. Historical round
12 inventories and its earlier 360 px verification remain unchanged snapshots.


Completion review
--------------------

The new disclosure diagram and normal HTML embedding are readable and match
the implemented per-copy transitions. The actual rebuilt project demo confirms
720 px width, initially folded metadata and a header-ID URL at the source Need.
Both refined file/HTTP variants pass explicit icon/unique-ID checks. Sphinx
warnings-as-errors, complete shared evidence validation and strict executable
mapping pass. :download:`Completion inventory <round-13-inventory.json>` records
the assessed content; unchanged context retains prior review states. No scoped
technical finding remains open. Owner acceptance retest is still pending.


Pane-frame follow-up review
-----------------------------

The owner's annotated screenshot identifies an unmarked clipping boundary and
blurred top-card edge. The refinement adds a 1 px neutral-grey frame to the pane,
inside its existing width, aligned to the graph's full outer height. Inset
padding and shadow-free cards keep a crisp top edge; the narrow layout cap and
hidden-pane rule remain. This state-neutral CSS change updates SWR064 and SY065
within the same presentation scope. All ten affected file/HTTP browser variants
pass. Owner acceptance retest remains pending; no new release/capacity claim.


The framed normal demo was visually inspected with two boxes; the separator is
continuous and the first card has a clean inset. Sphinx and complete evidence
validation pass for the follow-up (115 canonical cases, 809 executions). The
completion inventory now includes this state-neutral refinement.

Owner acceptance
------------------

The owner explicitly approved readiness item 2 on 2026-10-24, accepting this
final presentation and pane-frame follow-up. :doc:`round-14` records the
decision. Earlier pending-owner statements above remain historical. No new
manual retest execution is inferred.
