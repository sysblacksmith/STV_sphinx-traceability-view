.. _STV_ADR_009:

STV_ADR_009: Resolve evidence rows before exploration
=====================================================

Status: **accepted**. Date: 2026-10-24. Scope: model, graph, layout and render.
Decision owner: project owner through :doc:`../../concept-reviews/round-10`.
Supersedes: partially :ref:`STV_ADR_008` for test-lane assumptions when classified
rows are configured. Superseded by: none. Legacy-role decisions remain applicable.

Context
--------

:ref:`STV_CR_013` requests nine vertical categories and stable verification-boundary
classification; the owner explicitly chose a fallback row for unclassified or
conflicting records. :need:`STV_SHR_012`, :need:`STV_SYS_005`,
:need:`STV_SWR_012`, :need:`STV_SWR_037`, :need:`STV_SWR_055`,
:need:`STV_SWR_058` and :need:`STV_SWR_061` define the paths.

Decision
---------

Keep the default five-type preset and explicit legacy test role compatible.
Add configurable levels_by_tag and one-hop level_from placements with optional
fallback_level. MODEL validates placement selectors, named levels and relation
names. GRAPH resolves visible published records in two passes: fixed/tag owners
then owner-derived records, using indexed complete relationships. Serialize
object.level and placement_fallback only for classified records. Ordinary fixed
objects and old schema-1 graphs remain compatible with type-level fallback.
LAYOUT and RENDER control ordering share resolved-level lookup. Classified test
cases/executions use ordinary rank rows and stable slots, not the legacy lane.

The project configures stakeholder, system, system_tests, system_executions,
system_arch, software, software_tests, software_executions, software_arch,
unclassified_tests, problems. Cases use test_system/test_software tags; executions
inherit through incoming executed_by links. Missing/conflicting evidence uses
the common fallback row, displayed as Unclassified test evidence. Problem reports
stay last, root stays above all rows and empty rows retain existing physical
spacing. Fixed/tag owners can supply one-hop classification. Chained/cyclic data
links use fallback (or strict mode if no fallback is configured), never recursive
inference. No ID prefix heuristic is used.

Alternatives and consequences
------------------------------

Visible-neighbor median inference reclassifies shared cases during navigation.
ID prefixes are project naming conventions, not host metadata. Duplicating host
Need types breaks existing schemas. A mandatory build error for ambiguous data
was offered; the owner chose fallback retention. The chosen additive contract
keeps generic type names and existing graph identity/links, at the cost of an
extra row when ambiguous records exist. Wrong model configuration remains an
error. No dependency, network service, manual dragging, later occurrence mode,
capacity change or new semantic relation is introduced.

Handover and checks
--------------------

Owners: :need:`STV_SWE_MODEL`, :need:`STV_SWE_GRAPH`, :need:`STV_SWE_LAYOUT`,
:need:`STV_SWE_RENDER`. Use :need:`STV_TC_SW_046`, :need:`STV_TC_SW_047`,
:need:`STV_TC_SW_048`, :need:`STV_TC_SY_061` plus legacy/PR013/packaging regression
cases. The model/graph/build error ownership remains transactional. Update the
software dataflow and build-state action diagrams, inspect standalone/embedded
exports, then warnings-as-errors Sphinx and full traceability/test-coverage checks.
