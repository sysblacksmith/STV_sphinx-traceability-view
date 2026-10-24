Round 8: Maintenance acceptance review
======================================

Scope and delegated authority
-----------------------------

Date: 2026-10-24. Reviewer: Codex. Decision owner: project owner.
Base revision: ``17cafd9`` plus the recorded maintenance worktree.
:doc:`../change-requests/STV_CR_012_release-cancellation-and-cleanup` records the
owner's explicit instruction to fix the findings and perform acceptance review
before another release starts. This is scoped delegation to review and accept
clean affected design/test artifacts, not permission to publish a release.

Boundary and baseline
---------------------

The unchanged stakeholder/internal requirement baseline and accepted ADRs from
rounds 1-7 remain the context. No stakeholder intent or criterion is changed.
The review covers the current source-organization decision and all nine
component mappings, package/version/notice delivery, compact detail asset
identity, affected interfaces/technology/implementation/state documentation,
three existing inspector/Windows cases and the new compact-path/legal-guard
cases. The changed clean-wheel procedure is included. Unchanged requirement
allocations/derivations and system/software boundaries remain preserved.

The :download:`current artifact inventory <round-8-inventory.json>` records
content hashes and distinguishes scoped acceptance from retained prior baseline
acceptance. No blanket requirement verification is inferred from checks.

Findings and closure
--------------------

All following findings are closed in the current scoped worktree. The owner
remains the decision owner; the acceptance below is exercised under the
explicit delegation recorded above.

* **STV_R8_001, Windows delivery:** The old full identity-plus-content filename
  exceeded Windows file-loader limits. :need:`STV_PR_006` now uses one full
  content digest, with deduplication and unchanged per-object manifest identity.
  Before-fix failure and root/nested file/HTTP/retry passes are retained in
  :need:`STV_TC_WINDOWS_PATH`; :need:`STV_TC_COMPACT_PATHS` covers immutable
  digest/reference/deduplication invariants. Closed by implementation and actual
  regression evidence, not by path-length inference alone.
* **STV_R8_002, dependency notices:** npm-level ELK licensing omitted compiled
  Java/GWT-family materials. The pinned-binary inventory, retained source/POM
  evidence, original source URLs, copyright headers and Apache/EPL notices now
  cover that engineering scope. Build guards reject unknown binary/version or
  legal-input changes; Git attributes preserve checksum input bytes on Windows.
  The first isolated retest exposed the missing generated-site inventory copy;
  lifecycle delivery is corrected and final installed checks passed. Closed;
  no claim of an upstream compiler rebuild or general legal opinion is made.
* **STV_R8_003, version ownership:** Package, frontend and documentation release
  literals drifted independently. One package-root version shim now owns the
  maintained value. Hatch, Sphinx metadata and the runner derive from it; private
  npm manifests are unversioned. Historical evidence and independent dependency
  pins remain unchanged. Installed package/distribution versions agree.
* **STV_R8_004, semantic test links:** The new negative build guard initially
  linked SWR_046 despite not exercising entry-module registration. That link
  was removed from the marker and case, and the final guard rerun passed. Its
  SYS_009/SWR_042 links cover packaging-input failure behavior as a complement
  to the successful installed-wheel case; they do not claim full criterion
  verification by the guard alone. Closed.
* **STV_R8_005, visual routing:** The earlier state drawing shared return stems
  for reject/commit/failure and detail-dismiss paths; the pan self-loop also
  shared an outbound segment. The Draw.io generator now assigns separate ports
  and nested lanes; the timed detail transition uses an outer corridor. It was
  regenerated through Draw.io, then inspected standalone and embedded. Labels,
  arrowheads and each source/target route are readable with no coincident return
  segments. States/events/transitions are unchanged. Closed.
* **STV_R8_006, documentation consistency:** New heading underline warnings and
  a raw upstream Markdown notice accidentally collected as a Sphinx document
  caused the first review build to fail. Heading widths were corrected and the
  raw notice is retained as a text attachment. The clean warning-as-error
  rebuild passed. Failed logs remain retained. Closed.

Semantic and feasibility assessment
-----------------------------------

:need:`STV_SHR_015`, :need:`STV_SHR_017` and :need:`STV_SHR_018` retain their
accepted intent and the existing static/external/media exceptions. Their paths
through :need:`STV_SYS_003`, :need:`STV_SYS_006`, :need:`STV_SWR_015`,
:need:`STV_SWR_017` and :need:`STV_SWR_018` are unchanged. Compact asset names
preserve the body/digest/relative-URL contracts; the bundle and inspector retain
ownership. No requirement is weakened to promise arbitrary-depth paths.

:need:`STV_SYS_009`, :need:`STV_SWR_042` and :need:`STV_SWR_046` retain the
external installation boundary. The clean installed wheel checks actual metadata,
source-free import, generated views and notices. The negative legal-input case
supplements packaging integrity; it cannot substitute for installed behavior.

All nine software-element directories have matching README/test boundaries:
:need:`STV_SWE_DIRECTIVE`, :need:`STV_SWE_MODEL`, :need:`STV_SWE_GRAPH`,
:need:`STV_SWE_DETAIL_BUILD`, :need:`STV_SWE_BUNDLE`, :need:`STV_SWE_STATE`,
:need:`STV_SWE_LAYOUT`, :need:`STV_SWE_RENDER`, :need:`STV_SWE_INSPECT`.
Their containment in :need:`STV_SE_BUILD` / :need:`STV_SE_BROWSER` and
requirement allocations remain coherent. Public version/setup and maintained
asset-building helpers have explicit owners instead of new invented elements.

The cache case asserts shared concurrent promise/load identity and a different
build's fresh fragment. The retry case rejects a failed load, removes its script,
creates a new promise/script and resolves after registration. Their actual
assertions support the intended build-keyed cache/recovery contracts; normal,
negative and recovery behavior are explicit and independently runnable.
The compact-path case covers shared and changed content; the Windows case
covers actual rendered loading and retry. The license guard uses isolated inputs
and checks specific diagnostics; the host package case checks the success path.
All six affected test designs have implementable procedures, concrete expected
outcomes and actual linked attempts, including failed attempts.

Visual and structural checks
----------------------------

System, software and behavioral SVGs were inspected directly and inside their
published HTML object embeddings. Each connector was followed to its arrowhead;
the state overlap finding was corrected and re-exported before acceptance.
Sources remain adjacent to exports, with 2/9/11 portable element/requirement
links respectively. Screenshots and embedded object checks are retained in the
maintenance record's visual folder. Diagram rendering supplements the shared
source/published link validator; it does not replace it.

Strict executable mapping found 67 system/software requirements, 81 executable
cases and no unmapped active requirement. The shared --require-test-coverage
check additionally assesses all stakeholder/case/execution paths. Four later
occurrence-mode cases remain deliberately unexecuted. Source ownership remains
plain text rather than filesystem download links.

Acceptance decision
--------------------

Accepted under the scoped owner delegation: :ref:`STV_ADR_007`;
:need:`STV_TC_DETAIL_CACHE`, :need:`STV_TC_DETAIL_RETRY`,
:need:`STV_TC_COMPACT_PATHS`, :need:`STV_TC_LEGAL_GUARD`.
Reaffirmed after changed-procedure review: :need:`STV_TC_WINDOWS_PATH` and
:need:`STV_TC_F988267D01C9`.

Scoped ordinary-document acceptance covers the changed source mappings,
interface/implementation/state text, technology/licensing/version delivery
contracts and the rerouted Draw.io/SVG pair identified in the inventory.
Unchanged prior requirement/element/ADR acceptance is preserved; it is not
relabeled as newly accepted. There is no unresolved acceptance-blocking finding
in this maintenance scope. All concept/test acceptance states remain separate
from runtime requirement verification.

The development record has 79 distinct latest passing cases (59 Python,
20 JavaScript), zero latest failures/errors/skips. Earlier failed attempts are
retained. The canceled candidate's results do not qualify these changed inputs.
Two capacity cases and any future full release qualification remain outside
this owner-requested maintenance run. The owner must explicitly start the next
release; no new release, tag or publication was performed.
