import test from 'node:test';
import assert from 'node:assert/strict';
import {loadDetail} from '../inspect.js';

test('STV_SWR_015 STV_SWR_017: concurrent detail requests share one load and retain build identity', async () => {
  const scripts=[];
  const oldDocument=globalThis.document,oldData=globalThis.__STV_DATA__;
  globalThis.__STV_DATA__={fragments:{}};
  globalThis.document={createElement:()=>({remove(){this.removed=true;}}),head:{append:script=>scripts.push(script)}};
  try {
    const graph={identity:'cache-build',details:{A:{digest:'cache-fragment',url:'details/a.js'}}};
    const one=loadDetail(graph,'A','https://example.invalid/docs/');
    assert.strictEqual(loadDetail(graph,'A','https://example.invalid/docs/'),one);
    assert.equal(scripts.length,1);
    assert.equal(scripts[0].src,'https://example.invalid/docs/details/a.js');
    globalThis.__STV_DATA__.fragments['cache-fragment']='<p>Original build</p>';
    scripts[0].onload();
    assert.equal(await one,'<p>Original build</p>');
    assert.equal(scripts[0].removed,true);
    const next={identity:'next-build',details:{A:{digest:'next-fragment',url:'details/next.js'}}};
    const pending=loadDetail(next,'A','https://example.invalid/docs/');
    assert.equal(scripts.length,2);
    globalThis.__STV_DATA__.fragments['next-fragment']='<p>Next build</p>';
    scripts[1].onload();
    assert.equal(await pending,'<p>Next build</p>');
  } finally {globalThis.document=oldDocument;globalThis.__STV_DATA__=oldData;}
});

test('STV_SWR_015 STV_SWR_017: failed local detail loading can retry without a stale rejection', async () => {
  const scripts=[];
  const oldDocument=globalThis.document,oldData=globalThis.__STV_DATA__;
  globalThis.__STV_DATA__={fragments:{}};
  globalThis.document={createElement:()=>({remove(){this.removed=true;}}),head:{append:script=>scripts.push(script)}};
  try {
    const graph={identity:'retry-build',details:{A:{digest:'retry-fragment',url:'retry.js'}}};
    const failed=loadDetail(graph,'A','file:///docs/');
    scripts[0].onerror();
    await assert.rejects(failed,/Local detail asset unavailable/);
    assert.equal(scripts[0].removed,true);
    const retry=loadDetail(graph,'A','file:///docs/');
    assert.notStrictEqual(retry,failed);
    assert.equal(scripts.length,2);
    globalThis.__STV_DATA__.fragments['retry-fragment']='<p>Recovered</p>';
    scripts[1].onload();
    assert.equal(await retry,'<p>Recovered</p>');
  } finally {globalThis.document=oldDocument;globalThis.__STV_DATA__=oldData;}
});
