Stakeholder requirements
========================

Stakeholder outcomes and constraints. See :doc:`review` for scope decisions.

.. shr:: Embed a traceability view
   :id: STV_SHR_001
   :status: accepted
   :tags: feature_integration, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow documentation authors to embed an interactive
   traceability view in an RST document within a Sphinx-Needs project.

   **Acceptance criterion:** An author embeds a view in an RST page, builds the
   project as HTML, and a reader can use the view on the resulting page.

.. shr:: Select the starting object
   :id: STV_SHR_002
   :status: accepted
   :tags: feature_integration, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow documentation authors to select any existing Need
   object as the starting object of an embedded view by specifying its ID.

   **Scope clarification (owner, 2026-10-18):** Needs intentionally hidden by
   the host are excluded from exploration and cannot be used as starting IDs.
   Their connections are excluded as well; see :doc:`sources` and
   :need:`STV_SWR_048`. Baseline v1 history is retained.

   **Acceptance criterion:** For each Need type in an agreed demonstration project,
   an embedded view seeded with an existing ID of that type displays that object.

.. shr:: Initially collapse traced objects
   :id: STV_SHR_003
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall initially display the starting object with its related objects
   collapsed.

   **Acceptance criterion:** On first opening a view whose starting object has
   relationships, the starting object is visible and its related objects have not
   yet been revealed.

.. shr:: Offer expansion by traceability type
   :id: STV_SHR_004
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall initially provide a plus-sign expansion control for each
   traceability type available on the starting object.

   **Acceptance criterion:** For a starting object with multiple traceability types,
   the reader can identify and activate a separate plus-sign control for each type.

   **Review note:** Empty relationship types have no expansion control; see
   :need:`STV_SHR_029`. Incoming and outgoing relationships use separate controls
   with model-defined directional labels; see :need:`STV_SHR_035`.

.. shr:: Reveal related objects
   :id: STV_SHR_005
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to reveal the objects related to a displayed
   object through a selected traceability type by activating its expansion control.

   **Acceptance criterion:** Expanding a type reveals the related objects for that
   type, with their relationship to the expanded object identifiable.

.. shr:: Continue exploration
   :id: STV_SHR_006
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to continue expanding relationships from objects
   revealed during exploration.

   **Acceptance criterion:** In a demonstration with a path of at least three
   relationships, the reader follows the path by expanding each newly revealed
   object without changing the embedded starting ID.

   **Review note:** The intended outcome is exploration of the whole connected
   traceability structure. Bidirectional navigation is specified in
   :need:`STV_SHR_013`; cycles are covered by :need:`STV_SHR_024` and shared
   objects by :need:`STV_SHR_019` through :need:`STV_SHR_023`.

.. shr:: Collapse opened traces
   :id: STV_SHR_007
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to collapse previously expanded relationships
   interactively.

   **Acceptance criterion:** A reader expands a relationship, collapses it, and can
   expand it again.

   **Review note:** Objects reached through another open path remain visible
   as specified in :need:`STV_SHR_025`.

.. shr:: Inspect discovered objects
   :id: STV_SHR_008
   :status: accepted
   :tags: feature_inspection, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall display each Need object's ID and a shortened title in its
   visible node.

   **Acceptance criterion:** After revealing an object, a reader can inspect its
   ID and shortened title directly in the node without opening another page.

   **Review note:** Node fields and shortening limits are not configurable in
   the current scope. The internal concept specifies a fixed two-line title clamp (STV_SWR_008).
   Hover details and access to the original object are specified separately in
   :need:`STV_SHR_015` and :need:`STV_SHR_016`.

.. shr:: Preserve requirement levels
   :id: STV_SHR_009
   :status: accepted
   :tags: feature_layout, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall position visible stakeholder requirements above visible system
   requirements and visible system requirements above visible software requirements
   throughout interactive exploration.

   **Acceptance criterion:** Expanding and collapsing a demonstration containing all
   three levels preserves their relative vertical ordering, including when the
   starting object is a software requirement.

.. shr:: Position system architecture
   :id: STV_SHR_010
   :status: accepted
   :tags: feature_layout, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall position visible system architecture objects between the system
   requirement level and the software requirement level.

   **Acceptance criterion:** A view containing all three categories places the system
   architecture objects below system requirements and above software requirements.

.. shr:: Position software architecture
   :id: STV_SHR_011
   :status: accepted
   :tags: feature_layout, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall position visible software architecture objects below the software
   requirement level.

   **Acceptance criterion:** Expanding traces to software architecture objects places
   them below visible software requirements.

.. shr:: Position test cases beside artifacts
   :id: STV_SHR_012
   :status: accepted
   :tags: feature_layout, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall display test cases revealed through trace expansion to the right
   of the artifacts to which they are traced.

   **Acceptance criterion:** Expanding an artifact's test-case relationship displays
   the related test cases to its right, with the association identifiable.

   In shared-node mode, a test case linked to multiple visible artifacts shall
   appear once to the right of all those artifacts, with each revealed connection
   visible. In separate-occurrence mode, each occurrence shall appear to the
   right of its respective artifact.

   **Acceptance criterion for shared test cases:** Expanding test traces from
   two artifacts to the same test case displays one test node to the right of
   both artifacts in shared-node mode, and one occurrence to the right of each
   artifact in separate-occurrence mode.

.. shr:: Navigate relationships in both directions
   :id: STV_SHR_013
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner confirmation of bidirectional navigation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to explore both incoming and outgoing
   relationships from every displayed Need object, regardless of which endpoint
   authors the relationship.

   **Acceptance criterion:** Given software and system requirements linked to
   their respective parents, a reader starting at the software requirement can
   expand to its system and stakeholder requirements. Starting at the stakeholder
   requirement, the reader can follow the same relationships to the system and
   software requirements without additional authored inverse links.

.. shr:: Use a replaceable input data model
   :id: STV_SHR_014
   :status: accepted
   :tags: feature_integration, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner confirmation of replaceable input data model 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow documentation authors to supply and replace the data
   model defining the artifact types, relationship types and mappings to visual
   layout categories used by the traceability view without modifying the
   extension's implementation.

   **Acceptance criterion:** Using two Sphinx-Needs projects with different
   artifact and relationship type names, an author supplies the corresponding
   model for each project. Both views support expansion in both directions and
   position artifacts according to their supplied layout mappings, using the
   same extension implementation.

   **Review note:** The internal concept uses the supplemental Sphinx mapping
   described in :doc:`internal-interfaces`; the host type/link definitions remain
   authoritative.
   Invalid or incomplete models are covered by :need:`STV_SHR_036`. The shared method's
   schema is one possible input model, not a fixed schema for the extension.

.. shr:: Inspect object details on hover
   :id: STV_SHR_015
   :status: accepted
   :tags: feature_inspection, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner inspection interaction clarification 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall display a tooltip containing all information shown in the
   represented Need object's full documentation rendering when a reader hovers
   over its node, without requiring or offering tooltip field-selection
   configuration.

   **Acceptance criterion:** Hovering over a displayed node reveals a tooltip
   with the same information as the full rendered Need object, including its
   displayed metadata and body content, without navigating away from the
   traceability view or configuring a list of tooltip fields.

   **Widget scope clarification (owner, 2026-10-18):** Static rendered text,
   images and non-executable markup of third-party widgets are sufficient in
   MVP details; widget-specific JavaScript interaction remains on the original
   Need page. See :need:`STV_SWR_049` and :doc:`sources`. This clarification
   preserves baseline v1 history and does not waive STV's own interactions.

   **MVP scope clarification (owner, 2026-10-18):** For an external Need whose
   full body is not locally rendered, available metadata and the original-object
   link are sufficient, with a clear "Full details unavailable locally"
   indication. External pages need not be downloaded or cached. This explicitly
   agreed exception is recorded in :doc:`sources`; baseline v1 history is retained.

   **Remote-media clarification (owner, 2026-10-18):** Uncached remote
   embedded resources may be replaced by an unavailable-offline indication
   and an explicit original-resource link. Local bundled media remains
   available; automatic downloading is not required or permitted by this
   fallback. See :doc:`sources` and STV_REVIEW_007 in :doc:`concept-review`.
   This is an explicit scope amendment; baseline v1 history is retained.

   **Review note:** Keyboard access is covered by :need:`STV_SHR_034`; touch
   access is deferred beyond the initial release. Large tooltips are covered
   by :need:`STV_SHR_033`.
   "All information" refers
   to information displayed by the full Need rendering, not hidden internal data.

.. shr:: Open the original Need object in a new tab
   :id: STV_SHR_016
   :status: accepted
   :tags: feature_inspection, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner inspection interaction clarification 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall open the represented Need object's original documentation
   location in a new browser tab when a reader clicks its node.

   **Acceptance criterion:** Clicking a node opens the documentation page at the
   corresponding Need object in a new tab while preserving the original view's
   expanded and collapsed relationships in its existing tab.

.. shr:: Explore documentation offline
   :id: STV_SHR_017
   :status: accepted
   :tags: feature_distribution, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner offline and static hosting confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall make the generated traceability view usable offline from
   the built documentation files without network access or an application server.

   **Acceptance criterion:** With network access disabled, a reader opens the
   built HTML directly from disk, expands and collapses relationships in both
   directions, inspects node summaries and hover details, and opens a locally
   documented Need object in a new tab.

   **Review note:** Access to original documentation hosted outside the built
   documentation bundle depends on its availability; the owner agreed to retain
   external-object links without fetching/caching their destinations.

.. shr:: Explore documentation on static hosting
   :id: STV_SHR_018
   :status: accepted
   :tags: feature_distribution, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner offline and static hosting confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall make the generated traceability view usable when the built
   documentation is published on static hosting without an application server.

   **Acceptance criterion:** Serving only the generated documentation files from
   a static host allows a reader to expand and collapse relationships in both
   directions, inspect node summaries and hover details, and open the original
   Need documentation in a new tab.

.. shr:: Select how shared objects are displayed
   :id: STV_SHR_019
   :status: accepted
   :tags: feature_navigation, release_later
   :basis: owner
   :evidence: docs/sources.rst :: project owner shared object display selector request 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to select within the traceability view whether
   an object reached through multiple expanded branches appears as one shared
   node with its connections or as separate node occurrences for those branches.

   **Acceptance criterion:** With two expanded system requirements tracing to
   the same software requirement, the reader can select either one software
   requirement node connected to both system requirements or a separate
   occurrence for each branch, without rebuilding the documentation.

   **Review note:** Expansion state shall be preserved as specified in
   :need:`STV_SHR_021`. Separate occurrences expand independently as specified
   in :need:`STV_SHR_022`. They represent the same underlying Need object.

.. shr:: Default to shared nodes
   :id: STV_SHR_020
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner shared node default confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall initially select the shared-node display mode when a reader
   opens a traceability view.

   **Acceptance criterion:** Opening a view and expanding two branches that
   reach the same object displays one shared node with both connections without
   requiring the reader to change the display mode.

.. shr:: Preserve exploration when switching display modes
   :id: STV_SHR_021
   :status: accepted
   :tags: feature_navigation, release_later
   :basis: owner
   :evidence: docs/sources.rst :: project owner exploration state preservation confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall preserve the reader's expanded and collapsed relationships
   when switching between shared-node and separate-occurrence display modes.

   **Acceptance criterion:** After expanding multiple branches and leaving other
   relationships collapsed, the reader switches to the other mode and back.
   Previously expanded relationships remain expanded and previously collapsed
   relationships remain collapsed without the reader repeating navigation actions.

   **Review note:** In shared mode, independently expanded occurrences are
   combined as specified in :need:`STV_SHR_023`. Their independent states must
   remain recoverable when switching back without intervening navigation.

.. shr:: Explore separate occurrences independently
   :id: STV_SHR_022
   :status: accepted
   :tags: feature_navigation, release_later
   :basis: owner
   :evidence: docs/sources.rst :: project owner independent occurrence expansion confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to expand and collapse relationships on each
   separate occurrence of an object independently of its other occurrences.

   **Acceptance criterion:** With the same object visible in two branches in
   separate-occurrence mode, expanding or collapsing a relationship on one
   occurrence leaves the expansion state of the other occurrence unchanged.

.. shr:: Combine expanded traces in shared mode
   :id: STV_SHR_023
   :status: accepted
   :tags: feature_navigation, release_later
   :basis: owner
   :evidence: docs/sources.rst :: project owner union of expanded traces confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall display the union of relationships expanded on an object's
   separate occurrences when the reader switches to shared-node mode.

   **Acceptance criterion:** Given two occurrences of one object with different
   relationships expanded, switching to shared mode shows both sets of expanded
   relationships on one node. Switching back without intervening navigation
   restores each occurrence's previous independent expansion state.

   **Review note:** How navigation performed in shared mode updates previously
   saved independent occurrence states remains to be clarified.

.. shr:: Show cycles without repeating branches indefinitely
   :id: STV_SHR_024
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner cycle presentation confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall represent a relationship that returns to an object already
   on the current exploration path as a closing connection to that object in
   shared-node mode or a reference to its existing occurrence on that path in
   separate-occurrence mode, without creating a repeated branch for that return.

   **Acceptance criterion:** For relationships A to B, B to C and C to A,
   expanding the path through C shows the return to A in both display modes
   without adding another expandable occurrence of A on that path. The same
   behavior applies to a self-link and to traversing a relationship back to
   the preceding object using bidirectional navigation.

.. shr:: Preserve objects reached through other open paths
   :id: STV_SHR_025
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner overlapping path collapse confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall keep an object visible after a branch is collapsed if
   another open path from the starting object still reaches that object, and
   hide objects no longer reached by any open path, retaining the starting object.

   **Acceptance criterion:** In shared-node mode, two open branches reach a
   common object and its expanded descendants. Collapsing one branch leaves
   the common object and descendants visible through the other path. Collapsing
   the last path hides them. In separate-occurrence mode, collapsing one branch
   hides its unreachable occurrences while retaining occurrences reached through
   the other branch. A disconnected cycle does not keep its objects visible.

.. shr:: Require a valid starting ID
   :id: STV_SHR_026
   :status: accepted
   :tags: feature_integration, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner invalid starting ID confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall fail the Sphinx build when an embedded view omits its
   starting ID or supplies one that does not resolve to an existing Need object,
   with an error identifying the missing or unknown ID and the RST source
   location of that view.

   **Acceptance criterion:** Building a document containing a view with a
   nonexistent starting ID returns a nonzero exit code and reports that ID,
   the source filename and the location of the offending invocation.
   Omitting the starting ID also returns a nonzero exit code and reports the
   missing ID and the invocation's source filename and location.

.. shr:: Render valid traces despite unresolved targets
   :id: STV_SHR_027
   :status: accepted
   :tags: feature_integration, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner broken trace responsibility clarification 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall render the available Need objects and resolvable
   relationships when a trace references a nonexistent target, leaving broken
   trace validation and build failure to the host documentation build.

   **Acceptance criterion:** Given a valid starting object with both valid
   relationships and a relationship to a nonexistent target, view generation
   renders the available objects and valid relationships without raising an
   extension-specific build failure for the missing target. With host broken-link
   validation configured to fail, the overall build returns a nonzero exit code
   through that host validation.

   **Review note:** The host build must be configured to reject broken traces.
   A failed build's rendered output does not imply that publication succeeded.
   Unresolved targets are displayed as specified in :need:`STV_SHR_028`.

.. shr:: Identify unresolved trace targets in the view
   :id: STV_SHR_028
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner missing target placeholder confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall represent an unresolved trace target revealed through
   expansion as a clearly marked missing-object placeholder containing the
   referenced target ID and retaining the visible relationship to its source.

   **Acceptance criterion:** Expanding a relationship to a nonexistent target
   displays a placeholder showing the target ID, an explicit missing-object
   indication and its connection to the source object. The placeholder is
   distinguishable from a resolved Need object without relying on color alone.

.. shr:: Indicate objects without relationships
   :id: STV_SHR_029
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner empty relationship presentation confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall omit expansion controls for relationship types with no
   targets and display a "No related objects" indication on a node with no
   incoming or outgoing relationships.

   **Acceptance criterion:** A starting object with no relationships is visible
   with a "No related objects" indication and no expansion controls. An object
   with targets for only some relationship types offers expansion controls only
   for those types. An unresolved target counts as a target and can be revealed
   as the placeholder specified in :need:`STV_SHR_028`.

.. shr:: Distinguish artifact types by background color
   :id: STV_SHR_030
   :status: accepted
   :tags: feature_layout, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner artifact color clarification 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall use each artifact type's color from the host project's
   Sphinx-Needs ``needs_types`` configuration as its node background color,
   falling back to a built-in default color scheme for types without a
   configured color.

   **Acceptance criterion:** A view containing multiple artifact types assigns
   each node the background color configured for its artifact type. Changing
   a type's configured color and rebuilding updates that type's node backgrounds
   without a separate extension palette setting.
   With colors omitted for multiple types, those types receive consistent
   type-based colors from the default scheme while explicitly configured
   colors remain in use.

   **Review note:** The host model controls whether type colors are distinct.
   The built-in scheme requires no additional user configuration.

.. shr:: Mark artifacts that are not accepted
   :id: STV_SHR_031
   :status: accepted
   :tags: feature_layout, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner node border status clarification 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall display a red border around an artifact's node whenever
   the artifact's status is not among the accepted-status values defined by
   the input model, defaulting to ``accepted``, including when its status is
   missing or empty.

   **Acceptance criterion:** Nodes representing artifacts in ``draft`` and
   ``reviewed`` states have red borders; changing an artifact's status to
   ``accepted`` and rebuilding removes the red status border while retaining
   its artifact-type background color.
   With a replacement model defining ``approved`` as an accepted-status value,
   an artifact in that state has no red status border.
   Artifacts with missing or empty status values have red borders.

   **Review note:** Missing or empty status values count as not accepted,
   regardless of the configured accepted-status values.

.. shr:: Configure accepted-status values through the input model
   :id: STV_SHR_032
   :status: accepted
   :tags: feature_integration, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner accepted status mapping confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow the input model to define which artifact status values
   count as accepted for node-border styling, using ``accepted`` when no override
   is supplied.

   **Acceptance criterion:** Replacing the default acceptance mapping with one
   containing ``approved`` changes the status-based border styling accordingly
   without modifying the extension implementation.

.. shr:: Keep long tooltips readable within the browser window
   :id: STV_SHR_033
   :status: accepted
   :tags: feature_inspection, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner long tooltip behavior confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall keep tooltips within the visible browser window and allow
   readers to scroll through content that exceeds the available space while
   keeping the tooltip open as the pointer moves from its node into the tooltip
   and remains over either.

   **Acceptance criterion:** Hovering over a node near a window edge whose full
   content exceeds the available space displays a tooltip within the window.
   The reader can move the pointer into the tooltip and scroll to all its
   content without the tooltip closing.

.. shr:: Operate the view using the keyboard
   :id: STV_SHR_034
   :status: accepted
   :tags: feature_accessibility, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner keyboard access confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers using only the keyboard to expand and
   collapse traces, access and scroll object details, switch shared-object
   display modes, zoom and pan the view, and open original Need objects in new tabs, with a visible
   focus indicator identifying the currently focused control or node.

   **Acceptance criterion:** Without a pointing device, a reader can reach each
   listed interaction, perform it and move focus out of it. Details available
   on hover are also accessible and scrollable by keyboard, and focus remains
   visible throughout the workflow.

.. shr:: Distinguish incoming and outgoing trace controls
   :id: STV_SHR_035
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner directional trace controls confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall provide separate expansion and collapse controls for each
   nonempty incoming and outgoing relationship type on a displayed object,
   using the corresponding directional labels supplied by the input model.

   **Acceptance criterion:** For an object with both incoming and outgoing
   relationships of the same type, the reader sees separate labeled controls
   and can expand or collapse either direction without changing the other's
   expansion state. Replacing the model's directional labels changes the
   displayed labels without modifying the extension implementation.

.. shr:: Reject invalid or incomplete input models
   :id: STV_SHR_036
   :status: accepted
   :tags: feature_integration, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner model validation confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall fail the Sphinx build when its supplied input model is
   invalid or lacks required definitions, with an error identifying the affected
   model entry and the validation problem.

   **Acceptance criterion:** A model referencing an unknown layout category and
   a model omitting a required type mapping each cause a nonzero build exit code
   with an error identifying the problematic entry and the unknown or missing
   definition, rather than silently assigning a layout category.

   **Review note:** Required definitions must be specified when the input-model
   contract is defined. Explicit defaults, including the default color scheme
   and accepted-status value, are not missing required definitions.

.. shr:: Define additional ordered artifact levels
   :id: STV_SHR_037
   :status: accepted
   :tags: feature_layout, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner extensible layout levels confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow the input model to define additional artifact levels
   and their vertical order without modifying the extension implementation,
   using the agreed stakeholder, system requirement, system architecture,
   software requirement and software architecture hierarchy as the default.

   **Acceptance criterion:** A replacement model adds a hardware requirement
   level and specifies its position among the other levels. Expanding and
   collapsing traces displays hardware requirements at that position while
   preserving the model-defined order of the other levels.

   **Review note:** The ordering requirements in :need:`STV_SHR_009`,
   :need:`STV_SHR_010` and :need:`STV_SHR_011` describe the default hierarchy.
   Replacement models may define a different ordering. Test-case placement
   remains governed by :need:`STV_SHR_012`.

.. shr:: Explore multiple views independently on one page
   :id: STV_SHR_038
   :status: accepted
   :tags: feature_integration, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner multiple independent views confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow documentation authors to embed multiple traceability
   views on one RST page with individually specified starting IDs, each retaining
   independent expansion state and shared-object display-mode selection.

   **Acceptance criterion:** A built page contains two views with different
   starting IDs. Expanding or collapsing traces and changing the display mode
   in one view leaves the other view's starting object, expansion state and
   display-mode selection unchanged.

   **Review note:** Required for the initial release by owner decision.

.. shr:: Zoom the traceability view
   :id: STV_SHR_039
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner zoom and pan confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to zoom in and out of each traceability view
   without changing its expanded relationships or artifact-level ordering.

   **Acceptance criterion:** A reader increases and decreases the scale of an
   expanded graph using a pointing device or keyboard. Expanded relationships
   and relative artifact-level ordering remain unchanged, and other embedded
   views retain their own zoom settings.

.. shr:: Pan the traceability view
   :id: STV_SHR_040
   :status: accepted
   :tags: feature_navigation, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner zoom and pan confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to pan each traceability view to reach graph
   content outside its visible area without changing the graph's expansion state.

   **Acceptance criterion:** With an expanded graph extending beyond the view's
   visible area, a reader can bring its off-screen nodes into view using a
   pointing device or keyboard without collapsing branches. Panning one embedded
   view leaves other views' positions unchanged.

.. shr:: Support Firefox desktop
   :id: STV_SHR_041
   :status: accepted
   :tags: feature_compatibility, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner Firefox-only initial browser scope 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall support the agreed traceability-view interactions in the
   current stable desktop version of Firefox on Windows at the time of release
   verification.

   **Acceptance criterion:** The initial release's interaction acceptance checks
   pass in Firefox desktop on Windows for both HTML opened from disk and statically hosted
   documentation. Verification records identify the exact Firefox version and
   operating system used.

   **Review note:** Other browsers are outside the initial release's supported
   scope. Linux and macOS support are deferred beyond the initial release.

.. shr:: Support the initial documentation toolchain
   :id: STV_SHR_042
   :status: accepted
   :tags: feature_compatibility, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner initial toolchain confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall integrate with Sphinx 8.1.3 and Sphinx-Needs 8.2.0 using
   Python 3.10 or later.

   **Acceptance criterion:** With the specified Sphinx and Sphinx-Needs versions,
   documentation containing the extension builds successfully and its generated
   views pass the initial-release interaction checks. Verification records
   identify the Python versions actually tested, including Python 3.10.

   **Review note:** Broader Sphinx and Sphinx-Needs version compatibility is
   deferred. Python versions not actually tested must not be reported as verified.

.. shr:: Explore a bounded view of a large Needs project
   :id: STV_SHR_043
   :status: accepted
   :tags: feature_capacity, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner project size and view limit clarification 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall support traceability exploration in projects containing
   tens of thousands of Need objects while limiting each view to at most 200
   simultaneously displayed nodes.

   Every visible node occurrence shall count toward this limit, including
   separate occurrences of the same object and missing-target placeholders.

   **Acceptance criterion:** In a test project containing tens of thousands of
   Needs, a reader can explore relationships from a selected starting object,
   and no expansion causes an individual view to exceed 200 visible nodes.
   Two separate occurrences of one object count as two nodes, and each visible
   missing-target placeholder counts as one node.

   **Rationale:** The project may be large, while a view should remain small
   enough for readers to navigate meaningfully.

   **Review note:** The engineering measurement fixture is 30,000 Needs and
   90,000 edges; response-time/memory budgets will be agreed after first MVP
   measurements, per the recorded owner decision. Expansion limit handling is specified in
   :need:`STV_SHR_044`. Handling a display-mode switch that would exceed the
   limit follows :need:`STV_SHR_044`.

.. shr:: Explain expansions blocked by the node limit
   :id: STV_SHR_044
   :status: accepted
   :tags: feature_capacity, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner node limit handling confirmation 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall leave the view's graph and expansion state unchanged when
   a requested expansion would exceed 200 visible nodes and display a message
   explaining that the node limit has been reached and another branch must be
   collapsed before that trace can be expanded.

   **Acceptance criterion:** With 199 visible nodes, requesting an expansion
   that would add two nodes leaves the existing graph and expansion state
   unchanged and displays the limit explanation. An expansion reaching exactly
   200 nodes succeeds. No partial set of targets is shown for a blocked expansion.

   A requested display-mode switch that would exceed the limit shall likewise
   leave the current mode, graph and exploration state unchanged and explain
   that branches must be collapsed before switching.

   **Acceptance criterion for mode switching:** Switching to separate-occurrence
   mode when it would produce more than 200 nodes retains the current mode and
   graph and displays the limit explanation without discarding exploration state.



.. shr:: Reuse the host project's model definitions
   :id: STV_SHR_045
   :status: accepted
   :tags: feature_integration, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner MVP and integration decisions 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall reuse the host Sphinx-Needs project's artifact-type and
   relationship definitions, supplemented by replaceable layout-level and
   accepted-status mappings rather than a separately maintained complete model.

   **Acceptance criterion:** A host project supplies its existing type and
   relationship definitions and additional layout and acceptance mappings; the
   extension uses those definitions without requiring their duplicate entry.

.. shr:: Deliver a reusable installable Sphinx extension
   :id: STV_SHR_046
   :status: accepted
   :tags: feature_distribution, release_initial
   :basis: owner
   :evidence: docs/sources.rst :: project owner MVP and integration decisions 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall be available as a reusable installable Sphinx extension for
   integration into other Sphinx-Needs documentation projects.

   **Acceptance criterion:** A separate Sphinx-Needs project installs the packaged
   extension, enables it and builds an RST-embedded traceability view without
   copying implementation files from this repository.
