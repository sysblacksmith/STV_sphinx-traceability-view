1.1.0 candidate 2 qualification
===============================

Software baseline: **41e57ed76c2acb521cdeb033f4be7b01fac50115**.
The run began against the same software/test content before that explicit
baseline commit. :download:`software-baseline.json <software-baseline.json>`
records every compared file; product, packaging, workflow and executable test
inputs match the committed baseline. The only initial source-identity difference
is an RST paragraph indentation correction, not a software change.

Actual executed scope
---------------------

* **154 Python and 42 JavaScript cases passed** in one fresh full selection;
  zero failures, errors or skips. This includes the permanent reopened-SVG
  graph-label regression for :need:`STV_PR_016` on file and HTTP transports.
* The exact fixed wheel passed a fresh clean Python 3.10 installed-runtime
  check, pip check and Sphinx usage. Main verification used Python 3.13.17,
  Windows 11, Firefox 158.0.1 and geckodriver 0.37.1.
* Four additional maximum-size SVG checks passed: 200 nodes, ten open cards,
  wide/narrow viewports and both file/HTTP. Downloads, XML, visible graph nodes,
  wide visible detail text, crop bounds and reopened content were checked.
  The reopened wide SVG was visually inspected. Raw SVGs remain locally under
  ``docs/_build/export-capacity-1.1.0-fixed``; hashes and sizes are retained.
  The ``visible_cards`` diagnostic field counts viewport-overlapping boxes;
  actual ancestor clipping remains authoritative for what is rendered.
* Supplement host graph and selected detail bytes match the fresh candidate-2
  benchmark exactly; the temporary supplement used exact candidate-2 runtime
  bytes. The equivalence proof is retained rather than assuming fixture reuse.
* The fresh 30,000-Need / 90,000-link host built in 332.11 seconds.
  File and HTTP browser measurements each ran three times. Startup medians were
  527.3 ms (file) and
  563.1 ms (HTTP).
  These are measured observations; no numeric performance budget is agreed.
* 16 historical/current/rejected archive identities and the complete
  licensing supplements were inspected. Issued 1.0.0 files remain unchanged.
* 120 current canonical execution aggregates link observed variants; seven
  infrastructure/publication checks are retained separately. Occurrence-mode
  cases STV_TC_SY_041 through STV_TC_SY_044 remain deferred.

Documentation failures and retest
---------------------------------

The full runner correctly returned nonzero: its initial strict documentation
build found an indented paragraph and a short report heading. Those formatting
errors were corrected without changing product/test inputs. The source-stability
check records the document-only change. Original failed commands, logs, source
hashes and runner disposition remain intact; they are not rewritten as passes.
Final documentation, traceability and publication checks are retested separately
before the candidate can be declared ready for the release decision.

The software-only hosted PR run passed runtime/tests and documentation, then
failed traceability because the separately retained execution evidence was not
yet committed. Its log is retained. The complete evidence commit must receive
successful hosted checks before merge or tagging.

Limits and release decision
---------------------------

CR015-018 verification remains partial for extended/manual scenarios not all
covered by this selection. Native Save As UI, every timing/resource combination,
additional OS/browser versions and mobile/touch behavior are not fully qualified.
Save-location handling is browser-managed, as accepted. Universal SVG editor
support and occurrence mode remain outside scope. No acceptance status is changed
merely because an automated selection passed.

Candidate 1 is rejected for its observed missing-graph defect; do not publish its
archives or the older candidate-1 copies currently in ``dist``. Candidate 2 is the
only proposed publication input. :need:`STV_PR_016` is corrected without changing
requirements or the behavioral state machine. Owner review of these explicit
qualification limits and a final release decision remain required.

The release workflow has policy/artifact tests and owner-reported Trusted
Publisher/environment configuration. A live PyPI/Pages publication has not yet
occurred. No tag is created by this record.

Exact proposed publication assets
---------------------------------

.. code:: text

   4cfed985248b3f328d46c5ffb57a15b5c4d89c9be0f4296e0c3568bba18549eb  sphinx_traceability_view-1.1.0-py3-none-any.whl
   6e964833b68488b722bc761a0116155e589b3928813abeaa8d61a5824bf73785  sphinx_traceability_view-1.1.0.tar.gz

Evidence
--------

* :download:`Minimum-runtime commands <supplement-commands.json>`
* :download:`Python 3.10 interpreter <runtime310-version.txt>`
* :download:`Maximum-size export results <export-capacity.json>`
* :download:`Supplement fixture equivalence <supplement-fixture-equivalence.json>`
* :download:`Historical archive inspection <historical-check.json>`
* :download:`Runtime equivalence <runtime-equivalence.json>`
* :download:`Canonical selector mappings <case-results.json>`
* :download:`Hosted baseline validation log <hosted-baseline-validation.log>`
* :download:`Source archive <artifacts/sphinx_traceability_view-1.1.0.tar.gz>`
* :download:`Exact checksums <artifacts/SHA256SUMS>`
* :download:`Reopened maximum-size SVG screenshot <export-capacity-reopened.png>`

:doc:`cleanup-review` retains the optional 1.190 GiB / 23-directory proposal.
Nothing was deleted. All archives, evidence, current benchmarks, environments
and wheelhouse are retained; post-release review remains due if publication occurs.
