from pathlib import Path
import json
import os
import subprocess
import sys
import pytest
import shutil
from bs4 import BeautifulSoup

FIXTURE = Path(__file__).parent / "fixtures" / "minimal"


def manifest(output):
    soup = BeautifulSoup((output / "index.html").read_text(encoding="utf-8"), "html.parser")
    path = output / soup.select_one("script[data-stv-graph]")["src"]
    script=path.read_text(encoding="utf-8").rsplit(" = ", 1)[1]
    encoded_payload,_=json.JSONDecoder().raw_decode(script.removeprefix('JSON.parse('))
    return json.loads(encoded_payload)


def build(source, output, *options):
    env = dict(os.environ, PYTHONPATH=str(Path(__file__).parents[2] / "src"))
    return subprocess.run([sys.executable, "-m", "sphinx", "-b", "html", "-W", "--keep-going", *options, str(source), str(output)], env=env, capture_output=True, text=True)


@pytest.mark.requirements("STV_SYS_001", "STV_SWR_001", "STV_SWR_002", "STV_SWR_013", "STV_SWR_026")
def test_cross_page_bundle(tmp_path):
    result = build(FIXTURE, tmp_path)
    assert result.returncode == 0, result.stdout + result.stderr
    html = (tmp_path / "index.html").read_text(encoding="utf-8")
    assert "STV_PENDING" not in html
    soup = BeautifulSoup(html, "html.parser")
    roots = soup.select(".stv-view")
    assert len(roots) == 2
    assert json.loads(roots[0]["data-stv-seeds"]) == ["ROOT_A", "LEAF_B"]
    assert json.loads(roots[1]["data-stv-seeds"]) == []
    script = soup.select_one("script[data-stv-graph]")
    assert (tmp_path / script["src"]).is_file()
    fragments = list((tmp_path / "_static/stv/details").glob("*.js"))
    assert len(fragments) == 2
    assert any("formatted body" in p.read_text() for p in fragments)


@pytest.mark.requirements("STV_SYS_001", "STV_SWR_026", "STV_SWR_048")
@pytest.mark.parametrize("seed", ["UNKNOWN", "ROOT_A UNKNOWN", "HIDDEN_A"])
def test_invalid_seed_source_location(tmp_path, seed):
    source = tmp_path / "source"
    shutil.copytree(FIXTURE, source)
    (source / "index.rst").write_text(f"Invalid\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: {seed}\n", encoding="utf-8")
    with (source / "requirements.rst").open("a", encoding="utf-8") as stream:
        stream.write("\n.. shr:: Hidden\n   :id: HIDDEN_A\n   :hide:\n")
    result = build(source, tmp_path / "html")
    assert result.returncode != 0
    assert "index.rst:8" in result.stderr
    assert "unknown or hidden starting ID" in result.stderr


@pytest.mark.requirements("STV_SWR_027", "STV_SWR_028")
def test_host_owns_broken_trace_failure(tmp_path):
    source = tmp_path / "source"
    shutil.copytree(FIXTURE, source)
    with (source / "conf.py").open("a", encoding="utf-8") as stream:
        stream.write('\nneeds_report_dead_links = True\n')
    path = source / "requirements.rst"
    path.write_text(path.read_text(encoding="utf-8").replace(":traces: LEAF_B", ":traces: MISSING_A"), encoding="utf-8")
    output = tmp_path / "html"
    result = build(source, output)
    assert result.returncode != 0
    assert "MISSING_A" in result.stderr
    assert "STV_PENDING" not in (output / "index.html").read_text(encoding="utf-8")
    data = manifest(output)
    assert ["ROOT_A", "traces", "MISSING_A"] in data["edges"]
    assert "MISSING_A" not in data["objects"]


@pytest.mark.requirements("STV_SWR_015", "STV_SWR_018", "STV_SWR_048")
def test_incremental_body_change_hidden_and_deleted_objects(tmp_path):
    source = tmp_path / "source"
    shutil.copytree(FIXTURE, source)
    with (source / "requirements.rst").open("a", encoding="utf-8") as stream:
        stream.write('\n.. shr:: Initially visible\n   :id: HIDDEN_LATER\n')
    output = tmp_path / "html"
    assert build(source, output).returncode == 0
    old = manifest(output)
    path = source / "requirements.rst"
    path.write_text(path.read_text(encoding="utf-8").replace("formatted body", "changed rich body").replace(":id: HIDDEN_LATER", ":id: HIDDEN_LATER\n   :hide:"), encoding="utf-8")
    assert build(source, output).returncode == 0
    new = manifest(output)
    assert new["identity"] != old["identity"]
    assert new["details"]["ROOT_A"]["digest"] != old["details"]["ROOT_A"]["digest"]
    assert "HIDDEN_LATER" not in new["objects"]
    assert "HIDDEN_LATER" not in new["details"]
    assert build(source, output).returncode == 0
    assert manifest(output)["identity"] == new["identity"]


@pytest.mark.requirements("STV_SWR_001", "STV_SWR_026", "STV_SWR_043")
@pytest.mark.parametrize("count,success", [(200, True), (201, False)])
def test_seed_capacity_at_directive(tmp_path, count, success):
    source = tmp_path / "source"
    shutil.copytree(FIXTURE, source)
    ids = [f"NEED_{i:03}" for i in range(count)]
    (source / "requirements.rst").write_text("Requirements\n============\n\n" + "\n".join(f".. shr:: Item {i}\n   :id: {identity}\n" for i, identity in enumerate(ids)), encoding="utf-8")
    (source / "index.rst").write_text("Capacity\n========\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: " + " ".join(ids) + "\n", encoding="utf-8")
    result = build(source, tmp_path / "html")
    assert (result.returncode == 0) is success, result.stderr
    if not success:
        assert "index.rst:8" in result.stderr
        assert "200 distinct starting IDs" in result.stderr


@pytest.mark.requirements('STV_SYS_002','STV_SWR_014','STV_SWR_036','STV_SWR_045','STV_SWR_047','STV_SWR_048')
def test_alternate_host_schema_external_metadata_and_parts(tmp_path):
    result=build(FIXTURE.parent/'alternate_model',tmp_path)
    assert result.returncode==0,result.stdout+result.stderr
    data=manifest(tmp_path)
    assert data['model']['types']['hardware']['level']=='hardware'
    assert data['model']['relations']['traces']['outgoing']=='Traces to'
    assert data['objects']['EXTERNAL_A']['metadata']['owner']=='External owner'
    assert data['objects']['EXTERNAL_A']['docname'] is None
    assert 'GOAL_A.fragment' in data['objects']
    assert 'GOAL_A.fragment' not in data['entries']
    assert 'HIDDEN_A' not in data['objects']
    assert not any('HIDDEN_A' in edge for edge in data['edges'])


@pytest.mark.requirements('STV_SWR_036')
def test_invalid_mapping_has_entry_path_and_location(tmp_path):
    source=tmp_path/'source';shutil.copytree(FIXTURE,source)
    with (source/'conf.py').open('a',encoding='utf-8') as stream:
        stream.write('\ntraceability_view_model["types"]["shr"]["level"]="unknown"\n')
    result=build(source,tmp_path/'html')
    assert result.returncode!=0
    assert 'index.rst:8' in result.stderr
    assert 'types.shr' in result.stderr


@pytest.mark.requirements('STV_SWR_001')
def test_unsupported_builder_fails_clearly(tmp_path):
    result=build(FIXTURE,tmp_path,'-b','text')
    assert result.returncode!=0
    assert 'supports only the html builder' in result.stderr


@pytest.mark.requirements('STV_SWR_045')
def test_host_default_directional_labels_are_used(tmp_path):
    source=tmp_path/'source';shutil.copytree(FIXTURE,source)
    with (source/'conf.py').open('a',encoding='utf-8') as stream:
        stream.write('\nneeds_links={"traces":{}}\n')
    output=tmp_path/'html';result=build(source,output)
    assert result.returncode==0,result.stderr
    assert manifest(output)['model']['relations']['traces']=={'incoming':'traces incoming','outgoing':'traces'}
