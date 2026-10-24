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
        selectors = [key for key in ("level", "levels_by_tag", "level_from") if key in placement]
        path = f"traceability_view_model.types.{name}"
        if role == "test":
            if selectors or "fallback_level" in placement:
                raise ValueError(f"{path}: legacy test role cannot have a level selector")
        elif role not in (None, "stakeholder") or len(selectors) != 1:
            raise ValueError(f"{path}: expected one level/role placement")
        elif role == "stakeholder" and selectors != ["level"]:
            raise ValueError(f"{path}: stakeholder role requires a fixed level")
        elif selectors == ["level"]:
            if placement["level"] not in levels or "fallback_level" in placement:
                raise ValueError(f"{path}: invalid fixed level placement")
        else:
            selector = selectors[0]
            value = placement[selector]
            if selector == "level_from":
                if (not isinstance(value, dict) or set(value) != {"relation", "direction", "levels"}
                        or not isinstance(value["relation"], str)
                        or value["direction"] not in ("incoming", "outgoing")):
                    raise ValueError(f"{path}.level_from: expected relation, direction and levels")
                value = value["levels"]
            if (not isinstance(value, dict) or not value
                    or any(not isinstance(key, str) or not key or not isinstance(target, str)
                           or target not in levels for key, target in value.items())):
                raise ValueError(f"{path}.{selector}: expected nonempty level mapping")
            if "fallback_level" in placement and placement["fallback_level"] not in levels:
                raise ValueError(f"{path}.fallback_level: unknown level")
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
    owner_levels = {p["level"] for p in types.values() if "level" in p}
    owner_levels.update(level for p in types.values() for level in p.get("levels_by_tag", {}).values())
    owner_levels.update(p["fallback_level"] for p in types.values()
                        if "levels_by_tag" in p and "fallback_level" in p)
    for name, placement in types.items():
        if "level_from" not in placement:
            continue
        rule = placement["level_from"]
        path = f"traceability_view_model.types.{name}.level_from"
        if rule["relation"] not in model["relations"]:
            raise ValueError(f"{path}.relation: unknown host relation")
        if not set(rule["levels"]).issubset(owner_levels):
            raise ValueError(f"{path}.levels: owners must use fixed/tag-resolved levels")
    return model


DETAILS_LIMIT_DEFAULT = 10


def validate_details_limit(value=DETAILS_LIMIT_DEFAULT):
    """Keep author capacity exact across Python and the JavaScript consumer."""
    if type(value) is not int or not 1 <= value <= 9007199254740991:
        raise ValueError("traceability_view_details_limit: expected a positive integer no greater than 9007199254740991")
    return value
