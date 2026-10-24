import {persistentDetails} from '../../../frontend/src/inspect/persistent.js';
const root=document.getElementById('race-view'),stack=root.querySelector('.stv-details-stack'),workspace=root.querySelector('.stv-workspace'),fallback=root.querySelector('.stv-close-all');
const graph={identity:'controlled',details_limit:1,objects:{A:{title:'A',url:'a.html#A'},B:{title:'B',url:'b.html#B'}}};
const calls=[];
const manager=persistentDetails(root,graph,new URL('./',location.href),{stack,fallback,
  findTrigger:id=>document.getElementById('trigger-'+id),
  changed:size=>{stack.hidden=!size;workspace.classList.toggle('stv-has-details',size>0);},
  load:(_,id)=>new Promise((resolve,reject)=>calls.push({id,resolve,reject}))});
for(const id of ['A','B'])document.getElementById('trigger-'+id).onclick=()=>manager.open(id);
fallback.onclick=()=>manager.clear();
globalThis.persistentHarness={manager,calls};
