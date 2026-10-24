Project Metrics
===============

Status charts read the canonical Sphinx-Needs records on each documentation
build. Counts describe recorded workflow status; they do not establish release
readiness. See :doc:`maturity` for review history and verification context.

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

Test-case maturity
------------------

Maturity describes review status (draft, reviewed, accepted), not execution
outcome, pass rate or verification state. Populations use the canonical
``test_system`` and ``test_software`` tags, independently of requirement links.

.. container:: requirement-status-charts test-case-status-charts

   .. container:: requirement-status-card

      **System test cases**

      .. status-pie:: test_case
         :tag: test_system

      **Total:** :need_count:`type == 'test_case' and 'test_system' in tags`

   .. container:: requirement-status-card

      **Software test cases**

      .. status-pie:: test_case
         :tag: test_software

      **Total:** :need_count:`type == 'test_case' and 'test_software' in tags`

Scope management status
------------------------

Problem tickets use their New / Analyzed / Fixed lifecycle. Change requests
use their canonical Draft / Accepted / Implemented Need status. These lifecycles
do not change requirement acceptance or verification results.

.. container:: requirement-status-charts scope-status-charts

   .. container:: requirement-status-card

      **Problem tickets**

      .. status-pie:: problem_report

      **Total:** :need_count:`type == 'problem_report'`

   .. container:: requirement-status-card

      **Change requests**

      .. status-pie:: change_request

      **Total:** :need_count:`type == 'change_request'`
