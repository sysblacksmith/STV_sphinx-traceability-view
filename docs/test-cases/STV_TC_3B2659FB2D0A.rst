documentation visuals
=====================

.. test_case:: documentation visuals
   :id: STV_TC_3B2659FB2D0A
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_documentation_visuals
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_017, STV_SHR_018, STV_SYS_003
   :executed_by: STV_TE_22DE49BBDDE7EC3B, STV_TE_281E939E541ADC21
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_documentation_visuals``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_documentation_visuals" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_documentation_visuals(browser):
          published=Path(__file__).parents[1]/'docs/_build/html'
          assert (published/'demo.html').is_file(),'Build project documentation before publication checks'
          browser.set_window_size(1500,1300)
          browser.get((published/'demo.html').as_uri())
          wait=WebDriverWait(browser,20)
          wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))==2)
          assert 'Traceability view failed' not in browser.find_element(By.TAG_NAME,'body').text
          screenshots=Path(os.environ.get('STV_SCREENSHOTS','docs/_build/browser'));screenshots.mkdir(parents=True,exist_ok=True)
          browser.save_screenshot(str(screenshots/'project-demo.png'))
          browser.get((published/'state-machine.html').as_uri())
          assert browser.find_element(By.CSS_SELECTOR,'object[type="image/svg+xml"]').get_attribute('data').endswith('state-machine.svg')
          browser.save_screenshot(str(screenshots/'state-page.png'))
          browser.get((published/'state-machine.svg').as_uri())
          assert browser.find_elements(By.TAG_NAME,'svg')
          assert len(browser.find_elements(By.TAG_NAME,'a'))>=10
          browser.save_screenshot(str(screenshots/'state-diagram.png'))
          for name in ('system-architecture','software-architecture'):
              browser.get((published/(name+'.svg')).as_uri())
              assert browser.find_elements(By.TAG_NAME,'svg')
              assert browser.find_elements(By.TAG_NAME,'a')
              browser.save_screenshot(str(screenshots/(name+'.png')))
              page='architecture-system' if name.startswith('system') else 'architecture-software'
              browser.get((published/(page+'.html')).as_uri())
              assert browser.find_element(By.CSS_SELECTOR,'object[type="image/svg+xml"]')
              browser.save_screenshot(str(screenshots/(page+'-page.png')))

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
