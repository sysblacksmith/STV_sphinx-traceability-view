import test from 'node:test';
import assert from 'node:assert/strict';
import {seedCatalog,seedMatches} from '../src/seeds.js';
test('STV_SWR_057: local suggestions match IDs and titles and bound results',()=>{
 const catalog=seedCatalog({objects:Object.fromEntries(Array.from({length:15},(_,i)=>['ID_'+i,{title:'Example '+i}]))});
 assert.equal(seedMatches(catalog,' example ').total,15);
 assert.equal(seedMatches(catalog,'example').items.length,10);
 assert.equal(seedMatches(catalog,'id_14').items[0].id,'ID_14');
 assert.equal(seedMatches(catalog,'').total,0);
 assert.equal(seedMatches(catalog,'hidden').total,0);
});
