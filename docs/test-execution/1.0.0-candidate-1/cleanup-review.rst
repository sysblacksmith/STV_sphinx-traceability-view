Workspace cleanup review
========================

Status: **owner approved all 14 listed paths; all 14 removed successfully**. Sizes are logical bytes measured on 2026-10-24T12:07:52.542551+00:00.

.. list-table:: Exact approved and removed paths
   :header-rows: 1

   * - Project-relative directory (entire subtree)
     - Bytes
     - Reason / rebuild consequence
   * - ``.pytest_cache/``
     - 7785
     - Reproducible pytest cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``__pycache__/``
     - 2798
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``docs/test-scripts/__pycache__/``
     - 137700
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/__pycache__/``
     - 16283
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/bundle/__pycache__/``
     - 1817
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/bundle/tests/__pycache__/``
     - 2308
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/detail_build/__pycache__/``
     - 5627
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/detail_build/tests/__pycache__/``
     - 9263
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/directive/__pycache__/``
     - 7829
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/directive/tests/__pycache__/``
     - 4064
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/graph/__pycache__/``
     - 3261
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/graph/tests/__pycache__/``
     - 4857
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/model/__pycache__/``
     - 3336
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.
   * - ``src/sphinx_traceability_view/model/tests/__pycache__/``
     - 3064
     - Reproducible Python bytecode cache. Cache recreated on the next test/import; no product source or retained evidence is removed.

Logical size of removed cache content: **209,992 bytes** across 14 directories. Physical disk reclamation may differ from logical sizes. The original measured proposal is preserved in cleanup-proposal.json.

Checked Git status including ignored files, staged/unstaged diffs, packaging exclusions, test collection, release runner, README and evidence download references. Proposed cache directories are interpreter/pytest output, not referenced delivery inputs. The qualification runner has finished; no release run is using the proposed caches.

Retained data
-------------

* ``dist/ (all versions)``
* ``docs/test-execution/ (all candidate histories and artifacts)``
* ``.venv/``
* ``.venv-implementation/``
* ``frontend/node_modules/``
* ``docs/_build/wheelhouse/``
* ``docs/_build/html/``
* ``docs/_build/release-benchmark/1.0.0-candidate-1/ (current measured fixture)``

Other processes were not terminated or assumed disposable. No benchmark, temporary installation, backup, or loose log is proposed for manual deletion. Existing test-managed temporary-directory lifecycles were left unchanged.

The owner explicitly approved the exact 14 listed directories in the chat reply. All resolved paths were verified inside the project; all removals succeeded.
Only the approved caches were deleted. No staging, committing or tagging was performed. Intended release changes remain uncommitted.
Post-release cleanup review remains due when publication is known.

* :download:`Inventory and exact proposal <cleanup-proposal.json>`

* :download:`Approved cleanup outcome <cleanup-result.json>`
