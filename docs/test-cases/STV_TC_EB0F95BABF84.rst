empty seed catalog
==================

.. test_case:: empty seed catalog
   :id: STV_TC_EB0F95BABF84
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_release_seeds.py :: docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SHR_053, STV_SWR_051, STV_SWR_052, STV_SWR_057
   :executed_by: STV_TE_EAB2D41B5168D79C, STV_TE_F4B5B1B6C6055FE4
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[http]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_empty_seed_catalog(browser,short_output,protocol):
          source=short_output/'source';shutil.copytree(FIXTURE,source)
          (source/'requirements.rst').write_text('Requirements\n============\n',encoding='utf-8')
          (source/'index.rst').write_text('Project\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view::\n',encoding='utf-8')
          output=short_output/'html';result=build(source,output);assert result.returncode==0,result.stderr
          with published_url(output,protocol) as url:
              browser.get(url);wait=WebDriverWait(browser,20)
              wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
              root=browser.find_element(By.CSS_SELECTOR,'.stv-view')
              assert 'No stakeholder requirements.' in root.text
              assert not root.find_elements(By.CSS_SELECTOR,'[data-focus="root"],[data-focus="Next"]')
              field=root.find_element(By.CSS_SELECTOR,'.stv-seed-picker input')
              field.send_keys('anything');field.send_keys(Keys.ARROW_UP);field.send_keys(Keys.ENTER)
              assert field.get_attribute('aria-invalid')=='true'
              assert field.get_attribute('aria-expanded')=='false'
              assert root.get_attribute('data-stv-revision')=='0'
              root.find_element(By.XPATH,'.//button[text()="Project overview"]').click()
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='1')
              assert len(root.find_elements(By.CSS_SELECTOR,'.stv-node'))==1

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
