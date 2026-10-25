import {embeddedResource} from './resources.js';
const SVG='http://www.w3.org/2000/svg',XHTML='http://www.w3.org/1999/xhtml';
const forbidden=new Set(['SCRIPT','STYLE','IFRAME','OBJECT','EMBED','LINK','BASE','META','FORM','ANIMATE','ANIMATEMOTION','ANIMATETRANSFORM','SET']);
export function intersect(a,b){const x=Math.max(a.left,b.left),y=Math.max(a.top,b.top),right=Math.min(a.right,b.right),bottom=Math.min(a.bottom,b.bottom);return {left:x,top:y,right,bottom,width:Math.max(0,right-x),height:Math.max(0,bottom-y)};}
/** Synchronous capture owns detached DOM only; no live node survives this call. */
export function capture(workspace,{base,resources,regions=[]}={}) {
  if(document.fonts?.status==='loading')throw Error('Fonts are loading. Retry SVG export shortly.');
  const visual=window.visualViewport;
  const screen={left:visual?.offsetLeft||0,top:visual?.offsetTop||0,right:(visual?.offsetLeft||0)+(visual?.width||innerWidth),bottom:(visual?.offsetTop||0)+(visual?.height||innerHeight)};
  const crop=intersect(workspace.getBoundingClientRect(),screen);
  if(!crop.width||!crop.height)throw Error('No visible view area to export.');
  const fonts=new Set();
  function clone(node,clip) {
    if(node.nodeType===Node.TEXT_NODE)return document.createTextNode(node.data);
    if(node.nodeType!==Node.ELEMENT_NODE||forbidden.has(node.localName.toUpperCase()))return null;
    if(node.namespaceURI===SVG&&node.localName==='foreignObject')throw Error('Unsupported embedded SVG foreignObject resource.');
    if(['video','audio','canvas'].includes(node.localName))throw Error('Active media cannot be represented as a static SVG snapshot.');
    const style=getComputedStyle(node),rect=node.getBoundingClientRect();
    if(style.display==='none'||style.visibility==='hidden')return null;
    // SVG definitions have no screen rectangle but are needed for arrows/paint.
    const definition=node.namespaceURI===SVG&&!!node.closest('defs');
    const outside=!definition&&rect.width&&rect.height&&(!intersect(rect,clip).width||!intersect(rect,clip).height);
    if(outside&&(style.display!=='inline'||node.localName==='img')){
      if(node.namespaceURI===SVG||['absolute','fixed'].includes(style.position))return null;
      // Removing flow boxes changes scroll positions. Keep only their inert
      // geometry, never their text/media/identities, outside the visible crop.
      const empty=document.createElementNS(node.namespaceURI||XHTML,node.localName);
      for(const property of ['display','position','box-sizing','width','height','min-width','min-height','max-width','max-height','margin-top','margin-right','margin-bottom','margin-left','padding-top','padding-right','padding-bottom','padding-left','border-top-width','border-right-width','border-bottom-width','border-left-width','border-style','flex','order','grid-area','align-self','vertical-align','transform'])empty.style.setProperty(property,style.getPropertyValue(property));
      empty.style.visibility='hidden';empty.style.pointerEvents='none';return empty;
    }
    const copy=document.createElementNS(node.namespaceURI||XHTML,['textarea','select'].includes(node.localName)?'span':node.localName);
    for(const attr of node.attributes){if(!/^on|^data-|^aria-|^tabindex$|^style$|^srcset$|^src$|^href$|^xlink:href$/i.test(attr.name))copy.setAttributeNS(attr.namespaceURI,attr.name,attr.value);}
    for(const property of style) {
      let value=style.getPropertyValue(property);
      if(/url\(/i.test(value))value=value.replace(/url\(["']?([^"')]+)["']?\)/gi,(_,url)=>{
        if(url.startsWith('#'))return `url("${url}")`;
        const target=new URL(url,document.baseURI);
        if(target.hash&&target.pathname===new URL(document.baseURI).pathname)return `url("${target.hash}")`;
        return `url("${embeddedResource(url,base,resources)}")`;
      });
      copy.style.setProperty(property,value);
    }
    copy.style.animation='none';copy.style.transition='none';copy.style.caretColor='transparent';
    fonts.add(style.fontFamily);
    if(node.localName==='img'){
      if(!node.complete||!node.naturalWidth)throw Error('A visible image is unavailable or still loading. Retry after it loads.');
      copy.setAttribute('src',embeddedResource(node.currentSrc||node.src,base,resources));
    }
    if(node.localName==='image'){const href=node.getAttribute('href')||node.getAttribute('xlink:href');if(href)copy.setAttribute('href',embeddedResource(href,base,resources));}
    if(node.namespaceURI===SVG&&node.localName==='use'){
      const href=node.getAttribute('href')||node.getAttribute('xlink:href');
      if(href?.startsWith('#'))copy.setAttribute('href',href);else if(href)throw Error('External SVG references are not permitted.');
    }
    if(node.localName==='a'&&node.href){const url=new URL(node.getAttribute('href'),document.baseURI);if(['http:','https:','file:','mailto:','tel:'].includes(url.protocol))copy.setAttribute('href',url.href);}
    const clipping=/(hidden|auto|scroll|clip)/.test(style.overflowX+' '+style.overflowY);
    const childClip=clipping?intersect(clip,rect):clip;
    const target=(node.scrollTop||node.scrollLeft)?document.createElementNS(XHTML,'div'):copy;
    if(target!==copy){
      copy.style.overflow='hidden';copy.style.display='block';target.style.cssText=`position:relative;transform:translate(${-node.scrollLeft}px,${-node.scrollTop}px);width:${node.scrollWidth}px;flex:none;`;
      for(const property of ['display','flex-direction','flex-wrap','gap','align-items','justify-content','grid-template-columns','grid-auto-rows','grid-auto-flow'])target.style.setProperty(property,style.getPropertyValue(property));
      copy.append(target);
    }
    if(node.localName==='input'){
      copy.setAttribute('inert','');copy.removeAttribute('autofocus');
      copy.setAttribute('value',node.type==='password'?'*'.repeat(node.value.length):node.value);
      if(node.checked)copy.setAttribute('checked','');else copy.removeAttribute('checked');
      if(node.type==='image'&&node.src)copy.setAttribute('src',embeddedResource(node.src,base,resources));
    }else if(['textarea','select'].includes(node.localName)){
      const text=document.createElementNS(XHTML,'span');text.textContent=node.localName==='select'?node.selectedOptions?.[0]?.textContent||'':node.value||'';target.append(text);
    }else for(const child of node.childNodes){const value=clone(child,childClip);if(value)target.append(value);}
    for(const pseudo of node.localName==='input'?[]:['::before','::after']){
      const ps=getComputedStyle(node,pseudo),content=ps.content;
      if(content&&/^['"].*['"]$/.test(content)&&content.length>2){const span=document.createElementNS(XHTML,'span');span.textContent=content.slice(1,-1);for(const prop of ps)span.style.setProperty(prop,ps.getPropertyValue(prop));span.style.content='normal';pseudo==='::before'?target.prepend(span):target.append(span);}
    }
    return copy;
  }
  const svg=document.createElementNS(SVG,'svg');svg.setAttribute('width',crop.width);svg.setAttribute('height',crop.height);svg.setAttribute('viewBox',`0 0 ${crop.width} ${crop.height}`);svg.setAttribute('overflow','hidden');
  let background='white';
  for(let owner=workspace;owner;owner=owner.parentElement){const color=getComputedStyle(owner).backgroundColor;if(color!=='transparent'&&color!=='rgba(0, 0, 0, 0)'){background=color;break;}}
  const backdrop=document.createElementNS(SVG,'rect');backdrop.setAttribute('width',crop.width);backdrop.setAttribute('height',crop.height);backdrop.setAttribute('fill',background);svg.append(backdrop);
  for(const source of [workspace,...regions]){
    const rect=source.getBoundingClientRect();if(!intersect(rect,crop).width||!intersect(rect,crop).height)continue;
    const content=clone(source,crop);if(!content)continue;
    const wrapper=document.createElementNS(SVG,'foreignObject');wrapper.setAttribute('x',rect.left-crop.left);wrapper.setAttribute('y',rect.top-crop.top);wrapper.setAttribute('width',rect.width);wrapper.setAttribute('height',rect.height);
    content.style.position='relative';content.style.left='0';content.style.top='0';content.style.margin='0';content.style.width=`${rect.width}px`;content.style.height=`${rect.height}px`;content.style.transform='none';wrapper.append(content);svg.append(wrapper);
  }
  const selected=(resources.fonts||[]).filter(record=>[...fonts].some(f=>f.toLowerCase().includes(record.family.toLowerCase())));
  if(selected.some(f=>f.error))throw Error('A required local snapshot font is unavailable.');
  if(selected.length){const css=document.createElementNS(SVG,'style');css.textContent=selected.map(f=>f.css).join('\n');svg.prepend(css);}
  return Object.freeze({svg});
}
export function serialize(snapshot){
  const text=new XMLSerializer().serializeToString(snapshot.svg);
  if(new DOMParser().parseFromString(text,'image/svg+xml').querySelector('parsererror'))throw Error('SVG serialization failed.');
  return text;
}
