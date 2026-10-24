/** A published resolved level overrides type placement; legacy test roles stay contextual. */
export function levelIndex(graph,id) {
  const object=graph.objects[id],type=graph.model.types[object?.type];
  if(!type||type.role==='test')return -1;
  return graph.model.levels.indexOf(object.level??type.level);
}
