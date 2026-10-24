import {build} from 'esbuild';
import {readFile,writeFile,mkdir,readdir} from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
const output='../src/sphinx_traceability_view/static';
await mkdir(output,{recursive:true});
const audit=JSON.parse(await readFile('legal/elk-inventory.json','utf8'));
const elkBytes=await readFile('node_modules/elkjs/lib/elk.bundled.js');
const elkMeta=JSON.parse(await readFile('node_modules/elkjs/package.json','utf8'));
if(elkMeta.version!==audit.elkjs.version || createHash('sha256').update(elkBytes).digest('hex')!==audit.elkjs.sha256) throw Error('ELK dependency changed: renew the compiled-dependency audit before building');
for(const name of audit.notice_files) {
  const data=await readFile(`legal/${name}`);
  if(createHash('sha256').update(data).digest('hex')!==audit.notice_sha256[name]) throw Error(`Audited legal input changed: ${name}`);
}
const built=await build({metafile:true,entryPoints:['src/render/index.js'],bundle:true,format:'iife',platform:'browser',target:['firefox115'],outfile:`${output}/stv.js`,legalComments:'eof',minify:true});
await writeFile(`${output}/stv.css`,await readFile('src/render/stv.css'));
const notices=[];
// Derive npm attributions from the actual bundle inputs; do not maintain a
// second dependency allowlist that silently omits newly bundled packages.
const bundled=new Set(Object.keys(built.metafile.inputs).filter(p=>p.startsWith('node_modules/')).map(p=>{
  const parts=p.split('/').slice(1);return parts[0].startsWith('@')?parts.slice(0,2).join('/'):parts[0];
}));
// esbuild also supplies generated runtime scaffolding.
bundled.add('esbuild');
for(const name of [...bundled].sort()) {
  const base=`node_modules/${name}`;
  const metadata=JSON.parse(await readFile(`${base}/package.json`,'utf8'));
  notices.push(`${metadata.name} ${metadata.version} (${metadata.license})`);
  const files=(await readdir(base)).filter(n=>/^(license|notice|copying)/i.test(n));
  if(!files.length) throw Error(`No legal notice found for bundled dependency ${name}`);
  for(const name of files) notices.push(await readFile(path.join(base,name),'utf8'));
}
notices.push('ELK compiled dependency inventory\n'+JSON.stringify(audit,null,2));
for(const name of audit.notice_files) notices.push(name+'\n'+await readFile(`legal/${name}`,'utf8'));
await writeFile(`${output}/THIRD_PARTY_NOTICES.txt`,notices.join('\n\n'));
await mkdir(`${output}/vendor`,{recursive:true});
await writeFile(`${output}/vendor/elk.bundled.js`,elkBytes);
await writeFile(`${output}/vendor/ELK-INVENTORY.json`,JSON.stringify(audit,null,2)+'\n');
// Legal inputs are maintained with the project, not regenerated as a source claim.
await writeFile(`${output}/LICENSE.txt`,await readFile('../LICENSE'));
const sourceNotice=await readFile(`${output}/vendor/ELK-SOURCE.txt`,'utf8');
await writeFile(`${output}/THIRD_PARTY_NOTICES.txt`,notices.join('\n\n')+'\n\n'+sourceNotice);
