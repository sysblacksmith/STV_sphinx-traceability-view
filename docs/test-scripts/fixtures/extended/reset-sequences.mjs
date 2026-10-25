import test from 'node:test';
import assert from 'node:assert/strict';
import {initial,transition,visible} from '../../../../frontend/src/state/state.js';

test('STV_SWR_066 reset is fresh after every command class and cyclic shared traversal',()=>{
  const graph={objects:{A:{},B:{},C:{}},entries:['A','B'],adjacency:{
    A:{outgoing:{traces:['B','C']}},B:{outgoing:{traces:['C']}},C:{outgoing:{traces:['A']}}}};
  let state=initial();
  for(const command of [{type:'root'},{type:'root'},{type:'page',page:0},{type:'seed',id:'A'},
    {type:'group',id:'A',direction:'outgoing',relation:'traces'},
    {type:'group',id:'B',direction:'outgoing',relation:'traces'},
    {type:'group',id:'C',direction:'outgoing',relation:'traces'},{type:'overview'}]){
    const next=transition(graph,state,command);assert.equal(next.error,undefined);state=next.state;
    const before={expanded:[...state.expanded],pages:[...state.pages],seeds:[...state.seeds],revision:state.revision};
    const reset=transition(graph,state,{type:'collapse-all'});
    assert.notEqual(reset.state.expanded,state.expanded);assert.notEqual(reset.state.pages,state.pages);
    assert.notEqual(reset.state.seeds,state.seeds);assert.equal(reset.state.revision,state.revision+1);
    assert.equal(reset.state.expanded.size,0);assert.equal(reset.state.pages.size,0);
    assert.deepEqual(reset.state.seeds,state.seeds);
    assert.deepEqual(before,{expanded:[...state.expanded],pages:[...state.pages],seeds:[...state.seeds],revision:state.revision});
    assert.ok(visible(graph,reset.state).ids.length<=200);
  }
});

test('STV_SWR_066 reset preserves a 200-seed boundary after atomic overflow rejection',()=>{
  const ids=Array.from({length:201},(_,i)=>`N${i}`);
  const graph={objects:Object.fromEntries(ids.map(id=>[id,{}])),entries:ids,adjacency:{N0:{outgoing:{traces:['N200']}}}};
  const current=initial(ids.slice(0,200));
  const rejected=transition(graph,current,{type:'group',id:'N0',direction:'outgoing',relation:'traces'});
  assert.match(rejected.error,/200-node/);assert.equal(rejected.state,current);
  const reset=transition(graph,current,{type:'collapse-all'});
  assert.equal(reset.error,undefined);assert.deepEqual(reset.graph.ids,ids.slice(0,200));
  assert.equal(reset.state.expanded.size,0);
});
