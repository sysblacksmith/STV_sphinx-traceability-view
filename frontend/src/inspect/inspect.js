import {computePosition,autoUpdate,offset,flip,shift,size} from '@floating-ui/dom';
import {loadDetail,detailContent,associate} from './content.js';
export {loadDetail} from './content.js';
let sequence=0;
export function inspector(root,graph,base) {
  let panel,cleanup,trigger,timer,hoverTimer,hoverButton,token=0;
  const cancelHover=()=> {clearTimeout(hoverTimer);hoverButton=null;};
  const close=(restore=false)=> {const closingId=panel?.id;token++;cancelHover();clearTimeout(timer);cleanup?.();cleanup=null;panel?.remove();panel=null;
    associate(trigger,closingId,false);if(restore&&trigger?.isConnected)trigger.focus();trigger=null;};
  const schedule=()=> {cancelHover();clearTimeout(timer);timer=setTimeout(()=>{if(panel&&!panel.matches(':hover')&&!panel.contains(document.activeElement)&&!trigger?.matches(':hover')&&document.activeElement!==trigger)close();},220);};
  const open=async(id,button,keyboard=false)=> {
    if(trigger===button&&panel) {clearTimeout(timer);if(keyboard)panel.querySelector('button').focus();return;}
    close(); const request=++token;trigger=button;
    panel=document.createElement('aside');panel.className='stv-detail stv-hover-detail';panel.id=`${root.id}-detail-${++sequence}`;
    panel.setAttribute('aria-label',`Details for ${id}`);panel.setAttribute('role','dialog');panel.tabIndex=-1;
    const dismiss=document.createElement('button');dismiss.textContent='Close details';dismiss.onclick=()=>close(true);
    const original=document.createElement('a');original.textContent='Open original object';original.href=new URL(graph.objects[id].url,base).href;original.target='_blank';original.rel='noopener noreferrer';
    const body=document.createElement('div');body.textContent='Loading detailsâ€¦';
    panel.append(dismiss,original,body);document.body.append(panel);associate(button,panel.id);
    panel.onmouseenter=()=>clearTimeout(timer);panel.onmouseleave=schedule;panel.onfocusout=schedule;
    panel.onkeydown=e=>{if(e.key==='Escape'){e.preventDefault();close(true);}};
    const position=()=>computePosition(button,panel,{strategy:'fixed',middleware:[offset(8),flip(),shift({padding:12}),size({padding:12,apply({availableWidth,availableHeight,elements}){Object.assign(elements.floating.style,{maxWidth:`${Math.max(180,availableWidth)}px`,maxHeight:`${Math.max(100,availableHeight)}px`});}})]}).then(({x,y})=>{if(panel&&request===token)Object.assign(panel.style,{left:`${x}px`,top:`${y}px`});});
    cleanup=autoUpdate(button,panel,position);if(keyboard)dismiss.focus();
    try {
      const html=await loadDetail(graph,id,base); if(request!==token)return;
      body.replaceChildren(detailContent(html,graph,id,base,`${panel.id}-`));position();
    }catch(error){if(request===token)body.textContent=error.message;}
  };
  const hover=(id,button)=> {
    clearTimeout(timer);
    if(trigger===button&&panel || hoverButton===button)return;
    cancelHover();hoverButton=button;
    hoverTimer=setTimeout(()=>{hoverButton=null;if(button.isConnected)open(id,button);},1000);
  };
  return {open,hover,close,schedule};
}
