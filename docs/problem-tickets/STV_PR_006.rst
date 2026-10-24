Problem 6: Detail tooltips fail on long Windows paths
================================================================================

.. problem_report:: Detail tooltips fail on long Windows paths
   :id: STV_PR_006
   :status: analyzed
   :basis: owner
   :evidence: docs/problem-tickets/STV_PR_006.rst
   :priority: unassigned
   :verification_state: partial

   **Reporter/date:** Project owner, 2026-10-19.

   **Observed behavior:** Opening a node's detail tooltip consistently displays
   ``Local detail asset unavailable.`` instead of the published object body.
   The graph itself renders. The owner reports that the feature worked on
   another machine and initially suspected a machine-specific link setting.

   **Expected behavior:** Detail tooltips load their generated local assets
   when the built documentation is opened directly from disk, including from
   a nested Windows checkout. No machine-specific link customization should
   be required.

   **Original report:** "please check why the data tool tip feature does not
   work. it awlays drops a Local detail asset nt available error... it worked
   ion my other machine. i suspect a not properly customized link"

   **Reproduction and environment:** Windows; project documentation version
   0.2.0; VS Code integrated Chromium browser; direct ``file://`` navigation.
   Exact Windows and browser versions were not recorded. Before the local
   diagnostic change:

   #. Use the affected checkout at
      ``C:\Users\HH73SI\OneDrive - Bosch Group\PersonalDrive\LOKAL\REPOS\STV_sphinx-traceability-view``.
   #. Build documentation with ``.\build-docs.ps1``.
   #. Open ``docs/_build/html/demo.html`` directly from disk.
   #. Activate the details control for ``STV_SHR_001``.
   #. Observe the error in the detail panel and a failed request for the
      generated ``_static/stv/details/<identity-hash>-<content-hash>.js`` asset.

   **Root cause:** ``src/sphinx_traceability_view/bundle/__init__.py::emit`` generated
   each detail filename from two full SHA-256 hashes: the object identity hash
   and the fragment content hash. The filename alone was 132 characters.
   In this checkout the resulting absolute detail asset path was 263
   characters, beyond the traditional Windows 260-character path limit.
   The files existed on disk, but the browser rejected the local script load
   with ``net::ERR_UNEXPECTED``. Python successfully creating the files did
   not establish that the browser could load them.

   ``frontend/src/inspect/inspect.js::loadDetail`` received the script error event and
   displayed its generic asset-unavailable message. The generated URL resolved
   to the correct file; the Sphinx base URL and ``docs/conf.py`` link settings
   were not the cause. A shorter checkout path is consistent with the owner's
   other-machine observation, but that machine's environment was not checked.

   **Local diagnostic change, not a master-branch disposition:** Detail
   filenames now use only the full fragment content hash:
   ``_static/stv/details/<content-hash>.js``. This removes 65 characters,
   reducing the affected absolute paths from 263 to 198 characters without
   truncating the content hash. Identical fragments share one asset, matching
   their existing content-hash registration keys. The documentation was
   rebuilt to update graph references. This working-tree change is a proven
   candidate fix, not evidence of integration or release on master.

   **Affected artifacts:** :need:`STV_SWE_BUNDLE` and
   :need:`STV_SWE_INSPECT`; ``src/sphinx_traceability_view/bundle/__init__.py``,
   ``frontend/src/inspect/inspect.js`` and ``src/sphinx_traceability_view/bundle/tests/test_bundle.py``.

   **Actual checks on 2026-10-19:**

   * Before the change, browser activation of ``STV_SHR_001`` reproduced the
     exact tooltip error and ``net::ERR_UNEXPECTED`` on its 263-character
     detail asset path.
   * After the change and rebuild, the same page and control displayed the
     published requirement body with no failed requests during that check.
   * ``.\build-docs.ps1`` completed successfully.
   * ``.venv/Scripts/python.exe -m pytest src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_detail_assets_use_only_content_hash_for_portable_paths -q``
     passed: one test. It checks filename length by the full-content-hash-only
     naming contract, shared-fragment deduplication, graph references and
     generated registration content.
   * The existing Node-dependent bundle test could not execute because
     Node.js was unavailable on PATH. Full browser regression, HTTP transport,
     other browsers and the other machine were not verified in this session.

   **Acceptance criteria for the master fix:**

   #. Reproduce the failure on Windows with an existing generated asset whose
      absolute local path exceeds 260 characters under the old naming scheme.
   #. Keep generated asset paths compact without weakening content identity;
      preserve graph-to-detail references and shared-fragment registration.
   #. Rebuild and verify tooltip content over ``file://`` in the affected
      nested checkout, including a documentation page below the output root.
   #. Verify HTTP loading and the existing missing-asset error/retry behavior.
   #. Run the focused bundle tests and applicable browser regressions with
      their prerequisites available. Record supported path limits explicitly;
      shortening filenames does not guarantee arbitrary-depth paths work.

   **Disposition:** Analyzed; awaiting the proper master-branch implementation,
   regression verification and integration decision. Preserve the local
   before/after evidence when implementing the fix. Do not mark this report
   fixed solely because the diagnostic working-tree change succeeds locally.