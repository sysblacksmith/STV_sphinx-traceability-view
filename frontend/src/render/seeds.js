/** Local-only catalog; the graph already excludes host-hidden objects. */
export function seedCatalog(graph) {
  return Object.entries(graph.objects).map(([id,object])=>({id,title:object.title||'',
    search:(id+' '+(object.title||'')).toLowerCase()})).sort((a,b)=>a.id.localeCompare(b.id));
}
export function seedMatches(catalog,query,limit=10) {
  const q=query.trim().toLowerCase();
  if(!q)return {items:[],total:0};
  const matches=catalog.filter(item=>item.search.includes(q));
  return {items:matches.slice(0,limit),total:matches.length};
}
export function seedPicker(root,graph,onSeed,onOverview) {
  const make=(tag,cls,text)=>{const el=document.createElement(tag);if(cls)el.className=cls;if(text)el.textContent=text;return el;};
  const form=make('form','stv-seed-picker'),label=make('label','','Starting Need'),input=make('input');
  input.id=root.id+'-seed-input';label.htmlFor=input.id;input.type='text';input.autocomplete='off';
  input.placeholder='Need ID or title';input.setAttribute('role','combobox');input.setAttribute('aria-autocomplete','list');
  const list=make('ul','stv-seed-matches');list.id=root.id+'-seed-matches';list.setAttribute('role','listbox');list.hidden=true;
  input.setAttribute('aria-controls',list.id);input.setAttribute('aria-expanded','false');
  const hint=make('span','stv-seed-hint','Type an ID or title; choose a match or enter an exact ID.');
  hint.id=root.id+'-seed-hint';hint.setAttribute('role','status');input.setAttribute('aria-describedby',hint.id);
  const start=make('button','','Start at Need');start.type='submit';
  const overview=make('button','','Project overview');overview.type='button';
  const catalog=seedCatalog(graph);let items=[],active=-1;
  const close=()=>{list.hidden=true;input.setAttribute('aria-expanded','false');input.removeAttribute('aria-activedescendant');active=-1;};
  const confirm=id=> {
    id=id.trim();
    if(!id||!Object.hasOwn(graph.objects,id)) {
      input.setAttribute('aria-invalid','true');hint.textContent='Choose a matching Need or enter an exact existing ID. The view is unchanged.';return;
    }
    input.value=id;input.removeAttribute('aria-invalid');close();onSeed(id);
  };
  const render=()=> {
    const result=seedMatches(catalog,input.value);items=result.items;active=-1;list.replaceChildren();
    input.removeAttribute('aria-invalid');input.removeAttribute('aria-activedescendant');
    hint.textContent=input.value.trim()?`${result.total} matches${result.total>items.length?`; showing the first ${items.length}, refine your search`:''}.`:'Type an ID or title; choose a match or enter an exact ID.';
    for(const [index,item] of items.entries()) {
      const option=make('li','',item.id+' — '+item.title);option.id=list.id+'-'+index;option.setAttribute('role','option');option.setAttribute('aria-selected','false');
      option.onmousedown=e=>e.preventDefault();option.onclick=()=>confirm(item.id);list.append(option);
    }
    list.hidden=!items.length;input.setAttribute('aria-expanded',String(Boolean(items.length)));
  };
  input.oninput=render;
  input.onkeydown=e=> {
    if(e.key==='Escape'){close();return;}
    if(e.key==='ArrowDown'||e.key==='ArrowUp') {
      e.preventDefault();if(list.hidden)render();if(!items.length)return;
      active=active<0?(e.key==='ArrowDown'?0:items.length-1):(active+(e.key==='ArrowDown'?1:-1)+items.length)%items.length;
      [...list.children].forEach((el,index)=>el.setAttribute('aria-selected',String(index===active)));
      input.setAttribute('aria-activedescendant',list.children[active].id);list.children[active].scrollIntoView({block:'nearest'});
    }
  };
  input.onblur=close;
  form.onsubmit=e=>{e.preventDefault();confirm(active>=0?items[active].id:input.value);};
  overview.onclick=()=>{close();input.removeAttribute('aria-invalid');input.value='';onOverview();};
  form.append(label,input,start,overview,hint,list);return form;
}
