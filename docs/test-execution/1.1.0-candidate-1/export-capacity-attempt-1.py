from pathlib import Path
from datetime import datetime,timezone
import os,sys,shutil,tempfile,json,hashlib,time,xml.etree.ElementTree as ET
root=Path.cwd();record=root/'docs/test-execution/1.1.0-candidate-1';sys.path.insert(0,str(root/'docs/test-scripts'))
from test_browser import browser as fixture,published_url
from test_capacity import click_revision
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
os.environ['STV_GECKODRIVER']=r'C:/Users/fragg/.cache/selenium/geckodriver/win64/0.37.1/geckodriver.exe'
started=datetime.now(timezone.utc).isoformat();metrics=[];out=root/'docs/_build/export-capacity-1.1.0';out.mkdir(exist_ok=False)
with tempfile.TemporaryDirectory(prefix='stv-svgcap-') as temp:
 site=Path(temp)/'html';shutil.copytree(root/'docs/_build/release-benchmark/1.1.0-candidate-1/html',site)
 generator=fixture.__wrapped__();driver=next(generator)
 try:
  driver.set_script_timeout(120);wait=WebDriverWait(driver,90)
  for protocol in ['file','http']:
   driver.set_window_size(1600,1100)
   with published_url(site,protocol) as url:
    driver.get(url);view=wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-view[data-stv-revision]'));identity=view.get_attribute('data-stv-build')
    while len(driver.find_elements(By.CSS_SELECTOR,'.stv-nodes>.stv-node'))<200:
     selector=driver.execute_script('''const g=__STV_DATA__.graphs[arguments[0]],nodes=[...document.querySelectorAll('.stv-nodes>.stv-node')],ids=new Set(nodes.map(n=>n.querySelector('.stv-id').textContent));for(const b of document.querySelectorAll('.stv-groups button[aria-expanded="false"]')){const [id,r,d]=JSON.parse(b.dataset.focus),extra=g.adjacency[id][d][r].filter(t=>!ids.has(t));if(extra.length&&ids.size+extra.length<=200){b.id='capacity-action';return '#capacity-action';}}return null;''',identity)
     assert selector;assert 'error' not in click_revision(driver,selector);driver.execute_script("document.getElementById('capacity-action')?.removeAttribute('id')")
    buttons=view.find_elements(By.CSS_SELECTOR,'.stv-node [data-focus="details"]')[:10]
    for i,b in enumerate(buttons):
     driver.execute_script('arguments[0].click()',b)
     wait.until(lambda d:len(d.find_elements(By.CSS_SELECTOR,'.stv-persistent-detail .need'))==i+1)
    assert len(view.find_elements(By.CSS_SELECTOR,'.stv-node'))==200
    for width in [1600,900]:
     driver.set_window_size(width,1100);driver.execute_script('arguments[0].scrollIntoView({block:"start"})',view)
     driver.execute_script("[...arguments[0].querySelectorAll('button')].find(b=>b.textContent==='Reset viewport').click()",view)
     wait.until(lambda d:view.get_attribute('aria-busy')=='false');save=view.find_element(By.XPATH,".//button[.='Save as SVG']");wait.until(lambda d:save.is_enabled())
     driver.execute_script('window.exportBlob=null;const old=URL.createObjectURL;URL.createObjectURL=b=>{window.exportBlob=b;return old(b)}')
     before=set(driver.stv_download_directory.glob('*.svg'));start=time.perf_counter();save.click();wait.until(lambda d:d.execute_script('return window.exportBlob!==null'))
     text=driver.execute_async_script('const done=arguments[0];window.exportBlob.text().then(done)');elapsed=time.perf_counter()-start;ET.fromstring(text)
     downloaded=wait.until(lambda d:next(iter(set(driver.stv_download_directory.glob('*.svg'))-before),None));wait.until(lambda d:downloaded.read_text(encoding='utf-8')==text)
     assert '<script' not in text and 'data-stv-' not in text and 'Deterministic rich detail text.' in text
     path=out/f'{protocol}-{width}.svg';path.write_text(text,encoding='utf-8');driver.save_screenshot(str(record/f'export-capacity-{protocol}-{width}.png'))
     metrics.append(dict(protocol=protocol,width=width,visible_nodes=200,open_cards=10,svg_bytes=path.stat().st_size,svg_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),seconds=elapsed,path=path.relative_to(root).as_posix()))
    driver.get((out/f'{protocol}-1600.svg').as_uri());assert driver.find_elements(By.CSS_SELECTOR,'foreignObject');assert 'Deterministic rich detail text.' in driver.find_element(By.TAG_NAME,'body').text if driver.find_elements(By.TAG_NAME,'body') else 'Deterministic rich detail text.' in driver.page_source
 finally:
  try:next(generator)
  except StopIteration:pass
result=dict(started=started,finished=datetime.now(timezone.utc).isoformat(),result='passed',cases=metrics,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest());(record/'export-capacity.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
