// Preserve committed navigation slots after fresh semantic placement (ADR 008).
// Only the clicked band is anchored in y; other bands make room for growth.
// Shared tests may change median rank and are appended in their new band.
export function stabilize(nodes,ranks,bands,previous,anchor) {
  if(!previous?.nodes?.has(anchor)||!nodes.has(anchor)||!previous.bandTops)return;
  const oldAnchor=previous.nodes.get(anchor),freshAnchor=nodes.get(anchor);
  const dx=oldAnchor.x-freshAnchor.x;
  const tests=new Set(bands.flatMap(b=>b.tests));
  const oldTests=[...tests].filter(k=>previous.nodes.has(k));
  let lane=oldTests.length?previous.nodes.get(oldTests[0]).x:null;
  const place=(desired,width,occupied,limit)=> {
    const choices=[Math.min(desired,limit),...occupied.flatMap(n=>[n.x-width-48,n.x+n.width+48])];
    return choices.filter(x=>Number.isFinite(x)&&x<=limit&&occupied.every(n=>x+width+48<=n.x+1e-6||x>=n.x+n.width+48-1e-6))
      .sort((a,b)=>Math.abs(a-desired)-Math.abs(b-desired)||a-b)[0];
  };
  for(const band of bands) {
    const occupied=[];
    for(const key of band.normal.filter(k=>previous.nodes.has(k))) {
      const node=nodes.get(key);node.x=previous.nodes.get(key).x;occupied.push(node);
    }
    const newcomers=band.normal.filter(k=>!previous.nodes.has(k)).sort((a,b)=>nodes.get(a).x-nodes.get(b).x||a.localeCompare(b));
    for(const key of newcomers) {
      const node=nodes.get(key);
      node.x=place(node.x+dx,node.width,occupied,lane===null?Infinity:lane-96-node.width);
      occupied.push(node);
    }
  }
  if(lane===null)lane=Math.max(...bands.flatMap(b=>b.normal).map(k=>nodes.get(k).x+nodes.get(k).width))+96;
  const offsets=new Map();
  for(const band of bands) {
    let bottom=0;
    const kept=band.tests.filter(k=>previous.nodes.has(k)&&previous.ranks.get(k)===band.rank);
    for(const key of kept) {
      const offset=previous.nodes.get(key).y-previous.bandTops.get(band.rank);
      offsets.set(key,offset);bottom=Math.max(bottom,offset+nodes.get(key).height+24);
    }
    for(const key of band.tests.filter(k=>!offsets.has(k)).sort()) {
      offsets.set(key,bottom);bottom+=nodes.get(key).height+24;
    }
    band.stableHeight=Math.max(40,...band.normal.map(k=>nodes.get(k).height),bottom?bottom-24:0);
  }
  const anchorBand=bands.find(b=>b.rank===ranks.get(anchor));
  anchorBand.top=oldAnchor.y-(offsets.get(anchor)||0);
  const index=bands.indexOf(anchorBand);
  for(let i=index+1;i<bands.length;i++) {
    const band=bands[i],above=bands[i-1];
    band.top=Math.max(previous.bandTops.get(band.rank)??band.top,above.top+above.stableHeight+100);
  }
  for(let i=index-1;i>=0;i--) {
    const band=bands[i],below=bands[i+1];
    band.top=Math.min(previous.bandTops.get(band.rank)??band.top,below.top-band.stableHeight-100);
  }
  for(const band of bands) {
    for(const key of band.normal)nodes.get(key).y=band.top;
    for(const key of band.tests)Object.assign(nodes.get(key),{x:lane,y:band.top+offsets.get(key)});
  }
}
