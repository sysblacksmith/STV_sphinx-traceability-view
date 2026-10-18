System elements
===============

Proposed product elements. Sphinx, Sphinx-Needs, the static host and browser are
external execution dependencies, not product components with invented internals.

.. syse:: Sphinx build integration
   :id: STV_SE_BUILD
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed

   Consumes host configuration, resolved Needs and doctrees; produces validated view invocations and portable graph/detail/runtime files. Runs only during documentation generation. **Source mapping:** proposed; no runtime implementation exists. See :ref:`STV_ADR_001` and :ref:`STV_ADR_002`.

.. syse:: Browser exploration runtime
   :id: STV_SE_BROWSER
   :status: accepted
   :tags: release_initial
   :basis: inferred
   :evidence: docs/architecture/decisions/STV_ADR_001_static_extension.rst
   :priority: unassigned
   :verification_state: not_assessed

   Consumes generated immutable data and rendered detail fragments; owns independent per-view state, layout, accessible interactions and viewport. Runs in Firefox on Windows with no service dependency. **Source mapping:** proposed; no runtime implementation exists. See :ref:`STV_ADR_001` and :ref:`STV_ADR_002`.

