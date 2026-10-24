Project maturity
=================

This is the single location for the current project maturity summary and
links to its review and lifecycle evidence. Need ``:status:`` fields and ADR
status metadata remain authoritative for individual artifacts; the charts
below read those fields rather than duplicating them in prose.

Component source organization, 2026-10-24
-----------------------------------------

The owner requested direct software-element-to-code boundaries. The nine
existing elements now own matching component directories with sources, unit
tests and boundary READMEs; :doc:`elements-software` records the naming convention.
Cross-component checks remain in :doc:`test-scripts/index`. The public
extension setup and generated asset locations remain stable.

:doc:`change-requests/STV_CR_008_component-directories` records scope,
path migration and actual development verification. The source-organization
ADR (:ref:`STV_ADR_007`) and two new inspector case designs remain
proposed/draft pending review. This refactor does not update requirement
verification or supersede historical release execution results.

Requirement filenames and test levels, 2026-10-24
-------------------------------------------------

The owner requested explicit requirement filenames and a system/software split
of test specifications. See :doc:`change-requests/STV_CR_009_requirement-filenames-and-test-levels`.
Canonical requirement/test IDs, criteria, latest results and historical
execution records are retained. :doc:`test-cases/system-tests` contains
whole-tool checks; :doc:`test-cases/software-tests` contains component checks.
This organization does not infer new verification results or acceptance.

MIT licensing decision, 2026-10-24
----------------------------------

The owner selected MIT and supplied Henning Heikes as the copyright holder.
See :doc:`licensing` and :doc:`change-requests/STV_CR_011_mit-license`.
The repository license, package metadata and generated-view legal materials
are aligned. Third-party licenses remain separate; an ELK/GWT transitive-source
redistribution audit and employer/IP questions are not claimed resolved.
Historical release artifacts and verification states remain unchanged.

Current release increment
----------------------------------------

Method migration and requalification, 2026-10-19
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The owner requested migration to the shared test-case/execution model followed
by release qualification. :doc:`concept-reviews/round-7` accepts 81 concrete
case designs, covering all 120 requirements structurally. Seventy-six have
existing executables; four occurrence-mode procedures and the known long-path
regression remain planned and unexecuted. Existing requirement and architecture
acceptance is preserved.
The shared method now resolves from the renamed ``-agents`` repository.

This migration changes documentation and records. Product code is unchanged.
The known nested-Windows detail-loading report :need:`STV_PR_006` remains
analyzed and outside this migration's implementation scope. A passing existing
suite must not be described as resolving that report's acceptance criteria.
The requested full rerun passed all 76 executable cases (58 Python/browser and
18 JavaScript), with no failures/errors/skips, under Windows/Firefox 158.0 and
Python 3.10.9. See :doc:`test-execution/0.2.0-method-2/index`; the first attempt
and its corrected documentation assertions remain retained separately.

There are 152 new per-case execution records. All 76 executable cases now have
``last_result: passed``; the four later-mode cases and the known long-path
regression remain ``not_run``. The freshly rebuilt capacity fixture contains
30,000 Needs and 90,000 edges. Its unchanged identity was verified before reuse
for the rerun; both browser transports were exercised again.

Current verification for :need:`STV_SYS_003`, :need:`STV_SYS_006`,
:need:`STV_SWR_015`, :need:`STV_SWR_017` and :need:`STV_SWR_018` is partial
because the known nested-path detail-loading gap remains. Eight other system
and 50 delivered software requirements retain their passing disposition; four
later software requirements remain not_assessed. Requirement acceptance and
historical qualification evidence are preserved. Passing regression and method
gates do not establish new product-release readiness while this issue is open.

Prior v0.2.0 qualification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The owner approved the centered-layout and interactive-seed MVP and released
its stakeholder requirements on 2026-10-18. Concept review is complete in
:doc:`concept-reviews/round-6`: revised/new stakeholder requirements
003/047/052/053, software requirements 003/051/052/056/057, ADR 006 and their
affected contracts/diagrams are accepted. ADR 005 is partially superseded;
previous review snapshots remain historical. See
:doc:`change-requests/STV_CR_006_centered-layout-and-interactive-seeds`.

Full v0.2.0 qualification passed against candidate 5: 58 Python/browser and
18 JavaScript tests, with no failures/errors/skips, plus all packaging,
documentation, coverage, traceability and diagram gates. See
:doc:`test-execution/0.2.0-final/index` and :doc:`implementation-review`.
A collision defect found during release review is corrected and regression-tested;
new-tab navigation tests now wait for the actual destination. Ten system and
53 delivered software requirements are verified passed; four occurrence-mode
requirements remain not_assessed. Acceptance statuses are preserved. The
candidate is validated for owner release decision; external distribution still
requires the existing project-license decision. No publication is implied.

The owner approved the preceding usability stakeholder revisions on 2026-10-18
and delegated review and final implementation for v0.2.0. That internal concept
was accepted under :doc:`concept-reviews/round-4`; the subsequent amendment
has its own acceptance under round 6 and final verification in the record above.
See :doc:`change-requests/STV_CR_003_usability-problems` and :doc:`problem-tickets/index`.
User issue handover now uses first-class problem reports directly in
``docs/problem-tickets/``; the shared lifecycle/template update is recorded in
:doc:`change-requests/STV_CR_004_problem-report-handover`.
The fifth report's control-order fix is included; see
:doc:`change-requests/STV_CR_005_control-order`. Final verification remains independent
of concept acceptance; the previous smoke-only limit is superseded.

Previous baseline
----------------------------------------

Stakeholder baseline v1 and its explicitly recorded scope amendments are
owner-accepted. The internal concept, including the starting-node amendment, is accepted
under owner-delegated concept review, rounds 1 through 3. ADRs 001, 002, 004
and 005 are current accepted decisions; ADR 003 is partially superseded by
ADR 005 with its unaffected choices retained. Findings STV_REVIEW_001 through
STV_REVIEW_009 are resolved. See the individual review records for assessed
Need links, authority, revision identities and evidence.

The owner accepted the starting-node stakeholder amendment and selected paged
project-root links. Concept refinement and round-3 review are complete; see
:doc:`change-requests/STV_CR_002_starting-nodes` and :doc:`concept-reviews/round-3`.
The requirements and elements in that historical baseline were accepted. Historical review hashes
remain snapshots of their respective revisions.

The initial shared-identity MVP is implemented from clean input revision
``30aaba98776ecbe648558d278a985691d81bccb4`` under the owner's implementation
instruction on 2026-10-18. It includes the installable extension, offline
classic-script bundle, multiple seeds, paged project roots, semantic layout,
rich static details, original links and independent accessible viewports.

The stable candidate's executable suites passed. Its publication-only
documentation retest passed; the consolidated record is
:doc:`test-execution/0.1.0-final/index`. Initial system/software verification
fields are updated against those actual results and the criterion review in
:doc:`implementation-review`. Stakeholder verification and concept acceptance
remain independent; no owner release approval or external publication is implied.
Project licensing was subsequently resolved as MIT on 2026-10-24 (see
:doc:`licensing`); numeric performance budgets remain explicitly deferred;
separate-occurrence mode, touch and additional platforms are later scope.
Implementation checks are specified in :doc:`verification-plan`; scope decisions
and their original owner evidence remain in :doc:`review` and :doc:`sources`.

Requirement status
------------------

Status counts are calculated from the requirements on each documentation build.

.. container:: requirement-status-charts

   .. container:: requirement-status-card

      **Stakeholder requirements**

      .. status-pie:: shr

      **Total:** :need_count:`type == 'shr'`

   .. container:: requirement-status-card

      **System requirements**

      .. status-pie:: sysr

      **Total:** :need_count:`type == 'sysr'`

   .. container:: requirement-status-card

      **Software requirements**

      .. status-pie:: swr

      **Total:** :need_count:`type == 'swr'`

Architecture element status
---------------------------

.. container:: requirement-status-charts architecture-status-charts

   .. container:: requirement-status-card

      **System elements**

      .. status-pie:: syse

      **Total:** :need_count:`type == 'syse'`

   .. container:: requirement-status-card

      **Software elements**

      .. status-pie:: swe

      **Total:** :need_count:`type == 'swe'`

Review and lifecycle records
-----------------------------

.. toctree::
   :maxdepth: 2

   concept-review
   concept-reviews/documentation-reorganization
   change-requests/index
   problem-tickets/index
   implementation-review

Maintenance rule
----------------

Record project progress and maturity changes here. Give each concept-review
round its own RST file with linked assessed Needs and document/ADR references,
findings, decisions and check evidence. Preserve prior rounds as historical
snapshots. Artifact files contain their specification/design and canonical
status; do not append per-review progress paragraphs, review evidence to every
Need, or manually repeated status/count summaries throughout the site.
Review-only updates touch these central records; edit an artifact only when
its content, traceability, origin evidence or canonical status actually changes.

Implementation verification dashboard
------------------------------------------------------------

The table reads canonical fields; deferred occurrence-mode criteria remain
not_assessed. Executable definitions and results are linked from
:doc:`test-coverage` and :doc:`test-execution/0.1.0-final/index`.

.. needtable::
   :filter: type in ['sysr', 'swr']
   :columns: id;title;verification_state;tags
