Project maturity
=================

This is the single location for the current project maturity summary and
links to its review and lifecycle evidence. Need ``:status:`` fields and ADR
status metadata remain authoritative for individual artifacts; the charts
below read those fields rather than duplicating them in prose.

PRSA-005 clean publication remediation
--------------------------------------------------------------------------------

:need:`STV_PR_011` records the authorized fresh-tree publication fix and
:doc:`test-execution/prsa-005-fix/index` retains Sphinx cleanup and failure
preservation/rollback evidence. Only the inventoried ``docs/_build/html`` tree
is a publication input; previous output and diagnostics remain outside it.
The revised workflow/interface and new case designs await owner review.
Requirement verification is unchanged and no release is started.

PRSA-004 source archive remediation
--------------------------------------------------------------------------------

:need:`STV_PR_010` records the authorized source-archive boundary fix.
:doc:`test-execution/prsa-004-fix/index` retains the before-fix leaked-log
reproduction, passing actual-archive regression and offline rebuilt-wheel host
check. The revised packaging policy and new test design await owner review;
requirement verification is unchanged. No release is started.

PRSA-001 and PRSA-003 remediation
--------------------------------------------------------------------------------

The owner authorized historical licensing remediation and patched maintainer
tooling environments. :need:`STV_PR_008` and :need:`STV_PR_009` record scope,
implementation and checks. :doc:`licensing/historical/index` supplies the
historical supplement without changing archive bytes or Git history.
:doc:`test-execution/prsa-001-003-fix/index` records development compatibility
checks and current advisory results. The package runtime remains Python 3.10+;
documentation/test tooling requires Python 3.11+. Changed tooling documentation,
the supplement, new cases and refined offline bootstrap procedure await owner
review. No release is started.

PRSA-002 security fix awaiting owner review
-------------------------------------------

The owner authorized remediation of the detail transport-marker bypass.
:need:`STV_PR_007` links the affected interface and regression evidence in
:doc:`test-execution/prsa-002-fix/index`. New test designs and the interface
refinement await owner review. Prior acceptance history is retained; these
scoped development checks do not qualify a release or change requirement
verification fields. Later audit findings await individual proposal approval.

Release canceled; maintenance fixes accepted
------------------------------------------------

The owner canceled the release preparation and requested the underlying fixes,
version centralization, regression tests and acceptance review before another
release begins. See :doc:`change-requests/STV_CR_012_release-cancellation-and-cleanup`
and :doc:`test-execution/1.0.0-canceled`. The sole maintained version is now in
``src/sphinx_traceability_view/_version.py`` and identifies development work.
No replacement release is started.

The Windows-path report :need:`STV_PR_006` is fixed at its scoped regression
level. The pinned ELK compiled-dependency notice audit is complete; ADR 007,
the two inspector cases and the new path/build-guard case designs are accepted
under :doc:`concept-reviews/round-8`. Latest development outcomes are 79 passing
distinct cases (59 Python, 20 JavaScript); two capacity cases await future
release qualification. Existing requirement verification is not promoted.

:doc:`test-execution/maintenance-2026-10-24/index` retains before/after Windows
path evidence, development regressions and the dependency audit.
:doc:`concept-reviews/round-8` records the scoped acceptance review. Historical
release verification is preserved and does not qualify the changed inputs.

1.0.0 release preparation, 2026-10-24
-------------------------------------

The owner requested the first official GitHub release based on commit
``2960b25721df9eb727ae070317e4c2f4746bb909``. Version metadata is aligned at
1.0.0. The fresh :doc:`test-execution/1.0.0-candidate-1/index` records 78
passing executable cases (58 Python, 20 JavaScript), no failures/errors/skips,
Windows/Firefox file and HTTP capacity runs, isolated installed-wheel use,
artifact checksums and all supporting gates. All actual cases have new
execution links; prior attempts and acceptance states remain preserved.

:doc:`test-execution/1.0.0-candidate-1/qualification` records **incomplete final
qualification**: the nested Windows-path system case remains unexecuted,
ADR 007 and two inspector test designs still need acceptance review, and the
documented ELK/GWT redistribution audit remains open. Requirement verification
states are unchanged. Occurrence mode and other agreed limits remain visible.
No release commit, tag or publication is implied. The owner approved removal
of the 14 listed cache directories; all were removed. The post-release review
remains due when publication is known.

Component source organization, 2026-10-24
-----------------------------------------

The owner requested direct software-element-to-code boundaries. The nine
existing elements now own matching component directories with sources, unit
tests and boundary READMEs; :doc:`elements-software` records the naming convention.
Cross-component checks remain in :doc:`test-scripts/index`. The public
extension setup and generated asset locations remain stable.

:doc:`change-requests/STV_CR_008_component-directories` records scope,
path migration and actual development verification. The source-organization
ADR (:ref:`STV_ADR_007`) and two new inspector case designs were initially
proposed/draft; their scoped acceptance is now recorded in round 8. This refactor does not update requirement
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
