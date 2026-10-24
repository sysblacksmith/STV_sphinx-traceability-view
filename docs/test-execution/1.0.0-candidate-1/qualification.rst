1.0.0 readiness assessment
==========================

Disposition: **executable validation passed; final release qualification incomplete**.
No owner release decision, commit, tag, upload or hosted release is claimed.

Base revision: ``2960b25721df9eb727ae070317e4c2f4746bb909``. Candidate: ``1.0.0-candidate-1``; source/test identity ``4d726b535c181f9113d1b4fa96f048ef35a50920e3b224452341737181c3d026``.
The version updates are intentional worktree changes on this base; this is not an unchanged build of the base commit.
Execution timestamps with UTC offsets, commands, lock hashes, tool versions and per-case results are in the parent record.

Required versus executed gates
------------------------------

* 58/58 Python cases and 20/20 JavaScript cases passed; no failures, errors or skips.
* Windows, Python 3.10.9 (the minimum supported minor), Firefox 158.0.1, geckodriver 0.37.1 and Node v24.21.0 were used. Both existing project Python environments use 3.10.9; no different Python minor or additional OS/browser is claimed.
* File and static HTTP workflows, offline external-request policy, boundary/negative cases and 200-visible-node checks passed. Each capacity transport has three repetitions.
* Fresh real Sphinx fixture: 30,000 Needs, 90,000 authored edges; build 321.14 seconds. No prior benchmark result was reused.
* Isolated consumer environment installed the exact candidate wheel from the offline wheelhouse, with checkout imports removed and Node absent from PATH, and built a supported HTML host.
* Source-level suites and rendered fixture builds used checkout code. All 14 wheel runtime members match those checkout inputs byte for byte; this equivalence and the separate installed-wheel test are recorded without claiming every test imported from an installed wheel.
* Wheel and source archive built through the normal toolchain; wheel was built from the source archive. Versions, required assets, MIT/third-party notices and runtime test exclusions were checked. SHA-256 checksums and both artifacts are retained.
* Strict executable mapping, warnings-as-errors documentation, graph validation with --require-test-coverage and source/published diagram links passed. Final publication-documentation retest commands, timestamps and results are retained in ``final-validation.json`` after rendering.
* All 78 actual attempts were imported into canonical execution records; all 78 latest results are passed. Four occurrence-mode cases and the Windows-path system case remain not_run. Case acceptance statuses were preserved.

Criterion coverage and remaining gates
--------------------------------------

The delivered scope comprises 49 stakeholder, 10 system and 53 software requirements (112 total). Four stakeholder/software occurrence-mode pairs (eight requirements) remain explicit later scope. See the complete :download:`scope snapshot <requirement-scope.json>` and parent per-case mappings.

The acceptance criteria and executable assertions were reviewed against the verification plan and the historical :doc:`../../implementation-review`. Current checks cover model validation, seed/capacity bounds, graph state/cycles, geometry, static rich details/media exclusion, hidden-object handling, input/focus/error recovery, installed usage and both browser transports. Structural mapping does not establish full criterion coverage.

* :need:`STV_TC_WINDOWS_PATH` remains unexecuted. :need:`STV_PR_006` is still analyzed; current detail filenames retain two full hashes. Short-path test passes do not cover nested Windows paths beyond the original limit. :need:`STV_SYS_003`, :need:`STV_SYS_006`, :need:`STV_SWR_015`, :need:`STV_SWR_017` and :need:`STV_SWR_018` retain partial verification. No fresh stakeholder acceptance result is inferred.
* :ref:`STV_ADR_007` is proposed, and :need:`STV_TC_DETAIL_CACHE` / :need:`STV_TC_DETAIL_RETRY` remain draft despite actual passing executions. This release-test invocation does not establish concept-review acceptance.
* MIT was selected by the owner, and packaging checks confirm its delivery. The source-provenance/transitive-dependency redistribution audit documented in :doc:`../../licensing` remains outstanding before external rollout. No legal or employer approval is inferred.

The Windows regression needs its specified system evidence and issue-resolution workflow; the changed design/test artifacts need acceptance review; the redistribution audit needs a recorded disposition. Until those gates are closed, do not create a final v1.0.0 tag or describe this as release-ready.

Occurrence mode, touch and additional browser/platform qualification remain deferred. Widget-specific JavaScript parity is outside the static-detail contract. Numeric latency/memory budgets remain unagreed; no invented performance threshold was used.

Capacity observations
---------------------

Build output: 415,477,654 bytes, including graph 34,897,944 and detail assets 147,393,890 bytes. Browser process-tree working sets include helpers and can double-count shared pages.

.. list-table:: Measurements (three runs per transport)
   :header-rows: 1

   * - Transport
     - Startup median / maximum (ms)
     - Expansion median / maximum (ms)
     - Maximum measured process-tree working set (MiB)
   * - file
     - 612.10 / 635.78
     - 105.00 / 319.00
     - 1848.68
   * - http
     - 629.59 / 721.11
     - 92.50 / 254.00
     - 1739.61

Startup medians are below 0.7 seconds and measured expansion maxima below 0.32 seconds on this host. The approximately 1.5 GiB process-tree footprint and 321-second fixture build need owner review when setting budgets; these observations do not establish an agreed performance pass. Raw repetitions, collapse and first/cached-detail timings are retained in capacity-browser.json.

Supplemental evidence and handover drafts
-----------------------------------------

* :download:`Artifact checksums <SHA256SUMS.txt>`
* :download:`Package inspection <package-review.json>`
* :download:`Shared tool hashes <shared-tool-hashes.json>`
* :download:`Preparation and importer identity <preparation.json>`
* Historical tested source archive ``artifacts/sphinx_traceability_view-1.0.0.tar.gz``; :doc:`license supplement <../../licensing/historical/index>`
* :download:`Proposed preparation commit <commit-message.txt>`
* :download:`Conditional tag template <tag-release.ps1.txt>`
* :download:`Draft GitHub release notes <github-release-notes.md.txt>`

.. toctree::
   :maxdepth: 1

   cleanup-review

The owner approved removal of the exact 14 proposed cache directories (209,992 logical bytes); all were removed. All distributions, environments, dependencies, current build output and release evidence are retained. Post-release review remains due when actual publication is known.

Documentation retest history
----------------------------

The first final clean build failed on short heading underlines in the newly authored maturity/readiness records (four warnings, including a repeated warning). Those RST underlines were corrected without changing product/test inputs. The original final-documentation.log and all validation attempts remain retained in final-validation.json; the corrected clean rebuild uses final-documentation-2.log.
