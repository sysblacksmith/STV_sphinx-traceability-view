const pending=new Map();
export function loadResources(graph,base) {
  const record=graph.export_resources;
  if(!record)return Promise.resolve({assets:{},fonts:[]});
  if(!pending.has(record.digest))pending.set(record.digest,new Promise((resolve,reject)=>{
    const cached=globalThis.__STV_DATA__?.resources?.[record.digest];
    if(cached){resolve(cached);return;}
    const script=document.createElement('script');script.src=new URL(record.url,base).href;
    script.onload=()=>{script.remove();const data=globalThis.__STV_DATA__?.resources?.[record.digest];data?resolve(data):reject(Error('Export resource registration unavailable.'));};
    script.onerror=()=>{script.remove();pending.delete(record.digest);reject(Error('Local export resources unavailable. Reload the page to retry.'));};
    document.head.append(script);
  }));
  return pending.get(record.digest);
}
export function embeddedResource(value,base,records) {
  if(/^data:image\/(png|jpeg|gif|webp);base64,[a-z0-9+/=]+$/i.test(value))return value;
  const url=new URL(value,base),output=new URL(base);
  if(url.protocol!==output.protocol||url.host!==output.host||!url.pathname.startsWith(output.pathname))throw Error('External snapshot resource is not permitted.');
  const path=decodeURIComponent(url.pathname.slice(output.pathname.length));
  const record=Object.hasOwn(records.assets,path)?records.assets[path]:undefined;
  if(!record||record.error)throw Error(`Cannot export local resource ${path}: ${record?.error||'resource not bundled'}`);
  return record.data+(url.hash||'');
}
