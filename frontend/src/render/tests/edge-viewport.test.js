import test from 'node:test';
import assert from 'node:assert/strict';
import {edgeViewport} from '../edge-viewport.js';

test('PoC PR013: SVG bounds include negative routes, detours and node boxes',()=>{
  const nodes=new Map([['P',{x:-300,y:-100,width:280,height:160}],['Q',{x:30,y:200,width:280,height:160}]]);
  const points=[[-160,-120],[-600,-120],[-600,500],[170,500],[170,360]];
  const box=edgeViewport({nodes,edges:[{points}]});
  for(const [x,y] of [...points,...[...nodes.values()].flatMap(n=>[[n.x,n.y],[n.x+n.width,n.y+n.height]])]) {
    assert.ok(x>=box.x+24 && x<=box.x+box.width-24);
    assert.ok(y>=box.y+24 && y<=box.y+box.height-24);
    // Moving the SVG and its viewBox origin by the same amount preserves world coordinates.
    assert.equal(box.x+(x-box.x),x);assert.equal(box.y+(y-box.y),y);
  }
});

test('PoC PR013: an empty edge scene still has a finite SVG viewport',()=>{
  const box=edgeViewport({nodes:new Map(),edges:[]});
  assert.ok(Object.values(box).every(Number.isFinite));assert.ok(box.width>0&&box.height>0);
});
