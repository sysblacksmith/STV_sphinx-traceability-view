Concept review - round 1
=========================

.. _STV_CONCEPT_REVIEW_001:


Review authority and baseline
---------------------------------

Date: 2026-10-18. Reviewer: the assistant, acting under the project owner's
explicit invocation of concept-review in this conversation. Delegation evidence:
:doc:`../sources`, Concept review delegation and round 1. This authorizes acceptance
of substantively reviewed clean concept artifacts, not runtime verification.

Input: stakeholder baseline v1 plus the explicitly recorded external, hidden
and static-widget amendments; repository HEAD
``b8e82423dac908d707d52cb9f76279b8816251dd`` plus the pre-existing modified
worktree. At entry, modifications existed in ADR 004, both element registers,
implementation-plan, internal-interfaces, review, software, sources, stakeholder,
system, technology-stack and verification-plan. These were reviewed rather
than discarded. The shared live method and concept-review checklist governed
this round; its SHA-256 is recorded below.

Scope: the complete current concept, including all stakeholder-to-internal
paths and the accepted later-scope requirement intent. Implementation-grade
occurrence-mode design, runtime verification and the explicitly deferred project
license/performance budgets are not claimed complete. There are no historical
rejected/superseded ADRs to reclassify.

Review outcome
------------------

Partial acceptance: **8 system requirements, 42 software requirements, six
software elements and ADRs 001/003** are accepted under delegation. Two system
requirements, eight software requirements and five elements remain reviewed
with acceptance held for STV_REVIEW_007. ADRs 002/004 remain proposed.
The 46 stakeholder requirements retain their existing owner acceptance and
amendment evidence. All verification states remain not_assessed.

The two system elements and all nine software elements were already flagged
accepted in the input worktree without a referenced concept review. Their
original flags are recorded here as history. Round 1 supplies current evidence
for the six clean software elements; the five affected element revisions are
reviewed pending the open finding. This is not fabricated historical approval.

Findings and closure evidence
---------------------------------

.. _STV_REVIEW_001:

STV_REVIEW_001 - Hidden-object exceptions were inconsistent
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: semantic scope/traceability. Owner: delegated reviewer. State: resolved.
Affected: STV_SYS_001/004, STV_SWR_002/006/028/048 and detail extraction.
Evidence: seed resolution and full-graph obligations omitted the approved hidden
exception, and copying final Need fragments could retain generated links to
hidden targets. This conflicted with the owner's visibility decision and method
consistency rules. Impact: hidden identities or connections could be published.
Correction: made the exceptions explicit and allocated detail-reference filtering
to STV_SWE_DETAIL_BUILD as well as seed/graph components. Host-generated hidden
relationship references are excluded before detail serialization; this is not
arbitrary redaction of author-published prose. Closure: inspected the revised
requirements, extraction contract and hidden/part/count verification cases.
Runtime validation remains planned; the concept contradiction is corrected.

.. _STV_REVIEW_002:

STV_REVIEW_002 - Hover/keyboard detail activation lacked an obligation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: missing internal requirement. Owner: delegated reviewer. State: resolved.
Affected: STV_SHR_015/034, STV_SYS_006 and STV_SWR_015/033.
Evidence: capture and panel geometry were specified, but no SWR explicitly
required opening details on hover or keyboard activation. Impact: a structurally
covered design could omit the trigger. Correction: added STV_SWR_050 with
mixed system derivation and justified keyboard channeling, allocated to INSPECT
and RENDER. Closure: reviewed its criterion against the parent intent and added
an explicit verification case. Its acceptance is still held by finding 007.

.. _STV_REVIEW_003:

STV_REVIEW_003 - Review summaries and diagnostics were stale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: method/content consistency. Owner: delegated reviewer. State: resolved.
Affected: stakeholder review notes, STV_SYS_006/010, STV_SWR_028/041, model
interface and ADR index. Evidence: previously settled model/title/external-link
questions remained described as open; platform checks only had to run rather
than pass; a missing-label path was unspecified; ADR summary lacked per-record
state/scope/replacement metadata required by the method.
Correction: reconciled the recorded decisions, strengthened criteria to actual
pass outcomes, specified host-default labels followed by entry-specific errors
when still missing, and added the ADR metadata summary. No unapproved owner
preference was inferred. Closure: re-read affected text, references and criteria;
Sphinx and graph checks validate their mechanical consistency.

.. _STV_REVIEW_004:

STV_REVIEW_004 - Software picture omitted documented interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: architecture consistency. Owner: delegated reviewer. State: resolved.
Affected: software Draw.io/SVG and component contracts. Evidence: the picture
omitted model-to-graph input, graph-to-detail locations and reader commands back
to state. Correction: added those three interfaces to the Draw.io source and
re-exported through Draw.io using the shared linked scripts. Closure: inspected
all nine element boxes and interface edges and validated their published Need
anchors. No new unmodeled product component was introduced.

.. _STV_REVIEW_005:

STV_REVIEW_005 - Final detail identity and caching order were incomplete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: lifecycle/data contract. Owner: delegated reviewer. State: resolved.
Affected: bundle/detail/view contracts, ADR 002 and implementation/verification
plans. Evidence: filenames hashed only the Need ID, and pages were written
before final rendered detail hashes were available. Impact: changed content
could reuse stale browser assets, or a page could name an unknown final manifest.
Correction: content-hash detail files, then create the manifest identity from its
canonical payload, emit the graph, and finalize only STV-owned tagged script/root
attributes in output pages. Cache keys include build identity and expected
fragment digest. Current manifests exclude deleted/hidden IDs; publishing a
clean tree and the inability to revoke old distributed bundles are explicit.
Closure: traced the two-phase dataflow and added cached two-build/failure checks.
This is a reviewed design policy, not a claim that its runtime is implemented.

.. _STV_REVIEW_006:

STV_REVIEW_006 - Acceptance flags lacked review scope/evidence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: method/acceptance evidence. Owner: delegated reviewer. State: resolved.
Affected: both element registers and the concept inventory.
Evidence: the input had 11 accepted element flags without a concept-review
record while internal requirements/ADRs still lacked review evidence. Correction:
recorded the actual owner delegation, input state and current per-artifact
outcomes; appended review evidence without changing inferred design basis to
observed implementation. Closure: individual acceptance eligibility was checked;
blocked revisions are reviewed, not presented as fully accepted. No verification
state was promoted.

.. _STV_REVIEW_007:

STV_REVIEW_007 - Remote embedded resources conflict with offline details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: owner scope decision. Owner: project owner. State: resolved in
round 2. The following original round-1 evidence records why it was open and
blocked acceptance of the affected offline/detail path.
Affected: STV_SHR_015/017, STV_SYS_003/006, STV_SWR_015/016/017/018/033/047/049/050,
STV_SE_BUILD/BROWSER, STV_SWE_DETAIL_BUILD/BUNDLE/INSPECT, ADRs 002/004 and
architecture/interface/implementation/verification documents containing that path.
Evidence: implementation-plan says to preserve HTTP/HTTPS resource URLs while
requiring offline details and no runtime network dependency. A remote image,
iframe or CSS resource can trigger an automatic network request when the copied
fragment is inserted. The agreed external-object/page fallback does not yet
specify remote embedded media inside an otherwise local Need.
Impact: either offline operation or full rendered-media parity may be weakened.
Recommendation: preserve local bundled media; replace unavailable external
embedded media with a clear unavailable-offline indication and an explicit link,
with no automatic fetch. An alternative is requiring the host build to provide
local cached copies of all such resources.
Closure criterion: owner selects the policy; update requirement scope, resource
rewriting and fixtures; re-review the affected neighborhood and accept only then.
At round 1 the recommendation was not agreed and did not amend the accepted
stakeholder obligation. Round-2 closure: the owner explicitly confirmed the
recommendation. Updated SHR 015 scope evidence, SWR 015, SYS 006, both resource
contracts, ADRs 002/004 and verification fixtures. Re-read the affected offline
and inspection paths: local media remains local; uncached remote media becomes
a static unavailable-offline indication and explicit resource link. Neither
opening details nor extraction downloads remote media. Remote CSS imports and
url() resources, SVG, srcset and active embedded documents are covered. The
question and documentation correction are both complete; runtime verification
is still planned.

.. _STV_REVIEW_008:

STV_REVIEW_008 - Transitive notice list omitted BSD-3-Clause
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: dependency/packaging completeness. Owner: delegated reviewer.
State: resolved. Affected: technology-stack and dependency lock review.
Evidence: locked d3-ease 3.0.1 declares BSD-3-Clause, but the notice instructions
named only MIT/ISC transitive components. Correction: include BSD-3-Clause in
notice requirements and review all locked package metadata. Closure: direct
manifest/lock equality and installed-version entries checked; 40 locked package
entries include optional platform binaries. Project license selection remains
owner-deferred; this finding does not assign a project license.

Semantic coverage and allocation review
-------------------------------------------

All authored SYS/SWR parent links, allocations and software containment were
read against their endpoint content. Broad system parents aggregate several
obligations; the primary refinements below identify each specific contribution
rather than treating a nonempty backlink as sufficient evidence. Supporting
state/render components cooperate through the documented interfaces. This is
concept coverage, not proof of implementation satisfaction.

Direct channeled obligations address software-local state, presentation or
interaction and retain their individual no-system-impact rationale. Mixed-parent
SWR 050 ties full inspection to SYS 006 and keyboard details to SHR 034; its
software allocations remain inside the system parent's browser boundary.
SWR 048 allocations cover build-side seed, graph and copied-reference filtering.
All other SWR allocations match their named component responsibility; all nine
software elements belong to the system element in which their allocated behavior
executes. No requirement was linked merely to satisfy the graph validator.

.. list-table:: Primary contribution for every stakeholder requirement
   :header-rows: 1
   :widths: 18 25 57

   * - Stakeholder
     - Internal refinement
     - Semantic review
   * - STV_SHR_001
     - SYS 001 / SWR 001
     - RST invocation and source-located instance creation.
   * - STV_SHR_002
     - SYS 001 / SWR 002, 048
     - Cross-page seeds of any configured visible type; hidden exception retained.
   * - STV_SHR_003
     - SWR 003
     - One seed and empty expansion keys initially.
   * - STV_SHR_004
     - SWR 004
     - Nonempty directional plus controls.
   * - STV_SHR_005
     - SWR 005
     - Complete target-group expansion subject to atomic cap.
   * - STV_SHR_006
     - SYS 004 / SWR 006
     - Indexed traversal without arbitrary depth cutoff; controls/state provide continuation.
   * - STV_SHR_007
     - SWR 007, 025
     - Collapse removes the group and recomputes rooted visibility.
   * - STV_SHR_008
     - SWR 008
     - Complete ID plus two-line title, no field configuration.
   * - STV_SHR_009
     - SYS 005 / SWR 009
     - Default stakeholder/system/software semantic ranks.
   * - STV_SHR_010
     - SYS 005 / SWR 010
     - Default system architecture rank between system and software.
   * - STV_SHR_011
     - SYS 005 / SWR 011
     - Software architecture below software requirements.
   * - STV_SHR_012
     - SYS 005 / SWR 012
     - Shared tests right of all associated artifacts; later copies scoped separately.
   * - STV_SHR_013
     - SYS 004 / SWR 013
     - Canonical outgoing links produce incoming adjacency without authored duplicates.
   * - STV_SHR_014
     - SYS 002 / SWR 014
     - Host schema plus replaceable supplemental mappings.
   * - STV_SHR_015
     - SYS 006 / SWR 015, 047, 049, 050
     - Capture plus hover/keyboard opening and agreed external/widget scope; media policy held for 007.
   * - STV_SHR_016
     - SYS 006 / SWR 016
     - Original URI/new-tab action preserves source state; held with inspection path.
   * - STV_SHR_017
     - SYS 003 / SWR 017
     - Local classic scripts and assets; remote embedded-media policy held for 007.
   * - STV_SHR_018
     - SYS 003 / SWR 018
     - Relative file/static-host URLs; held with incomplete resource policy.
   * - STV_SHR_019
     - SWR 019
     - Later in-view occurrence selector, specification accepted without MVP implementation claim.
   * - STV_SHR_020
     - SWR 020
     - Single identity per object in default shared mode.
   * - STV_SHR_021
     - SWR 021
     - Later round-trip preservation; later shared-edit policy remains out of MVP scope.
   * - STV_SHR_022
     - SWR 022
     - Later expansion state keyed independently by occurrence.
   * - STV_SHR_023
     - SWR 023
     - Later shared union retains independent round-trip state intent.
   * - STV_SHR_024
     - SWR 024
     - Closing edges/terminal references prevent infinite cycle unfolding.
   * - STV_SHR_025
     - SWR 025
     - Root reachability retains shared paths and removes disconnected cycles.
   * - STV_SHR_026
     - SYS 001 / SWR 026
     - Missing/unknown seed errors include invocation source.
   * - STV_SHR_027
     - SYS 004 / SWR 027
     - Host owns broken-trace failure; valid graph remains renderable.
   * - STV_SHR_028
     - SYS 004 / SWR 028
     - Missing ID/text/connection, no false original link; hidden targets excluded.
   * - STV_SHR_029
     - SWR 029
     - No controls for empty groups; isolated-object indication.
   * - STV_SHR_030
     - SWR 030
     - Host colors and consistent built-in fallback palette.
   * - STV_SHR_031
     - SWR 031
     - Red border outside accepted set, including empty/missing status.
   * - STV_SHR_032
     - SWR 032
     - Accepted-status override with accepted default.
   * - STV_SHR_033
     - SYS 006 / SWR 033
     - Viewport bounds, pointer retention and scrolling; held with detail path.
   * - STV_SHR_034
     - SWR 034, 050
     - Keyboard controls, focus and detail activation/dismissal; media-specific component held.
   * - STV_SHR_035
     - SWR 035
     - Separate independently keyed controls with host directional labels.
   * - STV_SHR_036
     - SYS 002 / SWR 036
     - Entry-specific validation failure with agreed optional defaults.
   * - STV_SHR_037
     - SYS 005 / SWR 037
     - Authoritative ordered model levels, not graph-depth ranks.
   * - STV_SHR_038
     - SYS 007 / SWR 038
     - Independent state/viewport per view; later selectors conditional.
   * - STV_SHR_039
     - SWR 039
     - Pointer/keyboard zoom changes transform, not graph state.
   * - STV_SHR_040
     - SWR 040
     - Pointer/keyboard pan reaches off-screen graph content.
   * - STV_SHR_041
     - SYS 010 / SWR 041
     - Actual passing workflow results on recorded stable Firefox/Windows.
   * - STV_SHR_042
     - SYS 009 / SWR 042
     - Clean wheel on pinned host and minimum Python 3.10 check.
   * - STV_SHR_043
     - SYS 008 / SWR 043
     - 200 visible occurrences including placeholders; benchmark budgets deliberately later.
   * - STV_SHR_044
     - SYS 008 / SWR 044
     - Atomic rejected transition with explanation and unchanged state.
   * - STV_SHR_045
     - SYS 002 / SWR 045
     - Reuse host types/colors/labels without a duplicate registry.
   * - STV_SHR_046
     - SYS 009 / SWR 046
     - Installable package setup/assets for an independent host.

Checks and remaining conditions
-----------------------------------

Round 1 checks include warnings-as-errors Sphinx, shared graph validation with
repository-relative evidence and CSV output, published Draw.io/SVG Need links,
manifest/lock equality and dependency metadata, installed host API/lifecycle
source inspection, and actual semantic reading of the inventory above. Exact
result summary is recorded after the round's final build below. Primary host
reference inspected: `Sphinx event lifecycle
<https://www.sphinx-doc.org/en/master/extdev/event_callbacks.html>`_. Installed
Sphinx-Needs 8.2.0 registers write-started postprocessing before the proposed
priority 800 handler and lock release at build-finished priority 9999.

Original library smoke-check and extraction results remain dated historical
evidence in :doc:`../sources`; this review does not reclassify them as runtime tests.
No product code is implemented. Deferred license selection, measured budgets
and later occurrence-mode policy are recorded conditions, not hidden findings
or falsely passed checks. The open media decision prevents full concept acceptance.

Artifact inventory and content identities
---------------------------------------------

Each row records the reviewed source content at the end of round 1. SHA-256
identifies the historical reviewed revision; acceptance scope is limited as stated.
The review record itself is identified by STV_CONCEPT_REVIEW_001/round 1 and
retains its issue history rather than attempting a self-referential file hash.
The live method is a governing input, not a newly accepted project document.

Governing method SHA-256: ``2c62de645f8161149dcdfa777cbd83f03483629c9dc042dcc304dcbded313794``.

.. list-table:: Source inventory - round 1
   :header-rows: 1
   :widths: 38 27 35

   * - Artifact
     - Review outcome
     - SHA-256
   * - ``README.rst``
     - Accepted concept artifact; no runtime claim
     - ``688227c854bdd5bbce4a785dc0231cf8a03fe28bb615545e66b70cfcc273c73b``
   * - ``requirements-docs.txt``
     - Accepted concept artifact; no runtime claim
     - ``116d09fd3a50ab57b76508581f7a1740a18ced344da5963d5714fa34d3f7ab8c``
   * - ``build-docs.ps1``
     - Accepted concept artifact; no runtime claim
     - ``aa9e520335f627c96c9b5500806096ea773b2526e713a5f3c2ff25cb5c97b740``
   * - ``docs/conf.py``
     - Accepted concept artifact; no runtime claim
     - ``9cca316d52abcc7ce0de9a2eeda6d35db4bd7ed2f0be557d252f29e3392f0e50``
   * - ``docs/architecture-decisions.rst``
     - Accepted concept artifact; no runtime claim
     - ``88990382b262a2bbfd4a220878a799d6c6dd76fed2f4dc7a383bd3f9c6864edf``
   * - ``docs/architecture-software.rst``
     - Held for STV_REVIEW_007
     - ``3a94e02fb2dd6de711ac5c938d4e5f66ccaca6414a00a3c811d48123d12be404``
   * - ``docs/architecture-system.rst``
     - Held for STV_REVIEW_007
     - ``f6364d4619d31ca648d26ea78406c1cc13c688b28d6fed638dd661bcf9facb7c``
   * - ``docs/elements-software.rst``
     - Per-record accepted/reviewed; see outcome
     - ``1eeaecafa3af121383eb3ded3b387d828951dfb4a6fff615ac08d2f78a806ef4``
   * - ``docs/elements-system.rst``
     - Per-record accepted/reviewed; see outcome
     - ``1b4bb4fbdf20606065165c69ad9a99082fbb41e30d2a09a04ff5e94a462c438f``
   * - ``docs/implementation-plan.rst``
     - Held for STV_REVIEW_007
     - ``fc3fc80b1742e8e0578734815dc0376edb6ac3695b3623f21b89bb07f549db5d``
   * - ``docs/index.rst``
     - Accepted concept artifact; no runtime claim
     - ``d968b60bbbc8ec17442676eff9c521b4b17835a5f1d1ce40de1a1750e778894a``
   * - ``docs/internal-interfaces.rst``
     - Held for STV_REVIEW_007
     - ``8eeb8c6c73ad2f2a37ef68cebbf9daff684d825c12ed01776d3640a0ad9def32``
   * - ``docs/method.rst``
     - Shared governing/tool input, inspected
     - ``2c99227c99556525ce0d18ebc62653ab314a0151177130ca9a16a67179a913c0``
   * - ``docs/review.rst``
     - Current review/evidence register
     - ``bf4ba3afc98ce9c1090d8c26c4b2def49c4bf649d09bd0524f875eb65ecde467``
   * - ``docs/software.rst``
     - Per-record accepted/reviewed; see outcome
     - ``c857d866e7b2f75f196e3ae3352e50a16c1552ab98b90ff8df78a4af07615285``
   * - ``docs/sources.rst``
     - Current review/evidence register
     - ``cdff5aad6406457eac093452fe334550ee7b55cb37f59c40e7ec2938f4507488``
   * - ``docs/stakeholder.rst``
     - Owner-accepted baseline, reviewed as input
     - ``6b239356cb547ace9f3292d04eb6ebe195e301ed16edfeb181c216080dd34ea3``
   * - ``docs/system.rst``
     - Per-record accepted/reviewed; see outcome
     - ``acfe9d3947391d49d844a6dba634140dcae13e92636f5fd8e8c7b9289584518a``
   * - ``docs/technology-stack.rst``
     - Accepted concept artifact; no runtime claim
     - ``bd2750ce57a6297f4feae01b103ca07ca9c037ebf340f907c861344b0f5ef106``
   * - ``docs/traceability.rst``
     - Accepted concept artifact; no runtime claim
     - ``316d28c29bc4195040eae3af2e91c2412eeba9c34a02da4640a8cef71b28d995``
   * - ``docs/verification-plan.rst``
     - Held for STV_REVIEW_007
     - ``be1f43b28d950c6863888d82a0c2b7cfd9a1640830515c88d8bd9756188d6c63``
   * - ``docs/architecture/decisions/STV_ADR_001_static_extension.rst``
     - Accepted concept artifact; no runtime claim
     - ``dddf0a766caabc294d423e560a15f508bd904679068a1b1cb4511373028e9e73``
   * - ``docs/architecture/decisions/STV_ADR_002_portable_bundle.rst``
     - Held for STV_REVIEW_007
     - ``3da695cbb358d8a64b23d05b0b245151bb06400b8c82c13be3273fd932a608b1``
   * - ``docs/architecture/decisions/STV_ADR_003_state_layout.rst``
     - Accepted concept artifact; no runtime claim
     - ``45fe0d933b22c1e122b15001f895fde75450bc6134b25a0ee40765017fef96ed``
   * - ``docs/architecture/decisions/STV_ADR_004_dependencies.rst``
     - Held for STV_REVIEW_007
     - ``2bb498b18104f474849c46106af31d1c16d4e8c4495031f2f56de2d5616c5766``
   * - ``docs/architecture/diagrams/software-architecture.drawio``
     - Accepted concept artifact; no runtime claim
     - ``1635f87e2649602140f89885a810b17d8690c34010d24340647a09830ab8ee4b``
   * - ``docs/architecture/diagrams/software-architecture.svg``
     - Accepted concept artifact; no runtime claim
     - ``7f2cb1ccc42d5288574d6b1b3ddde0a03b23d30203d128c1bd4b6211591dd01a``
   * - ``docs/architecture/diagrams/system-architecture.drawio``
     - Accepted concept artifact; no runtime claim
     - ``b789f7bb8920f2099d8092eef20b030d506b2b965ad4f58e5027f32ccc8a1e00``
   * - ``docs/architecture/diagrams/system-architecture.svg``
     - Accepted concept artifact; no runtime claim
     - ``f3793b017dab7c8fe43b1205beb86452e91f0617b98e65859a4bf889fbfed8c9``
   * - ``docs/architecture/implementation/check-stack.mjs``
     - Accepted concept artifact; no runtime claim
     - ``97c0f0582660d50ac36efb796098d04e791bb5446049acdac676b9e12f915065``
   * - ``docs/architecture/implementation/package-lock.json``
     - Accepted concept artifact; no runtime claim
     - ``f96e2b0f5c29cee9f69563030caad259ebcafd4a650bd4196560f21bdeb051ba``
   * - ``docs/architecture/implementation/package.json``
     - Accepted concept artifact; no runtime claim
     - ``a7c1aced6534eff63ee4b01475dce5dfdac4d6449fc0d5f8777754ef2daeee60``
   * - ``docs/architecture/implementation/requirements-implementation.txt``
     - Accepted concept artifact; no runtime claim
     - ``e773332c782d0741e1aa07517e85a77cd365be32ff53b851e8baa50e280e6e7e``
   * - ``scripts/export-architecture.ps1``
     - Shared governing/tool input, inspected
     - ``70a249f5423e481f3597d2e288c394b2b45522dc495f40987375a13b2cf788c4``
   * - ``scripts/normalize-diagram-links.py``
     - Shared governing/tool input, inspected
     - ``3a42cc6444f1072e3532012a3daca8a3d5980fd44ebb46a307f42b1875dbf9a8``

Round 1 mechanical results: Sphinx warnings-as-errors passed; graph/evidence
validation passed (46 SHR, 10 SYS, 50 SWR, two system and nine software elements);
CSV export passed; 11 diagram Need links passed; source whitespace check passed.
Status audit confirms 46 existing accepted stakeholders, 56 accepted internal
Need records and 15 reviewed internal records. ADRs 001/003 are accepted;
002/004 remain proposed. No verification_state changed from not_assessed.

The architecture diagrams are accepted for the responsibilities and connections
they depict; they do not select the unresolved remote-resource policy. Likewise,
the technology stack is accepted as a dependency/packaging selection, not as
proof that every feature path has been accepted. Held parent/view documents
retain the explicit unresolved policy in their review scope.




Assessed Need objects
---------------------

Stakeholder:

:need:`STV_SHR_001`, :need:`STV_SHR_002`, :need:`STV_SHR_003`, :need:`STV_SHR_004`, :need:`STV_SHR_005`, :need:`STV_SHR_006`, :need:`STV_SHR_007`, :need:`STV_SHR_008`, :need:`STV_SHR_009`, :need:`STV_SHR_010`, :need:`STV_SHR_011`, :need:`STV_SHR_012`, :need:`STV_SHR_013`, :need:`STV_SHR_014`, :need:`STV_SHR_015`, :need:`STV_SHR_016`, :need:`STV_SHR_017`, :need:`STV_SHR_018`, :need:`STV_SHR_019`, :need:`STV_SHR_020`, :need:`STV_SHR_021`, :need:`STV_SHR_022`, :need:`STV_SHR_023`, :need:`STV_SHR_024`, :need:`STV_SHR_025`, :need:`STV_SHR_026`, :need:`STV_SHR_027`, :need:`STV_SHR_028`, :need:`STV_SHR_029`, :need:`STV_SHR_030`, :need:`STV_SHR_031`, :need:`STV_SHR_032`, :need:`STV_SHR_033`, :need:`STV_SHR_034`, :need:`STV_SHR_035`, :need:`STV_SHR_036`, :need:`STV_SHR_037`, :need:`STV_SHR_038`, :need:`STV_SHR_039`, :need:`STV_SHR_040`, :need:`STV_SHR_041`, :need:`STV_SHR_042`, :need:`STV_SHR_043`, :need:`STV_SHR_044`, :need:`STV_SHR_045`, :need:`STV_SHR_046`.

System:

:need:`STV_SYS_001`, :need:`STV_SYS_002`, :need:`STV_SYS_003`, :need:`STV_SYS_004`, :need:`STV_SYS_005`, :need:`STV_SYS_006`, :need:`STV_SYS_007`, :need:`STV_SYS_008`, :need:`STV_SYS_009`, :need:`STV_SYS_010`.

Software:

:need:`STV_SWR_001`, :need:`STV_SWR_002`, :need:`STV_SWR_003`, :need:`STV_SWR_004`, :need:`STV_SWR_005`, :need:`STV_SWR_006`, :need:`STV_SWR_007`, :need:`STV_SWR_008`, :need:`STV_SWR_009`, :need:`STV_SWR_010`, :need:`STV_SWR_011`, :need:`STV_SWR_012`, :need:`STV_SWR_013`, :need:`STV_SWR_014`, :need:`STV_SWR_015`, :need:`STV_SWR_016`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_019`, :need:`STV_SWR_020`, :need:`STV_SWR_021`, :need:`STV_SWR_022`, :need:`STV_SWR_023`, :need:`STV_SWR_024`, :need:`STV_SWR_025`, :need:`STV_SWR_026`, :need:`STV_SWR_027`, :need:`STV_SWR_028`, :need:`STV_SWR_029`, :need:`STV_SWR_030`, :need:`STV_SWR_031`, :need:`STV_SWR_032`, :need:`STV_SWR_033`, :need:`STV_SWR_034`, :need:`STV_SWR_035`, :need:`STV_SWR_036`, :need:`STV_SWR_037`, :need:`STV_SWR_038`, :need:`STV_SWR_039`, :need:`STV_SWR_040`, :need:`STV_SWR_041`, :need:`STV_SWR_042`, :need:`STV_SWR_043`, :need:`STV_SWR_044`, :need:`STV_SWR_045`, :need:`STV_SWR_046`, :need:`STV_SWR_047`, :need:`STV_SWR_048`, :need:`STV_SWR_049`, :need:`STV_SWR_050`.

Elements System:

:need:`STV_SE_BUILD`, :need:`STV_SE_BROWSER`.

Elements Software:

:need:`STV_SWE_DIRECTIVE`, :need:`STV_SWE_MODEL`, :need:`STV_SWE_GRAPH`, :need:`STV_SWE_DETAIL_BUILD`, :need:`STV_SWE_BUNDLE`, :need:`STV_SWE_STATE`, :need:`STV_SWE_LAYOUT`, :need:`STV_SWE_RENDER`, :need:`STV_SWE_INSPECT`.

