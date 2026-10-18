Concept review round 6: accepted centered-layout and seed-selection amendment
==========================================================================================

Authority and reviewed baseline
------------------------------------------------------------------------------------------

Date: 2026-10-18. Reviewer: Codex. After inspecting the MVP, the project owner
explicitly released its stakeholder requirements and requested completion of
concept acceptance; see :doc:`/sources`. This closes the inspection gate from
:doc:`round-5`. Input Git revision is
``e7a561cbf1e8706c784980eff8d24e299d4a9885`` plus the current uncommitted
release-preparation and amendment work. No commit, tag or publication is implied.

The reviewed baseline combines the unchanged accepted concept from :doc:`round-4`
with the complete amendment dependency neighborhood assessed in :doc:`round-5`.
The adjacent ``round-6-inventory.json`` records current content identities,
individual modeled artifacts and the shared method identity. Earlier inventories
remain snapshots. Current Needs outside this amendment retain their previous
acceptance; historical/deferred decisions are not silently promoted.

Accepted scope
------------------------------------------------------------------------------------------

* Owner-released stakeholder revisions: :need:`STV_SHR_003`,
  :need:`STV_SHR_047`, :need:`STV_SHR_052`, :need:`STV_SHR_053`.
* Reviewed software revisions: :need:`STV_SWR_003`, :need:`STV_SWR_051`,
  :need:`STV_SWR_052`, :need:`STV_SWR_056`, :need:`STV_SWR_057`.
* :ref:`STV_ADR_006` is accepted; :ref:`STV_ADR_005` is partially superseded
  for page size, initial project expansion and runtime seed mutability. Its
  unaffected decisions remain applicable, with reciprocal replacement links.
* Affected :doc:`/architecture-software`, :doc:`/internal-interfaces`,
  :doc:`/implementation-plan`, :doc:`/verification-plan`,
  :doc:`/state-machine` and its adjacent Draw.io/SVG pair are accepted.
  Existing owners :need:`STV_SWE_STATE`, :need:`STV_SWE_LAYOUT` and
  :need:`STV_SWE_RENDER` within :need:`STV_SE_BROWSER` remain sufficient.

Review coverage and closure
------------------------------------------------------------------------------------------

Structural and semantic review follows the four stakeholder obligations through
their software refinements and actual component responsibilities. SWR 003
implements the initial-collapse exception; SWR 051/052 combine project identity,
five-entry pages and the existing capacity contract. SWR 056/057 directly refine
SHR 052/053 because placement and local selection add no system interface,
deployment service or host schema. :need:`STV_SYS_001`, :need:`STV_SYS_008`,
:need:`STV_SWR_038`, :need:`STV_SWR_043`, :need:`STV_SWR_044` and
:need:`STV_SWR_048` continue to constrain embedding, isolation, capacity,
transactional failure and shared identity. No artificial system requirement is
needed. Existing system architecture, build interfaces and technology choices
retain their previously reviewed scope.

Completeness review covers empty entry/catalog cases, short/final pages,
cross-page expansion memory, hidden objects, exact confirmation versus typing,
independent views, replacement/overview reset, focus and layout rejection.
Centering uses visible lower-level spans, ignores test/same-rank connections,
retains shared children and prioritizes nonoverlap. Bounded semantic-rank passes
avoid recursive layout of cycles. ELK ordering, collision resolution, test lanes
and final obstacle-safe routes agree across ADR, interfaces, plan and runtime.
No new dependency, runtime request, license or packaging decision is introduced.

Finding **STV_REVIEW_014** (resolved): SWR 057 grouped stale completions with
errors requiring a diagnostic. A superseded completion must not overwrite a
newer request's state or diagnostic. Clarified this internal requirement to
discard stale results while invalid input/failed layout retains actionable
diagnostics. This preserves the released stakeholder intent and matches the
state-machine table and request-token contract. Closure: all three now agree.

ADR supersession and current maturity/verification/demo text were reconciled
with the owner's approval; round 5 and historical execution records are retained.
Rendered architecture and state-machine SVGs and their embedded pages were
inspected during the amendment and rechecked at acceptance. No unresolved
concept blocker remains. Numeric performance budgets, occurrence mode, touch,
additional platforms and the external-distribution license decision retain
their recorded deferrals.

Checks and disposition
------------------------------------------------------------------------------------------

Acceptance checks: Sphinx full HTML build with warnings as errors; shared
traceability validation; source/published diagram-link validation; strict
requirement/executable coverage inventory; publication/diagram browser smoke.
All acceptance checks passed: Sphinx returned zero warnings/errors; traceability
validated 53 stakeholder, 10 system and 57 software requirements, two system
and nine software elements, and five independent problem reports. All three
diagram source/export pairs and published targets passed link checks. Strict
coverage found 67 requirements and 68 executable cases, no unmapped active
requirements and no unknown IDs. Firefox ``test_documentation_visuals`` passed
(one case, 16 deselected); all three SVG exports and their embedded publication
views were inspected. These are acceptance/publication checks, not a new full
runtime qualification. Prior focused MVP
results remain in :doc:`/requirement-changes/centered-layout-and-interactive-seeds`.

The listed requirement revisions and ADR 006 are accepted under explicit owner
authority. Ordinary documents/diagrams are accepted at their inventory identities.
No verification field is changed by concept acceptance. Full v0.2.0 release
qualification, complete criterion review and a new consolidated execution record
remain required before claiming a verified release. The failed
``0.2.0-candidate-1`` is retained unchanged.
