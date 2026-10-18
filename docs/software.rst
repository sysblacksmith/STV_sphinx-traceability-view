Software requirements
=====================

Draft software specification derived from the accepted stakeholder baseline and
proposed system requirements. See :doc:`architecture-software` for interfaces
and :doc:`review` for remaining verification gaps. Later-mode clauses are not
MVP implementation commitments.

.. swr:: Register the RST entry point
   :id: STV_SWR_001
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_001
   :allocated_to: STV_SWE_DIRECTIVE

   The software shall register a traceability-view directive taking one starting Need ID and emit a serializable placeholder with source filename, line and per-page instance ID.

   **Acceptance criterion:** A host RST fixture with two directives produces distinct placeholders with the supplied IDs.

.. swr:: Resolve seeds after collection
   :id: STV_SWR_002
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_001
   :allocated_to: STV_SWE_GRAPH

   The software shall resolve starting IDs only after all host documents have contributed Needs, without restricting eligible seeds to selected types.

   **Acceptance criterion:** A seed defined on a later-read document resolves for each fixture type.

.. swr:: Initialize collapsed state
   :id: STV_SWR_003
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_003
   :allocated_to: STV_SWE_STATE

   The software shall initialize each view with only its starting object visible and no expanded relationship keys.

   **Acceptance criterion:** Initial state has one node and an empty expansion set.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Expose plus controls
   :id: STV_SWR_004
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_004
   :allocated_to: STV_SWE_RENDER

   The software shall render a plus control for every nonempty relationship-type and direction group on each collapsed displayed node.

   **Acceptance criterion:** The fixture exposes one control per nonempty group and activating it dispatches its group key.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Expand complete target groups
   :id: STV_SWR_005
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_005
   :allocated_to: STV_SWE_STATE

   The software shall reveal all targets of the selected object, relationship type and direction as one state transition, subject to the node cap.

   **Acceptance criterion:** Expanding a group displays every target or rejects the entire transition at the cap.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Traverse without depth cutoff
   :id: STV_SWR_006
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_004
   :allocated_to: STV_SWE_GRAPH

   The software shall provide indexed outgoing and incoming adjacency for every resolved object without imposing a traversal-depth cutoff.

   **Acceptance criterion:** A path crossing document boundaries can be followed beyond three hops from either end.

.. swr:: Collapse relationship groups
   :id: STV_SWR_007
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_007
   :allocated_to: STV_SWE_STATE

   The software shall remove the selected expansion key and recompute visible reachability from the seed.

   **Acceptance criterion:** A collapsed group can be reopened and does not remain as a visibility root.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Render fixed node summaries
   :id: STV_SWR_008
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_008
   :allocated_to: STV_SWE_RENDER

   The software shall show the complete ID and a title visually clamped to two lines while keeping the full ID visible without author field-selection settings.

   **Acceptance criterion:** Long-title nodes retain the complete ID and expose their full title in details; the two-line summary clamp is tested without making its field set configurable.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Order requirement ranks
   :id: STV_SWR_009
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall assign stakeholder, system and software requirements to increasing vertical ranks under the default mapping.

   **Acceptance criterion:** Their node bounding boxes remain vertically ordered after each expansion.

.. swr:: Insert system architecture rank
   :id: STV_SWR_010
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall place default system architecture nodes below system requirements and above software requirements.

   **Acceptance criterion:** A fixture with all three categories has nonoverlapping ordered rank bands.

.. swr:: Place software architecture rank
   :id: STV_SWR_011
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall place default software architecture nodes below software requirements.

   **Acceptance criterion:** Expanding architecture preserves the required rank order.

.. swr:: Place test nodes on the right
   :id: STV_SWR_012
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall place each revealed shared test node to the right of all visible artifacts connected to it by revealed test traces; later occurrence mode places each copy beside its source.

   **Acceptance criterion:** A test linked to two ranks appears once beyond both artifact right bounds in shared mode.

.. swr:: Index both trace directions
   :id: STV_SWR_013
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_004
   :allocated_to: STV_SWE_GRAPH

   The software shall construct incoming adjacency from canonical outgoing relations without requiring authors to duplicate inverse links.

   **Acceptance criterion:** A single authored relationship appears in both directional indexes with one canonical edge identity.

.. swr:: Normalize replacement mappings
   :id: STV_SWR_014
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_002
   :allocated_to: STV_SWE_MODEL

   The software shall normalize supplemental model mappings against host type and relationship definitions without hard-coded host type names in graph or layout algorithms.

   **Acceptance criterion:** Replacing types and mapping names changes the view without modifying extension code.

.. swr:: Publish full rendered details
   :id: STV_SWR_015
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_006
   :allocated_to: STV_SWE_DETAIL_BUILD

   The software shall capture the final host-rendered Need representation for each resolved object and make its displayed metadata and body available to details without a separate field whitelist.

   **Acceptance criterion:** A cross-page Need with custom metadata, formatted body and local images has equivalent information in details; hidden internal fields are not exposed.

.. swr:: Open canonical object links
   :id: STV_SWR_016
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_006
   :allocated_to: STV_SWE_INSPECT

   The software shall activate a node through an anchor targeting a new tab at the original document and Need anchor while leaving the source view state unchanged.

   **Acceptance criterion:** Activation from file and HTTP output opens the correct cross-page object and preserves exploration.

.. swr:: Avoid runtime network loading
   :id: STV_SWR_017
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_003
   :allocated_to: STV_SWE_BUNDLE

   The software shall emit local classic-script data and runtime assets, with local detail fragments, so startup and exploration require no fetch, module import, CDN or backend request.

   **Acceptance criterion:** With network disabled, file-URL output supports expansion, details and local links with no missing runtime assets.

.. swr:: Use portable output URLs
   :id: STV_SWR_018
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_003
   :allocated_to: STV_SWE_BUNDLE

   The software shall generate graph, asset and documentation URLs relative to the containing output page so nested pages work on static hosts and from disk.

   **Acceptance criterion:** The same nested-page bundle works below a non-root HTTP prefix and through file URLs.

.. swr:: Offer occurrence mode later
   :id: STV_SWR_019
   :status: draft
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
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_020
   :allocated_to: STV_SWE_STATE

   The software shall use one visible node per Need ID in the initial shared-node mode.

   **Acceptance criterion:** Opening two paths to the same Need produces one node with both revealed connections.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Retain state across later mode changes
   :id: STV_SWR_021
   :status: draft
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
   :status: draft
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
   :status: draft
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
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_024
   :allocated_to: STV_SWE_STATE

   The software shall represent a return to an ancestor ID as a closing edge in shared mode or a terminal reference in later occurrence mode instead of recursively adding occurrences.

   **Acceptance criterion:** Self-links, reverse traversal and A-B-C-A terminate without repeated branch growth.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Compute seed-rooted visibility
   :id: STV_SWR_025
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_025
   :allocated_to: STV_SWE_STATE

   The software shall retain only nodes reachable from the seed through currently expanded groups after collapse, including nodes shared by remaining paths.

   **Acceptance criterion:** A diamond retains the shared target until the last path closes; a disconnected cycle is removed.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Report invalid invocation seeds
   :id: STV_SWR_026
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_001
   :allocated_to: STV_SWE_DIRECTIVE

   The software shall raise a source-located build error for omitted seeds and for IDs unresolved after host collection.

   **Acceptance criterion:** Both missing and unknown seed fixtures return failure with the invocation file and line.

.. swr:: Tolerate host broken traces
   :id: STV_SWR_027
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_004
   :allocated_to: STV_SWE_GRAPH

   The software shall retain resolvable graph entries when targets are missing and avoid raising an extension-specific missing-target failure.

   **Acceptance criterion:** A dangling target does not prevent generation of valid view data; host broken-link validation still controls build status.

.. swr:: Create missing-target nodes
   :id: STV_SWR_028
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_004
   :allocated_to: STV_SWE_RENDER

   The software shall display a missing-target node with its referenced ID, explicit missing-object text and source connection when its group is expanded.

   **Acceptance criterion:** The placeholder is identifiable without color and does not pretend to offer a valid original-object link.

.. swr:: Indicate empty adjacency
   :id: STV_SWR_029
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_029
   :allocated_to: STV_SWE_RENDER

   The software shall omit controls for empty directional groups and show No related objects when both adjacency directions are empty.

   **Acceptance criterion:** An isolated node has the indication and no controls; a dangling target group still has a control.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Resolve type palette
   :id: STV_SWR_030
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_030
   :allocated_to: STV_SWE_MODEL

   The software shall use host type colors where present and a deterministic built-in type palette where absent.

   **Acceptance criterion:** Explicit colors survive mixed configured/unconfigured fixtures and omitted colors are consistent per type.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Apply acceptance borders
   :id: STV_SWR_031
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_031
   :allocated_to: STV_SWE_RENDER

   The software shall render a red border when status is missing, empty or outside the normalized accepted-status set, independently of type background.

   **Acceptance criterion:** Draft, reviewed and empty statuses are red; configured accepted statuses have no red status border.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Normalize accepted values
   :id: STV_SWR_032
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_032
   :allocated_to: STV_SWE_MODEL

   The software shall read accepted-status values from supplemental mappings and use the singleton accepted default when no override is supplied.

   **Acceptance criterion:** An approved override changes styling without requiring field-level tooltip settings.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Constrain and retain details overlays
   :id: STV_SWR_033
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_006
   :allocated_to: STV_SWE_INSPECT

   The software shall position details inside the viewport with overflow scrolling and retain them while the pointer moves from trigger to overlay or remains over either.

   **Acceptance criterion:** A long object at a viewport corner remains readable and scrollable without closing.

.. swr:: Provide keyboard interaction
   :id: STV_SWR_034
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_034
   :allocated_to: STV_SWE_RENDER

   The software shall expose focusable semantic controls for expansion, details, viewport movement and object links, with visible focus and a way to dismiss details without trapping focus.

   **Acceptance criterion:** The shared-mode workflow is completable without a pointer; later mode controls meet the same rule when delivered.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Label directional controls
   :id: STV_SWR_035
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_035
   :allocated_to: STV_SWE_RENDER

   The software shall use the host model's incoming and outgoing labels on separate controls carrying independent group identities.

   **Acceptance criterion:** An object with both directions of one relation can toggle each independently using distinguishable labels.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Reject invalid model entries
   :id: STV_SWR_036
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_002
   :allocated_to: STV_SWE_MODEL

   The software shall reject unknown types, unknown levels and missing required mappings with diagnostics identifying the relevant configuration entry.

   **Acceptance criterion:** Malformed fixtures fail before asset generation while omitted optional colors and acceptance values receive defaults.

.. swr:: Honor declared level ordering
   :id: STV_SWR_037
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_005
   :allocated_to: STV_SWE_LAYOUT

   The software shall build rank order from the normalized ordered level list and map all host types to declared levels or the test role.

   **Acceptance criterion:** An added hardware level is placed at its declared index without code changes.

.. swr:: Scope state to view roots
   :id: STV_SWR_038
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_007
   :allocated_to: STV_SWE_STATE

   The software shall instantiate exploration, focus and viewport state separately for every directive root while sharing only immutable project data.

   **Acceptance criterion:** Two views remain independent after navigation and viewport commands; later selectors are independent too.

.. swr:: Implement view-local zoom
   :id: STV_SWR_039
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_039
   :allocated_to: STV_SWE_RENDER

   The software shall change the view-local graph transform for zoom commands without mutating expansion sets or layout rank ordering.

   **Acceptance criterion:** Pointer and keyboard zoom preserve state and do not change another view.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Implement view-local pan
   :id: STV_SWR_040
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SHR_040
   :allocated_to: STV_SWE_RENDER

   The software shall translate the view-local graph viewport for pan commands without mutating graph topology.

   **Acceptance criterion:** All off-screen nodes can be brought into view by pointer or keyboard.

   **Rationale:** Channeling: this is a software-local interaction or presentation obligation with no additional system-boundary impact; a synthetic system requirement is unnecessary.

.. swr:: Verify Firefox on Windows
   :id: STV_SWR_041
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_010
   :allocated_to: STV_SWE_RENDER

   The software shall use browser interfaces exercised by the documented release checks on stable Firefox desktop for Windows in both file and HTTP contexts.

   **Acceptance criterion:** The release record states exact browser and OS versions and results for both contexts.

.. swr:: Package for the pinned toolchain
   :id: STV_SWR_042
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_009
   :allocated_to: STV_SWE_DIRECTIVE

   The software shall ship a wheel containing the Python extension and required browser assets with metadata documenting the initial Python and Sphinx compatibility contract.

   **Acceptance criterion:** A clean Python 3.10 environment with pinned Sphinx dependencies installs the wheel and builds the fixture.

.. swr:: Enforce visible occurrence capacity
   :id: STV_SWR_043
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_008
   :allocated_to: STV_SWE_STATE

   The software shall count all candidate visible node occurrences, including placeholders, against a constant limit of 200 before committing a graph transition.

   **Acceptance criterion:** Candidate sizes 199 and 200 pass, 201 fails; a tens-of-thousands graph fixture remains addressable through adjacency indexes.

.. swr:: Reject over-limit transitions atomically
   :id: STV_SWR_044
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_008
   :allocated_to: STV_SWE_STATE

   The software shall reject an expansion or later mode switch exceeding the node cap without changing prior graph, mode or expansion state and announce the reason.

   **Acceptance criterion:** An over-limit expansion adds no partial targets and explains that branches must be collapsed first.

.. swr:: Reuse canonical host definitions
   :id: STV_SWR_045
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_002
   :allocated_to: STV_SWE_MODEL

   The software shall read type names, colors and relation labels from the resolved host configuration and require only supplemental layout and acceptance information.

   **Acceptance criterion:** Changing a host type label or relation label is reflected without duplicate definitions in extension configuration.

.. swr:: Expose an installable entry module
   :id: STV_SWR_046
   :status: draft
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed
   :derives_from: STV_SYS_009
   :allocated_to: STV_SWE_DIRECTIVE

   The software shall provide a package entry module with Sphinx setup registration and bundled assets so an external project can enable the extension by module name.

   **Acceptance criterion:** A separate project enables the installed module and renders a seeded view without repository imports.

