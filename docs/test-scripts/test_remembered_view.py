"""CR019 real browser persistence, isolation, recovery and storage failure paths."""
import json
import os
from pathlib import Path
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser, short_output, published_url
from test_build import build
from test_persistent_details import prepare_source, open_box, panel_ids, toolbar, change_seed
from test_extended_controls import extended_site, ready, mount_controlled, command


def roots(driver):
    WebDriverWait(driver,30).until(lambda d: len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision]'))==2)
    WebDriverWait(driver,30).until(lambda d: all(not e.get_attribute('disabled') for e in d.find_elements(By.CSS_SELECTOR,'.stv-remember input')))
    return driver.find_elements(By.CSS_SELECTOR,'.stv-view')


def capture(driver,root):
    return driver.execute_script("""return {
      nodes:[...arguments[0].querySelectorAll('.stv-node')].map(n=>[n.dataset.key,n.style.left,n.style.top]),
      cards:[...arguments[0].querySelectorAll('.stv-persistent-detail')].map(n=>n.dataset.needId),
      transform:arguments[0].querySelector('.stv-scene').style.transform,
      enabled:arguments[0].querySelector('.stv-remember input').checked};""",root)


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_003','STV_SWR_063','STV_SWR_073','STV_SWR_074','STV_SWR_075')
@pytest.mark.parametrize('protocol',['file','http'])
def test_remembered_view_roundtrip_disable_isolation_and_card_order(browser,short_output,protocol):
    source=short_output/'source';prepare_source(source,3);out=short_output/'html';result=build(source,out);assert result.returncode==0,result.stdout+result.stderr
    with published_url(out,protocol) as url:
        browser.get(url);root,other=roots(browser)
        assert not root.find_element(By.CSS_SELECTOR,'.stv-remember input').is_selected()
        for id in ['BOX_00','BOX_01','BOX_02']:open_box(browser,root,id)
        change_seed(browser,root,'BOX_00')
        # Cards survive being outside the displayed graph; restore them independently.
        toolbar(browser,root,'Pan right');toolbar(browser,root,'Zoom in')
        checkbox=root.find_element(By.CSS_SELECTOR,'.stv-remember input');browser.execute_script('arguments[0].focus()',checkbox);checkbox.send_keys(Keys.SPACE)
        assert checkbox.is_selected()
        before=capture(browser,root);assert before['cards']==['BOX_00','BOX_01','BOX_02']
        # Later changes must update the snapshot, including expansion and transform.
        revision=int(root.get_attribute('data-stv-revision'))
        browser.execute_script("arguments[0].querySelector('.stv-groups button').click()",root)
        WebDriverWait(browser,20).until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1)
        toolbar(browser,root,'Pan down');before=capture(browser,root)
        other_before=capture(browser,other)
        browser.refresh();root,other=roots(browser)
        assert capture(browser,root)==before
        assert capture(browser,other)==other_before
        assert browser.execute_script('return document.activeElement===document.body')
        # Restoration must retain the stable-navigation contract on the next toggle.
        anchor=browser.execute_script("const n=[...arguments[0].querySelectorAll('.stv-node')].find(n=>JSON.parse(n.dataset.key)[1]==='BOX_00');return [n.style.left,n.style.top]",root)
        revision=int(root.get_attribute('data-stv-revision'));browser.execute_script("arguments[0].querySelector('.stv-groups button').click()",root)
        WebDriverWait(browser,20).until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1)
        assert browser.execute_script("const n=[...arguments[0].querySelectorAll('.stv-node')].find(n=>JSON.parse(n.dataset.key)[1]==='BOX_00');return [n.style.left,n.style.top]",root)==anchor
        assert capture(browser,root)['transform']==before['transform']
        # Expand again so the FIFO exercise can open another visible object.
        revision+=1;browser.execute_script("arguments[0].querySelector('.stv-groups button').click()",root)
        WebDriverWait(browser,20).until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1)
        open_box(browser,root,'BOX_03');assert panel_ids(browser,root)==['BOX_01','BOX_02','BOX_03']
        toolbar(browser,root,'Close all details');assert panel_ids(browser,root)==[]
        browser.refresh();root,other=roots(browser);assert panel_ids(browser,root)==[]
        live=capture(browser,root);root.find_element(By.CSS_SELECTOR,'.stv-remember input').send_keys(Keys.SPACE)
        after=capture(browser,root);assert after=={**live,'enabled':False}
        browser.refresh();root,_=roots(browser);assert not capture(browser,root)['enabled'];assert len(capture(browser,root)['nodes'])==12
        if os.environ.get('STV_REMEMBER_RECORD'):
            browser.save_screenshot(str(Path(os.environ['STV_REMEMBER_RECORD'])/(protocol+'.png')))


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_073','STV_SWR_074','STV_SWR_075')
def test_remembered_view_stale_corrupt_and_reduced_capacity(browser,short_output):
    source=short_output/'source';prepare_source(source,3);out=short_output/'html';result=build(source,out);assert result.returncode==0,result.stdout+result.stderr
    with published_url(out,'http') as url:
        browser.get(url);root,_=roots(browser)
        for id in ['BOX_00','BOX_01','BOX_02']:open_box(browser,root,id)
        root.find_element(By.CSS_SELECTOR,'.stv-remember input').click()
        key=browser.execute_script("return Object.keys(localStorage).find(k=>k.startsWith('stv:view:1:'))")
        data=json.loads(browser.execute_script('return localStorage.getItem(arguments[0])',key));data['cards']=['MISSING','BOX_01','BOX_02'];data['state']['seeds']=['BOX_00','MISSING'];data['state']['expanded']=['["MISSING","traces","outgoing"]']
        browser.execute_script('localStorage.setItem(arguments[0],arguments[1])',key,json.dumps(data));browser.refresh();root,_=roots(browser)
        assert [json.loads(n[0])[1] for n in capture(browser,root)['nodes']]==['BOX_00'];assert panel_ids(browser,root)==['BOX_01','BOX_02']
        browser.execute_script('localStorage.setItem(arguments[0],"{broken")',key);browser.refresh();root,_=roots(browser)
        assert len(capture(browser,root)['nodes'])==12;assert not capture(browser,root)['enabled'];assert 'unavailable' in root.find_element(By.CSS_SELECTOR,'.stv-memory-status').text


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_073','STV_SWR_075')
def test_remembered_view_storage_failure_and_pending_layout(browser,extended_site):
    with published_url(extended_site,'http') as url:
        browser.get(url);ready(browser);root=mount_controlled(browser)
        browser.execute_script("window.nativeSet=Storage.prototype.setItem;Storage.prototype.setItem=function(){throw Error('Injected quota')}")
        root.find_element(By.CSS_SELECTOR,'.stv-remember input').click()
        assert 'Injected quota' in root.find_element(By.CSS_SELECTOR,'.stv-memory-status').text
        command(browser,root,'Pan down');assert 'Injected quota' in root.find_element(By.CSS_SELECTOR,'.stv-memory-status').text
        browser.execute_script('Storage.prototype.setItem=window.nativeSet');command(browser,root,'Pan down')
        assert not root.find_element(By.CSS_SELECTOR,'.stv-memory-status').text
        before=browser.execute_script("return Object.keys(localStorage).filter(k=>k.includes('extended-controlled')).map(k=>[k,localStorage.getItem(k)])")
        browser.execute_script("window.extendedMode='delay';arguments[0].querySelector('.stv-groups button').click()",root)
        WebDriverWait(browser,20).until(lambda d:d.execute_script('return extendedPending.length')==1)
        assert browser.execute_script("return Object.keys(localStorage).filter(k=>k.includes('extended-controlled')).map(k=>[k,localStorage.getItem(k)])")==before
        browser.execute_script("window.extendedMode='normal'");command(browser,root,'Collapse all nodes')
        WebDriverWait(browser,20).until(lambda d:root.get_attribute('aria-busy')=='false')
        committed=browser.execute_script("return Object.keys(localStorage).filter(k=>k.includes('extended-controlled')).map(k=>[k,localStorage.getItem(k)])")
        browser.execute_async_script('const done=arguments[0];extendedPending.shift().resolve();setTimeout(done,100)')
        assert browser.execute_script("return Object.keys(localStorage).filter(k=>k.includes('extended-controlled')).map(k=>[k,localStorage.getItem(k)])")==committed
        # Property getter can fail before mount, without breaking fresh exploration.
        browser.execute_script("Object.defineProperty(window,'localStorage',{get(){throw Error('Injected blocked storage')},configurable:true})")
        # Reuse a new controlled root after removing the old test instance.
        browser.execute_script('arguments[0].remove()',root);root=mount_controlled(browser)
        assert 'Injected blocked storage' in root.find_element(By.CSS_SELECTOR,'.stv-memory-status').text
        assert len(root.find_elements(By.CSS_SELECTOR,'.stv-node'))==2

@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_073','STV_SWR_074','STV_SWR_075')
def test_remembered_overview_pages_and_last_save_wins_between_tabs(browser,short_output):
    source=short_output/'source';prepare_source(source,3);out=short_output/'html';result=build(source,out);assert result.returncode==0,result.stdout+result.stderr
    with published_url(out,'http') as url:
        browser.get(url);root,_=roots(browser);toolbar(browser,root,'Project overview')
        WebDriverWait(browser,20).until(lambda d:root.get_attribute('aria-busy')=='false')
        revision=int(root.get_attribute('data-stv-revision'))
        browser.execute_script("arguments[0].querySelector('[data-focus=Next]').click()",root)
        WebDriverWait(browser,20).until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1)
        root.find_element(By.CSS_SELECTOR,'.stv-remember input').click();toolbar(browser,root,'Pan down');expected=capture(browser,root)
        browser.refresh();root,_=roots(browser);assert capture(browser,root)==expected
        first=browser.current_window_handle;browser.switch_to.new_window('tab');browser.get(url);other,_=roots(browser);assert capture(browser,other)==expected
        toolbar(browser,other,'Zoom in');last=capture(browser,other)
        browser.switch_to.window(first);root,_=roots(browser);assert capture(browser,root)==expected
        browser.refresh();root,_=roots(browser);assert capture(browser,root)==last
        # A different documentation page with the same graph has its own scope.
        second=out/'another.html';second.write_text((out/'index.html').read_text(),encoding='utf-8')
        browser.get(url.replace('index.html','another.html'));root,_=roots(browser);assert not capture(browser,root)['enabled']
        browser.get(url);root,_=roots(browser);assert capture(browser,root)==last


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_073','STV_SWR_075')
def test_remembered_view_survives_browser_restart(short_output):
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    source=short_output/'source';prepare_source(source,3);out=short_output/'html';result=build(source,out);assert result.returncode==0,result.stdout+result.stderr
    profile=short_output/'profile';profile.mkdir()
    def launch():
        options=webdriver.FirefoxOptions();options.add_argument('-headless');options.add_argument('-profile');options.add_argument(str(profile))
        options.set_preference('network.proxy.type',1);options.set_preference('network.proxy.http','127.0.0.1');options.set_preference('network.proxy.http_port',9);options.set_preference('network.proxy.no_proxies_on','localhost,127.0.0.1')
        driver=webdriver.Firefox(service=Service(os.environ['STV_GECKODRIVER']),options=options);driver.set_window_size(1440,1100);return driver
    with published_url(out,'http') as url:
        driver=launch()
        try:
            driver.get(url);root,_=roots(driver);open_box(driver,root,'BOX_01');root.find_element(By.CSS_SELECTOR,'.stv-remember input').click();toolbar(driver,root,'Zoom out');expected=capture(driver,root)
        finally:driver.quit()
        driver=launch()
        try:
            driver.get(url);root,_=roots(driver);assert capture(driver,root)==expected
        finally:driver.quit()
