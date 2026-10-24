import ELK from 'elkjs/lib/elk.bundled.js';
import {stabilize} from './stability.js';
import {levelIndex} from './level.js';
const elk = new ELK();
const idOrder=new Intl.Collator('en',{numeric:true,sensitivity:'variant'});
// Open rectangle intersection: touching a boundary does not obscure a box.
export function crossesBox(p,q,n) {
  let low=0,high=1;
  for(const [axis,min,max] of [[0,n.x,n.x+n.width],[1,n.y,n.y+n.height]]) {
    const delta=q[axis]-p[axis];
    if(!delta) {if(p[axis]<=min||p[axis]>=max)return false;continue;}
    const a=(min-p[axis])/delta,b=(max-p[axis])/delta;
    low=Math.max(low,Math.min(a,b));high=Math.min(high,Math.max(a,b));
  }
  return low<high && high>0 && low<1;
}
/** ELK proposes ordering; domain bands own final geometry. */
export async function compute(graph, visible, boxes, context={}) {
  const rootKey = JSON.stringify(['project']);
  const keys = visible.ids.map(id => JSON.stringify(['need', id]));
  const objects = new Map(visible.ids.map(id => [JSON.stringify(['need', id]), id]));
  if (visible.project) keys.unshift(rootKey);
  const layout = await elk.layout({id: 'scene', layoutOptions: {
    'elk.algorithm': 'layered', 'elk.direction': 'DOWN', 'elk.randomSeed': '1'},
    children: keys.map(id => ({id, width:280, height:boxes.get(id) || 160})),
    edges: visible.edges.filter(([a,,b])=>graph.objects[a] && graph.objects[b]).map(([a,r,b],i)=>({id:String(i),sources:[JSON.stringify(['need',a])],targets:[JSON.stringify(['need',b])]}))});
  const suggestions = new Map(layout.children.map(n=>[n.id,n.x]));
  const levels = graph.model.levels;
  const ranks = new Map();
  for(const key of keys) {
    const id=objects.get(key), object=graph.objects[id];
    if(key===rootKey) {ranks.set(key,-1);continue;}
    if(object && graph.model.types[object.type].role!=='test') ranks.set(key,levelIndex(graph,id));
  }
  for(const key of keys.filter(k=>!ranks.has(k))) {
    const id=objects.get(key), connected=[];
    for(const [a,,b] of visible.edges) {
      const other=a===id?b:b===id?a:null;
      if(other!==null && ranks.has(JSON.stringify(['need',other]))) connected.push(ranks.get(JSON.stringify(['need',other])));
    }
    connected.sort((a,b)=>a-b);
    ranks.set(key,connected.length?connected[Math.floor((connected.length-1)/2)]:0);
  }
  const nodes=new Map(); let y=30;
  const bands=[];
  for(let rank=-1;rank<levels.length;rank++) {
    const band=keys.filter(k=>ranks.get(k)===rank);
    const normal=band.filter(k=>graph.model.types[graph.objects[objects.get(k)]?.type]?.role!=='test');
    const tests=band.filter(k=>!normal.includes(k));
    // Before any relationships are expanded, crossing minimization provides no
    // useful order. Present independent seed/project-entry rows by natural ID.
    normal.sort((a,b)=>!visible.edges.length
      ? idOrder.compare(objects.get(a)||a,objects.get(b)||b) || a.localeCompare(b,'en')
      : (suggestions.get(a)-suggestions.get(b)) || a.localeCompare(b));
    let x=30, height=0;
    for(const key of normal) {const h=boxes.get(key)||160;nodes.set(key,{x,y,width:280,height:h});x+=328;height=Math.max(height,h);}
    bands.push({rank,y,normal,tests,height}); y+=Math.max(height,40)+100;
  }
  // Geometric parenthood follows semantic rank, not authored link direction.
  const children=new Map();
  const connect=(parent,child)=> {
    if(!children.has(parent))children.set(parent,new Set());
    children.get(parent).add(child);
  };
  for(const [a,,b] of visible.edges) {
    const ka=JSON.stringify(['need',a]),kb=JSON.stringify(['need',b]);
    const ta=graph.model.types[graph.objects[a]?.type],tb=graph.model.types[graph.objects[b]?.type];
    if(!ta||!tb||ta.role==='test'||tb.role==='test')continue;
    if(ranks.get(ka)<ranks.get(kb))connect(ka,kb);
    else if(ranks.get(kb)<ranks.get(ka))connect(kb,ka);
  }
  if(visible.project)for(const id of visible.entries||[])connect(rootKey,JSON.stringify(['need',id]));
  for(const band of [...bands].reverse()) {
    const desired=new Map(band.normal.map(key=> {
      const boxes=[...(children.get(key)||[])].map(k=>nodes.get(k));
      const x=boxes.length?(Math.min(...boxes.map(n=>n.x))+Math.max(...boxes.map(n=>n.x+n.width)))/2-140:nodes.get(key).x;
      return [key,x];
    }));
    band.normal.sort((a,b)=>desired.get(a)-desired.get(b));
    // Least-displacement separation: pool only competing desired positions.
    // Subtracting the gap turns spacing into a nondecreasing sequence problem.
    const pools=[];
    for(const [index,key] of band.normal.entries()) {
      pools.push({first:index,last:index,sum:desired.get(key)-index*328,count:1});
      while(pools.length>1) {
        const a=pools.at(-2),b=pools.at(-1);
        if(a.sum/a.count<=b.sum/b.count)break;
        pools.splice(-2,2,{first:a.first,last:b.last,sum:a.sum+b.sum,count:a.count+b.count});
      }
    }
    for(const pool of pools)for(let index=pool.first;index<=pool.last;index++)
      nodes.get(band.normal[index]).x=pool.sum/pool.count+index*328;
  }
  const normalize=Math.max(0,30-Math.min(...[...nodes.values()].map(n=>n.x)));
  for(const node of nodes.values())node.x+=normalize;
  const right=Math.max(30,...[...nodes.values()].map(n=>n.x+n.width))+96;
  // A stacked test lane can increase a band height; shift subsequent bands together.
  let shift=0;
  for(const band of bands) {
    band.top=band.y+shift;
    for(const key of band.normal) nodes.get(key).y+=shift;
    let ty=band.y+shift;
    for(const key of band.tests.sort()) {const h=boxes.get(key)||160;nodes.set(key,{x:right,y:ty,width:280,height:h});ty+=h+24;}
    shift+=Math.max(0,ty-(band.y+shift)-24-band.height);
  }
  stabilize(nodes,ranks,bands,context.previous,context.anchor);
  const maxRight=Math.max(...[...nodes.values()].map(n=>n.x+n.width));
  const rankBounds = new Map();
  for(const [key,node] of nodes) {
    const rank=ranks.get(key),bounds=rankBounds.get(rank)||{top:Infinity,bottom:-Infinity};
    bounds.top=Math.min(bounds.top,node.y);bounds.bottom=Math.max(bounds.bottom,node.y+node.height);rankBounds.set(rank,bounds);
  }
  const edges=visible.edges.map(edge=>({edge,source:JSON.stringify(['need',edge[0]]),target:JSON.stringify(['need',edge[2]])}));
  if(visible.project) for(const id of visible.entries || [])
    edges.push({edge:[null,'entry',id],source:rootKey,target:JSON.stringify(['need',id])});
  edges.forEach((e,i)=> {
    const a=nodes.get(e.source),b=nodes.get(e.target);
    const above=b.y+b.height<=a.y,below=a.y+a.height<=b.y;
    const direct=above?[[a.x+a.width/2,a.y],[b.x+b.width/2,b.y+b.height]]:
      below?[[a.x+a.width/2,a.y+a.height],[b.x+b.width/2,b.y]]:
      a.x+a.width<=b.x?[[a.x+a.width,a.y+a.height/2],[b.x,b.y+b.height/2]]:
      [[a.x,a.y+a.height/2],[b.x+b.width,b.y+b.height/2]];
    if(e.source!==e.target && ![...nodes.values()].some(n=>crossesBox(...direct,n))) {
      e.points=direct;return;
    }
    const corridor=maxRight+32+i*12;
    const isTest=key=>graph.model.types[graph.objects[objects.get(key)]?.type]?.role==='test';
    if(e.source===e.target && isTest(e.source)) {
      e.points=[[a.x+a.width,a.y+a.height*.35],[corridor,a.y+a.height*.35],
        [corridor,a.y+a.height*.65],[a.x+a.width,a.y+a.height*.65]];
      return;
    }
    const exit=above?rankBounds.get(ranks.get(e.source)).top-12-(i%20)*2:rankBounds.get(ranks.get(e.source)).bottom+12+(i%20)*2;
    const entry=above?rankBounds.get(ranks.get(e.target)).bottom+12+(i%20)*2:rankBounds.get(ranks.get(e.target)).top-12-(i%20)*2;
    const start=isTest(e.source)?[[a.x+a.width,a.y+a.height/2],[corridor,a.y+a.height/2]]:
      [[a.x+a.width/2,above?a.y:a.y+a.height],[a.x+a.width/2,exit],[corridor,exit]];
    const end=isTest(e.target)?[[corridor,b.y+b.height/2],[b.x+b.width,b.y+b.height/2]]:
      [[corridor,entry],[b.x+b.width/2,entry],[b.x+b.width/2,above?b.y+b.height:b.y]];
    e.points=[...start,...end];
  });
  const rectangles=[...nodes.values()];
  const onBoundary=(p,n)=>((p[0]===n.x||p[0]===n.x+n.width)&&p[1]>=n.y&&p[1]<=n.y+n.height)||
    ((p[1]===n.y||p[1]===n.y+n.height)&&p[0]>=n.x&&p[0]<=n.x+n.width);
  for(const edge of edges) {
    if(!edge.points.every(p=>p.every(Number.isFinite)) ||
       !onBoundary(edge.points[0],nodes.get(edge.source)) ||
       !onBoundary(edge.points.at(-1),nodes.get(edge.target)))
      throw Error('Layout produced invalid edge ports.');
    for(let i=1;i<edge.points.length;i++)
      if(rectangles.some(n=>crossesBox(edge.points[i-1],edge.points[i],n)))
        throw Error('Layout produced an edge through a node.');
  }
  for(let i=0;i<rectangles.length;i++) {
    const a=rectangles[i];
    if(!Object.values(a).every(Number.isFinite)) throw Error('Layout produced invalid coordinates.');
    for(const b of rectangles.slice(i+1)) if(a.x<b.x+b.width && a.x+a.width>b.x && a.y<b.y+b.height && a.y+a.height>b.y)
      throw Error('Layout produced overlapping nodes.');
  }
  const x=Math.min(...rectangles.map(n=>n.x))-30;
  return {nodes,edges,ranks,bandTops:new Map(bands.map(b=>[b.rank,b.top])),x,width:maxRight-x+64+edges.length*12,height:Math.max(...rectangles.map(n=>n.y+n.height))+40};
}
