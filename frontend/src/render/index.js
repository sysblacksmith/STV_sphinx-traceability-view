import {mount} from './view.js';
import {schedulePageMetadata} from './page-metadata.js';
function start() {
  schedulePageMetadata();
  if(!document.querySelector('.stv-view'))return;
  const script=[...document.scripts].find(s=>s.hasAttribute('data-stv-root'));
  const base=new URL(script.dataset.stvRoot,document.baseURI);
  document.querySelectorAll('.stv-view').forEach(root=> {
    const graph=globalThis.__STV_DATA__?.graphs[root.dataset.stvBuild];
    if(!graph){root.textContent='Traceability graph unavailable: build finalization did not complete.';return;}
    mount(root,graph,base).catch(error=>{root.textContent=`Traceability view failed: ${error.message}`;});
  });
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start);else start();
