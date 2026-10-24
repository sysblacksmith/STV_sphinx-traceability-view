export const DEFAULT_DETAILS_LIMIT=10;
/** Insertion order is opening age; reads/reuse never refresh it. */
export function detailCollection(limit=DEFAULT_DETAILS_LIMIT) {
  if(!Number.isSafeInteger(limit)||limit<1)throw Error('traceability_view_details_limit must be a positive safe integer.');
  const entries=new Map();
  return {entries,limit,
    open(id,create) {
      if(entries.has(id))return {entry:entries.get(id),reused:true};
      const entry=create();let evicted;
      if(entries.size>=limit) {const oldest=entries.keys().next().value;evicted=entries.get(oldest);entries.delete(oldest);}
      entries.set(id,entry);return {entry,reused:false,evicted};
    },
    close(id) {const entry=entries.get(id);entries.delete(id);return entry;},
    clear() {const removed=[...entries.values()];entries.clear();return removed;}
  };
}
