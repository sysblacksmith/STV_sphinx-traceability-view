control order smoke
===================

.. test_case:: control order smoke
   :id: STV_TC_06CC5EE46517
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_browser.py :: tests/test_browser.py::test_control_order_smoke[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_051, STV_SWR_055
   :executed_by: STV_TE_E9DF4EB84C2C809D, STV_TE_48E662C1225F4525
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_browser.py::test_control_order_smoke[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_browser.py::test_control_order_smoke[http]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_control_order_smoke(browser,protocol):
          published=Path(__file__).parents[1]/'docs/_build/html'
          with published_url(published,protocol) as url:
              browser.get(url.rsplit('/',1)[0]+'/demo.html')
              _exercise_control_order(browser)

   **Interaction procedure and observable outcomes:**

   .. code-block:: python

      def _exercise_control_order(browser):
          wait=WebDriverWait(browser,20)
          wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))==2)
          root=browser.find_elements(By.CSS_SELECTOR,'.stv-view')[1]
          def buttons():
              node=next(n for n in root.find_elements(By.CSS_SELECTOR,'.stv-node')
                        if n.find_element(By.CSS_SELECTOR,'.stv-id').text=='STV_SWR_001')
              return node.find_elements(By.CSS_SELECTOR,'.stv-groups button')
          def identities():
              return [json.loads(b.get_attribute('data-focus'))[1:] for b in buttons()]
          expected=[['derives_from','outgoing'],['verifies','incoming'],['allocated_to','outgoing']]
          assert identities()==expected
          buttons()[0].click()
          wait.until(lambda d:root.get_attribute('data-stv-revision')=='1')
          assert identities()==expected
          assert buttons()[0].get_attribute('aria-expanded')=='true'
          buttons()[0].click()
          wait.until(lambda d:root.get_attribute('data-stv-revision')=='2')
          assert identities()==expected
          assert buttons()[0].get_attribute('aria-expanded')=='false'

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
