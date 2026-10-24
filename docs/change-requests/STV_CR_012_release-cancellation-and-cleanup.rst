STV_CR_012: Cancel release and close preparation findings
=========================================================

.. change_request:: STV_CR_012: Cancel release and close preparation findings
   :id: STV_CR_012
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_012_release-cancellation-and-cleanup.rst
   :priority: unassigned
   :verification_state: not_assessed

   .. rubric:: Owner request and authority

   Date: 2026-10-24. Source: owner request in this conversation, after the
   release-preparation commit ``17cafd9``.

   **Language-corrected request:** Cancel this release and fix the dependency
   redistribution findings first so the first release is clean. Reduce mentions
   of the actual release version to the places where it is needed, minimizing
   files changed during updates. Also perform acceptance review and regression
   testing for the fix. Do not start a new release yet; complete the fixes first.

   This authorizes product/documentation fixes within the existing obligations,
   regression validation and acceptance of clean changed design/test artifacts
   under concept review. It does not authorize a new release run, tag, push or
   publication. No stakeholder acceptance criterion is changed.

   .. rubric:: Scope and implementation

   * :need:`STV_PR_006`: compact full-content-hash detail assets, deduplication and
     a real nested Windows/file/HTTP/retry regression.
   * :ref:`STV_ADR_007`, source boundaries and previously draft inspector cases:
     substantive acceptance review with recorded source identities.
   * Bundled-dependency source/notices inventory and build guards, including
     compiled Guava/GWT, EMF and Xbase/Xtend families.
   * One maintained development version; derived package/Sphinx/runner metadata
     and an unversioned private frontend manifest. Historical version identities
     and pinned dependency versions remain untouched.

   See :doc:`../concept-reviews/round-8` and
   :doc:`../test-execution/maintenance-2026-10-24/index` for assessed artifacts,
   actual validation, failed-before-fix history and remaining release work.
