seed selection release
======================

.. test_case:: seed selection release
   :id: STV_TC_DE0C60E0BB97
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_release_seeds.py :: docs/test-scripts/test_release_seeds.py::test_seed_selection_release[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_003, STV_SHR_014, STV_SHR_026, STV_SHR_038, STV_SHR_047, STV_SHR_048, STV_SHR_052, STV_SHR_053, STV_SWR_003, STV_SWR_038, STV_SWR_048, STV_SWR_051, STV_SWR_052, STV_SWR_056, STV_SWR_057
   :executed_by: STV_TE_56BF0F252E2B0681, STV_TE_2BE1C4B126B18F38
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_release_seeds.py::test_seed_selection_release[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_release_seeds.py::test_seed_selection_release[file]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_seed_selection_release(browser,short_output,protocol):
          source=short_output/'source';shutil.copytree(FIXTURE,source)
          requirements='Requirements\n============\n\n'
          for i in range(12):
              requirements+=f'.. shr:: Goal {i}\n   :id: GOAL_{i:03}\n'
              if i==0:
                  requirements+='   :traces: '+', '.join(f'CHILD_{j}' for j in range(5))+'\n'
              requirements+='\n'
          requirements+='.. shr:: Secret hidden title\n   :id: HIDDEN_A\n   :hide:\n\n'
          requirements+='\n'.join(f'.. swr:: Software child {j}\n   :id: CHILD_{j}\n' for j in range(5))
          (source/'requirements.rst').write_text(requirements,encoding='utf-8')
          (source/'index.rst').write_text('Project\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view::\n\n.. traceability-view:: GOAL_000\n',encoding='utf-8')
          output=short_output/'html';result=build(source,output);assert result.returncode==0,result.stderr
          with published_url(output,protocol) as url:
              browser.get(url);wait=WebDriverWait(browser,20)
              wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))==2)
              roots=browser.find_elements(By.CSS_SELECTOR,'.stv-view');root=roots[0]
              field=root.find_element(By.CSS_SELECTOR,'.stv-seed-picker input')
              assert [n.text for n in root.find_elements(By.CSS_SELECTOR,'.stv-id')]==[f'GOAL_{i:03}' for i in range(5)]
              field.send_keys('software child')
              assert root.get_attribute('data-stv-revision')=='0'
              assert len(root.find_elements(By.CSS_SELECTOR,'.stv-seed-matches [role="option"]'))==5
              field.send_keys(Keys.ESCAPE)
              assert field.get_attribute('aria-expanded')=='false'
              field.send_keys(Keys.CONTROL,'a');field.send_keys(Keys.BACKSPACE);field.send_keys('software child')
              root.find_elements(By.CSS_SELECTOR,'.stv-seed-matches [role="option"]')[2].click()
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='1')
              assert [n.text for n in root.find_elements(By.CSS_SELECTOR,'.stv-id')]==['CHILD_2']
              assert browser.switch_to.active_element==field
              for invalid in ['', 'HIDDEN_A', 'Secret hidden', 'goal_000']:
                  field.send_keys(Keys.CONTROL,'a');field.send_keys(Keys.BACKSPACE)
                  if invalid:field.send_keys(invalid)
                  if invalid!='goal_000':
                      assert not root.find_elements(By.CSS_SELECTOR,'.stv-seed-matches [role="option"]')
                  field.send_keys(Keys.ENTER)
                  assert field.get_attribute('aria-invalid')=='true'
                  assert root.get_attribute('data-stv-revision')=='1'
              field.send_keys(Keys.CONTROL,'a');field.send_keys(Keys.BACKSPACE);field.send_keys(' GOAL_000 ');field.send_keys(Keys.ENTER)
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='2')
              assert [n.text for n in root.find_elements(By.CSS_SELECTOR,'.stv-id')]==['GOAL_000']
              control=root.find_element(By.CSS_SELECTOR,'[aria-label="Expand Traces (outgoing) for GOAL_000"]')
              browser.execute_script('arguments[0].click()',control)
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='3')
              boxes=browser.execute_script("""return Object.fromEntries([...arguments[0].querySelectorAll('.stv-node')].map(n=>[n.querySelector('.stv-id').textContent,{x:parseFloat(n.style.left),w:n.offsetWidth}]))""",root)
              children=[boxes[f'CHILD_{i}'] for i in range(5)]
              midpoint=(min(n['x'] for n in children)+max(n['x']+n['w'] for n in children))/2
              assert abs(boxes['GOAL_000']['x']+boxes['GOAL_000']['w']/2-midpoint)<1
              root.find_element(By.XPATH,'.//button[text()="Project overview"]').click()
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='4')
              assert len(root.find_elements(By.CSS_SELECTOR,'.stv-node'))==6
              assert roots[1].get_attribute('data-stv-revision')=='0'
              other=roots[1].find_element(By.CSS_SELECTOR,'.stv-seed-picker input')
              other.send_keys('CHILD_4');other.send_keys(Keys.ENTER)
              wait.until(lambda d:roots[1].get_attribute('data-stv-revision')=='1')
              assert root.get_attribute('data-stv-revision')=='4'
              assert [n.text for n in roots[1].find_elements(By.CSS_SELECTOR,'.stv-id')]==['CHILD_4']

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
