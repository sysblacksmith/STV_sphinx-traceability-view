import test from 'node:test';
import assert from 'node:assert/strict';
import {compute} from '../layout.js';
import {orderedGroups} from '../../render/groups.js';
const key=id=>JSON.stringify(['need',id]);
const levels=['stakeholder','system','system_cases','system_runs','system_arch','software','software_cases','software_runs','software_arch','fallback','problems'];
const ids=levels.map((_,i)=>`N_${i}`);
const graph={model:{levels,types:{ordinary:{level:'stakeholder'},case:{levels_by_tag:{}},run:{level_from:{}}}},
 objects:Object.fromEntries(ids.map((id,i)=>[id,{type:i===2||i===6?'case':i===3||i===7?'run':'ordinary',level:levels[i]}]))};
const edges=ids.slice(1).map((id,i)=>[ids[i],'r',id]);


test('STV_SWR_012 STV_SWR_037 STV_SWR_058: classified rows align and stay stable during navigation',async()=>{
  const g=structuredClone(graph);g.objects.PEER={type:'case',level:'system_cases'};
  const before={ids:[...ids,'PEER'],edges:[...edges,['N_2','r','N_5'],['PEER','r','N_3']]};
  const result=await compute(g,before,new Map());
  for(let i=1;i<ids.length;i++)assert.ok(result.nodes.get(key(ids[i])).y>result.nodes.get(key(ids[i-1])).y);
  assert.equal(result.nodes.get(key('PEER')).y,result.nodes.get(key('N_2')).y);
  for(const anchor of ['N_5','N_2','N_3']) {
    const reduced={ids:before.ids.filter(id=>id!=='PEER'),edges:before.edges.filter(([a,,b])=>a!=='PEER'&&b!=='PEER')};
    const next=await compute(g,reduced,new Map(),{previous:result,anchor:key(anchor)});
    for(const id of ids)assert.deepEqual(next.nodes.get(key(id)),result.nodes.get(key(id)));
    assert.equal(next.ranks.get(key('N_2')),2,'cross-level verification does not reclassify a case');
  }
});


test('STV_SWR_055: controls use resolved case and execution rows',()=>{
  const g={...graph,adjacency:{N_5:{outgoing:{down:['N_6'],up:['N_3'],mixed:['N_0','N_8']},incoming:{}}}};
  assert.deepEqual(orderedGroups(g,'N_5').map(x=>x.relation),['up','mixed','down']);
});


test('STV_SWR_012 STV_SWR_037: 200 classified nodes keep row alignment and safe cyclic routes',async()=>{
  const g=structuredClone(graph);g.objects=Object.fromEntries(Array.from({length:200},(_,i)=>[`R_${i}`,{type:'case',level:levels[i%9]}]));
  const all=Object.keys(g.objects),links=all.map((id,i)=>[id,'r',all[(i+9)%all.length]]);
  const result=await compute(g,{ids:all,edges:links},new Map());
  assert.equal(result.nodes.size,200);
  for(let rank=0;rank<9;rank++)assert.equal(new Set(all.filter(id=>g.objects[id].level===levels[rank]).map(id=>result.nodes.get(key(id)).y)).size,1);
});
