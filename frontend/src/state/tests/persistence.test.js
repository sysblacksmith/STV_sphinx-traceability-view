import assert from 'node:assert/strict';
import {test} from 'node:test';
import {initial,groupKey,visible} from '../state.js';
import {snapshot,restoreSnapshot,rememberedStorage,storageKey,restorePositions} from '../persistence.js';
// requirements: STV_SWR_073 STV_SWR_074 STV_SWR_075
const graph={project:'Test',objects:{A:{},B:{},C:{}},entries:['A','B','C'],model:{levels:['one']},details_limit:2,adjacency:{A:{outgoing:{traces:['B']}},B:{outgoing:{traces:['A','C']}}}};
const geometry={nodes:new Map([['A',{x:12,y:30,width:280,height:160}]]),ranks:new Map([['A',0]])};
const transform={x:-100,y:21,k:.7};
const saved=(state=initial(['A']))=>snapshot(graph,state,['A','B'],transform,geometry);
test('STV_SWR_074 exploration/page/card/viewport round trip',()=>{
 const state=initial(['A']);state.expanded.add(groupKey('A','traces','outgoing'));state.pages.set(0,new Set(state.expanded));
 const r=restoreSnapshot(JSON.stringify(saved(state)),graph);assert.deepEqual(r.state,state);assert.deepEqual(r.cards,['A','B']);assert.deepEqual(r.transform,transform);assert.deepEqual(visible(graph,r.state).ids,['A','B']);
 const overview=initial();overview.rootOpen=false;assert.deepEqual(restoreSnapshot(JSON.stringify(saved(overview)),graph).state,overview);
});
test('STV_SWR_074 stale/hidden IDs and reduced card limit',()=>{
 const d=saved();d.state.seeds.push('HIDDEN');d.cards.push('C','HIDDEN');d.state.expanded.push(groupKey('HIDDEN','traces','outgoing'),groupKey('A','obsolete','outgoing'));
 const r=restoreSnapshot(JSON.stringify(d),{...graph,details_limit:1});assert.deepEqual(r.state.seeds,['A']);assert.deepEqual(r.cards,['C']);assert.equal(r.state.expanded.size,0);
 d.state.seeds=['HIDDEN'];assert.throws(()=>restoreSnapshot(JSON.stringify(d),graph),/starting context/);
});
test('STV_SWR_074 malformed schema/state/page/transform rejected atomically',()=>{
 for(const mutate of [d=>d.version=2,d=>d.state=null,d=>d.cards={},d=>d.transform.k=0,d=>d.transform.x=null,d=>d.state.pages=[['bad',[]]],d=>d.state.expanded=null]){const d=saved();mutate(d);assert.throws(()=>restoreSnapshot(JSON.stringify(d),graph));}
 assert.throws(()=>restoreSnapshot('{bad',graph));const d=saved(initial());d.state.page=10;assert.throws(()=>restoreSnapshot(JSON.stringify(d),graph),/starting context/);
});
test('STV_SWR_074 200/201-node limits apply to seeds and expansions',()=>{
 const objects=Object.fromEntries(Array.from({length:201},(_,i)=>['N'+i,{}])),g={...graph,objects,adjacency:{},entries:[]},d=saved();d.state.seeds=Object.keys(objects).slice(0,200);
 assert.equal(visible(g,restoreSnapshot(JSON.stringify(d),g).state).ids.length,200);d.state.seeds.push('N200');assert.throws(()=>restoreSnapshot(JSON.stringify(d),g),/200-node/);
 d.state.seeds=['N0'];d.state.expanded=[groupKey('N0','traces','outgoing')];g.adjacency.N0={outgoing:{traces:Object.keys(objects).slice(1)}};assert.throws(()=>restoreSnapshot(JSON.stringify(d),g),/200-node/);
});
test('STV_SWR_073 isolation/removal/last-save-wins and guarded getter/quota errors',()=>{
 const records=new Map(),storage={getItem:k=>records.get(k)||null,setItem:(k,v)=>records.set(k,v),removeItem:k=>records.delete(k)};
 const keys=[storageKey('/docs/','P','/a','v1',[]),storageKey('/docs/','P','/a','v2',[]),storageKey('/docs/','P','/b','v1',[]),storageKey('/else/','P','/a','v1',[])];assert.equal(new Set(keys).size,4);
 const a=rememberedStorage(()=>storage,keys[0]),b=rememberedStorage(()=>storage,keys[1]);assert.equal(a.read(),null);a.write({x:1});b.write({x:2});a.write({x:3});assert.deepEqual(JSON.parse(a.read()),{x:3});a.clear();assert.equal(a.read(),null);assert.deepEqual(JSON.parse(b.read()),{x:2});
 for(const op of ['read','write','clear'])assert.throws(()=>rememberedStorage(()=>{throw Error('blocked');},'k')[op]({}),/blocked/);
 assert.throws(()=>rememberedStorage(()=>({...storage,setItem:()=>{throw Error('quota');}}),'k').write({}),/quota/);
});
test('STV_SWR_075 geometry reuse requires current dimensions and ranks',()=>{
 const d=saved(),target=new Map([['A',{x:90,y:100,width:280,height:160}]]);restorePositions(d.geometry,graph,visible(graph,initial(['A'])),target,geometry.ranks);assert.equal(target.get('A').x,12);
 target.get('A').x=90;target.get('A').height=161;restorePositions(d.geometry,graph,visible(graph,initial(['A'])),target,geometry.ranks);assert.equal(target.get('A').x,90);
});
