"""Regression for STV_PR_006 at the real Windows file/HTTP boundary."""
import json
import os
from pathlib import Path
import shutil
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser, published_url
from test_build import build, FIXTURE, manifest


@pytest.mark.browser
@pytest.mark.requirements('STV_SYS_003','STV_SYS_006','STV_SWR_015','STV_SWR_017','STV_SWR_018')
def test_nested_windows_detail_loading_and_retry(browser, tmp_path):
    source=tmp_path/'source';shutil.copytree(FIXTURE,source)
    (source/'nested').mkdir()
    (source/'nested/index.rst').write_text('Nested view\n===========\n\n.. traceability-view:: ROOT_A LEAF_B\n',encoding='utf-8')
    with (source/'index.rst').open('a',encoding='utf-8') as stream:stream.write('\n.. toctree::\n\n   nested/index\n')
    # Guarantee that old two-hash names exceed MAX_PATH, while compact full
    # content hashes fit. Do not depend on a particular checkout/user name.
    output=tmp_path/('nested-'+('x'*max(1,145-len(str(tmp_path))-8)))
    result=build(source,output);assert result.returncode==0,result.stdout+result.stderr
    graph=manifest(output);detail=graph['details']['ROOT_A'];asset=output/detail['url']
    old_path=asset.parent/('0'*64+'-'+detail['digest']+'.js')
    assert len(str(old_path))>260
    assert asset.is_file()
    record=Path(os.environ['STV_PATH_RECORD']) if os.environ.get('STV_PATH_RECORD') else None
    observations={'browser':browser.capabilities['browserVersion'],'old_path_length':len(str(old_path)),
                  'actual_path_length':len(str(asset)),'output':str(output),'checks':[]}
    wait=WebDriverWait(browser,15)
    saved=asset.read_bytes()
    try:
        for protocol in ('file','http'):
            with published_url(output,protocol) as root_url:
                for page in ('index.html','nested/index.html'):
                    url=root_url.rsplit('/',1)[0]+'/'+page
                    browser.get(url)
                    wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
                    control=browser.find_element(By.CSS_SELECTOR,'[aria-label="Details for ROOT_A"]')
                    browser.execute_script('arguments[0].focus()',control)
                    control.send_keys(Keys.ENTER)
                    wait.until(lambda d:'formatted body' in d.find_element(By.CSS_SELECTOR,'.stv-detail').text)
                    assert browser.find_elements(By.CSS_SELECTOR,'.stv-detail table')
                    assert browser.find_elements(By.CSS_SELECTOR,'.stv-detail a[href]')
                    observations['checks'].append({'protocol':protocol,'page':page,'result':'passed'})
                    browser.find_element(By.CSS_SELECTOR,'.stv-detail button').click()
                    # A fresh page has no fragment cache. Missing local data
                    # must report an error and allow recovery after restoration.
                    browser.get(url)
                    wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
                    asset.rename(asset.with_suffix('.unavailable'))
                    try:
                        control=browser.find_element(By.CSS_SELECTOR,'[aria-label="Details for ROOT_A"]')
                        browser.execute_script('arguments[0].click()',control)
                        wait.until(lambda d:'Local detail asset unavailable' in d.find_element(By.CSS_SELECTOR,'.stv-detail').text)
                    finally:asset.with_suffix('.unavailable').rename(asset)
                    # Dismiss/reopen exercises the reader-visible retry path.
                    browser.find_element(By.CSS_SELECTOR,'.stv-detail button').click()
                    browser.execute_script('arguments[0].click()',control)
                    wait.until(lambda d:'formatted body' in d.find_element(By.CSS_SELECTOR,'.stv-detail').text)
                    observations['checks'].append({'protocol':protocol,'page':page,'retry':'passed'})
                    if record:
                        record.mkdir(parents=True,exist_ok=True)
                        browser.save_screenshot(str(record/(protocol+'-'+page.replace('/','-')+'.png')))
        assert len(str(asset))<260
    finally:
        if record:
            record.mkdir(parents=True,exist_ok=True)
            (record/'observations.json').write_text(json.dumps(observations,indent=2),encoding='utf-8')
            browser.save_screenshot(str(record/'last-state.png'))
