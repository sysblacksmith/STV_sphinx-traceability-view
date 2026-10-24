import {levelIndex} from '../layout/level.js';
/** Order controls by semantic target placement, independent of link authorship. */
export function orderedGroups(graph,id) {
  const level=target=>levelIndex(graph,target);
  const source=level(id),groups=[];
  for(const direction of ['outgoing','incoming']) {
    for(const [relation,targets] of Object.entries(graph.adjacency[id]?.[direction]||{})) {
      if(!targets.length)continue;
      const ranks=targets.map(level);
      const order=source<0?1:ranks.every(rank=>rank>=0&&rank<source)?0:
        ranks.every(rank=>rank>source)?2:1;
      groups.push({direction,relation,targets,order});
    }
  }
  // Stable sort preserves host order among controls in the same category.
  return groups.sort((a,b)=>a.order-b.order);
}
