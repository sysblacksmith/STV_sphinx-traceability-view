import test from 'node:test';
import assert from 'node:assert/strict';
import {compute} from '../src/layout.js';
const key=id=>JSON.stringify(['need',id]);
test('STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037: semantic bands and shared test lane', async()=> {
  const model={levels:['stakeholder','hardware','system_arch','software','software_arch'],types:{
    goal:{level:'stakeholder'},hardware:{level:'hardware'},system:{level:'system_arch'},software:{level:'software'},module:{level:'software_arch'},test:{role:'test'}}};
  const objects=Object.fromEntries(['goal','hardware','system','software','module','test'].map(type=>[type,{type}]));
  const edges=[['software','r','goal'],['test','r','goal'],['test','r','software'],['module','r','module']];
  const result=await compute({objects,model,entries:['goal']},{ids:Object.keys(objects),edges,project:true},new Map(Object.keys(objects).map(id=>[key(id),160])));
  let previous=result.nodes.get(JSON.stringify(['project']));
  for(const id of ['goal','hardware','system','software','module']) {const node=result.nodes.get(key(id));assert.ok(node.y>previous.y+previous.height);previous=node;}
  const testNode=result.nodes.get(key('test'));
  assert.ok(testNode.x>=Math.max(...['goal','hardware','system','software','module'].map(id=>result.nodes.get(key(id)).x+280))+96);
  for(const edge of result.edges) {
    const a=result.nodes.get(edge.source),b=result.nodes.get(edge.target);
    const onBoundary=(p,n)=>((p[0]===n.x||p[0]===n.x+n.width)&&p[1]>=n.y&&p[1]<=n.y+n.height)||((p[1]===n.y||p[1]===n.y+n.height)&&p[0]>=n.x&&p[0]<=n.x+n.width);
    assert.ok(onBoundary(edge.points[0],a));assert.ok(onBoundary(edge.points.at(-1),b));
    for(let i=1;i<edge.points.length;i++)for(const n of result.nodes.values()) {
      const p=edge.points[i-1],q=edge.points[i];
      // Independent sampling also handles diagonal direct routes.
      const crosses=Array.from({length:999},(_,j)=>(j+1)/1000).some(t=> {
        const x=p[0]+t*(q[0]-p[0]),y=p[1]+t*(q[1]-p[1]);
        return x>n.x&&x<n.x+n.width&&y>n.y&&y<n.y+n.height;
      });
      assert.equal(crosses,false,'edge cannot pass through a node');
    }
  }
});

test('STV_SWR_053: clear facing ports and fan-in avoid outer detours', async()=> {
  const graph={model:{levels:['parent','child'],types:{p:{level:'parent'},c:{level:'child'}}},
    objects:{P:{type:'p'},A:{type:'c'},B:{type:'c'},C:{type:'c'}}};
  const result=await compute(graph,{ids:['P','A','B','C'],edges:[['A','r','P'],['B','r','P'],['P','r','C']]},new Map());
  for(const edge of result.edges) {
    assert.equal(edge.points.length,2);
    const a=result.nodes.get(edge.source),b=result.nodes.get(edge.target);
    if(a.y>b.y)assert.deepEqual(edge.points,[[a.x+140,a.y],[b.x+140,b.y+b.height]]);
    else assert.deepEqual(edge.points,[[a.x+140,a.y+a.height],[b.x+140,b.y]]);
  }
});

test('STV_SWR_053: blocked skipped-level edges retain safe detours', async()=> {
  const graph={model:{levels:['top','middle','bottom'],types:{t:{level:'top'},m:{level:'middle'},b:{level:'bottom'}}},
    objects:{T:{type:'t'},M:{type:'m'},B:{type:'b'}}};
  const result=await compute(graph,{ids:['T','M','B'],edges:[['B','r','T'],['T','r','B']]},new Map());
  const middle=result.nodes.get(key('M'));
  for(const edge of result.edges) {
    assert.ok(edge.points.length>2);
    for(let i=1;i<edge.points.length;i++) {
      const p=edge.points[i-1],q=edge.points[i];
      assert.ok(p[0]===q[0]||p[1]===q[1]);
      for(let t=.001;t<1;t+=.001) {
        const x=p[0]+t*(q[0]-p[0]),y=p[1]+t*(q[1]-p[1]);
        assert.ok(!(x>middle.x&&x<middle.x+middle.width&&y>middle.y&&y<middle.y+middle.height));
      }
    }
  }
});
