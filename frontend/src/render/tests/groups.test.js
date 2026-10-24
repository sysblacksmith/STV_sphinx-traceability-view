import test from 'node:test';
import assert from 'node:assert/strict';
import {orderedGroups} from '../groups.js';

test('STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship',()=> {
  const graph={model:{levels:['upper','middle','lower'],types:{
    p:{level:'upper'},m:{level:'middle'},c:{level:'lower'},t:{role:'test'}}},
    objects:{P:{type:'p'},M:{type:'m'},C:{type:'c'},T:{type:'t'}},
    adjacency:{M:{outgoing:{down:['C'],mixed:['P','C'],side:['M'],test:['T'],missing:['X'],empty:[]},
      incoming:{up:['P'],down2:['C'],up2:['P']}}}};
  const before=JSON.stringify(graph);
  assert.deepEqual(orderedGroups(graph,'M').map(g=>g.relation),
    ['up','up2','mixed','side','test','missing','down','down2']);
  assert.equal(JSON.stringify(graph),before,'ordering must not mutate graph data');
  assert.deepEqual(orderedGroups(graph,'X'),[]);
});

test('STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions',()=> {
  const graph={model:{levels:['hardware','software'],types:{h:{level:'hardware'},s:{level:'software'}}},
    objects:{A:{type:'s'},B:{type:'h'}},adjacency:{A:{outgoing:{custom:['B']},incoming:{same:['A']}}}};
  assert.deepEqual(orderedGroups(graph,'A').map(g=>g.relation),['custom','same']);
  graph.model.levels.reverse();
  assert.deepEqual(orderedGroups(graph,'A').map(g=>g.relation),['same','custom']);
});
