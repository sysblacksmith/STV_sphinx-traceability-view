"""Extended accepted procedures against real components and Sphinx host markup."""
from pathlib import Path
import base64
from importlib.resources import files
import re
import shutil
import subprocess
import tempfile
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser, published_url
from test_build import FIXTURE, build

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope='module')
def extended_site():
    with tempfile.TemporaryDirectory(prefix='stv-ex-') as temp:
        base=Path(temp); source=base/'source';shutil.copytree(FIXTURE,source)
        static=source/'_static';static.mkdir(exist_ok=True)
        shutil.copyfile(files('sphinx_rtd_theme')/'static/fonts/RobotoSlab/roboto-slab-v7-regular.woff2',static/'extended.woff2')
        (static/'extended.png').write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aWZkAAAAASUVORK5CYII='))
        (static/'extended.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"><rect width="20" height="20" fill="red"/></svg>')
        subprocess.run(['node',str(ROOT/'frontend/node_modules/esbuild/bin/esbuild'),str(ROOT/'docs/test-scripts/fixtures/extended/harness-entry.js'),'--bundle','--platform=browser','--format=iife','--global-name=STVExtended','--outfile='+str(static/'extended.js')],check=True,capture_output=True)
        with (source/'conf.py').open('a',encoding='utf-8') as f:f.write("\nhtml_static_path=['_static']\nhtml_js_files=['extended.js']\n")
        text='Requirements\n============\n\n'
        for i in range(12):
            text+=f'.. shr:: Goal {i}\n   :id: GOAL_{i:02}\n   :status: accepted\n   :traces: CHILD_00, CHILD_01\n\n   Goal body remains visible.\n\n'
            if i==0:text+='   '+('Long detail text for keyboard scrolling. '*500)+'\n\n'
        for i in range(4):
            text+=f'.. swr:: Child {i}\n   :id: CHILD_{i:02}\n   :status: accepted\n   :traces: CHILD_{(i+1)%4:02}\n\n   Child detail text {i}.\n\n'
        text+='.. shr:: Hidden sentinel\n   :id: HIDDEN_GOAL\n   :hide:\n\n'
        (source/'requirements.rst').write_text(text,encoding='utf-8')
        (source/'index.rst').write_text('Extended controls\n=================\n\n.. toctree::\n\n   requirements\n\n.. traceability-view::\n\n.. traceability-view:: GOAL_00 GOAL_01\n',encoding='utf-8')
        output=base/'html';result=build(source,output);assert result.returncode==0,result.stdout+result.stderr
        host=(output/'requirements.html').read_text(encoding='utf-8')
        host=re.sub(r'<script\b[^>]*src="[^"]*/stv\.js[^"]*"[^>]*>\s*</script>','',host)
        assert '/stv.js' not in host
        (output/'host-only.html').write_text(host,encoding='utf-8')
        yield output


def ready(driver):
    wait=WebDriverWait(driver,30)
    wait.until(lambda d:d.execute_script('return !!window.STVExtended && document.readyState==="complete"'))
    return wait


def command(driver,root,label):
    driver.execute_script("[...arguments[0].querySelectorAll('button')].find(b=>b.textContent===arguments[1]).click()",root,label)


def ids(driver,root):
    return driver.execute_script("return [...arguments[0].querySelectorAll('.stv-node')].map(n=>JSON.parse(n.dataset.key)[1])",root)


def mount_controlled(driver,mode='seeded',entries=None,presentation='unchanged'):
    result=driver.execute_async_script("""
      const done=arguments[arguments.length-1],graph=structuredClone(Object.values(__STV_DATA__.graphs)[0]);
      if(arguments[1]!==null)graph.entries=graph.entries.slice(0,arguments[1]);
      if(arguments[2]===null)delete graph.presentation;
      else if(arguments[2]!=='unchanged')graph.presentation=arguments[2];
      const root=document.createElement('div');root.className='stv-view';root.id='extended-controlled';
      root.dataset.stvSeeds=JSON.stringify(arguments[0]==='overview'?[]:['GOAL_00','GOAL_01']);
      document.body.prepend(root);window.extendedPending=[];window.extendedMode='normal';
      const layout=(...args)=>{
        const work=STVExtended.compute(...args);
        if(window.extendedMode==='reject')return Promise.reject(Error('Injected layout rejection'));
        if(window.extendedMode==='delay')return new Promise((resolve,reject)=>window.extendedPending.push({resolve:()=>work.then(resolve,reject),reject}));
        return work;
      };
      const base=new URL(document.querySelector('script[data-stv-root]').dataset.stvRoot,document.baseURI);
      STVExtended.mount(root,graph,base,layout).then(()=>done(true),e=>done(String(e)));
    """,mode,entries,presentation)
    assert result is True,result
    return driver.find_element(By.ID,'extended-controlled')


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_066')
@pytest.mark.parametrize('protocol',['file','http'])
def test_reset_stale_layout_failure_retry_and_independent_views(browser,extended_site,protocol):
    with published_url(extended_site,protocol) as url:
        browser.get(url);wait=ready(browser)
        wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision]'))==2)
        other=browser.find_elements(By.CSS_SELECTOR,'.stv-view')[1]
        unchanged=(ids(browser,other),other.get_attribute('data-stv-revision'))
        root=mount_controlled(browser);assert set(ids(browser,root))=={'GOAL_00','GOAL_01'}
        browser.execute_script("arguments[0].querySelector('[data-focus=details]').click()",root)
        wait.until(lambda d:root.find_elements(By.CSS_SELECTOR,'.stv-persistent-detail table.need'))
        cards=browser.execute_script("return [...arguments[0].querySelectorAll('.stv-persistent-detail')].map(p=>p.dataset.needId)",root)
        browser.execute_script("window.extendedMode='delay';arguments[0].querySelector('.stv-groups button[aria-expanded=false]').click()",root)
        wait.until(lambda d:d.execute_script('return window.extendedPending.length')==1)
        browser.execute_script("window.extendedMode='normal'");command(browser,root,'Collapse all nodes')
        wait.until(lambda d:root.get_attribute('aria-busy')=='false');revision=root.get_attribute('data-stv-revision')
        browser.execute_async_script('const done=arguments[0];window.extendedPending.shift().resolve();setTimeout(done,100)')
        assert root.get_attribute('data-stv-revision')==revision and set(ids(browser,root))=={'GOAL_00','GOAL_01'}
        browser.execute_script("arguments[0].querySelector('.stv-groups button[aria-expanded=false]').click()",root)
        wait.until(lambda d:len(ids(d,root))>2)
        expanded=set(ids(browser,root));revision=root.get_attribute('data-stv-revision')
        browser.execute_script("window.extendedMode='reject'");command(browser,root,'Collapse all nodes')
        wait.until(lambda d:'Injected layout rejection' in root.text)
        assert set(ids(browser,root))==expanded and root.get_attribute('data-stv-revision')==revision
        command(browser,root,'Save as SVG');assert 'Wait for layout' in root.text
        browser.execute_script("window.extendedMode='normal'");command(browser,root,'Retry layout')
        wait.until(lambda d:root.get_attribute('aria-busy')=='false' and set(ids(d,root))=={'GOAL_00','GOAL_01'})
        for _ in range(2):
            button=root.find_element(By.XPATH,".//button[.='Collapse all nodes']");button.send_keys(Keys.SPACE)
            wait.until(lambda d:root.get_attribute('aria-busy')=='false');assert browser.switch_to.active_element==button
        assert browser.execute_script("return [...arguments[0].querySelectorAll('.stv-persistent-detail')].map(p=>p.dataset.needId)",root)==cards
        assert (ids(browser,other),other.get_attribute('data-stv-revision'))==unchanged


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_066')
@pytest.mark.parametrize('count',[0,3,12])
def test_reset_overview_boundaries_and_page_restoration_cache(browser,extended_site,count):
    browser.get((extended_site/'index.html').as_uri());wait=ready(browser);root=mount_controlled(browser,'overview',count)
    assert len(ids(browser,root))==1+min(count,5)
    if count>5:
        command(browser,root,'Next');wait.until(lambda d:'Page 2' in root.text)
        browser.execute_script("arguments[0].querySelector('.stv-groups button[aria-expanded=false]').click()",root)
        wait.until(lambda d:root.get_attribute('aria-busy')=='false')
    command(browser,root,'Collapse all nodes');wait.until(lambda d:root.get_attribute('aria-busy')=='false')
    assert len(ids(browser,root))==1+min(count,5)
    assert not root.find_elements(By.CSS_SELECTOR,'.stv-groups button[aria-expanded=true]')
    if count>5:
        assert 'Page 1' in root.text
        command(browser,root,'Next');wait.until(lambda d:'Page 2' in root.text)
        assert not root.find_elements(By.CSS_SELECTOR,'.stv-groups button[aria-expanded=true]')


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_066')
@pytest.mark.parametrize('protocol',['file','http'])
def test_reset_uses_interactive_seed_and_retains_hidden_artifact_card(browser,extended_site,protocol):
    with published_url(extended_site,protocol) as url:
        browser.get(url);wait=ready(browser);root=mount_controlled(browser)
        browser.execute_script("arguments[0].querySelector('[data-focus=details]').click()",root)
        wait.until(lambda d:root.find_elements(By.CSS_SELECTOR,'.stv-persistent-detail table.need'))
        cards=browser.execute_script("return [...arguments[0].querySelectorAll('.stv-persistent-detail')].map(n=>n.dataset.needId)",root)
        field=root.find_element(By.CSS_SELECTOR,'.stv-seed-picker input');field.send_keys('CHILD_02');field.send_keys(Keys.ENTER)
        wait.until(lambda d:ids(d,root)==['CHILD_02'])
        browser.execute_script("arguments[0].querySelector('.stv-groups button[aria-label^=Expand]').click()",root)
        wait.until(lambda d:len(ids(d,root))>1)
        button=root.find_element(By.XPATH,".//button[.='Collapse all nodes']");button.send_keys(Keys.ENTER)
        wait.until(lambda d:ids(d,root)==['CHILD_02'] and root.get_attribute('aria-busy')=='false')
        assert browser.switch_to.active_element==button
        assert browser.execute_script("return [...arguments[0].querySelectorAll('.stv-persistent-detail')].map(n=>n.dataset.needId)",root)==cards
        assert not root.find_elements(By.CSS_SELECTOR,'.stv-groups button[aria-expanded=true]')


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_067','STV_SWR_068')
def test_typography_nested_units_late_children_and_repeat_scaling(browser,extended_site):
    browser.get((extended_site/'index.html').as_uri());ready(browser)
    value=browser.execute_script("""
      const panel=document.createElement('article');panel.style.fontSize='20px';
      panel.innerHTML='<span style="font-size:1.5em">em</span><code style="font-size:1.25rem">rem</code><h3 style="font-size:24px">heading</h3>';
      document.body.prepend(panel);const sizes=()=>[panel,...panel.children].map(e=>parseFloat(getComputedStyle(e).fontSize));
      const before=sizes();STVExtended.scaleTypography(panel,.7);const first=sizes();STVExtended.scaleTypography(panel,.7);const repeated=sizes();
      const child=document.createElement('b');child.style.fontSize='2em';child.textContent='late';panel.append(child);STVExtended.scaleTypography(panel,.7);
      const late=parseFloat(getComputedStyle(child).fontSize);STVExtended.scaleTypography(panel,1);return {before,first,repeated,late,restored:sizes().slice(0,4)};
    """)
    assert value['first']==value['repeated']
    assert all(abs(a*.7-b)<.5 for a,b in zip(value['before'],value['first']))
    assert abs(value['late']-28)<.5
    assert all(abs(a-b)<.5 for a,b in zip(value['before'],value['restored']))


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_067','STV_SWR_068')
@pytest.mark.parametrize('protocol',['file','http'])
def test_font_defaults_legacy_fallback_reuse_resize_and_host_isolation(browser,extended_site,protocol):
    measurements=[]
    with published_url(extended_site,protocol) as url:
        for presentation in [None,{'tooltip_font_scale':.7,'details_font_scale':.7},{'tooltip_font_scale':.8,'details_font_scale':.6}]:
            browser.get(url);wait=ready(browser);root=mount_controlled(browser,presentation=presentation)
            node=root.find_element(By.CSS_SELECTOR,'.stv-node');summary=node.find_element(By.CSS_SELECTOR,'.stv-title')
            original=browser.execute_script('return [getComputedStyle(document.body).fontSize,getComputedStyle(arguments[0]).fontSize]',summary)
            trigger=node.find_element(By.CSS_SELECTOR,'[data-focus=details]');browser.execute_script('arguments[0].click()',trigger)
            card=wait.until(lambda d:root.find_element(By.CSS_SELECTOR,'.stv-persistent-detail .need p'))
            size=browser.execute_script('return parseFloat(getComputedStyle(arguments[0]).fontSize)',card)
            browser.execute_script('arguments[0].click()',trigger)
            assert browser.execute_script('return parseFloat(getComputedStyle(arguments[0]).fontSize)',card)==size
            root.find_element(By.CSS_SELECTOR,'[data-persistent-close]').click();browser.execute_script('arguments[0].click()',trigger)
            card=wait.until(lambda d:root.find_element(By.CSS_SELECTOR,'.stv-persistent-detail .need p'))
            assert browser.execute_script('return parseFloat(getComputedStyle(arguments[0]).fontSize)',card)==size
            panel=root.find_element(By.CSS_SELECTOR,'.stv-persistent-detail')
            browser.execute_script('arguments[0].scrollTop=0;arguments[0].focus()',panel);panel.send_keys(Keys.PAGE_DOWN)
            wait.until(lambda d:d.execute_script('return arguments[0].scrollTop>0',panel))
            browser.set_window_size(950,800)
            assert browser.execute_script('return parseFloat(getComputedStyle(arguments[0]).fontSize)',card)==size
            assert browser.execute_script('return [getComputedStyle(document.body).fontSize,getComputedStyle(arguments[0]).fontSize]',summary)==original
            browser.set_window_size(1600,1100)
            root.find_element(By.CSS_SELECTOR,'[data-persistent-close]').click()
            command(browser,root,'Reset viewport')
            ActionChains(browser).move_to_element(root.find_element(By.CSS_SELECTOR,'.stv-toolbar button')).perform()
            ActionChains(browser).move_to_element(trigger).perform()
            hover=wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-hover-detail .need p'))
            hover_size=browser.execute_script('return parseFloat(getComputedStyle(arguments[0]).fontSize)',hover)
            measurements.append((size,hover_size))
    for index,(card_scale,hover_scale) in enumerate([(.7,.7),(.6,.8)],1):
        assert measurements[index][0]==pytest.approx(measurements[0][0]*card_scale,abs=.5)
        assert measurements[index][1]==pytest.approx(measurements[0][1]*hover_scale,abs=.5)


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_071')
def test_download_expiry_pagehide_and_error_ownership(browser,extended_site):
    browser.get((extended_site/'index.html').as_uri());ready(browser)
    value=browser.execute_script("""
      STVExtended.releaseDownloads();const saved={create:URL.createObjectURL,revoke:URL.revokeObjectURL,set:window.setTimeout,clear:window.clearTimeout,click:HTMLAnchorElement.prototype.click};
      const timers=new Map(),revoked=[],clicked=[];let next=0,fail=false,mime;
      try{
        URL.createObjectURL=blob=>{mime=blob.type;return 'blob:extended-'+(++next)};URL.revokeObjectURL=url=>revoked.push(url);
        window.setTimeout=(fn,ms)=>{timers.set(next,{fn,ms});return next};window.clearTimeout=id=>timers.delete(id);
        HTMLAnchorElement.prototype.click=function(){if(fail)throw Error('blocked');clicked.push({connected:this.isConnected,name:this.download})};
        STVExtended.saveSVG('<svg/>','<unsafe/name>');const early=revoked.length,delay=timers.get(1).ms;timers.get(1).fn();
        STVExtended.saveSVG('<svg/>','second');window.dispatchEvent(new Event('pagehide'));const afterPagehide=revoked.slice();fail=true;
        let error=false;try{STVExtended.saveSVG('<svg/>','error')}catch{error=true}
        return {mime,early,delay,afterPagehide,revoked,error,clicked,anchors:document.querySelectorAll('a[download]').length};
      }finally{URL.createObjectURL=saved.create;URL.revokeObjectURL=saved.revoke;window.setTimeout=saved.set;window.clearTimeout=saved.clear;HTMLAnchorElement.prototype.click=saved.click;STVExtended.releaseDownloads()}
    """)
    assert value['early']==0 and value['delay']>=60000
    assert value['afterPagehide']==['blob:extended-1','blob:extended-2']
    assert value['revoked']==['blob:extended-1','blob:extended-2','blob:extended-3']
    assert value['error'] and value['anchors']==0
    assert all(i['connected'] and re.fullmatch(r'stv-[a-zA-Z0-9_-]+\.svg',i['name']) for i in value['clicked'])
    assert value['mime']=='image/svg+xml;charset=utf-8'


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_070','STV_SWR_072')
def test_snapshot_clipping_immutable_text_resources_and_readiness(browser,extended_site,tmp_path):
    browser.get((extended_site/'index.html').as_uri());ready(browser)
    browser.execute_async_script('const done=arguments[0];document.fonts.ready.then(()=>done(true))')
    value=browser.execute_script("""
      const box=document.createElement('section');box.style.cssText='position:fixed;left:-20px;top:30px;width:300px;height:180px;overflow:hidden;background:white;z-index:10000';
      box.innerHTML='<style>.extended-pseudo::before{content:"PRE"}</style><div style="height:80px;overflow:auto"><div style="height:400px"><span class="extended-pseudo">Über &amp; &lt;script&gt; SAFE</span></div></div><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30"><defs><marker id="extended-arrow"><path d="M0 0L5 5"/></marker></defs><path marker-end="url(#extended-arrow)" d="M0 0L20 20"/></svg>';
      document.body.append(box);box.firstElementChild.nextElementSibling.scrollTop=10;
      const resources={assets:{},fonts:[]},base=new URL('./',document.baseURI),before=box.outerHTML;
      const rect=box.querySelector('span').getBoundingClientRect(),coordinates={x:rect.x,y:rect.y-30};
      const snapshot=STVExtended.capture(box,{base,resources}),text=STVExtended.serialize(snapshot);
      const unchanged=box.outerHTML===before;box.querySelector('span').textContent='LATER_REVISION';box.style.left='500px';
      const stable=STVExtended.serialize(snapshot)===text,xml=new DOMParser().parseFromString(text,'image/svg+xml');
      box.style.left='-10000px';let empty=false;try{STVExtended.capture(box,{base,resources})}catch(e){empty=e.message.includes('No visible')}
      box.style.left='0px';box.style.fontFamily='MissingFixture';let fontFailure=false;
      try{STVExtended.capture(box,{base,resources:{assets:{},fonts:[{family:'MissingFixture',error:'missing'}]}})}catch(e){fontFailure=e.message.includes('font')}
      const image=document.createElement('img');image.style.cssText='position:absolute;top:0;left:0;width:20px;height:20px';image.src=new URL('missing.png',base);box.append(image);let missing=false;
      try{STVExtended.capture(box,{base,resources})}catch(e){missing=e.message.includes('image is unavailable')}
      image.remove();const recovered=!!STVExtended.serialize(STVExtended.capture(box,{base,resources}));box.remove();
      return {unchanged,stable,empty,fontFailure,missing,recovered,text,coordinates,width:xml.documentElement.getAttribute('width'),height:xml.documentElement.getAttribute('height'),parserError:!!xml.querySelector('parsererror')};
    """)
    assert all(value[k] for k in ['unchanged','stable','empty','fontFailure','missing','recovered']), {k:v for k,v in value.items() if k!='text'}
    assert not value['parserError']
    assert abs(float(value['width'])-280)<1 and abs(float(value['height'])-180)<1
    assert 'Über' in value['text'] and '&lt;script&gt;' in value['text'] and 'PRE' in value['text']
    assert 'LATER_REVISION' not in value['text'] and '<script' not in value['text']
    saved=tmp_path/'geometry.svg';saved.write_text(value['text'],encoding='utf-8');browser.get(saved.as_uri())
    actual=browser.execute_script("const r=document.querySelector('.extended-pseudo').getBoundingClientRect();return {x:r.x,y:r.y}")
    assert all(abs(actual[k]-value['coordinates'][k])<=1 for k in ['x','y']), (actual,value['coordinates'])


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_069')
@pytest.mark.parametrize('protocol',['file','http'])
def test_host_bulk_mixed_rows_reinitialization_and_native_toggle(browser,extended_site,protocol):
    with published_url(extended_site,protocol) as url:
        browser.get(url.replace('index.html','host-only.html'));ready(browser)
        assert not browser.find_elements(By.CSS_SELECTOR,'.stv-page-metadata')
        browser.execute_script("""
          const table=document.querySelector('table.need'),row=document.createElement('tr');row.className='need meta';row.innerHTML='<td>Extra attributes</td>';table.querySelector('tbody').append(row);
          table.querySelector('tr.meta').classList.add('collapse_is_hidden');row.classList.remove('collapse_is_hidden');window.extendedNativeClicks=0;
          document.querySelectorAll('.needs_collapse span.needs').forEach(n=>n.addEventListener('click',()=>window.extendedNativeClicks++));
          window.extendedMarkup={table:table.id,icons:table.querySelectorAll('.needs_collapse span.needs').length};
          STVExtended.initializePageMetadata();STVExtended.initializePageMetadata();
        """)
        groups=browser.find_elements(By.CSS_SELECTOR,'.stv-page-metadata');assert len(groups)==1
        group=groups[0];controls=browser.find_elements(By.CSS_SELECTOR,'table.need .needs_collapse');assert controls
        for label,expected,key in [('Collapse all','false',Keys.ENTER),('Expand all','true',Keys.SPACE)]:
            for _ in range(2):
                button=group.find_element(By.XPATH,f".//button[.='{label}']");button.send_keys(key)
                assert all(c.get_attribute('aria-expanded')==expected for c in controls)
                assert browser.switch_to.active_element==button
        before=browser.execute_script('return extendedNativeClicks');controls[0].send_keys(Keys.ENTER)
        assert browser.execute_script('return extendedNativeClicks')==before+1, browser.execute_script("return {setup:extendedMarkup,control:document.querySelector('.needs_collapse').outerHTML}")
        assert controls[0].get_attribute('aria-expanded')=='false'
        assert 'Goal body remains visible.' in browser.find_element(By.TAG_NAME,'body').text
        assert browser.execute_script("return [...document.querySelectorAll('table.need .head,table.need .content')].every(e=>!e.classList.contains('collapse_is_hidden'))")
        browser.execute_script("document.querySelector('table.need').remove()")
        group.find_element(By.XPATH,".//button[.='Expand all']").click()
        assert 'Goal body remains visible.' in browser.find_element(By.TAG_NAME,'body').text


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_070','STV_SWR_071')
def test_export_pointer_snapshot_cancel_keyboard_and_serialization_recovery(browser,extended_site):
    browser.get((extended_site/'index.html').as_uri());wait=ready(browser);root=mount_controlled(browser)
    wait.until(lambda d:root.find_element(By.XPATH,".//button[.='Save as SVG']").is_enabled())
    browser.execute_async_script('const done=arguments[0];document.fonts.ready.then(()=>done(true))')
    value=browser.execute_async_script("""
      const root=arguments[0],done=arguments[1],save=[...root.querySelectorAll('button')].find(b=>b.textContent==='Save as SVG');
      root.scrollIntoView();const workspace=root.querySelector('.stv-workspace');workspace.style.position='relative';const note=document.createElement('span');note.style.cssText='position:absolute;top:20px;left:20px;z-index:1000';workspace.append(note);
      const originals={create:URL.createObjectURL,revoke:URL.revokeObjectURL,click:HTMLAnchorElement.prototype.click,serialize:XMLSerializer.prototype.serializeToString};
      const blobs=[];URL.createObjectURL=b=>{blobs.push(b);return 'blob:interaction-'+blobs.length};URL.revokeObjectURL=()=>{};HTMLAnchorElement.prototype.click=()=>{};
      const activate=detail=>save.dispatchEvent(new MouseEvent('click',{bubbles:true,detail}));
      const down=()=>save.dispatchEvent(new PointerEvent('pointerdown',{bubbles:true,button:0}));
      try{
        note.textContent='POINTER_BEFORE';down();note.textContent='POINTER_AFTER';activate(1);
        note.textContent='CANCEL_BEFORE';down();save.dispatchEvent(new PointerEvent('pointercancel'));note.textContent='CANCEL_AFTER';activate(1);
        note.textContent='BLUR_BEFORE';down();save.dispatchEvent(new Event('blur'));note.textContent='BLUR_AFTER';activate(1);
        note.textContent='OUTSIDE_BEFORE';down();document.body.dispatchEvent(new PointerEvent('pointerup',{bubbles:true}));note.textContent='OUTSIDE_AFTER';activate(1);
        note.textContent='KEY_BEFORE';down();note.textContent='KEY_AFTER';activate(0);
        const count=blobs.length;XMLSerializer.prototype.serializeToString=()=>{throw Error('Injected serializer failure')};activate(0);
        const error=root.querySelector('.stv-status').textContent;XMLSerializer.prototype.serializeToString=originals.serialize;activate(0);
        const recovered=blobs.length===count+1;
        XMLSerializer.prototype.serializeToString=function(node){activate(0);return originals.serialize.call(this,node)};
        const beforeNested=blobs.length;activate(0);const singleFlight=blobs.length===beforeNested+1;
        Promise.all(blobs.map(b=>b.text())).then(texts=>done({texts,error,recovered,singleFlight}));
      }catch(e){done({error:String(e)})}finally{STVExtended.releaseDownloads();URL.createObjectURL=originals.create;URL.revokeObjectURL=originals.revoke;HTMLAnchorElement.prototype.click=originals.click;XMLSerializer.prototype.serializeToString=originals.serialize;note.remove()}
    """,root)
    assert value['recovered'] and 'Injected serializer failure' in value['error'],value
    assert value['singleFlight'] and len(value['texts'])==7
    for text,expected,absent in zip(value['texts'],['POINTER_BEFORE','CANCEL_AFTER','BLUR_AFTER','OUTSIDE_AFTER','KEY_AFTER'],['POINTER_AFTER','CANCEL_BEFORE','BLUR_BEFORE','OUTSIDE_BEFORE','KEY_BEFORE']):
        assert expected in text and absent not in text


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_069')
def test_page_metadata_excludes_copies_and_handles_empty_pages(browser,extended_site):
    browser.get((extended_site/'host-only.html').as_uri());ready(browser)
    value=browser.execute_script("""
      for(const cls of ['stv-view','stv-detail']){const copy=document.createElement('div');copy.className=cls;copy.append(document.querySelector('table.need').cloneNode(true));document.body.append(copy)}
      const copies=[...document.querySelectorAll('.stv-view,.stv-detail')],before=copies.map(c=>c.innerHTML);
      STVExtended.schedulePageMetadata();return {before};
    """)
    group=WebDriverWait(browser,10).until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-page-metadata'))
    for label in ['Expand all','Collapse all']:
        group.find_element(By.XPATH,f".//button[.='{label}']").click()
    assert browser.execute_script("return [...document.querySelectorAll('.stv-view,.stv-detail')].map(c=>c.innerHTML)")==value['before']
    for mode in ['empty','no-metadata']:
        browser.get((extended_site/'host-only.html').as_uri());ready(browser)
        browser.execute_script("""
          if(arguments[0]==='empty')document.querySelectorAll('table.need').forEach(t=>t.remove());
          else document.querySelectorAll('table.need .needs_collapse,table.need tr.meta').forEach(n=>n.remove());
          STVExtended.initializePageMetadata();
        """,mode)
        groups=browser.find_elements(By.CSS_SELECTOR,'.stv-page-metadata')
        if mode=='empty':assert not groups
        else:
            assert len(groups)==1 and 'No collapsible Need attributes' in groups[0].text
            assert all(not b.is_enabled() for b in groups[0].find_elements(By.TAG_NAME,'button'))


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_068','STV_SWR_070','STV_SWR_072')
@pytest.mark.parametrize('protocol',['file','http'])
def test_real_font_and_selected_local_media_are_self_contained(browser,extended_site,protocol):
    font=base64.b64encode((extended_site/'_static/extended.woff2').read_bytes()).decode()
    png=base64.b64encode((extended_site/'_static/extended.png').read_bytes()).decode()
    svg=base64.b64encode((extended_site/'_static/extended.svg').read_bytes()).decode()
    with published_url(extended_site,protocol) as url:
        browser.get(url);ready(browser)
        value=browser.execute_async_script("""
          const [font,png,svg,done]=arguments;
          (async()=>{
            await document.fonts.ready;
            const box=document.createElement('article');box.style.cssText='position:fixed;left:20px;top:20px;width:400px;height:200px;background:white;z-index:10000';
            box.innerHTML='<p style="font-family:ExtendedReal">Readable local font</p><img width="20" height="20"><img width="20" height="20">';document.body.append(box);
            const base=new URL('./',document.baseURI),images=[...box.querySelectorAll('img')];
            images[0].src=new URL('_static/extended.png',base);images[0].srcset=new URL('_static/extended.png',base)+' 1x, '+new URL('_static/extended.png',base)+' 2x';
            images[1].src=new URL('_static/extended.svg',base);await Promise.all(images.map(i=>i.decode()));
            const face=new FontFace('ExtendedReal','url(data:font/woff2;base64,'+font+')');document.fonts.add(face);
            const load=document.fonts.load('16px ExtendedReal');box.getBoundingClientRect();let pendingRefused=false;
            const records={assets:{'_static/extended.png':{data:'data:image/png;base64,'+png},'_static/extended.svg':{data:'data:image/svg+xml;base64,'+svg}},fonts:[{family:'ExtendedReal',css:'@font-face{font-family:ExtendedReal;src:url(data:font/woff2;base64,'+font+')}'} ,{family:'UnselectedFont',error:'Must not be selected'}]};
            if(document.fonts.status==='loading'){try{STVExtended.capture(box,{base,resources:records})}catch(e){pendingRefused=e.message.includes('Fonts are loading')}}
            await load;await document.fonts.ready;STVExtended.scaleTypography(box,.7);
            const text=STVExtended.serialize(STVExtended.capture(box,{base,resources:records}));
            const result={loaded:face.status,pendingRefused,text,selected:images.map(i=>i.currentSrc)};box.remove();document.fonts.delete(face);done(result);
          })().catch(e=>done({error:String(e)}));
        """,font,png,svg)
    assert 'error' not in value,value
    assert value['loaded']=='loaded'
    assert 'data:font/woff2;base64,'+font in value['text']
    assert 'data:image/png;base64,'+png in value['text'] and 'data:image/svg+xml;base64,'+svg in value['text']
    assert 'UnselectedFont' not in value['text'] and 'srcset=' not in value['text']


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_070','STV_SWR_072')
def test_export_resource_retry_and_pending_fonts_refuse_capture(browser,extended_site):
    browser.get((extended_site/'index.html').as_uri());ready(browser)
    value=browser.execute_async_script("""
      const done=arguments[0];(async()=>{
        await document.fonts.ready;const original=document.head.append,base=new URL('./',document.baseURI);
        let attempts=0,failed=false;const digest='extended-injected-registration',graph={export_resources:{digest,url:'extended-resource.js'}};
        document.head.append=function(script){
          if(!script.src?.endsWith('extended-resource.js'))return original.call(this,script);
          attempts++;if(attempts===1)setTimeout(()=>script.onerror(),0);
          else{__STV_DATA__.resources[digest]={assets:{},fonts:[]};setTimeout(()=>script.onload(),0)}
        };
        try{await STVExtended.loadResources(graph,base)}catch(e){failed=e.message.includes('Reload the page')}
        const retried=await STVExtended.loadResources(graph,base);document.head.append=original;
        const box=document.createElement('div');box.style.cssText='position:fixed;top:0;left:0;width:100px;height:100px';box.textContent='READY';document.body.append(box);
        let fontBlocked=false;Object.defineProperty(document,'fonts',{configurable:true,value:{status:'loading'}});
        try{STVExtended.capture(box,{base,resources:retried})}catch(e){fontBlocked=e.message.includes('Fonts are loading')}finally{delete document.fonts}
        const recovered=STVExtended.serialize(STVExtended.capture(box,{base,resources:retried})).includes('READY');box.remove();
        done({attempts,failed,fontBlocked,recovered});
      })().catch(e=>done({error:String(e)}));
    """)
    assert value=={'attempts':2,'failed':True,'fontBlocked':True,'recovered':True}
