Interactive traceability view
=============================

Sphinx-Needs extension providing offline interactive traceability exploration.
Requirements and architecture are indexed in ``docs/index.rst``.
Project maturity and review records are maintained in ``docs/maturity.rst``.

Build documentation
-------------------

Run the PowerShell script using the project's existing ``.venv`` (Python 3.11+ for documentation tooling).
On the first run, install the pinned documentation dependencies and build::

   .\build-docs.ps1 -InstallDependencies

For subsequent builds::

   .\build-docs.ps1

The script works independently of the current working directory, treats Sphinx
warnings as errors, and returns a nonzero exit code on failure. Successful output
is written to ``docs/_build/html/index.html``. Virtual environment activation is
not required.

Each build uses a fresh staging directory. After success, it replaces the HTML
tree and writes ``_stv-publication.json`` with file sizes and SHA-256 hashes.
A failed build preserves the previous HTML tree. Earlier output and diagnostic
staging are retained beside ``html`` under ``docs/_build/``; publish only the
``html`` directory. Rebuilding into an existing output with a direct Sphinx
command does not provide this clean-publication guarantee.

The configuration imports the shared model, status-chart extension and styling
directly, and includes the live central method. It discovers the shared skill
under an ancestor's ``-agents/skills`` or ``~/.agents/skills``. To select another
location, set ``REQUIREMENTS_SKILL_DIR`` to the shared
``reverse-engineer-requirements`` skill directory. Its repository-level
``method.md`` must also be present.

After building, run the shared validator (replace ``<shared-skill>`` with the
selected reverse-engineer-requirements skill directory)::

   .\.venv\Scripts\python.exe <shared-skill>/scripts/validate_traceability.py docs/_build/html/needs.json --version <major.minor> --repo-root . --require-test-coverage --csv docs/_build/traceability.csv --test-csv docs/_build/test-traceability.csv

The internal specification includes conventional and channeled derivation paths,
allocations and containment. Graph validation establishes structural checks;
it does not establish semantic correctness, internal design acceptance or
successful runtime verification.

Architecture diagrams
---------------------

Keep each .drawio source and its same-named .svg export together in
``docs/architecture/diagrams``. Edit the Draw.io source and export SVG only::

   & <shared-skill>/scripts/export-architecture.ps1 -ProjectRoot .

Use the selected shared skill checkout directly. No project-local symbolic
links or administrator rights for link creation are required.

The export script uses Draw.io and restores portable links from each paired
Draw.io source. It accepts ``-ProjectRoot`` and ``-DiagramDirectory`` for other
project layouts. To validate the published targets after building::

   .\.venv\Scripts\python.exe <shared-skill>/scripts/normalize-diagram-links.py --diagram-dir docs/architecture/diagrams --published-dir docs/_build/html

Sphinx embeds the linked SVGs as interactive objects.

Implementation handover
-----------------------

Start with ``docs/implementation-plan.rst`` for module contracts and delivery
steps, ``docs/technology-stack.rst`` for selected libraries/versions/licenses,
and ``docs/verification-plan.rst`` for completion gates. Exact npm manifests and
lock are in ``docs/architecture/implementation``; Python direct implementation
pins are alongside them. Runtime verification is tracked in ``docs/maturity.rst``.

Build and use the extension
---------------------------

Maintainers build the checked-in browser assets and Python distribution::

   cd frontend
   npm.cmd ci
   node build.js
   cd ..
   .\.venv-implementation\Scripts\python.exe -m build --no-isolation

Install the generated wheel from ``dist/`` in the host's
Python environment and add ``sphinx_traceability_view`` to ``extensions`` in
``conf.py``. Node is needed only when rebuilding browser assets. Host types and
relationships remain authoritative; see ``docs/internal-interfaces.rst`` for
replacement model configuration. Embed a project root or explicit seeds::

   .. traceability-view::

   .. traceability-view:: NEED_A NEED_B

Build the host with Sphinx's HTML builder. Open the output directly from disk
or serve it through static HTTP. On Windows, keep the output root short enough
that content-addressed detail paths stay below Firefox's local file-path limit.
The project's documentation includes a live ``demo.html`` using its own Needs.

Use in another Sphinx project
-----------------------------

See `Getting Started <docs/getting-started.rst>`_ for installation, the live
demonstration and the minimal integration steps for an existing Sphinx project.
The following sections provide additional host-model and compatibility details.

Host model configuration
~~~~~~~~~~~~~~~~~~~~~~~~

The default mapping expects exactly the five Need types ``shr``, ``sysr``,
``syse``, ``swr`` and ``swe`` used by this project's requirements model.
For other schemas, set ``traceability_view_model`` in the host's ``conf.py``.
For example, a host defining types ``goal``, ``requirement`` and ``component``
can use::

   traceability_view_model = {
       "levels": ["goals", "requirements", "components"],
       "types": {
           "goal": {"level": "goals", "role": "stakeholder"},
           "requirement": {"level": "requirements"},
           "component": {"level": "components"},
       },
       "accepted_statuses": ["accepted"],
   }

Map every configured host Need type, using its directive name as the key.
Project-root mode requires a type with the ``stakeholder`` role. Test types
use ``{"role": "test"}`` without a level. Adapt ``accepted_statuses`` to the
host's status vocabulary. Relationships come from the host's ``needs_links``
configuration and require both incoming and outgoing labels. See
``docs/internal-interfaces.rst`` for the full interface contract.

Current compatibility and delivery limits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. stv-compatibility-start

The current package requires Python 3.10 or newer and pins Sphinx 8.1.3,
Sphinx-Needs 8.2.0 and Beautiful Soup 4.13.5. Check compatibility with the host's
documentation dependencies before installation. Only the ``html`` builder is
supported when a traceability view is present. Each view supports up to 200
visible graph nodes. On Windows, use a short HTML output path when opening
files directly in Firefox.

.. stv-compatibility-end

STV-owned code and documentation are licensed under MIT; see Licensing below.

User issue handover
-------------------

Report issues in ``docs/problem-tickets/`` and keep screenshots/logs beside the report.
The folder index and ``report.rst.template`` describe the format; informal text
is also accepted for normalization by the problem solver. Reports use stable
``problem_report`` Need IDs and ``new``, ``analyzed``, ``fixed`` states. Fixed
reports remain in place, with evidence and any pending owner/release review.

Development verification
------------------------

``scripts/normalize-diagram-links.py`` is a relative symbolic link to the
shared ``-agents`` diagram utility. Keep that repository alongside this
checkout. Make utility changes explicitly in the shared repository rather
than editing through this link. The documentation and release workflow also
depend on the shared method, model and tools as described above.

Verify development changes::

   .\.venv-implementation\Scripts\python.exe -m pytest -m "not browser"
   node --test frontend/src/*/tests/*.test.js
   .\.venv-implementation\Scripts\python.exe scripts/check-coverage.py --strict

For Firefox verification set ``STV_GECKODRIVER`` to an explicitly provisioned
driver and run ``pytest docs/test-scripts/test_browser.py`` in the implementation environment.
The packaging test needs a built wheel and an offline runtime wheelhouse at
``docs/_build/wheelhouse``. Source tests, release results and deferred criteria
are linked from the central maturity page.

The documentation's ``test-cases/index`` specifies canonical cases and their
requirement links. Per-case execution records retain actual attempts, while
``last_result`` shows each case's latest recorded outcome. Planned
occurrence-mode cases remain unexecuted. Review acceptance and recorded test
results are independent.

For full qualification, select the shared skill explicitly (the release
runner's legacy fallback predates the directory rename)::

   $env:REQUIREMENTS_SKILL_DIR = '<shared-skill>'
   .\.venv-implementation\Scripts\python.exe scripts/verify-release.py --record <new-record-name> --driver <provisioned-geckodriver>
   .\.venv-implementation\Scripts\python.exe docs/test-execution/import-case-results.py <new-record-name>

Replace the placeholders with the shared ``reverse-engineer-requirements``
directory, a unique execution name and the provisioned driver path. Retain failed
attempts. Import results only after the runner has finished; then rebuild and
validate the published requirement/test/execution graph. Inspect the generated
cleanup proposal and approve exact paths before deleting disposable output.

Retain the entire ``dist/`` directory during cleanup, including wheels and
source archives for current and older versions. The owner removes older
versions manually after uploading them to GitHub. Copies retained as test
evidence do not replace the distribution files in ``dist/``.


Architecture-to-code navigation
-------------------------------

Each software element owns a directory named after the lowercase suffix of
its canonical ``STV_SWE_*`` ID. Python build components live under
``src/sphinx_traceability_view/``; browser components live under ``frontend/src/``.
Each component contains its unit tests in ``tests/`` and a ``README.rst``
explaining its boundary. ``docs/elements-software.rst`` identifies each element
through its component and test naming conventions. Run all Python tests with ``python -m pytest``
and browser-component unit tests with ``node --test frontend/src/*/tests/*.test.js``.
Host integration, browser and release checks remain in ``docs/test-scripts/``.
Component tests are excluded from the installed wheel.


Licensing
---------

Copyright (c) 2026 Henning Heikes. STV-owned code and documentation are licensed
under the MIT License. The standard terms are in the repository-root ``LICENSE``
file and in the package license files. Credit to Henning Heikes and STV is
appreciated; this is a request, not an additional license condition.

Bundled third-party code retains its own licenses: Floating UI uses MIT,
D3 components use ISC/BSD-3-Clause, and ELK.js uses EPL-2.0. The distribution's
combined SPDX expression reflects these bundled components; it does not change
the MIT license of STV-owned code. See ``THIRD_PARTY_NOTICES.txt`` and
``vendor/ELK-SOURCE.txt`` in the packaged static assets. Generated views copy
these notices and ``LICENSE.txt`` alongside their browser assets.

The Sphinx documentation includes a Licensing page with the MIT text,
third-party notices and upstream source-availability information. This license
selection does not assert employer approval or resolve employment-related IP
ownership; those questions remain separate from the repository license.

Version maintenance
-------------------

The sole maintained STV version is ``src/sphinx_traceability_view/_version.py``.
Hatch reads it for distributions; Sphinx configuration, extension metadata and
the release runner derive their versions from it. The private frontend build
is unversioned. Replace the validator example's ``<major.minor>`` with the
documentation version. Historical release/review records and dependency versions
are immutable evidence, not values to update during a version bump.

Historical distributions
------------------------

Retained historical archives require the license supplement in
``docs/licensing/historical/`` (project MIT license, full third-party notices,
source references and archive hashes). Keep those materials with any copy.
Historical artifacts remain evidence; their original bytes are unchanged and
current documentation no longer offers them as binary downloads.

Source archive contents
------------------------

The source distribution uses an explicit file allowlist in ``pyproject.toml``.
It contains the Python implementation, prepared browser assets, editable browser
sources, audited legal inputs, frontend lock/build files and Python build inputs.
A wheel can be rebuilt from this archive without Node. Engineering documentation,
execution history and local build/tool environments remain in the repository;
they are not source-package inputs. Archive selection ignores VCS negations so
retaining execution logs in Git cannot accidentally publish them in a package.

Automated validation and provenance
-----------------------------------

GitHub workflows validate package/fixture changes with read-only tokens and
immutable action pins. A separate manual main-branch workflow prepares
checksummed candidate bytes and, for a public repository, build provenance.
Neither workflow publishes a release. ``docs/ci-and-provenance.rst`` describes
the check scope, verification commands and unapplied branch-protection proposal.
Hosted runs and protection activation remain separate owner steps.
