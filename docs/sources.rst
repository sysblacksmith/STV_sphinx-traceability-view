Sources and evidence
====================

Source: project owner discussion in this chat, 2026-10-18. The initial request describes RST embedding, a starting Need ID, interactive expansion and collapse, hierarchical artifact placement and test cases on the right. Requirement wording is a draft interpretation, not formal acceptance.


Project owner clarification, 2026-10-18: explicitly confirmed navigation in both directions. Basis for STV_SHR_013.

Project owner clarification, 2026-10-18: agreed to configurable model mappings
and explicitly stated that the data model shall be an input and replaceable.
Basis for STV_SHR_014.

Project owner clarification, 2026-10-18: requested shortened information in
nodes, details in hover tooltips, and a node click opening the corresponding
Need object in a new tab. Basis for the refinement of STV_SHR_008 and for
STV_SHR_015 and STV_SHR_016.

Project owner clarification, 2026-10-18: confirmed that the generated
documentation must work offline and on static hosting without an application
server, with the data needed for exploration included in the build output.
Basis for STV_SHR_017 and STV_SHR_018.

Project owner clarification, 2026-10-18: requested an option selectable within
the view to choose between a shared node and separate occurrences per branch
for an object reached through multiple branches. Basis for STV_SHR_019.

Project owner clarification, 2026-10-18: agreed that one shared node shall be
the default display mode. Basis for STV_SHR_020.

Project owner clarification, 2026-10-18: explicitly confirmed that switching
display modes must preserve exploration state and identified this as an
implicit expectation of the earlier mode-switching request. Basis for STV_SHR_021.

Project owner clarification, 2026-10-18: agreed to independent expansion of
separate occurrences and showing the union of their expanded traces when
switching to shared mode. Basis for STV_SHR_022 and STV_SHR_023.

Project owner clarification, 2026-10-18: agreed that cycles show the closing
connection to the existing object, using a reference to the existing occurrence
in separate-occurrence mode, rather than generating endlessly repeated branches.
Basis for STV_SHR_024.

Project owner clarification, 2026-10-18: agreed that collapsing one branch
retains objects reached through another open path, and objects disappear only
when no open path from the starting object reaches them. Basis for STV_SHR_025.

Project owner clarification, 2026-10-18: agreed that an invalid starting ID
shall fail the Sphinx build with a clear error identifying the ID and its
source location. Basis for STV_SHR_026.

Project owner clarification, 2026-10-18: broken traces shall fail the build
through the build's own validation rather than the extension; the extension
shall render anyway. Basis for STV_SHR_027.

Project owner clarification, 2026-10-18: confirmed that a missing trace target
shall appear as a clearly marked placeholder containing its ID so that the
broken trace remains visible for investigation. Basis for STV_SHR_028.

Project owner clarification, 2026-10-18: agreed that an object with no
relationships displays "No related objects" without expansion controls, and
relationship types with no targets have no plus sign. Basis for STV_SHR_029.

Project owner clarification, 2026-10-18: agreed that omitting the starting ID
shall fail the build with an error identifying the RST invocation. Additional
basis for STV_SHR_026.

Project owner clarification, 2026-10-18: agreed to ID and shortened title in
nodes, without configurable fields or shortening limits for now. Requested
different background colors by artifact type and red "edge color" for artifacts
not in state "accepted"; the meaning of edge remains to be clarified.
Basis for refinement of STV_SHR_008 and for STV_SHR_030.

Project owner clarification, 2026-10-18: confirmed that red "edge color" means
the border around the node when the artifact is not in state "accepted".
Basis for STV_SHR_031.

Project owner clarification, 2026-10-18: confirmed that the replaceable input
model defines which status values count as accepted, defaulting to "accepted".
Basis for STV_SHR_032 and refinement of STV_SHR_031.

Project owner clarification, 2026-10-18: requested all information shown by
the full Need object in its tooltip, with no configurable field selection,
and expressed concern about accumulating too many configuration options.
Basis for refinement of STV_SHR_015.

Project owner clarification, 2026-10-18: agreed that long tooltips stay within
the browser window, remain open while hovered and allow scrolling through
their content. Basis for STV_SHR_033.

Project owner clarification, 2026-10-18: agreed to keyboard-only expansion,
collapse, detail inspection, display-mode switching and opening original
objects, with a visible focus indicator. Basis for STV_SHR_034.

Project owner clarification, 2026-10-18: deferred touch-device interaction
support to a later release; no target release was assigned.

Project owner clarification, 2026-10-18: agreed to separate incoming and
outgoing trace controls using directional labels supplied by the input model,
such as "derives from" and "refined by". Basis for STV_SHR_035.

Project owner clarification, 2026-10-18: agreed to reusing artifact-type colors
from the host Sphinx-Needs configuration. Basis for refinement of STV_SHR_030.

Project owner clarification, 2026-10-18: requested a default color scheme when
artifact-type colors are not configured. Additional basis for STV_SHR_030.

Project owner clarification, 2026-10-18: agreed that an artifact without a
status value counts as not accepted and has a red node border. Additional
basis for STV_SHR_031.

Project owner clarification, 2026-10-18: agreed that shared test cases appear
once to the right of all connected artifacts with their connections visible,
or as separate occurrences to the right of each respective artifact in
separate-occurrence mode. Additional basis for STV_SHR_012.

Project owner clarification, 2026-10-18: agreed that invalid or incomplete
input models fail the build with a clear error identifying the model entry
and problem instead of silently guessing placement. Basis for STV_SHR_036.

Project owner clarification, 2026-10-18: agreed that the replaceable input
model may define additional ordered artifact levels, using the discussed
hierarchy as the default. Basis for STV_SHR_037.

Project owner clarification, 2026-10-18: confirmed that the initial release
must support multiple views on one RST page with different starting IDs and
independent expansion and display-mode state. Basis for STV_SHR_038.

Project owner clarification, 2026-10-18: confirmed zoom and pan as required
for the initial release. Basis for STV_SHR_039 and STV_SHR_040.

Project owner clarification, 2026-10-18: selected Firefox only as the initial
browser support scope. Basis for STV_SHR_041.

Project owner clarification, 2026-10-18: selected Windows only as the initial
supported operating system. Additional basis for STV_SHR_041.

Project owner clarification, 2026-10-18: confirmed Python 3.10+, Sphinx 8.1.3
and Sphinx-Needs 8.2.0 as the initial compatibility baseline, with broader
Sphinx/Sphinx-Needs version support deferred. Basis for STV_SHR_042.

Project owner clarification, 2026-10-18: projects can contain tens of thousands
of Needs, but each view may be limited to 200 because larger views become
difficult to navigate. Basis for STV_SHR_043.

Project owner clarification, 2026-10-18: agreed that an expansion exceeding
200 visible nodes leaves the view unchanged and explains that another branch
must be collapsed, without showing only a partial set of targets.
Basis for STV_SHR_044.

Project owner clarification, 2026-10-18: confirmed that every visible node
occurrence, including duplicates and missing-target placeholders, counts toward
the 200-node limit. Additional basis for STV_SHR_043.

Project owner clarification, 2026-10-18: agreed to rejecting mode switches
that exceed the node limit without changing the view. Requested focusing on
high-level requirements now and refining details after an MVP is available.
Additional basis for STV_SHR_044 and the MVP discovery checkpoint.

Project owner MVP and integration decisions, 2026-10-18: agreed to start
with shared-node mode and defer the alternative mode, reuse host Sphinx-Needs
definitions with additional mappings, and deliver a reusable installable Sphinx
extension. Basis for release allocation and STV_SHR_045 and STV_SHR_046.

Stakeholder baseline v1 acceptance
----------------------------------

Decision owner: project owner (the user in this project conversation).
Decision date: 2026-10-18.
Scope: stakeholder requirements STV_SHR_001 through STV_SHR_046, including
the documented MVP and deferred release allocations.
Approval evidence: explicit instruction in this conversation, "let this be our
baseline of stkh requirements. set them to accepted".
This approval establishes requirement acceptance, not verification or downstream
traceability coverage. Verification states remain not_assessed.
