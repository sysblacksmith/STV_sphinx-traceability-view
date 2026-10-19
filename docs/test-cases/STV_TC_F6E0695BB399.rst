offline exploration
===================

.. test_case:: offline exploration
   :id: STV_TC_F6E0695BB399
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_browser.py :: tests/test_browser.py::test_offline_exploration[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_004, STV_SHR_008, STV_SHR_015, STV_SHR_016, STV_SHR_017, STV_SHR_018, STV_SHR_029, STV_SHR_031, STV_SHR_033, STV_SHR_034, STV_SHR_035, STV_SHR_038, STV_SHR_039, STV_SHR_040, STV_SWR_004, STV_SWR_008, STV_SWR_015, STV_SWR_016, STV_SWR_017, STV_SWR_018, STV_SWR_029, STV_SWR_031, STV_SWR_033, STV_SWR_034, STV_SWR_035, STV_SWR_038, STV_SWR_039, STV_SWR_040, STV_SWR_050, STV_SYS_003, STV_SYS_007
   :executed_by: STV_TE_CD6E815F9CAC0F7F, STV_TE_381A684E64CE327D
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_browser.py::test_offline_exploration[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_browser.py::test_offline_exploration[http]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_offline_exploration(browser, short_output, protocol):
          tmp_path = short_output
          output = tmp_path / "nested" / "documentation"
          result = build(FIXTURE, output)
          assert result.returncode == 0, result.stderr
          server = None
          try:
              if protocol == "http":
                  server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(tmp_path)))
                  threading.Thread(target=server.serve_forever, daemon=True).start()
                  url = f"http://127.0.0.1:{server.server_port}/nested/documentation/index.html"
              else:
                  url = (output / "index.html").as_uri()
              browser.get(url)
              wait = WebDriverWait(browser, 20)
              wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, '.stv-view[data-stv-revision="0"]')) == 2)
              roots = browser.find_elements(By.CSS_SELECTOR, ".stv-view")
              assert len(roots[0].find_elements(By.CSS_SELECTOR, ".stv-node")) == 2
              assert len(roots[1].find_elements(By.CSS_SELECTOR, ".stv-node")) == 2
              root_button = roots[1].find_element(By.CSS_SELECTOR, '[data-focus="root"]')
              browser.execute_script("arguments[0].focus()", root_button)
              root_button.send_keys(Keys.ENTER)
              wait.until(lambda d: roots[1].get_attribute("data-stv-revision") == "1")
              assert len(roots[1].find_elements(By.CSS_SELECTOR, ".stv-node")) == 1
              assert roots[0].get_attribute("data-stv-revision") == "0"
              inspect = roots[0].find_element(By.CSS_SELECTOR, '[aria-label="Details for ROOT_A"]')
              browser.execute_script("arguments[0].focus()", inspect)
              inspect.send_keys(Keys.ENTER)
              try:
                  wait.until(lambda d: "formatted body" in d.find_element(By.CSS_SELECTOR, ".stv-detail").text)
              except Exception:
                  print(browser.find_element(By.CSS_SELECTOR, ".stv-detail").get_attribute("outerHTML"))
                  raise
              assert browser.find_elements(By.CSS_SELECTOR, ".stv-detail table")
              browser.switch_to.active_element.send_keys(Keys.ESCAPE)
              wait.until(lambda d: not d.find_elements(By.CSS_SELECTOR, ".stv-detail"))
              assert browser.switch_to.active_element == inspect
              assert roots[0].find_element(By.CSS_SELECTOR, '.stv-node.stv-unaccepted .stv-id').text == 'LEAF_B'
              assert roots[0].find_element(By.CSS_SELECTOR, '.stv-node:not(.stv-unaccepted) .stv-id').text == 'ROOT_A'
              # Pointer hover presents the same final host fragment; pointer travel
              # into the interactive panel keeps it open beyond the dismissal grace.
              ActionChains(browser).move_to_element(inspect).perform()
              wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, '.stv-detail'))
              panel=browser.find_element(By.CSS_SELECTOR,'.stv-detail')
              ActionChains(browser).move_to_element(panel).perform()
              wait.until(lambda d: 'formatted body' in panel.text)
              assert browser.execute_script('return arguments[0].getBoundingClientRect().right <= innerWidth',panel)
              assert browser.execute_script('return arguments[0].getBoundingClientRect().bottom <= innerHeight',panel)
              panel.find_element(By.CSS_SELECTOR,'button').click()
              # View-local transforms are shared by edge and node layers.
              other_transform=roots[1].find_element(By.CSS_SELECTOR,'.stv-scene').get_attribute('style')
              for label in ['Zoom in','Pan right','Pan down']:
                  control=roots[0].find_element(By.CSS_SELECTOR,f'[aria-label="{label}"]')
                  browser.execute_script('arguments[0].focus()',control);control.send_keys(Keys.ENTER)
              assert roots[1].find_element(By.CSS_SELECTOR,'.stv-scene').get_attribute('style') == other_transform
              roots[0].find_element(By.CSS_SELECTOR,'[aria-label="Reset viewport"]').click()
              viewport=roots[0].find_element(By.CSS_SELECTOR,'.stv-viewport')
              scene=roots[0].find_element(By.CSS_SELECTOR,'.stv-scene')
              before_drag=scene.get_attribute('style')
              x,y=browser.execute_script('const r=arguments[0].getBoundingClientRect();return [Math.min(r.right,innerWidth)-20,Math.min(r.bottom,innerHeight)-20]',viewport)
              drag=ActionChains(browser)
              drag.w3c_actions.pointer_action.move_to_location(x,y)
              drag.click_and_hold().move_by_offset(-80,-60).release().perform()
              wait.until(lambda d:scene.get_attribute('style')!=before_drag)
              before_wheel=scene.get_attribute('style')
              ActionChains(browser).scroll_from_origin(ScrollOrigin.from_element(viewport),0,-120).perform()
              wait.until(lambda d:scene.get_attribute('style')!=before_wheel)
              assert len(browser.window_handles)==1
              assert roots[1].find_element(By.CSS_SELECTOR,'.stv-scene').get_attribute('style') == other_transform
              roots[0].find_element(By.CSS_SELECTOR,'[aria-label="Reset viewport"]').click()
              group=roots[0].find_element(By.CSS_SELECTOR,'[aria-label="Expand Traces (outgoing) for ROOT_A"]')
              browser.execute_script('arguments[0].focus()',group);group.send_keys(Keys.ENTER)
              wait.until(lambda d: roots[0].get_attribute('data-stv-revision')=='1')
              assert len(roots[0].find_elements(By.CSS_SELECTOR,'.stv-node'))==2
              assert len(roots[0].find_elements(By.CSS_SELECTOR,'.stv-edges polyline'))==1
              reverse=roots[0].find_element(By.CSS_SELECTOR,'[aria-label="Expand Traced by (incoming) for LEAF_B"]')
              browser.execute_script('arguments[0].focus()',reverse);reverse.send_keys(Keys.ENTER)
              wait.until(lambda d:roots[0].get_attribute('data-stv-revision')=='2')
              assert len(roots[0].find_elements(By.CSS_SELECTOR,'.stv-edges polyline'))==1
              original=roots[0].find_element(By.CSS_SELECTOR,'.stv-summary')
              before=browser.current_window_handle
              browser.execute_script('arguments[0].focus()',original);original.send_keys(Keys.ENTER)
              wait.until(lambda d: len(d.window_handles)==2)
              browser.switch_to.window(next(handle for handle in browser.window_handles if handle!=before))
              wait.until(lambda d:d.current_url.endswith('requirements.html#ROOT_A'))
              wait.until(lambda d:d.find_elements(By.ID,'ROOT_A'))
              assert browser.current_url.endswith('requirements.html#ROOT_A')
              browser.close();browser.switch_to.window(before)
              # The card background belongs to the original-object anchor; separate
              # group/detail controls remain above that stretched hit region.
              card=roots[0].find_element(By.CSS_SELECTOR,'[data-key*="ROOT_A"]')
              ActionChains(browser).move_to_element_with_offset(card,-card.size['width']/2+3,-card.size['height']/2+3).click().perform()
              wait.until(lambda d:len(d.window_handles)==2)
              browser.switch_to.window(next(handle for handle in browser.window_handles if handle!=before))
              wait.until(lambda d:d.current_url.endswith('requirements.html#ROOT_A'))
              wait.until(lambda d:d.find_elements(By.ID,'ROOT_A'))
              assert browser.current_url.endswith('requirements.html#ROOT_A')
              browser.close();browser.switch_to.window(before)
              artifact = os.environ.get("STV_SCREENSHOTS")
              if artifact:
                  Path(artifact).mkdir(parents=True, exist_ok=True)
                  browser.save_screenshot(str(Path(artifact) / f"{protocol}-example.png"))
          finally:
              if server:
                  server.shutdown()
                  server.server_close()

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
