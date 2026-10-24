import {build} from 'esbuild';
import {readFile,writeFile,mkdir,readdir} from 'node:fs/promises';
import path from 'node:path';
const output='../src/sphinx_traceability_view/static';
await mkdir(output,{recursive:true});
await build({entryPoints:['src/render/index.js'],bundle:true,format:'iife',platform:'browser',target:['firefox115'],outfile:`${output}/stv.js`,legalComments:'eof',minify:true});
await writeFile(`${output}/stv.css`,await readFile('src/render/stv.css'));
const notices=[];
for(const folder of await readdir('node_modules')) {
  const children=folder.startsWith('@') ? (await readdir(`node_modules/${folder}`)).map(c=>`${folder}/${c}`) : [folder];
  for(const child of children) {
    const base=`node_modules/${child}`;
    try {
      const metadata=JSON.parse(await readFile(`${base}/package.json`,'utf8'));
      if(!['elkjs','d3-selection','d3-zoom','d3-dispatch','d3-drag','d3-interpolate','d3-transition','d3-color','d3-ease','d3-timer','@floating-ui/dom','@floating-ui/core','@floating-ui/utils'].includes(metadata.name)) continue;
      notices.push(`${metadata.name} ${metadata.version} (${metadata.license})`);
      for(const name of await readdir(base)) if(/^(license|notice|copying)/i.test(name)) notices.push(await readFile(path.join(base,name),'utf8'));
    } catch(error) {if(error.code!=='ENOENT') throw error;}
  }
}
await writeFile(`${output}/THIRD_PARTY_NOTICES.txt`,notices.join('\n\n'));
await mkdir(`${output}/vendor`,{recursive:true});
await writeFile(`${output}/vendor/elk.bundled.js`,await readFile('node_modules/elkjs/lib/elk.bundled.js'));
await writeFile(`${output}/vendor/ELK-SOURCE.txt`, 'ELK.js 0.10.0, unmodified bundled JavaScript source.\nEPL-2.0; upstream source: https://github.com/kieler/elkjs/tree/v0.10.0\nThe adjacent elk.bundled.js is the unmodified distributed source used by this runtime.\n');
