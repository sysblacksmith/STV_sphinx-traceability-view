import test from 'node:test';
import assert from 'node:assert/strict';
import {initial,transition,groupKey} from '../state.js';
test('STV_SWR_066 reset retains current roots and clears every restoration cache',()=>{
  const graph={objects:{A:{},B:{}},entries:['A','B'],adjacency:{}};
  const state=initial(['A','B']);state.expanded.add(groupKey('A','traces','outgoing'));state.pages.set(2,new Set(['old']));
  const result=transition(graph,state,{type:'collapse-all'});
  assert.deepEqual(result.state.seeds,['A','B']);assert.equal(result.state.expanded.size,0);assert.equal(result.state.pages.size,0);assert.equal(result.state.revision,1);
  assert.equal(state.expanded.size,1);assert.equal(state.pages.size,1);
  const overview=initial();overview.page=1;overview.rootOpen=false;
  const reset=transition(graph,overview,{type:'collapse-all'});
  assert.equal(reset.state.page,0);assert.equal(reset.state.rootOpen,true);assert.deepEqual(reset.graph.entries,['A','B']);
});
