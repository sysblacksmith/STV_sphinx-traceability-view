"""Content-addressed classic scripts, committed only after complete extraction."""
import hashlib
import json
import os


def encoded(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")).replace("<", "\\u003c")


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(value, encoding="utf-8")
    os.replace(temporary, path)


def emit(graph, fragments, output):
    graph = dict(graph, details={})
    files = {}
    for identity, fragment in fragments.items():
        content_hash = digest(fragment)
        name = f"_static/stv/details/{digest(identity)}-{content_hash}.js"
        graph["details"][identity] = {"url": name, "digest": content_hash}
        files[name] = 'globalThis.__STV_DATA__ ||= {graphs:{},fragments:{}};globalThis.__STV_DATA__.fragments[' + encoded(content_hash) + '] = ' + encoded(fragment) + ';'
    identity = digest(encoded(graph))
    graph["identity"] = identity
    name = f"_static/stv/graph-{identity}.js"
    # JSON.parse preserves data keys such as __proto__; object-literal source
    # would interpret that key as a prototype assignment. Null dictionaries
    # also prevent missing IDs such as "constructor" resolving through inheritance.
    files[name] = 'globalThis.__STV_DATA__ ||= {graphs:{},fragments:{}};globalThis.__STV_DATA__.graphs[' + encoded(identity) + '] = JSON.parse(' + encoded(encoded(graph)) + ',(_,v)=>v&&typeof v==="object"&&!Array.isArray(v)?Object.assign(Object.create(null),v):v);'
    for relative, content in files.items():
        atomic(output / relative, content)
    return identity, name
