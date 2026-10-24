"""Run with STV_GECKODRIVER explicitly set; uses installed release Firefox."""
from functools import partial
from contextlib import contextmanager
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import json
import threading
import tempfile
import time
import subprocess
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from test_build import build, FIXTURE


@pytest.mark.browser
@pytest.mark.requirements('STV_SYS_006', 'STV_SWR_050', 'STV_SWR_054')
@pytest.mark.parametrize('protocol',['file','http'])
def test_usability_smoke(browser, short_output, protocol):
    """Viewport, hover lifecycle and explicit activation on both transports."""
    output = short_output / 'usability'
    result = build(FIXTURE, output)
    assert result.returncode == 0, result.stderr
    with published_url(output,protocol) as url:
        browser.get(url)
        _exercise_usability(browser)


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


@contextmanager
def published_url(output, protocol):
    server=None
    try:
        if protocol=='http':
            server=ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(output.parent)))
            threading.Thread(target=server.serve_forever,daemon=True).start()
            yield f'http://127.0.0.1:{server.server_port}/{output.name}/index.html'
        else:yield (output/'index.html').as_uri()
    finally:
        if server:server.shutdown();server.server_close()


@pytest.fixture
def browser():
    driver_path = os.environ.get("STV_GECKODRIVER")
    if not driver_path:
        pytest.fail("Set STV_GECKODRIVER to the provisioned geckodriver executable")
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    options.set_preference("network.dns.disablePrefetch", True)
    options.set_preference("network.prefetch-next", False)
    options.set_preference("network.proxy.type", 1)
    options.set_preference("network.proxy.http", "127.0.0.1")
    options.set_preference("network.proxy.http_port", 9)
    options.set_preference("network.proxy.ssl", "127.0.0.1")
    options.set_preference("network.proxy.ssl_port", 9)
    options.set_preference("network.proxy.no_proxies_on", "localhost,127.0.0.1")
    driver = webdriver.Firefox(service=Service(driver_path), options=options)
    driver.set_window_size(1440, 1100)
    yield driver
    driver.quit()


@pytest.fixture
def short_output():
    # Firefox's Windows file loader rejects paths beyond MAX_PATH. Content
    # hashes deliberately use full digests, so keep the fixture root short.
    with tempfile.TemporaryDirectory(prefix="stv-") as directory:
        assert Path(directory).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
        yield Path(directory)


@pytest.mark.browser
@pytest.mark.requirements("STV_SYS_003", "STV_SYS_007", "STV_SWR_004", "STV_SWR_008", "STV_SWR_015", "STV_SWR_016", "STV_SWR_017", "STV_SWR_018", "STV_SWR_029", "STV_SWR_031", "STV_SWR_033", "STV_SWR_034", "STV_SWR_035", "STV_SWR_038", "STV_SWR_039", "STV_SWR_040", "STV_SWR_050")
@pytest.mark.parametrize("protocol", ["file", "http"])
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


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_051','STV_SWR_052')
@pytest.mark.parametrize('protocol',['file','http'])
def test_project_paging(browser,short_output,protocol):
    import shutil
    source=short_output/'source';shutil.copytree(FIXTURE,source)
    (source/'requirements.rst').write_text('Requirements\n============\n\n'+'\n'.join(f'.. shr:: Stakeholder {i}\n   :id: GOAL_{i:03}\n' for i in range(201)),encoding='utf-8')
    (source/'index.rst').write_text('Project\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view::\n',encoding='utf-8')
    output=short_output/'html';result=build(source,output);assert result.returncode==0,result.stderr
    with published_url(output,protocol) as url:
        browser.get(url)
        _assert_project_pages(browser)


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_056','STV_SWR_057','STV_SWR_038')
@pytest.mark.parametrize('protocol',['file','http'])
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


def _assert_project_pages(browser):
    wait=WebDriverWait(browser,30)
    wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
    root=browser.find_element(By.CSS_SELECTOR,'.stv-view')
    assert root.find_element(By.CSS_SELECTOR,'.stv-project strong').text=='STV <Example>'
    assert not root.find_elements(By.CSS_SELECTOR,'.stv-project a,.stv-project [data-focus="details"]')
    found=[]
    for page in range(41):
        found.extend(e.get_attribute('textContent') for e in root.find_elements(By.CSS_SELECTOR,'.stv-id'))
        assert f'Page {page+1} of 41 / 201' in root.find_element(By.CSS_SELECTOR,'.stv-project').text
        previous=root.find_element(By.CSS_SELECTOR,'[data-focus="Previous"]')
        assert previous.get_attribute('aria-disabled') == str(page==0).lower()
        next_button=root.find_element(By.CSS_SELECTOR,'[data-focus="Next"]')
        assert next_button.get_attribute('aria-disabled') == str(page==40).lower()
        if page<40:
            browser.execute_script('arguments[0].focus()',next_button);next_button.send_keys(Keys.ENTER)
            wait.until(lambda d:root.get_attribute('data-stv-revision')==str(page+1))
            assert browser.switch_to.active_element.get_attribute('data-focus') == 'Next'
    assert len(found)==len(set(found))==201
    assert root.find_element(By.CSS_SELECTOR,'[data-focus="Next"]').get_attribute('aria-disabled')=='true'


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_044','STV_SWR_052','STV_SWR_058')
@pytest.mark.parametrize('protocol',['file','http'])
def test_async_layout_failure_and_stale_completion(browser,short_output,protocol):
    project=Path(__file__).parents[2]
    script="import{build}from'esbuild';await build({entryPoints:[process.argv[1]],bundle:true,format:'iife',outfile:process.argv[2]})"
    result=subprocess.run(['node','--input-type=module','-e',script,str(project/'docs/test-scripts/fixtures/browser-harness.js'),str(short_output/'harness.js')],cwd=project/'frontend',capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    (short_output/'index.html').write_text('<link rel="stylesheet" href="'+(project/'src/sphinx_traceability_view/static/stv.css').as_uri()+'"><div class="stv-view" id="test-view" data-stv-seeds=\'["A"]\'></div><script src="harness.js"></script>',encoding='utf-8')
    # Keep the host alive across all injected completions.
    with published_url(short_output,protocol) as url:
        browser.get(url)
        _assert_async_layout(browser)


def _assert_async_layout(browser):
    browser.execute_script('''
      window.graph={schema:1,project:'Test',entries:['A'],model:{levels:['goal'],types:{goal:{level:'goal',color:'#fff'}},accepted_statuses:['accepted'],relations:{r:{incoming:'From',outgoing:'To'}}},
      objects:{A:{id:'A',title:'A',type:'goal',status:'accepted',url:'a.html'},B:{id:'B',title:'B',type:'goal',status:'accepted',url:'b.html'}},
      adjacency:{A:{incoming:{},outgoing:{r:['B']}},B:{incoming:{r:['A']},outgoing:{}}},details:{}};
      window.calls=[];
      window.mounted=stvHarness.mount(document.getElementById('test-view'),graph,new URL('./',location.href),(...args)=>new Promise((resolve,reject)=>calls.push({args,resolve,reject})));
    ''')
    wait=WebDriverWait(browser,20)
    wait.until(lambda d:d.execute_script('return calls.length')==1)
    browser.execute_script('calls[0].reject(Error("Controlled initial layout failure"))')
    wait.until(lambda d:'Controlled initial' in d.find_element(By.CSS_SELECTOR,'.stv-status').text)
    assert len(browser.find_elements(By.CSS_SELECTOR,'.stv-node'))==1
    browser.find_element(By.CSS_SELECTOR,'[aria-label="Retry layout"]').click()
    wait.until(lambda d:d.execute_script('return calls.length')==2)
    browser.execute_script('stvHarness.compute(...calls[1].args).then(calls[1].resolve)')
    wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'[data-stv-revision="0"]'))
    control=browser.find_element(By.CSS_SELECTOR,'[aria-label="Expand To (outgoing) for A"]')
    browser.execute_script('arguments[0].focus();arguments[0].click();arguments[0].click()',control)
    wait.until(lambda d:d.execute_script('return calls.length')==4)
    browser.execute_script('stvHarness.compute(...calls[3].args).then(calls[3].resolve)')
    wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'[data-stv-revision="1"]'))
    assert len(browser.find_elements(By.CSS_SELECTOR,'.stv-nodes > .stv-node'))==2
    browser.execute_script('calls[2].reject(Error("Stale result must be ignored"))')
    assert 'Stale result' not in browser.find_element(By.CSS_SELECTOR,'.stv-status').text
    control=browser.find_element(By.CSS_SELECTOR,'[aria-label="Collapse To (outgoing) for A"]')
    browser.execute_script('arguments[0].focus();arguments[0].click()',control)
    wait.until(lambda d:d.execute_script('return calls.length')==5)
    assert browser.execute_script('return calls[4].args[3].previous.nodes.size===2 && calls[4].args[3].anchor===JSON.stringify(["need","A"])')
    browser.execute_script('calls[4].reject(Error("Controlled subsequent failure"))')
    wait.until(lambda d:'Controlled subsequent' in d.find_element(By.CSS_SELECTOR,'.stv-status').text)
    assert len(browser.find_elements(By.CSS_SELECTOR,'.stv-nodes > .stv-node'))==2
    assert browser.find_element(By.CSS_SELECTOR,'.stv-view').get_attribute('data-stv-revision')=='1'
    assert browser.switch_to.active_element.get_attribute('aria-expanded')=='true'
    control=browser.find_element(By.CSS_SELECTOR,'[aria-label="Collapse To (outgoing) for A"]')
    browser.execute_script('''arguments[0].focus();arguments[0].click();const outside=document.createElement('button');outside.id='outside-view';outside.textContent='Outside view';document.body.append(outside);outside.focus();''',control)
    wait.until(lambda d:d.execute_script('return calls.length')==6)
    assert browser.execute_script('return calls[5].args[3].previous===calls[4].args[3].previous'), 'Failure must retain the last committed geometry snapshot'
    browser.execute_script('stvHarness.compute(...calls[5].args).then(calls[5].resolve)')
    wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'[data-stv-revision="2"]'))
    assert browser.switch_to.active_element.get_attribute('id')=='outside-view'


@pytest.mark.browser
@pytest.mark.requirements('STV_SYS_004','STV_SYS_005','STV_SYS_006','STV_SYS_010','STV_SWR_008','STV_SWR_012','STV_SWR_015','STV_SWR_029','STV_SWR_031','STV_SWR_033','STV_SWR_037','STV_SWR_041','STV_SWR_047','STV_SWR_048','STV_SWR_049','STV_SWR_050')
@pytest.mark.parametrize('protocol',['file','http'])
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


@pytest.mark.browser
@pytest.mark.requirements('STV_SYS_004','STV_SWR_027','STV_SWR_028','STV_SWR_029')
@pytest.mark.parametrize('protocol',['file','http'])
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


@pytest.mark.browser
def test_documentation_visuals(browser):
    published=Path(__file__).parents[2]/'docs/_build/html'
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


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_055')
@pytest.mark.parametrize('protocol',['file','http'])
def test_control_order_smoke(browser,protocol):
    published=Path(__file__).parents[2]/'docs/_build/html'
    with published_url(published,protocol) as url:
        browser.get(url.rsplit('/',1)[0]+'/demo.html')
        _exercise_control_order(browser)


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
