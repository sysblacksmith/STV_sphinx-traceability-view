"""PR014: make the actual graph clipping edge visible without changing interaction."""
import json
import os
from pathlib import Path
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser, short_output, published_url
from test_build import build, FIXTURE


def geometry(driver,root):
    return driver.execute_script("""const v=arguments[0].querySelector('.stv-viewport'),n=arguments[0].querySelector('.stv-node'),s=getComputedStyle(v),r=v.getBoundingClientRect(),b=n.getBoundingClientRect();
      const x=Math.max(r.left+2,Math.min(r.right-2,b.left+b.width/2));
      const hit=y=>document.elementFromPoint(x,y)?.closest('.stv-node')?.dataset.key||null;
      return {viewport:{x:r.x,y:r.y,width:r.width,height:r.height},node:{top:b.top,bottom:b.bottom},
        clipTop:r.top+v.clientTop,clientHeight:v.clientHeight,clientWidth:v.clientWidth,
        borderWidth:parseFloat(s.borderTopWidth),borderStyle:s.borderTopStyle,borderColor:s.borderTopColor,
        aboveHit:hit(r.top-2),borderHit:hit(r.top+.5),insideHit:hit(r.top+v.clientTop+2),
        nodeKey:n.dataset.key,world:[n.style.left,n.style.top],
        statusBottom:arguments[0].querySelector('.stv-status').getBoundingClientRect().bottom,
        toolbarBottom:arguments[0].querySelector('.stv-toolbar').getBoundingClientRect().bottom};""",root)


def activate(driver,root,label):
    driver.execute_script("[...arguments[0].querySelectorAll('.stv-toolbar button')].find(b=>b.textContent===arguments[1]).click()",root,label)


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_062')
@pytest.mark.parametrize('protocol',['file','http'])
def test_viewport_boundary_tracks_clipping_and_controls(browser,short_output,protocol):
    result=build(FIXTURE,short_output/'html');assert result.returncode==0,result.stdout+result.stderr
    observations=[]
    with published_url(short_output/'html',protocol) as url:
        browser.set_window_size(780,1100);browser.get(url);wait=WebDriverWait(browser,20)
        wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))==2)
        roots=browser.find_elements(By.CSS_SELECTOR,'.stv-view');root,other=roots
        other_before=browser.execute_script("return [arguments[0].dataset.stvRevision,arguments[0].querySelector('.stv-scene').style.transform]",other)
        initial=geometry(browser,root)
        # Public controls move a real node through the overflow boundary.
        activate(browser,root,'Pan down');clipped=geometry(browser,root)
        assert clipped['node']['top']<clipped['clipTop']<clipped['node']['bottom'],clipped
        assert clipped['aboveHit'] is None and clipped['insideHit']==clipped['nodeKey'],clipped
        observations.append({'stage':'clipped','geometry':clipped})
        target=os.environ.get('STV_BOUNDARY_RECORD')
        if target:
            out=Path(target);out.mkdir(parents=True,exist_ok=True)
            (out/(protocol+'.json')).write_text(json.dumps(observations,indent=2),encoding='utf-8')
            browser.save_screenshot(str(out/(protocol+'.png')))
        assert clipped['borderWidth']==1 and clipped['borderStyle']=='solid',clipped
        assert clipped['borderColor']=='rgb(153, 153, 153)',clipped
        assert clipped['borderHit'] is None,'The marker is outside the clipped node area'
        assert clipped['world']==initial['world'] and clipped['clientHeight']==975
        activate(browser,root,'Zoom in');zoomed=geometry(browser,root)
        assert zoomed['viewport']==clipped['viewport'],'The marker must not move with the scene'
        assert zoomed['world']==initial['world']
        # Mimic a host theme's global border-box rule without changing the widget.
        browser.execute_script("const s=document.createElement('style');s.textContent='* {box-sizing:border-box}';document.head.append(s)")
        for width in [1440,780]:
            browser.set_window_size(width,1100);g=geometry(browser,root)
            assert g['clientHeight']==975 and g['borderWidth']==1
            assert abs(g['viewport']['width']-g['clientWidth'])<.1
            assert g['viewport']['y']>=max(g['statusBottom'],g['toolbarBottom'])-.5
            assert g['world']==initial['world'];observations.append({'stage':f'width-{width}-border-box','geometry':g})
        activate(browser,root,'Reset viewport')
        control=root.find_element(By.CSS_SELECTOR,'.stv-groups button')
        control.send_keys(Keys.ENTER)
        wait.until(lambda d:root.get_attribute('data-stv-revision')=='1')
        assert len(root.find_elements(By.CSS_SELECTOR,'.stv-node'))==2
        assert browser.execute_script("return [arguments[0].dataset.stvRevision,arguments[0].querySelector('.stv-scene').style.transform]",other)==other_before
        final=geometry(browser,root);assert final['borderWidth']==1 and final['clientHeight']==975
        if target:
            (out/(protocol+'.json')).write_text(json.dumps(observations,indent=2),encoding='utf-8')
            browser.save_screenshot(str(out/(protocol+'-controls.png')))
