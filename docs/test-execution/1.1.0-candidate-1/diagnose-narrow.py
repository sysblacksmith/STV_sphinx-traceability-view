from pathlib import Path
from datetime import datetime,timezone
import os,sys,shutil,tempfile,json,hashlib,time,xml.etree.ElementTree as ET
root=Path.cwd();record=root/'docs/test-execution/1.1.0-candidate-1';sys.path.insert(0,str(root/'docs/test-scripts'))
from test_browser import browser as fixture,published_url
from test_capacity import click_revision
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
os.environ['STV_GECKODRIVER']=r'C:/Users/fragg/.cache/selenium/geckodriver/win64/0.37.1/geckodriver.exe'
started=datetime.now(timezone.utc).isoformat();metrics=[];out=root/'docs/_build/export-capacity-1.1.0';out.mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(prefix='stv-svgcap-') as temp:
 site=root/'docs/_build/release-benchmark/1.1.0-candidate-1/html'
 generator=fixture.__wrapped__();driver=next(generator)
 try:
  driver.set_script_timeout(120);wait=WebDriverWait(driver,90)
  for protocol in ['http']:
   driver.set_window_size(1600,1100)
   with published_url(site,protocol) as url:
    driver.get(url);view=wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-view[data-stv-revision]'));identity=view.get_attribute('data-stv-build');driver.execute_script("const s=document.createElement('style');s.textContent='div.document{width:100%!important;margin:0!important}div.body{max-width:none!important;width:auto!important}div.bodywrapper{margin:0!important}div.sphinxsidebar{display:none!important}';document.head.append(s)")
    while len(driver.find_elements(By.CSS_SELECTOR,'.stv-nodes>.stv-node'))<200:
     selector=driver.execute_script('''const g=__STV_DATA__.graphs[arguments[0]],nodes=[...document.querySelectorAll('.stv-nodes>.stv-node')],ids=new Set(nodes.map(n=>n.querySelector('.stv-id').textContent));for(const b of document.querySelectorAll('.stv-groups button[aria-expanded="false"]')){const [id,r,d]=JSON.parse(b.dataset.focus),extra=g.adjacency[id][d][r].filter(t=>!ids.has(t));if(extra.length&&ids.size+extra.length<=200){b.id='capacity-action';return '#capacity-action';}}return null;''',identity)
     assert selector;assert 'error' not in click_revision(driver,selector);driver.execute_script("document.getElementById('capacity-action')?.removeAttribute('id')")
    buttons=view.find_elements(By.CSS_SELECTOR,'.stv-node [data-focus="details"]')[:10]
    for i,b in enumerate(buttons):
     print('Opening',protocol,i,b.get_attribute('outerHTML'),flush=True)
     driver.execute_script('arguments[0].click()',b)
     try:WebDriverWait(driver,15).until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-persistent-detail table.need'))==i+1)
     except Exception:
      print('Panels:',driver.execute_script("return [...document.querySelectorAll('.stv-persistent-detail')].map(p=>p.textContent)"),flush=True)
      driver.save_screenshot(str(record/'export-capacity-diagnostic.png'))
      raise
    assert len(view.find_elements(By.CSS_SELECTOR,'.stv-node'))==200
    for width in [900]:
     driver.set_window_size(width,1100);driver.execute_script('arguments[0].scrollIntoView({block:"start"})',view)
     driver.execute_script("[...arguments[0].querySelectorAll('button')].find(b=>b.textContent==='Reset viewport').click()",view)
     wait.until(lambda d:view.get_attribute('aria-busy')=='false');save=view.find_element(By.XPATH,".//button[.='Save as SVG']");wait.until(lambda d:save.is_enabled())
     driver.execute_script('window.exportBlob=null;const old=URL.createObjectURL;URL.createObjectURL=b=>{window.exportBlob=b;return old(b)}')
     visible_cards=driver.execute_script("return [...document.querySelectorAll('.stv-persistent-detail')].filter(p=>{const r=p.getBoundingClientRect();return r.top<innerHeight&&r.bottom>0&&r.left<innerWidth&&r.right>0}).length");before=set(driver.stv_download_directory.glob('*.svg'));start=time.perf_counter();save.click();wait.until(lambda d:d.execute_script('return window.exportBlob!==null'))
     text=driver.execute_async_script('const done=arguments[0];window.exportBlob.text().then(done)');elapsed=time.perf_counter()-start;ET.fromstring(text)
     downloaded=wait.until(lambda d:next(iter(set(driver.stv_download_directory.glob('*.svg'))-before),None));wait.until(lambda d:downloaded.read_text(encoding='utf-8')==text)
     assert '<script' not in text and 'data-stv-' not in text
     print('TEXT',len(text),'detail?', 'Deterministic rich detail text.' in text,'IDs?', 'BENCHMARK_LONG_IDENTIFIER_' in text,flush=True)
     print('GEOMETRY',driver.execute_script("return {scrollY,screen:[innerWidth,innerHeight],workspace:document.querySelector('.stv-workspace').getBoundingClientRect().toJSON(),cards:[...document.querySelectorAll('.stv-persistent-detail')].map(p=>p.getBoundingClientRect().toJSON())}"),flush=True)
     svg=ET.fromstring(text);assert 0<float(svg.get('width'))<=driver.execute_script('return innerWidth');assert 0<float(svg.get('height'))<=driver.execute_script('return innerHeight')
     print('Export',protocol,width,'visible cards',visible_cards,'bytes',len(text),flush=True)
     path=out/f'{protocol}-{width}.svg';path.write_text(text,encoding='utf-8');driver.save_screenshot(str(record/f'export-capacity-{protocol}-{width}.png'))
     metrics.append(dict(protocol=protocol,width=width,visible_nodes=200,open_cards=10,visible_cards=visible_cards,svg_bytes=path.stat().st_size,svg_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),seconds=elapsed,path=path.relative_to(root).as_posix()))
    pass
 finally:
  try:next(generator)
  except StopIteration:pass
result=dict(started=started,finished=datetime.now(timezone.utc).isoformat(),result='passed',cases=metrics,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(record/'narrow-diagnostic.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
