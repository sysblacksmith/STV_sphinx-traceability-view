import test from 'node:test';
import assert from 'node:assert/strict';
import {filename,saveSVG,releaseDownloads} from '../download.js';
test('STV_SWR_071 download uses safe filenames and releases owned URLs',()=>{
  assert.equal(filename('../bad\\name'),'stv-___bad_name.svg');assert.ok(filename('a'.repeat(200)).length<90);
  const oldDocument=globalThis.document,create=URL.createObjectURL,revoke=URL.revokeObjectURL;
  const events=[];let blob;
  globalThis.document={body:{append:a=>events.push('append')},createElement:()=>({click(){events.push('click');},remove(){events.push('remove');}})};
  URL.createObjectURL=b=>{blob=b;return 'blob:probe';};URL.revokeObjectURL=url=>events.push(url);
  try{saveSVG('<svg/>','test');assert.equal(blob.type,'image/svg+xml;charset=utf-8');assert.deepEqual(events,['append','click','remove']);releaseDownloads();assert.equal(events.at(-1),'blob:probe');}
  finally{globalThis.document=oldDocument;URL.createObjectURL=create;URL.revokeObjectURL=revoke;}
});
