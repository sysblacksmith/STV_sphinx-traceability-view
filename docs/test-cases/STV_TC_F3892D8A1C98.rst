seed layout replacement failure and staleness
=============================================

.. test_case:: seed layout replacement failure and staleness
   :id: STV_TC_F3892D8A1C98
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_release_seeds.py :: docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_044, STV_SHR_053, STV_SWR_044, STV_SWR_057
   :executed_by: STV_TE_CDCABD8ACB9C2964, STV_TE_B65229E135C87272
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[http]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_seed_layout_replacement_failure_and_staleness(browser,short_output,protocol):
          from pathlib import Path
          project=Path(__file__).parents[1]
          script="import{build}from'esbuild';await build({entryPoints:[process.argv[1]],bundle:true,format:'iife',outfile:process.argv[2]})"
          result=subprocess.run(['node','--input-type=module','-e',script,str(project/'docs/test-scripts/fixtures/browser-harness.js'),str(short_output/'harness.js')],cwd=project/'frontend',capture_output=True,text=True)
          assert result.returncode==0,result.stderr
          (short_output/'index.html').write_text('<link rel="stylesheet" href="'+(project/'src/sphinx_traceability_view/static/stv.css').as_uri()+'"><div class="stv-view" id="test-view" data-stv-seeds=\'["A"]\'></div><script src="harness.js"></script>',encoding='utf-8')
          with published_url(short_output,protocol) as url:
              browser.get(url);_assert_async_layout(browser)
              wait=WebDriverWait(browser,20);root=browser.find_element(By.CSS_SELECTOR,'.stv-view')
              field=root.find_element(By.CSS_SELECTOR,'.stv-seed-picker input')
              previous=root.find_element(By.CSS_SELECTOR,'.stv-scene').get_attribute('style')
              field.send_keys('B');field.send_keys(Keys.ENTER)
              wait.until(lambda d:d.execute_script('return calls.length')==7)
              browser.execute_script('calls[6].reject(Error("Seed layout failure"))')
              wait.until(lambda d:'Seed layout failure' in root.find_element(By.CSS_SELECTOR,'.stv-status').text)
              assert root.get_attribute('data-stv-revision')=='2'
              assert root.find_element(By.CSS_SELECTOR,'.stv-scene').get_attribute('style')==previous
              assert browser.switch_to.active_element==field
              for identity,count in [('A',8),('B',9)]:
                  field.send_keys(Keys.CONTROL,'a');field.send_keys(Keys.BACKSPACE);field.send_keys(identity);field.send_keys(Keys.ENTER)
                  wait.until(lambda d:d.execute_script('return calls.length')==count)
              browser.execute_script('stvHarness.compute(...calls[8].args).then(calls[8].resolve)')
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='3')
              browser.execute_script('stvHarness.compute(...calls[7].args).then(calls[7].resolve)')
              wait.until(lambda d:d.execute_script('return document.querySelectorAll(".stv-measure").length')==0)
              assert root.get_attribute('data-stv-revision')=='3'
              assert [n.text for n in root.find_elements(By.CSS_SELECTOR,'.stv-id')]==['B']
              assert browser.switch_to.active_element==field

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
