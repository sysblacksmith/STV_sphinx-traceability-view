import json
import subprocess
import pytest
from sphinx_traceability_view.bundle import emit


@pytest.mark.requirements('STV_SWR_017','STV_SWR_018','STV_SWR_027')
def test_classic_registration_treats_prototype_keys_and_script_text_as_data(tmp_path):
    graph={'schema':1,'objects':{'__proto__':{'id':'__proto__','title':'</script>\u2028'}},'adjacency':{'__proto__':{'incoming':{},'outgoing':{}}}}
    identity,path=emit(graph,{'__proto__':'<p>Published body</p>'},tmp_path)
    script=(tmp_path/path).read_text(encoding='utf-8')
    assert '</script>' not in script
    result=subprocess.run(['node','-e','require(process.argv[1]);const g=Object.values(globalThis.__STV_DATA__.graphs)[0];process.stdout.write(JSON.stringify({ids:Object.keys(g.objects),prototype:Object.getPrototypeOf(g.objects),missing:typeof g.objects.constructor,title:g.objects.__proto__.title}));',str(tmp_path/path)],capture_output=True,text=True,encoding='utf-8')
    assert result.returncode==0,result.stderr
    data=json.loads(result.stdout)
    assert data=={'ids':['__proto__'],'prototype':None,'missing':'undefined','title':graph['objects']['__proto__']['title']}
