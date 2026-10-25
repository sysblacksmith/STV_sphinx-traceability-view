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
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst; docs/change-requests/STV_CR_006_centered-layout-and-interactive-seeds.rst
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

.. swr:: Place classified test evidence in its resolved rows
   :id: STV_SWR_012
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall treat classified test cases and executions as ordinary nodes
   in their resolved semantic row, sharing its top coordinate and horizontal
   collision rules. Their ranks shall not depend on currently revealed neighbors.
   The explicitly configured legacy test role shall continue to place shared tests
   once to the right of associated ordinary artifacts, with median-rank stacking.

   **Acceptance criterion:** Nine-category, shared cross-level test and multiple
   execution fixtures retain fixed classified rows, alignment, identity and safe
   routes across expansion/collapse and different seeds. The owner-selected common
   fallback row retains unclassified/conflicting evidence. Existing legacy-role
   fixtures still satisfy their right-side/median-rank constraints. Later occurrence
   mode remains deferred; this change does not claim to deliver it.

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

   The software shall position transient hover details inside the browser viewport with overflow scrolling and retain them while the pointer moves from trigger to overlay or remains over either.

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

.. swr:: Honor resolved declared level ordering
   :id: STV_SWR_037
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall derive ranks from the normalized ordered level list, using
   an object's resolved level when supplied and otherwise its fixed type placement.
   Only explicit legacy test-role nodes use contextual median ranks and a side lane.
   The synthetic project root stays above all configured rows; empty rows retain
   spacing, and unrelated custom categories retain their declared placement.

   **Acceptance criterion:** Added hardware, nine classified categories, fallback
   and problem rows respect the declared indices. Nodes in one classified row align
   at their top edges; hidden/missing and legacy-role behavior remains usable.

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

.. swr:: Separate transient hover and explicit persistent details
   :id: STV_SWR_050
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/concept-reviews/round-1.rst :: STV_REVIEW_002; docs/change-requests/STV_CR_003_usability-problems.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_006, STV_SHR_034, STV_SHR_015
   :allocated_to: STV_SWE_INSPECT, STV_SWE_RENDER

   Hover shall open a transient node-anchored panel after 1000 ms. Departure,
   Escape, scene commit and viewport movement cancel pending hover; entering the
   Details button shall retain its timer. Explicit Details activation shall bypass
   the delay and open/focus the persistent collection of STV_SWR_063/064 instead.
   Both paths shall show equivalent full information through the same safe detail
   transport/restoration, without navigating away. Hover never consumes collection
   capacity; explicit activation cancels the current hover without closing boxes.

   **Acceptance criterion:** Sustained/brief hover, pointer travel and scrolling,
   viewport-edge placement, Escape cancellation and immediate keyboard Details
   pass independently. Both show equivalent static content; persistent boxes survive
   graph changes while hover retains its dismissal behavior.

   **Rationale:** SYS 006 owns original-object inspection; direct SHR 034/015 paths
   refine keyboard/timing locally without an additional system boundary.

.. swr:: Provide the artificial project entry node
   :id: STV_SWR_051
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/change-requests/STV_CR_002_starting-nodes.rst; docs/change-requests/STV_CR_006_centered-layout-and-interactive-seeds.rst
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
   :evidence: docs/change-requests/STV_CR_002_starting-nodes.rst; docs/change-requests/STV_CR_006_centered-layout-and-interactive-seeds.rst
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
   :evidence: docs/change-requests/STV_CR_003_usability-problems.rst
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
   :evidence: docs/change-requests/STV_CR_003_usability-problems.rst
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
   :evidence: docs/problem-tickets/STV_PR_005.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_051
   :allocated_to: STV_SWE_RENDER

   The software shall order nonempty relationship controls by the normalized
   resolved levels of all targets relative to the source: wholly above, neutral, wholly
   below. Mixed, same-level, unresolved and legacy test-role groups are neutral.
   Classified case/execution groups use their resolved semantic levels.
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
   :evidence: docs/change-requests/STV_CR_006_centered-layout-and-interactive-seeds.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_052
   :allocated_to: STV_SWE_LAYOUT

   On fresh layout after semantic rank projection, layout shall derive each normal parent's
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

   Relationship/root toggles prioritize the stable-navigation policy of
   :need:`STV_SHR_054` / :need:`STV_SWR_058` over renewed parent centering.
   Initialization, seed replacement, overview return and page changes use fresh
   placement. Reset viewport changes only the transform, never node positions.

.. swr:: Confirm local interactive seeds and restore project overview
   :id: STV_SWR_057
   :status: accepted
   :tags: release_initial
   :basis: owner
   :evidence: docs/change-requests/STV_CR_006_centered-layout-and-interactive-seeds.rst
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
   overwriting the newer request's state or diagnostic. Successful replacement shall close transient hover details, retain persistent
   detail boxes, clear prior
   expansions/page memory and reset that view's viewport; focus shall remain in
   its initiating picker control. Unconfirmed typing shall not change the graph.

   **Acceptance criterion:** ID/title search, exact-ID confirmation, keyboard
   suggestions, invalid/hidden input, empty catalogs, repeated changes, overview
   return, layout failure/staleness and independent views pass file/HTTP checks.
   Runtime seed replacement requires neither source edits nor a Sphinx rebuild.

   **Channeling rationale:** Selection and reset operate within the existing
   browser state/renderer and immutable graph, adding no system obligation.

.. swr:: Stabilize committed navigation geometry
   :id: STV_SWR_058
   :status: accepted
   :tags: release_initial, navigation_stability
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_013.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_054
   :allocated_to: STV_SWE_LAYOUT, STV_SWE_RENDER

   For group/root toggles, layout shall use the last committed per-view geometry
   and activated node as an anchor. Preserve surviving ordinary x slots, anchor
   position and same-band ordinary y. Place newcomers in nearest available slots
   with 48 px separation; ties choose the leftmost slot. Preserve the test lane x
   while any legacy test-role node survives and keep ordinary nodes at least
   96 px to its left. Classified test cases/executions instead retain ordinary
   slots in their fixed rows.
   Retain legacy test offsets when their rank is unchanged; append new or reranked legacy tests
   without overlap. Anchor the activated band and move other bands only as needed
   for their measured height plus 100 px separation. Negative coordinates are valid.

   **Acceptance criterion:** Expansion, collapse, repeated identical input, upward
   band growth, shared-test reranking, project root toggles and a 200-node scene
   remain finite and nonoverlapping. Surviving ordinary horizontal slots and clicked
   node coordinates stay unchanged; unrelated views and viewport transforms stay
   unchanged. Failure/stale completion preserves the previous committed geometry.
   Fresh initialization, seed, overview and page commands omit prior geometry.

   **Channeling rationale:** This is software-local layout/render state within the
   existing browser boundary; no system interface or deployment obligation changes.

.. swr:: Render complete edge bounds at any graph origin
   :id: STV_SWR_059
   :status: accepted
   :tags: release_initial, navigation_stability
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_013.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_054
   :allocated_to: STV_SWE_RENDER

   The renderer shall derive SVG bounds from all final node corners and route
   points with 24 px marker padding. Apply equal SVG CSS and viewBox origins so
   negative coordinates retain the same world-to-screen mapping as HTML nodes.
   Accumulate extrema without spreading route arrays. Restore focus without native
   scrolling. Initial fitting and explicit Reset viewport shall include negative
   node extents; toggles shall preserve the current D3 transform.

   **Acceptance criterion:** Firefox file/HTTP upward and downward negative-route
   fixtures contain every polyline point and align endpoints with node borders
   within 2 screen px. Empty geometry has finite positive SVG bounds. Reset fits
   the scene and focus does not move it; pan/zoom and independent views still work.

   **Channeling rationale:** SVG clipping/focus are local presentation concerns;
   no new system boundary, transport or external service is introduced.

.. swr:: Use natural ID order for fresh unexpanded rows
   :id: STV_SWR_060
   :status: accepted
   :tags: release_initial, navigation_stability
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_013.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_055
   :allocated_to: STV_SWE_LAYOUT

   When the fresh visible graph has no authored relationship edges, sort ordinary
   nodes within each semantic rank by the full Need ID using English numeric
   collation, case-sensitive variant comparison and a deterministic lexical tie.
   Synthetic entry links do not disable this policy. With authored edges use ELK
   ordering and fresh parent centering; incremental navigation preserves old slots.

   **Acceptance criterion:** Shuffled REQ_20, REQ_10, REQ_3, REQ_2, REQ_1 seeded and
   project-entry rows use natural order; expanding REQ_2 preserves all seed slots.
   Different ranks and the separate test lane remain intact.

   **Channeling rationale:** Row ordering is local to the existing layout component
   and needs no additional system requirement or boundary.

.. swr:: Resolve configurable per-object placement at build time
   :id: STV_SWR_061
   :status: accepted
   :tags: release_initial, classified_rows
   :basis: owner
   :evidence: docs/change-requests/STV_CR_013_artifact_vertical_target_position.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_002, STV_SHR_012
   :allocated_to: STV_SWE_MODEL, STV_SWE_GRAPH

   Supplemental type placement shall support exactly one fixed level, legacy
   test role, tag-to-level map, or one-hop relation-owner level map. Resolve
   tag placements first and owner-derived placements next against the complete
   published graph, never against visible edges or ID prefixes. Serialize the
   resolved level with each classified object. A configured fallback level
   retains missing/conflicting classifications and carries an unclassified
   indication; without fallback, unresolved classification fails with Need ID.
   Invalid model shape, unknown level or relation always fails with entry path.
   Exclude hidden records before classification; never expose hidden owner IDs.

   **Acceptance criterion:** Renamed host types/tags/relations, zero/one/conflicting
   tags, orphan/multiple owners, mixed owner classes, hidden owners and execution
   seeds produce their explicit row or configured fallback deterministically.
   Owners already resolved to fixed/tag rows can supply execution placement;
   chained owner-derived links are not inferred and use fallback/strict handling. Host data remains unmodified,
   output is deterministic and classification requires O(N + E) indexing.

.. swr:: Mark the viewport clipping edge
   :id: STV_SWR_062
   :status: accepted
   :tags: release_initial, viewport
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_014_node_disappears_behind_invisible_line.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_056
   :allocated_to: STV_SWE_RENDER

   The renderer shall draw a 1 CSS-pixel solid neutral-grey top border on the
   overflow-hidden viewport, after toolbar/status and outside the transformed
   scene. Explicit content-box sizing shall preserve its 975 px client height
   under content-box and border-box host themes. No overlay or extra input
   handler shall be introduced; the border shall span the viewport width.

   **Acceptance criterion:** Firefox file/HTTP checks reproduce a node crossing
   the real clip edge. Hit tests above/on the border exclude the node while a
   point just inside the content hits it. Pan/zoom retain the border's position,
   resize follows control wrapping/width, client height remains 975 px, and
   keyboard expansion/Reset and independent-view behavior remain usable.

   **Channeling rationale:** A visible clipping marker is local renderer
   presentation, adding no deployment, system interface or cross-boundary duty.

.. swr:: Own a per-view persistent detail collection
   :id: STV_SWR_063
   :status: accepted
   :tags: release_initial, persistent_details
   :basis: owner
   :evidence: docs/change-requests/STV_CR_014_persistent-right-side-details.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_057
   :allocated_to: STV_SWE_INSPECT

   Maintain an insertion-ordered collection keyed by Need ID, separate from hover
   and exploration state. Reuse/focus does not reorder. On new insertion at the
   configured capacity remove the oldest live entry, then append the new entry.
   Manual close removes only its entry; Close all clears only this view. Scene,
   viewport, seed, page and overview operations do not clear it. Async completion
   may update only the same still-live entry; closed/evicted/reopened entries must
   not receive stale content. Loading/error remain identifiable and closable;
   close/reopen retries failed transport using the existing cache policy.

   **Acceptance criterion:** Default/override/one-slot capacity, reuse versus reopen,
   FIFO after focus, independent close/all, independent views, delayed completion,
   eviction/close races, explicit failure/retry and graph replacement pass.
   **Channeling rationale:** Inspection state is browser-local with no new system
   interface, persistence service or domain graph mutation.

.. swr:: Present and focus persistent detail boxes
   :id: STV_SWR_064
   :status: accepted
   :tags: release_initial, persistent_details
   :basis: owner
   :evidence: docs/change-requests/STV_CR_014_persistent-right-side-details.rst; docs/problem-tickets/STV_PR_015_detail-presentation.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_057, STV_SHR_034
   :allocated_to: STV_SWE_RENDER, STV_SWE_INSPECT

   Render a per-view dock beside the graph at widths above 1120 CSS px; below it
   at narrower container widths. Target dock width is 720 px, with independent
   vertical stack scrolling and bounded scrollable boxes. A 1 CSS-pixel solid
   neutral-grey frame shall mark all four pane edges. In side-by-side layout its
   top and full outer height align with the graph viewport; retain inset padding
   and shadow-free cards so the first box has a clean, distinct top edge.
   Identify every artifact
   and retain original links and safe rich-body restoration with unique IDs/IDREFs.
   Place a view-local Close all details control at the right end of the toolbar.
   Explicit open/reuse focuses its Close control and reveals it without changing
   D3 graph geometry. Manual close restores the current artifact trigger if it
   exists, else Close all; eviction must not leave focus on removed content.
   Async content must not steal focus. Escape dismisses hover only. Reset computes
   fit from current viewport dimensions, including an open dock.

   Copied Need metadata starts folded in both hover and persistent details. Its
   own arrow toggles only that copy by pointer, Enter or Space, with focusable
   button semantics and accurate expanded/controls associations. Reusing a box
   preserves its disclosure state. The artifact-ID header link opens the actual
   source document/Need in a new tab; ordinary body anchors remain local where
   appropriate. No host document-ready script is required for copied controls.

   **Acceptance criterion:** Keyboard traversal/read/scroll/close, responsive layout,
   long bodies/stack, unique fragment IDs, fallback focus after artifact removal,
   non-stealing async content, surviving collection during graph changes and a
   current-width Reset, folded metadata/toggle keyboard behavior and canonical
   header-ID navigation pass on file/HTTP. No modal focus trap or graph overlay.
   **Channeling rationale:** Presentation and focus remain within renderer/inspector
   responsibilities, without new deployment or system boundary.

.. swr:: Validate and publish the persistent details limit
   :id: STV_SWR_065
   :status: accepted
   :tags: release_initial, persistent_details
   :basis: owner
   :evidence: docs/change-requests/STV_CR_014_persistent-right-side-details.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SYS_002, STV_SHR_057
   :allocated_to: STV_SWE_DIRECTIVE, STV_SWE_MODEL

   Register traceability_view_details_limit as a Sphinx author setting, default 10.
   Accept positive integers up to 9007199254740991 (the exact JavaScript integer
   range); reject booleans, nonintegers, zero, negatives and larger values with a
   source/config-located diagnostic before publishing graph data. Publish the
   validated value in additive schema-1 graph.details_limit; older graphs without
   this optional field use 10. Every view enforces its own collection limit.

   **Acceptance criterion:** Default, 1 and 3 serialize and drive actual eviction;
   invalid types/bounds fail clearly. Rebuilds reflect changed configuration.
   The runtime does not require Node, a service or reader-side configuration.

.. swr:: Reset view-local exploration to current roots
   :id: STV_SWR_066
   :status: draft
   :tags: change_increment
   :basis: documented
   :evidence: docs/change-requests/STV_CR_015_collapse-all-nodes.rst; docs/internal-interfaces.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_058
   :allocated_to: STV_SWE_STATE, STV_SWE_RENDER

   The software shall handle collapse-all as one atomic view-local transition
   using the current mode and seeds, clearing expanded groups and all stored
   project-page expansion sets. In project mode it shall restore page zero and
   the initially open entry group. It shall advance the revision to invalidate
   stale layout results, preserve persistent cards, and retain keyboard focus
   on the command. A fresh fit shall use the actual graph viewport dimensions.

   **Acceptance criterion:** Multiple seeds, interactive reseeding, shared paths/cycles, empty/fewer-than-five
   project entries and a previously closed entry group reset to their defined
   initial states. Returning to another project page cannot restore old expansions.
   Other views and persistent entries/order are unchanged. Repeated resets remain
   valid within the existing 200-node limit.

   **Channeling rationale:** This is a browser presentation/session or author
   presentation-setting obligation within the existing extension boundary; it
   adds no separate cross-system service, deployment or interface obligation.

.. swr:: Validate and serialize independent detail font scales
   :id: STV_SWR_067
   :status: draft
   :tags: change_increment
   :basis: documented
   :evidence: docs/change-requests/STV_CR_017_configurable-detail-font-size.rst; docs/internal-interfaces.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_060
   :allocated_to: STV_SWE_MODEL, STV_SWE_DIRECTIVE

   The software shall accept author settings traceability_view_tooltip_font_scale
   and traceability_view_details_font_scale, each defaulting to 0.7. Values shall
   be finite positive numbers, excluding booleans. Invalid values shall fail the
   build with the setting name. It shall serialize both settings as graph
   presentation fields without modifying the host Need model.

   **Acceptance criterion:** Default, 1.0 and independent 0.8/0.6 values are published unchanged. Zero,
   negative, boolean, string, NaN and infinite values fail deterministically.
   Missing presentation fields in older bundles mean 1.0, preserving their
   pre-change appearance; new builds always publish explicit defaults.

   **Channeling rationale:** This is a browser presentation/session or author
   presentation-setting obligation within the existing extension boundary; it
   adds no separate cross-system service, deployment or interface obligation.

.. swr:: Scale copied detail typography once per presentation
   :id: STV_SWR_068
   :status: draft
   :tags: change_increment
   :basis: documented
   :evidence: docs/change-requests/STV_CR_017_configurable-detail-font-size.rst; docs/internal-interfaces.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_060
   :allocated_to: STV_SWE_INSPECT, STV_SWE_RENDER

   The software shall apply the effective font scale independently to each hover
   or persistent detail copy, against that presentation's unscaled computed
   typography. It shall scale nested headings, metadata, tables and code exactly
   once, preserve relative hierarchy and browser zoom, and leave original Need
   pages and graph summaries unchanged.

   **Acceptance criterion:** At identical browser zoom, representative text computed sizes are 0.7 times
   their scale-1.0 baselines within 0.5 CSS px rounding. Independent overrides
   affect only the intended presentation. Reuse, reopen and delayed content do
   not compound scaling; scrolling, disclosure and visible focus remain usable.

   **Channeling rationale:** This is a browser presentation/session or author
   presentation-setting obligation within the existing extension boundary; it
   adds no separate cross-system service, deployment or interface obligation.

.. swr:: Control rendered page metadata through scoped bulk actions
   :id: STV_SWR_069
   :status: draft
   :tags: change_increment
   :basis: documented
   :evidence: docs/change-requests/STV_CR_018_page-wide-need-attribute-controls.rst; docs/internal-interfaces.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_061
   :allocated_to: STV_SWE_RENDER, STV_SWE_DIRECTIVE

   The software shall initialize one page-level pair of Collapse all / Expand all
   controls on pages with rendered host Needs. When no collapsible metadata
   exists, both controls shall be disabled with a no-attributes explanation. Actions shall
   set every eligible host disclosure explicitly rather than blindly toggling,
   synchronize row visibility, icons and ARIA, and preserve individual controls.
   It shall exclude STV view subtrees and copied detail overlays.

   **Acceptance criterion:** Mixed open/closed sections, several types, out-of-viewport Needs and absent
   metadata behave deterministically. Repeated initialization adds no duplicate
   controls/handlers. Pointer and Enter/Space work, titles/body stay visible,
   and host individual toggles still work after either bulk operation. Pages
   without rendered host Needs have no bulk controls; Needs without metadata
   retain disabled controls and an explanation.

   **Channeling rationale:** This is a browser presentation/session or author
   presentation-setting obligation within the existing extension boundary; it
   adds no separate cross-system service, deployment or interface obligation.

.. swr:: Capture a clipped inert visible-area SVG snapshot
   :id: STV_SWR_070
   :status: draft
   :tags: change_increment
   :basis: documented
   :evidence: docs/change-requests/STV_CR_016_save-current-view-as-svg.rst; docs/internal-interfaces.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_011
   :allocated_to: STV_SWE_EXPORT

   The software shall freeze a committed per-view presentation, crop its graph
   viewport and visible detail regions to the screen-visible workspace bounds,
   and serialize an inert SVG containing the current geometry, computed styles,
   clipping and scroll state. It shall exclude toolbar/status controls, other
   views and off-screen regions. It shall copy rather than mutate live DOM.

   **Acceptance criterion:** A panned graph with clipped nodes, scrolled long cards, folded attributes,
   narrow stacked layout and a visible transient tooltip exports the same visible
   crop. XML parses, SVG reopens independently in Firefox, and script/event/form
   behavior and graph datasets are absent. A concurrent layout commit cannot
   mix revisions; a new attempt captures the new revision.

.. swr:: Save and release SVG downloads without changing exploration
   :id: STV_SWR_071
   :status: draft
   :tags: change_increment
   :basis: documented
   :evidence: docs/change-requests/STV_CR_016_save-current-view-as-svg.rst; docs/internal-interfaces.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_011
   :allocated_to: STV_SWE_EXPORT, STV_SWE_RENDER

   The software shall offer a keyboard-accessible Save as SVG control and deliver
   successful snapshots as image/svg+xml Blob downloads with a safe .svg filename.
   Browser-managed Save As and documented browser download settings shall provide
   location choice. It shall prevent duplicate concurrent exports per view,
   announce errors, and release temporary nodes/object URLs without altering
   graph, detail collection, focus ownership or stored state.

   **Acceptance criterion:** Location-prompt mode allows saving to a chosen folder or cancelling. Automatic
   download mode is identified in user guidance without claiming that the app can
   force a dialog or detect completion. Export failure preserves the live view
   and permits retry; repeated exports and pagehide do not leak object URLs.

.. swr:: Bundle safe export resources for offline snapshots
   :id: STV_SWR_072
   :status: draft
   :tags: change_increment
   :basis: documented
   :evidence: docs/change-requests/STV_CR_016_save-current-view-as-svg.rst; docs/internal-interfaces.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_011
   :allocated_to: STV_SWE_DETAIL_BUILD, STV_SWE_BUNDLE, STV_SWE_EXPORT

   The software shall embed required output-local detail images and fonts in
   content-addressed export resource records during bundle finalization. It shall
   resolve resources only inside the final output root, preserve the existing
   unavailable-remote-media policy, and rewrite snapshot resources to validated
   self-contained data or inline SVG. It shall not fetch resources during export
   or copy active external resources into the saved SVG.

   **Acceptance criterion:** Local PNG/SVG, srcset selection, CSS image/font resources and paths containing
   non-ASCII characters work under file and HTTP. Traversal, remote URLs, active
   SVG and malformed resources cannot execute or access outside files. Missing
   required visible resources fail visibly; off-screen content is not loaded for
   capture. Hidden Needs and transport/graph data are not export payloads.
