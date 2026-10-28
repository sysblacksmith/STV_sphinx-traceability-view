import {initial,visible,PAGE_SIZE} from './state.js';
export const storageKey=(base,project,path,id,seeds)=>'stv:view:1:'+JSON.stringify([String(base),project,path,id,seeds]);
const validList=value=>Array.isArray(value)&&value.length<=10000&&value.every(x=>typeof x==='string'&&x.length<=10000);
const validTransform=t=>t&&[t.x,t.y,t.k].every(Number.isFinite)&&Math.abs(t.x)<=1e8&&Math.abs(t.y)<=1e8&&t.k>=.15&&t.k<=3;
/** Browser data is untrusted. Only the current published graph grants visibility. */
export function restoreSnapshot(raw,graph) {
  const data=JSON.parse(raw),saved=data?.state;
  if(data?.version!==1||!saved||!['seeds','project'].includes(saved.mode)||!validList(saved.seeds)||!validList(saved.expanded)||
    !Array.isArray(saved.pages)||saved.pages.length>10000||!Number.isInteger(saved.page)||saved.page<0||typeof saved.rootOpen!=='boolean'||
    !validList(data.cards)||!validTransform(data.transform))throw Error('Invalid remembered view; using normal startup.');
  const exists=id=>Object.hasOwn(graph.objects,id);
  const groups=list=>{
    if(!validList(list))throw Error('Invalid remembered expansion state.');
    return new Set(list.filter(key=>{
      let tuple;try{tuple=JSON.parse(key);}catch{return false;}
      return Array.isArray(tuple)&&tuple.length===3&&tuple.every(x=>typeof x==='string')&&exists(tuple[0])&&
        ['incoming','outgoing'].includes(tuple[2])&&Object.hasOwn(graph.adjacency[tuple[0]]?.[tuple[2]]||{},tuple[1]);
    }));
  };
  const seeds=[...new Set(saved.seeds.filter(exists))];
  if(saved.mode==='seeds'&&!seeds.length||saved.mode==='project'&&saved.page>=Math.max(1,Math.ceil(graph.entries.length/PAGE_SIZE)))
    throw Error('Remembered starting context is unavailable; using normal startup.');
  const state={...initial(saved.mode==='seeds'?seeds:[]),page:saved.page,rootOpen:saved.rootOpen,expanded:groups(saved.expanded)};
  for(const entry of saved.pages){
    if(!Array.isArray(entry)||entry.length!==2||!Number.isInteger(entry[0])||entry[0]<0)throw Error('Invalid remembered page memory.');
    const expanded=groups(entry[1]);
    if(entry[0]<Math.ceil(graph.entries.length/PAGE_SIZE))state.pages.set(entry[0],expanded);
  }
  visible(graph,state); // Enforce rooted reachability and the ordinary 200-node cap.
  const cards=[...new Set(data.cards.filter(exists))].slice(-(graph.details_limit??10));
  return {state,cards,transform:data.transform,geometry:data.geometry};
}
export const geometrySignature=(graph,view)=>JSON.stringify([view.ids,view.edges,view.entries,view.project,graph.model]);
export function snapshot(graph,state,cards,transform,geometry) {
  return {version:1,state:{mode:state.mode,seeds:state.seeds,expanded:[...state.expanded],pages:[...state.pages].map(([page,set])=>[page,[...set]]),page:state.page,rootOpen:state.rootOpen},cards,
    transform:{x:transform.x,y:transform.y,k:transform.k},geometry:{signature:geometrySignature(graph,visible(graph,state)),bandTops:[...(geometry.bandTops||[])],nodes:[...geometry.nodes].map(([key,n])=>[key,{...n,rank:geometry.ranks.get(key)}])}};
}
/** Access lazily: even the localStorage property getter may throw. */
export function rememberedStorage(getStorage,key) {
  return {read:()=>getStorage().getItem(key),write:data=>getStorage().setItem(key,JSON.stringify(data)),clear:()=>getStorage().removeItem(key)};
}
/** Reuse positions only with current semantic/dimension/topology identity. */
export function restorePositions(saved,graph,view,nodes,ranks,bands=[]) {
  if(!saved||saved.signature!==geometrySignature(graph,view)||!Array.isArray(saved.nodes)||saved.nodes.length!==nodes.size)return;
  const positions=new Map(saved.nodes);
  if(positions.size!==nodes.size)return;
  for(const [key,n] of nodes){
    const p=positions.get(key);
    if(!p||![p.x,p.y,p.width,p.height].every(Number.isFinite)||Math.abs(p.x)>1e7||Math.abs(p.y)>1e7||p.width!==n.width||p.height!==n.height||p.rank!==ranks.get(key))return;
  }
  const tops=new Map(Array.isArray(saved.bandTops)?saved.bandTops:[]);
  for(const band of bands){
    const top=tops.get(band.rank);
    if(!Number.isFinite(top)||Math.abs(top)>1e7||band.normal.some(key=>positions.get(key).y!==top)||band.tests.some(key=>positions.get(key).y<top))return;
  }
  for(const [key,n] of nodes)Object.assign(n,{x:positions.get(key).x,y:positions.get(key).y});
  for(const band of bands)band.top=tops.get(band.rank);
}
