import {detailCollection,DEFAULT_DETAILS_LIMIT} from './collection.js';
import {loadDetail,detailContent,associate} from './content.js';
import {scaleTypography} from './typography.js';
let sequence=0;
/** Collection DOM is independent of graph commits and transient hover. */
export function persistentDetails(root,graph,base,{stack,findTrigger,fallback,changed,load=loadDetail}) {
  const collection=detailCollection(graph.details_limit===undefined?DEFAULT_DETAILS_LIMIT:graph.details_limit);
  function remove(entry) {
    if(!entry)return;
    associate(entry.trigger,entry.panel.id,false);associate(findTrigger(entry.id),entry.panel.id,false);
    entry.panel.remove();
  }
  function sync() {
    for(const entry of collection.entries.values()) {
      const trigger=findTrigger(entry.id);
      if(entry.trigger!==trigger)associate(entry.trigger,entry.panel.id,false);
      entry.trigger=trigger;associate(trigger,entry.panel.id);
    }
    changed(collection.entries.size);
  }
  function close(id) {
    const entry=collection.close(id);if(!entry)return;
    remove(entry);sync();(findTrigger(id)||fallback).focus();
  }
  function clear(restore=true) {for(const entry of collection.clear())remove(entry);sync();if(restore)fallback.focus();}
  function reveal(entry) {
    entry.dismiss.focus({preventScroll:true});entry.dismiss.scrollIntoView({block:'nearest',inline:'nearest'});
  }
  function open(id) {
    if(!graph.objects[id])return;
    const {entry,reused,evicted}=collection.open(id,()=> {
      const panel=document.createElement('article');panel.className='stv-detail stv-persistent-detail';
      panel.id=`${root.id}-persistent-${++sequence}`;panel.dataset.needId=id;panel.tabIndex=-1;
      panel.setAttribute('role','region');panel.setAttribute('aria-label',`Details for ${id}`);
      const title=document.createElement('h3');title.textContent=`${id}: ${graph.objects[id].title}`;
      const dismiss=document.createElement('button');dismiss.textContent='Close details';dismiss.type='button';dismiss.dataset.persistentClose='';dismiss.setAttribute('aria-label',`Close details for ${id}`);dismiss.onclick=()=>close(id);
      const original=document.createElement('a');original.textContent='Open original object';original.href=new URL(graph.objects[id].url,base).href;original.target='_blank';original.rel='noopener noreferrer';
      const body=document.createElement('div');body.className='stv-persistent-body';body.tabIndex=0;body.textContent='Loading details...';body.setAttribute('aria-live','polite');
      panel.append(title,dismiss,original,body);return {id,panel,dismiss,body};
    });
    if(reused){sync();reveal(entry);return;}
    remove(evicted);stack.append(entry.panel);scaleTypography(entry.panel,graph.presentation?.details_font_scale??1);sync();reveal(entry);
    Promise.resolve().then(()=>load(graph,id,base)).then(html=> {
      if(collection.entries.get(id)!==entry||!entry.panel.isConnected)return;
      entry.body.replaceChildren(detailContent(html,graph,id,base,`${entry.panel.id}-`));
      scaleTypography(entry.panel,graph.presentation?.details_font_scale??1);
    }).catch(error=>{if(collection.entries.get(id)===entry&&entry.panel.isConnected)entry.body.textContent=error.message;});
  }
  sync();return {open,close,clear,sync};
}
