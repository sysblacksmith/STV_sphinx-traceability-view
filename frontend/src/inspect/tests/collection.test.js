import test from 'node:test';
import assert from 'node:assert/strict';
import {detailCollection,DEFAULT_DETAILS_LIMIT} from '../collection.js';

test('STV_SWR_063: persistent collection reuses identity without refreshing FIFO age',()=>{
  const c=detailCollection(3);let created=0;const open=id=>c.open(id,()=>({id,serial:++created}));
  const a=open('A').entry;open('B');open('C');
  assert.equal(open('A').entry,a);assert.equal(created,3);assert.deepEqual([...c.entries.keys()],['A','B','C']);
  assert.equal(open('D').evicted,a);assert.deepEqual([...c.entries.keys()],['B','C','D']);
  c.close('C');assert.equal(open('E').evicted,undefined);assert.deepEqual([...c.entries.keys()],['B','D','E']);
  c.close('B');open('B');assert.deepEqual([...c.entries.keys()],['D','E','B']);assert.equal(open('F').evicted.id,'D');
});

test('STV_SWR_063: default, one-slot and independent detail collections enforce their own capacity',()=>{
  assert.equal(DEFAULT_DETAILS_LIMIT,10);const c=detailCollection(),other=detailCollection(1);
  for(let i=0;i<11;i++)c.open(String(i),()=>({id:String(i)}));
  assert.equal(c.entries.size,10);assert.equal(c.entries.has('0'),false);
  other.open('A',()=>({id:'A'}));assert.equal(other.open('B',()=>({id:'B'})).evicted.id,'A');
  c.clear();assert.equal(c.entries.size,0);assert.equal(other.entries.size,1);
  for(const bad of [0,-1,true,'3',1.5,null,Infinity,Number.MAX_SAFE_INTEGER+1])assert.throws(()=>detailCollection(bad),/positive safe integer/);
});
