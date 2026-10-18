Interactive traceability view
=============================

Sphinx-Needs extension providing offline interactive traceability exploration.
Requirements and architecture are indexed in ``docs/index.rst``.
Project maturity and review records are maintained in ``docs/maturity.rst``.

Build documentation
-------------------

Run the PowerShell script using the project's existing ``.venv`` (Python 3.10+).
On the first run, install the pinned documentation dependencies and build::

   .\build-docs.ps1 -InstallDependencies

For subsequent builds::

   .\build-docs.ps1

The script works independently of the current working directory, treats Sphinx
warnings as errors, and returns a nonzero exit code on failure. Successful output
is written to ``docs/_build/html/index.html``. Virtual environment activation is
not required.

The configuration imports the shared model, status-chart extension and styling
directly, and includes the live central method. It discovers the shared skill
under an ancestor's ``#agents/skills`` or ``~/.agents/skills``. To select another
location, set ``REQUIREMENTS_SKILL_DIR`` to the shared
``reverse-engineer-requirements`` skill directory. Its repository-level
``method.md`` must also be present.

After building, run the shared validator (replace ``<shared-skill>`` with the
selected reverse-engineer-requirements skill directory)::

   .\.venv\Scripts\python.exe <shared-skill>/scripts/validate_traceability.py docs/_build/html/needs.json --version 0.1 --repo-root . --csv docs/_build/traceability.csv

The internal specification includes conventional and channeled derivation paths,
allocations and containment. Graph validation establishes structural checks;
it does not establish semantic correctness, internal design acceptance or
successful runtime verification.

Architecture diagrams
---------------------

Keep each .drawio source and its same-named .svg export together in
``docs/architecture/diagrams``. Edit the Draw.io source and export SVG only::

   .\scripts\export-architecture.ps1

Both scripts in ``scripts/`` are symbolic links to the shared
``#agents/skills/reverse-engineer-requirements/scripts`` tooling. Preserve these
links and the shared checkout when setting up the workspace; Windows link
creation may require Developer Mode or administrator rights.

The export script uses Draw.io and restores portable links from each paired
Draw.io source. It accepts ``-ProjectRoot`` and ``-DiagramDirectory`` for other
project layouts. To validate the published targets after building::

   .\.venv\Scripts\python.exe scripts/normalize-diagram-links.py --diagram-dir docs/architecture/diagrams --published-dir docs/_build/html

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

Install STV as a Python package in the consuming project's documentation
environment, then use its directive in that project's RST pages. Consumers
need the wheel and its Python dependencies; they do not need this repository,
the shared ``#agents`` checkout, Draw.io or Node.

1. Download the wheel (``.whl``) for the desired release from
   `GitHub Releases <https://github.com/sysforger/STV_sphinx-traceability-view/releases>`_.
   The repository is private, so downloading requires an account with repository
   access. For an unpublished local build, use the wheel generated in ``dist/``.
   From the download directory, using the consuming project's documentation
   Python environment, install the wheel::

      python -m pip install ./sphinx_traceability_view-<version>-py3-none-any.whl

   Replace ``<version>`` with the downloaded release version; the placeholder
   is not a literal shell argument. For repeatable developer and CI setup,
   select a specific release and download its wheel to a consistent relative
   location before installing. CI needs authenticated access to this private
   repository. Keep credentials out of requirements files and committed URLs.

2. Add the extension to the existing ``extensions`` list in ``conf.py``::

      extensions = [
          # Keep the project's existing extensions here.
          "sphinx_traceability_view",
      ]

   STV loads Sphinx-Needs automatically. Keep the project's existing Need types
   and relationships: they remain authoritative.

3. Add a page to the project's toctree and embed a project-root view::

      Traceability
      ============

      .. traceability-view::

   Alternatively, start from specific existing Need IDs::

      .. traceability-view:: MY_SHR_001 MY_SWE_BACKEND

   Replace these example IDs with IDs from the consuming project. Multiple
   views can appear on the same page.

4. Build the documentation normally using Sphinx's HTML builder, for example::

      python -m sphinx -b html docs docs/_build/html

   STV writes the graph data, lazy detail bundles, JavaScript and CSS into the
   HTML output. Distribute the complete output directory as static documentation.
   Readers need only a browser; no Python, Node or separate application server
   is required. Static HTTP hosting and direct opening from disk are supported.

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

The current package requires Python 3.10 or newer and pins Sphinx 8.1.3,
Sphinx-Needs 8.2.0 and Beautiful Soup 4.13.5. Check compatibility with the host's
documentation dependencies before installation. Only the ``html`` builder is
supported when a traceability view is present. Each view supports up to 200
visible graph nodes. On Windows, use a short HTML output path when opening
files directly in Firefox.

No project license has been assigned; resolve that decision before external
distribution.

Development verification
------------------------

Verify development changes::

   .\.venv-implementation\Scripts\python.exe -m pytest -m "not browser"
   node --test frontend/test/*.test.js
   .\.venv-implementation\Scripts\python.exe scripts/check-coverage.py --strict

For Firefox verification set ``STV_GECKODRIVER`` to an explicitly provisioned
driver and run ``pytest tests/test_browser.py`` in the implementation environment.
The packaging test needs a built wheel and an offline runtime wheelhouse at
``docs/_build/wheelhouse``. Source tests, release results and deferred criteria
are linked from the central maturity page. No project license has been assigned;
the owner must resolve that decision before external distribution.
