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

Internal specification source baseline
--------------------------------------

The owner requested internal system/software specification and architecture
for sphinx-traceability-view on 2026-10-18. Input: accepted stakeholder baseline
v1 (STV_SHR_001 through STV_SHR_046), the shared method including channeling,
and documentation at repository revision 322084f. No product implementation
exists at this design point. Newly authored design documents are uncommitted
work relative to that revision; source mappings in element records are proposed.

Technical feasibility references inspected: installed Sphinx-Needs 8.2.0
``data.py`` exposes ``SphinxNeedsData.get_needs_view``; use is isolated in the
adapter and requires a pinned-toolchain integration test. Official references:

* `Sphinx extension application API <https://www.sphinx-doc.org/en/master/extdev/appapi.html>`_
* `Sphinx-Needs 8.2.0 Python API <https://sphinx-needs.readthedocs.io/en/8.2.0/api.html>`_

The live central method is rendered in :doc:`method`. Internal requirements
are inferred engineering refinements, and ADRs are proposals; no owner approval
or successful runtime verification is implied by their existence.

Concrete technology selection and design checks
-----------------------------------------------

Owner request, 2026-10-18: complete the technology choices and produce an
implementation-ready concept. Basis for STV_ADR_004, technology-stack,
implementation-plan and verification-plan. No acceptance of those proposals
or product implementation is implied.

Verified exact npm/PyPI package metadata on 2026-10-18 for ELK.js 0.10.0,
D3 zoom/selection 3.0.0, Floating UI DOM 1.7.4, esbuild 0.25.12,
Beautiful Soup 4.13.5, Hatchling 1.27.0, build 1.3.0, pytest 8.4.2 and
Selenium 4.35.0. Direct source references and rationale are in
:doc:`technology-stack`; the npm lock records transitive versions/integrities.

Temporary Node 24.21.0/npm 11.19.0 check: exact npm install completed;
ELK cyclic A-B-C-A fixture produced finite coordinates; esbuild IIFE had
150 bundled inputs, 1,508,230 minified bytes and no dynamic-import expression.
The reproducible source check is
``docs/architecture/implementation/check-stack.mjs``. The initial measurement
used an equivalent file-entry check; the committed check bundles from stdin
and additionally asserts that no unresolved output imports remain.

Temporary Python check: Beautiful Soup 4.13.5 with html.parser located all
113 exported Need objects in their original generated HTML across five pages,
retaining ID text and acceptance criteria for requirement types. This did not
exercise a product runtime or prove general media/anchor rewriting.

External Need detail scope confirmation, 2026-10-18: the project owner
confirmed available metadata, original-object link and a clear unavailable-local-
details indication as sufficient for the MVP when external bodies are not
locally rendered, without downloading/caching external pages. Explicit scope
clarification to STV_SHR_015; basis for STV_SWR_047 and related internal refinements.
Hidden Need visibility was not decided by this answer.

Hidden Need visibility confirmation, 2026-10-18: owner agreed that Needs
intentionally hidden by the host and their connections are excluded from STV,
and hidden starting IDs are rejected. Basis for STV_SWR_048 and explicit
scope clarification of STV_SHR_002. Hidden targets are not missing-target
placeholders; baseline v1 history remains recorded.

Third-party widget scope confirmation, 2026-10-18: owner confirmed that MVP
details preserve rendered text, images and markup while widget-specific
JavaScript behavior remains on the original Need page. Basis for STV_SWR_049
and an explicit clarification of STV_SHR_015; baseline v1 history is retained.

Project license decision, 2026-10-18: the owner requested deferring selection
until later. No project distribution license has been selected.

Performance budget decision, 2026-10-18: owner agreed to measure the first
MVP against the planned large-project fixture, then agree response-time and
memory budgets from those results. The hard 200-visible-node limit is unchanged.

Concept review delegation and round 1
--------------------------------------

On 2026-10-18 the project owner explicitly invoked the concept-review skill
in this conversation ("please conduct the ... concept-review"). This invokes
its review-and-accept workflow for the current STV concept. The assistant
acts as delegated reviewer; this is not a claim of separate line-by-line owner
review. Scope, findings, per-artifact outcomes and acceptance evidence are
recorded in :doc:`concept-review`. Requirements verification remains
not_assessed. No project license or remote-media exception was inferred.

The input included pre-existing accepted flags on both system elements and
all nine software elements without a referenced concept-review record. Round 1
preserves that fact as history, supplies current review evidence for clean
records and marks affected records reviewed where acceptance is held for 007.

Round 1 validation results, 2026-10-18: Sphinx 8.1.3 build with
-E -a -W --keep-going succeeded. Shared graph/evidence validation succeeded
for 46 stakeholder, 10 system, 50 software requirements and 11 architecture
elements; CSV paths exported. All 11 published diagram-to-Need links validated.
Manifest/lock direct pins agree; all verification states remain not_assessed.
The missing hover/keyboard trigger obligation is now STV_SWR_050. Seven findings
were corrected and re-reviewed; STV_REVIEW_007 awaits owner input. No runtime
implementation acceptance or performance result is claimed.


Concept review round 2 - remote media and diagram readability
--------------------------------------------------------------

2026-10-18: The project owner confirmed the recommended unavailable-offline
indication and explicit-link fallback for uncached remote embedded media as
sufficient, then identified overlapping/crossing architecture arrows missed
by round 1. The owner requested correction of both pictures and preventive
guidance in concept-creation and concept-review. This explicitly amends the
inspection scope of STV_SHR_015, preserving baseline v1 history. Round 2
continues the previously recorded owner-delegated concept acceptance scope;
it does not assert runtime verification. See :doc:`concept-review`.

v0.2.0 stakeholder release and delegated review
-----------------------------------------------

2026-10-18: The owner formally released the new and changed stakeholder
requirements and requested concept-review of the internal specification/design,
delegated release to final implementation, and complete concept-implementation
validation for v0.2.0. This accepts the exact current revisions of
:need:`STV_SHR_015`, :need:`STV_SHR_049`, :need:`STV_SHR_050` and
:need:`STV_SHR_051`, including the five usability fixes. The owner authorized
independent repository edits and requested a proposed commit message and release
description at completion. Commit, tagging, pushing and publication are not
requested. Existing later-release deferrals remain unchanged. Review decisions
and implementation results are linked from :doc:`maturity`.

Centered-layout and interactive-seed MVP clarification
------------------------------------------------------

2026-10-18: After the retained failed v0.2.0 release execution, the owner
requested parent centering over visible child spans with collision avoidance,
an initially open project overview of five stakeholders per page, and a local
ID/title picker in every view. Exact confirmation replaces only its view;
invalid input preserves exploration and Project overview returns to its initial
page. The owner authorized provisional concept review and MVP implementation
for inspection. This is confirmation of intent and draft prototype authority,
not formal acceptance of the newly written requirements or release approval.
See :doc:`change-requests/STV_CR_006_centered-layout-and-interactive-seeds`.

Centered-layout amendment approval and concept acceptance delegation
------------------------------------------------------------------------------------------

2026-10-18: After inspecting the new MVP, the project owner stated:
"i love it. please proceed to make the requirements accepted by finishing the
concept review. i release the stakeholder requirements to you."
This explicitly releases the current revisions of STV_SHR_003/047/052/053
and delegates acceptance of the clean affected internal concept. The scoped
review, requirement/ADR decisions and artifact identities are recorded in
:doc:`concept-reviews/round-6`. It does not establish full implementation
verification or authorize committing, tagging or publication.

PR013 owner and design evidence
-------------------------------

2026-10-24: owner confirmation of stable-navigation PoC, corrected Firefox arrows
and numeric initial IDs, followed by explicit concept-creation/review/implementation
instruction. See :need:`STV_PR_013`, :doc:`concept-reviews/round-9` and retained
:doc:`test-execution/pr013-poc/index`. This revises fresh-versus-incremental
centering intent; no external dependency/version assertion is introduced.

CR_013 input and fallback decision
-----------------------------------

Owner-authored CR_013 RST/SVG and adjacent backup PPTX, 2026-10-24; explicit
instruction to create/review/implement the concept and subsequent choice to keep
unclassified evidence in a fallback row. See :ref:`STV_CR_013` and
:doc:`concept-reviews/round-10`. The input is not prior runtime verification.

PR014 owner evidence
----------------------

Owner-provided normalized RST and annotated PNG, 2026-10-24, requesting a thin
grey marker at the existing graph clipping boundary, followed by explicit
analysis/plan/full-V-cycle implementation instruction. The intake names an
originating PPTX; only its exported evidence was supplied here. See
:need:`STV_PR_014` and :doc:`concept-reviews/round-11`.

CR014 owner decisions
------------------------

2026-10-24: owner-authored CR014, explicit complete-V-cycle instruction, answers
choosing reuse without age refresh, independent stacks and retention across
seed/overview/page changes, followed by the configurable-capacity request. See
:ref:`STV_CR_014` and :doc:`concept-reviews/round-12`. No runtime result is inferred.


PR015 owner acceptance findings, 2026-10-24
--------------------------------------------

Conversation evidence: the owner requested twice the detail-view width,
initially folded status/tags and other secondary attributes, a working fold arrow
and correct original-artifact navigation from the Need ID. The owner noted that
other links work. :need:`STV_PR_015` is the corrected-language normalized intake;
:doc:`concept-reviews/round-13` owns scoped refinement/review.

v1.0.0 release instruction, 2026-10-24
----------------------------------------

Owner conversation: "ok, i give my go for number 1 and 2. 3 and 4 remain for
later. right now i want to release v1.0.0 without setting the repo to public,
yet." Numbering refers to the preceding readiness assessment. See
:ref:`release-1-0-0-authority` and :doc:`concept-reviews/round-14`.

The owner clarified that the release must not be labelled private and may
become publicly visible later. Remaining security findings are accepted as
nonblocking deferred work for v1.0.0. No visibility change is requested now.

CR015-018 acceptance and Save As clarification, 2026-10-25
----------------------------------------------------------

Owner conversation (language-corrected): "I have reviewed the stakeholder
requirements and the CRs and accept their content. Please proceed with
concept-creation." This approves the four prepared CRs and STV_SHR_058-061, not
new internal requirements, ADRs, implementation or a release. The earlier request
and current-seed/visible-area/page-scope answers remain in the canonical CRs.

Owner clarification: use browser-managed Save As with documented settings,
including enabling a location prompt when automatic downloads otherwise select
a default folder. This resolves the open location-interface question in CR016.
The owner also requested working on main; the local branch was safely updated
to origin/main at 8dbbe79 and all uncommitted concept work was retained.
