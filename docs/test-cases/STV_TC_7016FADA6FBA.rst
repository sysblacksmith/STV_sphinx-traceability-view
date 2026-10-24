alternate model geometry details and external
=============================================

.. test_case:: alternate model geometry details and external
   :id: STV_TC_7016FADA6FBA
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_008, STV_SHR_012, STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_026, STV_SHR_029, STV_SHR_031, STV_SHR_033, STV_SHR_037, STV_SHR_041, STV_SHR_047, STV_SHR_048, STV_SWR_008, STV_SWR_012, STV_SWR_015, STV_SWR_029, STV_SWR_031, STV_SWR_033, STV_SWR_037, STV_SWR_041, STV_SWR_047, STV_SWR_048, STV_SWR_049, STV_SWR_050, STV_SYS_004, STV_SYS_005, STV_SYS_006, STV_SYS_010
   :executed_by: STV_TE_61313CFB6F4999CF, STV_TE_80B3F0B64A8C7517
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[file]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_alternate_model_geometry_details_and_external(browser,short_output,protocol):
          output=short_output/'html';result=build(FIXTURE.parent/'alternate_model',output);assert result.returncode==0,result.stderr
          with published_url(output,protocol) as url:
              browser.get(url);wait=WebDriverWait(browser,30)
              wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))==3)
              roots=browser.find_elements(By.CSS_SELECTOR,'.stv-view');root=roots[0]
              assert browser.execute_script('''const n=arguments[0].querySelector('.stv-node').getBoundingClientRect(),v=arguments[0].querySelector('.stv-viewport').getBoundingClientRect();return n.top>=v.top&&n.bottom<=v.bottom''',root)
              def group(identity,direction):
                  return root.find_element(By.CSS_SELECTOR,f'[aria-label="Expand Traces {"to" if direction=="outgoing" else "from"} ({direction}) for {identity}"]')
              control=group('SOFTWARE_A','outgoing');browser.execute_script('arguments[0].focus()',control);control.send_keys(Keys.ENTER)
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='1')
              control=group('GOAL_A','outgoing');browser.execute_script('arguments[0].focus()',control);control.send_keys(Keys.ENTER)
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='2')
              boxes=browser.execute_script('''return Object.fromEntries([...arguments[0].querySelectorAll('.stv-nodes>.stv-node')].map(n=>[n.querySelector('.stv-id').textContent,{x:parseFloat(n.style.left),y:parseFloat(n.style.top),width:n.offsetWidth,height:n.offsetHeight}]))''',root)
              assert len(boxes)==6
              assert 'HIDDEN_A' not in boxes
              for a,b in zip(['GOAL_A','HARDWARE_A','SYSTEM_A','SOFTWARE_A'],['HARDWARE_A','SYSTEM_A','SOFTWARE_A','MODULE_A']):assert boxes[a]['y']+boxes[a]['height']<boxes[b]['y']
              assert boxes['CHECK_A']['x']>=max(v['x']+v['width'] for k,v in boxes.items() if k!='CHECK_A')+96
              assert len(root.find_elements(By.CSS_SELECTOR,'.stv-edges polyline'))==7
              assert browser.execute_script('''const title=arguments[0].querySelector('[data-key*="GOAL_A"] .stv-title');return title.scrollHeight>title.clientHeight&&title.clientHeight<=2*parseFloat(getComputedStyle(title).lineHeight)+1''',root)
              long_id=roots[1].find_element(By.CSS_SELECTOR,'[data-key*=LONG_IDENTIFIER] .stv-id')
              assert long_id.get_attribute('textContent')=='LONG_IDENTIFIER_WITH_MANY_SEGMENTS_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'
              assert browser.execute_script('return arguments[0].scrollWidth<=arguments[0].clientWidth',long_id)
              assert len(roots[1].find_elements(By.CSS_SELECTOR,'.stv-unaccepted'))==2
              # A part seed inspects the complete published containing Need.
              part=roots[2].find_element(By.CSS_SELECTOR,'[aria-label="Details for GOAL_A.fragment"]')
              browser.execute_script('arguments[0].focus()',part);part.send_keys(Keys.ENTER)
              wait.until(lambda d:'Static widget text' in d.find_element(By.CSS_SELECTOR,'.stv-detail').text)
              panel=browser.find_element(By.CSS_SELECTOR,'.stv-detail')
              assert 'Fixture owner' in panel.text
              assert 'Resource unavailable offline' in panel.text
              assert not panel.find_elements(By.CSS_SELECTOR,'script,iframe,object,[onerror]')
              assert not browser.execute_script('return window.STV_WIDGET_EXECUTED===true')
              assert panel.find_element(By.CSS_SELECTOR,'img[data-stv-src]').get_attribute('complete')=='true'
              assert browser.execute_script('return arguments[0].naturalWidth',panel.find_element(By.CSS_SELECTOR,'img[data-stv-src]'))>0
              assert browser.execute_script('return arguments[0].naturalWidth',panel.find_element(By.CSS_SELECTOR,'.fixture-widget img'))>0
              label=panel.find_element(By.CSS_SELECTOR,'label');field=panel.find_element(By.CSS_SELECTOR,'input')
              assert label.get_attribute('for')==field.get_attribute('id')
              assert field.get_attribute('id').startswith(panel.get_attribute('id'))
              assert 'HIDDEN_A' not in panel.text
              assert not browser.execute_script("return performance.getEntriesByType('resource').some(e=>e.name.includes('example.invalid'))")
              assert browser.execute_script('return arguments[0].scrollHeight>arguments[0].clientHeight',panel)
              browser.execute_script('arguments[0].focus()',panel);panel.send_keys(Keys.END)
              wait.until(lambda d:browser.execute_script('return arguments[0].scrollTop>0',panel))
              original=panel.find_element(By.CSS_SELECTOR,'a[href*="example.invalid/remote.png"]')
              assert original.text=='Original resource'
              panel.find_element(By.CSS_SELECTOR,'button').click()
              external=roots[1].find_element(By.CSS_SELECTOR,'[aria-label="Details for EXTERNAL_A"]')
              browser.execute_script('arguments[0].focus()',external);external.send_keys(Keys.ENTER)
              wait.until(lambda d:'External owner' in d.find_element(By.CSS_SELECTOR,'.stv-detail').text)
              assert 'full body unavailable offline' in browser.find_element(By.CSS_SELECTOR,'.stv-detail').text
              browser.find_element(By.CSS_SELECTOR,'.stv-detail button').click()
              isolated=roots[1].find_element(By.CSS_SELECTOR,'.stv-unaccepted')
              browser.execute_script('arguments[0].focus()',isolated.find_element(By.CSS_SELECTOR,'[data-focus="details"]'))
              wait.until(lambda d:isolated.find_element(By.CSS_SELECTOR,'.stv-id').text=='ISOLATED_A')
              assert isolated.find_element(By.CSS_SELECTOR,'.stv-id').text=='ISOLATED_A'
              assert 'No relationships' in isolated.text
              assert not isolated.find_elements(By.CSS_SELECTOR,'.stv-groups button')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
