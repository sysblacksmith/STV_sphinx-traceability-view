"""Resolve evidence placement from complete published metadata, never view state."""


def resolve_placements(records, objects, adjacency, model):
    types = model["types"]
    resolved = {}

    def assign(identity, choices):
        placement = types[objects[identity]["type"]]
        if len(choices) == 1:
            level = next(iter(choices))
        else:
            level = placement.get("fallback_level")
            if level is None:
                raise ValueError(f"Need {identity!r}: placement classification is missing or conflicting")
            objects[identity]["placement_fallback"] = True
        objects[identity]["level"] = level
        resolved[identity] = level

    for identity, obj in objects.items():
        placement = types[obj["type"]]
        if "level" in placement:
            resolved[identity] = placement["level"]
        elif "levels_by_tag" in placement:
            tags = records[identity].get("tags") or []
            if not isinstance(tags, (list, tuple, set, frozenset)):
                tags = []
            assign(identity, {level for tag, level in placement["levels_by_tag"].items() if tag in tags})

    for identity, obj in objects.items():
        placement = types[obj["type"]]
        if "level_from" not in placement:
            continue
        rule = placement["level_from"]
        owners = adjacency[identity][rule["direction"]].get(rule["relation"], [])
        choices = set()
        complete = bool(owners)
        for owner in owners:
            other = objects.get(owner)
            if other and "level_from" in types[other["type"]]:
                complete = False
                continue
            target = rule["levels"].get(resolved.get(owner))
            if target is None or (other and other.get("placement_fallback")):
                complete = False
            else:
                choices.add(target)
        assign(identity, choices if complete else set())
