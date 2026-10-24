Historical licensing and toolchain remediation
================================================================================

Development work authorized for :need:`STV_PR_008` (PRSA-001) and
:need:`STV_PR_009` (PRSA-003). Prior PRSA-002 implementation is retained and
included in regression. No release, tag, commit or publication is performed.
The owner removed former hosted Releases; retained history receives a complete
:doc:`historical license supplement <../../licensing/historical/index>`.

Changes and verification scope
--------------------------------------------------------------------------------

Ten distinct retained historical archives have matching audited ELK fingerprints.
One historical frontend lock dependency set was found across available Git
history. The full notices and source references therefore apply to those
versions. Thirteen historical archive download roles were retired; 24 generated
binary copies were moved to ignored local quarantine, preserving their hashes.
Original archives, test results and Git history are unchanged.

Both active environments now use Python 3.13.17 with patched certifi, pip and
setuptools. Documentation uses Pillow 13 and implementation uses pytest 9.
Exact maintained pins remain in the requirements files. Documentation/test
tooling requires Python 3.11+; base package runtime remains Python 3.10+.
The offline wheelhouse was resolved separately on actual Python 3.10 and 3.13.
Inactive former environments/wheelhouse are retained locally as old evidence.
They are not used by the build/test scripts or published as dependency supplies.

The initial requirements install failed on a pre-existing first-line encoding
marker; the requirements file was normalized and installation passed. The
first Python 3.10 offline attempt exposed an omitted version-marker dependency
(``tomli``), because cross-version pip resolution did not evaluate every marker
for the target interpreter. Resolving under both actual interpreters corrected
this; both attempts remain retained. Final checks are consolidated below.

Review and release limits
--------------------------------------------------------------------------------

The supplement, tooling documentation and new case designs await owner review.
Requirement verification and prior concept acceptance are unchanged. No capacity
qualification or new release readiness claim is made. PRSA-004 and later
findings await separate proposal approval. Removed hosted source archives were
not available for inspection and are not republished or described as repaired.

Retained evidence
--------------------------------------------------------------------------------

* :download:`Both active environments <environments.json>`
* :download:`Offline wheel identities <wheelhouse.json>`
* :download:`Current package advisory queries <advisories.json>`
* :download:`Official Python provenance <python-provenance.json>`
* :download:`Retired generated archive hashes <retired-downloads.json>`
* :download:`Initial requirements install error <install-implementation.log>`
* :download:`Corrected implementation install <install-implementation-retry.log>`
* :download:`Documentation install <install-docs.log>`
* :download:`Initial cross-version wheel resolution <wheelhouse-download.log>`
* :download:`Actual Python 3.10 wheel resolution <wheelhouse-runtime310.log>`
* :download:`Actual Python 3.13 wheel resolution <wheelhouse-runtime313.log>`
* :download:`Initial offline Python 3.10 attempt <runtime310-initial.json>`
* :download:`Offline Python 3.10 host checks <runtime310.json>`
* :download:`Development-only package build <development-build.log>`
* :download:`Python regression log <pytest.log>`
* :download:`Python JUnit results <pytest.xml>`
* :download:`JavaScript JUnit results <node.xml>`

Final development outcomes
--------------------------------------------------------------------------------

**84 regression cases passed:** 62 Python cases and all 22 JavaScript cases,
using the refreshed implementation environment. This includes the full existing
browser, Windows-path, host integration, package and legal-build-guard cases;
the two release capacity cases were excluded. The separate Python 3.10 offline
bootstrap/install/build and installed-module identity checks passed.
Both active environments pass ``pip check``. The final OSV query reports no
matches across both environments and all current wheelhouse package versions.
This is a point-in-time advisory check, not a guarantee against unknown flaws.

* :download:`Exact commands and source/artifact hashes <verification.json>`

The initial documentation build ran before the regression JUnit report existed
and failed on that missing download target. It is retained in
:download:`sphinx-initial.log <sphinx-initial.log>`. The corrected final build
runs after all linked results have been written.

Canonical case results
--------------------------------------------------------------------------------

84 regression outcomes and two standalone integration checks are linked below.
New and refined case designs await owner review; historical acceptance remains
in prior review records. No requirement verification field is promoted.

.. toctree::
   :maxdepth: 1

   cases

* :download:`Case-result mapping <case-results.json>`
* :download:`Historical supplement verification <historical-licenses.log>`

Final documentation and distribution checks
--------------------------------------------------------------------------------

The normal HTML output was rebuilt successfully with warnings treated as
errors. Its download tree contains zero historical STV wheels/source archives.
All five rendered supplement downloads exist and match the maintained source
files exactly. Strict executable coverage has no unmapped active requirements;
the shared validator passes repository-relative evidence checks and complete
requirement-to-test coverage. These structural checks are separate from owner
review and release approval.

* :download:`Successful Sphinx build <sphinx.log>`
* :download:`Successful traceability validation <traceability.log>`
* :download:`Rendered supplement/download checks <publication-checks.json>`
* :download:`Historical frontend lock identities <historical-frontend-locks.json>`

Validation command (``<shared-skill>`` is the configured
reverse-engineer-requirements skill):

.. code-block:: text

   .venv-implementation/Scripts/python.exe scripts/check-coverage.py --strict
   .venv-implementation/Scripts/python.exe <shared-skill>/scripts/validate_traceability.py docs/_build/html/needs.json --version 1.0 --repo-root . --require-test-coverage
