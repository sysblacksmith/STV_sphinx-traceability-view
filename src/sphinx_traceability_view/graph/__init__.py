"""Adapt the completed NeedsView into deterministic, bidirectional graph data."""
from urllib.parse import urlsplit
from collections.abc import Mapping
from .placement import resolve_placements


def metadata_value(value):
    if isinstance(value, Mapping):
        return {str(key): metadata_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [metadata_value(item) for item in value]
    if isinstance(value, (str, int, float, bool, type(None))):
        return value
    return str(value)


def snapshot(needs, model, uri, project):
    records = list(needs.to_list_with_parts())
    hidden = {n.get("id_complete", n["id"]) for n in records if n.get("hide")}
    hidden.update(n.get("id_complete", n["id"]) for n in records if n.get("id_parent") in hidden)
    objects = {}
    for n in records:
        identity = n.get("id_complete", n["id"])
        if identity in hidden:
            continue
        original = n.get("external_url") if n.get("is_external") else uri(n["docname"]) + "#" + identity
        if not original or urlsplit(original).scheme.lower() not in ("", "http", "https"):
            raise ValueError(f"Need {identity!r}: original documentation URL must be a local path or HTTP(S) URL")
        objects[identity] = {"id": identity, "title": n.get("title", n.get("content", "")),
                             "type": n["type"], "status": n.get("status") or "",
                             "url": original, "docname": n.get("docname"),
                             "parent": n.get("id_parent") if n.get("is_part") else None,
                             "external": bool(n.get("is_external"))}
        if n.get("is_external"):
            excluded = set(model["relations"]) | {name + "_back" for name in model["relations"]} | {"parts"}
            objects[identity]["metadata"] = {key: metadata_value(value) for key, value in n.items()
                if key not in excluded}
    edges = set()
    for n in records:
        source = n.get("id_complete", n["id"])
        if source not in objects:
            continue
        for relation in model["relations"]:
            for target in n.get(relation, []):
                if target not in hidden:
                    edges.add((source, relation, target))
    adjacency = {i: {"incoming": {}, "outgoing": {}} for i in objects}
    for source, relation, target in sorted(edges):
        adjacency[source]["outgoing"].setdefault(relation, []).append(target)
        if target in objects:
            adjacency[target]["incoming"].setdefault(relation, []).append(source)
    resolve_placements({n.get("id_complete", n["id"]): n for n in records}, objects, adjacency, model)
    return {"schema": 1, "project": project, "model": model,
            "objects": dict(sorted(objects.items())), "edges": sorted(edges), "adjacency": adjacency,
            "entries": sorted(i for i, n in objects.items() if not n["parent"] and model["types"][n["type"]].get("role") == "stakeholder")}, hidden
