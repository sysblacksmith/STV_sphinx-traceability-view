PRSA-004 source archive boundary verification
================================================================================

The owner authorized the next finding after committing earlier remediations.
:need:`STV_PR_010` records scope, cause and the revised packaging policy.
This is development verification, not a release qualification or publication.

Results and identities
--------------------------------------------------------------------------------

The regression initially failed with the previous configuration. Its actual
archive contains ``docs/test-execution/private/probe.log`` despite the intended
exclusion. With an explicit allowlist and VCS-independent selection, it passes:
none of the seeded execution/build/audit/tool/cache files or local-only sentinel
bytes appear in the produced archive. Required source, legal and build inputs
remain present. A wheel rebuilt from that archive retains identical assets and
notices.

The actual development sdist from the checkout contains **66 files**, zero
execution-history files and zero logs. Its rebuilt wheel passes the existing
isolated offline installation/Sphinx host test without Node. Latest results:
**two passing cases**, with the expected pre-fix failure preserved separately.
Exact artifact hashes, member inventories and source identities are below.
The runtime, frontend bundle and maintained version are unchanged.

Scope and review limits
--------------------------------------------------------------------------------

Engineering documentation and execution history remain in the repository rather
than in the source package. Historical archives/results are unchanged. The new
archive policy and regression design await owner review. Requirement verification
and prior acceptance records are not promoted. No broader browser/capacity run,
new release, commit, tag, push or publication was performed. PRSA-005 and later
remain outside this fix.

Evidence
--------------------------------------------------------------------------------

* :download:`Commands, baseline and source hashes <verification.json>`
* :download:`Before-fix log <before.log>`
* :download:`Before-fix JUnit <before.xml>`
* :download:`Confirmed leaked execution-log member <before-members.json>`
* :download:`After-fix log <after.log>`
* :download:`After-fix JUnit <after.xml>`
* :download:`Fixture archive members <archive-check/members.json>`
* :download:`Fixture build hashes <archive-check/artifacts.json>`
* :download:`Actual development build <build.log>`
* :download:`Actual archive inventory and build hashes <actual-archive.json>`
* :download:`Offline consumer log <package.log>`
* :download:`Offline consumer JUnit <package.xml>`
* :download:`Installed consumer identity <consumer/identity.txt>`
* :download:`Installed consumer environment <consumer/environment.txt>`
* :download:`Case result mapping <case-results.json>`

.. toctree::
   :maxdepth: 1

   cases

Documentation and traceability
--------------------------------------------------------------------------------

The Sphinx HTML build passes with warnings treated as errors. Strict executable
coverage reports 67 requirements, 87 executable cases and no unmapped active
requirements or unknown IDs. The shared validator passes full requirement-test
coverage and repository-relative evidence checks. These checks do not confer
owner acceptance or release readiness.

* :download:`Successful Sphinx build <sphinx.log>`
* :download:`Successful traceability validation <traceability.log>`

Commands from the repository root (``<shared-skill>`` is the configured
reverse-engineer-requirements skill):

.. code-block:: text

   .venv-implementation/Scripts/python.exe scripts/check-coverage.py --strict
   .venv/Scripts/python.exe -m sphinx -E -a -W --keep-going -b html docs docs/_build/html
   .venv-implementation/Scripts/python.exe <shared-skill>/scripts/validate_traceability.py docs/_build/html/needs.json --version 1.0 --repo-root . --require-test-coverage
