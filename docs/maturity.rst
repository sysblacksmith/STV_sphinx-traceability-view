Project maturity
=================

This is the single location for the current project maturity summary and
links to its review and lifecycle evidence. Need ``:status:`` fields and ADR
status metadata remain authoritative for individual artifacts; the charts
below read those fields rather than duplicating them in prose.

Current draft increment
-----------------------

The 2026-10-18 usability problem fixes are draft changes awaiting owner review.
See :doc:`requirement-changes/usability-problems` and :doc:`problems/index`.
User issue handover now uses first-class problem reports directly in
``docs/problems/``; the shared lifecycle/template update is recorded in
:doc:`requirement-changes/problem-report-handover`.
The fifth report's control-order fix is also a smoke-tested draft awaiting
owner review; see :doc:`requirement-changes/control-order`.
Changed requirements return to draft with verification not assessed. Smoke
checks do not replace full release verification or extend historical acceptance.

Current baseline
----------------

Stakeholder baseline v1 and its explicitly recorded scope amendments are
owner-accepted. The internal concept, including the starting-node amendment, is accepted
under owner-delegated concept review, rounds 1 through 3. ADRs 001, 002, 004
and 005 are current accepted decisions; ADR 003 is partially superseded by
ADR 005 with its unaffected choices retained. Findings STV_REVIEW_001 through
STV_REVIEW_009 are resolved. See the individual review records for assessed
Need links, authority, revision identities and evidence.

The owner accepted the starting-node stakeholder amendment and selected paged
project-root links. Concept refinement and round-3 review are complete; see
:doc:`requirement-changes/starting-nodes` and :doc:`concept-reviews/round-3`.
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
Project licensing and numeric performance budgets remain explicitly deferred;
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
   requirement-changes/starting-nodes
   requirement-changes/usability-problems
   requirement-changes/problem-report-handover
   requirement-changes/control-order
   problems/index
   test-coverage
   test-execution/index
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
