import test from 'node:test';
import assert from 'node:assert/strict';
import {scaleTypography} from '../typography.js';
test('STV_SWR_068 descendant typography is scaled once from unmodified baselines',()=>{
  const parent={style:{},querySelectorAll:()=>[child]},child={style:{}};
  const previous=globalThis.getComputedStyle;
  globalThis.getComputedStyle=element=>({fontSize:element===parent?'20px':parent.style.fontSize||'20px'});
  try{scaleTypography(parent,0.7);assert.equal(parent.style.fontSize,'14px');assert.equal(child.style.fontSize,'14px');scaleTypography(parent,0.7);assert.equal(child.style.fontSize,'14px');}
  finally{globalThis.getComputedStyle=previous;}
});
