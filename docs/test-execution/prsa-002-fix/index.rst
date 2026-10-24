PRSA-002 development fix verification
=====================================

The owner authorized this security fix after confirming removal of hosted
GitHub releases. :need:`STV_PR_007` records the cause, scope and owner authority.
The extractor now discards authored transport markers and the inspector checks
restored URL/CSS resources independently. The shipped browser bundle is rebuilt.

**Results:** 33 passing cases: 11 Python (including six real Firefox cases over
file/HTTP), plus all 22 JavaScript cases. The new bypass regression requires no
marker execution or loopback requests and preserves local images, srcset,
links, styles and tables. Adjacent offline and alternate-model detail cases pass.
Initial fixture errors and their corrections are retained separately.

**Review and limits:** New case designs and the interface refinement await
owner review. Requirement verification fields and prior acceptance history
are unchanged. Full capacity, packaging and release qualification were not run;
no replacement release, tag or distribution was created. Other audit findings
remain outside this fix.

* :download:`Exact commands, environment and source hashes <verification.json>`
* :download:`Python/browser JUnit <pytest.xml>`
* :download:`Python/browser log <pytest.log>`
* :download:`JavaScript JUnit <node.xml>`
* :download:`Initial fixture attempt summary <initial-attempt.txt>`
* :download:`Case result mapping <case-results.json>`

.. toctree::
   :maxdepth: 1

   cases

Documentation and traceability checks
-------------------------------------

The Sphinx HTML build passed with warnings treated as errors. Strict executable
coverage reports 67 requirements and 86 executable cases with no unmapped active
requirements or unknown IDs. The shared traceability validator passed with
``--require-test-coverage`` and repository-relative evidence checks.

Commands, from the repository root:

.. code-block:: text

   .venv-implementation/Scripts/python.exe scripts/check-coverage.py --strict
   .venv-implementation/Scripts/python.exe -m sphinx -E -a -W --keep-going -b html docs docs/_build/prsa-002-html
   .venv-implementation/Scripts/python.exe <shared-skill>/scripts/validate_traceability.py docs/_build/prsa-002-html/needs.json --version 1.0 --repo-root . --require-test-coverage

``<shared-skill>`` is the existing reverse-engineer-requirements skill selected
by the project. The export key is Sphinx's major/minor ``version``; the product
version remains derived from its single maintained source.

* :download:`Successful Sphinx log <sphinx.log>`
* :download:`Successful traceability log <traceability.log>`
* :download:`Initial heading warnings, corrected before handover <sphinx-initial.log>`
* :download:`Initial incorrect export-key invocation <traceability-initial.log>`

The initial HTML build failed on short RST title underlines, then passed after
correction. The first validator invocation used the full development version
instead of the exported major/minor key; the corrected invocation passed.
