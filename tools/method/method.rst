Minimal requirements and allocation model
=========================================

.. method-version::

Purpose and limits
------------------

This is a small project-specific information model, aligned with the
traceability intent of Automotive SPICE 4.0, not an official VDA schema.
Links alone do not demonstrate agreement, consistency, feasibility,
implementation quality, verification coverage or process capability.
Requirements recovered from source start as review drafts, even when the
behavior is implemented.

Research starting point: `VDA Automotive SPICE
4.0 <https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf?trk=public_post-text>`__,
SYS.1, SYS.2.BP5, SYS.3.BP4, SWE.1.BP5, SWE.2.BP4 and Annex C.5. These
address stakeholder/system/software consistency and architecture
traceability. This model covers a subset of those concerns and includes
explicit requirement-to-test and test-to-execution traceability; it does
not constitute a complete verification or lifecycle model.

Workflow phases and documentation continuity
--------------------------------------------

Elicit stakeholder needs and establish source evidence before refining
system and software requirements, architecture and an
implementation-ready concept. Recover existing behavior from evidence
when an implementation already exists. Review concept consistency
separately from implementation and runtime verification. Acceptance
requires recorded owner authority, scope, date and artifact identity.
Preserve rejected and superseded history. Changed accepted artifacts
require review of their affected contracts and traceability. A passing
build alone establishes neither acceptance nor verification.

Record baseline amendments as change requests. Obtain explicit approval
of changed stakeholder obligations before internal refinement. Defect
correction preserves accepted intent; changed needs require a baseline
amendment. Explicitly authorized draft prototypes remain drafts until
reviewed. Limited smoke checks do not justify full verification claims.

Central maturity and review records
-----------------------------------

Centralize project maturity in ``maturity.rst`` under Miscellaneous,
including the current baseline, review/implementation/verification
readiness, and explicit deferrals. Place the nine generated status
charts on ``project-metrics.rst``, titled **Project Metrics**, under the
top-level **Scope management** group alongside **Change Requests** and
**Problem Tickets**, following the shared layout. Store each
concept-review round in its own RST file (for example
``concept-reviews/round-1.rst``), linked from that page or a stable
review index. Each round links assessed Needs using ``:need:`` and
documents/ADRs using ``:doc:``/``:ref:``, and records scope, authority,
artifact identities, findings, decisions and checks. Preserve historical
rounds; do not rewrite historical hashes to match later files.

Artifact sources retain their substantive requirements/design, origin
evidence and canonical Need/ADR status. Keep review acceptance evidence,
dated progress and lifecycle commentary in the central records, rather
than adding per-review paragraphs or evidence suffixes to every
artifact, repeating status counts in prose, or synchronizing maturity
summaries across chapters. A review-only update changes the central
records; change an artifact only for a real content, traceability,
origin-evidence or canonical-status change. Keep ADR replacement links
and the actual selected decision on the ADR; record
proposal/review/acceptance history centrally with ADR references.
Centralization must not omit acceptance authority or change verification
state.

Use stable, phase-neutral wording in artifact content from concept
development onward. For example, label source/module mappings
``Source:`` or ``Source mapping:``, without a ``Proposed`` prefix that
would later be removed solely because implementation has begun or
completed. Apply this equally to interface contracts, implementation
plans and other concept artifacts: use stable descriptions such as “MVP
software design contract”, “Distribution name” and “Product files and
responsibilities” from the outset. Do not add phase disclaimers such as
“not an implemented API”, “not existing implementation claims”, or
“accepted” merely to remove or replace them at the next phase. Record
acceptance and whether the design is implemented in the central
maturity/review records; artifact content alone is not implementation
evidence. Preserve canonical Need/ADR status fields.

Portable documentation and repository location
----------------------------------------------

Establish the canonical repository location early: inspect configured
Git remotes and prior owner answers first. If the GitHub URL is missing,
ask the owner for it or ask them to create the intended repository and
hand over its URL, including visibility/access constraints. Respect an
explicitly chosen alternative host or local-only project. Continue
independent work while this is pending; do not invent a URL or
create/publish a repository without authorization.

Write maintained README, setup, installation and handover instructions
with repository-relative paths, paths relative to a stated working
directory, or clearly named configurable placeholders. Do not embed
author-machine drive paths, home directories or absolute local file
links. Use canonical repository and release-page URLs for shared
downloads; keep general instructions version-independent, while
reproducible dependency/release selections pin actual versions where
needed. Explain placeholder substitution and private-repository
authentication without committing credentials. Do not claim a release
asset exists before publication; describe local build output as the
fallback. Preserve original paths in historical execution logs and
evidence where they identify the actual run. Check maintained
documentation for machine-specific paths before handover.

Published artifact source ownership uses plain repository-relative
naming references, not local filesystem hyperlinks or source-code
download roles. Follow the shared layout for architecture-owned
components, unit-test placement and the system/software test split.
Preserve published document/Need navigation and deliberately retained
execution-evidence attachments.

Nine types
----------

+-----------------------+-----------------------+-----------------------+
| Directive             | Meaning               | Suggested stable ID   |
+=======================+=======================+=======================+
| ``shr``               | Stakeholder outcome   | ``PRJ_SHR_001``       |
|                       | or constraint         |                       |
+-----------------------+-----------------------+-----------------------+
| ``sysr``              | Observable system     | ``PRJ_SYS_001``       |
|                       | behavior or           |                       |
|                       | constraint            |                       |
+-----------------------+-----------------------+-----------------------+
| ``swr``               | Software behavior or  | ``PRJ_SWR_001``       |
|                       | interface obligation  |                       |
+-----------------------+-----------------------+-----------------------+
| ``syse``              | System architecture   | ``PRJ_SE_BACKEND``    |
|                       | element               |                       |
+-----------------------+-----------------------+-----------------------+
| ``swe``               | Software architecture | ``PRJ_SWE_STORAGE``   |
|                       | element or            |                       |
|                       | responsibility        |                       |
+-----------------------+-----------------------+-----------------------+
| ``problem_report``    | User-reported issue   | ``PRJ_PR_001``        |
|                       | and its resolution    |                       |
|                       | handover              |                       |
+-----------------------+-----------------------+-----------------------+
| ``change_request``    | Owner request, scoped | ``PRJ_CR_001``        |
|                       | acceptance and        |                       |
|                       | implementation        |                       |
|                       | lifecycle             |                       |
+-----------------------+-----------------------+-----------------------+
| ``test_case``         | Repeatable            | ``PRJ_TC_SY_001`` /   |
|                       | verification          | ``PRJ_TC_SW_001``     |
|                       | procedure             |                       |
+-----------------------+-----------------------+-----------------------+
| ``test_execution``    | One actual execution  | ``PRJ_TE_001``        |
|                       | of one test case      |                       |
+-----------------------+-----------------------+-----------------------+

Logical software elements may reside in the same source file. External
dependencies may be modeled as system elements if their boundary and
lack of internal source are explicit; do not invent their internals.
File names and libraries are evidence or design, not automatically
requirements.

Five canonical relations
------------------------

+-----------------------+-----------------------+-----------------------+
| Link                  | Allowed direction     | Inverse generated by  |
|                       |                       | Sphinx-Needs          |
+=======================+=======================+=======================+
| ``derives_from``      | ``sysr -> shr``,      | ``derives_from_back`` |
|                       | ``swr -> sysr``,      | (refined by)          |
|                       | ``swr -> shr``        |                       |
|                       | (channeling)          |                       |
+-----------------------+-----------------------+-----------------------+
| ``allocated_to``      | ``sysr -> syse``,     | ``allocated_to_back`` |
|                       | ``swr -> swe``        |                       |
+-----------------------+-----------------------+-----------------------+
| ``part_of``           | ``swe -> syse``       | ``part_of_back``      |
|                       |                       | (contains)            |
+-----------------------+-----------------------+-----------------------+
| ``verifies``          | ``test_c              | ``verifies_back``     |
|                       | ase -> shr/sysr/swr`` | (verified by)         |
+-----------------------+-----------------------+-----------------------+
| ``executed_by``       | ``test_cas            | ``executed_by_back``  |
|                       | e -> test_execution`` | (execution of)        |
+-----------------------+-----------------------+-----------------------+

No parent links are authored on ``shr``. Read the hierarchy downward
using generated backlinks. Software-to-system-architecture trace is
composed through ``swr.allocated_to -> swe.part_of -> syse``; avoid
manually duplicating this path. Keep at least one allocated software
element within the system allocation of **each** parent system
requirement. Tables must expose these paths. In a software-realized
scope every SHR has a SYS child or a justified directly derived SWR
through channeling, every SYS a SWR child, every child has a parent and
every architecture element participates in an allocation. If another
domain is present, define and disclose an exception or extend the model.

Channeling stakeholder requirements directly to software
--------------------------------------------------------

**Channeling** permits a software requirement to derive directly from a
stakeholder requirement when that obligation has no system-level impact.
Author ``swr.derives_from -> shr``; the stakeholder-to-software
direction is provided by the generated ``derives_from_back`` relation.
This uses the existing canonical derivation relation, not a new link
type. Do not introduce an artificial system requirement solely to
complete the usual hierarchy.

Record the rationale for channeling in the software requirement,
explaining why no system-level obligation is needed. If a stakeholder
requirement also has system-level concerns, retain ordinary system
refinement for those concerns; channeling does not waive them. A
software requirement may have stakeholder and system parents where each
derivation is justified.

Channeled software requirements still require acceptance criteria,
evidence and allocation to software architecture elements. Their
allocated software elements retain the normal ``part_of`` containment in
system architecture. Parent-allocation consistency checks apply to
actual system-requirement parents, not to stakeholder parents, which
have no system allocation. Direct derivation establishes traceability,
not proof that a stakeholder requirement has been satisfied.

Traceability tables and CSV exports must expose direct SHR-to-SWR paths,
leaving the system-requirement cell empty rather than fabricating an
intermediate requirement. Coverage review must recognize a justified
direct SWR child as stakeholder refinement. In a fully channeled scope,
absence of system requirements is permitted when explicitly justified;
architecture allocation remains required. Review the no-system-impact
rationale semantically rather than inferring its validity from link
presence alone.

The shared graph validator accepts direct ``swr -> shr`` derivations and
checks allocation consistency only against actual system-requirement
parents. A system architecture element participates either through
directly allocated system requirements or through contained software
elements with allocated software requirements. Unused elements remain
errors. Fully channeled scopes may omit system requirements; the
rationale for doing so remains a semantic review item. CSV exports
include direct paths with an empty system-requirement cell, and
mixed-parent software requirements expose both direct and conventional
paths.

Problem-report intake and handover
----------------------------------

Use the canonical intake location, filenames, attachment placement and
index defined by the ``documentation-layout.rst``. Keep resolved reports
with their stable IDs and evidence; a filename does not determine
lifecycle state. Use one ``.. problem_report::`` Need per issue.
Informal text reports are valid intake: normalize them while preserving
meaning and source identity, rather than requiring users to know RST
first.

Report status uses exactly ``new``, ``analyzed``, ``fixed``:

-  ``new``: user handover recorded, analysis outstanding; do not invent
   a diagnosis.
-  ``analyzed``: cause or bounded diagnosis, impact, affected
   Need/document links and proposed disposition recorded;
   implementation/verification may be pending.
-  ``fixed``: the authorized fix is implemented and has linked, actual
   verification evidence at the agreed level. State remaining owner
   review, full regression or release work explicitly; a smoke-tested
   draft can be fixed without being an accepted requirement or approved
   release. Unresolved/failed evidence stays analyzed. A recurrence
   reopens fixed to analyzed with its history retained.

Reports use common ID/title, basis, evidence, priority and verification
fields; their body records reporter/date when known, observed and
expected behavior, reproduction information, original wording,
attachments, analysis, disposition and actual checks. Unknown details
remain unknown. ``verification_state`` describes the demonstrated
issue-resolution criteria at the agreed scope, independently of report
status; use partial for smoke-only evidence when complete criteria
remain. New reports start not_assessed. Do not automatically mark linked
requirements passed or accepted when a report is fixed.

Use ``:need:`` references in report bodies for affected
requirements/elements and ``:doc:`` links for design, changes and
results. Reports are outside the mandatory derivation/allocation
coverage graph: do not derive requirements from a report, allocate
reports as requirements or require every project to have a report. The
three canonical relations retain their existing allowed type pairs.
Changed intent is expressed in normal requirements with
report/change-record evidence. The shared validator enforces status by
type; the Sphinx status field enum is the union needed to serialize both
independent lifecycles. Requirement/element charts retain their three
review states; the report chart uses only its three states.

``problem-solver`` consumes this folder and returns analysis, changes
and evidence to the same records. ``manage-change``, concept
creation/review and implementation consume the linked impacts in their
authorized phase and hand results back to the report. Keep cross-cutting
review/release history central, referencing the report rather than
duplicating its original evidence.

Attributes
----------

Core: explicit ``id``, ``title``, ``status``, ``tags``. Extension
fields:

-  ``basis``: ``observed`` (code/configuration), ``documented``
   (existing prose), ``owner`` (explicit decision), ``inferred``
   (reconstructed purpose).
-  ``evidence``: repository-relative path plus symbol/section; or a
   named owner decision with date. Use multiple references when
   necessary.
-  ``priority``: ``unassigned`` until a responsible stakeholder assigns
   ``high``, ``medium`` or ``low``.
-  ``verification_state``: ``not_assessed`` until results justify
   ``passed``, ``failed`` or ``partial``.
-  ``last_result``: required on ``test_case``; see test execution rules
   below.
-  ``result``, ``executed_at``: required on ``test_execution``; see
   below.

These test-specific fields are not required on requirements or
architecture elements.

Requirements and architecture elements start at ``draft``; ``reviewed``
and ``accepted`` require actual review/agreement evidence. Problem
reports instead use ``new``, ``analyzed`` and ``fixed``; change requests
use ``draft``, ``accepted`` and ``implemented``. These record lifecycles
do not express acceptance or verification of linked requirements.
Requirements bodies contain the obligation, **Acceptance criterion**,
and relevant **Rationale**, **Existing checks** or **Review note**.
Elements contain boundary/responsibility and source mapping; they are
descriptive, without a shall obligation.

Test cases and execution history
--------------------------------

Model planned checks as ``test_case`` Needs with stable IDs and explicit
``verifies`` links to the requirements whose criteria they exercise.
Allocate canonical case IDs as ``<PROJECT>_TC_SY_001`` for system cases
and ``<PROJECT>_TC_SW_001`` for software cases (at least three digits).
Maintain independent numeric counters for SY and SW, shared across files
within that category. Use the next unused number in the category; never
reuse retired IDs or renumber cases merely after sorting, moving or
renaming documents. Classify by the actual verification boundary, not
the prefixes of linked requirements. A deliberate category change
requires an explicit ID migration and retained mapping. Do not derive
case IDs from hashes, executable names or descriptive suffixes. Existing
IDs remain stable unless the owner explicitly authorizes migration; then
retain an old-to-new map, update live references and preserve original
execution payloads, checksums and acceptance history. An ID-only
migration does not imply a new run or acceptance. Each case must verify
at least one requirement. This is many-to-many: a requirement may need
several cases and a case may cover several requirements. Record
preconditions, inputs, procedure or executable selector, expected
outcomes and criterion-level scope. Test cases use
draft/reviewed/accepted status independently of their results.

For each actual attempt, add a unique ``test_execution`` Need under the
existing release execution folder and link it using the case’s
``executed_by`` relation. An execution belongs to exactly one case; a
suite run has separate per-case records which may reference the same
report. Preserve earlier attempts, including failures and skips.
Execution status is ``recorded``; ``result`` is one of ``passed``,
``failed``, ``error``, ``skipped``, ``blocked``. Require ``executed_at``
as an ISO 8601 timestamp with timezone. Its evidence must identify the
retained report/log and case, candidate/source/test identity,
environment and actual invocation.

The test-case attribute ``last_result`` uses those same results plus
``not_run``. Initialize it to ``not_run`` without execution links, then
synchronize it with the uniquely latest linked execution by
``executed_at``, never by ID or file order. Use distinct timestamps to
order repeated attempts unambiguously. Do not replace historical results
when the implementation or test changes. The latest recorded result does
not prove a changed candidate passed; assess execution identity and full
criterion coverage before changing a requirement’s
``verification_state``. The common verification field remains
independent of test-case review status.

Early elicitation/reconstruction may leave test coverage pending and
cases unexecuted. During concept creation, develop and link concrete
test cases alongside their requirements; concept review includes these
cases and their criterion coverage in its inventory and acceptance
decision. Before declaring the current concept scope ready or accepted,
require explicit test coverage for every in-scope requirement using
``--require-test-coverage`` and semantic review. Unexecuted cases remain
``not_run``; product execution is not a concept gate. Before release
qualification is declared complete, every in-scope requirement must have
explicit ``verifies_back`` coverage and relevant actual execution
evidence. Include stakeholder acceptance checks at the appropriate
level; derivation links alone do not constitute test coverage. Review
coverage semantically, not merely by counting links. Run the shared
validator with ``--require-test-coverage`` on the qualification scope;
document explicit deferrals separately rather than inventing tests or
results. The ordinary validator permits early requirement-only models,
but always checks authored test/execution links, record ownership,
result values and latest-result consistency.

Example (common basis/evidence/priority/verification fields omitted for
brevity):

.. code:: rst

   .. test_case:: Reject an invalid input
      :id: PRJ_TC_SW_001
      :status: accepted
      :verifies: PRJ_SWR_001
      :executed_by: PRJ_TE_001
      :last_result: passed

      Preconditions, input, procedure and expected rejection behavior.

   .. test_execution:: Invalid-input check on candidate 1
      :id: PRJ_TE_001
      :status: recorded
      :result: passed
      :executed_at: 2026-10-19T12:00:00+00:00
      :evidence: docs/test-execution/candidate-1/pytest.xml :: test_invalid_input

      Actual candidate/test identity, environment and invocation.

Architecture design decisions
-----------------------------

Record significant system and software architecture choices as
Architecture Decision Records (ADRs). Capture choices that affect
boundaries, responsibilities, interfaces, technology, deployment,
persistence or quality trade-offs. An ADR explains why a design was
chosen; architecture elements describe the resulting structure, and
requirements state the obligations it must satisfy. Keep the nine Need
types and five canonical relations above unchanged: ADRs are ordinary
RST documents with stable labels, not an additional Need type.

Storage and traceability
~~~~~~~~~~~~~~~~~~~~~~~~

Store project ADRs in the documentation source under
``architecture/decisions/``. Use an ``architecture-decisions.rst`` index
titled **Architecture Design Decisions**, included in the
**Architecture** chapter’s toctree beside the system/software
architecture views, element pages and traceability tables. Its toctree
includes every ADR, including superseded and rejected records. Keep ADRs
in the authoritative source repository; the shared method defines their
format, not their project-specific content.

Use a stable, project-unique ID such as ``PRJ_ADR_001``, a filename such
as ``architecture/decisions/PRJ_ADR_001_browser_review.rst``, and an
explicit RST label such as ``.. _PRJ_ADR_001:``. Never reuse an ID or
renumber old records. The index lists records by ID/title. Each ADR
retains its canonical status, decision date, scope and replacement
links; maturity summaries and review/lifecycle history belong in the
central maturity/review records rather than a manually synchronized
status table.

Link related requirements and architecture elements using ``:need:``
references to their stable IDs. Use ``:ref:`` for ADR-to-ADR links and
references from architecture views or element descriptions back to the
relevant decision. Reference supporting source paths, specifications,
experiments or review records explicitly. These document references
supplement the canonical requirements graph; they do not replace
derivation, allocation or containment links.

Record contents
~~~~~~~~~~~~~~~

Each ADR contains the following design metadata and sections; the
questions/history entries below specify centrally linked records rather
than mandatory inline logs. State explicitly when information is unknown
or a section is not applicable; do not invent alternatives, approval or
rationale to complete a template.

-  **Metadata:** Stable ID and descriptive title; status; date in
   ``YYYY-MM-DD`` format; decision type/scope (system, software or
   solution architecture); decision owner when known (acceptance
   evidence is recorded centrally with an ADR reference); related
   specifications, requirement IDs and affected element IDs;
   supersedes/superseded-by links when applicable.
-  **Context:** The design problem, relevant stakeholder needs,
   constraints, quality drivers, assumptions and source baseline.
   Distinguish established facts from inferred motivations.
-  **Decision:** The selected approach and its boundary, including
   phased scope and deferred work. Make clear which parts of earlier
   decisions remain applicable.
-  **Rationale:** Why this approach addresses the context and decision
   criteria. Document the trade-offs rather than merely naming the
   chosen technology.
-  **Logical components and interfaces:** Affected responsibilities,
   boundaries, interactions and deployment/persistence implications,
   linked to the system/software element descriptions. Keep detailed
   architecture views in their own pages and reference them here.
-  **Consequences and constraints:** Benefits, costs, risks,
   operational/security implications and effects on requirements,
   implementation and verification. Record any required requirement
   refinement as follow-up work.
-  **Alternatives considered:** Plausible options actually considered,
   with their rejection or deferral reasons. Mark reconstructed
   alternatives as inferred.
-  **Open design questions:** Record unresolved questions and
   assumptions centrally with an ADR reference, owner and resolution
   criterion when known. The ADR retains the resulting design
   constraints; verification plans retain the actual planned checks.
-  **Decision history:** Keep dated proposal, review, acceptance and
   supersession events in central maturity/review records linked to this
   ADR. Preserve actual predecessor/successor links on the ADR.

Lifecycle and recovery
~~~~~~~~~~~~~~~~~~~~~~

Use ``proposed``, ``accepted``, ``rejected`` or ``superseded`` as ADR
statuses, independently of Need review statuses. A recovered design
choice starts as ``proposed`` unless existing records provide evidence
of another status. Code demonstrates an implemented approach, not
stakeholder acceptance or the original reasons for choosing it. Label
observed implementation, documented decisions, owner statements and
inferred rationale explicitly using the method’s evidence distinctions.

Acceptance requires a named decision owner or a referenced
approval/review record and date. Preserve genuine historical acceptance
when importing an existing ADR, citing the source; do not imply that the
current author obtained new approval. Open design details may remain in
an accepted ADR if their scope and consequences are explicit.

When an accepted choice materially changes, create a new ADR. Mark the
predecessor ``superseded``, add reciprocal replacement links and a dated
history entry, and retain its original context, decision and rationale.
Describe whether supersession is complete or partial. For example,
replacing a VS Code frontend with a browser frontend may leave a
UI-independent Python engine unchanged. A rejected proposal remains
available with its rejection rationale. Correct editorial errors with
history where needed; do not silently rewrite an accepted decision into
a different one.

An architecture decision does not silently change stakeholder
requirements. If the chosen design introduces a new obligation or scope,
refine the appropriate system/software requirements through their normal
review process and link the affected records. Resolve conflicts with
accepted requirements explicitly before treating the design as an agreed
baseline.

Documentation review
~~~~~~~~~~~~~~~~~~~~

During recovery, inspect existing ADRs and design notes alongside the
implementation. Record missing rationale or approval as gaps. During
documentation review, check unique IDs and labels, metadata, evidence,
valid requirement/element references, reciprocal supersession links,
absence of supersession cycles, and inclusion of all records in the
Architecture navigation. Check that current architecture views agree
with applicable accepted decisions and disclose any implementation
divergence. A successful Sphinx build or requirements graph validation
does not establish ADR acceptance or semantic consistency; review these
separately.

Recovery and quality review
---------------------------

1. Establish system boundary and source baseline. Inventory entry
   points, stores, processes, clients and external dependencies.
   Existing architecture pictures are navigation aids, not independent
   implementation evidence.
2. Recover stakeholder goals; mark inferred goals honestly. Translate
   capabilities into system outcomes before writing software detail.
3. Write atomic, testable software obligations. Preserve supported
   interface semantics and numerical thresholds, but distinguish current
   configuration from a justified product constraint. Do not convert
   every helper function into a requirement.
4. Link child to parent and allocate to evidenced elements. Check
   rationale, not merely nonempty links. Review contradictions and
   environment impact separately.
5. Name a practical acceptance criterion for every requirement. A test
   reference is supporting evidence, not proof it was executed or that
   the entire requirement passed.
6. Build and validate. Check typed endpoints, orphan/coverage rules,
   generated inverses, required metadata, element containment and
   allocation consistency. Review inferred intent, priorities, edge
   cases, missing nonfunctional budgets and unverified interfaces.

Use a separate gap list for unknown
timing/throughput/retention/reliability budgets, unclear security
policies, missing approval and absent tests. Never fill these gaps with
plausible numbers. The build may pass while these review decisions
remain open.

Sphinx reuse
------------

For new documentation projects, default to the Read the Docs theme
unless the user requests another theme or the project already has an
established theme. Add ``sphinx-rtd-theme==3.1.0`` to the pinned
documentation dependencies and configure:

.. code:: python

   extensions = ['sphinx_needs', 'sphinx_rtd_theme']
   html_theme = 'sphinx_rtd_theme'

Preserve any other required extensions. Avoid carrying over
theme-specific options from another theme. This combination was built
successfully with Sphinx 8.1.3 and Sphinx-Needs 8.2.0. Primary theme
setup documentation: `Read the Docs theme
installation <https://sphinx-rtd-theme.readthedocs.io/en/stable/installing.html>`__.

Use Python 3.10+, Sphinx 8.1.3 and Sphinx-Needs 8.2.0 for the tested
configuration. Import ``NEEDS_TYPES``, ``NEEDS_LINKS``, ``NEEDS_FIELDS``
from ``tools/method/tooling/traceability_model.py`` into conf.py. Enable
``sphinx_needs`` and ``needs_build_json``. Bind the shared model to the
Sphinx-Needs 8.2 configuration as follows:

.. code:: python

   from traceability_model import NEEDS_TYPES, NEEDS_LINKS, NEEDS_FIELDS

   needs_types = NEEDS_TYPES
   needs_links = NEEDS_LINKS
   needs_fields = NEEDS_FIELDS
   needs_build_json = True

``NEEDS_LINKS`` is a dictionary keyed by relation name. Use
``needs_links``, not the deprecated ``needs_extra_links`` option, which
expects a list and rejects this dictionary. Keep the central model
unchanged; adapt configuration to the pinned Sphinx-Needs API.

Version-specific primary documentation:
`configuration <https://sphinx-needs.readthedocs.io/en/8.2.0/configuration.html>`__,
`tables <https://sphinx-needs.readthedocs.io/en/8.2.0/directives/needtable.html>`__,
`JSON
export <https://sphinx-needs.readthedocs.io/en/8.2.0/builders.html>`__.

Build with
``python -m sphinx -E -a -W --keep-going -b html SOURCE OUTPUT``, then
run
``python tools/method/tooling/validate_traceability.py OUTPUT/needs.json --version VERSION --repo-root REPOSITORY``.
The latter also checks that evidence paths exist; it does not prove the
cited statements. Add ``--csv OUTPUT/traceability.csv`` for derived
requirement/allocation paths and
``--test-csv OUTPUT/test-traceability.csv`` for
requirement/test/execution paths, including uncovered requirements and
unexecuted cases. Run both commands in automation and preserve nonzero
exit codes. No diagram renderer or network is required for the build
after dependencies are installed.

Publish the method
------------------

Keep this complete method as a versioned local file in each consuming
project. A short Methods chapter includes the local RST file using
Docutils include tracking. Updates are explicit imports, reviewed and
committed with the project. Builds never discover another checkout or
fetch remote method content.

Documentation presentation
--------------------------

Use the accompanying documentation layout, local status chart extension
and local stylesheet. Preserve project-specific evidence and decisions
separately from imported files. All imports and static paths resolve
inside the project.

Build environment and failure reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prefer an existing project virtual environment when preparing build
commands or scripts (on Windows, ``.venv/Scripts/python.exe``); do not
assume that ``python`` or ``py`` selects it. Build scripts should
resolve paths relative to their own location, preserve failed
dependency-install and Sphinx exit codes, and make dependency
installation explicit. If the user asks to run the build themselves,
prepare the script without running the build.

When a build is authorized, run the actual pinned Sphinx toolchain with
warnings treated as errors. Correct configuration/deprecation warnings
and RST syntax warnings, including short heading underlines, rather than
suppressing them. Repeat after corrections and report success only on a
zero exit code. If execution is unavailable, state that the build
remains unverified. Keep full graph coverage findings separate from HTML
build results, especially for stakeholder-only drafts.

Architecture diagram authoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Author architecture diagrams as editable Draw.io ``.drawio`` sources and
export SVG only for publication. Keep each .drawio source and its
same-basename .svg export directly beside each other in the same project
directory; do not separate editable sources and exports into different
folders; regenerate SVG through Draw.io after source edits rather than
hand-editing exported SVG. Do not use raster architecture exports or
independently authored SVG diagrams. Status charts retain their existing
shared renderer.

Link every architecture element box to its Sphinx-Needs object using the
stable Need ID and generated document anchor. Link requirements shown in
diagrams likewise. External context or artifact boxes without a Need
record must not have fabricated targets. Keep URLs portable and relative
to the SVG’s published location; target the containing documentation
window where appropriate. Verify all link targets exist after the Sphinx
build.

Embed linked SVGs in HTML with an object or inline mechanism that
preserves clickable links; an ordinary image element disables SVG
interaction. Provide a direct SVG fallback link. Follow the shared
documentation layout for placement and width. Validate that Draw.io
exports retain the expected links, not just that the SVG file exists. If
Draw.io export is unavailable, report the blocker instead of
substituting a handwritten SVG.

Reproducing owner prompts
-------------------------

When reproducing owner prompts in documentation, correct typos,
spelling, capitalization and grammar while preserving meaning, scope,
technical identifiers and values. Label edited quotations as
language-corrected. Do not invent missing prompt text: distinguish
reconstructions and summaries from recovered quotations, and state their
evidence and gaps. Preserve exact code, logs and technical evidence;
retain verbatim prose only when explicitly requested or its exact
wording is material.

Shared project layout
---------------------

The ``documentation-layout.rst`` is authoritative for the target
directory tree, filename conventions, initialization timing, navigation
and migration rules used by projects. This method remains authoritative
for Need types, typed relations, IDs, evidence, lifecycle and
verification semantics; directory names do not introduce new Need types.

Change-request lifecycle and metrics
------------------------------------

Use one ``.. change_request::`` Need per canonical CR document, with the
stable ``<PROJECT>_CR_<number>`` ID, title, status, basis, evidence,
priority and independent verification_state fields. Preserve the
original request, date/provenance, scope, owner decisions, affected
Need/doc links and implementation context in its body. Use rubrics for
internal headings inside the Need. Preserve existing document filenames
and legacy RST labels during migration; canonical cross-links can use
``:need:``. Never invent missing owner wording or acceptance evidence.

CR status uses exactly **draft**, **accepted**, **implemented**. Draft
means recorded/proposed intent; accepted requires actual owner approval
of the agreed request; implemented requires completion of that agreed
work. Status does not accept linked requirements, establish full
verification or approve a release. Update the canonical Need status from
actual evidence and keep dated review/ implementation history centrally
in maturity/review. Existing historical prose and execution histories
remain unchanged during migration.

Change requests are optional scope-management records outside mandatory
requirement derivation/allocation, just like problem reports. Reference
affected Needs/documents in their bodies; do not use a CR as a
requirement parent, an architecture allocation or a test verification
target. The validator enforces their own status enum and rejects those
illegal typed relations. Missing status is invalid; do not invent an
Unclassified canonical state or parse prose.

Metrics has a Scope management status subsection with separate canonical
``problem_report`` (new/analyzed/fixed) and ``change_request``
(draft/accepted/implemented) pies and matching ``need_count`` totals.
Charts read exported Needs, not document metadata, filenames or Git
stashes. Existing projects without CRs remain valid and display the
no-data message/zero total. Ordinary release instructions belong in
maturity, not the CR register.

Default page metadata controls
------------------------------

Enable the local ``need_controls`` Sphinx extension with the shared rendering
setup described in ``documentation-layout.rst``. It supplies page-wide Collapse
all and Expand all buttons for Need metadata by default, while preserving Need
titles, bodies and individual disclosure controls.
