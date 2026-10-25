import test from 'node:test';
import assert from 'node:assert/strict';
import {intersect} from '../snapshot.js';
test('STV_SWR_070 visible crop intersects screen and never invents dimensions',()=>{
  assert.deepEqual(intersect({left:-20,top:50,right:900,bottom:1000},{left:0,top:0,right:800,bottom:600}),{left:0,top:50,right:800,bottom:600,width:800,height:550});
  assert.equal(intersect({left:0,top:900,right:20,bottom:1000},{left:0,top:0,right:800,bottom:600}).height,0);
});
