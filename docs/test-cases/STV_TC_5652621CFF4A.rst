interactive seed smoke
======================

.. test_case:: interactive seed smoke
   :id: STV_TC_5652621CFF4A
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_interactive_seed_smoke[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_038, STV_SHR_052, STV_SHR_053, STV_SWR_038, STV_SWR_056, STV_SWR_057
   :executed_by: STV_TE_542E4BF583AB9821, STV_TE_E5587901B2158B26
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_interactive_seed_smoke[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_interactive_seed_smoke[file]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_interactive_seed_smoke(browser,short_output,protocol):
          output=short_output/'seed-picker';result=build(FIXTURE,output)
          assert result.returncode==0,result.stderr
          with published_url(output,protocol) as url:
              browser.get(url);wait=WebDriverWait(browser,20)
              wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))==2)
              roots=browser.find_elements(By.CSS_SELECTOR,'.stv-view');root=roots[0]
              field=root.find_element(By.CSS_SELECTOR,'.stv-seed-picker input')
              field.send_keys('missing');field.send_keys(Keys.ENTER)
              assert field.get_attribute('aria-invalid')=='true'
              assert root.get_attribute('data-stv-revision')=='0'
              field.clear();field.send_keys('software detail')
              wait.until(lambda d:root.find_element(By.CSS_SELECTOR,'.stv-seed-matches').is_displayed())
              assert 'LEAF_B' in root.find_element(By.CSS_SELECTOR,'.stv-seed-matches').text
              field.send_keys(Keys.ARROW_DOWN);field.send_keys(Keys.ENTER)
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='1')
              assert [n.text for n in root.find_elements(By.CSS_SELECTOR,'.stv-id')]==['LEAF_B']
              assert roots[1].get_attribute('data-stv-revision')=='0'
              root.find_element(By.XPATH,'.//button[text()="Project overview"]').click()
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='2')
              assert len(root.find_elements(By.CSS_SELECTOR,'.stv-project'))==1
              assert [n.text for n in root.find_elements(By.CSS_SELECTOR,'.stv-id')]==['ROOT_A']
              centers=browser.execute_script("return [...arguments[0].querySelectorAll('.stv-node')].map(n=>parseFloat(n.style.left)+n.offsetWidth/2)",root)
              assert abs(centers[0]-centers[1])<1

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
