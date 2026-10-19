async layout failure and stale completion
=========================================

.. test_case:: async layout failure and stale completion
   :id: STV_TC_9E5477EFE2F1
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_browser.py :: tests/test_browser.py::test_async_layout_failure_and_stale_completion[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_044, STV_SHR_047, STV_SWR_044, STV_SWR_052
   :executed_by: STV_TE_D099D363BCFCAD31, STV_TE_5DCC25155978FEA9
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_browser.py::test_async_layout_failure_and_stale_completion[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_browser.py::test_async_layout_failure_and_stale_completion[file]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_async_layout_failure_and_stale_completion(browser,short_output,protocol):
          project=Path(__file__).parents[1]
          script="import{build}from'esbuild';await build({entryPoints:[process.argv[1]],bundle:true,format:'iife',outfile:process.argv[2]})"
          result=subprocess.run(['node','--input-type=module','-e',script,str(project/'tests/fixtures/browser-harness.js'),str(short_output/'harness.js')],cwd=project/'frontend',capture_output=True,text=True)
          assert result.returncode==0,result.stderr
          (short_output/'index.html').write_text('<link rel="stylesheet" href="'+(project/'src/sphinx_traceability_view/static/stv.css').as_uri()+'"><div class="stv-view" id="test-view" data-stv-seeds=\'["A"]\'></div><script src="harness.js"></script>',encoding='utf-8')
          # Keep the host alive across all injected completions.
          with published_url(short_output,protocol) as url:
              browser.get(url)
              _assert_async_layout(browser)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
