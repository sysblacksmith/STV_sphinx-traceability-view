System requirements
===================

System-level behavior, constraints and architecture allocation.

Executable criteria and retained results: :doc:`test-coverage` and
:doc:`test-execution/0.1.0-final/index`.

.. sysr:: Author and resolve embedded views
   :id: STV_SYS_001
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_001, STV_SHR_002, STV_SHR_026, STV_SHR_047, STV_SHR_048
   :allocated_to: STV_SE_BUILD

   The system shall resolve each RST view invocation against the completed
   host Needs collection and associate it with a unique view instance and all
   explicitly selected valid starting objects, or an artificial project-named
   root linked to the stakeholder requirements when no IDs are supplied.
   Any explicitly supplied unknown or host-hidden seed shall fail with the
   invocation source location.

   **Acceptance criterion:** Zero-, one- and multiple-ID invocations resolve
   independently. Zero IDs selects the project root; multiple valid IDs select
   every specified object. Any invalid explicit ID fails with the ID, filename
   and invocation location.

.. sysr:: Integrate the host data model
   :id: STV_SYS_002
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_014, STV_SHR_036, STV_SHR_045
   :allocated_to: STV_SE_BUILD

   The system shall obtain artifact and relationship definitions from the host project and validate supplemental layout and acceptance mappings before generating views.

   **Acceptance criterion:** Two differently named host schemas generate correctly mapped views without duplicate type definitions; an unknown level or missing required mapping fails with its entry path.

.. sysr:: Deliver a self-contained documentation bundle
   :id: STV_SYS_003
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: partial
   :derives_from: STV_SHR_017, STV_SHR_018
   :allocated_to: STV_SE_BUILD, STV_SE_BROWSER

   The system shall deliver all graph data, detail content and runtime assets required for exploration in the generated documentation bundle without a runtime service or network dependency.

   **Acceptance criterion:** The same output supports navigation and local-object inspection under file URLs with networking disabled and under static HTTP hosting.

.. sysr:: Expose the complete host trace graph
   :id: STV_SYS_004
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_006, STV_SHR_013, STV_SHR_027, STV_SHR_028
   :allocated_to: STV_SE_BUILD, STV_SE_BROWSER

   The system shall make authored relationships between non-hidden objects traversable in either direction while excluding host-hidden objects and incident links and preserving genuinely unresolved target identities and delegating broken-trace build failure to host validation.

   **Acceptance criterion:** A cross-document chain can be followed from either end; a missing target appears as a placeholder and host validation determines overall build failure.

.. sysr:: Preserve semantic layout
   :id: STV_SYS_005
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_009, STV_SHR_010, STV_SHR_011, STV_SHR_012, STV_SHR_037
   :allocated_to: STV_SE_BROWSER

   The system shall preserve the input model's ordered artifact levels and place revealed tests to the right of their associated artifacts independently of the starting object.

   **Acceptance criterion:** A software-seeded view reveals higher levels above it, an added hardware level respects its declared position, and shared tests remain right of every connected artifact.

.. sysr:: Provide original-object inspection
   :id: STV_SYS_006
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: partial
   :derives_from: STV_SHR_015, STV_SHR_016, STV_SHR_033
   :allocated_to: STV_SE_BUILD, STV_SE_BROWSER

   The system shall provide locally rendered Need information and its original documentation location for inspection, using available metadata, the original link and an unavailable-details indication for external Needs without locally rendered bodies.

   **Acceptance criterion:** A locally rendered object on another page has equivalent displayed metadata/body in hover or keyboard details and opens at its original anchor from file and HTTP URLs. An external object without a local body shows metadata, its original link and the unavailable-details indication; widget-specific script behavior is not required. Uncached remote embedded media uses the owner-approved unavailable-offline indication and explicit resource link, without automatic retrieval; local bundled media remains available.

.. sysr:: Isolate view sessions
   :id: STV_SYS_007
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_038
   :allocated_to: STV_SE_BROWSER

   The system shall isolate each embedded view's exploration and viewport state from other views on the same page.

   **Acceptance criterion:** Expanding, zooming and panning one of two views leaves the other unchanged.

.. sysr:: Bound exploration of large projects
   :id: STV_SYS_008
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_043, STV_SHR_044
   :allocated_to: STV_SE_BUILD, STV_SE_BROWSER

   The system shall expose the project graph for exploration while limiting each view to 200 visible node occurrences and committing only transitions that respect that limit.

   **Acceptance criterion:** A tens-of-thousands fixture remains explorable; a transition to 200 succeeds and one to 201 leaves prior state unchanged with an explanation.

.. sysr:: Deliver the reusable extension
   :id: STV_SYS_009
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_042, STV_SHR_046
   :allocated_to: STV_SE_BUILD

   The system shall provide an installable extension usable in a separate host project with Python 3.10+, Sphinx 8.1.3 and Sphinx-Needs 8.2.0.

   **Acceptance criterion:** A built wheel installs into a clean host environment and produces an embedded HTML view without copying repository implementation files.

.. sysr:: Support the initial execution platform
   :id: STV_SYS_010
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: passed
   :derives_from: STV_SHR_041
   :allocated_to: STV_SE_BROWSER

   The system shall support the initial release workflow in stable desktop Firefox on Windows.

   **Acceptance criterion:** All in-scope MVP interaction checks pass on recorded stable Firefox and Windows versions against file and static HTTP output.
