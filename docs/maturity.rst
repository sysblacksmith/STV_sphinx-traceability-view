Project maturity
=================

This is the single location for the current project maturity summary and
links to its review and lifecycle evidence. Need ``:status:`` fields and ADR
status metadata remain authoritative for individual artifacts; the charts
below read those fields rather than duplicating them in prose.

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
All current requirements and elements are accepted. Historical review hashes
remain snapshots of their respective revisions.

Implementation has not started. Requirement verification remains not_assessed;
concept acceptance and documentation checks do not establish runtime results.
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
