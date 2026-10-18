Review and open questions
=========================

Working assumptions — not agreed requirements
------------------------------------------------------------

- The extension consumes the host project's Needs and traceability relations.
- Exploration is a reading activity; editing Needs is outside the current draft.
- Engineering levels refer to semantic categories rather than the distance from
  the starting object. Unrevealed ancestors need not be displayed automatically.
- “Tree” describes the exploration experience; the underlying relationships may
  include shared targets and cycles.

Open questions
--------------

1. Can readers follow both outgoing and incoming relationships from every object,
   including navigating upward from a software requirement to its system and
   stakeholder requirements?
2. Must the extension support arbitrary project-defined Need types and link types,
   with configurable mapping to layout levels, or a fixed schema initially?
3. Does inspecting an object mean opening its documentation, viewing details in
   place, or both?
4. Must the built HTML work offline and on static hosting without an application
   server?
5. How should shared objects, cycles, and collapse of overlapping paths behave?
6. What should authors/readers see for a missing starting ID, broken relationship,
   or an object with no relationships?
7. Which browsers, Sphinx/Sphinx-Needs versions, accessibility needs, graph sizes,
   and response-time targets must the first release support?

These questions are not additional obligations. Resolve them iteratively rather
than assigning unsupported defaults or performance numbers.

Method and coverage
-------------------

This stakeholder-only draft follows the shared stakeholder elicitation method.
No system/software refinement, architecture allocation, implementation decisions,
formal acceptance, or verification results are claimed. The shared documentation
model defines five artifact types but no test-case type; the extension's handling
of host-project test types and links needs an explicit mapping. No change to the
shared model is implied by the requested visualization.

Revision history
----------------

- 2026-10-18: Initial draft from the project owner's description. Created stable
  IDs STV_SHR_001 through STV_SHR_012. All requirements remain drafts; priorities
  and release allocations remain unassigned.

- 2026-10-18: Converted the initial Markdown draft into canonical RST Needs, preserving all 12 IDs; added the shared-method documentation structure.

