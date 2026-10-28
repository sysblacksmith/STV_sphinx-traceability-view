"""Extended output-boundary, dependency and script-record resource procedures."""
import base64
import hashlib
import json
from pathlib import Path
import re
import pytest
from sphinx_traceability_view.detail_build.export_resources import collect
from sphinx_traceability_view.bundle import emit
import shutil
import subprocess
from test_build import FIXTURE, build, manifest


@pytest.mark.requirements('STV_SWR_072')
@pytest.mark.parametrize('reference',['../outside.png','%2e%2e/outside.png','https://example.invalid/beacon.png','//example.invalid/beacon.png','javascript:alert(1)'])
def test_svg_resource_escape_and_remote_targets_never_read_outside(tmp_path,monkeypatch,reference):
    root=tmp_path/'output';root.mkdir();outside=tmp_path/'outside.png';outside.write_bytes(b'PRIVATE_SENTINEL')
    (root/'probe.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg"><image href="{reference}"/></svg>')
    original=Path.read_bytes;reads=[]
    def guarded(path):
        assert path.resolve().is_relative_to(root.resolve()),str(path)
        reads.append(path.name);return original(path)
    monkeypatch.setattr(Path,'read_bytes',guarded)
    result=collect(root)
    assert 'error' in result['assets']['probe.svg']
    assert 'outside.png' not in reads


@pytest.mark.requirements('STV_SWR_072')
def test_real_symlink_escape_does_not_read_target(tmp_path,monkeypatch):
    root=tmp_path/'output';root.mkdir();outside=tmp_path/'outside.png';outside.write_bytes(b'PRIVATE_SENTINEL')
    (root/'alias.png').symlink_to(outside)
    original=Path.read_bytes
    def guarded(path):
        assert path.resolve().is_relative_to(root.resolve()),'Outside file content was read'
        return original(path)
    monkeypatch.setattr(Path,'read_bytes',guarded)
    result=collect(root,['<img data-stv-src="alias.png">'])
    assert not any('data' in value for value in result['assets'].values())


@pytest.mark.requirements('STV_SWR_072')
def test_nested_svg_cycles_are_explicit_failures(tmp_path):
    for source,target in [('a.svg','b.svg'),('b.svg','a.svg')]:
        (tmp_path/source).write_text(f'<svg xmlns="http://www.w3.org/2000/svg"><image href="{target}"/></svg>')
    result=collect(tmp_path)['assets']
    assert 'Cyclic' in result['a.svg']['error'] and 'Cyclic' in result['b.svg']['error']


@pytest.mark.requirements('STV_SWR_072')
@pytest.mark.parametrize('body',['<script/>','<foreignObject/>','<rect onclick="alert(1)"/>','<style>@import "remote.css";</style>'])
def test_active_svg_elements_attributes_and_imports_are_rejected(tmp_path,body):
    (tmp_path/'active.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg">'+body+'</svg>')
    assert 'error' in collect(tmp_path)['assets']['active.svg']


@pytest.mark.requirements('STV_SWR_072')
def test_css_import_cycle_encoded_names_srcset_fonts_and_deterministic_records(tmp_path):
    pixel=b'\x89PNG\r\n\x1a\nfixture'
    (tmp_path/'über space.png').write_bytes(pixel)
    (tmp_path/'second.png').write_bytes(pixel+b'second')
    (tmp_path/'unused.png').write_bytes(pixel+b'UNSELECTED')
    (tmp_path/'font.woff2').write_bytes(b'wOF2font-bytes')
    (tmp_path/'bad.png').write_bytes(b'not-an-image')
    (tmp_path/'a.css').write_text('@import "b.css"; @font-face{font-family:"Fixture </script>";src:url(font.woff2)}')
    (tmp_path/'b.css').write_text('@import "a.css"; .photo{background:url("%C3%BCber%20space.png")}')
    (tmp_path/'index.html').write_text('<link rel="stylesheet" href="a.css">')
    fragments=['<img data-stv-src="%C3%BCber%20space.png" data-stv-srcset="second.png 2x">','<img data-stv-src="missing.png"><img data-stv-src="bad.png">']
    one=collect(tmp_path,fragments);two=collect(tmp_path,fragments)
    assert one==two and 'unused.png' not in one['assets']
    assert {'über space.png','second.png','font.woff2','missing.png','bad.png'}==set(one['assets'])
    assert 'error' in one['assets']['missing.png'] and 'error' in one['assets']['bad.png']
    assert base64.b64decode(one['assets']['über space.png']['data'].split(',',1)[1])==pixel
    assert one['assets']['über space.png']['sha256']==hashlib.sha256(pixel).hexdigest()
    assert one['fonts'] and 'data:font/woff2;base64,' in one['fonts'][0]['css']
    emit({}, {}, tmp_path, one)
    script=next((tmp_path/'_static/stv/resources').glob('*.js')).read_text(encoding='utf-8')
    assert '</script>' not in script
    encoded=re.search(r'JSON.parse\((.*)\);$',script)[1]
    assert json.loads(json.loads(encoded))==one


@pytest.mark.requirements('STV_SWR_067','STV_SWR_068')
def test_font_settings_defaults_identity_and_named_build_errors(tmp_path):
    source=tmp_path/'source';shutil.copytree(FIXTURE,source)
    config=(source/'conf.py').read_text(encoding='utf-8');output=tmp_path/'html'
    assert build(source,output).returncode==0
    default=manifest(output)
    assert default['presentation']=={'tooltip_font_scale':.7,'details_font_scale':.7}
    for setting,field in [('tooltip','tooltip_font_scale'),('details','details_font_scale')]:
        (source/'conf.py').write_text(config+f'\ntraceability_view_{setting}_font_scale=0.6\n',encoding='utf-8')
        result=build(source,output);assert result.returncode==0,result.stderr
        changed=manifest(output);assert changed['identity']!=default['identity'] and changed['presentation'][field]==.6
        other='details_font_scale' if setting=='tooltip' else 'tooltip_font_scale'
        assert changed['presentation'][other]==.7
        (source/'conf.py').write_text(config+f'\ntraceability_view_{setting}_font_scale=0\n',encoding='utf-8')
        invalid=build(source,output)
        assert invalid.returncode!=0 and f'traceability_view_{setting}_font_scale' in invalid.stderr


@pytest.mark.requirements('STV_SWR_066')
def test_extended_reset_command_sequences():
    root=Path(__file__).resolve().parents[2]
    result=subprocess.run(['node','--test-reporter=tap',str(root/'docs/test-scripts/fixtures/extended/reset-sequences.mjs')],cwd=root,capture_output=True,text=True)
    assert result.returncode==0,result.stdout+result.stderr
    assert '# pass 2' in result.stdout
