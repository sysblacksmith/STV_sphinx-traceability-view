"""CR_013: published classified rows, fallback evidence and stable navigation."""
from pathlib import Path
import json
import os
import shutil
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser, short_output, published_url
from test_build import FIXTURE, build

LEVELS=['stakeholder','system','system_cases','system_runs','system_arch','software','software_cases','software_runs','software_arch','fallback','problems']
EXPECTED={'ROW_G':0,'ROW_SYS':1,'ROW_TS':2,'ROW_TS2':2,'ROW_ES':3,'ROW_ES2':3,'ROW_ES3':3,'ROW_A':4,'ROW_W':5,'ROW_TW':6,'ROW_EW':7,'ROW_C':8,'ROW_U':9,'ROW_EU':9,'ROW_ORPHAN':9,'ROW_PR':10}


def prepare_source(source):
    shutil.copytree(FIXTURE,source)
    types=[{'directive':name,'title':name,'prefix':name.upper()+'_','color':'#ddeeff','style':'node'} for name in ['goal','system','arch','software','component','case','run','problem']]
    links={name:{'incoming':name+' incoming','outgoing':name+' outgoing'} for name in ['traces','checks','attempts']}
    model={'levels':LEVELS,'types':{'goal':{'level':'stakeholder','role':'stakeholder'},'system':{'level':'system'},'arch':{'level':'system_arch'},'software':{'level':'software'},'component':{'level':'software_arch'},'problem':{'level':'problems'},
       'case':{'levels_by_tag':{'system_boundary':'system_cases','software_boundary':'software_cases'},'fallback_level':'fallback'},
       'run':{'level_from':{'relation':'attempts','direction':'incoming','levels':{'system_cases':'system_runs','software_cases':'software_runs'}},'fallback_level':'fallback'}}}
    with (source/'conf.py').open('a',encoding='utf-8') as f:f.write(f"\nneeds_types={types!r}\nneeds_links={links!r}\ntraceability_view_model={model!r}\n")
    (source/'index.rst').write_text('Classified rows\n===============\n\n.. toctree::\n\n   requirements\n\n'+''.join('.. traceability-view:: '+id+'\n\n' for id in ['ROW_W','ROW_TS','ROW_ES']),encoding='utf-8')
    records=[('ROW_G','goal',{'traces':['ROW_SYS']}),('ROW_SYS','system',{'traces':['ROW_TS','ROW_TS2']}),
      ('ROW_TS','case',{'tags':['system_boundary'],'checks':['ROW_SYS','ROW_W'],'attempts':['ROW_ES','ROW_ES2']}),
      ('ROW_TS2','case',{'tags':['system_boundary'],'attempts':['ROW_ES3']}),
      ('ROW_ES','run',{'traces':['ROW_A']}),('ROW_ES2','run',{}),('ROW_ES3','run',{}),
      ('ROW_A','arch',{'traces':['ROW_W']}),('ROW_W','software',{'traces':['ROW_TW','ROW_U','ROW_ORPHAN']}),
      ('ROW_TW','case',{'tags':['software_boundary'],'checks':['ROW_W'],'attempts':['ROW_EW']}),
      ('ROW_EW','run',{'traces':['ROW_C']}),('ROW_C','component',{'traces':['ROW_G','ROW_PR']}),
      ('ROW_U','case',{'tags':['system_boundary','software_boundary'],'attempts':['ROW_EU']}),('ROW_EU','run',{}),('ROW_ORPHAN','run',{}),('ROW_PR','problem',{})]
    text='Requirements\n============\n\n'
    for id,type,fields in records:
        text+=f'.. {type}:: {id} title\n   :id: {id}\n'
        for field,values in fields.items():text+='   :'+field+': '+', '.join(values)+'\n'
        text+='\n   Rich **body** for '+id+'.\n\n'
    (source/'requirements.rst').write_text(text,encoding='utf-8')


def boxes(driver,root):
    return driver.execute_script("""return Object.fromEntries([...arguments[0].querySelectorAll('.stv-node')].map(n=>{const r=n.getBoundingClientRect();return [JSON.parse(n.dataset.key)[1],{x:parseFloat(n.style.left),y:parseFloat(n.style.top),height:n.offsetHeight,left:r.left,top:r.top}]}));""",root)


@pytest.mark.browser
@pytest.mark.requirements('STV_SYS_002','STV_SYS_005','STV_SWR_012','STV_SWR_037','STV_SWR_055','STV_SWR_058','STV_SWR_061')
@pytest.mark.parametrize('protocol',['file','http'])
def test_published_classified_rows_and_fallback_navigation(browser,short_output,protocol):
    source=short_output/'source';prepare_source(source)
    result=build(source,short_output/'html');assert result.returncode==0,result.stdout+result.stderr
    observations=[]
    with published_url(short_output/'html',protocol) as url:
        browser.get(url);wait=WebDriverWait(browser,20)
        wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))==3)
        roots=browser.find_elements(By.CSS_SELECTOR,'.stv-view')
        for index,root in enumerate(roots):
            browser.execute_script('arguments[0].scrollIntoView()',root)
            other_revisions=[r.get_attribute('data-stv-revision') for r in roots]
            for _ in range(40):
                before=boxes(browser,root);revision=int(root.get_attribute('data-stv-revision'))
                action=browser.execute_script("""const root=arguments[0],graph=__STV_DATA__.graphs[root.dataset.stvBuild],seen=new Set([...root.querySelectorAll('.stv-id')].map(n=>n.textContent));
                  for(const b of root.querySelectorAll('.stv-groups button[aria-expanded="false"]')) {const [id,r,d]=JSON.parse(b.dataset.focus);if(graph.adjacency[id][d][r].some(x=>!seen.has(x)))return b;}return null;""",root)
                if action is None:break
                anchor=json.loads(action.get_attribute('data-focus'))[0]
                browser.execute_script('arguments[0].click()',action)
                wait.until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1)
                after=boxes(browser,root)
                assert all(abs(after[anchor][axis]-before[anchor][axis])<.5 for axis in ['x','y','left','top'])
                for id in set(before)&set(after):
                    assert abs(after[id]['x']-before[id]['x'])<.5
                    if EXPECTED[id]==EXPECTED[anchor]:assert abs(after[id]['y']-before[id]['y'])<.5
                assert all(r.get_attribute('data-stv-revision')==other_revisions[i] for i,r in enumerate(roots) if i!=index)
            actual=boxes(browser,root);assert set(actual)==set(EXPECTED)
            for rank in range(len(LEVELS)):
                row=[v for id,v in actual.items() if EXPECTED[id]==rank]
                assert len({v['y'] for v in row})==1
                if rank+1<len(LEVELS):assert max(v['y']+v['height'] for v in row)<min(v['y'] for id,v in actual.items() if EXPECTED[id]==rank+1)
            assert len(root.find_elements(By.CSS_SELECTOR,'.stv-placement-warning'))==3
            assert all(n.get_attribute('textContent')=='Unclassified test evidence' for n in root.find_elements(By.CSS_SELECTOR,'.stv-placement-warning'))
            directions=browser.execute_script("""const n=[...arguments[0].querySelectorAll('.stv-node')].find(n=>JSON.parse(n.dataset.key)[1]==='ROW_TS');return [...n.querySelectorAll('.stv-groups button')].map(b=>JSON.parse(b.dataset.focus).slice(1));""",root)
            assert directions==[['traces','incoming'],['checks','outgoing'],['attempts','outgoing']]
            browser.execute_script("[...arguments[0].querySelectorAll('.stv-toolbar button')].find(b=>b.textContent==='Reset viewport').click()",root)
            assert {id:(v['x'],v['y']) for id,v in boxes(browser,root).items()}=={id:(v['x'],v['y']) for id,v in actual.items()}
            # All polylines still end at actual node borders in screen space.
            assert browser.execute_script("""const root=arguments[0],svg=root.querySelector('.stv-edges'),m=svg.getScreenCTM(),rects=[...root.querySelectorAll('.stv-node')].map(n=>n.getBoundingClientRect());
              const on=p=>rects.some(r=>((Math.abs(p.x-r.left)<2||Math.abs(p.x-r.right)<2)&&p.y>=r.top-2&&p.y<=r.bottom+2)||((Math.abs(p.y-r.top)<2||Math.abs(p.y-r.bottom)<2)&&p.x>=r.left-2&&p.x<=r.right+2));
              return [...svg.querySelectorAll('polyline')].every(p=>[p.points[0],p.points[p.points.length-1]].every(q=>on(new DOMPoint(q.x,q.y).matrixTransform(m))));""",root)
            observations.append({'seed':['ROW_W','ROW_TS','ROW_ES'][index],'rows':{id:EXPECTED[id] for id in actual},'world_boxes':actual})
            # Collapse a seed group and verify its stable anchor plus fixed classifications.
            control=browser.execute_script("return arguments[0].querySelector('.stv-groups button[aria-expanded=true]')",root)
            if control:
                anchor=json.loads(control.get_attribute('data-focus'))[0];before=boxes(browser,root);revision=int(root.get_attribute('data-stv-revision'))
                browser.execute_script('arguments[0].click()',control);wait.until(lambda d:int(root.get_attribute('data-stv-revision'))==revision+1)
                after=boxes(browser,root);assert (after[anchor]['x'],after[anchor]['y'])==(before[anchor]['x'],before[anchor]['y'])
        target=os.environ.get('STV_CLASSIFIED_RECORD')
        if target:
            directory=Path(target);directory.mkdir(parents=True,exist_ok=True)
            (directory/(protocol+'.json')).write_text(json.dumps(observations,indent=2),encoding='utf-8')
            browser.save_screenshot(str(directory/(protocol+'.png')))
