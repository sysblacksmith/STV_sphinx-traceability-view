"""PR013 PoC: reader-visible anchor and peer stability during group navigation."""
import json
import os
from pathlib import Path
import shutil
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser,short_output,published_url
from test_build import build,FIXTURE


def positions(driver):
    return driver.execute_script("""return Object.fromEntries([...document.querySelector('.stv-view').querySelectorAll('.stv-node')].map(n=>{
      const r=n.getBoundingClientRect();return [JSON.parse(n.dataset.key)[1],{left:r.left,top:r.top,x:parseFloat(n.style.left),y:parseFloat(n.style.top)}];}));""")


def prepare_source(source):
    shutil.copytree(FIXTURE,source)
    with (source/'conf.py').open('a',encoding='utf-8') as stream:stream.write("\nneeds_id_regex = r'^[A-Z]+$'\n")
    (source/'index.rst').write_text('Stable navigation\n=================\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: P Q\n',encoding='utf-8')
    requirements='Requirements\n============\n\n'
    for parent,children in [('P',['A','B','C','D','E']),('Q',['F'])]:
        requirements+=f'.. shr:: Parent {parent}\n   :id: {parent}\n   :traces: '+', '.join(children)+'\n\n   Parent content.\n\n'
    for child in 'ABCDEF':requirements+=f'.. swr:: Child {child}\n   :id: {child}\n\n   Child content.\n\n'
    (source/'requirements.rst').write_text(requirements,encoding='utf-8')


@pytest.mark.browser
@pytest.mark.parametrize('protocol',['file','http'])
def test_poc_group_navigation_keeps_existing_nodes_still(browser,short_output,protocol):
    source=short_output/'source';prepare_source(source)
    output=short_output/'html';result=build(source,output);assert result.returncode==0,result.stdout+result.stderr
    observations=[]
    with published_url(output,protocol) as url:
        browser.get(url);wait=WebDriverWait(browser,15)
        wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
        try:
            for revision,parent in enumerate(['P','Q','P','P'],1):
                before=positions(browser)
                control=browser.execute_script('return [...document.querySelectorAll(".stv-view .stv-node")].find(n=>JSON.parse(n.dataset.key)[1]===arguments[0]).querySelector(".stv-groups button")',parent)
                browser.execute_script('arguments[0].focus({preventScroll:true})',control)
                control.send_keys(Keys.ENTER)
                wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-view').get_attribute('data-stv-revision')==str(revision))
                after=positions(browser)
                deltas={identity:{k:after[identity][k]-value[k] for k in value} for identity,value in before.items() if identity in after}
                observations.append({'parent':parent,'revision':revision,'before':before,'after':after,'deltas':deltas})
                assert all(abs(v)<.5 for identity in ['P','Q'] for v in deltas[identity].values()),deltas
                assert all(abs(v)<.5 for values in deltas.values() for v in values.values()),deltas
                assert browser.execute_script('return document.activeElement.closest(".stv-node").dataset.key')==json.dumps(['need',parent],separators=(',',':'))
        finally:
            record=os.environ.get('STV_POSITION_RECORD')
            if record:
                path=Path(record);path.mkdir(parents=True,exist_ok=True)
                (path/(protocol+'.json')).write_text(json.dumps(observations,indent=2),encoding='utf-8')
                browser.save_screenshot(str(path/(protocol+'.png')))


@pytest.mark.browser
@pytest.mark.parametrize('protocol',['file','http'])
@pytest.mark.parametrize('direction',['down','up'])
def test_poc_arrow_viewport_covers_negative_routes(browser,short_output,protocol,direction):
    source=short_output/'source';prepare_source(source)
    parent='P'
    if direction=='up':
        (source/'index.rst').write_text('Upward stability\n================\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: A B\n',encoding='utf-8')
        with (source/'conf.py').open('a',encoding='utf-8') as stream:
            stream.write("\nneeds_links['traces']['outgoing'] = 'Deliberately long wrapping outgoing relationship label ' * 12\n")
            stream.write("needs_types.append({'directive':'top','title':'Top','prefix':'TOP_','color':'#ddd','style':'node'})\n")
            stream.write("traceability_view_model['levels'].insert(0,'top')\ntraceability_view_model['types']['top']={'level':'top'}\n")
        text=(source/'requirements.rst').read_text()
        text+='\n.. top:: Earlier ancestor\n   :id: R\n   :traces: P\n\n   Ancestor content.\n'
        (source/'requirements.rst').write_text(text)
        parent='A'
    result=build(source,short_output/'html');assert result.returncode==0,result.stdout+result.stderr
    with published_url(short_output/'html',protocol) as url:
        browser.get(url);wait=WebDriverWait(browser,15)
        wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
        before=positions(browser)
        browser.execute_script('const n=[...document.querySelectorAll(".stv-view .stv-node")].find(n=>JSON.parse(n.dataset.key)[1]===arguments[0]);[...n.querySelectorAll(".stv-groups button")].find(b=>JSON.parse(b.dataset.focus)[1]==="traces").click()',parent)
        wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-view').get_attribute('data-stv-revision')=='1')
        if direction=='up':
            browser.execute_script('const n=[...document.querySelectorAll(".stv-view .stv-node")].find(n=>JSON.parse(n.dataset.key)[1]==="P");[...n.querySelectorAll(".stv-groups button")].find(b=>JSON.parse(b.dataset.focus)[1]==="traces"&&JSON.parse(b.dataset.focus)[2]==="incoming").click()')
            wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-view').get_attribute('data-stv-revision')=='2')
        after=positions(browser)
        assert all(abs(after[k][axis]-value)<.5 for k,values in before.items() for axis,value in values.items())
        observed=browser.execute_script("""const svg=document.querySelector('.stv-view svg.stv-edges');
          const b=svg.hasAttribute('viewBox')?svg.viewBox.baseVal:{x:0,y:0,width:svg.width.baseVal.value,height:svg.height.baseVal.value};
          const paths=[...svg.querySelectorAll('polyline')],pts=paths.flatMap(p=>[...p.points]);
          const negative=pts.filter(p=>p.x<0||p.y<0).length;
          const outside=pts.filter(p=>p.x<b.x||p.x>b.x+b.width||p.y<b.y||p.y>b.y+b.height).map(p=>[p.x,p.y]);
          const boxes=[...document.querySelectorAll('.stv-view .stv-node')].map(n=>n.getBoundingClientRect());
          const boundary=p=>boxes.some(r=>(Math.abs(p.x-r.left)<2||Math.abs(p.x-r.right)<2)&&p.y>=r.top-2&&p.y<=r.bottom+2||(Math.abs(p.y-r.top)<2||Math.abs(p.y-r.bottom)<2)&&p.x>=r.left-2&&p.x<=r.right+2);
          const matrix=svg.getScreenCTM();
          const aligned=paths.every(p=>[p.points[0],p.points[p.points.length-1]].every(v=>boundary(new DOMPoint(v.x,v.y).matrixTransform(matrix))));
          return {negative,outside,aligned,viewBox:{x:b.x,y:b.y,width:b.width,height:b.height},paths:paths.length};""")
        record=os.environ.get('STV_POSITION_RECORD')
        if record:
            path=Path(record);path.mkdir(parents=True,exist_ok=True)
            (path/(protocol+'-'+direction+'-arrows.json')).write_text(json.dumps(observed,indent=2),encoding='utf-8')
        assert observed['negative']>0,observed
        assert observed['outside']==[],observed
        assert observed['aligned'],observed


@pytest.mark.browser
@pytest.mark.parametrize('protocol',['file','http'])
def test_poc_initial_numeric_seed_order(browser,short_output,protocol):
    source=short_output/'source';shutil.copytree(FIXTURE,source)
    ids=['REQ_20','REQ_10','REQ_3','REQ_2','REQ_1']
    (source/'index.rst').write_text('Numeric seeds\n=============\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: '+ ' '.join(ids)+'\n',encoding='utf-8')
    text='Requirements\n============\n\n'
    for identity in ids:
        text+=f'.. shr:: Seed {identity}\n   :id: {identity}\n'
        if identity=='REQ_2':text+='   :traces: CHILD_A\n'
        text+='\n   Seed content.\n\n'
    text+='.. swr:: Child\n   :id: CHILD_A\n\n   Child content.\n'
    (source/'requirements.rst').write_text(text,encoding='utf-8')
    result=build(source,short_output/'html');assert result.returncode==0,result.stdout+result.stderr
    with published_url(short_output/'html',protocol) as url:
        browser.get(url);wait=WebDriverWait(browser,15)
        wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
        before=positions(browser)
        order=sorted(before,key=lambda k:before[k]['x'])
        assert order==['REQ_1','REQ_2','REQ_3','REQ_10','REQ_20'],order
        browser.execute_script('const n=[...document.querySelectorAll(".stv-view .stv-node")].find(n=>JSON.parse(n.dataset.key)[1]==="REQ_2");n.querySelector(".stv-groups button").click()')
        wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-view').get_attribute('data-stv-revision')=='1')
        after=positions(browser)
        assert all(abs(after[k][axis]-value)<.5 for k,values in before.items() for axis,value in values.items())
        record=os.environ.get('STV_POSITION_RECORD')
        if record:
            path=Path(record);path.mkdir(parents=True,exist_ok=True)
            (path/(protocol+'-numeric-order.json')).write_text(json.dumps({'order':order,'old_nodes_unchanged':True},indent=2),encoding='utf-8')
