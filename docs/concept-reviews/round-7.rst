Round 7: Test-case and execution traceability migration
================================================================================

Authority and boundary
----------------------

On 2026-10-19 the project owner invoked concept-creation and concept-review to
rework STV to the updated shared method, authorized necessary file changes and
requested autonomous completion followed by release qualification. This delegates
review and acceptance of clean concept artifacts under the invoked workflow;
it does not approve a commit, tag or publication.

Input revision: ``77354cc578d23a5430b75df8c47ba34c1b7a0341``. Product behavior,
requirements, architecture boundaries, technology choices and ADR decisions are
unchanged. Existing concept acceptance is preserved against its historical
records. This round reviews the new verification design and its consistency
with all existing requirement criteria, allocations and release scope.

Creation and review scope
-------------------------

The canonical :doc:`../test-cases/index` contains 76 executable procedures,
four planned occurrence-mode acceptance procedures and a planned nested-Windows
regression preserving the known :need:`STV_PR_006` gap. Each executable case keeps
its exact collected selector, parameter variant, source procedure and observable
assertions. Shared cases cover several requirements without duplicating the
test implementation. The migration mapping is retained as
:download:`round-7-test-map.json <round-7-test-map.json>`. The one-time
``migrate-test-traces.py`` and ``finalize-method-qualification.py`` helpers
were removed after the completed migration. Their implementations remain in
Git history; historical inventories retain their original paths and hashes.
The reusable result importer, canonical cases and execution evidence remain.

Every stakeholder, system and software requirement has direct test-case
coverage. Executable links identify the criterion portions exercised, not
automatic full-requirement pass claims. Full criterion review uses the case set
together with :doc:`../implementation-review` and :doc:`../verification-plan`.
The four later-mode cases specify occurrence selection, independent expansion,
state restoration and merged expansion sets, with cycles and capacity rejection.
They remain unexecuted; no product implementation is added or inferred.

Semantic review and findings
--------------------------------------------------------------------------------

* Host/model cases exercise seeded and project-root collection, hidden/invalid
  IDs, mapping and palette defaults, alternate schemas and source diagnostics.
  Parameter variants preserve the boundary inputs rather than hiding them in
  a generic test-group label.
* State/geometry cases check rooted visibility, diamonds and cycles, atomic
  199/200/201 bounds, semantic bands/test lanes, direct ports, obstacle detours,
  centering, collision avoidance, project paging and seed replacement.
* File/HTTP browser procedures check actual details, original links, external
  and missing objects, keyboard/hover behavior, viewport and independent views,
  asynchronous failure and stale completions. Capacity procedures use the real
  30,000-Need/90,000-edge host fixture; numeric latency budgets remain deferred.
* Packaging checks use the built candidate wheel in an isolated Python 3.10
  consumer with locked offline dependencies and no Node runtime on its PATH.
* The new host mapping places test cases in the existing test lane and execution
  records on an explicit host-defined level. This uses the existing configurable
  product model; no product schema/default or runtime code changes are needed.

Finding **STV_REVIEW_015**: the documentation located the shared method using
the obsolete the historical tooling repository directory. Corrected its discovery to the historical tooling repository;
the environment override remains available. Historical paths in execution logs
remain accurate snapshots and are preserved.

Finding **STV_REVIEW_016**: executable coverage was a generated prose inventory
without canonical test-case or execution links. Added explicit cases, planned
later-mode procedures, backlink tables and per-attempt execution rules. New
case results start at ``not_run``; existing passes are not invented as new
executions. Structural checks and semantic review are recorded below.

Problem :need:`STV_PR_006` remains analyzed. Its long-path diagnostic handover
is outside this documentation-only migration's implementation scope. Existing
short-path tests cannot establish its nested-Windows acceptance criteria; the
new release must disclose that known issue independently of its suite results.

Review checks and disposition
-----------------------------

Finding **STV_REVIEW_017** (resolved): the documentation's new incoming
``verifies`` group invalidated the browser fixture's hard-coded two-control
expectation. The first full run retained both file/HTTP failures. The owner
explicitly approved updating this test expectation on 2026-10-19. It now checks
upward derivation, neutral incoming verification and downward allocation in that
order, before and after toggling expansion. Both case specifications were
re-reviewed against the corrected assertion; product code is unchanged.

The browser helper procedures were expanded into the case specifications so
their observable assertions are available with their selectors. A separate
accepted case :need:`STV_TC_SY_045` preserves concrete nested-checkout,
file/HTTP, missing-asset/retry and content-identity regression steps from
:need:`STV_PR_006`. It remains ``not_run`` and explicitly blocks any new claim
that the known product issue has been qualified or fixed. The complete reviewed
design set is now 81 cases; 76 are executable and five are planned.

Generated demo, system/software architecture and state-machine screenshots from
the first run were visually inspected: the new verification controls are
visible, and existing diagram boxes, labels and connectors remain readable.
No diagram source or export was changed. A recheck inventory records the final
case-design identities separately from the initial migration snapshot:
:download:`recheck inventory <round-7-recheck-inventory.json>`. All 81 designs
are accepted under the same delegation; the long-path case's missing execution
remains a product qualification gap rather than a missing test-design artifact.

The warnings-as-errors Sphinx build and shared validator with repository-relative
evidence checks, ``--require-test-coverage``, allocation CSV and test/execution CSV
passed on 2026-10-19: 53 stakeholder, 10 system, 57 software requirements,
11 architecture elements, six problem reports and 80 test cases. The initial
publication check found short heading underlines; those were corrected before
the passing rebuild. All 80 case designs are accepted by Codex under the
recorded owner delegation. No blocking concept-migration finding remains.

The :download:`content-identity inventory <round-7-inventory.json>` records the
method hash and assessed sources. Case design hashes exclude changing
``last_result`` and ``executed_by`` fields so subsequent execution recording
does not imply a changed test procedure. Other concept acceptance/history is
preserved. Concept acceptance does not set results or requirement verification
to passed; the subsequent release records supply actual outcomes.



.. note::

   Publication copy: private tooling locations are omitted. The unchanged original
   is retained under engineering-history/pre-portable-method in the checkout.
