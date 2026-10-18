Interactive traceability view
=============================

Specification for a Sphinx-Needs extension providing interactive traceability
exploration. Accepted stakeholder baseline v1 is in ``docs/stakeholder.rst``.
Draft internal requirements are in ``docs/system.rst`` and ``docs/software.rst``;
proposed architecture, interfaces and ADRs are indexed in the documentation.
Design review gaps are recorded in ``docs/review.rst``. Runtime implementation
has not started.

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
pins are alongside them. These are design inputs, not an implemented package.
