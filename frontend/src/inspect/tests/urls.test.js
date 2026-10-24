import test from 'node:test';
import assert from 'node:assert/strict';
import {detailURL,detailCSS} from '../urls.js';

test('STV_SWR_017 STV_SWR_018: restored detail paths stay inside the output root',()=>{
  for(const base of ['https://example.invalid/docs/','file:///C:/docs/']) {
    assert.equal(String(detailURL('images/local.png',base)),new URL('images/local.png',base).href);
    for(const raw of ['javascript:window.marker=1','data:text/html,bad','https://elsewhere.invalid/x','//elsewhere.invalid/x','/outside','../outside','%2e%2e/outside','..%2foutside','\\\\elsewhere.invalid/x'])assert.equal(detailURL(raw,base),null,raw);
    assert.equal(detailURL('data:image/png;base64,AAAA',base,{image:true}),'data:image/png;base64,AAAA');
    assert.equal(detailURL('data:image/svg+xml,bad',base,{image:true}),null);
    assert.equal(detailURL('data:image/png;base64,AAAA',base),null);
  }
});

test('STV_SWR_015 STV_SWR_017: restored CSS rejects noncanonical and remote resource paths',()=>{
  const base='https://example.invalid/docs/';
  assert.equal(detailCSS('color:red;background:url("images/a.png")',base),'color:red;background:url("https://example.invalid/docs/images/a.png")');
  assert.equal(detailCSS('background:url("https://elsewhere.invalid/a")',base),'background:none');
  for(const css of ['@import "https://elsewhere.invalid/x"','background:url(https://elsewhere.invalid/x)','background:u\\72l("x")'])assert.equal(detailCSS(css,base),'');
});
