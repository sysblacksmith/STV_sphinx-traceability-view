Stakeholder requirements
========================

Draft stakeholder requirements from the project owner discussion on 2026-10-18.
Priorities and release allocations remain unassigned. See :doc:`review` for
assumptions, open questions and coverage limitations.

.. shr:: Embed a traceability view
   :id: STV_SHR_001
   :status: draft
   :tags: feature_integration
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow documentation authors to embed an interactive
   traceability view in an RST document within a Sphinx-Needs project.

   **Acceptance criterion:** An author embeds a view in an RST page, builds the
   project as HTML, and a reader can use the view on the resulting page.

.. shr:: Select the starting object
   :id: STV_SHR_002
   :status: draft
   :tags: feature_integration
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow documentation authors to select any existing Need
   object as the starting object of an embedded view by specifying its ID.

   **Acceptance criterion:** For each Need type in an agreed demonstration project,
   an embedded view seeded with an existing ID of that type displays that object.

.. shr:: Initially collapse traced objects
   :id: STV_SHR_003
   :status: draft
   :tags: feature_navigation
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall initially display the starting object with its related objects
   collapsed.

   **Acceptance criterion:** On first opening a view whose starting object has
   relationships, the starting object is visible and its related objects have not
   yet been revealed.

.. shr:: Offer expansion by traceability type
   :id: STV_SHR_004
   :status: draft
   :tags: feature_navigation
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall initially provide a plus-sign expansion control for each
   traceability type available on the starting object.

   **Acceptance criterion:** For a starting object with multiple traceability types,
   the reader can identify and activate a separate plus-sign control for each type.

   **Review note:** Whether types with no related objects also receive a control
   is unresolved, as is how incoming and outgoing relationships are distinguished.

.. shr:: Reveal related objects
   :id: STV_SHR_005
   :status: draft
   :tags: feature_navigation
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to reveal the objects related to a displayed
   object through a selected traceability type by activating its expansion control.

   **Acceptance criterion:** Expanding a type reveals the related objects for that
   type, with their relationship to the expanded object identifiable.

.. shr:: Continue exploration
   :id: STV_SHR_006
   :status: draft
   :tags: feature_navigation
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to continue expanding relationships from objects
   revealed during exploration.

   **Acceptance criterion:** In a demonstration with a path of at least three
   relationships, the reader follows the path by expanding each newly revealed
   object without changing the embedded starting ID.

   **Review note:** The intended outcome is exploration of the whole connected
   traceability structure. Directionality and treatment of cycles and shared
   objects require clarification before reachability can be fully specified.

.. shr:: Collapse opened traces
   :id: STV_SHR_007
   :status: draft
   :tags: feature_navigation
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to collapse previously expanded relationships
   interactively.

   **Acceptance criterion:** A reader expands a relationship, collapses it, and can
   expand it again.

   **Review note:** Visibility of descendants also reached through another open
   relationship remains to be defined.

.. shr:: Inspect discovered objects
   :id: STV_SHR_008
   :status: draft
   :tags: feature_inspection
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall allow readers to inspect a Need object revealed in the view.

   **Acceptance criterion:** After revealing an object, a reader can access its
   associated documentation content.

   **Review note:** Opening the original documentation, showing details within the
   view, or offering both remains undecided.

.. shr:: Preserve requirement levels
   :id: STV_SHR_009
   :status: draft
   :tags: feature_layout
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
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
   :status: draft
   :tags: feature_layout
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall position visible system architecture objects between the system
   requirement level and the software requirement level.

   **Acceptance criterion:** A view containing all three categories places the system
   architecture objects below system requirements and above software requirements.

.. shr:: Position software architecture
   :id: STV_SHR_011
   :status: draft
   :tags: feature_layout
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall position visible software architecture objects below the software
   requirement level.

   **Acceptance criterion:** Expanding traces to software architecture objects places
   them below visible software requirements.

.. shr:: Position test cases beside artifacts
   :id: STV_SHR_012
   :status: draft
   :tags: feature_layout
   :basis: owner
   :evidence: sources.rst - project owner discussion 2026-10-18
   :priority: unassigned
   :verification_state: not_assessed

   The system shall display test cases revealed through trace expansion to the right
   of the artifacts to which they are traced.

   **Acceptance criterion:** Expanding an artifact's test-case relationship displays
   the related test cases to its right, with the association identifiable.

   **Review note:** Placement of a test case shared by multiple artifacts remains
   undecided.


