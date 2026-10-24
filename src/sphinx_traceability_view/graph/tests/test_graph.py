import pytest
from copy import deepcopy
from sphinx_traceability_view.graph import snapshot
from sphinx_traceability_view.model import normalize

TYPES = [{"directive": "goal", "title": "Goal", "color": "#abc"}, {"directive": "case", "title": "Case"}]
LINKS = [{"option": "verifies", "incoming": "Verified by", "outgoing": "Verifies"}]
MODEL = {"levels": ["goals"], "types": {"goal": {"level": "goals", "role": "stakeholder"}, "case": {"role": "test"}}}


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


ROW_TYPES=[{'directive':name,'title':name} for name in ['goal','case','run']]
ROW_LINKS=[{'option':name,'incoming':name+' in','outgoing':name+' out'} for name in ['checks','attempts']]
ROW_MODEL={'levels':['goals','system_cases','system_runs','software_cases','software_runs','fallback'],
 'types':{'goal':{'level':'goals','role':'stakeholder'},
 'case':{'levels_by_tag':{'sys':'system_cases','sw':'software_cases'},'fallback_level':'fallback'},
 'run':{'level_from':{'relation':'attempts','direction':'incoming','levels':{'system_cases':'system_runs','software_cases':'software_runs'}},'fallback_level':'fallback'}}}


def row_records():
    def n(id,type,**fields):return dict(id=id,type=type,title=id,docname='requirements',**fields)
    return Needs([n('G','goal'),n('S','case',tags=['sys'],checks=['G'],attempts=['ES','ESAME','EMIX']),
        n('S2','case',tags=['sys'],attempts=['ESAME']),n('W','case',tags=['sw'],attempts=['EW','EMIX']),
        n('U','case',tags=[],attempts=['EU']),n('M','case',tags=['sys','sw'],attempts=['EM']),
        n('H','case',tags=['sys'],hide=True,attempts=['EH']),
        *[n(id,'run') for id in ['ES','ESAME','EW','EMIX','EU','EM','EH','ORPHAN']],
        n('CHAIN_A','run',attempts=['CHAIN_B']),n('CHAIN_B','run',attempts=['CHAIN_A'])])


@pytest.mark.requirements('STV_SWR_061')
def test_classification_is_complete_graph_based_portable_and_deterministic():
    records=row_records();original=deepcopy(records);model=normalize(ROW_TYPES,ROW_LINKS,ROW_MODEL)
    graph,hidden=snapshot(records,model,lambda d:d+'.html','Rows')
    assert records==original and hidden=={'H'}
    assert graph['objects']['S']['level']=='system_cases'
    assert graph['objects']['W']['level']=='software_cases'
    assert graph['objects']['ES']['level']==graph['objects']['ESAME']['level']=='system_runs'
    assert graph['objects']['EW']['level']=='software_runs'
    for id in ['U','M','EMIX','EU','EM','EH','ORPHAN','CHAIN_A','CHAIN_B']:
        assert graph['objects'][id]['level']=='fallback'
        assert graph['objects'][id]['placement_fallback'] is True
    assert all('H' not in targets for links in graph['adjacency'].values() for d in links.values() for targets in d.values())
    assert graph==snapshot(Needs(reversed(records)),model,lambda d:d+'.html','Rows')[0]
    assert 'level' not in graph['objects']['G'],'fixed types keep the old additive contract'


@pytest.mark.requirements('STV_SWR_061')
@pytest.mark.parametrize('records',[Needs([dict(id='U',type='case',docname='r')]),Needs([dict(id='ORPHAN',type='run',docname='r')])])
def test_unclassified_records_without_fallback_fail_with_need_identity(records):
    model=deepcopy(ROW_MODEL)
    for placement in model['types'].values():placement.pop('fallback_level',None)
    with pytest.raises(ValueError,match=records[0]['id']+'.*placement classification'):
        snapshot(records,normalize(ROW_TYPES,ROW_LINKS,model),lambda d:d+'.html','Rows')


@pytest.mark.requirements('STV_SWR_061')
def test_outgoing_owner_mapping_and_malformed_tags_use_defined_policy():
    model=deepcopy(ROW_MODEL);model['types']['run']['level_from']['direction']='outgoing'
    records=Needs([dict(id='S',type='case',tags=['sys'],docname='r'),dict(id='R',type='run',attempts=['S'],docname='r'),dict(id='BAD',type='case',tags=None,docname='r')])
    result=snapshot(records,normalize(ROW_TYPES,ROW_LINKS,model),lambda d:d+'.html','Rows')[0]
    assert result['objects']['R']['level']=='system_runs'
    assert result['objects']['BAD']['placement_fallback']


@pytest.mark.requirements('STV_SWR_061')
def test_large_classified_graph_resolves_every_execution_from_its_case():
    records=Needs()
    for i in range(15000):
        records.append(dict(id=f'C_{i}',type='case',tags=['sys' if i%2==0 else 'sw'],attempts=[f'E_{i}'],docname='r'))
        records.append(dict(id=f'E_{i}',type='run',docname='r'))
    graph,_=snapshot(records,normalize(ROW_TYPES,ROW_LINKS,ROW_MODEL),lambda d:d+'.html','Large classified graph')
    assert len(graph['objects'])==30000 and len(graph['edges'])==15000
    for i in range(15000):
        assert graph['objects'][f'E_{i}']['level']==('system_runs' if i%2==0 else 'software_runs')
        assert 'placement_fallback' not in graph['objects'][f'E_{i}']
