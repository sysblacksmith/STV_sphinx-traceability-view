Project maturity
=================

This is the single location for the current project maturity summary and
links to its review and lifecycle evidence. Need ``:status:`` fields and ADR
status metadata remain authoritative for individual artifacts. The charts in
:doc:`project-metrics` read those fields directly.

CR015-018 development implementation, 2026-10-25
--------------------------------------------------------------------------------

The owner invoked concept-implementation for accepted baseline ``2c4236a`` on
``concept-cr015-018``. The four CRs now have implemented status: graph collapse
keeps current roots/cards, visible-area SVG export uses safe local resources and
browser-managed downloads, tooltip/card font scales default independently to
0.7, and host pages have scoped bulk metadata controls. :doc:`implementation-review`
records actual source/test mappings, checks, artifacts and limits.

The developer check sets include 42 frontend passes, 87 non-browser passes,
57 broad Firefox passes and later targeted retests after edge corrections.
Packaging is verified in an isolated offline consumer without Node. The updated
behavioral tables and adjacent Draw.io/SVG sources describe the actual command,
error/recovery and download-lease states. Runtime product/dependency versions and
existing release artifacts remain unchanged; development archives are isolated.

Verification for the new requirements/CRs is partial, not a new release pass.
The nine formal case designs remain accepted/not_run pending complete recorded
qualification; development pytest/Node checks are identified separately. No new
release, deployment, push or implementation commit is authorized by these results.
Prior concept/release history below remains historical evidence for its exact
artifacts. The working demo is rebuilt locally for owner inspection.


CR015-018 accepted concept, 2026-10-25
--------------------------------------------------------------------------------

The owner requested the concept on a side branch and delegated acceptance of
clean artifacts explicitly. Branch ``concept-cr015-018`` preserves creation
commit ``2e1eace``. :doc:`concept-reviews/round-15` records the scoped review,
five resolved findings, semantic paths, diagram assessment and exact acceptance
inventory. The source identities are in
``docs/concept-reviews/round-15-inventory.json``. Earlier creation-stage pending
statements below are historical, superseded only for this reviewed increment.

Accepted internal revisions: STV_SYS_011, STV_SWR_066 through STV_SWR_072,
DIRECTIVE/MODEL/DETAIL_BUILD/BUNDLE/STATE/RENDER/INSPECT/EXPORT, ADR011 and
STV_TC_SY_066 through STV_TC_SY_069 plus STV_TC_SW_051 through STV_TC_SW_055.
This is 25 modeled artifacts and one ADR. Ordinary architecture/interface/plan
and picture acceptance is recorded in the inventory without invented statuses.
Existing stakeholder acceptance is preserved; CRs remain accepted, not implemented.

The host-icon/ARIA/mixed-state contract, host readiness gate, capture font/resource
readiness and zero-area failure policy were tightened. The metadata diagram was
re-exported with source-owned label padding; review round 14 was restored to the
review index. No current acceptance blocker remains after the final checks.
Product implementation is not authorized by review acceptance and is unchanged.
New cases remain not_run with no execution records; requirement verification
stays not_assessed. Deferred occurrence mode, full-graph export, universal vector
editor support and mobile/touch qualification retain their existing boundaries.

Validation: strict fresh Sphinx/publication build, full graph/evidence validation
with --require-test-coverage and both CSV exports, published diagram targets,
canonical acceptance/result-state assertions and git diff --check passed. All six current diagrams and three containing HTML pages were rendered
for visual review; the corrected metadata picture was rechecked separately.
Native SVG feasibility remains distinct from unexecuted implementation tests.
Implementation handover is :doc:`implementation-plan` and
:doc:`verification-plan`; execute the risky offline export slice first.


Creation history: CR015-018, 2026-10-25
--------------------------------------------------------------------------------

The owner explicitly reviewed and accepted :need:`STV_CR_015` through
:need:`STV_CR_018` and :need:`STV_SHR_058` through :need:`STV_SHR_061` on
2026-10-25, then invoked concept creation. Their canonical states are accepted;
verification remains not_assessed. The owner also approved browser-managed
Save As with documented location-prompt settings. :doc:`sources` records the
approval and :doc:`review` the resolved scope. This does not accept later
internal drafts or authorize product implementation, staging or committing.

Input identity: prepared stakeholder/CR working-tree revisions based on
633bee2a1fb569f5366bdf6a93ec96ed9fbcb04d. At the owner's request, work moved to
main after a safe fast-forward to 8dbbe79; all uncommitted amendments were retained.
Repository: https://github.com/sysblacksmith/STV_sphinx-traceability-view.
Prior accepted reviews/ADRs/results retain their historical identities.

The concept adds draft :need:`STV_SYS_011`, :need:`STV_SWR_066` through
:need:`STV_SWR_072`, :need:`STV_SWE_EXPORT` and proposed :ref:`STV_ADR_011`.
Changed component revisions DIRECTIVE, MODEL, DETAIL_BUILD, BUNDLE, STATE,
RENDER and INSPECT reopen to draft/not_assessed because their contracts expand;
unchanged GRAPH/LAYOUT and all other accepted requirements remain unchanged.
No accepted ADR is superseded. The new SVG path is a companion Draw.io/SVG
architecture view with real Need links, not a replacement of the retained core.

Nine canonical cases :need:`STV_TC_SY_066` through :need:`STV_TC_SY_069` and
:need:`STV_TC_SW_051` through :need:`STV_TC_SW_055` cover all new requirements.
They are draft/not_run without execution links. Existing relevant offline,
security, keyboard, capacity and persistent-detail cases remain regression scope;
historical passing executions do not verify this increment. Font configuration,
reset/cache semantics, page scope, export crop/resources/save/error contracts,
packaging and staged delivery are in :doc:`internal-interfaces`,
:doc:`implementation-plan` and :doc:`verification-plan`.

Feasibility checks: installed Draw.io exported view-export.drawio to its adjacent
SVG, and the standard normalizer verified its five linked component targets.
Headless installed Firefox opened a standalone SVG fixture combining XHTML
foreignObject, styled text, nested scroll clipping and vector line geometry;
exit 0 and screenshot inspection confirmed the intended text/clip rendering.
The new architecture SVG was also rendered and visually inspected: five arrows
have separate routing space, clear labels and no unrelated-box crossings.
Temporary fixture/screenshots/profiles remain ignored under
``docs/_build/concept-feasibility``. These are native-API feasibility observations,
not product test executions or proof of arbitrary host snapshot fidelity.
No new third-party dependency is introduced; primary API limitations are cited
in ADR011. Full resource/style/capture integration is the first implementation
slice and requires the specified tests before claiming runtime correctness.

Creation-stage checks: the shared validator with --require-test-coverage and
--repo-root . passed for the generated increment: 18 CRs, 61 SHRs, 11 SYS,
72 SWR, ten software elements and 124 cases; all 920 historical executions
remain unchanged. Complete derivation and test CSV matrices were exported to
``docs/_build/cr015-018-concept-traceability.csv`` and
``docs/_build/cr015-018-concept-test-traceability.csv``. A strict Sphinx pass
initially identified short heading underlines in newly added sections; these
were corrected before the final rebuild. The final strict Sphinx/publication
build passed; strict graph/evidence/test coverage and all published diagram
links passed on that completed output. The new diagram was inspected both as
standalone SVG and embedded in the generated architecture page. Canonical-state
checks confirmed accepted stakeholder input, draft/not_assessed internal
requirements, and draft/not_run cases with no fabricated executions.
``git diff --check`` passed; no source/frontend/package input was changed.
No runtime product tests were executed or invented.

The concept has selected ownership, APIs, serialization/resource boundaries,
error policies, configuration and staged exit criteria. It is ready for scoped
concept review and implementation planning; acceptance remains outstanding.
The first export vertical slice must validate full integration fidelity before
implementation acceptance. Implementation-ready design does not mean
implemented or verified software.


.. _release-1-0-0-authority:

v1.0.0 released
-----------------------------------

The owner approved PRSA-001 through PRSA-005 remediation and PR015 final
presentation on 2026-10-24. See :doc:`concept-reviews/round-14`. Earlier pending-owner
statements below are historical and superseded for this exact scope.
The owner requests v1.0.0 without visibility-specific release labels. Repository
visibility is a separate setting and is unchanged. Runner improvements and
hosted hardening are owner-accepted nonblocking deferrals; PRSA-006 remains open.
This is a release authorization, not a requirements change request. The owner
explicitly confirmed that release intent belongs here, not in the CR register.
v1.0.0 was published on GitHub at 22:51:13 Europe/Berlin on 2026-10-24,
with annotated tag commit ``77d52d82447db434cf5071c820c9a7135fa21caf``.
All 122 Python and 36 JavaScript tests and final qualification gates passed.
The exact wheel/source/checksum assets have verified hosted digests.
See :doc:`test-execution/1.0.0-candidate-2/qualification` and
:doc:`test-execution/1.0.0-candidate-2/post-release`.

PR014 visible viewport boundary fixed
---------------------------------------

:need:`STV_PR_014` is fixed. :doc:`concept-reviews/round-11` records scoped
concept acceptance and :doc:`test-execution/pr014-boundary/index` retains before/
after reproduction, 70 passing development checks and installed asset evidence.
The viewport has a fixed thin grey top border while retaining its 975 px client
height and existing clipping/navigation. The normal demo is rebuilt. No graph,
layout, state, dependency or version changes; no new capacity/release claim.

CR_013 classified evidence rows implemented
--------------------------------------------

:ref:`STV_CR_013` is implemented with nine target rows and the owner's labelled
fallback row. :doc:`concept-reviews/round-10` records the accepted concept and
implementation re-review; :doc:`test-execution/cr013-rows/index` retains 134
latest passing tests, including real Firefox file/HTTP and both 30,000-record
classification and 200-visible-node capacity checks. Four new canonical case
designs have actual aggregate executions. Existing legacy models, source-free
wheel consumption, endpoint routing and PR013 stability passed regression.
The project demo uses the new classified model. Release qualification remains
a separate owner-started activity; unrelated security/hosted gates stay open.

PR013 stable navigation finalized
---------------------------------

:need:`STV_PR_013` is fixed. :doc:`concept-reviews/round-9` records the scoped
accepted concept, partial ADR supersession and test-design re-review.
:doc:`test-execution/pr013-final/index` retains 111 distinct latest passing
component, integration, Firefox file/HTTP, capacity and clean-package outcomes.
Six new accepted test designs cover stable slots, negative SVG bounds and
natural initial order. Fresh centering remains separately verified. Two initial
placeholder visibility assertions failed; explicit viewport fitting corrected
the test procedure and both retests passed without product changes.

Ordinary x slots and the clicked band stay fixed during group/root navigation;
other bands can move for height and shared tests can change associated ranks.
The normal documentation/demo is rebuilt. This completes the development fix,
not a release; the canceled candidate stays canceled and the next release
requires the owner's explicit instruction. Unrelated PRSA gates remain below.

PRSA-006 local preparation; hosted hardening pending
--------------------------------------------------------------------------------

:need:`STV_PR_012` remains analyzed with partial verification. Pinned CI and
manual provenance workflows, checksum generation and an unapplied protection
profile are prepared. :doc:`ci-and-provenance` defines their trust boundary and
:doc:`test-execution/prsa-006-fix/index` retains local validation. GitHub's
private-plan restriction prevents rulesets; hosted runs, attestations and chosen
protections remain unconfirmed. New/refined workflow and case designs await
owner review. No release or remote setting change is performed.

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
The shared method now resolves from the renamed the historical tooling repository repository.

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

Review and lifecycle records
-----------------------------

.. toctree::
   :maxdepth: 2

   concept-review
   concept-reviews/round-14
   concept-reviews/documentation-reorganization
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

CR014 persistent details
--------------------------

The owner accepted the persistent per-view details amendment and clarified
reuse, lifetime and configurable capacity. Concept round 12 and ADR 010 are
accepted. The implementation passes all 156 distinct executable checks,
including file/HTTP default/override capacity, loading races and the rebuilt
30,000-record capacity fixture. The fresh wheel/source distribution passes
clean-consumer checks. See :doc:`test-execution/cr014-details/index` for actual
attempts, criterion review, source identity and retained failures. No release
is started; unrelated draft designs, occurrence-mode deferral and publication
gates retain their existing states.


PR015 detail acceptance corrections
--------------------------------------

The owner reported narrow boxes, inert/unfolded metadata controls and a copied
artifact-ID link returning to the view. :need:`STV_PR_015` records the causes and
fix. Round 13 accepts the scoped design correction and regression case;
:doc:`test-execution/pr015-details/index` retains the failing baseline and 127
passing distinct development checks. The dock is now 720 px, copied metadata
starts folded and toggles accessibly, and header IDs open actual source Needs.
Owner acceptance retest is pending. Capacity and release qualification remain
outside this correction; earlier results remain historical.


The PR015 pane-frame follow-up marks the open dock's full boundary with a thin
grey line and removes card shadows. Ten affected Firefox file/HTTP procedures
pass; the current normal demo is rebuilt for owner retest. This CSS-only change
does not imply a new full regression, capacity or release qualification.



Independent method tooling, 2026-10-25
--------------------------------------------------------------------------------

The owner requested independent publication and authorized implementation of a
portable method package and explicit import workflow. STV now keeps method package
1.0.0, including its model, charts, CSS and validators, under tools/method.
Documentation and release tools resolve only local files; no skill registration
or separate tooling checkout is a build requirement.

This is a documentation/tooling migration. It does not change product requirements,
canonical IDs, acceptance flags, verification states or historical execution results.
Importer regression checks and existing graph-validator checks passed in the cloud.
Full Sphinx, package and Windows/browser qualification are not claimed by those
checks; PR CI records the applicable build results. Historical raw attachments
remain in the checkout and are excluded from the public website, as described in
:doc:`ci-and-provenance`.


.. note::

   The documentation/tooling restructuring took place in commit
   ``a807a1b8300151fc1dfc2e64a792d24a48d46f38``. Earlier documentation
   can be found in Git history.


Additional browser smoke check, 2026-10-25
--------------------------------------------------------------------------------

The owner reported a minimal manual STV smoke test using Microsoft Edge. This
provides additional browser confidence; browser/OS versions and individual
procedures were not recorded. It does not extend the formal release qualification
or establish full Edge coverage.
