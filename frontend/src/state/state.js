/** Pure, seed-rooted shared-identity state. Keys are JSON tuples. */
export const groupKey = (id, relation, direction) => JSON.stringify([id, relation, direction]);
export const PAGE_SIZE = 5;
export function initial(seedIds = []) {
  return {mode: seedIds.length ? 'seeds' : 'project', seeds: [...new Set(seedIds)],
    expanded: new Set(), pages: new Map(), page: 0, rootOpen: !seedIds.length, revision: 0};
}
export function visible(graph, state) {
  const ids = new Set(state.mode === 'seeds' ? state.seeds : []);
  const entries = state.mode === 'project' && state.rootOpen ? graph.entries.slice(state.page * PAGE_SIZE, (state.page + 1) * PAGE_SIZE) : [];
  entries.forEach(id => ids.add(id));
  const count = () => ids.size + (state.mode === 'project' ? 1 : 0);
  if (count() > 200) throw Error('200-node limit: collapse branches before expanding this group.');
  const queue = [...ids], edges = new Map();
  for (let offset = 0; offset < queue.length; offset++) {
    const id = queue[offset];
    for (const direction of ['outgoing', 'incoming']) {
      for (const [relation, targets] of Object.entries(graph.adjacency[id]?.[direction] || {})) {
        if (!state.expanded.has(groupKey(id, relation, direction))) continue;
        for (const target of targets) {
          const edge = direction === 'outgoing' ? [id, relation, target] : [target, relation, id];
          edges.set(JSON.stringify(edge), edge);
          if (!ids.has(target)) { ids.add(target); queue.push(target); }
          if (count() > 200) throw Error('200-node limit: collapse branches before expanding this group.');
        }
      }
    }
  }
  return {ids: [...ids], edges: [...edges.values()], project: state.mode === 'project', entries};
}
export function transition(graph, current, command) {
  const next = {...current, expanded: new Set(current.expanded), pages: new Map(current.pages), revision: current.revision + 1};
  try {
    if (command.type === 'collapse-all') {
      Object.assign(next,initial(current.mode==='seeds'?current.seeds:[]),{revision:current.revision+1});
    } else if (command.type === 'seed') {
      const id=typeof command.id==='string'?command.id.trim():'';
      if(!id || !Object.hasOwn(graph.objects,id))throw Error('Choose an existing Need ID.');
      Object.assign(next,initial([id]),{revision:current.revision+1});
    } else if (command.type === 'overview') {
      Object.assign(next,initial(),{revision:current.revision+1});
    } else if (command.type === 'group') {
      const {id, relation, direction} = command;
      if (!visible(graph, current).ids.includes(id) || !graph.adjacency[id]?.[direction]?.[relation]?.length)
        throw Error('This relationship group is unavailable.');
      const key = groupKey(id, relation, direction);
      next.expanded.has(key) ? next.expanded.delete(key) : next.expanded.add(key);
    } else if (command.type === 'root') {
      if (current.mode !== 'project' || !graph.entries.length) throw Error('No stakeholder requirements.');
      next.rootOpen = !current.rootOpen;
    } else if (command.type === 'page') {
      if (current.mode!=='project' || !current.rootOpen || !Number.isInteger(command.page) || command.page < 0 || command.page >= Math.ceil(graph.entries.length / PAGE_SIZE))
        throw Error('This stakeholder page is unavailable.');
      next.pages.set(current.page, new Set(current.expanded));
      next.page = command.page;
      next.expanded = new Set(next.pages.get(next.page) || []);
    } else throw Error('Unknown exploration command.');
    return {state: next, graph: visible(graph, next)};
  } catch (error) { return {state: current, error: error.message}; }
}
