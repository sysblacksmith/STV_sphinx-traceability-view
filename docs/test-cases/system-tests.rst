System test cases
=================

Canonical specifications at the system verification level. Each case retains
its own Need ID, requirement links and execution history. See :doc:`index`
for classification and evidence semantics.

.. needtable::
   :filter: type == 'test_case' and 'test_system' in tags
   :columns: id;title;status;verifies;last_result;executed_by

STV_TC_SY_001: usability smoke
------------------------------

.. test_case:: usability smoke
   :id: STV_TC_SY_001
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_usability_smoke[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_049, STV_SWR_050, STV_SWR_054, STV_SYS_006
   :executed_by: STV_TE_EDDA1B963CE797B3, STV_TE_E61ABF83926193AC, STV_TE_4C69746CC553D7A0, STV_TE_8791048E05CC01B1, STV_TE_FA148C6483A7987B
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_usability_smoke[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_usability_smoke[http]" -q``.

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

STV_TC_SY_002: control order smoke
----------------------------------

.. test_case:: control order smoke
   :id: STV_TC_SY_002
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_control_order_smoke[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_051, STV_SWR_055
   :executed_by: STV_TE_E9DF4EB84C2C809D, STV_TE_48E662C1225F4525, STV_TE_42F89514387F2644, STV_TE_3EA3780EE4C691D4, STV_TE_68DEC3FFAD82756F
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_control_order_smoke[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_control_order_smoke[http]" -q``.

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

STV_TC_SY_003: missing placeholder and detail error
---------------------------------------------------

.. test_case:: missing placeholder and detail error
   :id: STV_TC_SY_003
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_027, STV_SHR_028, STV_SHR_029, STV_SWR_027, STV_SWR_028, STV_SWR_029, STV_SYS_004
   :executed_by: STV_TE_1E7C90AF591203FD, STV_TE_01014AFFA8103E08, STV_TE_B71B51810DD8B805, STV_TE_98FA5AFD1CF5BE75, STV_TE_0B004B872559B017, STV_TE_6AA25FA7CA5F5192, STV_TE_CECBFB91BF01D342
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[file]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_missing_placeholder_and_detail_error(browser,short_output,protocol):
          import shutil
          source=short_output/'source';shutil.copytree(FIXTURE,source)
          path=source/'requirements.rst';path.write_text(path.read_text(encoding='utf-8').replace(':traces: LEAF_B',':traces: MISSING_A'),encoding='utf-8')
          output=short_output/'html';result=build(source,output)
          assert result.returncode!=0 and 'MISSING_A' in result.stderr
          saved={script:script.read_bytes() for script in (output/'_static/stv/details').glob('*.js')}
          for script in saved:script.unlink()
          with published_url(output,protocol) as url:
              browser.get(url);wait=WebDriverWait(browser,20)
              wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
              root=browser.find_element(By.CSS_SELECTOR,'.stv-view')
              control=root.find_element(By.CSS_SELECTOR,'[aria-label="Expand Traces (outgoing) for ROOT_A"]')
              browser.execute_script('arguments[0].focus()',control);control.send_keys(Keys.ENTER)
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='1')
              missing=root.find_element(By.CSS_SELECTOR,'.stv-missing')
              # Stable navigation can discover a node left of the current viewport.
              # Check its identity, then explicitly fit before testing visible content.
              assert 'MISSING_A' in missing.get_attribute('textContent')
              geometry=browser.execute_script('return [...arguments[0].querySelectorAll(".stv-node")].map(n=>[n.dataset.key,n.style.left,n.style.top])',root)
              browser.execute_script('[...arguments[0].querySelectorAll(".stv-toolbar button")].find(b=>b.textContent==="Reset viewport").click()',root)
              assert browser.execute_script('return [...arguments[0].querySelectorAll(".stv-node")].map(n=>[n.dataset.key,n.style.left,n.style.top])',root)==geometry
              assert 'MISSING_A' in missing.text and 'Missing object' in missing.text
              assert not missing.find_elements(By.CSS_SELECTOR,'a,button')
              inspect=root.find_element(By.CSS_SELECTOR,'[aria-label="Details for ROOT_A"]')
              browser.execute_script('arguments[0].focus()',inspect);inspect.send_keys(Keys.ENTER)
              wait.until(lambda d:'Local detail asset unavailable' in d.find_element(By.CSS_SELECTOR,'.stv-detail').text)
              browser.switch_to.active_element.send_keys(Keys.ESCAPE)
              wait.until(lambda d:not d.find_elements(By.CSS_SELECTOR,'.stv-detail'))
              for script,content in saved.items():script.write_bytes(content)
              inspect.send_keys(Keys.ENTER)
              wait.until(lambda d:'formatted body' in d.find_element(By.CSS_SELECTOR,'.stv-detail').text)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_004: failed finalization retains pending page and previous assets
---------------------------------------------------------------------------

.. test_case:: failed finalization retains pending page and previous assets
   :id: STV_TC_SY_004
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_failed_finalization_retains_pending_page_and_previous_assets
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SHR_027, STV_SWR_015, STV_SWR_017, STV_SWR_027
   :executed_by: STV_TE_2FE927B84AC573F5, STV_TE_5428B57695F57556, STV_TE_370A22653A3C61D1, STV_TE_AB3AB31683DE7C64, STV_TE_35ACFC65C5B99B80, STV_TE_644E38E89EF5303D, STV_TE_147E98E60DA06020, STV_TE_FB2A4E45E7928173
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_failed_finalization_retains_pending_page_and_previous_assets``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_failed_finalization_retains_pending_page_and_previous_assets" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_failed_finalization_retains_pending_page_and_previous_assets(tmp_path):
          from types import SimpleNamespace
          from sphinx.errors import SphinxError
          from sphinx_traceability_view.directive.lifecycle import finish
          pending='<section data-stv-build="STV_PENDING"></section>'
          (tmp_path/'index.html').write_text(pending,encoding='utf-8')
          (tmp_path/'requirements.html').write_text('<p>Expected Need body missing</p>',encoding='utf-8')
          previous=tmp_path/'_static/stv/graph-old.js';previous.parent.mkdir(parents=True);previous.write_text('previous complete asset',encoding='utf-8')
          graph={'model':{'relations':{}},'objects':{'A':{'url':'requirements.html#A','external':False,'parent':None}}}
          app=SimpleNamespace(_stv_graph=graph,_stv_hidden=set(),outdir=str(tmp_path),env=SimpleNamespace(stv_views={'index':[{}]}))
          with pytest.raises(SphinxError,match='Rendered Need.*missing'):
              finish(app,None)
          assert (tmp_path/'index.html').read_text(encoding='utf-8')==pending
          assert previous.read_text(encoding='utf-8')=='previous complete asset'
          assert list(previous.parent.glob('graph-*.js'))==[previous]

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_005: seed layout replacement failure and staleness
------------------------------------------------------------

.. test_case:: seed layout replacement failure and staleness
   :id: STV_TC_SY_005
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_release_seeds.py :: docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_044, STV_SHR_053, STV_SWR_044, STV_SWR_057
   :executed_by: STV_TE_3B3E61D7DFC99D73, STV_TE_0EEADCA1406FD6ED, STV_TE_776A0D0F470417C5, STV_TE_938B27916A316D0E, STV_TE_1DC0F35D41063248
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[file]" -q``.

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

STV_TC_SY_006: alternate host schema external metadata and parts
----------------------------------------------------------------

.. test_case:: alternate host schema external metadata and parts
   :id: STV_TC_SY_006
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_alternate_host_schema_external_metadata_and_parts
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_026, STV_SHR_036, STV_SHR_045, STV_SHR_047, STV_SHR_048, STV_SWR_014, STV_SWR_036, STV_SWR_045, STV_SWR_047, STV_SWR_048, STV_SYS_002
   :executed_by: STV_TE_19C8684FFE688A1D, STV_TE_CECCD71A1F7BD48C, STV_TE_AA534A6986BCE95B, STV_TE_8105F93F757B5B04, STV_TE_1DEFDCD63760E5EB, STV_TE_4D22B3B6FFD3CE4C, STV_TE_5878BEA6800904D7
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_alternate_host_schema_external_metadata_and_parts``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_alternate_host_schema_external_metadata_and_parts" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_alternate_host_schema_external_metadata_and_parts(tmp_path):
          result=build(FIXTURE.parent/'alternate_model',tmp_path)
          assert result.returncode==0,result.stdout+result.stderr
          data=manifest(tmp_path)
          assert data['model']['types']['hardware']['level']=='hardware'
          assert data['model']['relations']['traces']['outgoing']=='Traces to'
          assert data['objects']['EXTERNAL_A']['metadata']['owner']=='External owner'
          assert data['objects']['EXTERNAL_A']['docname'] is None
          assert 'GOAL_A.fragment' in data['objects']
          assert 'GOAL_A.fragment' not in data['entries']
          assert 'HIDDEN_A' not in data['objects']
          assert not any('HIDDEN_A' in edge for edge in data['edges'])

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_007: documentation visuals
------------------------------------

.. test_case:: documentation visuals
   :id: STV_TC_SY_007
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_documentation_visuals
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_017, STV_SHR_018, STV_SYS_003
   :executed_by: STV_TE_22DE49BBDDE7EC3B, STV_TE_281E939E541ADC21, STV_TE_C9B10F63B52B82BE, STV_TE_8D236D778E5397B0, STV_TE_8BA9F97053CDDB86
   :last_result: passed

   **Level:** System/browser acceptance.

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

STV_TC_SY_008: invalid seed source location
-------------------------------------------

.. test_case:: invalid seed source location
   :id: STV_TC_SY_008
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_invalid_seed_source_location[UNKNOWN]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_026, STV_SHR_047, STV_SHR_048, STV_SWR_026, STV_SWR_048, STV_SYS_001
   :executed_by: STV_TE_55AFED6304CFE81F, STV_TE_93AFE98F3EE60BE8, STV_TE_785BF58793290B0E, STV_TE_C6840C674379E70A, STV_TE_98C1FD50055BD13A, STV_TE_B541FAAB192B3BBE, STV_TE_4CA68E5E713B77CF
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_invalid_seed_source_location[UNKNOWN]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_invalid_seed_source_location[UNKNOWN]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_seed_source_location(tmp_path, seed):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          (source / "index.rst").write_text(f"Invalid\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: {seed}\n", encoding="utf-8")
          with (source / "requirements.rst").open("a", encoding="utf-8") as stream:
              stream.write("\n.. shr:: Hidden\n   :id: HIDDEN_A\n   :hide:\n")
          result = build(source, tmp_path / "html")
          assert result.returncode != 0
          assert "index.rst:8" in result.stderr
          assert "unknown or hidden starting ID" in result.stderr

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_009: control order smoke
----------------------------------

.. test_case:: control order smoke
   :id: STV_TC_SY_009
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_control_order_smoke[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_051, STV_SWR_055
   :executed_by: STV_TE_193BABCE01804ECD, STV_TE_D54F9EC1B8C3DC2D, STV_TE_89DA2BE17EC0FB60, STV_TE_97A2EA6B2A2DFFD8, STV_TE_60E832B730CEF95E
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_control_order_smoke[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_control_order_smoke[file]" -q``.

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

STV_TC_SY_010: interactive seed smoke
-------------------------------------

.. test_case:: interactive seed smoke
   :id: STV_TC_SY_010
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_interactive_seed_smoke[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_038, STV_SHR_052, STV_SHR_053, STV_SWR_038, STV_SWR_056, STV_SWR_057
   :executed_by: STV_TE_542E4BF583AB9821, STV_TE_E5587901B2158B26, STV_TE_BC32CB88DE8FEAB6, STV_TE_E7F31A178D716764, STV_TE_62167E711ACEA294
   :last_result: passed

   **Level:** System/browser acceptance.

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

STV_TC_SY_011: seed capacity at directive
-----------------------------------------

.. test_case:: seed capacity at directive
   :id: STV_TC_SY_011
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_seed_capacity_at_directive[200-True]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_001, STV_SHR_026, STV_SHR_043, STV_SHR_048, STV_SWR_001, STV_SWR_026, STV_SWR_043
   :executed_by: STV_TE_A5B37D2B297444D4, STV_TE_10B3E6446E94D385, STV_TE_B88FABBBBA1DB23F, STV_TE_BE6098AB231764A5, STV_TE_A15052A1362D4FBC, STV_TE_15D0BD9F9CF33DA9, STV_TE_C7A76049793288AA
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_seed_capacity_at_directive[200-True]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_seed_capacity_at_directive[200-True]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_seed_capacity_at_directive(tmp_path, count, success):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          ids = [f"NEED_{i:03}" for i in range(count)]
          (source / "requirements.rst").write_text("Requirements\n============\n\n" + "\n".join(f".. shr:: Item {i}\n   :id: {identity}\n" for i, identity in enumerate(ids)), encoding="utf-8")
          (source / "index.rst").write_text("Capacity\n========\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: " + " ".join(ids) + "\n", encoding="utf-8")
          result = build(source, tmp_path / "html")
          assert (result.returncode == 0) is success, result.stderr
          if not success:
              assert "index.rst:8" in result.stderr
              assert "200 distinct starting IDs" in result.stderr

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_012: missing placeholder and detail error
---------------------------------------------------

.. test_case:: missing placeholder and detail error
   :id: STV_TC_SY_012
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_027, STV_SHR_028, STV_SHR_029, STV_SWR_027, STV_SWR_028, STV_SWR_029, STV_SYS_004
   :executed_by: STV_TE_69D0670DBA913348, STV_TE_7FB8F491ACEA8640, STV_TE_134FB6EFA234AE0A, STV_TE_C907D3DAAB33A698, STV_TE_F460306704A9DB56, STV_TE_F9FF69F5AF8B80F1, STV_TE_64C890A655FDC0CE
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[http]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_missing_placeholder_and_detail_error(browser,short_output,protocol):
          import shutil
          source=short_output/'source';shutil.copytree(FIXTURE,source)
          path=source/'requirements.rst';path.write_text(path.read_text(encoding='utf-8').replace(':traces: LEAF_B',':traces: MISSING_A'),encoding='utf-8')
          output=short_output/'html';result=build(source,output)
          assert result.returncode!=0 and 'MISSING_A' in result.stderr
          saved={script:script.read_bytes() for script in (output/'_static/stv/details').glob('*.js')}
          for script in saved:script.unlink()
          with published_url(output,protocol) as url:
              browser.get(url);wait=WebDriverWait(browser,20)
              wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
              root=browser.find_element(By.CSS_SELECTOR,'.stv-view')
              control=root.find_element(By.CSS_SELECTOR,'[aria-label="Expand Traces (outgoing) for ROOT_A"]')
              browser.execute_script('arguments[0].focus()',control);control.send_keys(Keys.ENTER)
              wait.until(lambda d:root.get_attribute('data-stv-revision')=='1')
              missing=root.find_element(By.CSS_SELECTOR,'.stv-missing')
              # Stable navigation can discover a node left of the current viewport.
              # Check its identity, then explicitly fit before testing visible content.
              assert 'MISSING_A' in missing.get_attribute('textContent')
              geometry=browser.execute_script('return [...arguments[0].querySelectorAll(".stv-node")].map(n=>[n.dataset.key,n.style.left,n.style.top])',root)
              browser.execute_script('[...arguments[0].querySelectorAll(".stv-toolbar button")].find(b=>b.textContent==="Reset viewport").click()',root)
              assert browser.execute_script('return [...arguments[0].querySelectorAll(".stv-node")].map(n=>[n.dataset.key,n.style.left,n.style.top])',root)==geometry
              assert 'MISSING_A' in missing.text and 'Missing object' in missing.text
              assert not missing.find_elements(By.CSS_SELECTOR,'a,button')
              inspect=root.find_element(By.CSS_SELECTOR,'[aria-label="Details for ROOT_A"]')
              browser.execute_script('arguments[0].focus()',inspect);inspect.send_keys(Keys.ENTER)
              wait.until(lambda d:'Local detail asset unavailable' in d.find_element(By.CSS_SELECTOR,'.stv-detail').text)
              browser.switch_to.active_element.send_keys(Keys.ESCAPE)
              wait.until(lambda d:not d.find_elements(By.CSS_SELECTOR,'.stv-detail'))
              for script,content in saved.items():script.write_bytes(content)
              inspect.send_keys(Keys.ENTER)
              wait.until(lambda d:'formatted body' in d.find_element(By.CSS_SELECTOR,'.stv-detail').text)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_013: cross page bundle
--------------------------------

.. test_case:: cross page bundle
   :id: STV_TC_SY_013
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_cross_page_bundle
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_001, STV_SHR_002, STV_SHR_013, STV_SHR_026, STV_SHR_048, STV_SWR_001, STV_SWR_002, STV_SWR_013, STV_SWR_026, STV_SYS_001
   :executed_by: STV_TE_764956AD4834A5CE, STV_TE_7BF04875B87C2A7D, STV_TE_4B3E601321BA8924, STV_TE_226A0A5469B1E2C8, STV_TE_18FC22178525A93E, STV_TE_3E778A3C5CF09B0C, STV_TE_6B9128D591CDF82B
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_cross_page_bundle``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_cross_page_bundle" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_cross_page_bundle(tmp_path):
          result = build(FIXTURE, tmp_path)
          assert result.returncode == 0, result.stdout + result.stderr
          html = (tmp_path / "index.html").read_text(encoding="utf-8")
          assert "STV_PENDING" not in html
          soup = BeautifulSoup(html, "html.parser")
          roots = soup.select(".stv-view")
          assert len(roots) == 2
          assert json.loads(roots[0]["data-stv-seeds"]) == ["ROOT_A", "LEAF_B"]
          assert json.loads(roots[1]["data-stv-seeds"]) == []
          script = soup.select_one("script[data-stv-graph]")
          assert (tmp_path / script["src"]).is_file()
          fragments = list((tmp_path / "_static/stv/details").glob("*.js"))
          assert len(fragments) == 2
          assert any("formatted body" in p.read_text() for p in fragments)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_014: invalid seed source location
-------------------------------------------

.. test_case:: invalid seed source location
   :id: STV_TC_SY_014
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_invalid_seed_source_location[ROOT_A UNKNOWN]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_026, STV_SHR_047, STV_SHR_048, STV_SWR_026, STV_SWR_048, STV_SYS_001
   :executed_by: STV_TE_97AA7EB41C45F077, STV_TE_39301A83113F7C7D, STV_TE_9EBE4F77A19E95FE, STV_TE_D18E0A7F3567D77B, STV_TE_1C3AE7E9B5E53605, STV_TE_5F20F75886471936, STV_TE_8E740204118C54D9
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_invalid_seed_source_location[ROOT_A UNKNOWN]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_invalid_seed_source_location[ROOT_A UNKNOWN]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_seed_source_location(tmp_path, seed):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          (source / "index.rst").write_text(f"Invalid\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: {seed}\n", encoding="utf-8")
          with (source / "requirements.rst").open("a", encoding="utf-8") as stream:
              stream.write("\n.. shr:: Hidden\n   :id: HIDDEN_A\n   :hide:\n")
          result = build(source, tmp_path / "html")
          assert result.returncode != 0
          assert "index.rst:8" in result.stderr
          assert "unknown or hidden starting ID" in result.stderr

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_015: alternate model geometry details and external
------------------------------------------------------------

.. test_case:: alternate model geometry details and external
   :id: STV_TC_SY_015
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_008, STV_SHR_012, STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_026, STV_SHR_029, STV_SHR_031, STV_SHR_033, STV_SHR_037, STV_SHR_041, STV_SHR_047, STV_SHR_048, STV_SWR_008, STV_SWR_012, STV_SWR_015, STV_SWR_029, STV_SWR_031, STV_SWR_033, STV_SWR_037, STV_SWR_041, STV_SWR_047, STV_SWR_048, STV_SWR_049, STV_SWR_050, STV_SYS_004, STV_SYS_005, STV_SYS_006, STV_SYS_010
   :executed_by: STV_TE_61313CFB6F4999CF, STV_TE_80B3F0B64A8C7517, STV_TE_F3C4E90AA84CED2E, STV_TE_FFFF8323BE7629F1, STV_TE_6C0CA12C41B4B075, STV_TE_8B8C5753AB0D6BEB
   :last_result: passed

   **Level:** System/browser acceptance.

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

STV_TC_SY_016: usability smoke
------------------------------

.. test_case:: usability smoke
   :id: STV_TC_SY_016
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_usability_smoke[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_049, STV_SWR_050, STV_SWR_054, STV_SYS_006
   :executed_by: STV_TE_5A3DAC2CD84CDE46, STV_TE_A92CAC9AEFDF41DE, STV_TE_28071DAEB935E86B, STV_TE_281973898519845F, STV_TE_8D4A42C5790D2EC3
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_usability_smoke[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_usability_smoke[file]" -q``.

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

STV_TC_SY_017: large project at visible capacity
------------------------------------------------

.. test_case:: large project at visible capacity
   :id: STV_TC_SY_017
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_capacity.py :: docs/test-scripts/test_capacity.py::test_large_project_at_visible_capacity[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_043, STV_SHR_044, STV_SWR_043, STV_SWR_044, STV_SYS_008
   :executed_by: STV_TE_010F955390602276, STV_TE_5FEC76D970E683E5, STV_TE_3A0908374B1E6391, STV_TE_FC0887B66F8AAE1A
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_capacity.py::test_large_project_at_visible_capacity[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_capacity.py::test_large_project_at_visible_capacity[file]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_large_project_at_visible_capacity(browser,protocol):
          output=Path(os.environ.get('STV_CAPACITY_OUTPUT','docs/_build/benchmark-v2/html')).resolve()
          assert (output/'index.html').is_file(),'Run scripts/benchmark.py before capacity verification'
          runs=[]
          browser.set_script_timeout(35)
          temporary=tempfile.TemporaryDirectory(prefix='stv-cap-') if protocol=='file' else None
          if temporary:
              assert Path(temporary.name).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
              # Full hash names need a short physical output root in Windows Firefox.
              short=Path(temporary.name)/'html';shutil.copytree(output,short);output=short
          try:
              _measure_capacity(browser,output,protocol,runs)
          finally:
              if temporary:
                  assert Path(temporary.name).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
                  temporary.cleanup()
          result={'browser':browser.capabilities['browserVersion'],'geckodriver':browser.capabilities.get('moz:geckodriverVersion'),
                  'memory_scope':'Sum of working sets of the isolated Firefox process tree, including content/GPU helpers; shared pages may be counted more than once',
                  'runs':runs,'startup_median_ms':statistics.median(r['startup_ms'] for r in runs),
                  'startup_max_ms':max(r['startup_ms'] for r in runs),
                  'expansion_median_ms':statistics.median(v for r in runs for v in r['expansion_ms']),
                  'expansion_max_ms':max(v for r in runs for v in r['expansion_ms'])}
          target=Path(os.environ.get('STV_CAPACITY_METRICS','docs/_build/capacity-browser.json'));target.parent.mkdir(parents=True,exist_ok=True)
          aggregate=json.loads(target.read_text(encoding='utf-8')) if target.exists() else {}
          aggregate[protocol]=result
          target.write_text(json.dumps(aggregate,indent=2),encoding='utf-8')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_018: invalid mapping has entry path and location
----------------------------------------------------------

.. test_case:: invalid mapping has entry path and location
   :id: STV_TC_SY_018
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_invalid_mapping_has_entry_path_and_location
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_25353B9B728085D0, STV_TE_386D5C547F786FC8, STV_TE_1BA15C05B4E308DA, STV_TE_62AC4B0AB9B248F8, STV_TE_04003BC62A11DADD, STV_TE_BEB0736CCC12C0B6, STV_TE_B1B8242C880AB7CE
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_invalid_mapping_has_entry_path_and_location``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_invalid_mapping_has_entry_path_and_location" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_mapping_has_entry_path_and_location(tmp_path):
          source=tmp_path/'source';shutil.copytree(FIXTURE,source)
          with (source/'conf.py').open('a',encoding='utf-8') as stream:
              stream.write('\ntraceability_view_model["types"]["shr"]["level"]="unknown"\n')
          result=build(source,tmp_path/'html')
          assert result.returncode!=0
          assert 'index.rst:8' in result.stderr
          assert 'types.shr' in result.stderr

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_019: seed selection release
-------------------------------------

.. test_case:: seed selection release
   :id: STV_TC_SY_019
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_release_seeds.py :: docs/test-scripts/test_release_seeds.py::test_seed_selection_release[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_003, STV_SHR_014, STV_SHR_026, STV_SHR_038, STV_SHR_047, STV_SHR_048, STV_SHR_052, STV_SHR_053, STV_SWR_003, STV_SWR_038, STV_SWR_048, STV_SWR_051, STV_SWR_052, STV_SWR_056, STV_SWR_057
   :executed_by: STV_TE_DFBF01DD6EFAC659, STV_TE_04E3FD1C4E20AEF7, STV_TE_FD08039E2FB58CC9, STV_TE_E78BA064DCE82BD6, STV_TE_EA142C83B0548AF5
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_release_seeds.py::test_seed_selection_release[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_release_seeds.py::test_seed_selection_release[http]" -q``.

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

STV_TC_SY_020: async layout failure and stale completion
--------------------------------------------------------

.. test_case:: async layout failure and stale completion
   :id: STV_TC_SY_020
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_044, STV_SHR_047, STV_SWR_044, STV_SWR_052
   :executed_by: STV_TE_D099D363BCFCAD31, STV_TE_5DCC25155978FEA9, STV_TE_B72094ADA2795468, STV_TE_DDA147A234F1EB90, STV_TE_74238165C37854A2
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[file]" -q``.

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
          result=subprocess.run(['node','--input-type=module','-e',script,str(project/'docs/test-scripts/fixtures/browser-harness.js'),str(short_output/'harness.js')],cwd=project/'frontend',capture_output=True,text=True)
          assert result.returncode==0,result.stderr
          (short_output/'index.html').write_text('<link rel="stylesheet" href="'+(project/'src/sphinx_traceability_view/static/stv.css').as_uri()+'"><div class="stv-view" id="test-view" data-stv-seeds=\'["A"]\'></div><script src="harness.js"></script>',encoding='utf-8')
          # Keep the host alive across all injected completions.
          with published_url(short_output,protocol) as url:
              browser.get(url)
              _assert_async_layout(browser)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_021: interactive seed smoke
-------------------------------------

.. test_case:: interactive seed smoke
   :id: STV_TC_SY_021
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_interactive_seed_smoke[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_038, STV_SHR_052, STV_SHR_053, STV_SWR_038, STV_SWR_056, STV_SWR_057
   :executed_by: STV_TE_23223A8584B5C6B5, STV_TE_4C07297DF2CE4C54, STV_TE_63082524BD2D8904, STV_TE_633C7D44A74AC0EC, STV_TE_30779BF2349D192A
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_interactive_seed_smoke[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_interactive_seed_smoke[http]" -q``.

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

STV_TC_SY_022: invalid seed source location
-------------------------------------------

.. test_case:: invalid seed source location
   :id: STV_TC_SY_022
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_invalid_seed_source_location[HIDDEN_A]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_026, STV_SHR_047, STV_SHR_048, STV_SWR_026, STV_SWR_048, STV_SYS_001
   :executed_by: STV_TE_DA7D6F5E8EF93887, STV_TE_0898010E7C9AF0A4, STV_TE_2CDA237388E56731, STV_TE_72C2FBE6E1A2D120, STV_TE_FE11303CE3990960, STV_TE_06A072906D5A03D1, STV_TE_971193CC70E48D46
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_invalid_seed_source_location[HIDDEN_A]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_invalid_seed_source_location[HIDDEN_A]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_seed_source_location(tmp_path, seed):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          (source / "index.rst").write_text(f"Invalid\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: {seed}\n", encoding="utf-8")
          with (source / "requirements.rst").open("a", encoding="utf-8") as stream:
              stream.write("\n.. shr:: Hidden\n   :id: HIDDEN_A\n   :hide:\n")
          result = build(source, tmp_path / "html")
          assert result.returncode != 0
          assert "index.rst:8" in result.stderr
          assert "unknown or hidden starting ID" in result.stderr

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_023: seed capacity at directive
-----------------------------------------

.. test_case:: seed capacity at directive
   :id: STV_TC_SY_023
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_seed_capacity_at_directive[201-False]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_001, STV_SHR_026, STV_SHR_043, STV_SHR_048, STV_SWR_001, STV_SWR_026, STV_SWR_043
   :executed_by: STV_TE_686277C8A7C1D863, STV_TE_5EBB8A15272B4D9F, STV_TE_8F17CFA55BF7EBA1, STV_TE_649684CCAC6F8A53, STV_TE_19BECE77146BA374, STV_TE_37235BA0631DE3C2, STV_TE_7CA638873EC75B4A
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_seed_capacity_at_directive[201-False]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_seed_capacity_at_directive[201-False]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_seed_capacity_at_directive(tmp_path, count, success):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          ids = [f"NEED_{i:03}" for i in range(count)]
          (source / "requirements.rst").write_text("Requirements\n============\n\n" + "\n".join(f".. shr:: Item {i}\n   :id: {identity}\n" for i, identity in enumerate(ids)), encoding="utf-8")
          (source / "index.rst").write_text("Capacity\n========\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: " + " ".join(ids) + "\n", encoding="utf-8")
          result = build(source, tmp_path / "html")
          assert (result.returncode == 0) is success, result.stderr
          if not success:
              assert "index.rst:8" in result.stderr
              assert "200 distinct starting IDs" in result.stderr

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_024: prior fatal exception is not replaced by bundle generation
-------------------------------------------------------------------------

.. test_case:: prior fatal exception is not replaced by bundle generation
   :id: STV_TC_SY_024
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_prior_fatal_exception_is_not_replaced_by_bundle_generation
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_027, STV_SWR_027
   :executed_by: STV_TE_B273D034597B28B8, STV_TE_D2AD87B422D36273, STV_TE_13B11B8AE03CF870, STV_TE_10081046B1450184, STV_TE_05C8C8194E3C5F0D, STV_TE_95BAD407570E981E, STV_TE_E6D08074BE5F60AD, STV_TE_C9F5F024FD54FD79
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_prior_fatal_exception_is_not_replaced_by_bundle_generation``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_prior_fatal_exception_is_not_replaced_by_bundle_generation" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_prior_fatal_exception_is_not_replaced_by_bundle_generation(tmp_path):
          from types import SimpleNamespace
          from sphinx_traceability_view.directive.lifecycle import finish
          page=tmp_path/'index.html';page.write_text('previous complete page',encoding='utf-8')
          app=SimpleNamespace(_stv_graph={},outdir=str(tmp_path))
          finish(app,RuntimeError('Earlier fatal failure'))
          assert page.read_text(encoding='utf-8')=='previous complete page'
          assert not (tmp_path/'_static').exists()

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_025: project paging
-----------------------------

.. test_case:: project paging
   :id: STV_TC_SY_025
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_project_paging[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_8A63E99187C976E3, STV_TE_6723673D161CA9BA, STV_TE_0BE55BC5BDF3AC65, STV_TE_21BB65233C33EB7E, STV_TE_22F4D540350790A3
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_project_paging[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_project_paging[http]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_project_paging(browser,short_output,protocol):
          import shutil
          source=short_output/'source';shutil.copytree(FIXTURE,source)
          (source/'requirements.rst').write_text('Requirements\n============\n\n'+'\n'.join(f'.. shr:: Stakeholder {i}\n   :id: GOAL_{i:03}\n' for i in range(201)),encoding='utf-8')
          (source/'index.rst').write_text('Project\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view::\n',encoding='utf-8')
          output=short_output/'html';result=build(source,output);assert result.returncode==0,result.stderr
          with published_url(output,protocol) as url:
              browser.get(url)
              _assert_project_pages(browser)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_026: incremental body change hidden and deleted objects
-----------------------------------------------------------------

.. test_case:: incremental body change hidden and deleted objects
   :id: STV_TC_SY_026
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_incremental_body_change_hidden_and_deleted_objects
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_015, STV_SHR_018, STV_SHR_026, STV_SHR_047, STV_SHR_048, STV_SWR_015, STV_SWR_018, STV_SWR_048
   :executed_by: STV_TE_A7840F205B45812E, STV_TE_1FEF2B44838D4155, STV_TE_AD072603469BA90E, STV_TE_8447E3E24802A7A4, STV_TE_F5233640F6DF867D, STV_TE_55D1143DA9DE27A7, STV_TE_010FFE0C52956BBD
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_incremental_body_change_hidden_and_deleted_objects``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_incremental_body_change_hidden_and_deleted_objects" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_incremental_body_change_hidden_and_deleted_objects(tmp_path):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          with (source / "requirements.rst").open("a", encoding="utf-8") as stream:
              stream.write('\n.. shr:: Initially visible\n   :id: HIDDEN_LATER\n')
          output = tmp_path / "html"
          assert build(source, output).returncode == 0
          old = manifest(output)
          path = source / "requirements.rst"
          path.write_text(path.read_text(encoding="utf-8").replace("formatted body", "changed rich body").replace(":id: HIDDEN_LATER", ":id: HIDDEN_LATER\n   :hide:"), encoding="utf-8")
          assert build(source, output).returncode == 0
          new = manifest(output)
          assert new["identity"] != old["identity"]
          assert new["details"]["ROOT_A"]["digest"] != old["details"]["ROOT_A"]["digest"]
          assert "HIDDEN_LATER" not in new["objects"]
          assert "HIDDEN_LATER" not in new["details"]
          assert build(source, output).returncode == 0
          assert manifest(output)["identity"] == new["identity"]

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_027: host owns broken trace failure
---------------------------------------------

.. test_case:: host owns broken trace failure
   :id: STV_TC_SY_027
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_host_owns_broken_trace_failure
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_027, STV_SHR_028, STV_SWR_027, STV_SWR_028
   :executed_by: STV_TE_89DB9F0DFA6EBD36, STV_TE_DC50B0D40735701B, STV_TE_93C0D8BF6B430F32, STV_TE_C22DE139B2E5DF52, STV_TE_F75BB11AA22CCBEA, STV_TE_5BD3D06F689A4099, STV_TE_71A42A22CDFDE17A
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_host_owns_broken_trace_failure``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_host_owns_broken_trace_failure" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_host_owns_broken_trace_failure(tmp_path):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          with (source / "conf.py").open("a", encoding="utf-8") as stream:
              stream.write('\nneeds_report_dead_links = True\n')
          path = source / "requirements.rst"
          path.write_text(path.read_text(encoding="utf-8").replace(":traces: LEAF_B", ":traces: MISSING_A"), encoding="utf-8")
          output = tmp_path / "html"
          result = build(source, output)
          assert result.returncode != 0
          assert "MISSING_A" in result.stderr
          assert "STV_PENDING" not in (output / "index.html").read_text(encoding="utf-8")
          data = manifest(output)
          assert ["ROOT_A", "traces", "MISSING_A"] in data["edges"]
          assert "MISSING_A" not in data["objects"]

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_028: seed selection release
-------------------------------------

.. test_case:: seed selection release
   :id: STV_TC_SY_028
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_release_seeds.py :: docs/test-scripts/test_release_seeds.py::test_seed_selection_release[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_003, STV_SHR_014, STV_SHR_026, STV_SHR_038, STV_SHR_047, STV_SHR_048, STV_SHR_052, STV_SHR_053, STV_SWR_003, STV_SWR_038, STV_SWR_048, STV_SWR_051, STV_SWR_052, STV_SWR_056, STV_SWR_057
   :executed_by: STV_TE_56BF0F252E2B0681, STV_TE_2BE1C4B126B18F38, STV_TE_BB04E44583D97C0D, STV_TE_AD1513DB7BEF1B53, STV_TE_F3E1482ECEAD8334
   :last_result: passed

   **Level:** System/browser acceptance.

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

STV_TC_SY_029: host default directional labels are used
-------------------------------------------------------

.. test_case:: host default directional labels are used
   :id: STV_TC_SY_029
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_host_default_directional_labels_are_used
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_045, STV_SWR_045
   :executed_by: STV_TE_379307EDD1A87108, STV_TE_45E5FFF9B4722E84, STV_TE_C1E476628B443676, STV_TE_CFF8782DE1D60572, STV_TE_B8467BD319FACA48, STV_TE_580685ED94D01FB9, STV_TE_4C39FAAE619D9350
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_host_default_directional_labels_are_used``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_host_default_directional_labels_are_used" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_host_default_directional_labels_are_used(tmp_path):
          source=tmp_path/'source';shutil.copytree(FIXTURE,source)
          with (source/'conf.py').open('a',encoding='utf-8') as stream:
              stream.write('\nneeds_links={"traces":{}}\n')
          output=tmp_path/'html';result=build(source,output)
          assert result.returncode==0,result.stderr
          assert manifest(output)['model']['relations']['traces']=={'incoming':'traces incoming','outgoing':'traces'}

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_030: offline exploration
----------------------------------

.. test_case:: offline exploration
   :id: STV_TC_SY_030
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_offline_exploration[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_004, STV_SHR_008, STV_SHR_015, STV_SHR_016, STV_SHR_017, STV_SHR_018, STV_SHR_029, STV_SHR_031, STV_SHR_033, STV_SHR_034, STV_SHR_035, STV_SHR_038, STV_SHR_039, STV_SHR_040, STV_SWR_004, STV_SWR_008, STV_SWR_015, STV_SWR_016, STV_SWR_017, STV_SWR_018, STV_SWR_029, STV_SWR_031, STV_SWR_033, STV_SWR_034, STV_SWR_035, STV_SWR_038, STV_SWR_039, STV_SWR_040, STV_SWR_050, STV_SYS_003, STV_SYS_007
   :executed_by: STV_TE_CFC88A8408D563AF, STV_TE_36AF6C6B39F1B4F5, STV_TE_387407E224540198, STV_TE_4A72E96BA6DE2E1E, STV_TE_536E631428F4AA4A, STV_TE_174B9C66EB0119E6
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_offline_exploration[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_offline_exploration[file]" -q``.

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

STV_TC_SY_031: project paging
-----------------------------

.. test_case:: project paging
   :id: STV_TC_SY_031
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_project_paging[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_CBBC2FACA177EA6A, STV_TE_8F519B08D780D32F, STV_TE_9C2EF2AAB951A88F, STV_TE_92C56796616E739A, STV_TE_77A4405F2A5366B4
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_project_paging[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_project_paging[file]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_project_paging(browser,short_output,protocol):
          import shutil
          source=short_output/'source';shutil.copytree(FIXTURE,source)
          (source/'requirements.rst').write_text('Requirements\n============\n\n'+'\n'.join(f'.. shr:: Stakeholder {i}\n   :id: GOAL_{i:03}\n' for i in range(201)),encoding='utf-8')
          (source/'index.rst').write_text('Project\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view::\n',encoding='utf-8')
          output=short_output/'html';result=build(source,output);assert result.returncode==0,result.stderr
          with published_url(output,protocol) as url:
              browser.get(url)
              _assert_project_pages(browser)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_032: async layout failure and stale completion
--------------------------------------------------------

.. test_case:: async layout failure and stale completion
   :id: STV_TC_SY_032
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_044, STV_SHR_047, STV_SWR_044, STV_SWR_052
   :executed_by: STV_TE_3A7FDDC0E8DA0DCC, STV_TE_9DEB9C844A02AF74, STV_TE_BC7B47354D524871, STV_TE_9D6EBF6A6F0743F7, STV_TE_80574D51B50F80B0
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[http]" -q``.

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
          result=subprocess.run(['node','--input-type=module','-e',script,str(project/'docs/test-scripts/fixtures/browser-harness.js'),str(short_output/'harness.js')],cwd=project/'frontend',capture_output=True,text=True)
          assert result.returncode==0,result.stderr
          (short_output/'index.html').write_text('<link rel="stylesheet" href="'+(project/'src/sphinx_traceability_view/static/stv.css').as_uri()+'"><div class="stv-view" id="test-view" data-stv-seeds=\'["A"]\'></div><script src="harness.js"></script>',encoding='utf-8')
          # Keep the host alive across all injected completions.
          with published_url(short_output,protocol) as url:
              browser.get(url)
              _assert_async_layout(browser)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_033: alternate model geometry details and external
------------------------------------------------------------

.. test_case:: alternate model geometry details and external
   :id: STV_TC_SY_033
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_008, STV_SHR_012, STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_026, STV_SHR_029, STV_SHR_031, STV_SHR_033, STV_SHR_037, STV_SHR_041, STV_SHR_047, STV_SHR_048, STV_SWR_008, STV_SWR_012, STV_SWR_015, STV_SWR_029, STV_SWR_031, STV_SWR_033, STV_SWR_037, STV_SWR_041, STV_SWR_047, STV_SWR_048, STV_SWR_049, STV_SWR_050, STV_SYS_004, STV_SYS_005, STV_SYS_006, STV_SYS_010
   :executed_by: STV_TE_A7749A458DE50DB9, STV_TE_C45BE36EF5E5D893, STV_TE_0B94DF5EA07D94A1, STV_TE_5479348C2D1ACE13, STV_TE_4BC4C1C6145FF78B, STV_TE_82B77D01320C4E9B
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[http]" -q``.

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

STV_TC_SY_034: empty seed catalog
---------------------------------

.. test_case:: empty seed catalog
   :id: STV_TC_SY_034
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_release_seeds.py :: docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SHR_053, STV_SWR_051, STV_SWR_052, STV_SWR_057
   :executed_by: STV_TE_EAB2D41B5168D79C, STV_TE_F4B5B1B6C6055FE4, STV_TE_CD508D01E393339D, STV_TE_DA00E9FE56E5A125, STV_TE_6513DAB610F6BAE5
   :last_result: passed

   **Level:** System/browser acceptance.

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

STV_TC_SY_035: large project at visible capacity
------------------------------------------------

.. test_case:: large project at visible capacity
   :id: STV_TC_SY_035
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_capacity.py :: docs/test-scripts/test_capacity.py::test_large_project_at_visible_capacity[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_043, STV_SHR_044, STV_SWR_043, STV_SWR_044, STV_SYS_008
   :executed_by: STV_TE_EA4C3D20E892A129, STV_TE_A62ED5B70EFE8DD0, STV_TE_8DB38CDB318CBFBD, STV_TE_1B0FA04DA16E3401
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_capacity.py::test_large_project_at_visible_capacity[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_capacity.py::test_large_project_at_visible_capacity[http]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_large_project_at_visible_capacity(browser,protocol):
          output=Path(os.environ.get('STV_CAPACITY_OUTPUT','docs/_build/benchmark-v2/html')).resolve()
          assert (output/'index.html').is_file(),'Run scripts/benchmark.py before capacity verification'
          runs=[]
          browser.set_script_timeout(35)
          temporary=tempfile.TemporaryDirectory(prefix='stv-cap-') if protocol=='file' else None
          if temporary:
              assert Path(temporary.name).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
              # Full hash names need a short physical output root in Windows Firefox.
              short=Path(temporary.name)/'html';shutil.copytree(output,short);output=short
          try:
              _measure_capacity(browser,output,protocol,runs)
          finally:
              if temporary:
                  assert Path(temporary.name).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
                  temporary.cleanup()
          result={'browser':browser.capabilities['browserVersion'],'geckodriver':browser.capabilities.get('moz:geckodriverVersion'),
                  'memory_scope':'Sum of working sets of the isolated Firefox process tree, including content/GPU helpers; shared pages may be counted more than once',
                  'runs':runs,'startup_median_ms':statistics.median(r['startup_ms'] for r in runs),
                  'startup_max_ms':max(r['startup_ms'] for r in runs),
                  'expansion_median_ms':statistics.median(v for r in runs for v in r['expansion_ms']),
                  'expansion_max_ms':max(v for r in runs for v in r['expansion_ms'])}
          target=Path(os.environ.get('STV_CAPACITY_METRICS','docs/_build/capacity-browser.json'));target.parent.mkdir(parents=True,exist_ok=True)
          aggregate=json.loads(target.read_text(encoding='utf-8')) if target.exists() else {}
          aggregate[protocol]=result
          target.write_text(json.dumps(aggregate,indent=2),encoding='utf-8')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_036: seed layout replacement failure and staleness
------------------------------------------------------------

.. test_case:: seed layout replacement failure and staleness
   :id: STV_TC_SY_036
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_release_seeds.py :: docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_044, STV_SHR_053, STV_SWR_044, STV_SWR_057
   :executed_by: STV_TE_CDCABD8ACB9C2964, STV_TE_B65229E135C87272, STV_TE_0A999588B6A1920C, STV_TE_F0A444E2D30EB34A, STV_TE_031D77745B96D6B3
   :last_result: passed

   **Level:** System/browser acceptance.

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

STV_TC_SY_037: offline exploration
----------------------------------

.. test_case:: offline exploration
   :id: STV_TC_SY_037
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_browser.py :: docs/test-scripts/test_browser.py::test_offline_exploration[http]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_004, STV_SHR_008, STV_SHR_015, STV_SHR_016, STV_SHR_017, STV_SHR_018, STV_SHR_029, STV_SHR_031, STV_SHR_033, STV_SHR_034, STV_SHR_035, STV_SHR_038, STV_SHR_039, STV_SHR_040, STV_SWR_004, STV_SWR_008, STV_SWR_015, STV_SWR_016, STV_SWR_017, STV_SWR_018, STV_SWR_029, STV_SWR_031, STV_SWR_033, STV_SWR_034, STV_SWR_035, STV_SWR_038, STV_SWR_039, STV_SWR_040, STV_SWR_050, STV_SYS_003, STV_SYS_007
   :executed_by: STV_TE_CD6E815F9CAC0F7F, STV_TE_381A684E64CE327D, STV_TE_2FF9EA5FEF88B39F, STV_TE_F0C2845AEA49F292, STV_TE_CC11AD7C6E64725A, STV_TE_CE60972C9269D472
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_browser.py::test_offline_exploration[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_browser.py::test_offline_exploration[http]" -q``.

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

STV_TC_SY_038: clean wheel host
-------------------------------

.. test_case:: clean wheel host
   :id: STV_TC_SY_038
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_package.py :: docs/test-scripts/test_package.py::test_clean_wheel_host
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_042, STV_SHR_046, STV_SWR_042, STV_SWR_046, STV_SYS_009
   :executed_by: STV_TE_78A7F282F37C6E00, STV_TE_61BD7D777495C79E, STV_TE_46FCDBE70FFEE8BD, STV_TE_23CFB2E2F59258A0, STV_TE_7BEB3B1B6625A5DC, STV_TE_01F92BEF833F1EDE, STV_TE_E9C945EDF4A0769F, STV_TE_9AFC30AFCB2544CA, STV_TE_8C0DFF558A66DCA0, STV_TE_B4CE34E817E66D0A, STV_TE_8C81216F00482ADD
   :last_result: passed

   **Level:** System packaging integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_package.py::test_clean_wheel_host``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_package.py::test_clean_wheel_host" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   **PRSA-003 refinement:** Patch offline bootstrap tooling before installation.
   Prior design acceptance is preserved in historical reviews; the refined
   procedure awaits owner review.

   .. code-block:: python

      def test_clean_wheel_host():
          wheels=[Path(os.environ['STV_WHEEL'])] if os.environ.get('STV_WHEEL') else sorted((ROOT/'dist').glob('*.whl'))
          assert wheels,'Build the wheel before packaging verification'
          wheel=wheels[-1]
          wheelhouse=ROOT/'docs/_build/wheelhouse'
          assert wheelhouse.is_dir(),'Provision the runtime wheelhouse before offline packaging verification'
          with zipfile.ZipFile(wheel) as archive:
              names=archive.namelist()
              assert not any("/tests/" in name for name in names), "Unit tests must not ship in the runtime wheel"
              for asset in ('stv.js','stv.css','LICENSE.txt','THIRD_PARTY_NOTICES.txt','vendor/elk.bundled.js','vendor/ELK-SOURCE.txt','vendor/ELK-INVENTORY.json'):
                  assert f'sphinx_traceability_view/static/{asset}' in names
              packaged_inventory=json.loads(archive.read('sphinx_traceability_view/static/vendor/ELK-INVENTORY.json'))
              assert hashlib.sha256(archive.read('sphinx_traceability_view/static/vendor/elk.bundled.js')).hexdigest()==packaged_inventory['elkjs']['sha256']
              metadata=archive.read(next(name for name in names if name.endswith('.dist-info/METADATA'))).decode()
              assert not any('Requires-Dist: '+name in metadata for name in ('pytest','selenium','esbuild'))
              assert 'License-Expression: MIT AND ISC AND BSD-3-Clause AND Apache-2.0 AND EPL-1.0 AND EPL-2.0' in metadata
              assert 'Copyright (c) 2026 Henning Heikes' in archive.read('sphinx_traceability_view/static/LICENSE.txt').decode()
              license_members=[name for name in names if '.dist-info/licenses/' in name]
              assert any(name.endswith('/LICENSE') for name in license_members)
              assert any(name.endswith('/THIRD_PARTY_NOTICES.txt') for name in license_members)
              assert any(name.endswith('/ELK-SOURCE.txt') for name in license_members)
          source_archive=wheel.parent/(wheel.name.split('-py3-')[0]+'.tar.gz')
          with tarfile.open(source_archive,'r:gz') as archive:
              names=archive.getnames()
              assert any(name.endswith('/LICENSE') for name in names)
              assert any(name.endswith('/static/THIRD_PARTY_NOTICES.txt') for name in names)
              assert any(name.endswith('/static/vendor/ELK-SOURCE.txt') for name in names)

          with tempfile.TemporaryDirectory(prefix='stv-wheel-') as directory:
              root=Path(directory);envpath=root/'env'
              assert root.resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
              subprocess.run([sys.executable,'-m','venv',str(envpath)],check=True,capture_output=True)
              python=envpath/'Scripts/python.exe'
              bootstrap=subprocess.run([str(python),'-m','pip','install','--no-index','--find-links',str(wheelhouse),'-r',str(ROOT/'requirements-tooling.txt')],capture_output=True,text=True)
              assert bootstrap.returncode==0,bootstrap.stdout+bootstrap.stderr
              result=subprocess.run([str(python),'-m','pip','install','--no-index','--find-links',str(wheelhouse),str(wheel)],capture_output=True,text=True)
              assert result.returncode==0,result.stdout+result.stderr
              source=root/'source';shutil.copytree(ROOT/'docs/test-scripts/fixtures/minimal',source)
              env=dict(os.environ);env.pop('PYTHONPATH',None)
              env['PATH']=str(envpath/'Scripts')+os.pathsep+str(Path(os.environ['SystemRoot'])/'System32')
              result=subprocess.run([str(python),'-m','sphinx','-b','html','-W',str(source),str(root/'html')],env=env,cwd=root,capture_output=True,text=True)
              assert result.returncode==0,result.stdout+result.stderr
              assert 'STV_PENDING' not in (root/'html/index.html').read_text(encoding='utf-8')
              static=root/'html/_static/stv'
              assert (static/'LICENSE.txt').read_bytes()==(ROOT/'LICENSE').read_bytes()
              assert 'https://github.com/kieler/elkjs/tree/0.10.0' in (static/'vendor/ELK-SOURCE.txt').read_text(encoding='utf-8')
              notices=(static/'THIRD_PARTY_NOTICES.txt').read_text(encoding='utf-8')
              assert 'Eclipse Public License' in notices
              assert 'Apache License' in notices
              assert 'EMF-GWT common/ecore' in notices
              inventory=json.loads((static/'vendor/ELK-INVENTORY.json').read_text())
              assert inventory==packaged_inventory
              assert {x['license'] for x in inventory['compiled_dependencies']} >= {'Apache-2.0','EPL-1.0','EPL-2.0','MIT'}
              assert 'https://github.com/eclipse-elk/elk/tree/v0.10.0' in notices

              probe=subprocess.run([str(python),'-c','import sphinx_traceability_view as s;from importlib.metadata import version;assert s.__version__==version("sphinx-traceability-view");print(s.__file__);print(s.__version__)'],env=env,cwd=root,capture_output=True,text=True,check=True)
              assert str(envpath).lower() in probe.stdout.lower()
              retained=os.environ.get('STV_CONSUMER_RECORD')
              if retained:
                  destination=Path(retained);destination.mkdir(parents=True,exist_ok=True)
                  (destination/'build.log').write_text(result.stdout+result.stderr,encoding='utf-8')
                  frozen=subprocess.run([str(python),'-m','pip','freeze'],capture_output=True,text=True,check=True)
                  (destination/'environment.txt').write_text(frozen.stdout,encoding='utf-8')
                  (destination/'identity.txt').write_text(probe.stdout+'\nPATH='+env['PATH']+'\n',encoding='utf-8')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_039: empty seed catalog
---------------------------------

.. test_case:: empty seed catalog
   :id: STV_TC_SY_039
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_release_seeds.py :: docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SHR_053, STV_SWR_051, STV_SWR_052, STV_SWR_057
   :executed_by: STV_TE_F0A3E069E2F6967C, STV_TE_C419E178B9EBDAC3, STV_TE_52CF8B9BF7AA0812, STV_TE_0055C4B135295D6D, STV_TE_75640254413F6888
   :last_result: passed

   **Level:** System/browser acceptance.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[file]" -q``.

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

STV_TC_SY_040: unsupported builder fails clearly
------------------------------------------------

.. test_case:: unsupported builder fails clearly
   :id: STV_TC_SY_040
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_unsupported_builder_fails_clearly
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_001, STV_SWR_001
   :executed_by: STV_TE_B17272C4602B2A77, STV_TE_BE1ACFDE9841CB9D, STV_TE_DB3A63198D744D1A, STV_TE_5D5D6764322F0A1B, STV_TE_F6C5F1F06B8C8442, STV_TE_B4A4DD22BA6B72F8, STV_TE_09A2807578D5A808
   :last_result: passed

   **Level:** System integration through the public Sphinx build interface.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_unsupported_builder_fails_clearly``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_unsupported_builder_fails_clearly" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_unsupported_builder_fails_clearly(tmp_path):
          result=build(FIXTURE,tmp_path,'-b','text')
          assert result.returncode!=0
          assert 'supports only the html builder' in result.stderr

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_SY_041: Select separate occurrences
------------------------------------------

.. test_case:: Select separate occurrences
   :id: STV_TC_SY_041
   :status: accepted
   :tags: release_later, test_system
   :basis: documented
   :evidence: docs/requirements-stakeholder.rst; docs/requirements-software.rst
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_019, STV_SWR_019
   :last_result: not_run

   **Level/environment:** Planned browser acceptance, Windows/Firefox,
   file and nested static HTTP output, network blocked.

   **Preconditions/inputs:** Future occurrence-mode implementation; two
   parents sharing one child with two disjoint nonempty relationship groups.

   **Procedure:** Open a two-parent graph sharing one child. Select separate-occurrence mode, then shared mode.

   **Expected outcomes:** Separate mode shows two child occurrences; shared mode shows one. The selector and visible mode agree.

   Repeat with a cycle and a missing target to verify termination and visible
   placeholder identity. Start at 199 visible occurrences and request two more:
   the transition must be rejected atomically with the node-limit explanation.
   A transition to exactly 200 succeeds. Attempt a mode switch producing 201:
   retain mode, graph and exploration state and explain the limit.

   **Execution/evidence:** No executable implementation exists in v0.2.0.
   Retain per-case results, candidate identity and file/HTTP screenshots when
   the future release implements this scope; no execution record is invented.

STV_TC_SY_042: Restore occurrence exploration
---------------------------------------------

.. test_case:: Restore occurrence exploration
   :id: STV_TC_SY_042
   :status: accepted
   :tags: release_later, test_system
   :basis: documented
   :evidence: docs/requirements-stakeholder.rst; docs/requirements-software.rst
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_021, STV_SWR_021
   :last_result: not_run

   **Level/environment:** Planned browser acceptance, Windows/Firefox,
   file and nested static HTTP output, network blocked.

   **Preconditions/inputs:** Future occurrence-mode implementation; two
   parents sharing one child with two disjoint nonempty relationship groups.

   **Procedure:** In separate mode expand different groups in each occurrence. Switch to shared mode and back.

   **Expected outcomes:** Each occurrence recovers its own expanded and collapsed groups without losing prior exploration.

   Repeat with a cycle and a missing target to verify termination and visible
   placeholder identity. Start at 199 visible occurrences and request two more:
   the transition must be rejected atomically with the node-limit explanation.
   A transition to exactly 200 succeeds. Attempt a mode switch producing 201:
   retain mode, graph and exploration state and explain the limit.

   **Execution/evidence:** No executable implementation exists in v0.2.0.
   Retain per-case results, candidate identity and file/HTTP screenshots when
   the future release implements this scope; no execution record is invented.

STV_TC_SY_043: Isolate occurrence expansion
-------------------------------------------

.. test_case:: Isolate occurrence expansion
   :id: STV_TC_SY_043
   :status: accepted
   :tags: release_later, test_system
   :basis: documented
   :evidence: docs/requirements-stakeholder.rst; docs/requirements-software.rst
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_022, STV_SWR_022
   :last_result: not_run

   **Level/environment:** Planned browser acceptance, Windows/Firefox,
   file and nested static HTTP output, network blocked.

   **Preconditions/inputs:** Future occurrence-mode implementation; two
   parents sharing one child with two disjoint nonempty relationship groups.

   **Procedure:** In separate mode show two occurrences of one child through different parents. Expand a group on only the first.

   **Expected outcomes:** Only the first occurrence changes; the other retains its original graph and expansion state.

   Repeat with a cycle and a missing target to verify termination and visible
   placeholder identity. Start at 199 visible occurrences and request two more:
   the transition must be rejected atomically with the node-limit explanation.
   A transition to exactly 200 succeeds. Attempt a mode switch producing 201:
   retain mode, graph and exploration state and explain the limit.

   **Execution/evidence:** No executable implementation exists in v0.2.0.
   Retain per-case results, candidate identity and file/HTTP screenshots when
   the future release implements this scope; no execution record is invented.

STV_TC_SY_044: Merge shared expansion sets
------------------------------------------

.. test_case:: Merge shared expansion sets
   :id: STV_TC_SY_044
   :status: accepted
   :tags: release_later, test_system
   :basis: documented
   :evidence: docs/requirements-stakeholder.rst; docs/requirements-software.rst
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_023, STV_SWR_023
   :last_result: not_run

   **Level/environment:** Planned browser acceptance, Windows/Firefox,
   file and nested static HTTP output, network blocked.

   **Preconditions/inputs:** Future occurrence-mode implementation; two
   parents sharing one child with two disjoint nonempty relationship groups.

   **Procedure:** In separate mode expand disjoint groups on two copies. Switch to shared mode.

   **Expected outcomes:** One shared object remains with the union of both expanded groups and no duplicate canonical edges.

   Repeat with a cycle and a missing target to verify termination and visible
   placeholder identity. Start at 199 visible occurrences and request two more:
   the transition must be rejected atomically with the node-limit explanation.
   A transition to exactly 200 succeeds. Attempt a mode switch producing 201:
   retain mode, graph and exploration state and explain the limit.

   **Execution/evidence:** No executable implementation exists in v0.2.0.
   Retain per-case results, candidate identity and file/HTTP screenshots when
   the future release implements this scope; no execution record is invented.

STV_TC_SY_045: Inspect details from a nested Windows checkout
-------------------------------------------------------------

.. test_case:: Inspect details from a nested Windows checkout
   :id: STV_TC_SY_045
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/problem-tickets/STV_PR_006.rst
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SHR_018, STV_SYS_003, STV_SYS_006, STV_SWR_015, STV_SWR_017, STV_SWR_018
   :executed_by: STV_TE_1EA0D25151D74A7C, STV_TE_8691313C00B21F3E, STV_TE_3E9F0CC9AE6D1527, STV_TE_ADB1B05CE41E118B, STV_TE_610BEE40C54D1DA7
   :last_result: passed

   **Level/environment:** Windows browser system acceptance; stable Firefox
   with recorded version, direct file URLs and nested static HTTP hosting.

   **Executable selector:** ``docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry``.

   **Preconditions/inputs:** The fixture computes a nested output root where
   old two-hash asset paths exceed 260 characters and compact paths fit. Retain
   the actual measured lengths and the failed pre-fix attempt. Root and nested
   view pages display ROOT_A's formatted body, table and source links.

   **Procedure:** Build the host using the actual implementation. Open both
   pages over file and HTTP, activate Details with keyboard, compare rich
   content and links, then reload to clear fragment memory. Temporarily rename
   the detail asset, activate Details by pointer and require the unavailable
   error. Restore the asset, dismiss/reopen and require successful recovery.

   **Expected outcomes:** All four page/transport combinations display the
   correct body and retry successfully. The old path exceeds 260 characters,
   compact assets exist and fit below that threshold. The companion compact
   asset software case verifies full digest identity and deduplication.

   **Evidence:** Per-case JUnit/log, before/after path observations and rendered
   screenshots in the maintenance execution record. No arbitrary-depth path,
   other browser or other-machine support is inferred.

STV_TC_SY_046: Reject unaudited distribution inputs
---------------------------------------------------

.. test_case:: Reject unaudited distribution inputs
   :id: STV_TC_SY_046
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_legal_guard.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042
   :executed_by: STV_TE_7F0E0FAA905ACCA8, STV_TE_FA10CBBD5A653BBA, STV_TE_B143FA7927D35E75, STV_TE_506DA5166F4226E8, STV_TE_1074CEBE7559F606, STV_TE_EF7E4DAFEAFBC4FA, STV_TE_EE13FB7DE2E2F1CD
   :last_result: passed

   **Level:** System build/distribution interface.

   **Executable selector:** ``docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices``.

   **Preconditions:** Pinned Node/esbuild installation and maintained legal
   inventory; use an isolated copy for dependency/legal inputs.

   **Procedure and expected outcomes:** Invoke the real frontend build against
   a changed ELK version, changed binary, modified legal text and missing EPL
   notice. Each must fail with its specific audit/input diagnostic before
   distributing browser output. Preserve installed dependencies unchanged.

   **Evidence:** Per-case JUnit and command log. The clean installed-wheel case
   separately verifies the successful shipping path and notice inventory.

STV_TC_SY_047: Authored transport markers remain inert over file
----------------------------------------------------------------

.. test_case:: Authored transport markers remain inert over file
   :id: STV_TC_SY_047
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_detail_transport.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_015, STV_SWR_017, STV_SWR_018, STV_SWR_049
   :executed_by: STV_TE_55377E9CDFC887DC, STV_TE_04F7EDED17CC043F
   :last_result: passed

   **Level:** Integrated system/browser regression.

   **Preconditions and inputs:** Existing implementation environment; Node for
   frontend tests and provisioned Firefox/geckodriver for browser cases.
   Use a fresh isolated build; the test controls only harmless marker values
   and loopback resources. No external requests are needed.

   **Executable selector:** ``docs/test-scripts/test_detail_transport.py::test_authored_transport_markers_stay_inert[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_detail_transport.py::test_authored_transport_markers_stay_inert[file]" -q``.

   **Procedure and expected outcomes:** Build and open the real fixture in Firefox over file. Open details and click the inert link; require no marker execution or loopback beacon requests, no forged src/srcset, and preserved local images, srcset, navigation, CSS and table.

   **Evidence:** Retain actual JUnit results, commands and source identities in
   :doc:`../test-execution/prsa-002-fix/index`. Design review remains pending.

STV_TC_SY_048: Authored transport markers remain inert over HTTP
----------------------------------------------------------------

.. test_case:: Authored transport markers remain inert over HTTP
   :id: STV_TC_SY_048
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_detail_transport.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_015, STV_SWR_017, STV_SWR_018, STV_SWR_049
   :executed_by: STV_TE_5DD66163012116DE, STV_TE_073124C33BD1B11A
   :last_result: passed

   **Level:** Integrated system/browser regression.

   **Preconditions and inputs:** Existing implementation environment; Node for
   frontend tests and provisioned Firefox/geckodriver for browser cases.
   Use a fresh isolated build; the test controls only harmless marker values
   and loopback resources. No external requests are needed.

   **Executable selector:** ``docs/test-scripts/test_detail_transport.py::test_authored_transport_markers_stay_inert[http]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_detail_transport.py::test_authored_transport_markers_stay_inert[http]" -q``.

   **Procedure and expected outcomes:** Repeat the file regression over a loopback HTTP server, with the same expected outcomes and explicit external navigation link retained without activation.

   **Evidence:** Retain actual JUnit results, commands and source identities in
   :doc:`../test-execution/prsa-002-fix/index`. Design review remains pending.

STV_TC_SY_049: Retained historical archives carry a complete licensing supplement
---------------------------------------------------------------------------------

.. test_case:: Retained historical archives carry a complete licensing supplement
   :id: STV_TC_SY_049
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: scripts/historical-licenses.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042, STV_SWR_046
   :executed_by: STV_TE_89D9283C4480C51F
   :last_result: passed

   **Level:** Repository/distribution integration.

   **Preconditions:** Retained project Git objects and supplement for the
   historical case; patched offline runtime wheelhouse, development artifact
   and existing Python 3.10 executable for runtime compatibility.

   **Executable selector:** ``scripts/historical-licenses.py``.

   **Invocation:** Run the indicated script with the implementation Python;
   the runtime script additionally takes ``--python310 <executable>``.

   **Procedure and expected outcomes:** Check every available historical Git archive and retained canonical archive. Require the audited upstream ELK fingerprint and byte-identical complete supplement materials; retain immutable artifact hashes.

   **Evidence:** Actual result in ``historical-licenses.log`` and source/environment identity
   in :doc:`../test-execution/prsa-001-003-fix/index`. Design review is pending.

STV_TC_SY_050: Patched offline distribution remains usable on Python 3.10
-------------------------------------------------------------------------

.. test_case:: Patched offline distribution remains usable on Python 3.10
   :id: STV_TC_SY_050
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-execution/prsa-001-003-fix/check-runtime310.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042, STV_SWR_046
   :executed_by: STV_TE_A097E5958A89160A
   :last_result: passed

   **Level:** Repository/distribution integration.

   **Preconditions:** Retained project Git objects and supplement for the
   historical case; patched offline runtime wheelhouse, development artifact
   and existing Python 3.10 executable for runtime compatibility.

   **Executable selector:** ``docs/test-execution/prsa-001-003-fix/check-runtime310.py``.

   **Invocation:** Run the indicated script with the implementation Python;
   the runtime script additionally takes ``--python310 <executable>``.

   **Procedure and expected outcomes:** Create a Python 3.10 environment, install patched bootstrap tools and the development wheel from the offline wheelhouse, run pip check, build the minimal Sphinx host, and verify installed module identity and copied inventory.

   **Evidence:** Actual result in ``runtime310.json`` and source/environment identity
   in :doc:`../test-execution/prsa-001-003-fix/index`. Design review is pending.

STV_TC_SY_051: Actual source archive respects the distribution boundary
-----------------------------------------------------------------------

.. test_case:: Actual source archive respects the distribution boundary
   :id: STV_TC_SY_051
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_sdist.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042, STV_SWR_046
   :executed_by: STV_TE_053E27C9576BC49A, STV_TE_3F0DEB05F990600D, STV_TE_74B1E2689D5AA322, STV_TE_1DDD21C8F37EF5DC
   :last_result: passed

   **Level:** Packaging integration.

   **Preconditions and inputs:** Existing implementation environment and
   frontend/legal assets. The test copies build inputs to an isolated source
   tree and seeds local-only evidence/cache/tool files, including execution
   logs subject to root and nested ignore negations.

   **Executable selector:** ``docs/test-scripts/test_sdist.py::test_sdist_excludes_local_evidence_and_rebuilds_wheel``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest docs/test-scripts/test_sdist.py -q``.

   **Procedure and expected outcomes:** Build the actual source archive and
   its wheel using the normal build frontend. Inspect tar members and content;
   require no seeded evidence or local-only sentinel bytes, and require source,
   legal and build inputs. Compare rebuilt wheel browser assets and notices
   byte-for-byte with their source archive members. The separate existing
   installed-wheel case verifies an isolated offline consumer.

   **Evidence:** Retain JUnit/log results, source identity, artifact hashes and
   member inventory in :doc:`../test-execution/prsa-004-fix/index`. The initial
   old-configuration failure is historical; the latest outcome is independent
   of owner acceptance and release readiness.

STV_TC_SY_052: Clean rebuild retires obsolete publication files
---------------------------------------------------------------

.. test_case:: Clean rebuild retires obsolete publication files
   :id: STV_TC_SY_052
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_publication.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042
   :executed_by: STV_TE_D5D5C30CB3605726, STV_TE_00DF8B8564A416AA, STV_TE_0BA0673DB0572C62, STV_TE_DF5D6826958881EC, STV_TE_9A991F5CD63BFC3C
   :last_result: passed

   **Level:** Maintainer/Sphinx publication integration.

   **Preconditions and inputs:** Existing implementation environment and local
   extension source. Use isolated temporary Sphinx source/build directories;
   no installed public output or external service is modified by the case.

   **Executable selector:** ``docs/test-scripts/test_publication.py::test_clean_publication_removes_obsolete_assets``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest docs/test-scripts/test_publication.py -q``.

   **Procedure and expected outcomes:** Build the real Sphinx fixture with two Needs, a retired page and a download. Remove one Need/page/download reference and seed an obsolete output file. Rebuild; require one current graph, no old graph/page/download, no public doctree cache, and a complete byte-verified manifest. Previous output must remain outside html.

   **Evidence:** Retain actual JUnit/log outcomes, source hashes and relative
   file inventory in :doc:`../test-execution/prsa-005-fix/index`. New design
   review remains pending; these are not full release qualification cases.

STV_TC_SY_053: Failed documentation build preserves published bytes
-------------------------------------------------------------------

.. test_case:: Failed documentation build preserves published bytes
   :id: STV_TC_SY_053
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_publication.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042
   :executed_by: STV_TE_04F65BAA6CDB685B, STV_TE_057BEBB8A33EC7E4, STV_TE_4B16C75492B3457D, STV_TE_37C71B72B4C9EB26, STV_TE_55FA0354073DF3AF
   :last_result: passed

   **Level:** Maintainer/Sphinx publication integration.

   **Preconditions and inputs:** Existing implementation environment and local
   extension source. Use isolated temporary Sphinx source/build directories;
   no installed public output or external service is modified by the case.

   **Executable selector:** ``docs/test-scripts/test_publication.py::test_failed_build_preserves_published_tree``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest docs/test-scripts/test_publication.py -q``.

   **Procedure and expected outcomes:** Build successfully and snapshot every publication file. Introduce an unknown Sphinx directive. Require a nonzero build result and an identical published file/hash snapshot.

   **Evidence:** Retain actual JUnit/log outcomes, source hashes and relative
   file inventory in :doc:`../test-execution/prsa-005-fix/index`. New design
   review remains pending; these are not full release qualification cases.

STV_TC_SY_054: Failed directory promotion restores previous publication
-----------------------------------------------------------------------

.. test_case:: Failed directory promotion restores previous publication
   :id: STV_TC_SY_054
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_publication.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042
   :executed_by: STV_TE_257F51CA54DE5456, STV_TE_D90868BD589779C5, STV_TE_E0C20537B8E451DF, STV_TE_D03C25CCCCEF8DF9, STV_TE_4658E397071ACF9C
   :last_result: passed

   **Level:** Maintainer/Sphinx publication integration.

   **Preconditions and inputs:** Existing implementation environment and local
   extension source. Use isolated temporary Sphinx source/build directories;
   no installed public output or external service is modified by the case.

   **Executable selector:** ``docs/test-scripts/test_publication.py::test_failed_promotion_restores_previous_tree``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest docs/test-scripts/test_publication.py -q``.

   **Procedure and expected outcomes:** Build successfully and snapshot all published files. Inject an OSError only for the fresh-stage-to-html rename after the prior output is moved. Require the failure to propagate and every previous publication file/hash to be restored.

   **Evidence:** Retain actual JUnit/log outcomes, source hashes and relative
   file inventory in :doc:`../test-execution/prsa-005-fix/index`. New design
   review remains pending; these are not full release qualification cases.

STV_TC_SY_055: CI policy rejects privilege and provenance drift
---------------------------------------------------------------

.. test_case:: CI policy rejects privilege and provenance drift
   :id: STV_TC_SY_055
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_ci_security.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042
   :executed_by: STV_TE_136F9269B7351A90, STV_TE_30562D2F63C7ED1A, STV_TE_A0B0212F491B4997, STV_TE_4E407028E958FA48
   :last_result: passed

   **Level:** CI/distribution integration.

   **Preconditions and inputs:** Maintained implementation environment for
   workflow/checksum tests, real GitHub workflow files, Git and GNU sha256sum.
   The runtime case requires the development wheel installed on Python 3.10.
   No hosted workflow or attestation service is used in these local checks.

   **Executable selector:** ``docs/test-scripts/test_ci_security.py::test_workflow_policy_accepts_reviewed_files_and_rejects_privilege_drift``.

   **Invocation:** Run pytest for ``docs/test-scripts/test_ci_security.py``;
   for the runtime case, use the installed Python 3.10 host to run
   ``scripts/ci.py runtime``.

   **Procedure and expected outcomes:** Load both real workflow files, require the reviewed least-privilege policy, and mutate copies to request write tokens, unsafe triggers, mutable action tags, privileged repository code, missing attestation jobs, altered subjects or an unrestricted attestation condition. Every modified variant must be rejected.

   **Evidence:** Retain actual reports, commands and source/artifact identities
   in :doc:`../test-execution/prsa-006-fix/index`. Case design review is pending;
   local verification does not prove a hosted run or attestation occurred.

STV_TC_SY_056: Candidate checksums detect changed artifact bytes
----------------------------------------------------------------

.. test_case:: Candidate checksums detect changed artifact bytes
   :id: STV_TC_SY_056
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_ci_security.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042
   :executed_by: STV_TE_0086C904AA50BF6E, STV_TE_F46E8734D73CCD1D, STV_TE_D0BFD3B60852DD51, STV_TE_EAC633983360B5F2
   :last_result: passed

   **Level:** CI/distribution integration.

   **Preconditions and inputs:** Maintained implementation environment for
   workflow/checksum tests, real GitHub workflow files, Git and GNU sha256sum.
   The runtime case requires the development wheel installed on Python 3.10.
   No hosted workflow or attestation service is used in these local checks.

   **Executable selector:** ``docs/test-scripts/test_ci_security.py::test_candidate_checksums_detect_changed_artifact_bytes``.

   **Invocation:** Run pytest for ``docs/test-scripts/test_ci_security.py``;
   for the runtime case, use the installed Python 3.10 host to run
   ``scripts/ci.py runtime``.

   **Procedure and expected outcomes:** Generate checksums and source metadata for a wheel/source pair. Verify both with GNU sha256sum, alter wheel bytes and require verification failure. An extra wheel must make checksum generation fail rather than omit an ambiguous subject.

   **Evidence:** Retain actual reports, commands and source/artifact identities
   in :doc:`../test-execution/prsa-006-fix/index`. Case design review is pending;
   local verification does not prove a hosted run or attestation occurred.

STV_TC_SY_057: CI runtime command imports the installed Python 3.10 package
---------------------------------------------------------------------------

.. test_case:: CI runtime command imports the installed Python 3.10 package
   :id: STV_TC_SY_057
   :status: draft
   :tags: release_initial, test_system
   :basis: documented
   :evidence: scripts/ci.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_009, STV_SWR_042
   :executed_by: STV_TE_B5A2DB777F66970D
   :last_result: passed

   **Level:** CI/distribution integration.

   **Preconditions and inputs:** Maintained implementation environment for
   workflow/checksum tests, real GitHub workflow files, Git and GNU sha256sum.
   The runtime case requires the development wheel installed on Python 3.10.
   No hosted workflow or attestation service is used in these local checks.

   **Executable selector:** ``scripts/ci.py runtime``.

   **Invocation:** Run pytest for ``docs/test-scripts/test_ci_security.py``;
   for the runtime case, use the installed Python 3.10 host to run
   ``scripts/ci.py runtime``.

   **Procedure and expected outcomes:** Install the newly built development wheel into a Python 3.10 host, execute the CI runtime subcommand, require an installed-package import outside the checkout, matching installed version, a successful pip check and warnings-as-errors Sphinx fixture build.

   **Evidence:** Retain actual reports, commands and source/artifact identities
   in :doc:`../test-execution/prsa-006-fix/index`. Case design review is pending;
   local verification does not prove a hosted run or attestation occurred.

STV_TC_SY_058: Stable keyboard navigation and project root toggles
------------------------------------------------------------------

.. test_case:: Stable keyboard navigation and project root toggles
   :id: STV_TC_SY_058
   :status: accepted
   :tags: release_initial, test_system, navigation_stability
   :basis: documented
   :evidence: docs/test-scripts/test_position_stability.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_054, STV_SWR_058
   :executed_by: STV_TE_BFC00DA35F1B2273
   :last_result: passed

   **Level/environment:** System browser integration: Windows, Firefox/geckodriver, both file and loopback HTTP, external network blocked.

   **Preconditions:** Rebuilt local browser asset and isolated fixtures. Current
   development identity is retained separately from historical PoC evidence.

   **Selector/invocation:** ``test_group_navigation_keeps_existing_nodes_still``
   and ``test_project_root_preserves_anchor`` in ``test_position_stability.py``;
   also ``test_async_layout_failure_and_stale_completion`` in ``test_browser.py``;
   run with pytest using STV_GECKODRIVER.

   **Inputs/procedure:** Build isolated P/Q seeds, A-F children; focus and activate
   P,Q,P,P controls with Enter, recording all before/after world and screen boxes.
   Repeat for a seedless project root with collapsed/reopened stakeholder entries.

   **Expected:** All surviving nodes in the simple unchanged-height fixture move
   less than 0.5 px, clicked focus is restored without native scrolling, revision
   advances once per successful toggle and root coordinates remain stationary.
   The async harness additionally asserts last-successful snapshot identity after
   failure/stale work; independent-view cases remain complementary gates.

STV_TC_SY_059: Negative route rendering and viewport reset
----------------------------------------------------------

.. test_case:: Negative route rendering and viewport reset
   :id: STV_TC_SY_059
   :status: accepted
   :tags: release_initial, test_system, navigation_stability
   :basis: documented
   :evidence: docs/test-scripts/test_position_stability.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_054, STV_SWR_059
   :executed_by: STV_TE_E018DFA57A2EB582
   :last_result: passed

   **Level/environment:** System browser integration: Windows, Firefox/geckodriver, both file and loopback HTTP, external network blocked.

   **Preconditions:** Rebuilt local browser asset and isolated fixtures. Current
   development identity is retained separately from historical PoC evidence.

   **Selector/invocation:** ``test_arrow_viewport_covers_negative_routes`` in
   ``test_position_stability.py`` with pytest and STV_GECKODRIVER.

   **Inputs/procedure:** Expand downward P to five children (negative x), and upward
   A to P then R with a wrapping relation label (negative y). Read final SVG route
   points, viewBox and screen CTM. Record retained node positions. Activate Reset
   viewport and inspect fitted node boxes; repeat on file and HTTP.

   **Expected:** At least one negative point in each configured direction fixture,
   every route point inside the padded viewBox, and first/last route endpoints on
   node boundaries within 2 screen px. Surviving nodes do not move on toggles.
   Reset fits all node boxes inside the viewport without changing world positions;
   markers and paths remain visible. Pan/zoom and focus have existing adjacent cases.

STV_TC_SY_060: Natural seeded order survives expansion
------------------------------------------------------

.. test_case:: Natural seeded order survives expansion
   :id: STV_TC_SY_060
   :status: accepted
   :tags: release_initial, test_system, navigation_stability
   :basis: documented
   :evidence: docs/test-scripts/test_position_stability.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_055, STV_SWR_060
   :executed_by: STV_TE_873F1D2F001CA837
   :last_result: passed

   **Level/environment:** System browser integration: Windows, Firefox/geckodriver, both file and loopback HTTP, external network blocked.

   **Preconditions:** Rebuilt local browser asset and isolated fixtures. Current
   development identity is retained separately from historical PoC evidence.

   **Selector/invocation:** ``test_initial_numeric_seed_order`` in
   ``test_position_stability.py`` with pytest and STV_GECKODRIVER.

   **Inputs/procedure:** Build shuffled REQ_20, REQ_10, REQ_3, REQ_2, REQ_1 seeds,
   read actual DOM/world x ordering and expand REQ_2 to CHILD_A.

   **Expected:** Initial left-to-right IDs are REQ_1, REQ_2, REQ_3, REQ_10, REQ_20;
   all existing world/screen coordinates remain within 0.5 px after expansion.
   Project-mode ordering is independently covered by STV_TC_SW_045.

STV_TC_SY_061: Published nine-row evidence navigation
-----------------------------------------------------------

.. test_case:: Published nine-row evidence navigation
   :id: STV_TC_SY_061
   :status: accepted
   :tags: release_initial, test_system
   :basis: documented
   :evidence: docs/test-scripts/test_classified_rows.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_009, STV_SHR_010, STV_SHR_011, STV_SHR_012, STV_SHR_054, STV_SYS_002, STV_SYS_005, STV_SWR_012, STV_SWR_037, STV_SWR_055, STV_SWR_058, STV_SWR_061
   :executed_by: STV_TE_17192149B6D99989
   :last_result: passed

   **Level/environment:** Windows Firefox/geckodriver; file and local HTTP with
   external requests blocked; built package assets and isolated Sphinx host.
   **Procedure:** Build all nine categories with same-row peers, multiple actual
   execution identities, a cross-level shared case and fallback case/execution.
   Start in turn at software, case and execution; expand all relevant groups,
   record DOM/world coordinates, Reset to inspect complete scene and collapse.
   **Expected:** Nine ordered rows and same-row top alignment; fallback below
   software architecture, visible unclassified labels and valid endpoints. Shared
   case appears once and does not switch row with visible requirements. Anchor and
   surviving peers stay stationary. Original links/details, independent views,
   natural seed order, project root and absent categories retain their contracts.
   Run pytest docs/test-scripts/test_classified_rows.py with STV_GECKODRIVER.
