Software requirements
=====================

Software behavior, interfaces and architecture allocation. See
:doc:`architecture-software` for component interfaces.

Executable criteria and retained results: :doc:`test-coverage` and
:doc:`test-execution/0.1.0-final/index`.

.. swr:: Register the RST entry point
   :id: STV_SWR_001
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_001
   :allocated_to: STV_SWE_DIRECTIVE

   The software shall register a traceability-view directive accepting an optional whitespace-separated list of starting Need IDs and emit a serializable placeholder with source filename, line and per-page instance ID.

   Repeated IDs shall normalize to their first occurrence. Commas are not list
   separators; an explicit unknown token remains an invalid ID.

   **Acceptance criterion:** Zero-, one- and multiple-ID fixtures produce
   distinct placeholders recording the supplied seed list or project-root mode
   and each invocation's source location.

.. swr:: Resolve seeds after collection
   :id: STV_SWR_002
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_001
   :allocated_to: STV_SWE_GRAPH

   The software shall resolve starting IDs only after all host documents have contributed Needs, for any configured type, excluding host-hidden objects and their parts.

   **Acceptance criterion:** A visible seed defined on a later-read document resolves for each fixture type; hidden seeds are rejected as specified in STV_SWR_048.

.. swr:: Initialize collapsed state
   :id: STV_SWR_003
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst; docs/requirement-changes/centered-layout-and-interactive-seeds.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_003
   :allocated_to: STV_SWE_STATE

   The software shall initialize each view with every distinct selected seed
   visible, or the project node and first five stakeholder entries when no
   seeds were supplied,
   and no expanded relationship keys.

   **Acceptance criterion:** One seed produces one node; multiple distinct
   seeds within the capacity limit produce their corresponding nodes; no
   seeds produces the project node and at most five stakeholder entries. Every
   case has an empty ordinary expansion set; project entries are the sole
   automatic expansion exception.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Expose plus controls
   :id: STV_SWR_004
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_004
   :allocated_to: STV_SWE_RENDER

   The software shall render a plus control for every nonempty relationship-type and direction group on each collapsed displayed node.

   **Acceptance criterion:** The fixture exposes one control per nonempty group and activating it dispatches its group key.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Expand complete target groups
   :id: STV_SWR_005
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_005
   :allocated_to: STV_SWE_STATE

   The software shall reveal all targets of the selected object, relationship type and direction as one state transition, subject to the node cap.

   **Acceptance criterion:** Expanding a group displays every target or rejects the entire transition at the cap.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Traverse without depth cutoff
   :id: STV_SWR_006
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_004
   :allocated_to: STV_SWE_GRAPH

   The software shall provide indexed outgoing and incoming adjacency for every non-hidden resolved object without imposing a traversal-depth cutoff.

   **Acceptance criterion:** A path crossing document boundaries can be followed beyond three hops from either end.

.. swr:: Collapse relationship groups
   :id: STV_SWR_007
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_007
   :allocated_to: STV_SWE_STATE

   The software shall remove the selected expansion key and recompute visible reachability from all selected seeds, or from the
   artificial project node in project-root mode.

   **Acceptance criterion:** A collapsed group can be reopened and does not remain as a visibility root.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Render fixed node summaries
   :id: STV_SWR_008
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_008
   :allocated_to: STV_SWE_RENDER

   The software shall show the complete ID and a title visually clamped to two lines while keeping the full ID visible without author field-selection settings.

   **Acceptance criterion:** Long-title nodes retain the complete ID and expose their full title in details; the two-line summary clamp is tested without making its field set configurable.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Order requirement ranks
   :id: STV_SWR_009
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall assign stakeholder, system and software requirements to increasing vertical ranks under the default mapping.

   **Acceptance criterion:** Their node bounding boxes remain vertically ordered after each expansion.

.. swr:: Insert system architecture rank
   :id: STV_SWR_010
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall place default system architecture nodes below system requirements and above software requirements.

   **Acceptance criterion:** A fixture with all three categories has nonoverlapping ordered rank bands.

.. swr:: Place software architecture rank
   :id: STV_SWR_011
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall place default software architecture nodes below software requirements.

   **Acceptance criterion:** Expanding architecture preserves the required rank order.

.. swr:: Place test nodes on the right
   :id: STV_SWR_012
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall place each revealed shared test node to the right of all visible artifacts connected to it by revealed test traces; later occurrence mode places each copy beside its source.

   **Acceptance criterion:** A test linked to two ranks appears once beyond both artifact right bounds in shared mode.

.. swr:: Index both trace directions
   :id: STV_SWR_013
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_004
   :allocated_to: STV_SWE_GRAPH

   The software shall construct incoming adjacency from canonical outgoing relations without requiring authors to duplicate inverse links.

   **Acceptance criterion:** A single authored relationship appears in both directional indexes with one canonical edge identity.

.. swr:: Normalize replacement mappings
   :id: STV_SWR_014
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_002
   :allocated_to: STV_SWE_MODEL

   The software shall normalize supplemental model mappings against host type and relationship definitions without hard-coded host type names in graph or layout algorithms, including
   an explicit stakeholder role on normally placed types for project-root selection.

   **Acceptance criterion:** Replacing types and mapping names changes the view
   without modifying extension code. A project-root invocation requires at least
   one type designated as stakeholder; no matching objects is a valid empty
   project, while a missing designation produces an entry-located model error.

.. swr:: Publish full rendered details
   :id: STV_SWR_015
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_006
   :allocated_to: STV_SWE_DETAIL_BUILD

   The software shall capture the final host-rendered Need representation for each locally rendered resolved object and make its displayed metadata and body available to details without a separate field whitelist.

   Uncached remote embedded media shall be replaced with an unavailable-offline
   indication and explicit original-resource link, without automatic retrieval.
   This includes resource-bearing HTML/SVG attributes and remote CSS imports
   or url() references. Local bundled media shall remain available.

   **Acceptance criterion:** A cross-page Need with custom metadata, formatted
   body and local images has equivalent information in details; hidden internal
   fields are not exposed. Remote media/CSS fixtures show the fallback and
   preserve the original URL without automatic network requests.

.. swr:: Open canonical object links
   :id: STV_SWR_016
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_006
   :allocated_to: STV_SWE_INSPECT

   The software shall activate a node through an anchor targeting a new tab at the original document and Need anchor while leaving the source view state unchanged.

   **Acceptance criterion:** Activation from file and HTTP output opens the correct cross-page object and preserves exploration.

.. swr:: Avoid runtime network loading
   :id: STV_SWR_017
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_003
   :allocated_to: STV_SWE_BUNDLE

   The software shall emit local classic-script data and runtime assets, with local detail fragments, so startup and exploration require no fetch, module import, CDN or backend request.

   **Acceptance criterion:** With network disabled, file-URL output supports expansion, details and local links with no missing runtime assets.

.. swr:: Use portable output URLs
   :id: STV_SWR_018
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_003
   :allocated_to: STV_SWE_BUNDLE

   The software shall generate graph, asset and documentation URLs relative to the containing output page so nested pages work on static hosts and from disk.

   **Acceptance criterion:** The same nested-page bundle works below a non-root HTTP prefix and through file URLs.

.. swr:: Offer occurrence mode later
   :id: STV_SWR_019
   :status: accepted
   :tags: release_later
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_019
   :allocated_to: STV_SWE_STATE

   The software shall provide a later-release in-view selector between shared identity nodes and path-specific occurrences without rebuilding.

   **Acceptance criterion:** A two-parent fixture changes between one shared node and two occurrences using the selector.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Use shared identity initially
   :id: STV_SWR_020
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_020
   :allocated_to: STV_SWE_STATE

   The software shall use one visible node per Need ID in the initial shared-node mode.

   **Acceptance criterion:** Opening two paths to the same Need produces one node with both revealed connections.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Retain state across later mode changes
   :id: STV_SWR_021
   :status: accepted
   :tags: release_later
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_021
   :allocated_to: STV_SWE_STATE

   The software shall retain separate-occurrence expansion states across later display-mode projections and restore them when switching back without intervening navigation.

   **Acceptance criterion:** A round trip between modes restores previously different expansion sets for two occurrences.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Key later expansions by occurrence
   :id: STV_SWR_022
   :status: accepted
   :tags: release_later
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_022
   :allocated_to: STV_SWE_STATE

   The software shall key separate-occurrence expansion state by path occurrence rather than Need ID so changing one copy does not change another.

   **Acceptance criterion:** Expanding one of two copies changes only that copy.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Project later shared expansion union
   :id: STV_SWR_023
   :status: accepted
   :tags: release_later
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_023
   :allocated_to: STV_SWE_STATE

   The software shall compute a shared node's expanded groups as the union of its occurrence groups when projecting separate occurrences to shared mode.

   **Acceptance criterion:** Two copies with disjoint expanded groups produce one shared node with both groups expanded.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Close repeated paths safely
   :id: STV_SWR_024
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_024
   :allocated_to: STV_SWE_STATE

   The software shall represent a return to an ancestor ID as a closing edge in shared mode or a terminal reference in later occurrence mode instead of recursively adding occurrences.

   **Acceptance criterion:** Self-links, reverse traversal and A-B-C-A terminate without repeated branch growth.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Compute seed-rooted visibility
   :id: STV_SWR_025
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_025
   :allocated_to: STV_SWE_STATE

   The software shall retain all starting nodes and all objects reachable
   from any starting node through currently expanded groups after collapse,
   including objects shared by remaining paths. In project-root mode the
   artificial project node is the starting node.

   **Acceptance criterion:** A diamond retains the shared target until the last path closes; a disconnected cycle is removed. A multi-seed fixture retains every
   seed and objects still reached from any other seed.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Report invalid invocation seeds
   :id: STV_SWR_026
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_001
   :allocated_to: STV_SWE_DIRECTIVE

   The software shall raise a source-located build error identifying any
   explicitly supplied ID unresolved after host collection, while treating
   an omitted seed list as project-root mode.

   **Acceptance criterion:** An unknown ID supplied alone or among valid IDs
   fails with that ID, invocation file and line. An invocation without IDs
   selects project-root mode without an invalid-seed error. Repeated IDs are
   deduplicated before initial capacity validation; more than 200 distinct
   explicit seeds fails with an invocation-located capacity error, without
   dropping or truncating supplied IDs.

.. swr:: Tolerate host broken traces
   :id: STV_SWR_027
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_004
   :allocated_to: STV_SWE_GRAPH

   The software shall retain resolvable graph entries when targets are missing and avoid raising an extension-specific missing-target failure.

   **Acceptance criterion:** A dangling target does not prevent generation of valid view data; host broken-link validation still controls build status.

.. swr:: Create missing-target nodes
   :id: STV_SWR_028
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_004
   :allocated_to: STV_SWE_RENDER

   The software shall display a missing-target node with its referenced ID, explicit missing-object text and source connection when its group is expanded.

   **Acceptance criterion:** Expanding a genuine missing-target group shows the target ID, missing-object text and source connection without relying on color. No valid original-object link is offered. Hidden targets do not become placeholders.

.. swr:: Indicate empty adjacency
   :id: STV_SWR_029
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_029
   :allocated_to: STV_SWE_RENDER

   The software shall omit controls for empty directional groups and show No related objects when both adjacency directions are empty.

   **Acceptance criterion:** An isolated node has the indication and no controls; a dangling target group still has a control.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Resolve type palette
   :id: STV_SWR_030
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_030
   :allocated_to: STV_SWE_MODEL

   The software shall use host type colors where present and a deterministic built-in type palette where absent.

   **Acceptance criterion:** Explicit colors survive mixed configured/unconfigured fixtures and omitted colors are consistent per type.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Apply acceptance borders
   :id: STV_SWR_031
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_031
   :allocated_to: STV_SWE_RENDER

   The software shall render a red border when status is missing, empty or outside the normalized accepted-status set, independently of type background.

   **Acceptance criterion:** Draft, reviewed and empty statuses are red; configured accepted statuses have no red status border.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Normalize accepted values
   :id: STV_SWR_032
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_032
   :allocated_to: STV_SWE_MODEL

   The software shall read accepted-status values from supplemental mappings and use the singleton accepted default when no override is supplied.

   **Acceptance criterion:** An approved override changes styling without requiring field-level tooltip settings.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Constrain and retain details overlays
   :id: STV_SWR_033
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_006
   :allocated_to: STV_SWE_INSPECT

   The software shall position details inside the viewport with overflow scrolling and retain them while the pointer moves from trigger to overlay or remains over either.

   **Acceptance criterion:** A long object at a viewport corner remains readable and scrollable without closing.

.. swr:: Provide keyboard interaction
   :id: STV_SWR_034
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_034
   :allocated_to: STV_SWE_RENDER

   The software shall expose focusable semantic controls for expansion, details, viewport movement and object links, with visible focus and a way to dismiss details without trapping focus.

   **Acceptance criterion:** The shared-mode workflow is completable without a pointer; later mode controls meet the same rule when delivered.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Label directional controls
   :id: STV_SWR_035
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_035
   :allocated_to: STV_SWE_RENDER

   The software shall use the host model's incoming and outgoing labels on separate controls carrying independent group identities.

   **Acceptance criterion:** An object with both directions of one relation can toggle each independently using distinguishable labels.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Reject invalid model entries
   :id: STV_SWR_036
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_002
   :allocated_to: STV_SWE_MODEL

   The software shall reject unknown types, unknown levels and missing required mappings with diagnostics identifying the relevant configuration entry.

   **Acceptance criterion:** Malformed fixtures fail before asset generation while omitted optional colors and acceptance values receive defaults.

.. swr:: Honor declared level ordering
   :id: STV_SWR_037
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall build rank order from the normalized ordered level list and map all host types to declared levels or the test role.

   **Acceptance criterion:** An added hardware level is placed at its declared index without code changes.

.. swr:: Scope state to view roots
   :id: STV_SWR_038
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_007
   :allocated_to: STV_SWE_STATE

   The software shall instantiate exploration, focus and viewport state separately for every directive root while sharing only immutable project data.

   **Acceptance criterion:** Two views remain independent after navigation and viewport commands; later selectors are independent too.

.. swr:: Implement view-local zoom
   :id: STV_SWR_039
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_039
   :allocated_to: STV_SWE_RENDER

   The software shall change the view-local graph transform for zoom commands without mutating expansion sets or layout rank ordering.

   **Acceptance criterion:** Pointer and keyboard zoom preserve state and do not change another view.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Implement view-local pan
   :id: STV_SWR_040
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_040
   :allocated_to: STV_SWE_RENDER

   The software shall translate the view-local graph viewport for pan commands without mutating graph topology.

   **Acceptance criterion:** All off-screen nodes can be brought into view by pointer or keyboard.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Verify Firefox on Windows
   :id: STV_SWR_041
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_010
   :allocated_to: STV_SWE_RENDER

   The software shall use browser interfaces exercised by the documented release checks on stable Firefox desktop for Windows in both file and HTTP contexts.

   **Acceptance criterion:** All in-scope interaction checks pass in both file and HTTP contexts; the release record states the exact stable Firefox and Windows versions and actual results.

.. swr:: Package for the pinned toolchain
   :id: STV_SWR_042
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_009
   :allocated_to: STV_SWE_DIRECTIVE

   The software shall ship a wheel containing the Python extension and required browser assets with metadata documenting the initial Python and Sphinx compatibility contract.

   **Acceptance criterion:** A clean Python 3.10 environment with pinned Sphinx dependencies installs the wheel and builds the fixture.

.. swr:: Enforce visible occurrence capacity
   :id: STV_SWR_043
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_008
   :allocated_to: STV_SWE_STATE, STV_SWE_DIRECTIVE

   The software shall count all candidate visible node occurrences, including placeholders, against a constant limit of 200 before committing initialization, project-page selection or a graph
   transition; the artificial project node counts as one occurrence.

   **Acceptance criterion:** Candidate sizes 199 and 200 pass, 201 fails;
   200 distinct explicit seeds initialize, 201 fail before publication; a tens-of-thousands graph fixture remains addressable through adjacency indexes.

   **Review note:** By owner decision on 2026-10-18, response-time and memory
   budgets will be agreed after first MVP benchmark measurements; the node cap
   is mandatory independently of those future budgets.

.. swr:: Reject over-limit transitions atomically
   :id: STV_SWR_044
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_008
   :allocated_to: STV_SWE_STATE

   The software shall reject an expansion or later mode switch exceeding the node cap without changing prior graph, mode or expansion state and announce the reason.

   **Acceptance criterion:** An over-limit expansion adds no partial targets and explains that branches must be collapsed first.

.. swr:: Reuse canonical host definitions
   :id: STV_SWR_045
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_002
   :allocated_to: STV_SWE_MODEL

   The software shall read type names, colors and relation labels from the resolved host configuration and require only supplemental layout and acceptance information.

   **Acceptance criterion:** Changing a host type label or relation label is reflected without duplicate definitions in extension configuration.

.. swr:: Expose an installable entry module
   :id: STV_SWR_046
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_009
   :allocated_to: STV_SWE_DIRECTIVE

   The software shall provide a package entry module with Sphinx setup registration and bundled assets so an external project can enable the extension by module name.

   **Acceptance criterion:** A separate project enables the installed module and renders a seeded view without repository imports.

.. swr:: Inspect external Needs without local full content
   :id: STV_SWR_047
   :status: accepted
   :tags: release_initial
   :basis: owner
   :evidence: docs/sources.rst :: external Need detail scope confirmation 2026-10-18
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_006
   :allocated_to: STV_SWE_DETAIL_BUILD, STV_SWE_INSPECT

   The software shall display available metadata, the original-object link and
   a "Full details unavailable locally" indication when inspecting an external
   Need without a locally rendered full body, without downloading or caching
   external pages.

   **Acceptance criterion:** With external networking disabled, an external Need
   without local full content has inspectable metadata and the indication. Its
   original link is available, but opening that external destination is not
   represented as an offline capability. No external page download is attempted.

.. swr:: Respect host-hidden Need objects
   :id: STV_SWR_048
   :status: accepted
   :tags: release_initial
   :basis: owner
   :evidence: docs/sources.rst :: hidden Need visibility confirmation 2026-10-18
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_001, STV_SYS_004
   :allocated_to: STV_SWE_DIRECTIVE, STV_SWE_GRAPH, STV_SWE_DETAIL_BUILD

   The software shall exclude host-hidden Needs and their incident relationships
   from the published view data and reject a hidden Need used as a starting ID
   with a source-located build error.

   **Acceptance criterion:** A visible Need tracing to a hidden Need exposes
   neither the hidden node nor that connection or a missing-target placeholder
   in the view or generated graph/detail data. A directive seeded with the hidden
   ID fails with its source filename and invocation location. Visible objects
   and their other relationships remain explorable.

   **Review note:** Filtering precedes serialization and adjacency generation;
   hiding a node only in the browser is insufficient. Hidden-object exclusion
   takes precedence over placeholder creation for genuinely unresolved targets.

   **Detail filtering:** Exclude host-generated relationship references to hidden
   targets from copied detail fragments as well as graph indexes and counts.
   Do not synthesize a placeholder revealing a filtered target. This is host
   visibility conformance, not redaction of prose already deliberately published
   by the author.

.. swr:: Preserve static third-party widget content in details
   :id: STV_SWR_049
   :status: accepted
   :tags: release_initial
   :basis: owner
   :evidence: docs/sources.rst :: third-party widget scope confirmation 2026-10-18
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_006
   :allocated_to: STV_SWE_DETAIL_BUILD, STV_SWE_INSPECT

   The software shall preserve the rendered text, images and non-executable
   markup of third-party widgets in object details without requiring their
   widget-specific JavaScript behavior in the MVP, while retaining access to
   the original Need page for the full interaction.

   **Acceptance criterion:** A fixture with a widget containing static rendered
   text and an image retains that content in details without executing copied
   widget scripts. The original-object link opens its documentation page.
   No interactive parity or generated snapshot of script-only content is claimed.

   **Review note:** This does not remove STV's own keyboard, scrolling or link
   interactions. Widget-specific JavaScript behavior in details is deferred.

.. swr:: Open details through hover or keyboard activation
   :id: STV_SWR_050
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/concept-reviews/round-1.rst :: STV_REVIEW_002; docs/requirement-changes/usability-problems.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_006, STV_SHR_034, STV_SHR_015
   :allocated_to: STV_SWE_INSPECT, STV_SWE_RENDER

   The software shall open the same full-detail panel when the reader hovers
   over a node or activates its keyboard-accessible Details control, without
   navigating away from the view.

   **Acceptance criterion:** A visible object exposes equivalent information
   through hover and keyboard Details activation. The panel permits keyboard
   scrolling and dismissal with focus restored to its trigger; new-tab node
   navigation remains a separate action.

   **Rationale:** The system parent carries full-object inspection; direct
   channeling from STV_SHR_034 refines keyboard interaction and from STV_SHR_015
   refines hover timing. These software-local interactions add no system
   responsibility or interface, so no new system obligation is needed.

   Hover activation shall wait 1000 ms. Leaving the node, dismissal, a scene commit or viewport movement shall cancel pending activation; moving from the node onto its Details button shall not restart the delay. Explicit Details activation shall bypass the delay.

   **Additional acceptance criterion:** No panel appears after a brief hover/departure; one appears after sustained hover. Keyboard activation opens immediately and Escape cancels a pending hover.

.. swr:: Provide the artificial project entry node
   :id: STV_SWR_051
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/requirement-changes/starting-nodes.rst; docs/requirement-changes/centered-layout-and-interactive-seeds.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_001
   :allocated_to: STV_SWE_GRAPH, STV_SWE_STATE, STV_SWE_RENDER

   The software shall provide an artificial project-named entry node for
   seedless views and an expandable group linking it to all non-hidden Needs
   identified as stakeholder requirements by the input data model, without
   inserting a fabricated Need into the host collection.

   The label shall use the host Sphinx project name. The root has no Need
   status, original-object link or full-detail overlay, and is placed above
   all configured artifact bands without changing their order.

   **Acceptance criterion:** A seedless fixture initially displays the
   project node and first stakeholder entries through the project-page
   contract of STV_SWR_052 while retaining the existing 200-node capacity limit. The project node remains visible
   during collapse, counts toward the visible-node limit and is distinguished
   from real Needs without a fabricated original-Need link. Replacing the input
   model's stakeholder type names does not require source-code changes.

.. swr:: Page stakeholder entry links
   :id: STV_SWR_052
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/requirement-changes/starting-nodes.rst; docs/requirement-changes/centered-layout-and-interactive-seeds.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_047, STV_SYS_008
   :allocated_to: STV_SWE_STATE, STV_SWE_RENDER

   The software shall expose all project-root stakeholder entry links through
   deterministic pages of at most five non-hidden top-level Needs, with accessible
   Previous/Next controls and page/total information, without relaxing the
   200-visible-node limit or changing ordinary trace-group expansion semantics.

   **Acceptance criterion:** A 201-stakeholder fixture offers 41 pages and
   every stakeholder ID appears on exactly one entry page. The initially open
   root reveals at most five entries. Page changes retain the project root,
   show only the selected page's rooted exploration and restore that page's
   independent accepted expansion state when revisited. Hidden entries and
   Need parts are not listed as top-level stakeholder roots. An empty project
   shows a no-stakeholder-requirements indication without an empty plus control.

   **Rationale:** Direct stakeholder derivation refines the software-local
   paging interaction explicitly chosen by the owner. SYS 008 retains the
   cross-boundary capacity constraint; no new artificial system obligation is
   required for paging controls.

.. swr:: Prefer direct facing-edge routes
   :id: STV_SWR_053
   :status: accepted
   :tags: release_initial
   :basis: owner
   :evidence: docs/requirement-changes/usability-problems.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_050
   :allocated_to: STV_SWE_LAYOUT

   The software shall test direct facing-edge segments against visible box interiors and use a direct segment when clear. Upward paths use source top and target bottom; downward paths use source bottom and target top. Overlapping vertical ranges use facing horizontal sides. Blocked paths and self-links retain obstacle-avoiding corridor routes.

   **Channeling rationale:** Facing ports and routing are local to the existing
   browser layout component, with no system responsibility or interface change.

   **Acceptance criterion:** Geometry smoke cases cover upward/downward links, clear fan-in, a blocked skipped level, test-lane links and a self-link, with endpoints on boundaries and no segment crossing a box interior.

.. swr:: Set enlarged standard viewport
   :id: STV_SWR_054
   :status: accepted
   :tags: release_initial
   :basis: owner
   :evidence: docs/requirement-changes/usability-problems.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_049
   :allocated_to: STV_SWE_RENDER

   The stylesheet shall set the standard viewport height to 975 CSS pixels.

   **Acceptance criterion:** The rendered viewport reports a computed height of 975px.

   **Channeling rationale:** Viewport height is a software-local stylesheet
   property within the existing renderer, with no additional system obligation.

.. swr:: Order controls using target semantic levels
   :id: STV_SWR_055
   :status: accepted
   :tags: release_initial
   :basis: owner
   :evidence: docs/problems/problem_5.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_051
   :allocated_to: STV_SWE_RENDER

   The software shall order nonempty relationship controls by the normalized
   levels of all targets relative to the source: wholly above, neutral, wholly
   below. Mixed, same-level, unresolved and test-role groups are neutral.
   Preserve the existing outgoing-then-incoming host order within each category,
   without changing group identities, labels, membership or expansion state.

   **Acceptance criterion:** Upward incoming and outgoing groups precede neutral
   and downward groups with stable ties. Replacement level mappings drive the
   order without relation-name assumptions. Expansion and collapse retain order
   and the existing keyboard/focus behavior.

   **Channeling rationale:** Control order is software-local presentation within
   the existing renderer, with no additional system obligation or interface.

.. swr:: Center parent boxes with collision-aware semantic placement
   :id: STV_SWR_056
   :status: accepted
   :tags: release_initial
   :basis: owner
   :evidence: docs/requirement-changes/centered-layout-and-interactive-seeds.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_052
   :allocated_to: STV_SWE_LAYOUT

   After semantic rank projection, layout shall derive each normal parent's
   desired horizontal center from the leftmost and rightmost boxes of its
   visible lower-level children, including synthetic project-entry children.
   It shall resolve competing desired positions deterministically with at least
   the existing inter-node gap, retain one shared box per Need and preserve
   level/test-lane constraints before recomputing all edge routes.

   **Acceptance criterion:** A five-child star centers exactly. Competing parents,
   shared children, cycles, reverse-authored links and isolated nodes preserve
   finite geometry, nonoverlap, semantic levels, shared identity and safe routes.

   **Channeling rationale:** Horizontal placement is local to the existing
   browser layout responsibility and adds no system interface or boundary.

.. swr:: Confirm local interactive seeds and restore project overview
   :id: STV_SWR_057
   :status: accepted
   :tags: release_initial
   :basis: owner
   :evidence: docs/requirement-changes/centered-layout-and-interactive-seeds.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_053
   :allocated_to: STV_SWE_RENDER, STV_SWE_STATE

   Each renderer shall offer a labelled local ID/title search with keyboard and
   pointer match selection and explicit confirmation. Matching is case-insensitive;
   free-text confirmation requires an exact existing ID after trimming. The
   catalog shall use only the published non-hidden graph and make no requests.
   Confirmation shall propose a fresh single-seed state; Project overview shall
   propose a fresh open first project page. Both shall pass capacity and layout
   checks before replacing only that view's committed scene and exploration.
   Invalid input or failed layout shall preserve the previous scene/state
   with a diagnostic. Stale layout completions shall be discarded without
   overwriting the newer request's state or diagnostic. Successful replacement shall close old details, clear prior
   expansions/page memory and reset that view's viewport; focus shall remain in
   its initiating picker control. Unconfirmed typing shall not change the graph.

   **Acceptance criterion:** ID/title search, exact-ID confirmation, keyboard
   suggestions, invalid/hidden input, empty catalogs, repeated changes, overview
   return, layout failure/staleness and independent views pass file/HTTP checks.
   Runtime seed replacement requires neither source edits nor a Sphinx rebuild.

   **Channeling rationale:** Selection and reset operate within the existing
   browser state/renderer and immutable graph, adding no system obligation.
