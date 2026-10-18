import {computePosition,autoUpdate,offset,flip,shift,size} from '@floating-ui/dom';
const promises=new Map();
let sequence=0;
export function loadDetail(graph,id,base) {
  const key=JSON.stringify([graph.identity,id]);
  if(!promises.has(key)) promises.set(key,new Promise((resolve,reject)=> {
    const detail=graph.details[id],script=document.createElement('script');
    if(globalThis.__STV_DATA__.fragments[detail.digest]) {resolve(globalThis.__STV_DATA__.fragments[detail.digest]);return;}
    script.src=new URL(detail.url,base).href;
    script.onload=()=>{const html=globalThis.__STV_DATA__.fragments[detail.digest];html===undefined?reject(Error('Detail registration unavailable.')):resolve(html);script.remove();};
    script.onerror=()=>{reject(Error('Local detail asset unavailable.'));script.remove();promises.delete(key);};
    document.head.append(script);
  }));
  return promises.get(key);
}
export function inspector(root,graph,base) {
  let panel,cleanup,trigger,timer,hoverTimer,hoverButton,token=0;
  const cancelHover=()=> {clearTimeout(hoverTimer);hoverButton=null;};
  const close=(restore=false)=> {token++;cancelHover();clearTimeout(timer);cleanup?.();cleanup=null;panel?.remove();panel=null;
    trigger?.removeAttribute('aria-controls');if(restore&&trigger?.isConnected)trigger.focus();trigger=null;};
  const schedule=()=> {cancelHover();clearTimeout(timer);timer=setTimeout(()=>{if(panel&&!panel.matches(':hover')&&!panel.contains(document.activeElement)&&!trigger?.matches(':hover')&&document.activeElement!==trigger)close();},220);};
  const open=async(id,button,keyboard=false)=> {
    if(trigger===button&&panel) {clearTimeout(timer);if(keyboard)panel.querySelector('button').focus();return;}
    close(); const request=++token;trigger=button;
    panel=document.createElement('aside');panel.className='stv-detail';panel.id=`${root.id}-detail-${++sequence}`;
    panel.setAttribute('aria-label',`Details for ${id}`);panel.setAttribute('role','dialog');panel.tabIndex=-1;
    const dismiss=document.createElement('button');dismiss.textContent='Close details';dismiss.onclick=()=>close(true);
    const original=document.createElement('a');original.textContent='Open original object';original.href=new URL(graph.objects[id].url,base).href;original.target='_blank';original.rel='noopener noreferrer';
    const body=document.createElement('div');body.textContent='Loading details…';
    panel.append(dismiss,original,body);document.body.append(panel);button.setAttribute('aria-controls',panel.id);
    panel.onmouseenter=()=>clearTimeout(timer);panel.onmouseleave=schedule;panel.onfocusout=schedule;
    panel.onkeydown=e=>{if(e.key==='Escape'){e.preventDefault();close(true);}};
    const position=()=>computePosition(button,panel,{strategy:'fixed',middleware:[offset(8),flip(),shift({padding:12}),size({padding:12,apply({availableWidth,availableHeight,elements}){Object.assign(elements.floating.style,{maxWidth:`${Math.max(180,availableWidth)}px`,maxHeight:`${Math.max(100,availableHeight)}px`});}})]}).then(({x,y})=>{if(panel&&request===token)Object.assign(panel.style,{left:`${x}px`,top:`${y}px`});});
    cleanup=autoUpdate(button,panel,position);if(keyboard)dismiss.focus();
    try {
      const html=await loadDetail(graph,id,base); if(request!==token)return;
      const template=document.createElement('template');template.innerHTML=html;
      const prefix=`${panel.id}-`,ids=new Map();
      template.content.querySelectorAll('[id]').forEach(el=>{ids.set(el.id,prefix+el.id);el.id=prefix+el.id;});
      template.content.querySelectorAll('*').forEach(el=> {
        const css=value=>value.replace(/url\("([^\"]*)"\)/gi,(_,url)=>`url("${new URL(url,base).href}")`);
        if(el.hasAttribute('data-stv-style'))el.setAttribute('style',css(el.getAttribute('data-stv-style')));
        if(el.hasAttribute('data-stv-css'))el.textContent=css(el.getAttribute('data-stv-css'));
        for(const attr of ['href','src','poster','xlink:href']) {
          const value=el.getAttribute(`data-stv-${attr.replace(':','-')}`);
          if(value!==null) {
            const url=new URL(value,base),fragment=decodeURIComponent(url.hash.slice(1));
            if(attr==='href'&&ids.has(fragment)&&url.pathname===new URL(graph.objects[id].url,base).pathname) el.setAttribute(attr,'#'+ids.get(fragment));
            else el.setAttribute(attr,url.href);
          }
        }
        if(el.hasAttribute('data-stv-srcset')) {
          const sources=[...el.getAttribute('data-stv-srcset').matchAll(/\s*(data:[^\s]+|[^,\s]+)(?:\s+([0-9.]+[wx]))?\s*(?:,|$)/g)];
          el.setAttribute('srcset',sources.map(([,u,d])=>[new URL(u.replace(/,$/,''),base).href,d||''].join(' ').trim()).join(', '));
        }
        for(const attr of ['for','aria-labelledby','aria-describedby','headers','aria-controls']) if(el.hasAttribute(attr))el.setAttribute(attr,el.getAttribute(attr).split(/\s+/).map(v=>ids.get(v)||v).join(' '));
      });
      body.replaceChildren(template.content);position();
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
