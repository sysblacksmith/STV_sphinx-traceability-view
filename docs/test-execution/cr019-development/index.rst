CR019 development verification
===============================

This is a development increment, not a release qualification. Candidate source
and test SHA-256 identities and actual tool versions are retained in
``candidate.json`` alongside this page. Input baseline is
``ae0c0b5a5af6a03e13fd3ef4911888bfaa66442e`` plus the identified worktree.
The runs occurred on 2026-10-28 UTC using Linux x86_64, Python 3.12,
Firefox 159.0, geckodriver 0.37.1 and Node 24.19.0. Native browser sandbox
process creation is restricted in this container; Firefox content sandboxing
was disabled for this isolated test environment. Product/browser defaults are
unchanged. Browser runtime networking was blocked except localhost by the
existing fixture policy.

Actual results
--------------

* ``feature.xml``: six final feature checks passed, including direct-file/HTTP
  reload, stable post-reload navigation, ordered cards/FIFO, opt-out, isolation,
  stale/corrupt state, blocked/quota storage, layout races, overview paging,
  separate pages, concurrent tabs and a full browser restart with the same profile.
* ``browser-initial.xml``: 42 cases passed before a Firefox NoSuchWindow error
  during setup of the next existing navigation test. No assertion failed in
  that run. ``browser-retest.xml``: all four remaining navigation cases passed
  on fresh browser startup. Together these cover 46 distinct selected cases:
  six feature and 40 existing regression cases. This is not a single all-green
  release execution. The final feature rerun includes added anchor assertions.
* ``node.tap``: 48 JavaScript tests passed, including six new snapshot/storage
  cases and current-graph authority, 200/201-node limits and geometry reuse.
* ``python.xml``: all 107 non-browser Python tests passed. This includes clean
  offline wheel installation/build without Node and source-distribution rebuild.
  The Linux development artifact retains version 1.1.0; it is not a new release.
* Strict Sphinx/publication, complete graph/evidence validation with test
  coverage and both trace CSV exports passed. Executable mapping reports 86
  SYS/SWR requirements and no unmapped active requirement or unknown ID.
* Draw.io 32.6.1 exported the editable remembered-view source to its adjacent
  SVG. Link checks and Firefox standalone/embedded visual inspection passed.

Commands and reproduction
-------------------------

Use the repository virtual environment and pinned dependencies. Provision
``STV_GECKODRIVER`` and a Firefox executable on PATH as in the browser fixture.
Run from the repository root unless a working directory is stated:

.. code-block:: text

   # frontend/ working directory
   npm ci
   node build.js
   node --test --test-isolation=none --test-reporter=tap src/*/tests/*.test.js

   # repository root
   python -m build --no-isolation
   python -m pytest -m "not browser" -q
   python -m pytest docs/test-scripts/test_remembered_view.py -q
   python -m pytest docs/test-scripts/test_persistent_details.py docs/test-scripts/test_extended_controls.py docs/test-scripts/test_position_stability.py -q
   python scripts/check-coverage.py --strict
   python scripts/build_docs.py
   python tools/method/tooling/validate_traceability.py docs/_build/html/needs.json --version 1.1 --require-test-coverage --repo-root . --csv docs/_build/cr019-trace.csv --test-csv docs/_build/cr019-tests.csv
   python scripts/normalize-diagram-links.py --diagram-dir docs/architecture/diagrams --published-dir docs/_build/html

The clean-wheel test needs runtime wheels under ``docs/_build/wheelhouse``;
prepare them using pip download before offline installation. Node's process
isolation in this environment reported only file-level wrappers; explicit
``--test-isolation=none`` executes and reports all 48 named assertions/cases.
The extended reset harness uses the same option; its two cases both execute.

Corrections and limits
----------------------

Initial integration attempts exposed incorrect event-listener wiring and an
unchecked-view pagehide regression; both were fixed and the affected tests
rerun. Linux setup needed hatchling and an offline wheelhouse. Existing test
harnesses assumed a Windows venv path and a JavaScript esbuild launcher; they
now use a platform-aware interpreter and esbuild's JavaScript API. Generated
license newlines are normalized without changing audited vendor bytes.
The publication audit rejected a private tooling name in the review prose;
the public record now uses portable workflow wording, and the audit passed.

Formal :need:`STV_TC_SW_056` and :need:`STV_TC_SY_070` remain accepted test
designs with last_result not_run: these developer runs do not invent formal
execution Needs. :need:`STV_SWR_073`, :need:`STV_SWR_074`,
:need:`STV_SWR_075` and the amended stakeholder obligations have partial
verification. Windows desktop qualification, additional browsers, release
publication and later occurrence-mode behavior remain outside this increment.
The previous release and historical acceptance/results are unchanged.
