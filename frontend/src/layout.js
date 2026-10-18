import ELK from 'elkjs/lib/elk.bundled.js';
const elk = new ELK();
/** ELK proposes ordering; domain bands own final geometry. */
export async function compute(graph, visible, boxes) {
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
    if(object && graph.model.types[object.type].role!=='test') ranks.set(key,levels.indexOf(graph.model.types[object.type].level));
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
    normal.sort((a,b)=>(suggestions.get(a)-suggestions.get(b)) || a.localeCompare(b));
    let x=30, height=0;
    for(const key of normal) {const h=boxes.get(key)||160;nodes.set(key,{x,y,width:280,height:h});x+=328;height=Math.max(height,h);}
    bands.push({rank,y,normal,tests,height}); y+=Math.max(height,40)+100;
  }
  const right=Math.max(30,...[...nodes.values()].map(n=>n.x+n.width))+96;
  // A stacked test lane can increase a band height; shift subsequent bands together.
  let shift=0;
  for(const band of bands) {
    for(const key of band.normal) nodes.get(key).y+=shift;
    let ty=band.y+shift;
    for(const key of band.tests.sort()) {const h=boxes.get(key)||160;nodes.set(key,{x:right,y:ty,width:280,height:h});ty+=h+24;}
    shift+=Math.max(0,ty-(band.y+shift)-24-band.height);
  }
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
    const corridor=maxRight+32+i*12;
    const isTest=key=>graph.model.types[graph.objects[objects.get(key)]?.type]?.role==='test';
    const exit=rankBounds.get(ranks.get(e.source)).bottom+12+(i%20)*2;
    const entry=rankBounds.get(ranks.get(e.target)).top-12-(i%20)*2;
    const start=isTest(e.source)?[[a.x+a.width,a.y+a.height/2],[corridor,a.y+a.height/2]]:
      [[a.x+a.width/2,a.y+a.height],[a.x+a.width/2,exit],[corridor,exit]];
    const end=isTest(e.target)?[[corridor,b.y+b.height/2],[b.x+b.width,b.y+b.height/2]]:
      [[corridor,entry],[b.x+b.width/2,entry],[b.x+b.width/2,b.y]];
    e.points=[...start,...end];
  });
  const rectangles=[...nodes.values()];
  for(let i=0;i<rectangles.length;i++) {
    const a=rectangles[i];
    if(!Object.values(a).every(Number.isFinite)) throw Error('Layout produced invalid coordinates.');
    for(const b of rectangles.slice(i+1)) if(a.x<b.x+b.width && a.x+a.width>b.x && a.y<b.y+b.height && a.y+a.height>b.y)
      throw Error('Layout produced overlapping nodes.');
  }
  return {nodes,edges,width:maxRight+64+edges.length*12,height:Math.max(...rectangles.map(n=>n.y+n.height))+40};
}
