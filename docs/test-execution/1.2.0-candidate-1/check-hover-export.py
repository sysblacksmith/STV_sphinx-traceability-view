"""Supplement: capture a real visible hover before pointer activation dismisses it."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'docs/test-scripts'))
from test_browser import browser, published_url
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

record=Path(__file__).resolve().parent
results=[]
for protocol in ['file','http']:
    session=browser.__wrapped__();driver=next(session)
    try:
        with published_url(ROOT/'docs/_build/html',protocol) as url:
            driver.get(url.replace('index.html','demo.html'))
            wait=WebDriverWait(driver,30)
            root=wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-view[data-stv-revision]'))
            driver.execute_script('arguments[0].scrollIntoView({block:"start"})',root)
            first=root.find_element(By.CSS_SELECTOR,'.stv-node:not(.stv-project)')
            ActionChains(driver).move_to_element(first).perform()
            hover=wait.until(lambda d:d.find_element(By.CSS_SELECTOR,'.stv-hover-detail table.need'))
            visible_words=driver.execute_script("""
              const table=arguments[0],workspace=arguments[1].querySelector('.stv-workspace').getBoundingClientRect(),panel=table.closest('.stv-hover-detail').getBoundingClientRect();
              const clip={left:Math.max(0,workspace.left,panel.left),top:Math.max(0,workspace.top,panel.top),right:Math.min(innerWidth,workspace.right,panel.right),bottom:Math.min(innerHeight,workspace.bottom,panel.bottom)};
              const walker=document.createTreeWalker(table,NodeFilter.SHOW_TEXT),words=[];let node;
              while(node=walker.nextNode())for(const match of node.data.matchAll(/\\S+/g)){
                const range=document.createRange();range.setStart(node,match.index);range.setEnd(node,match.index+match[0].length);
                const rect=range.getBoundingClientRect(),style=getComputedStyle(node.parentElement);
                if(style.visibility!=='hidden'&&rect.width>0&&rect.height>0&&rect.left>=clip.left&&rect.top>=clip.top&&rect.right<=clip.right&&rect.bottom<=clip.bottom)words.push(match[0]);
              }return words;
            """,hover,root)
            assert visible_words
            driver.save_screenshot(str(record/f'hover-before-{protocol}.png'))
            save=root.find_element(By.XPATH,".//button[.='Save as SVG']")
            wait.until(lambda d:save.is_enabled())
            value=driver.execute_async_script("""
              const save=arguments[0],root=arguments[1],done=arguments[2];
              const originalCreate=URL.createObjectURL,originalClick=HTMLAnchorElement.prototype.click;
              let blob;URL.createObjectURL=value=>{blob=value;return originalCreate(value)};HTMLAnchorElement.prototype.click=()=>{};
              const revision=root.dataset.stvRevision;
              save.dispatchEvent(new PointerEvent('pointerdown',{button:0,bubbles:true}));
              document.querySelectorAll('.stv-hover-detail').forEach(p=>p.remove());
              save.dispatchEvent(new MouseEvent('click',{detail:1,bubbles:true}));
              URL.createObjectURL=originalCreate;HTMLAnchorElement.prototype.click=originalClick;
              if(!blob){done({error:root.querySelector('.stv-status').textContent});return}
              blob.text().then(text=>done({text,revisionUnchanged:root.dataset.stvRevision===revision}));
            """,save,root)
            assert 'error' not in value,value
            assert value['revisionUnchanged']
            assert 'stv-hover-detail' in value['text'] and 'data-stv-' not in value['text']
            assert '<script' not in value['text']
            ET.fromstring(value['text'])
            path=record/f'hover-export-{protocol}.svg';path.write_text(value['text'],encoding='utf-8')
            driver.get(path.as_uri())
            reopened=driver.find_element(By.CSS_SELECTOR,'.stv-hover-detail table.need')
            assert all(word in reopened.text for word in visible_words),(reopened.text,visible_words)
            driver.save_screenshot(str(record/f'hover-reopened-{protocol}.png'))
            results.append({'protocol':protocol,'result':'passed','visible_words_checked':len(visible_words),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'bytes':path.stat().st_size})
    finally:
        try:next(session)
        except StopIteration:pass
(record/'hover-export.json').write_text(json.dumps({'recorded_at':datetime.now(timezone.utc).isoformat(),'results':results},indent=2)+'\n',encoding='utf-8')
print(json.dumps(results,indent=2))
