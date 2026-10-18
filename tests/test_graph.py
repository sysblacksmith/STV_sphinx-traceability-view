import pytest
from sphinx_traceability_view.graph import snapshot
from test_model import normalize, TYPES, LINKS, MODEL


class Needs(list):
    def to_list_with_parts(self):
        return self


@pytest.mark.requirements("STV_SWR_013", "STV_SWR_027", "STV_SWR_047", "STV_SWR_048")
def test_hidden_parts_external_and_missing_targets():
    model = normalize(TYPES, LINKS, MODEL)
    base = dict(type="goal", title="Title", status="accepted", docname="nested/requirements")
    needs = Needs([
        dict(base, id="A", verifies=["B", "HIDDEN", "MISSING", "HIDDEN.part", "A.part"]),
        dict(base, id="B", is_external=True, docname=None, external_url="https://example.org/B", constraints_results={'rule':{'passed':True}}),
        dict(base, id="HIDDEN", hide=True),
        dict(base, id="part", id_complete="HIDDEN.part", id_parent="HIDDEN", is_part=True),
        dict(base, id="part", id_complete="A.part", id_parent="A", is_part=True),
    ])
    def uri(docname):
        assert docname is not None
        return docname + ".html"
    graph, hidden = snapshot(needs, model, uri, "Project")
    assert set(graph["objects"]) == {"A", "A.part", "B"}
    assert hidden == {"HIDDEN", "HIDDEN.part"}
    assert graph["entries"] == ["A", "B"]
    assert graph["objects"]["B"]["url"] == "https://example.org/B"
    assert graph["objects"]["B"]["metadata"]['constraints_results']=={'rule':{'passed':True}}
    assert graph["objects"]["A.part"]["url"].endswith("#A.part")
    assert graph["adjacency"]["A"]["outgoing"]["verifies"] == ["A.part", "B", "MISSING"]
    assert graph["adjacency"]["B"]["incoming"]["verifies"] == ["A"]
    assert "MISSING" not in graph["objects"]


@pytest.mark.requirements('STV_SWR_047')
@pytest.mark.parametrize('url',['javascript:bad()','data:text/html,bad','file:///private.html'])
def test_external_original_url_rejects_executable_or_nonportable_navigation(url):
    model=normalize(TYPES,LINKS,MODEL)
    needs=Needs([dict(id='EXTERNAL',type='goal',is_external=True,external_url=url)])
    with pytest.raises(ValueError,match='EXTERNAL.*original documentation URL'):
        snapshot(needs,model,lambda name:name+'.html','Project')
