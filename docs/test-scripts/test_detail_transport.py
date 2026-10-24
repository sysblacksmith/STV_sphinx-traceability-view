"""PRSA-002: authored transport markers cannot become active detail content."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import base64
import shutil
import threading
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser, short_output, published_url
from test_build import build, FIXTURE


@pytest.mark.browser
@pytest.mark.requirements('STV_SWR_015','STV_SWR_017','STV_SWR_018','STV_SWR_049')
@pytest.mark.parametrize('protocol',['file','http'])
def test_authored_transport_markers_stay_inert(browser, short_output, protocol):
    requests=[]
    class Beacon(BaseHTTPRequestHandler):
        def do_GET(self):
            requests.append(self.path)
            self.send_response(204);self.end_headers()
        def log_message(self,*args):
            pass
    server=ThreadingHTTPServer(('127.0.0.1',0),Beacon)
    threading.Thread(target=server.serve_forever,daemon=True).start()
    try:
        remote=f'http://127.0.0.1:{server.server_port}/beacon'
        source=short_output/'source';shutil.copytree(FIXTURE,source)
        (source/'pixel.png').write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+aV1cAAAAASUVORK5CYII='))
        with (source/'conf.py').open('a',encoding='utf-8') as stream:
            stream.write("\nhtml_extra_path = ['pixel.png']\n")
        markup=f'''.. shr:: Inert marker regression
   :id: PROBE

   .. raw:: html

      <a class="probe-link" data-stv-href="javascript:window.__stvMarker=1">Inert link</a>
      <img class="probe-image" data-stv-src="{remote}" data-stv-srcset="{remote} 1x">
      <div class="probe-style" data-stv-style='background:url("{remote}")'>Inert style</div>
      <style data-stv-css='@import "{remote}";'></style>
      <img class="local-image" src="pixel.png" data-stv-src="{remote}">
      <img class="local-srcset" srcset="pixel.png 1x">
      <a class="local-link" href="requirements.html#ROOT_A" data-stv-href="javascript:window.__stvMarker=1">Local reference</a>
      <a class="external-link" href="https://example.invalid/reference">Explicit external reference</a>
      <div class="local-style" style="background-image:url(pixel.png);color:red">Formatted content</div>
      <table><tr><td>Preserved table</td></tr></table>

.. traceability-view:: PROBE
'''
        (source/'index.rst').write_text('Transport regression\n====================\n\n.. toctree::\n\n   requirements\n\n'+markup,encoding='utf-8')
        output=short_output/'html'
        result=build(source,output);assert result.returncode==0,result.stdout+result.stderr
        with published_url(output,protocol) as url:
            browser.get(url)
            wait=WebDriverWait(browser,15)
            wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'[aria-label="Details for PROBE"]'))
            browser.execute_script("document.querySelector('[aria-label=\"Details for PROBE\"]').click()")
            wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-detail .probe-link'))
            panel=browser.find_element(By.CSS_SELECTOR,'.stv-detail')
            inert=panel.find_element(By.CSS_SELECTOR,'.probe-link')
            assert inert.get_attribute('href') is None
            browser.execute_script('arguments[0].click()',inert)
            assert browser.execute_script('return window.__stvMarker||0')==0
            assert panel.find_element(By.CSS_SELECTOR,'.probe-image').get_attribute('src') is None
            assert panel.find_element(By.CSS_SELECTOR,'.probe-image').get_dom_attribute('srcset') is None
            image=panel.find_element(By.CSS_SELECTOR,'.local-image')
            wait.until(lambda d:d.execute_script('return arguments[0].complete && arguments[0].naturalWidth>0',image))
            assert image.get_attribute('src').endswith('/pixel.png')
            assert panel.find_element(By.CSS_SELECTOR,'.local-srcset').get_attribute('srcset').endswith('/pixel.png 1x')
            assert panel.find_element(By.CSS_SELECTOR,'.local-link').get_attribute('href').endswith('/requirements.html#ROOT_A')
            assert panel.find_element(By.CSS_SELECTOR,'.external-link').get_attribute('href')=='https://example.invalid/reference'
            style=panel.find_element(By.CSS_SELECTOR,'.local-style').get_attribute('style')
            assert 'pixel.png' in style and 'red' in style
            assert 'Preserved table' in panel.find_element(By.CSS_SELECTOR,'table').text
            time.sleep(.3)
            assert requests==[],requests
    finally:
        server.shutdown();server.server_close()
