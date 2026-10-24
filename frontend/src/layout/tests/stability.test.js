import test from 'node:test';
import assert from 'node:assert/strict';
import {compute} from '../layout.js';
const key=id=>JSON.stringify(['need',id]);
const graph={model:{levels:['parent','child','leaf'],types:{p:{level:'parent'},c:{level:'child'},l:{level:'leaf'},t:{role:'test'}}},
  objects:{P:{type:'p'},Q:{type:'p'},L:{type:'l'},T:{type:'t'},...Object.fromEntries('ABCDEF'.split('').map(id=>[id,{type:'c'}]))}};
const view=ids=>({ids,edges:[...ids.filter(id=>'ABCDE'.includes(id)).map(id=>['P','r',id]),...(ids.includes('F')?[['Q','r','F']]:[])]});

test('PoC PR013: expand and collapse preserve existing primary slots',async()=>{
  let previous=await compute(graph,view(['P','Q']),new Map());
  for(const [ids,anchor] of [[['P','Q','A','B','C','D','E'],'P'],[['P','Q','A','B','C','D','E','F'],'Q'],[['P','Q','F'],'P']]) {
    const result=await compute(graph,view(ids),new Map(),{previous,anchor:key(anchor)});
    for(const id of ids)if(previous.nodes.has(key(id)))assert.deepEqual(result.nodes.get(key(id)),previous.nodes.get(key(id)),id);
    const again=await compute(graph,view(ids),new Map(),{previous,anchor:key(anchor)});
    assert.deepEqual([...result.nodes],[...again.nodes]);
    previous=result;
  }
});

test('PoC PR013: existing test lane is stable while new primary nodes fit beside it',async()=>{
  const before={ids:['P','Q','T'],edges:[['P','r','T']]};
  const previous=await compute(graph,before,new Map());
  const next=view(['P','Q','T','A','B','C','D','E']);next.edges.push(['P','r','T']);
  const result=await compute(graph,next,new Map(),{previous,anchor:key('P')});
  for(const id of before.ids)assert.deepEqual(result.nodes.get(key(id)),previous.nodes.get(key(id)),id);
  for(const id of 'ABCDE')assert.ok(result.nodes.get(key(id)).x+280+96<=result.nodes.get(key('T')).x);
});

test('PoC PR013: a growing earlier band makes room above the clicked lower band',async()=>{
  const before={ids:['P','A','L'],edges:[['P','r','A'],['A','r','L']]};
  const sizes=new Map([[key('T'),800]]);
  const previous=await compute(graph,before,sizes);
  const result=await compute(graph,{ids:[...before.ids,'T'],edges:[...before.edges,['A','r','T']]},sizes,{previous,anchor:key('L')});
  assert.deepEqual(result.nodes.get(key('L')),previous.nodes.get(key('L')));
  assert.ok(result.nodes.get(key('A')).y<previous.nodes.get(key('A')).y);
  assert.ok(result.nodes.get(key('P')).y+160<result.nodes.get(key('A')).y);
});


test('PoC PR013: initial seed and project rows use natural numeric ID order',async()=>{
  const ids=['REQ_20','REQ_10','REQ_3','REQ_2','REQ_1'];
  const g={model:{levels:['parent','child'],types:{p:{level:'parent'},c:{level:'child'}}},objects:Object.fromEntries([...ids.map(id=>[id,{type:'p'}]),['CHILD_A',{type:'c'}]])};
  for(const project of [false,true]) {
    const v={ids,edges:[],project,entries:project?ids:[]};
    const initial=await compute(g,v,new Map());
    const order=geometry=>ids.slice().sort((a,b)=>geometry.nodes.get(key(a)).x-geometry.nodes.get(key(b)).x);
    assert.deepEqual(order(initial),['REQ_1','REQ_2','REQ_3','REQ_10','REQ_20']);
    const expanded=await compute(g,{...v,ids:[...ids,'CHILD_A'],edges:[['REQ_2','r','CHILD_A']]},new Map(),{previous:initial,anchor:key('REQ_2')});
    for(const id of ids)assert.deepEqual(expanded.nodes.get(key(id)),initial.nodes.get(key(id)));
    assert.deepEqual(order(expanded),order(initial));
  }
});
