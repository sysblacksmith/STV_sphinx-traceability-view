import test from 'node:test';
import assert from 'node:assert/strict';
import {initial, visible, transition, groupKey} from '../src/state.js';
function graph(edges, entries = []) {
  const adjacency = {};
  for (const [a, r, b] of edges) {
    adjacency[a] ||= {incoming: {}, outgoing: {}};
    adjacency[b] ||= {incoming: {}, outgoing: {}};
    (adjacency[a].outgoing[r] ||= []).push(b);
    (adjacency[b].incoming[r] ||= []).push(a);
  }
  return {edges, entries, adjacency};
}
const toggle = (g, s, id, direction='outgoing') => transition(g, s, {type:'group', id, relation:'r', direction}).state;
test('STV_SWR_003 STV_SWR_007 STV_SWR_020 STV_SWR_024 STV_SWR_025: rooted diamond and isolated cycle', () => {
  const g = graph([['A','r','B'],['A','r','C'],['B','r','D'],['C','r','D'],['D','r','B']]);
  let s = initial(['A', 'A', 'Z']);
  assert.deepEqual(visible(g,s).ids, ['A','Z']);
  for (const id of ['A','B','C','D']) s = toggle(g,s,id);
  assert.equal(visible(g,s).ids.filter(i=>i==='D').length,1);
  s = toggle(g,s,'B'); assert.ok(visible(g,s).ids.includes('D'));
  s = toggle(g,s,'C'); assert.deepEqual(new Set(visible(g,s).ids),new Set(['A','Z','B','C']));
  s = toggle(g,s,'A'); assert.deepEqual(visible(g,s).ids,['A','Z']);
  s = toggle(g,s,'A'); assert.ok(visible(g,s).ids.includes('B'));
});
test('STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity', () => {
  for (const size of [199,200,201]) {
    const g = graph(Array.from({length:size-1},(_,i)=>['A','r',String(i)]));
    const s = initial(['A']), result = transition(g,s,{type:'group',id:'A',relation:'r',direction:'outgoing'});
    if (size <= 200) assert.equal(result.graph.ids.length,size);
    else { assert.equal(result.state,s); assert.match(result.error,/200-node/); assert.equal(s.expanded.size,0); }
  }
});
test('STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff', () => {
  const g = graph(Array.from({length:8},(_,i)=>[String(i),'r',String(i+1)]));
  let s=initial(['8']); for(let i=8;i>0;i--) s=toggle(g,s,String(i),'incoming');
  assert.equal(visible(g,s).ids.length,9); assert.equal(visible(g,s).edges.length,8);
  s=initial(['0']);for(let i=0;i<8;i++)s=toggle(g,s,String(i));
  assert.equal(visible(g,s).ids.length,9);
});
test('STV_SWR_024: self-loop terminates and collapse restores the only seed',()=> {
  const g=graph([['A','r','A']]);let s=toggle(g,initial(['A']),'A');
  assert.deepEqual(visible(g,s).ids,['A']);assert.equal(visible(g,s).edges.length,1);
  s=toggle(g,s,'A');assert.equal(visible(g,s).edges.length,0);
});
test('STV_SWR_051 STV_SWR_052: project pages preserve independent expansion and collapsed root', () => {
  const entries=Array.from({length:201},(_,i)=>String(i).padStart(3,'0'));
  const g=graph([['000','r','child'],['050','r','other']],entries);
  let s=initial(); assert.equal(visible(g,s).ids.length,0);
  s=transition(g,s,{type:'root'}).state; assert.equal(visible(g,s).ids.length,50);
  s=toggle(g,s,'000');
  s=transition(g,s,{type:'page',page:1}).state; assert.ok(!visible(g,s).ids.includes('child'));
  s=toggle(g,s,'050'); s=transition(g,s,{type:'page',page:0}).state;
  assert.ok(visible(g,s).ids.includes('child')); assert.ok(!visible(g,s).ids.includes('other'));
  s=transition(g,s,{type:'root'}).state; assert.equal(visible(g,s).ids.length,0);
  s=transition(g,s,{type:'root'}).state; assert.ok(visible(g,s).ids.includes('child'));
  const all=[]; for(let page=0;page<5;page++) {s=transition(g,s,{type:'page',page}).state; all.push(...visible(g,s).ids.filter(i=>entries.includes(i)));}
  assert.equal(new Set(all).size,201);
  assert.notEqual(groupKey('a,b','c','incoming'),groupKey('a','b,c','incoming'));
});
test('STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges',()=> {
  const g=graph([['000','r','050']],Array.from({length:51},(_,i)=>String(i).padStart(3,'0')));
  let s=transition(g,initial(),{type:'root'}).state;s=toggle(g,s,'000');
  const v=visible(g,s);assert.ok(v.ids.includes('050'));assert.ok(!v.entries.includes('050'));
  assert.equal(v.entries.length,50);
});
test('STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views',()=> {
  for(const size of [0,1,50,51,199,200,201]) {
    const entries=Array.from({length:size},(_,i)=>String(i).padStart(3,'0')),g=graph([],entries),fresh=initial();
    const opened=transition(g,fresh,{type:'root'});
    if(!size){assert.equal(opened.state,fresh);assert.match(opened.error,/No stakeholder/);continue;}
    let s=opened.state;const seen=[];
    for(let page=0;page<Math.ceil(size/50);page++) {s=transition(g,s,{type:'page',page}).state;seen.push(...visible(g,s).entries);assert.ok(visible(g,s).ids.length<=50);}
    assert.deepEqual(seen,entries);assert.equal(fresh.rootOpen,false);
    const rejected=transition(g,s,{type:'page',page:Math.ceil(size/50)});assert.equal(rejected.state,s);
  }
  for(const total of [199,200,201]) {
    const entries=['A'],g=graph(Array.from({length:total-2},(_,i)=>['A','r','child'+i]),entries);
    const s=transition(g,initial(),{type:'root'}).state;
    const result=transition(g,s,{type:'group',id:'A',relation:'r',direction:'outgoing'});
    if(total<=200)assert.equal(result.graph.ids.length+1,total);else assert.equal(result.state,s);
  }
});
