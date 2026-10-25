import test from 'node:test';
import assert from 'node:assert/strict';
import {setRows} from '../page-metadata.js';
function element(...values){const classes=new Set(values);return {classes,classList:{contains:name=>classes.has(name),toggle:(name,on)=>on?classes.add(name):classes.delete(name)}};}
test('STV_SWR_069 bulk state normalizes mixed rows and repeated actions never invert them',()=>{
  const rows=[element('meta','collapse_is_hidden'),element('meta')],icons=[element('collapsed'),element('visible')];
  setRows(rows,icons,false);setRows(rows,icons,false);
  assert.ok(rows.every(r=>r.classes.has('collapse_is_hidden')&&r.classes.has('meta')));
  assert.equal(icons[0].classes.has('collapse_is_hidden'),true);assert.equal(icons[1].classes.has('collapse_is_hidden'),false);
  setRows(rows,icons,true);setRows(rows,icons,true);assert.ok(rows.every(r=>!r.classes.has('collapse_is_hidden')));
  assert.equal(icons[0].classes.has('collapse_is_hidden'),false);assert.equal(icons[1].classes.has('collapse_is_hidden'),true);
});
