.. _STV_CONCEPT_REVIEW_003:

Concept review - round 3: starting nodes
========================================

Authority, baseline and scope
------------------------------

Date: 2026-10-18. Reviewer: the assistant acting under owner delegation.
The owner accepted the stakeholder amendment, then explicitly instructed
"thats right. go for it!" in response to the proposed concept-creation and
concept-review sequence. Scope: incorporate and review that amendment and
its affected dependency neighborhood in the existing concept; not product
implementation. Decisions and paging approval are recorded in
:doc:`../change-requests/STV_CR_002_starting-nodes`.

Input HEAD: ``6060b63856a879cab6f5321e53133df0fa1f9641`` with a clean worktree.
Prior rounds remain historical; this focused round reuses their evidence for
unchanged paths, libraries, contracts and diagram readability. It does not
claim a newly repeated full semantic review of every unchanged artifact.

Assessed Needs and semantic paths
----------------------------------

Stakeholder scope:

:need:`STV_SHR_001`, :need:`STV_SHR_002`, :need:`STV_SHR_003`, :need:`STV_SHR_007`, :need:`STV_SHR_014`, :need:`STV_SHR_025`, :need:`STV_SHR_026`, :need:`STV_SHR_034`, :need:`STV_SHR_043`, :need:`STV_SHR_044`, :need:`STV_SHR_045`, :need:`STV_SHR_047`, :need:`STV_SHR_048`.

System refinements:

:need:`STV_SYS_001`, :need:`STV_SYS_002`, :need:`STV_SYS_005`, :need:`STV_SYS_008`.

Software refinements:

:need:`STV_SWR_001`, :need:`STV_SWR_003`, :need:`STV_SWR_007`, :need:`STV_SWR_014`, :need:`STV_SWR_025`, :need:`STV_SWR_026`, :need:`STV_SWR_043`, :need:`STV_SWR_051`, :need:`STV_SWR_052`.

Changed software responsibilities:

:need:`STV_SWE_DIRECTIVE`, :need:`STV_SWE_MODEL`, :need:`STV_SWE_GRAPH`, :need:`STV_SWE_STATE`, :need:`STV_SWE_LAYOUT`, :need:`STV_SWE_RENDER`, :need:`STV_SWE_INSPECT`.

Containment and unchanged collaborating boundaries:

:need:`STV_SE_BUILD`, :need:`STV_SE_BROWSER`, :need:`STV_SWE_BUNDLE`, :need:`STV_SWE_DETAIL_BUILD`.

SYS 001 refines SHR 047/048 through optional/list invocation, source-located
validation and project entry metadata within BUILD. SWR 001/026 own directive
parsing/validation in DIRECTIVE; SWR 051 owns project metadata and synthetic
entry behavior in GRAPH/STATE/RENDER, covering its actual system parent's
build allocation through GRAPH. SWR 014 refines model replacement under SYS
002 and MODEL, rather than hard-coding stakeholder type names. Existing SWR
003/007/025 channel software-local initialization/collapse obligations directly
from SHR 003/007/025 to STATE; multiple roots do not require synthetic system
requirements. SWR 043 extends SYS 008 capacity validation across DIRECTIVE and
STATE. SWR 052 mixes software-local SHR 047 paging with the SYS 008 capacity
constraint and is allocated to STATE/RENDER within the browser boundary.
Each named parent/child, allocation and containment was read for meaning.

SHR 047 is covered by SYS 001 and SWR 051/052; SHR 048 by SYS 001 and SWR
001/003/025/026. Existing hidden-data, identity, semantic level, keyboard,
offline and capacity constraints remain applicable. The synthetic root is not
a Need, so Need-only ID/status/detail/link rules are not fabricated for it.
Paging applies solely to virtual root-entry links; it does not weaken ordinary
authored relationship expansion or create a new canonical relation type.

Findings and correction evidence
---------------------------------

.. _STV_REVIEW_010:

STV_REVIEW_010 - Project entry overflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: capacity/scope. Owner: project owner. State: resolved.
Evidence: one root plus more than 199 stakeholder entries cannot fit the
accepted 200-node cap. Rejecting the root group would prevent project-wide
entry navigation. The owner chose paging over rejection. Correction: clarify
SHR 047, add SWR 052 and define 50-entry pages with page-local exploration and
atomic cap/layout commit. Closure: all stakeholder IDs remain accessible across
pages; the root counts toward the cap and normal trace groups remain atomic.
The 0/1/50/51/199/200/201 fixtures are specified for implementation verification.

.. _STV_REVIEW_011:

STV_REVIEW_011 - Single-root contracts and historical decision conflicts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Category: cross-artifact consistency/identity. Owner: delegated reviewer.
State: resolved. Evidence: required single-ID syntax, one-root reachability and
omitted-ID failure remained in interfaces/implementation and the clarification
register; arbitrary synthetic IDs could collide with host Needs or accidentally
receive original-object/detail/status semantics. Correction: optional positional
list, deduplication, explicit-seed validation, tagged identity, project name
and stakeholder-role contract, separate root band, project-page commands and
real-Need-only inspection. Updated component responsibilities and verification
fixtures. Closure: re-read the complete parse-to-render path, error behavior,
page restoration and trace identities. ADR 005 partially supersedes ADR 003,
with reciprocal links; the older decision body and prior acceptance are retained.
Other boundary, bundle and dependency decisions remain unchanged.

Reviewed artifacts and outcome
--------------------------------

Accepted revised SYS 001 and SWR 001/003/007/014/025/026/043/051, new SWR 052,
and changed DIRECTIVE/MODEL/GRAPH/STATE/LAYOUT/RENDER/INSPECT responsibilities.
Unchanged Need acceptance is retained. All 48 stakeholder, 10 system and 52
software requirements plus two system/nine software elements are accepted.
ADR 005 is accepted under the recorded delegation; ADR 003 is partially
superseded, preserving its unaffected design and historical acceptance.

The affected author, model, graph/state, rendering, capacity and verification
contracts were substantively reviewed in :doc:`../internal-interfaces`,
:doc:`../implementation-plan`, :doc:`../architecture-software`,
:doc:`../elements-software`, :doc:`../verification-plan` and
:ref:`STV_ADR_005`. The existing diagram components and all connections still
match the design: initialization metadata follows existing MODEL/GRAPH/BUNDLE
paths and commands stay within STATE/LAYOUT/RENDER/INSPECT. No diagram geometry
or source link changed; prior visual evidence applies to identical bytes.
The current SVGs were visually inspected again; no routing defect was found.

Checks and limitations
-----------------------

Installed Docutils argument parsing was exercised for omitted, single,
multiple and repeated whitespace-separated arguments: four feasibility cases
passed. This tests the chosen host parser facility, not an implemented STV
directive. No dependency/version selection changed. Sphinx warnings-as-errors,
shared graph/evidence validation with CSV output, published diagram links and
source whitespace checks passed after the final status changes.

Runtime implementation and browser/state/geometry/packaging verification remain
pending; all verification_state values remain not_assessed. The tests in the
verification plan are planned checks. Project licensing, measured performance
budgets, later occurrence mode and broader platforms retain their explicit
deferrals. No concept blocker remains in this amendment's reviewed scope.

Content identities
--------------------

The following identify the accepted/retained artifact snapshot for this round.
The record itself is excluded from self-referential hashing. Files omitted
from the focused inventory retain earlier review evidence; central maturity
and amendment documents record workflow history rather than product behavior.

.. list-table:: Round 3 inventory
   :header-rows: 1

   * - Artifact
     - SHA-256
   * - ``docs/stakeholder.rst``
     - ``57ffda245ea5209802138ee849c1b3913805826f0853e0311492041198d5b524``
   * - ``docs/system.rst``
     - ``963a624ce089922887263548117a9947b2bef072ac96b4a1b64c742681de19b5``
   * - ``docs/software.rst``
     - ``c7db063d486cc3137bc37d53acb9fc9ec4adfe9ee4d906612eb8d4e2d44fb44b``
   * - ``docs/elements-software.rst``
     - ``0f9f9593ac5efacf01f71e1b0045ab8ded56f79215c8a5aa62922b35e040f26b``
   * - ``docs/elements-system.rst``
     - ``0a272985e0155f9b96a3f62103b6f4e05c718c7d4071f88ff82fc723f3760aff``
   * - ``docs/internal-interfaces.rst``
     - ``3fb69864b9ab1dcb3e67bce28fa9db5dd7d20960cb937826acf00283f0431dc5``
   * - ``docs/implementation-plan.rst``
     - ``705b8bfb13f23339e9bc4bde17c76ce67c4921d38db8f3ea070c2035c8a3208c``
   * - ``docs/verification-plan.rst``
     - ``776f7758b1ce20626ba2449ddae9c7bf7064325a2d3d6007101dcfc5f5792a38``
   * - ``docs/architecture-software.rst``
     - ``41fd9deb010b2d9b0584f3d4ec326144acfe6a25dfebe2c97e40790cca518618``
   * - ``docs/architecture-system.rst``
     - ``8962eb822058a272beeac4c909e6f9f1708b31d3e89504fa0a5389f05ee14a42``
   * - ``docs/architecture-decisions.rst``
     - ``1c645cde487937d3f0bacfc9aaf24b349d835d4632d58d212520ec3950e80cc5``
   * - ``docs/technology-stack.rst``
     - ``f8f4fcb3cc74e50c9e20e8d23fc30bb2a622a8a7d05b7e3c44d472099c0bd9db``
   * - ``docs/review.rst``
     - ``061ade0649318346d128256d258fc7742bd4428c7ffa9b2dc905bf6b386c0d42``
   * - ``docs/traceability.rst``
     - ``684b96d372e2dcd7642126225d7be9ea339411a979029036915e3ec168230bfb``
   * - ``docs/architecture/decisions/STV_ADR_001_static_extension.rst``
     - ``df61e6a0507bf2ca1f2a3da03bab841de2293323f91c6daf4d52f9c66ad41e91``
   * - ``docs/architecture/decisions/STV_ADR_002_portable_bundle.rst``
     - ``4a5e396b61e42daae49a976c6d9eb995ad04aceb6cdaae5badd77e397802f66d``
   * - ``docs/architecture/decisions/STV_ADR_003_state_layout.rst``
     - ``43a609ae6acd1c966a0698324c1f3170b6577731d84aaa563f8574811441e2d5``
   * - ``docs/architecture/decisions/STV_ADR_004_dependencies.rst``
     - ``03fc636b6ae2dbbba9e6393f8a481485a87867adfa630d90b5d0e0524bcb47b6``
   * - ``docs/architecture/decisions/STV_ADR_005_starting_nodes.rst``
     - ``37e9921deb1526b12f0b2fade1e1b99041f83e17ea291bfb393c5b653b5a6453``
   * - ``docs/architecture/diagrams/software-architecture.drawio``
     - ``a952999f9cef4df1996fd0611dd1212f036eda9c386edc605ba2d9a482eaa315``
   * - ``docs/architecture/diagrams/software-architecture.svg``
     - ``018b59cb2b49870f25f4ce98604ac37dd369f497fbdaa9325795efa334bf2b64``
   * - ``docs/architecture/diagrams/system-architecture.drawio``
     - ``511fae6bfbd5ed0d8dec26f4838b7933cc009bab147a9d0a6669db487c9b69a1``
   * - ``docs/architecture/diagrams/system-architecture.svg``
     - ``fe394549a5e26b06a7080389d26762fc30896ec9477daaf9ce6099a20f39d77d``
