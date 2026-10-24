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
