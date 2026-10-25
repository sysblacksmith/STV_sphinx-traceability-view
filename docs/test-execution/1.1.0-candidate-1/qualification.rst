1.1.0 candidate qualification
==============================

The candidate is based on ``9dd462b5df9e0e5433d6c973f43b2a33fb8973ee`` plus the retained worktree
identity ``b54c8f64cf420cfbb01a1ebae331dfd7891abf8a60e802881d1bac9c3ae2a5fa``. No historical record was overwritten.

Disposition: rejected after supplemental SVG inspection
-------------------------------------------------------

**Do not publish this candidate.** The original executable selection passed,
but supplemental inspection found :need:`STV_PR_016`: visible graph nodes can
be missing from the SVG. The old runtime fails the permanent overflow/graph
regression; the corrected runtime passes all four existing export variants.
The original results and exact candidate-1 archives remain immutable evidence.
A fresh candidate 2 must qualify the changed product and test inputs.

The earlier supplemental count/layout assertion errors remain retained. The
narrow diagnostic's completion is not a fidelity pass; its missing graph text
is evidence of this defect. Native/dialog/manual limitations below are retained.

Executed gates
--------------

* One complete selection: **154 Python and 42 JavaScript cases passed**;
  zero failures, errors or skips. Source/test inputs remained stable during
  that run. Exact commands, timestamps, environment and selectors are retained.
* The exact wheel also passed clean installed Python 3.10 runtime checks,
  including pip check, module identity and Sphinx usage without checkout imports.
* Windows 11, Python 3.13.17, Firefox 158.0.1 and geckodriver 0.37.1 are the
  recorded main environment. File and nested static HTTP workflows were executed.
* A fresh 30,000-Need / 90,000-link fixture built in 316.80 seconds.
  Both browser transports were measured three times. Median startup was
  532.1 ms from disk
  and 554.2 ms over HTTP.
  No agreed numeric performance budget exists; these are observations.
* Strict Twine validation, both long descriptions, source-to-wheel rebuild,
  isolated offline installation, clean Sphinx publication, workflow policy,
  requirement graph and published diagram links passed.
* 14 archive identities and the complete historical licensing
  supplement were freshly inspected. Issued 1.0.0 archives remain unchanged.
* 120 canonical execution aggregates retain observed current results; seven
  additional publication/infrastructure checks are reported separately.

Scope and remaining limits
--------------------------

This is a passing **automated release selection**, not proof that every extended
scenario in the accepted case designs was executed. CR015-018 requirement and
case verification remains partial for that reason. Native Save As dialogs,
200-node SVG export with all complex detail/resource combinations, every timing
race and the complete extended manual procedures are not all qualified by this
selection. Owner feature feedback is useful acceptance evidence but is not
relabeled as a detailed automated execution.

Additional browsers/operating systems and mobile/touch qualification remain
outside the recorded Windows/Firefox boundary. Occurrence-mode procedures
STV_TC_SY_041 through STV_TC_SY_044 remain deferred. Existing static third-party
widget limitations remain. Browser-managed save-location settings are documented.

The owner must review these limits before a final release decision. The new
release publishing workflow has local policy/artifact checks but has not yet
performed a live PyPI or Pages publication. The owner reports its Trusted
Publisher and environment tag rules configured. No tag or release is created
by this qualification record.

Exact candidate artifacts
-------------------------

.. code:: text

   bb0c64d44c056b5a8d7fb9945775f628586e5a340fbebc56f75ca66527d87b74  sphinx_traceability_view-1.1.0-py3-none-any.whl
   37e6b1e586fd4436de9dcdf7f9fa6d9a1b17bc7210d6793e363375f02b43633b  sphinx_traceability_view-1.1.0.tar.gz

The retained source archive and wheel, not later rebuilds, are the proposed
publication inputs. ``scripts/release.py`` validates their tag/version,
checksums, metadata and source contents before the hosted workflow publishes.

Supporting evidence
-------------------

* :download:`Minimum-runtime commands <supplement-commands.json>`
* :download:`Historical archive inspection <historical-check.json>`
* :download:`Runtime equivalence <runtime-equivalence.json>`
* :download:`Canonical selector mappings <case-results.json>`
* :download:`Infrastructure results <infrastructure-results.json>`
* :download:`Source archive <artifacts/sphinx_traceability_view-1.1.0.tar.gz>`
* :download:`Exact checksums <artifacts/SHA256SUMS>`

:doc:`cleanup-review` lists an optional 1.190 GiB cleanup proposal. Nothing was
deleted; current artifacts, evidence, benchmark, environments and wheelhouse are
retained. Post-release cleanup review remains due if publication proceeds.
