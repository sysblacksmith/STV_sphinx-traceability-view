import {select} from 'd3-selection';
import {zoom,zoomIdentity} from 'd3-zoom';
import {initial,visible,transition,groupKey} from './state.js';
import {compute} from './layout.js';
import {inspector} from './inspect.js';
import {orderedGroups} from './groups.js';
const nodeKey=id=>JSON.stringify(['need',id]);
const rootKey=JSON.stringify(['project']);
function element(tag,cls,text) {const e=document.createElement(tag);if(cls)e.className=cls;if(text!==undefined)e.textContent=text;return e;}
function button(text,action,label=text) {const b=element('button','',text);b.type='button';b.setAttribute('aria-label',label);b.onclick=action;return b;}
export async function mount(root,graph,base,layout=compute) {
  if(graph.schema!==1)throw Error(`Unsupported STV schema ${graph.schema}`);
  let state=initial(JSON.parse(root.dataset.stvSeeds)),request=0,home=zoomIdentity,hasCommitted=false;
  const toolbar=element('div','stv-toolbar'),status=element('p','stv-status');status.setAttribute('role','status');
  const viewport=element('div','stv-viewport');viewport.tabIndex=0;viewport.setAttribute('aria-label','Trace graph viewport');
  const scene=element('div','stv-scene'),nodesLayer=element('div','stv-nodes');
  const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');svg.classList.add('stv-edges');svg.setAttribute('aria-hidden','true');
  scene.append(svg,nodesLayer);viewport.append(scene);root.replaceChildren(toolbar,status,viewport);
  const details=inspector(root,graph,base),nodeElements=new Map();
  root.addEventListener('keydown',e=>{if(e.key==='Escape')details.close();});
  const zoomer=zoom().scaleExtent([0.15,3]).filter(e=>e.type==='wheel'||(!e.button&&!e.target.closest('article,button,a')))
    .on('zoom',event=>{scene.style.transform=`translate(${event.transform.x}px,${event.transform.y}px) scale(${event.transform.k})`;details.close();});
  select(viewport).call(zoomer).on('dblclick.zoom',null);
  for(const [label,action] of [['Zoom in',()=>select(viewport).call(zoomer.scaleBy,1.25)],['Zoom out',()=>select(viewport).call(zoomer.scaleBy,0.8)],
    ['Pan left',()=>select(viewport).call(zoomer.translateBy,100,0)],['Pan right',()=>select(viewport).call(zoomer.translateBy,-100,0)],
    ['Pan up',()=>select(viewport).call(zoomer.translateBy,0,100)],['Pan down',()=>select(viewport).call(zoomer.translateBy,0,-100)]])toolbar.append(button(label,action));
  toolbar.append(button('Reset viewport',()=>select(viewport).call(zoomer.transform,home)));
  const retry=button('Retry layout',()=>update(null));retry.hidden=true;toolbar.append(retry);
  viewport.addEventListener('focusin',e=> {
    // Native Tab focus can scroll an overflow-hidden element. Fold that motion
    // into the same D3 transform rather than keeping a second viewport offset.
    if(viewport.scrollLeft||viewport.scrollTop) {
      const dx=-viewport.scrollLeft,dy=-viewport.scrollTop,k=viewport.__zoom.k;
      viewport.scrollLeft=0;viewport.scrollTop=0;
      select(viewport).call(zoomer.translateBy,dx/k,dy/k);
    }
    const rect=e.target.getBoundingClientRect(),view=viewport.getBoundingClientRect();
    const dx=rect.left<view.left?view.left-rect.left+20:rect.right>view.right?view.right-rect.right-20:0;
    const dy=rect.top<view.top?view.top-rect.top+20:rect.bottom>view.bottom?view.bottom-rect.bottom-20:0;
    if(dx||dy){const k=viewport.__zoom.k;select(viewport).call(zoomer.translateBy,dx/k,dy/k);}
  });
  function makeNode(key,s) {
    const id=key===rootKey?null:JSON.parse(key)[1],object=graph.objects[id];
    const node=element('article','stv-node');node.dataset.key=key;
    if(id===null) {
      node.classList.add('stv-project');node.append(element('strong','',graph.project));
      if(!graph.entries.length)node.append(element('p','','No stakeholder requirements.'));
      else {
        const expand=button(s.rootOpen?'−':'+',()=>update({type:'root'}),'Toggle stakeholder requirements');expand.setAttribute('aria-expanded',String(s.rootOpen));expand.dataset.focus='root';node.append(expand);
        if(s.rootOpen) {
          const pages=Math.ceil(graph.entries.length/50);
          node.append(element('p','',`Page ${s.page+1} of ${pages} / ${graph.entries.length} stakeholder requirements`));
          for(const [label,page] of [['Previous',s.page-1],['Next',s.page+1]]) {
            const unavailable=page<0||page>=pages;
            const control=button(label,()=>{if(!unavailable)update({type:'page',page});},`${label} stakeholder page`);control.setAttribute('aria-disabled',String(unavailable));control.dataset.focus=label;node.append(control);
          }
        }
      }
    } else if(!object) {
      node.classList.add('stv-missing');node.append(element('strong','',id),element('p','','Missing object'));
    } else {
      const type=graph.model.types[object.type];node.style.backgroundColor=type.color;
      if(!object.status||!graph.model.accepted_statuses.includes(object.status))node.classList.add('stv-unaccepted');
      const link=element('a','stv-summary');link.href=new URL(object.url,base).href;link.target='_blank';link.rel='noopener noreferrer';
      link.append(element('strong','stv-id',id),element('span','stv-title',object.title));node.append(link);
      const controls=element('div','stv-groups');
      for(const {direction,relation,targets} of orderedGroups(graph,id)) {
        const key=groupKey(id,relation,direction),open=s.expanded.has(key);
        const label=`${graph.model.relations[relation][direction]} (${direction})`;
        const control=button(`${open?'−':'+'} ${label} (${targets.length})`,()=>update({type:'group',id,relation,direction}),`${open?'Collapse':'Expand'} ${label} for ${id}`);
        control.dataset.focus=key;control.setAttribute('aria-expanded',String(open));controls.append(control);
      }
      if(!controls.children.length)controls.append(element('span','','No relationships'));
      node.append(controls);
      const inspect=button('Details',()=>details.open(id,inspect,true),`Details for ${id}`);inspect.dataset.focus='details';
      inspect.onmouseenter=()=>details.hover(id,inspect);
      inspect.onkeydown=e=>{if(e.key==='Escape')details.close(true);};
      node.onmouseenter=()=>details.hover(id,inspect);node.onmouseleave=details.schedule;
      node.append(inspect);
    }
    return node;
  }
  async function update(command) {
    const result=command?transition(graph,state,command):{state,graph:visible(graph,state)};
    if(result.error){status.textContent=result.error;return;}
    const ticket=++request;root.setAttribute('aria-busy','true');status.textContent='Laying out graph…';
    const focused=document.activeElement,focusNode=focused?.closest('.stv-node');
    let focusKey=focusNode?.dataset.key,focusControl=focused?.dataset.focus;
    const initiatingKey=focusKey,initiatingControl=focusControl;
    const staged=new Map(),measure=element('div','stv-measure');root.append(measure);
    const keys=result.graph.ids.map(nodeKey);if(result.graph.project)keys.unshift(rootKey);
    const boxes=new Map();
    for(const key of keys){const n=makeNode(key,result.state);n.style.position='relative';measure.append(n);staged.set(key,n);boxes.set(key,Math.ceil(n.getBoundingClientRect().height));}
    try {
      const geometry=await layout(graph,result.graph,boxes);
      if(ticket!==request)return;
      const active=document.activeElement;
      const ownPanel=active?.closest('.stv-detail')?.id.startsWith(root.id+'-detail-');
      const restoreFocus=root.contains(active)||ownPanel;
      if(command?.type!=='page'&&root.contains(active)) {
        focusKey=active.closest('.stv-node')?.dataset.key;focusControl=active.dataset.focus;
      }
      details.close();state=result.state;
      for(const [key,old] of nodeElements)if(!staged.has(key)){old.remove();nodeElements.delete(key);}
      for(const [key,n] of staged) {
        let target=nodeElements.get(key);
        // Preserve element identity across layouts so focus can be restored precisely.
        if(target) {target.replaceChildren(...n.childNodes);target.className=n.className;target.style.cssText=n.style.cssText;target.onmouseenter=n.onmouseenter;target.onmouseleave=n.onmouseleave;}
        else {target=n;nodesLayer.append(target);nodeElements.set(key,target);}
        const box=geometry.nodes.get(key);Object.assign(target.style,{position:'absolute',left:`${box.x}px`,top:`${box.y}px`});
      }
      svg.replaceChildren();svg.setAttribute('width',geometry.width);svg.setAttribute('height',geometry.height);
      const defs=document.createElementNS(svg.namespaceURI,'defs'),marker=document.createElementNS(svg.namespaceURI,'marker');
      marker.id=`${root.id}-arrow`;for(const [k,v] of Object.entries({viewBox:'0 0 10 10',refX:9,refY:5,markerWidth:7,markerHeight:7,orient:'auto-start-reverse'}))marker.setAttribute(k,v);
      const arrow=document.createElementNS(svg.namespaceURI,'path');arrow.setAttribute('d','M 0 0 L 10 5 L 0 10 z');arrow.setAttribute('fill','#536174');marker.append(arrow);defs.append(marker);svg.append(defs);
      for(const edge of geometry.edges){const path=document.createElementNS(svg.namespaceURI,'polyline');path.setAttribute('points',edge.points.map(p=>p.join(',')).join(' '));path.setAttribute('marker-end',`url(#${marker.id})`);const title=document.createElementNS(svg.namespaceURI,'title');title.textContent=edge.edge[1];path.append(title);svg.append(path);}
      scene.style.width=`${geometry.width}px`;scene.style.height=`${geometry.height}px`;
      home=zoomIdentity.translate(0,30-Math.min(...[...geometry.nodes.values()].map(n=>n.y)));
      if(!hasCommitted){select(viewport).call(zoomer.transform,home);hasCommitted=true;}
      root.dataset.stvRevision=String(state.revision);status.textContent=`${keys.length} visible ${keys.length===1?'node':'nodes'}`;retry.hidden=true;
      if(focusKey&&restoreFocus){const owner=nodeElements.get(focusKey),initiator=nodeElements.get(initiatingKey);const match=owner&&[...owner.querySelectorAll('button,a')].find(e=>e.dataset.focus===focusControl&&!e.disabled);const fallback=initiator&&[...initiator.querySelectorAll('button,a')].find(e=>e.dataset.focus===initiatingControl&&!e.disabled);(match||owner?.querySelector('button,a')||fallback||toolbar.querySelector('button')).focus();}
    }catch(error){if(ticket===request){status.textContent=`Layout failed: ${error.message}`;retry.hidden=false;
      if(!nodeElements.size){let y=20;for(const [key,n]of staged){Object.assign(n.style,{position:'absolute',left:'20px',top:`${y}px`});y+=boxes.get(key)+20;nodesLayer.append(n);nodeElements.set(key,n);}}}}
    finally{measure.remove();if(ticket===request)root.setAttribute('aria-busy','false');}
  }
  await update(null);
}
