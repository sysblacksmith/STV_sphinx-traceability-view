/* Page-wide Sphinx-Needs metadata controls. No product extension required. */
(()=>{
const initialized=new WeakSet();
function setRows(rows,icons,open){
  rows.forEach(r=>r.classList.toggle('collapse_is_hidden',!open));
  icons.forEach(i=>i.classList.toggle('collapse_is_hidden',i.classList.contains('collapsed')?!open:open));
}
function initializePageMetadata(documentRoot=document) {
  if(initialized.has(documentRoot)||documentRoot.querySelector('.stv-page-metadata,.method-page-metadata'))return;
  const tables=[...documentRoot.querySelectorAll('table.need')].filter(t=>!t.closest('.stv-view,.stv-detail'));
  if(!tables.length)return;
  initialized.add(documentRoot);
  const disclosures=[];
  let rowSequence=0;
  const ownerDocument=documentRoot.ownerDocument||documentRoot;
  const freshRowId=()=>{let id;do{id=`method-host-row-${++rowSequence}`;}while(ownerDocument.getElementById(id));return id;};
  const missingHost=typeof window.jQuery!=='function';
  let unsupported=missingHost;
  for(const table of tables)for(const control of table.querySelectorAll('.needs_collapse')){
    if(control.closest('table.need')!==table)continue;
    if(missingHost)continue;
    const classes=control.id.split('__').slice(2);
    const rows=[...table.querySelectorAll('tr')].filter(r=>r.closest('table.need')===table&&classes.some(c=>r.classList.contains(c)));
    if(!rows.length||rows.some(row=>row.classList.contains('head')||row.classList.contains('content'))){unsupported=true;continue;}
    const icons=[...control.querySelectorAll('span.needs.collapsed,span.needs.visible')];
    const sync=()=>{
      const open=rows.every(r=>!r.classList.contains('collapse_is_hidden'));
      control.setAttribute('aria-expanded',String(open));control.setAttribute('aria-label',`${open?'Hide':'Show'} artifact metadata`);
      rows.forEach(r=>{if(!r.id)r.id=freshRowId();});control.setAttribute('aria-controls',rows.map(r=>r.id).join(' '));
    };
    const set=open=>{
      const states=rows.map(r=>!r.classList.contains('collapse_is_hidden'));
      if(states.every(s=>s===open)){sync();return;}
      if(states.every(s=>s===states[0]))icons.find(i=>!i.classList.contains('collapse_is_hidden'))?.click();
      setRows(rows,icons,open);sync();
    };
    control.setAttribute('role','button');control.tabIndex=0;
    control.addEventListener('keydown',event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();icons.find(i=>!i.classList.contains('collapse_is_hidden'))?.click();sync();}});
    icons.forEach(icon=>icon.addEventListener('click',sync));sync();disclosures.push({set});
  }
  const group=documentRoot.createElement('div');group.className='method-page-metadata';group.setAttribute('role','group');group.setAttribute('aria-label','Need attributes on this page');
  for(const [label,open] of [['Collapse all',false],['Expand all',true]]){const button=documentRoot.createElement('button');button.type='button';button.textContent=label;button.disabled=!disclosures.length||unsupported;button.addEventListener('click',()=>disclosures.forEach(d=>d.set(open)));group.append(button);}
  if(!disclosures.length||unsupported){const text=documentRoot.createElement('span');text.textContent=missingHost?'Page-wide controls unavailable: host metadata handlers unavailable. Reload to retry.':unsupported?'Page-wide controls unavailable: unsupported Need disclosure markup.':'No collapsible Need attributes on this page.';group.append(text);}
  tables[0].parentNode.insertBefore(group,tables[0]);
}
function schedulePageMetadata(){
  const ready=()=>{if(typeof window.jQuery==='function')window.jQuery(()=>setTimeout(()=>initializePageMetadata(),0));else setTimeout(()=>initializePageMetadata(),0);};
  if(document.readyState==='complete')ready();else window.addEventListener('load',ready,{once:true});
}

schedulePageMetadata();
})();
