// Design feasibility check, not a product acceptance test.
// Run after npm ci in this directory: node check-stack.mjs
import ELK from 'elkjs/lib/elk.bundled.js';
import {build} from 'esbuild';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {dirname} from 'node:path';

const elk = new ELK({algorithms: ['layered']});
const graph = {
  id: 'root',
  layoutOptions: {'elk.algorithm': 'layered', 'elk.direction': 'DOWN', 'elk.randomSeed': '1'},
  children: ['a', 'b', 'c'].map(id => ({id, width: 280, height: 140})),
  edges: [
    {id: 'ab', sources: ['a'], targets: ['b']},
    {id: 'bc', sources: ['b'], targets: ['c']},
    {id: 'ca', sources: ['c'], targets: ['a']},
  ],
};
const result = await elk.layout(graph);
assert(result.children.every(node => Number.isFinite(node.x) && Number.isFinite(node.y)));

const output = await build({
  stdin: {
    contents: `import ELK from 'elkjs/lib/elk.bundled.js';
      import {select} from 'd3-selection';
      import {zoom} from 'd3-zoom';
      import {computePosition,flip,shift,size,autoUpdate} from '@floating-ui/dom';
      globalThis.STVTechnologyCheck = {ELK,select,zoom,computePosition,flip,shift,size,autoUpdate};`,
    resolveDir: dirname(fileURLToPath(import.meta.url)),
  },
  bundle: true,
  format: 'iife',
  platform: 'browser',
  target: 'firefox128',
  splitting: false,
  write: false,
  metafile: true,
  legalComments: 'eof',
  minify: true,
});
const code = output.outputFiles[0].text;
assert(!/\bimport\s*\(/.test(code));
assert(Object.values(output.metafile.outputs).every(file => file.imports.length === 0));
console.log(JSON.stringify({
  elkCycleNodes: result.children.length,
  bundleBytes: Buffer.byteLength(code),
  bundledInputs: Object.keys(output.metafile.inputs).length,
  unresolvedImports: false,
}));
