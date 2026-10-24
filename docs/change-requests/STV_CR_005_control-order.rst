.. _STV_CR_005:

Draft relationship-control ordering
===================================

.. change_request:: Draft relationship-control ordering
   :id: STV_CR_005
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_005_control-order.rst
   :priority: unassigned
   :verification_state: not_assessed

   Record: ``STV_CR_005``. Sequence follows the originating request.

   .. rubric:: Owner request and scope

   On 2026-10-18 the owner requested conversion, analysis and correction of the new
   text ticket, continuing the authorized draft/smoke workflow. The normalized
   report is :need:`STV_PR_005`. Typographical and capitalization errors are corrected
   without changing intent. No release or requirement acceptance is implied.

   .. rubric:: Requirements and design

   New :need:`STV_SHR_051` is channeled directly into :need:`STV_SWR_055`, allocated
   to :need:`STV_SWE_RENDER`. No system requirement or system-architecture update
   is needed. Existing group identities, target sets, expansion/collapse semantics,
   directional labels and keyboard focus remain applicable.

   The renderer's ``orderedGroups`` helper classifies all targets using configured
   semantic levels before expansion. Wholly upward groups precede neutral groups,
   then wholly downward groups. Mixed directions, same-level, test-role and missing
   targets remain neutral; stable ties preserve existing host order. This disclosed
   policy avoids calling a mixed group exclusively parent- or child-directed and
   does not split the existing relation/direction controls. The same rule applies
   after expansion, so the collapse control remains in place.

   .. rubric:: Implementation and verification

   Source: ``frontend/src/render/groups.js`` and ``frontend/src/render/view.js``. Contracts and
   plans are maintained in :doc:`/internal-interfaces`, :doc:`/implementation-plan`
   and :doc:`/verification-plan`. No state/event/guard changes require a behavioral
   diagram update. Executable mappings remain in :doc:`/test-coverage`.

   Checks executed on 2026-10-18 (Europe/Berlin), Windows with Node 24.21.0,
   the existing project Python environments and installed Firefox/geckodriver:

   * ``node --test test/groups.test.js`` from ``frontend``: 2 passed. Covers both
     relationship directions, neutral edge cases, stable ties, graph immutability
     and replacement level mappings.
   * ``node build.js`` from ``frontend``: passed; packaged runtime bundle updated.
   * ``.venv-implementation/Scripts/python.exe -m pytest docs/test-scripts/test_browser.py -q
     -k control_order_smoke`` with ``STV_GECKODRIVER`` set: 1 passed, 12 deselected.
     The real project demo lists the upward derives-from control before the
     downward allocation control and retains order/state through expand/collapse.
   * ``scripts/check-coverage.py --strict``: passed, 65 system/software requirements,
     60 executable cases, no unmapped active requirements or unknown IDs.
   * Sphinx with ``-E -a -W --keep-going -q -b html docs docs/_build/html``: passed
     after correcting two RST underline lengths. Shared traceability/evidence
     validation and diff checks are the final documentation gates.
   * ``quick_validate.py`` passed for the updated ``problem-solver`` skill in the
     agents repository. Conversion now corrects user-prose typos, capitalization
     and obvious grammar while preserving meaning, technical values and provenance;
     a second typo-filled verbatim copy is required only when exact wording matters.

   :need:`STV_PR_005` is fixed with partial smoke verification. Requirements remain
   draft/not assessed; full regression, owner review and release work remain
   deferred. No product behavior beyond control presentation was changed.
