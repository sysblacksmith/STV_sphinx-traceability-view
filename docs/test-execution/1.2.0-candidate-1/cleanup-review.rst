Workspace cleanup review
========================

No approved cleanup had been performed when this proposal was issued. This is a concrete optional cleanup proposal after
all active qualification consumers finish. Post-release review remains due
when publication completes. All distributions, evidence and normal development
environments/dependencies are retained. Both Python environments use a base
interpreter outside disposable build output.

.. list-table:: Reproducible output eligible for cleanup
   :header-rows: 1

   * - Project-relative path
     - MiB
     - Rebuild consequence
   * - ``docs/_build/ci-runtime``
     - 6.44
     - Recreate capacity host, offline wheelhouse or temporary consumer as needed
   * - ``docs/_build/release-benchmark``
     - 410.64
     - Recreate capacity host, offline wheelhouse or temporary consumer as needed
   * - ``docs/_build/release-runtime310``
     - 122.99
     - Recreate capacity host, offline wheelhouse or temporary consumer as needed
   * - ``docs/_build/test-map.json``
     - 0.04
     - Recreate capacity host, offline wheelhouse or temporary consumer as needed
   * - ``docs/_build/wheelhouse``
     - 25.38
     - Recreate capacity host, offline wheelhouse or temporary consumer as needed
   * - ``src/sphinx_traceability_view/__pycache__``
     - 0.00
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/bundle/__pycache__``
     - 0.00
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/bundle/tests/__pycache__``
     - 0.01
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/detail_build/__pycache__``
     - 0.03
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/detail_build/tests/__pycache__``
     - 0.04
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/directive/__pycache__``
     - 0.02
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/directive/tests/__pycache__``
     - 0.01
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/graph/__pycache__``
     - 0.01
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/graph/tests/__pycache__``
     - 0.03
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/model/__pycache__``
     - 0.01
     - Python recreates it on next import
   * - ``src/sphinx_traceability_view/model/tests/__pycache__``
     - 0.02
     - Python recreates it on next import
   * - ``docs/test-scripts/__pycache__``
     - 1.06
     - Python recreates it on next import
   * - ``scripts/__pycache__``
     - 0.05
     - Python recreates it on next import
   * - ``tools/method/tooling/__pycache__``
     - 0.03
     - Python recreates it on next import
   * - ``.pytest_cache``
     - 0.02
     - Recreated by subsequent tests/imports
   * - ``__pycache__``
     - 0.01
     - Recreated by subsequent tests/imports
   * - ``docs/__pycache__``
     - 0.00
     - Recreated by subsequent tests/imports
   * - ``docs/test-execution/1.2.0-candidate-1/__pycache__``
     - 0.03
     - Recreated by subsequent tests/imports

Total proposed space: **566.88 MiB**.

Retained: current HTML, all of ``dist/``, canonical execution records,
source/test inputs, original problem attachments, ``next_steps.rst``, security
audit records, normal virtual environments and frontend dependencies.

* :download:`Full inventory and Git status <workspace-inventory.json>`

Cleanup execution
-----------------

The owner approved this exact list after testing on 2026-11-01. Removed **566.88 MiB** from 23 listed paths. There were 0 failed removals. The current 2174 HTML files, 37 distribution files and 123 canonical evidence files were verified unchanged by SHA-256. Only current HTML remains under ``docs/_build``. Task-created raw SVG duplicates were separately retained in a verified lossless archive. The normal development environments remain usable; future capacity/offline tests must regenerate the host and reprovision the wheelhouse.

* :download:`Cleanup receipt, preservation hashes and final inventory <cleanup-receipt.json>`
* :download:`Minimum-runtime dependency versions <runtime310-environment.txt>`
* :download:`Supplemental runtime wheel hashes <supplement-runtime-wheel-hashes.json>`
