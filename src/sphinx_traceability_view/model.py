"""Validate layout metadata without altering the host schema."""
from copy import deepcopy

DEFAULT = {
    "levels": ["stakeholder", "system", "system_arch", "software", "software_arch"],
    "types": {"shr": {"level": "stakeholder", "role": "stakeholder"},
              "sysr": {"level": "system"}, "syse": {"level": "system_arch"},
              "swr": {"level": "software"}, "swe": {"level": "software_arch"}},
    "accepted_statuses": ["accepted"],
}
PALETTE = ["#dceaf7", "#e1efdc", "#f7e5ca", "#e9ddf2", "#d8efeb"]


def normalize(host_types, host_links, supplied=None, project_mode=False):
    model = deepcopy(DEFAULT if supplied is None else supplied)
    if not isinstance(model, dict):
        raise ValueError("traceability_view_model: expected a mapping")
    levels = model.get("levels")
    if not isinstance(levels, list) or not levels or any(not isinstance(x, str) or not x for x in levels) or len(set(levels)) != len(levels):
        raise ValueError("traceability_view_model.levels: expected unique nonempty level names")
    types = model.get("types", {})
    if not isinstance(types, dict):
        raise ValueError("traceability_view_model.types: expected a mapping")
    names = {t["directive"] for t in host_types}
    if set(types) != names:
        raise ValueError(f"traceability_view_model.types: missing {sorted(names-set(types))}; unknown {sorted(set(types)-names)}")
    host = {t["directive"]: t for t in host_types}
    for index, name in enumerate(sorted(names)):
        placement = types[name]
        if not isinstance(placement, dict):
            raise ValueError(f"traceability_view_model.types.{name}: expected a mapping")
        role = placement.get("role")
        if role not in (None, "stakeholder", "test") or (role == "test" and "level" in placement) or (role != "test" and placement.get("level") not in levels):
            raise ValueError(f"traceability_view_model.types.{name}: invalid level/role placement")
        placement["color"] = host[name].get("color") or PALETTE[index % len(PALETTE)]
        placement["title"] = host[name].get("title", name)
    if project_mode and not any(t.get("role") == "stakeholder" for t in types.values()):
        raise ValueError("traceability_view_model.types: project mode requires a stakeholder role")
    statuses = model.setdefault("accepted_statuses", ["accepted"])
    if not isinstance(statuses, list) or any(not isinstance(x, str) for x in statuses):
        raise ValueError("traceability_view_model.accepted_statuses: expected a list of strings")
    model["relations"] = {}
    relations = ({"option": name, **value} for name, value in host_links.items()) if isinstance(host_links, dict) else host_links
    for relation in relations:
        name = relation["option"]
        if any(not isinstance(relation.get(direction), str) or not relation[direction].strip()
               for direction in ("incoming", "outgoing")):
            raise ValueError(f"needs_links.{name}: incoming and outgoing labels are required")
        model["relations"][name] = {k: relation[k] for k in ("incoming", "outgoing")}
    return model
