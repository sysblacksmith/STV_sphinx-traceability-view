from copy import deepcopy
import pytest
from sphinx_traceability_view.model import normalize

TYPES = [{"directive": "goal", "title": "Goal", "color": "#abc"}, {"directive": "case", "title": "Case"}]
LINKS = [{"option": "verifies", "incoming": "Verified by", "outgoing": "Verifies"}]
MODEL = {"levels": ["goals"], "types": {"goal": {"level": "goals", "role": "stakeholder"}, "case": {"role": "test"}}}


@pytest.mark.requirements("STV_SWR_014", "STV_SWR_030", "STV_SWR_032", "STV_SWR_036", "STV_SWR_045")
def test_host_normalization():
    source = deepcopy(MODEL)
    model = normalize(TYPES, LINKS, source, True)
    assert source == MODEL
    assert model["types"]["goal"]["color"] == "#abc"
    assert model["types"]["case"]["color"]
    assert model["relations"]["verifies"]["incoming"] == "Verified by"
    assert model["accepted_statuses"] == ["accepted"]
    source["accepted_statuses"] = ["approved"]
    assert normalize(TYPES, LINKS, source)["accepted_statuses"] == ["approved"]
    assert normalize(list(reversed(TYPES)), LINKS, source)['types']['case']['color']==model['types']['case']['color']


@pytest.mark.requirements("STV_SWR_036")
@pytest.mark.parametrize("change,path", [
    ({"levels": ["goals", "goals"]}, "levels"),
    ({"types": {"goal": {"level": "unknown"}, "case": {"role": "test"}}}, "types.goal"),
    ({"types": {}}, "types"), ({"accepted_statuses": "accepted"}, "accepted_statuses")])
def test_invalid_model(change, path):
    with pytest.raises(ValueError, match=path):
        normalize(TYPES, LINKS, dict(MODEL, **change))


@pytest.mark.requirements('STV_SWR_036','STV_SWR_045')
@pytest.mark.parametrize('incoming',['', ' ', None, 1])
def test_invalid_directional_labels(incoming):
    with pytest.raises(ValueError,match='needs_links.verifies'):
        normalize(TYPES,[dict(LINKS[0],incoming=incoming)],MODEL)


CLASSIFIED_TYPES = TYPES + [{"directive": "run", "title": "Run"}]
CLASSIFIED_LINKS = LINKS + [{"option": "attempts", "incoming": "Of case", "outgoing": "Attempts"}]
CLASSIFIED_MODEL = {"levels": ["goals", "system_cases", "system_runs", "software_cases", "software_runs", "fallback"],
    "types": {"goal": {"level": "goals", "role": "stakeholder"},
              "case": {"levels_by_tag": {"sys": "system_cases", "sw": "software_cases"}, "fallback_level": "fallback"},
              "run": {"level_from": {"relation": "attempts", "direction": "incoming", "levels": {"system_cases": "system_runs", "software_cases": "software_runs"}}, "fallback_level": "fallback"}}}


@pytest.mark.requirements('STV_SWR_061')
def test_classified_model_is_portable_and_does_not_mutate_input():
    original=deepcopy(CLASSIFIED_MODEL)
    model=normalize(CLASSIFIED_TYPES,CLASSIFIED_LINKS,original,True)
    assert original==CLASSIFIED_MODEL
    assert model['types']['case']['levels_by_tag']['sys']=='system_cases'
    assert model['types']['run']['level_from']['relation']=='attempts'


@pytest.mark.requirements('STV_SWR_061')
@pytest.mark.parametrize('placement,path',[
    ({'levels_by_tag':{}},'levels_by_tag'),
    ({'levels_by_tag':{'sys':'absent'}},'levels_by_tag'),
    ({'levels_by_tag':{'':'system_cases'}},'levels_by_tag'),
    ({'level':'goals','levels_by_tag':{'sys':'system_cases'}},'types.case'),
    ({'role':'test','levels_by_tag':{'sys':'system_cases'}},'types.case'),
    ({'role':'stakeholder','levels_by_tag':{'sys':'system_cases'}},'types.case'),
    ({'levels_by_tag':{'sys':'system_cases'},'fallback_level':'absent'},'fallback_level'),
    ({'level_from':{'relation':'absent','direction':'incoming','levels':{'goals':'system_cases'}}},'level_from.relation'),
    ({'level_from':{'relation':'attempts','direction':'sideways','levels':{'goals':'system_cases'}}},'level_from'),
    ({'level_from':{'relation':'attempts','direction':'incoming','levels':{}}},'level_from'),
    ({'level_from':{'relation':'attempts','direction':'incoming','levels':{'system_runs':'system_cases'}}},'level_from.levels'),
    ({'level':'goals','fallback_level':'fallback'},'fixed level'),
])
def test_classified_model_rejects_invalid_selectors(placement,path):
    model=deepcopy(CLASSIFIED_MODEL);model['types']['case']=placement
    # Remove the other owner map when it would depend on the removed tag map.
    model['types']['run']={'level':'software_runs'}
    with pytest.raises(ValueError,match=path):normalize(CLASSIFIED_TYPES,CLASSIFIED_LINKS,model)
