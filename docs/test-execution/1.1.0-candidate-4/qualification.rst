STV 1.1.0 final qualification
=============================

Software baseline: ``41e57ed76c2acb521cdeb033f4be7b01fac50115``.
Final executable test baseline:
``3b32d6be34a8a5c3bea1f118e4b24cb919901a28``.
The owner requested completion of extended qualification before publication,
then authorized continuing the release. No publication is asserted by this
pre-publication execution record; successful hosted checks remain required.

Observed results
-----------------

* **229 automated cases passed: 187 Python and 42 JavaScript**, with zero
  failures, errors or skips, in one complete final selection. The Python wrapper
  additionally checks two Node reset scenarios; these are not added again to
  the 229-case total.
* All **120 current canonical cases** have actual execution evidence; seven
  infrastructure checks are retained separately. The four occurrence-mode
  cases remain explicitly deferred. Acceptance statuses are preserved.
* A fresh offline Python **3.10.9** installation of the exact candidate wheel
  passed dependency checks, installed-package import, the CI runtime command
  and a separate clean Sphinx host build. Main qualification used Python
  **3.13.17**, Windows 11 and Firefox **158.0.1** / geckodriver **0.37.1**.
* The 30,000-Need / 90,000-link host fixture was reused only after checking
  exact wheel, runtime/source, dependency, toolchain and fixture equivalence.
  Current browser capacity measurements ran again; this is not a new host build.
* The four 200-node / ten-card SVG checks at wide/narrow widths and file/HTTP
  remain applicable through exact product and fixture byte equivalence.
  Their original timestamps, files and hashes remain in candidate 2.
* Real visible-hover export passed separately on file and HTTP, retaining all
  fully visible source words after the live hover closed. Source/reopened
  screenshots were inspected; the source and SVG geometry checks remain linked.
* The owner observed native Save As, folder selection and cancellation, then
  confirmed readable, usable cards/tooltips and keyboard scrolling at 125%
  and 150% zoom in Firefox 158.0.1 (64-bit). These are owner observations,
  distinguished from agent-run browser assertions.
* Fresh inspection confirms **16 distinct archive identities** and complete
  licensing supplements. Issued 1.0.0 distributions remain unchanged.

The original runner returned nonzero only because its initial documentation
build found two newly added evidence pages missing from a toctree. The entries
were corrected without modifying product or executable test inputs. The failed
log and original result remain intact; final strict documentation and evidence
checks are retained separately in ``final-validation.json``. Only scoped
verification metadata changes after the full run; criteria and acceptance
statuses are unchanged.

Candidate history
------------------

Candidate 1 is rejected for :need:`STV_PR_016`, missing graph nodes in exported
SVGs. Candidate 2 fixes that defect and passed its 196-case selection, clean
minimum-runtime check and maximum-size supplements. Candidate 3 adds extended
procedures but its Node wrapper expected a different default reporter format:
228 passed and one test-wrapper failure. Its actual two Node assertions passed.
Explicit TAP output corrects the wrapper in the committed final test baseline;
candidate 4 passes all 229 executable cases. Failed attempts are retained.

The source and wheel rebuilt for candidates 2, 3 and 4 are byte-identical.
Publish only the final selected assets below; older candidate-1 copies in
``dist`` are rejected and remain retained for history.

Exact publication assets
-------------------------

.. code:: text

   4cfed985248b3f328d46c5ffb57a15b5c4d89c9be0f4296e0c3568bba18549eb  sphinx_traceability_view-1.1.0-py3-none-any.whl
   6e964833b68488b722bc761a0116155e589b3928813abeaa8d61a5824bf73785  sphinx_traceability_view-1.1.0.tar.gz

The final GitHub Release must carry these exact distributions and their
``SHA256SUMS`` before publication. The isolated workflow validates the tagged
source/assets, publishes to PyPI through Trusted Publishing, then deploys the
matching documentation. The first live PyPI/Pages run is a publication-time
check, not something the local tests can prove.

.. toctree::
   :maxdepth: 1

   extended-qualification
   cleanup-review

Evidence
---------

* :download:`Final local gates <final-validation.json>`
* :download:`Canonical selector results <case-results.json>`
* :download:`Recorded test baseline <test-baseline.json>`
* :download:`Capacity reuse proof <capacity-reuse.json>`
* :download:`Fresh runtime commands <supplement-commands.json>`
* :download:`Historical licensing check <historical-check.json>`
* :download:`Verification assessment <verification-assessment.json>`
* :download:`Exact checksums <artifacts/SHA256SUMS>`

Scope remains Windows/Firefox on file and HTTP. Additional OS/browser versions,
mobile/touch optimization and universal vector-editor support are not claimed;
occurrence mode remains deferred. Optional cleanup is proposed only. Nothing
was deleted; all distributions and evidence remain, and the post-release
workspace review remains due after publication.
