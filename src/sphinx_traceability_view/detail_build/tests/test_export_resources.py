"""Safe output-local records, independent of reader network access."""
import base64
import pytest
from sphinx_traceability_view.detail_build.export_resources import collect


@pytest.mark.requirements('STV_SWR_072')
def test_export_resources_embed_local_content_and_reject_active_svg(tmp_path):
    (tmp_path / 'pixel.png').write_bytes(b'\x89PNG\r\n\x1a\nimage')
    (tmp_path / 'safe.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"><image href="pixel.png"/></svg>')
    (tmp_path / 'active.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"><script>alert(1)</script></svg>')
    (tmp_path / 'escape.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"><image href="../outside.png"/></svg>')
    result = collect(tmp_path)['assets']
    assert result['pixel.png']['data'].startswith('data:image/png;base64,')
    decoded = base64.b64decode(result['safe.svg']['data'].split(',', 1)[1])
    assert b'data:image/png;base64,' in decoded
    assert 'error' in result['active.svg']
    assert 'escapes' in result['escape.svg']['error']


@pytest.mark.requirements('STV_SWR_072')
def test_unreferenced_images_do_not_enter_the_graph_resource_record(tmp_path):
    for name in ('visible.png', 'unreferenced-private-name.png'):
        (tmp_path / name).write_bytes(b'\x89PNG\r\n\x1a\nimage')
    result = collect(tmp_path, ['<img data-stv-src="visible.png">'])
    assert set(result['assets']) == {'visible.png'}


@pytest.mark.requirements('STV_SWR_072')
def test_inline_detail_font_faces_embed_local_bytes(tmp_path):
    (tmp_path / 'font.woff2').write_bytes(b'wOF2test-font')
    fragment = '<style data-stv-css="@font-face {font-family: Demo; src: url(font.woff2)}"></style>'
    result = collect(tmp_path, [fragment])
    assert result['fonts'][0]['family'] == 'Demo'
    assert 'data:font/woff2;base64,' in result['fonts'][0]['css']


@pytest.mark.requirements('STV_SWR_072')
@pytest.mark.parametrize('encoding', ['utf-8', 'utf-16'])
def test_svg_entity_declarations_are_rejected_before_parsing(tmp_path, encoding):
    xml = '<!DOCTYPE svg [<!ENTITY label "text">]><svg xmlns="http://www.w3.org/2000/svg"><text>&label;</text></svg>'
    (tmp_path / 'entity.svg').write_bytes(xml.encode(encoding))
    assert 'entity declarations' in collect(tmp_path)['assets']['entity.svg']['error']
