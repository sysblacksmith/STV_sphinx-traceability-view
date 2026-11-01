"""Release-only criterion supplements; run explicitly, preserving JUnit evidence."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'docs/test-scripts'))
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser, short_output, published_url
from test_build import build
from test_persistent_details import prepare_source, open_box, toolbar, panel_ids, change_seed
from test_remembered_view import roots, capture
from test_extended_controls import extended_site, ready, mount_controlled, command


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_073', 'STV_SWR_074', 'STV_SWR_075')
@pytest.mark.parametrize('protocol', ['file', 'http'])
def test_narrow_restore_reduced_cards_and_untrusted_snapshot(browser, short_output, protocol):
    source = short_output / 'source'
    output = short_output / 'html'
    prepare_source(source, 3)
    result = build(source, output)
    assert result.returncode == 0, result.stdout + result.stderr
    browser.set_window_size(900, 1100)
    with published_url(output, protocol) as url:
        browser.get(url)
        root, _ = roots(browser)
        for identity in ['BOX_00', 'BOX_01', 'BOX_02']:
            open_box(browser, root, identity)
        root.find_element(By.CSS_SELECTOR, '.stv-remember input').click()
        toolbar(browser, root, 'Pan down')
        before = capture(browser, root)
        browser.refresh()
        root, _ = roots(browser)
        assert capture(browser, root) == before
        assert browser.execute_script('return document.activeElement===document.body')
        browser.save_screenshot(str(Path(__file__).parent / f'remember-narrow-{protocol}.png'))
        key = browser.execute_script("return Object.keys(localStorage).find(k=>k.startsWith('stv:view:1:'))")
        saved = json.loads(browser.execute_script('return localStorage.getItem(arguments[0])', key))
        # Current published graph, never saved HTML, owns restored content.
        saved['html'] = '<img src=x onerror="window.snapshotExecuted=true">'
        saved['cards'] += ['HIDDEN_SENTINEL', '<script>window.snapshotExecuted=true</script>']
        browser.execute_script('localStorage.setItem(arguments[0],arguments[1])', key, json.dumps(saved))
        browser.refresh()
        root, _ = roots(browser)
        assert panel_ids(browser, root) == ['BOX_00', 'BOX_01', 'BOX_02']
        assert not browser.execute_script('return !!window.snapshotExecuted')
        assert not root.find_elements(By.CSS_SELECTOR, '[onerror]')
        # Rebuild the same publication with a smaller current card capacity.
        conf = source / 'conf.py'
        with conf.open('a', encoding='utf-8') as stream:
            stream.write('\ntraceability_view_details_limit = 1\n')
        result = build(source, output)
        assert result.returncode == 0, result.stdout + result.stderr
        browser.refresh()
        root, _ = roots(browser)
        assert panel_ids(browser, root) == ['BOX_02']
        # Invalid viewport data falls back atomically to ordinary startup.
        saved['transform']['k'] = 0
        browser.execute_script('localStorage.setItem(arguments[0],arguments[1])', key, json.dumps(saved))
        browser.refresh()
        root, _ = roots(browser)
        assert not capture(browser, root)['enabled']
        assert not panel_ids(browser, root)
        assert len(capture(browser, root)['nodes']) == 12
        assert root.find_element(By.CSS_SELECTOR, '.stv-memory-status').get_attribute('role') == 'status'


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_073', 'STV_SWR_075')
@pytest.mark.parametrize('protocol', ['file', 'http'])
def test_failed_layout_and_storage_removal_preserve_live_view(browser, extended_site, protocol):
    with published_url(extended_site, protocol) as url:
        browser.get(url)
        wait = ready(browser)
        root = mount_controlled(browser)
        checkbox = root.find_element(By.CSS_SELECTOR, '.stv-remember input')
        checkbox.click()
        read = "return Object.keys(localStorage).filter(k=>k.includes('extended-controlled')).map(k=>[k,localStorage.getItem(k)])"
        saved = browser.execute_script(read)
        assert saved
        before = capture(browser, root)
        browser.execute_script("window.extendedMode='reject';arguments[0].querySelector('.stv-groups button').click()", root)
        wait.until(lambda d: 'Injected layout rejection' in root.text)
        assert browser.execute_script(read) == saved
        assert capture(browser, root) == before
        browser.execute_script("window.extendedMode='normal'")
        command(browser, root, 'Retry layout')
        wait.until(lambda d: root.get_attribute('aria-busy') == 'false')
        assert capture(browser, root)['enabled']
        before = capture(browser, root)
        browser.execute_script("window.nativeRemove=Storage.prototype.removeItem;Storage.prototype.removeItem=function(){throw Error('Injected remove failure')}")
        checkbox.click()
        assert capture(browser, root) == {**before, 'enabled': False}
        status = root.find_element(By.CSS_SELECTOR, '.stv-memory-status')
        assert 'Injected remove failure' in status.text
        assert status.get_attribute('role') == 'status'
        browser.execute_script('Storage.prototype.removeItem=window.nativeRemove')
        checkbox.click()
        checkbox.click()
        assert not status.text
        assert browser.execute_script(read) == []


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_073', 'STV_SWR_074', 'STV_SWR_075')
@pytest.mark.parametrize('protocol', ['file', 'http'])
def test_history_two_saved_views_pages_and_changed_viewport(browser, short_output, protocol):
    source = short_output/'source'
    output = short_output/'html'
    prepare_source(source, 3)
    result = build(source, output)
    assert result.returncode == 0, result.stdout + result.stderr
    (output/'another.html').write_text((output/'index.html').read_text(encoding='utf-8'), encoding='utf-8')
    with published_url(output, protocol) as url:
        browser.get(url)
        root, other = roots(browser)
        open_box(browser, root, 'BOX_01')
        change_seed(browser, root, 'BOX_00')
        root.find_element(By.CSS_SELECTOR, '.stv-remember input').click()
        toolbar(browser, root, 'Pan down')
        change_seed(browser, other, 'BOX_04')
        other.find_element(By.CSS_SELECTOR, '.stv-remember input').click()
        toolbar(browser, other, 'Zoom in')
        expected = [capture(browser, element) for element in (root, other)]
        browser.refresh()
        assert [capture(browser, element) for element in roots(browser)] == expected
        browser.get(url.replace('index.html', 'another.html'))
        root, other = roots(browser)
        assert not capture(browser, root)['enabled']
        root.find_element(By.CSS_SELECTOR, '.stv-remember input').click()
        toolbar(browser, root, 'Zoom out')
        page_expected = capture(browser, root)
        browser.back()
        assert [capture(browser, element) for element in roots(browser)] == expected
        browser.forward()
        root, _ = roots(browser)
        assert capture(browser, root) == page_expected
        browser.back()
        root, _ = roots(browser)
        assert capture(browser, root)['cards'] == expected[0]['cards']
        browser.set_window_size(900, 1100)
        browser.refresh()
        root, other = roots(browser)
        current = capture(browser, root)
        assert current['transform'] == expected[0]['transform']
        assert current['cards'] == expected[0]['cards']
        assert [node[0] for node in current['nodes']] == [node[0] for node in expected[0]['nodes']]
        toolbar(browser, root, 'Pan right')
        assert capture(browser, root)['transform'] != current['transform']
        toolbar(browser, root, 'Zoom in')
        assert capture(browser, other)['transform'] == expected[1]['transform']
