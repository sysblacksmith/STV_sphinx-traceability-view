.. _STV_CR_013:

STV_CR_013: Vertical target levels for artifacts and test records
=======================================================================

Owner request and provenance
------------------------------------

Date: 2026-10-24. Status: implemented and development-verified after delegated concept review.

**Language-corrected owner request:** Create a change-request RST file for the
new target levels depicted in ``STV_CR_013_artifact_vertical_target_position.pptx``.
Ensure that test cases and other artifacts align beneath one another in this
vertical order.

Evidence: the target-level diagram below and the owner's request in this
conversation. The adjacent file
``STV_CR_013_artifact_vertical_target_position.pptx`` is retained as backup
source material.

.. figure:: STV_CR_013_artifact_vertical_target_position.svg
   :alt: Top-to-bottom order: stakeholder requirement, system requirement, system test case, system test execution record, system architecture element, software requirement, software test case, software test execution record, software architecture element.
   :width: 360px
   :align: center

   Requested vertical target levels for artifacts, test cases and execution records.

Requested behavior
--------------------------

Use the following top-to-bottom target order. Artifacts in the same target
level occupy a common horizontal row; different target levels appear beneath
one another, with test cases and execution records integrated into this vertical arrangement.

.. list-table:: Requested vertical target levels
   :header-rows: 1
   :widths: 10 45 45

   * - Order
     - Artifact category
     - Position relative to adjacent categories
   * - 1
     - Stakeholder Requirement
     - Above System Requirement
   * - 2
     - System Requirement
     - Below Stakeholder Requirement; above System Test Case
   * - 3
     - System Test Case
     - Below System Requirement; above System Test Execution Record
   * - 4
     - System Test Execution Record
     - Below System Test Case; above System Architecture Element
   * - 5
     - System Architecture Element
     - Below System Test Execution Record; above Software Requirement
   * - 6
     - Software Requirement
     - Below System Architecture Element; above Software Test Case
   * - 7
     - Software Test Case
     - Below Software Requirement; above Software Test Execution Record
   * - 8
     - Software Test Execution Record
     - Below Software Test Case; above Software Architecture Element
   * - 9
     - Software Architecture Element
     - Below Software Test Execution Record

The slide uses a single vertical stack to express the category order. This
record does not impose identical horizontal coordinates on every node in a
branching graph or prescribe pixel offsets, row spacing or a layout algorithm.
Existing nonoverlap, identity and navigation constraints remain relevant.

Proposed acceptance criteria for stakeholder refinement
---------------------------------------------------------------

* A demonstration containing all nine categories displays their rows in the
  order above. No visible node occupies a different category's target row.
* System and software test cases occupy their respective test rows rather than
  relying solely on placement to the right of the artifacts they verify.
* System and software test execution records occupy their respective execution
  rows directly below the corresponding test-case category and above the
  corresponding architecture category. Multiple executions of one test remain
  individually identifiable and linked to their actual test case.
* Multiple visible objects in one category align on that category's row without
  overlapping. Relationship edges continue to identify their actual endpoints.
* Expanding and collapsing relationships preserves the relative vertical order
  of the visible categories, including entry from a software requirement, test
  case or test execution record. An absent category does not reverse the remaining categories' order.
* A test case linked to multiple requirement levels retains its verification
  boundary classification; the requirement it verifies alone does not silently
  reclassify the test or cause it to alternate between rows during exploration.

These original proposal criteria are now refined by the accepted canonical
requirements and review in :doc:`/concept-reviews/round-10`. Actual development
results are retained in :doc:`/test-execution/cr013-rows/index`.

Affected baseline and downstream contracts
-------------------------------------------

* :need:`STV_SHR_009`, :need:`STV_SHR_010` and :need:`STV_SHR_011` retain
  ordinary category order with test-case/execution rows inserted between them.
* :need:`STV_SHR_012` replaces the project's mandatory side lane with classified
  rows and owner-selected fallback. Prior acceptance is retained in earlier
  review rounds; explicit legacy-role models remain compatible.
* :need:`STV_SYS_005`, :need:`STV_SWR_012` and :need:`STV_SWR_037` define
  same-row alignment and resolved rank ordering. :need:`STV_SWR_061` owns
  configurable build-time classification and fallback handling.
* :need:`STV_SWE_MODEL` / :need:`STV_SWE_GRAPH` validate and resolve placement;
  :need:`STV_SWE_LAYOUT` / :need:`STV_SWE_RENDER` consume it for geometry,
  directional controls, fallback labels and stable navigation.
* :doc:`/internal-interfaces` defines additive object-level serialization and
  the tag/owner selectors. :doc:`/verification-plan` and the canonical system/
  software test specifications define observable criterion coverage.

Extensible ordered levels, hidden-object exclusion, shared identity, visible
capacity, compatible child-span centering and independent views are retained.
Later occurrence behavior remains separately deferred.

Resolved scope and concept decisions
--------------------------------------

* Configurable tag maps classify cases; one-hop incoming executed_by links
  classify executions from their cases, independently of current visibility.
* The owner explicitly chose a common fallback row for missing/conflicting
  evidence. It appears below Software Architecture and above Problem Tickets;
  nodes are labelled Unclassified test evidence and retain all interactions.
* Fixed/tag owners support execution classification. Invalid configuration
  fails early; chained/cyclic or unresolved record links use the configured
  fallback rather than recursive inference. Strict mode is available by
  omitting fallback_level.
* Problem Tickets retain the final custom row; project root remains above all
  rows. Empty configured levels retain physical spacing. No additional domain
  type or canonical relation is invented.
* Fixed-level and explicitly selected legacy test-role models stay compatible;
  the project's model uses the nine-category arrangement. Shared identity,
  routing, cap, offline delivery and PR013 stable navigation are retained.
* Later occurrence mode remains deferred; no release is initiated here.

Concept and implementation completion
--------------------------------------

:ref:`STV_ADR_009` and :doc:`/concept-reviews/round-10` record scoped acceptance,
partial supersession, the four concrete test designs and implementation feedback.
:doc:`/test-execution/cr013-rows/index` retains 134 distinct passing tests:
model/graph, 30,000-record classification, frontend geometry/controls, Firefox
file/HTTP, clean-package/source-archive and 200-visible-node capacity checks.
The normal documentation and its embedded demo are rebuilt with the new model.
No commit, tag or release is created by this work.
