const leases=new Map();
export function filename(id){return `stv-${String(id).replace(/[^a-z0-9_-]/gi,'_').slice(0,80)||'view'}.svg`;}
export function releaseDownloads(){for(const [url,timer]of leases){clearTimeout(timer);URL.revokeObjectURL(url);}leases.clear();}
export function saveSVG(text,id) {
  const url=URL.createObjectURL(new Blob([text],{type:'image/svg+xml;charset=utf-8'}));
  const anchor=document.createElement('a');anchor.href=url;anchor.download=filename(id);
  try{document.body.append(anchor);anchor.click();leases.set(url,setTimeout(()=>{URL.revokeObjectURL(url);leases.delete(url);},60000));}
  catch(error){URL.revokeObjectURL(url);throw error;}
  finally{anchor.remove();}
}
if(typeof window!=='undefined')window.addEventListener('pagehide',releaseDownloads);
