import {detailURL,detailCSS} from './urls.js';
const promises=new Map();
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

export function detailContent(html,graph,id,base,prefix) {
      const template=document.createElement('template');template.innerHTML=html;
      const ids=new Map();
      template.content.querySelectorAll('[id]').forEach(el=>{ids.set(el.id,prefix+el.id);el.id=prefix+el.id;});
      template.content.querySelectorAll('*').forEach(el=> {
        const css=value=>detailCSS(value,base);
        if(el.hasAttribute('data-stv-style'))el.setAttribute('style',css(el.getAttribute('data-stv-style')));
        if(el.hasAttribute('data-stv-css'))el.textContent=css(el.getAttribute('data-stv-css'));
        for(const attr of ['href','src','poster','xlink:href']) {
          const value=el.getAttribute(`data-stv-${attr.replace(':','-')}`);
          if(value!==null) {
            const url=detailURL(value,base,{image:attr!=='href'});
            if(!url) {el.removeAttribute(attr);continue;}
            const fragment=typeof url==='string'?'':decodeURIComponent(url.hash.slice(1));
            if(attr==='href'&&!el.closest('.needs-id')&&ids.has(fragment)&&url.pathname===new URL(graph.objects[id].url,base).pathname) el.setAttribute(attr,'#'+ids.get(fragment));
            else el.setAttribute(attr,String(url));
          }
        }
        if(el.hasAttribute('data-stv-srcset')) {
          const sources=[...el.getAttribute('data-stv-srcset').matchAll(/\s*(data:[^\s]+|[^,\s]+)(?:\s+([0-9.]+[wx]))?\s*(?:,|$)/g)];
          const safe=sources.flatMap(([,u,d])=>{const target=detailURL(u.replace(/,$/,''),base,{image:true});return target?[[String(target),d||''].join(' ').trim()]:[];});
          if(safe.length)el.setAttribute('srcset',safe.join(', '));else el.removeAttribute('srcset');
        }
        for(const attr of ['for','aria-labelledby','aria-describedby','headers','aria-controls']) if(el.hasAttribute(attr))el.setAttribute(attr,el.getAttribute(attr).split(/\s+/).map(v=>ids.get(v)||v).join(' '));
      });
  for(const link of template.content.querySelectorAll('.needs-id a[href]')) {
    link.target='_blank';link.rel='noopener noreferrer';
  }
  initializeMetadata(template.content,prefix);
  return template.content;
}

export function associate(button,id,add=true) {
  if(!button||!id)return;
  const ids=new Set((button.getAttribute('aria-controls')||'').split(/\s+/).filter(Boolean));
  if(add)ids.add(id);else ids.delete(id);
  if(ids.size)button.setAttribute('aria-controls',[...ids].join(' '));else button.removeAttribute('aria-controls');
}

/** Host document-ready handlers do not initialize lazily inserted fragments. */
function initializeMetadata(fragment,prefix) {
  const occupied=new Set([...fragment.querySelectorAll('[id]')].map(node=>node.id));
  let sequence=0;
  const freshId=()=>{let id;do{id=`${prefix}metadata-${++sequence}`;}while(occupied.has(id));occupied.add(id);return id;};
  for(const control of fragment.querySelectorAll('.needs_collapse')) {
    const encoded=control.id.startsWith(prefix)?control.id.slice(prefix.length):control.id;
    const classes=encoded.split('__').slice(2);
    const table=control.closest('table.need');
    const rows=table?[...table.querySelectorAll('tr')].filter(row=>row.closest('table.need')===table&&classes.some(name=>row.classList.contains(name))):[];
    if(!rows.length){control.hidden=true;continue;}
    control.id=freshId();control.setAttribute('role','button');control.tabIndex=0;
    for(const row of rows)if(!row.id)row.id=freshId();
    control.setAttribute('aria-controls',rows.map(row=>row.id).join(' '));
    const set=open=> {
      control.setAttribute('aria-expanded',String(open));
      control.setAttribute('aria-label',`${open?'Hide':'Show'} artifact metadata`);
      for(const row of rows){row.hidden=!open;row.classList.toggle('collapse_is_hidden',!open);}
      for(const icon of control.querySelectorAll('.needs.collapsed, .needs.visible')) {
        const hidden=icon.classList.contains('collapsed')?!open:open;
        icon.hidden=hidden;icon.classList.toggle('collapse_is_hidden',hidden);
      }
    };
    const toggle=()=>set(control.getAttribute('aria-expanded')!=='true');
    control.addEventListener('click',event=>{event.preventDefault();toggle();});
    control.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();toggle();}});
    set(false);
  }
}
