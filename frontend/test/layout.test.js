import test from 'node:test';
import assert from 'node:assert/strict';
import {compute} from '../src/layout.js';
const key=id=>JSON.stringify(['need',id]);

test('STV_SWR_056: competing parents do not displace a separate centered parent',async()=>{
 const objects={P:{type:'p'},Q:{type:'p'},R:{type:'p'},...Object.fromEntries(['A','B','C','D','E','F'].map(id=>[id,{type:'c'}]))};
 const graph={objects,model:{levels:['p','c'],types:{p:{level:'p'},c:{level:'c'}}}};
 const edges=[['P','r','A'],...['Q','R'].flatMap(p=>['B','C','D','E','F'].map(c=>[p,'r',c]))];
 const result=await compute(graph,{ids:Object.keys(objects),edges},new Map());
 const center=id=>result.nodes.get(key(id)).x+140;
 assert.equal(center('P'),center('A'),'a noncompeting parent can remain exactly centered');
 const desired=(Math.min(...['B','C','D','E','F'].map(center))+Math.max(...['B','C','D','E','F'].map(center)))/2;
 assert.equal((center('Q')+center('R'))/2,desired,'shared-parent displacement balances locally');
 assert.equal(Math.abs(center('Q')-center('R')),328);
});

test('STV_SWR_056: cyclic shared geometry with isolated nodes remains deterministic and separated',async()=>{
 const graph={model:{levels:['top','middle','bottom'],types:{p:{level:'top'},a:{level:'middle'},b:{level:'bottom'},t:{role:'test'}}},
  objects:{P:{type:'p'},Q:{type:'p'},A:{type:'a'},B:{type:'b'},Z:{type:'b'},T:{type:'t'}}};
 const visible={ids:Object.keys(graph.objects),edges:[['P','r','A'],['A','r','P'],['Q','r','A'],['A','r','B'],['B','r','P'],['T','r','A'],['T','r','B']]};
 const sizes=new Map(Object.keys(graph.objects).map((id,i)=>[key(id),100+i*31]));
 const result=await compute(graph,visible,sizes),again=await compute(graph,visible,sizes);
 assert.deepEqual([...result.nodes],[...again.nodes]);
 assert.equal(result.nodes.size,6);
 for(const [id,a] of result.nodes) {
  assert.ok([a.x,a.y,a.width,a.height].every(Number.isFinite));
  for(const [other,b] of result.nodes)if(id!==other)
   assert.ok(a.x+a.width<=b.x||b.x+b.width<=a.x||a.y+a.height<=b.y||b.y+b.height<=a.y);
 }
 const t=result.nodes.get(key('T'));
 assert.ok(t.x>=Math.max(...['P','Q','A','B','Z'].map(id=>result.nodes.get(key(id)).x+280))+96);
 assert.ok(result.nodes.get(key('P')).y<result.nodes.get(key('A')).y);
 assert.ok(result.nodes.get(key('A')).y<result.nodes.get(key('B')).y);
});

test('STV_SWR_056: parent and project center over five visible children',async()=>{
 const ids=['P','A','B','C','D','E'];
 const graph={model:{levels:['parent','child'],types:{p:{level:'parent'},c:{level:'child'}}},objects:Object.fromEntries(ids.map(id=>[id,{type:id==='P'?'p':'c'}]))};
 const result=await compute(graph,{ids,edges:ids.slice(1).map(id=>[id,'r','P']),project:true,entries:['P']},new Map());
 const parent=result.nodes.get(key('P')),children=ids.slice(1).map(id=>result.nodes.get(key(id)));
 const middle=(Math.min(...children.map(n=>n.x))+Math.max(...children.map(n=>n.x+n.width)))/2;
 assert.equal(parent.x+parent.width/2,middle);
 const project=result.nodes.get(JSON.stringify(['project']));assert.equal(project.x,parent.x);
});

test('STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap',async()=>{
 const graph={model:{levels:['p','c'],types:{p:{level:'p'},c:{level:'c'}}},objects:{P:{type:'p'},Q:{type:'p'},A:{type:'c'}}};
 const result=await compute(graph,{ids:['P','Q','A'],edges:[['P','r','A'],['Q','r','A']]},new Map());
 const p=result.nodes.get(key('P')),q=result.nodes.get(key('Q'));
 assert.equal(result.nodes.size,3);assert.ok(Math.abs(p.x-q.x)>=328);
});
test('STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane', async()=> {
  const model={levels:['stakeholder','hardware','system_arch','software','software_arch'],types:{
    goal:{level:'stakeholder'},hardware:{level:'hardware'},system:{level:'system_arch'},software:{level:'software'},module:{level:'software_arch'},test:{role:'test'}}};
  const objects=Object.fromEntries(['goal','hardware','system','software','module','test'].map(type=>[type,{type}]));
  const edges=[['software','r','goal'],['test','r','goal'],['test','r','software'],['module','r','module'],['test','r','test']];
  const result=await compute({objects,model,entries:['goal']},{ids:Object.keys(objects),edges,project:true},new Map(Object.keys(objects).map(id=>[key(id),160])));
  let previous=result.nodes.get(JSON.stringify(['project']));
  for(const id of ['goal','hardware','system','software','module']) {const node=result.nodes.get(key(id));assert.ok(node.y>previous.y+previous.height);previous=node;}
  const testNode=result.nodes.get(key('test'));
  const loop=result.edges.find(e=>e.edge[0]==='test'&&e.edge[2]==='test');
  assert.notDeepEqual(loop.points[0],loop.points.at(-1),'self-link needs distinct ports');
  assert.ok(new Set(loop.points.map(p=>p[1])).size>1,'self-link needs a visible loop');
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
