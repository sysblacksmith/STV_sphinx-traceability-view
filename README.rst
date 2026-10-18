Interactive traceability view
=============================

Draft requirements for a Sphinx-Needs extension providing interactive
traceability exploration. The canonical stakeholder requirements are in
``docs/stakeholder.rst``; unresolved questions are in ``docs/review.rst``.

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

Once downstream requirements and allocations exist, run the shared validator::

   .\.venv\Scripts\python.exe <shared-skill>/scripts/validate_traceability.py docs/_build/html/needs.json --version 0.1 --repo-root .

The current stakeholder-only draft cannot pass full downstream coverage checks.
An HTML build does not establish acceptance or semantic traceability coverage.
