usability smoke
===============

.. test_case:: usability smoke
   :id: STV_TC_025DB3F44E8E
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_browser.py :: tests/test_browser.py::test_usability_smoke[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_049, STV_SWR_050, STV_SWR_054, STV_SYS_006
   :executed_by: STV_TE_EDDA1B963CE797B3, STV_TE_E61ABF83926193AC
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_browser.py::test_usability_smoke[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_browser.py::test_usability_smoke[http]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_usability_smoke(browser, short_output, protocol):
          """Viewport, hover lifecycle and explicit activation on both transports."""
          output = short_output / 'usability'
          result = build(FIXTURE, output)
          assert result.returncode == 0, result.stderr
          with published_url(output,protocol) as url:
              browser.get(url)
              _exercise_usability(browser)

   **Interaction procedure and observable outcomes:**

   .. code-block:: python

      def _exercise_usability(browser):
          wait = WebDriverWait(browser, 10)
          wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, '.stv-view[data-stv-revision="0"]'))
          root = browser.find_element(By.CSS_SELECTOR, '.stv-view')
          viewport = root.find_element(By.CSS_SELECTOR, '.stv-viewport')
          assert browser.execute_script('return getComputedStyle(arguments[0]).height', viewport) == '975px'
          node = root.find_element(By.CSS_SELECTOR, '.stv-node')
          details = node.find_element(By.CSS_SELECTOR, '[data-focus="details"]')
          toolbar = root.find_element(By.CSS_SELECTOR, '.stv-toolbar button')
          ActionChains(browser).move_to_element(node).perform()
          time.sleep(.3)
          assert not browser.find_elements(By.CSS_SELECTOR, '.stv-detail')
          ActionChains(browser).move_to_element(toolbar).perform()
          time.sleep(1.1)
          assert not browser.find_elements(By.CSS_SELECTOR, '.stv-detail')
          # Measure the actual deadline, independently of WebDriver command latency.
          browser.execute_script("""
            window.hoverTimes={};
            arguments[0].addEventListener('mouseenter',()=>{hoverTimes.node=performance.now()},{once:true});
            arguments[1].addEventListener('mouseenter',()=>{hoverTimes.button=performance.now()},{once:true});
            const observer=new MutationObserver(()=>{if(document.querySelector('.stv-detail')){
              hoverTimes.open=performance.now();observer.disconnect();}});
            observer.observe(document.body,{childList:true});
          """,node,details)
          ActionChains(browser).move_to_element_with_offset(node,-node.size['width']/2+8,-node.size['height']/2+8).perform()
          time.sleep(.5)
          ActionChains(browser).move_to_element(details).perform()
          wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, '.stv-detail'))
          times=browser.execute_script('return hoverTimes')
          assert 950 <= times['open']-times['node'] < 1500, times
          assert 0 <= times['open']-times['button'] < 850, times
          # Hover did not focus the view: real Escape must still dismiss it.
          browser.execute_script('document.body.tabIndex=-1;document.body.focus()')
          browser.switch_to.active_element.send_keys(Keys.ESCAPE)
          assert not browser.find_elements(By.CSS_SELECTOR,'.stv-detail')
          ActionChains(browser).move_to_element(toolbar).perform()
          ActionChains(browser).move_to_element(node).perform()
          time.sleep(.2)
          browser.switch_to.active_element.send_keys(Keys.ESCAPE)
          time.sleep(1.1)
          assert not browser.find_elements(By.CSS_SELECTOR,'.stv-detail')
          browser.execute_script('arguments[0].focus()', details)
          details.send_keys(Keys.ENTER)
          assert browser.find_elements(By.CSS_SELECTOR, '.stv-detail')
          browser.switch_to.active_element.send_keys(Keys.ESCAPE)
          assert not browser.find_elements(By.CSS_SELECTOR, '.stv-detail')
          assert browser.switch_to.active_element == details
          # Last, test each cancellation from the same reset viewport, with no
          # pointer departure after the action masking whether it cancels the timer.
          for selector in ('[aria-label="Pan right"]','.stv-groups button'):
              browser.execute_script("arguments[0].querySelector('[aria-label=\"Reset viewport\"]').click()",root)
              ActionChains(browser).move_to_element(toolbar).perform()
              ActionChains(browser).move_to_element(node).perform()
              time.sleep(.2)
              browser.execute_script('arguments[0].querySelector(arguments[1]).click()',root,selector)
              wait.until(lambda d:root.get_attribute('aria-busy')=='false')
              time.sleep(1.1)
              assert not browser.find_elements(By.CSS_SELECTOR,'.stv-detail')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
