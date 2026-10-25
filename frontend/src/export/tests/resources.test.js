import test from 'node:test';
import assert from 'node:assert/strict';
import {embeddedResource} from '../resources.js';
test('STV_SWR_072 snapshot resources reject remote paths and inherited dictionary entries',()=>{
  const base='file:///docs/',records={assets:{'image.png':{data:'data:image/png;base64,eA=='},'bad.svg':{error:'active SVG'}}};
  assert.equal(embeddedResource('file:///docs/image.png',base,records),'data:image/png;base64,eA==');
  for(const value of ['https://example.org/a.png','file:///private.png','file:///docs/constructor','file:///docs/bad.svg'])assert.throws(()=>embeddedResource(value,base,records));
});
