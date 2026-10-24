// Transport markers are generated for output-local paths, never arbitrary URLs.
export function detailURL(value,base,{image=false}={}) {
  const raw=String(value).trim();
  if(!raw || /[\u0000-\u001f\u007f\\]/.test(raw))return null;
  if(image && /^data:image\/(?:png|jpeg|gif|webp)(?:;[^,]*)?,/i.test(raw))return raw;
  if(/^[a-z][a-z0-9+.-]*:/i.test(raw) || raw.startsWith('/') || /%(?:2f|5c)/i.test(raw.split(/[?#]/,1)[0]))return null;
  try {
    const root=new URL('.',base),url=new URL(raw,root);
    if(!['file:','http:','https:'].includes(root.protocol) || url.protocol!==root.protocol || url.origin!==root.origin || !url.pathname.startsWith(root.pathname))return null;
    return url;
  } catch {return null;}
}

export function detailCSS(value,base) {
  // Python emits canonical quoted url() values. Reject alternate/escaped
  // transport syntax rather than restoring an unchecked browser resource.
  const css=String(value).replace(/\/\*[\s\S]*?\*\//g,'');
  if(/[\\]|@import/i.test(css))return '';
  const pattern=/url\(\s*"([^"]*)"\s*\)/gi;
  if(/url\s*\(/i.test(css.replace(pattern,'')))return '';
  return css.replace(pattern,(_,raw)=>{
    const target=detailURL(raw,base,{image:true});
    return target ? `url("${String(target).replaceAll('"','%22')}")` : 'none';
  });
}
