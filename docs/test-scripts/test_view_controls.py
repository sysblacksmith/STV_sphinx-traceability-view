"""CR015-018: real browser controls and standalone visible-area export."""
from pathlib import Path
import base64
import xml.etree.ElementTree as ET
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser, short_output, published_url
from test_build import build
from test_persistent_details import prepare_source, open_box, panel


@pytest.mark.browser
@pytest.mark.requirements('STV_SYS_011', 'STV_SWR_070', 'STV_SWR_071', 'STV_SWR_072')
@pytest.mark.parametrize('protocol', ['file', 'http'])
@pytest.mark.parametrize('card_count', [1, 10])
def test_standalone_svg_visible_details(browser, short_output, protocol, card_count):
    source = short_output / 'export-source'
    prepare_source(source)
    (source / 'pixel.png').write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aWZkAAAAASUVORK5CYII='))
    requirements = source / 'requirements.rst'
    text = requirements.read_text(encoding='utf-8')
    text = text.replace('   Long rendered detail paragraph 0 for BOX_00', '   .. image:: pixel.png\n\n   .. raw:: html\n\n      <input type="password" value="export-test-sensitive-sentinel" aria-label="Password probe">\n\n   Long rendered detail paragraph 0 for BOX_00', 1)
    requirements.write_text(text, encoding='utf-8')
    output = short_output / 'export-output'
    result = build(source, output)
    assert result.returncode == 0, result.stderr
    with published_url(output, protocol) as url:
        browser.get(url)
        wait = WebDriverWait(browser, 20)
        root = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, '.stv-view[data-stv-revision]'))
        open_box(browser, root, 'BOX_00')
        wait.until(lambda d: 'Long rendered' in panel(d, root, 'BOX_00').text)
        for index in range(1, card_count):
            identity = f'BOX_{index:02}'
            open_box(browser, root, identity)
            wait.until(lambda d: 'Long rendered' in panel(d, root, identity).text)
        # Reproduce the large-layout invariant without building 30k Needs:
        # move the scene's own box off-screen, compensating its children so
        # the rendered graph stays exactly where it was.
        geometry = browser.execute_script("""
          const scene=arguments[0].querySelector('.stv-scene');
          const first=scene.querySelector('.stv-node');
          const before=first.getBoundingClientRect();
          const scale=new DOMMatrix(getComputedStyle(scene).transform).a;
          scene.style.left=`${20000*scale}px`;
          for(const child of scene.children)
            child.style.left=`${(parseFloat(getComputedStyle(child).left)||0)-20000}px`;
          const after=first.getBoundingClientRect();
          return {sceneLeft:scene.getBoundingClientRect().left, width:innerWidth,
            dx:Math.abs(before.left-after.left),dy:Math.abs(before.top-after.top)};
        """, root)
        assert geometry['sceneLeft'] > geometry['width'], geometry
        assert geometry['dx'] < 0.5 and geometry['dy'] < 0.5, geometry
        browser.execute_script('window.exportBlob=null; const create=URL.createObjectURL; URL.createObjectURL=b=>{window.exportBlob=b; return create(b);};')
        save = root.find_element(By.XPATH, ".//button[.='Save as SVG']")
        wait.until(lambda d: save.is_enabled())
        # Empty crop fails without requesting a download and remains recoverable.
        browser.execute_script("arguments[0].querySelector('.stv-workspace').style.transform='translateY(2000px)'", root)
        save.click()
        assert 'No visible view area' in root.text
        assert not browser.execute_script('return window.exportBlob')
        browser.execute_script("arguments[0].querySelector('.stv-workspace').style.transform=''", root)
        browser.save_screenshot(str(short_output / 'export-source.png'))
        save.click()
        wait.until(lambda d: d.execute_script('return window.exportBlob!==null'))
        text = browser.execute_async_script('const done=arguments[0]; window.exportBlob.text().then(done);')
        assert '<svg' in text and 'Long rendered' in text
        assert ET.fromstring(text).find('{http://www.w3.org/2000/svg}rect').get('fill') == browser.execute_script('return getComputedStyle(arguments[0]).backgroundColor', root)
        if card_count == 1:
            assert 'data:image/png;base64,' in text
        assert 'data-stv-' not in text and '<script' not in text
        assert 'export-test-sensitive-sentinel' not in text
        assert 'SVG download requested' in root.text
        downloaded = wait.until(lambda d: next(iter(d.stv_download_directory.glob('*.svg')), None))
        wait.until(lambda d: downloaded.read_text(encoding='utf-8') == text)
        saved = short_output / 'standalone.svg'
        saved.write_text(text, encoding='utf-8')
        # Prove that the snapshot does not depend on the source output tree.
        output.resolve().relative_to(short_output.resolve())
        output.rename(output.with_name(output.name + '-unavailable'))
        browser.get(saved.as_uri())
        assert browser.find_elements(By.CSS_SELECTOR, 'foreignObject')
        # Positioned scenes can lie outside their own box while overflowing
        # graph nodes remain visible. Export must retain those descendants.
        assert browser.find_elements(By.CSS_SELECTOR, '.stv-node .stv-id')
        assert browser.execute_script("""
          const frame=document.documentElement.getBoundingClientRect();
          return [...document.querySelectorAll('.stv-node .stv-id')].some(node=>{
            const r=node.getBoundingClientRect();
            return node.textContent.includes('BOX_') && r.width>0 && r.height>0
              && r.bottom>frame.top && r.top<frame.bottom
              && r.right>frame.left && r.left<frame.right;
          });
        """)
        assert browser.execute_script("return document.documentElement.textContent.includes('Long rendered')")
        assert browser.execute_script("""
          const frame=document.documentElement.getBoundingClientRect();
          return [...document.querySelectorAll('.stv-persistent-body p')].some(p=>{
            const r=p.getBoundingClientRect();
            return p.textContent.includes('Long rendered') && getComputedStyle(p).visibility!=='hidden'
              && r.bottom>frame.top && r.top<frame.bottom && r.right>frame.left && r.left<frame.right;
          });
        """)
        browser.save_screenshot(str(short_output / 'export-reopened.png'))


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_066')
@pytest.mark.parametrize('protocol', ['file', 'http'])
def test_collapse_all_keeps_current_roots_and_open_details(browser, short_output, protocol):
    source = short_output / 'reset-source'
    prepare_source(source)
    output = short_output / 'reset-output'
    result = build(source, output)
    assert result.returncode == 0, result.stderr
    with published_url(output, protocol) as url:
        browser.get(url)
        wait = WebDriverWait(browser, 20)
        root = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, '.stv-view[data-stv-revision]'))
        open_box(browser, root, 'BOX_00')
        wait.until(lambda d: 'Long rendered' in panel(d, root, 'BOX_00').text)
        button = root.find_element(By.XPATH, ".//button[.='Collapse all nodes']")
        expand = root.find_element(By.CSS_SELECTOR, 'button[aria-label^="Expand"][aria-label$="for BOX_00"]')
        expand.click()
        wait.until(lambda d: root.get_attribute('aria-busy') == 'false' and root.find_elements(By.CSS_SELECTOR, '.stv-edges polyline'))
        if protocol == 'file':
            button.click()
        else:
            button.send_keys(Keys.SPACE)
        wait.until(lambda d: root.get_attribute('aria-busy') == 'false')
        assert not root.find_elements(By.CSS_SELECTOR, '.stv-edges polyline')
        assert len(root.find_elements(By.CSS_SELECTOR, '.stv-node')) == 12
        assert panel(browser, root, 'BOX_00').is_displayed()
        assert browser.switch_to.active_element == button


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_069')
@pytest.mark.parametrize('protocol', ['file', 'http'])
def test_page_metadata_without_a_graph(browser, short_output, protocol):
    source = short_output / 'page-source'
    prepare_source(source)
    requirements = source / 'requirements.rst'
    text = requirements.read_text(encoding='utf-8').replace('id="probe-field"', 'id="stv-host-row-1"')
    requirements.write_text(text, encoding='utf-8')
    output = short_output / 'page-output'
    result = build(source, output)
    assert result.returncode == 0, result.stderr
    with published_url(output, protocol) as url:
        browser.get(url.replace('index.html', 'requirements.html'))
        wait = WebDriverWait(browser, 20)
        group = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, '.stv-page-metadata'))
        assert not browser.find_elements(By.CSS_SELECTOR, '.stv-view')
        assert len(browser.find_elements(By.CSS_SELECTOR, '.stv-page-metadata')) == 1
        group.find_element(By.XPATH, ".//button[.='Expand all']").click()
        controls = browser.find_elements(By.CSS_SELECTOR, 'table.need .needs_collapse')
        assert controls and all(c.get_attribute('aria-expanded') == 'true' for c in controls)
        assert browser.execute_script("return [...document.querySelectorAll('table.need .needs_collapse[aria-controls]')].every(c=>c.getAttribute('aria-controls').split(' ').every(id=>{const rows=[...document.querySelectorAll('[id]')].filter(n=>n.id===id);return rows.length===1&&rows[0].closest('table.need')===c.closest('table.need');}))")
        group.find_element(By.XPATH, ".//button[.='Collapse all']").click()
        assert all(c.get_attribute('aria-expanded') == 'false' for c in controls)
        controls[0].send_keys(' ')
        assert controls[0].get_attribute('aria-expanded') == 'true'
        assert 'Long rendered' in browser.find_element(By.TAG_NAME, 'body').text


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_067', 'STV_SWR_068')
def test_font_scales_are_independent_and_applied_once(browser, short_output):
    sizes = []
    hover_sizes = []
    for name, extra in [('baseline', '\ntraceability_view_details_font_scale=1.0\ntraceability_view_tooltip_font_scale=1.0\n'), ('default', ''), ('override', '\ntraceability_view_details_font_scale=0.6\ntraceability_view_tooltip_font_scale=0.8\n')]:
        source = short_output / name
        prepare_source(source)
        with (source / 'conf.py').open('a', encoding='utf-8') as stream:
            stream.write(extra)
        output = short_output / (name + '-output')
        result = build(source, output)
        assert result.returncode == 0, result.stderr
        browser.get((output / 'index.html').as_uri())
        wait = WebDriverWait(browser, 20)
        root = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, '.stv-view[data-stv-revision]'))
        open_box(browser, root, 'BOX_00')
        wait.until(lambda d: 'Long rendered' in panel(d, root, 'BOX_00').text)
        measure = lambda: browser.execute_script("return parseFloat(getComputedStyle(arguments[0].querySelector('.stv-persistent-body p')).fontSize)", panel(browser, root, 'BOX_00'))
        value = measure()
        open_box(browser, root, 'BOX_00')
        assert measure() == value
        sizes.append(value)
        ActionChains(browser).move_to_element(root.find_element(By.CSS_SELECTOR, '.stv-node')).perform()
        hover = wait.until(lambda d: d.find_element(By.CSS_SELECTOR, '.stv-hover-detail .need p'))
        hover_sizes.append(browser.execute_script('return parseFloat(getComputedStyle(arguments[0]).fontSize)', hover))
    assert sizes[1] == pytest.approx(sizes[0] * 0.7, abs=0.5)
    assert sizes[2] == pytest.approx(sizes[0] * 0.6, abs=0.5)
    assert hover_sizes[1] == pytest.approx(hover_sizes[0] * 0.7, abs=0.5)
    assert hover_sizes[2] == pytest.approx(hover_sizes[0] * 0.8, abs=0.5)


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_069')
def test_page_controls_disclose_unsupported_markup_without_partial_success(browser, short_output):
    source = short_output / 'unsupported-source'
    prepare_source(source)
    requirements = source / 'requirements.rst'
    text = requirements.read_text(encoding='utf-8').replace('   Long rendered detail paragraph 0 for BOX_00', '   .. raw:: html\n\n      <span class="needs needs_collapse" id="unsupported__show__content"></span>\n\n   Long rendered detail paragraph 0 for BOX_00', 1)
    requirements.write_text(text, encoding='utf-8')
    output = short_output / 'unsupported-output'
    result = build(source, output)
    assert result.returncode == 0, result.stderr
    browser.get((output / 'requirements.html').as_uri())
    group = WebDriverWait(browser, 20).until(lambda d: d.find_element(By.CSS_SELECTOR, '.stv-page-metadata'))
    assert 'unsupported Need disclosure markup' in group.text
    assert all(not b.is_enabled() for b in group.find_elements(By.TAG_NAME, 'button'))
    assert 'Long rendered' in browser.find_element(By.TAG_NAME, 'body').text


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_069')
def test_page_controls_disclose_missing_host_handler_dependency(browser, short_output):
    source = short_output / 'missing-host-source'
    prepare_source(source)
    output = short_output / 'missing-host-output'
    result = build(source, output)
    assert result.returncode == 0, result.stderr
    scripts = list(output.rglob('jquery.js'))
    assert scripts
    for script in scripts:
        script.resolve().relative_to(output.resolve())
        script.rename(script.with_suffix('.disabled'))
    browser.get((output / 'requirements.html').as_uri())
    group = WebDriverWait(browser, 20).until(lambda d: d.find_element(By.CSS_SELECTOR, '.stv-page-metadata'))
    assert 'host metadata handlers unavailable' in group.text
    assert all(not b.is_enabled() for b in group.find_elements(By.TAG_NAME, 'button'))
