"""Release-level interactive seed criteria beyond the MVP smoke selection."""
import shutil
import subprocess
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from test_build import build, FIXTURE
from test_browser import browser, short_output, published_url, _assert_async_layout


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_003','STV_SWR_038','STV_SWR_048','STV_SWR_051','STV_SWR_052','STV_SWR_056','STV_SWR_057')
@pytest.mark.parametrize('protocol',['file','http'])
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


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_051','STV_SWR_052','STV_SWR_057')
@pytest.mark.parametrize('protocol',['file','http'])
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


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_044','STV_SWR_057')
@pytest.mark.parametrize('protocol',['file','http'])
def test_seed_layout_replacement_failure_and_staleness(browser,short_output,protocol):
    from pathlib import Path
    project=Path(__file__).parents[1]
    script="import{build}from'esbuild';await build({entryPoints:[process.argv[1]],bundle:true,format:'iife',outfile:process.argv[2]})"
    result=subprocess.run(['node','--input-type=module','-e',script,str(project/'tests/fixtures/browser-harness.js'),str(short_output/'harness.js')],cwd=project/'frontend',capture_output=True,text=True)
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
