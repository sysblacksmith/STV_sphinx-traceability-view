"""CR014: independent persistent docks, configurable FIFO and hover coexistence."""
from pathlib import Path
import json
import os
import shutil
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser,short_output,published_url
from test_build import FIXTURE,build,manifest

IDS=[f'BOX_{i:02}' for i in range(12)]

def prepare_source(source,limit=None):
    shutil.copytree(FIXTURE,source)
    if limit is not None:
        with (source/'conf.py').open('a',encoding='utf-8') as f:f.write(f'\ntraceability_view_details_limit={limit!r}\n')
    (source/'index.rst').write_text('Persistent details\n==================\n\n.. raw:: html\n\n   <style>div.document{width:100%!important}div.body{max-width:none!important}div.bodywrapper{margin-left:0!important}.sphinxsidebar{display:none}</style>\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: '+' '.join(IDS)+'\n\n.. traceability-view:: BOX_00\n',encoding='utf-8')
    text='Requirements\n============\n\n'
    for i,id in enumerate(IDS):
        text+=f'.. shr:: Artifact {id}\n   :id: {id}\n   :status: accepted\n'
        if i==0:text+='   :traces: '+', '.join(IDS[1:])+'\n'
        text+='\n'+''.join('   Long rendered detail paragraph '+str(j)+' for '+id+'. '*20+'\n\n' for j in range(16))
        if i==0:text+='   .. raw:: html\n\n      <label for="probe-field">Probe field</label><input id="probe-field"><a href="requirements.html#probe-field">Fragment link</a>\n\n'
    (source/'requirements.rst').write_text(text,encoding='utf-8')


def panel_ids(driver,root):
    return driver.execute_script("return [...arguments[0].querySelectorAll('.stv-persistent-detail')].map(p=>p.dataset.needId)",root)


def open_box(driver,root,id):
    driver.execute_script("const n=[...arguments[0].querySelectorAll('.stv-node')].find(n=>JSON.parse(n.dataset.key)[1]===arguments[1]);n.querySelector('[data-focus=details]').click()",root,id)


def panel(driver,root,id):
    return driver.execute_script("return [...arguments[0].querySelectorAll('.stv-persistent-detail')].find(p=>p.dataset.needId===arguments[1])",root,id)


def toolbar(driver,root,text):
    driver.execute_script("[...arguments[0].querySelectorAll('.stv-toolbar button')].find(b=>b.textContent===arguments[1]).click()",root,text)


def change_seed(driver,root,id):
    revision=int(root.get_attribute('data-stv-revision'));field=root.find_element(By.CSS_SELECTOR,'.stv-seed-picker input');field.clear();field.send_keys(id)
    driver.execute_script("[...arguments[0].querySelectorAll('.stv-seed-picker button')].find(b=>b.textContent==='Start at Need').click()",root)
    WebDriverWait(driver,20).until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1)


@pytest.mark.requirements('STV_SWR_065')
@pytest.mark.parametrize('limit',[None,1,3])
def test_persistent_limit_is_published_by_real_host(short_output,limit):
    source=short_output/'source';prepare_source(source,limit)
    result=build(source,short_output/'html');assert result.returncode==0,result.stdout+result.stderr
    assert manifest(short_output/'html')['details_limit']==(10 if limit is None else limit)


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_050','STV_SWR_063','STV_SWR_064','STV_SWR_065')
@pytest.mark.parametrize('protocol',['file','http'])
@pytest.mark.parametrize('limit',[None,3])
def test_persistent_stack_fifo_scope_navigation_and_responsive_layout(browser,short_output,protocol,limit):
    source=short_output/'source';prepare_source(source,limit);result=build(source,short_output/'html');assert result.returncode==0,result.stdout+result.stderr
    with published_url(short_output/'html',protocol) as url:
        browser.set_window_size(1600,1200);browser.get(url);wait=WebDriverWait(browser,20)
        wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))==2)
        root,other=browser.find_elements(By.CSS_SELECTOR,'.stv-view')
        world=browser.execute_script("return [...arguments[0].querySelectorAll('.stv-node')].map(n=>[n.dataset.key,n.style.left,n.style.top])",root)
        for id in IDS[:3]:open_box(browser,root,id)
        wait.until(lambda d:'Long rendered' in panel(browser,root,IDS[0]).text)
        first=panel(browser,root,IDS[0]);identity=first.get_attribute('id');open_box(browser,root,IDS[0])
        assert panel(browser,root,IDS[0]).get_attribute('id')==identity
        assert panel_ids(browser,root)==IDS[:3]
        assert browser.execute_script("return document.activeElement.closest('.stv-persistent-detail').dataset.needId")==IDS[0]
        # Hover has its own timer/panel and consumes no persistent slot.
        node=browser.execute_script("return [...arguments[0].querySelectorAll('.stv-node')].find(n=>JSON.parse(n.dataset.key)[1]===arguments[1])",root,IDS[0])
        toolbar(browser,root,'Reset viewport');browser.execute_script('arguments[0].scrollIntoView({block:"center"})',node);ActionChains(browser).move_to_element(node).perform();wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-hover-detail input'))
        assert panel_ids(browser,root)==IDS[:3]
        ids=browser.execute_script("return [...document.querySelectorAll('[id]')].map(n=>n.id)");assert len(ids)==len(set(ids))
        browser.switch_to.active_element.send_keys(Keys.ESCAPE);assert not browser.find_elements(By.CSS_SELECTOR,'.stv-hover-detail')
        assert panel_ids(browser,root)==IDS[:3]
        panel(browser,root,IDS[1]).find_element(By.CSS_SELECTOR,'button').send_keys(Keys.ENTER)
        open_box(browser,root,IDS[3]);assert panel_ids(browser,root)==[IDS[0],IDS[2],IDS[3]]
        for id in IDS[4:]:open_box(browser,root,id)
        expected=IDS[2:] if limit is None else IDS[9:]
        assert panel_ids(browser,root)==expected
        panel(browser,root,expected[0]).find_element(By.CSS_SELECTOR,'button').click()
        # Manual close frees one slot; reopening appends without evicting.
        open_box(browser,root,expected[0]);expected=expected[1:]+expected[:1];assert panel_ids(browser,root)==expected
        browser.execute_script('arguments[0].focus()',panel(browser,root,expected[0]));open_box(browser,root,IDS[1]);expected=expected[1:]+[IDS[1]]
        assert panel_ids(browser,root)==expected
        assert browser.execute_script("return [...arguments[0].querySelectorAll('.stv-node')].map(n=>[n.dataset.key,n.style.left,n.style.top])",root)==world
        assert browser.execute_script("const r=arguments[0].getBoundingClientRect(),b=arguments[0].querySelector('.stv-close-all').getBoundingClientRect();return r.right-b.right<20&&b.right<=r.right",root)
        assert browser.execute_script("const v=arguments[0].querySelector('.stv-viewport').getBoundingClientRect(),s=arguments[0].querySelector('.stv-details-stack').getBoundingClientRect();return s.left>=v.right-1",root)
        assert browser.execute_script("const s=arguments[0].querySelector('.stv-details-stack');return s.scrollHeight>s.clientHeight",root)
        if os.environ.get('STV_PERSISTENT_RECORD'):
            out=Path(os.environ['STV_PERSISTENT_RECORD']);out.mkdir(parents=True,exist_ok=True)
            browser.execute_script('arguments[0].scrollIntoView({block:"start"})',root)
            browser.save_screenshot(str(out/f'{limit}-{protocol}-wide.png'))
        for label in ['Pan down','Zoom in','Reset viewport']:toolbar(browser,root,label);assert panel_ids(browser,root)==expected
        change_seed(browser,root,IDS[0]);assert panel_ids(browser,root)==expected
        for _ in range(2):
            revision=int(root.get_attribute('data-stv-revision'))
            browser.execute_script("arguments[0].querySelector('.stv-groups button').click()",root)
            wait.until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1)
            assert panel_ids(browser,root)==expected
        toolbar(browser,root,'Reset viewport')
        assert browser.execute_script("const v=arguments[0].querySelector('.stv-viewport').getBoundingClientRect(),n=arguments[0].querySelector('.stv-node').getBoundingClientRect();return n.left>=v.left&&n.right<=v.right&&n.top>=v.top&&n.bottom<=v.bottom",root)
        revision=int(root.get_attribute('data-stv-revision'));toolbar(browser,root,'Project overview');wait.until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1)
        revision+=1;browser.execute_script("arguments[0].querySelector('[data-focus=Next]').click()",root);wait.until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1);assert panel_ids(browser,root)==expected
        # All boxes survive paging; BOX_11 is absent so its Close uses the toolbar fallback.
        missing=IDS[11]
        if missing in expected:
            panel(browser,root,missing).find_element(By.CSS_SELECTOR,'button').click();expected.remove(missing)
            assert browser.execute_script("return document.activeElement.classList.contains('stv-close-all')")
        open_box(browser,other,IDS[0]);assert len(panel_ids(browser,other))==1 and panel_ids(browser,root)==expected
        toolbar(browser,root,'Close all details');assert panel_ids(browser,root)==[] and panel_ids(browser,other)==[IDS[0]]
        change_seed(browser,root,IDS[0]);open_box(browser,root,IDS[0]);browser.set_window_size(650,1100);open_box(browser,root,IDS[0])
        assert browser.execute_script("const v=arguments[0].querySelector('.stv-viewport').getBoundingClientRect(),s=arguments[0].querySelector('.stv-details-stack').getBoundingClientRect();return s.top>=v.bottom-1",root)
        p=panel(browser,root,IDS[0]);wait.until(lambda d:'Long rendered' in p.text);assert browser.execute_script('return arguments[0].scrollHeight>arguments[0].clientHeight',p)
        browser.execute_script('arguments[0].focus()',p);p.send_keys(Keys.END);wait.until(lambda d:browser.execute_script('return arguments[0].scrollTop>0',p))
        target=os.environ.get('STV_PERSISTENT_RECORD')
        if target:
            browser.execute_script('arguments[0].scrollTop=0;arguments[0].scrollIntoView({block:"start"})',p)
            out=Path(target);out.mkdir(parents=True,exist_ok=True);browser.save_screenshot(str(out/(f'{limit}-{protocol}.png')))
            (out/(f'{limit}-{protocol}.json')).write_text(json.dumps(dict(limit=10 if limit is None else limit,order_before_clear=expected,browser=browser.capabilities['browserVersion']),indent=2),encoding='utf-8')
        browser.execute_script("window.dispatchEvent(new PageTransitionEvent('pagehide',{persisted:true}))")
        assert panel_ids(browser,root)==panel_ids(browser,other)==[]


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_063','STV_SWR_064')
@pytest.mark.parametrize('protocol',['file','http'])
def test_persistent_completion_identity_eviction_and_retry(browser,short_output,protocol):
    import subprocess
    project=Path(__file__).parents[2]
    command="import{build}from'esbuild';await build({entryPoints:[process.argv[1]],bundle:true,format:'iife',outfile:process.argv[2]})"
    result=subprocess.run(['node','--input-type=module','-e',command,str(project/'docs/test-scripts/fixtures/persistent-harness.js'),str(short_output/'harness.js')],cwd=project/'frontend',capture_output=True,text=True)
    assert result.returncode==0,result.stderr
    shutil.copyfile(project/'src/sphinx_traceability_view/static/stv.css',short_output/'stv.css')
    (short_output/'index.html').write_text('<link rel="stylesheet" href="stv.css"><div class="stv-view" id="race-view"><div class="stv-toolbar"><button class="stv-close-all">Close all details</button></div><div class="stv-workspace"><div class="stv-viewport"><button id="trigger-A">Details A</button><button id="trigger-B">Details B</button></div><section class="stv-details-stack"></section></div></div><button id="outside">Outside</button><script src="harness.js"></script>',encoding='utf-8')
    with published_url(short_output,protocol) as url:
        browser.get(url);wait=WebDriverWait(browser,15)
        wait.until(lambda d:d.execute_script('return !!globalThis.persistentHarness'))
        def click(id):browser.execute_script('document.getElementById(arguments[0]).click()',id)
        def count(n):wait.until(lambda d:d.execute_script('return persistentHarness.calls.length')==n)
        def text():return browser.find_element(By.CSS_SELECTOR,'.stv-persistent-detail').text
        click('trigger-A');count(1);old=browser.find_element(By.CSS_SELECTOR,'.stv-persistent-detail').get_attribute('id')
        browser.execute_script('persistentHarness.manager.close("A")');click('trigger-A');count(2)
        assert browser.find_element(By.CSS_SELECTOR,'.stv-persistent-detail').get_attribute('id')!=old
        browser.execute_script('persistentHarness.calls[0].resolve("<p>STALE OLD A</p>")')
        assert 'STALE' not in text()
        browser.execute_script('persistentHarness.calls[1].resolve(arguments[0])', '<label for="field">New A</label><input id="field"><p>READY NEW A</p>')
        wait.until(lambda d:'READY NEW A' in text())
        p=browser.find_element(By.CSS_SELECTOR,'.stv-persistent-detail');assert p.find_element(By.CSS_SELECTOR,'label').get_attribute('for')==p.find_element(By.CSS_SELECTOR,'input').get_attribute('id')
        browser.execute_script('persistentHarness.manager.close("A")');assert browser.switch_to.active_element.get_attribute('id')=='trigger-A'
        click('trigger-A');count(3);click('trigger-B');count(4)
        browser.execute_script('persistentHarness.calls[2].resolve("<p>EVICTED A</p>")')
        assert browser.find_element(By.CSS_SELECTOR,'.stv-persistent-detail').get_attribute('data-need-id')=='B' and 'EVICTED' not in text()
        browser.execute_script('persistentHarness.calls[3].reject(Error("Controlled failure"))');wait.until(lambda d:'Controlled failure' in text())
        browser.find_element(By.CSS_SELECTOR,'.stv-persistent-detail button').click();click('trigger-B');count(5)
        browser.execute_script('persistentHarness.calls[4].resolve("<p>RETRY READY B</p>")');wait.until(lambda d:'RETRY READY B' in text())
        click('trigger-A');count(6);browser.execute_script('persistentHarness.manager.clear();persistentHarness.calls[5].resolve("<p>AFTER CLEAR</p>")')
        assert not browser.find_elements(By.CSS_SELECTOR,'.stv-persistent-detail')
        click('trigger-A');count(7);browser.execute_script('document.getElementById("outside").focus();persistentHarness.calls[6].resolve("<p>NO FOCUS THEFT</p>")')
        wait.until(lambda d:'NO FOCUS THEFT' in text());assert browser.switch_to.active_element.get_attribute('id')=='outside'
        click('trigger-A');assert browser.execute_script('return persistentHarness.calls.length')==7
        assert browser.execute_script("return document.activeElement.hasAttribute('data-persistent-close')")




@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_016','STV_SWR_018','STV_SWR_064')
@pytest.mark.parametrize('protocol',['file','http'])
def test_detail_metadata_controls_width_and_artifact_navigation(browser,short_output,protocol):
    source=short_output/'source';prepare_source(source)
    needs=source/'requirements.rst';needs.write_text(needs.read_text().replace(':status: accepted',':status: accepted\n   :tags: acceptance'),encoding='utf-8')
    result=build(source,short_output/'html');assert result.returncode==0,result.stdout+result.stderr
    with published_url(short_output/'html',protocol) as url:
        browser.set_window_size(2200,1200);browser.get(url);wait=WebDriverWait(browser,20)
        root=wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
        open_box(browser,root,IDS[0]);p=wait.until(lambda d:panel(d,root,IDS[0]))
        wait.until(lambda d:p.find_elements(By.CSS_SELECTOR,'table.need .needs_collapse'))
        row=p.find_element(By.CSS_SELECTOR,'tr.meta');toggle=p.find_element(By.CSS_SELECTOR,'.needs_collapse')
        header=p.find_element(By.CSS_SELECTOR,'.needs-id a')
        original=p.find_element(By.CSS_SELECTOR,':scope>a').get_attribute('href')
        observed={'width':browser.execute_script('return arguments[0].querySelector(".stv-details-stack").getBoundingClientRect().width',root),'initially_folded':not row.is_displayed(),'artifact_href':header.get_attribute('href'),'original_href':original}
        browser.execute_script('arguments[0].click()',toggle);observed['opens']=row.is_displayed()
        browser.execute_script('arguments[0].click()',toggle);observed['closes']=not row.is_displayed()
        assert observed['width']==720 and observed['initially_folded'] and observed['opens'] and observed['closes'] and observed['artifact_href']==original,observed
        frame=browser.execute_script("const s=arguments[0].querySelector('.stv-details-stack'),v=arguments[0].querySelector('.stv-viewport'),p=s.querySelector('.stv-persistent-detail'),c=getComputedStyle(s);return {borders:[c.borderTopWidth,c.borderRightWidth,c.borderBottomWidth,c.borderLeftWidth],style:c.borderLeftStyle,color:c.borderLeftColor,top:s.getBoundingClientRect().top-v.getBoundingClientRect().top,height:s.getBoundingClientRect().height-v.getBoundingClientRect().height,inset:p.getBoundingClientRect().top-s.getBoundingClientRect().top,shadow:getComputedStyle(p).boxShadow}",root)
        assert frame['borders']==['1px']*4 and frame['style']=='solid' and frame['color']=='rgb(153, 153, 153)',frame
        assert frame['top']==0 and frame['height']==0 and frame['inset']>=8 and frame['shadow']=='none',frame
        assert toggle.find_element(By.CSS_SELECTOR,'.needs.visible').is_displayed()
        assert not toggle.find_element(By.CSS_SELECTOR,'.needs.collapsed').is_displayed()
        if os.environ.get('STV_METADATA_RECORD'):
            out=Path(os.environ['STV_METADATA_RECORD']);out.mkdir(parents=True,exist_ok=True)
            browser.execute_script('arguments[0].scrollIntoView({block:"start"})',root)
            browser.save_screenshot(str(out/(protocol+'-folded-wide.png')))
        assert toggle.get_attribute('role')=='button' and toggle.get_attribute('aria-expanded')=='false'
        assert row.get_attribute('id') in toggle.get_attribute('aria-controls').split()
        browser.execute_script('arguments[0].focus()',toggle);toggle.send_keys(Keys.SPACE)
        assert row.is_displayed() and toggle.get_attribute('aria-expanded')=='true'
        assert toggle.find_element(By.CSS_SELECTOR,'.needs.collapsed').is_displayed()
        assert not toggle.find_element(By.CSS_SELECTOR,'.needs.visible').is_displayed()
        toggle.send_keys(Keys.ENTER);assert not row.is_displayed()
        browser.execute_script('arguments[0].click()',toggle);open_box(browser,root,IDS[0])
        assert row.is_displayed()
        open_box(browser,root,IDS[1]);q=panel(browser,root,IDS[1]);wait.until(lambda d:q.find_elements(By.CSS_SELECTOR,'tr.meta'))
        assert not q.find_element(By.CSS_SELECTOR,'tr.meta').is_displayed() and row.is_displayed()
        anchor=p.find_element(By.LINK_TEXT,'Fragment link')
        assert anchor.get_attribute('href').endswith('#'+p.find_element(By.CSS_SELECTOR,'input').get_attribute('id'))
        parent=browser.current_window_handle;handles=browser.window_handles
        browser.execute_script('arguments[0].click()',header);wait.until(lambda d:len(d.window_handles)==len(handles)+1)
        browser.switch_to.window(next(h for h in browser.window_handles if h not in handles))
        wait.until(lambda d:d.current_url==original and d.find_elements(By.ID,IDS[0]))
        assert browser.find_element(By.ID,IDS[0]).tag_name=='table'
        browser.close();browser.switch_to.window(parent)
        toolbar(browser,root,'Reset viewport')
        node=browser.execute_script("return [...arguments[0].querySelectorAll('.stv-node')].find(n=>JSON.parse(n.dataset.key)[1]===arguments[1])",root,IDS[0])
        browser.execute_script('arguments[0].scrollIntoView({block:"center"})',node);ActionChains(browser).move_to_element(node).perform()
        hover=wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-hover-detail table.need'))
        assert not hover.find_element(By.CSS_SELECTOR,'tr.meta').is_displayed()
        browser.execute_script('arguments[0].click()',hover.find_element(By.CSS_SELECTOR,'.needs_collapse'))
        assert hover.find_element(By.CSS_SELECTOR,'tr.meta').is_displayed()
        assert not q.find_element(By.CSS_SELECTOR,'tr.meta').is_displayed()
        ids=browser.execute_script("return [...document.querySelectorAll('[id]')].map(n=>n.id)");assert len(ids)==len(set(ids))
        browser.switch_to.active_element.send_keys(Keys.ESCAPE)
        browser.set_window_size(1050,1100)
        assert browser.execute_script("const v=arguments[0].querySelector('.stv-viewport').getBoundingClientRect(),s=arguments[0].querySelector('.stv-details-stack').getBoundingClientRect();return s.top>=v.bottom-1&&s.width<=720",root)
        target=os.environ.get('STV_METADATA_RECORD')
        if target:
            out=Path(target);out.mkdir(parents=True,exist_ok=True)
            browser.execute_script('arguments[0].scrollIntoView({block:"start"})',p)
            browser.save_screenshot(str(out/(protocol+'.png')))
            (out/(protocol+'.json')).write_text(json.dumps(observed,indent=2),encoding='utf-8')
