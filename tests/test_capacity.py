"""Real-browser measurements against the generated 30k/90k Sphinx fixture."""
import ctypes
from ctypes import wintypes
import json
import os
from pathlib import Path
import statistics
import shutil
import tempfile
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from test_browser import browser, published_url


def working_set(pid):
    class Counters(ctypes.Structure):
        _fields_=[('cb',wintypes.DWORD),('PageFaultCount',wintypes.DWORD)]+[(name,ctypes.c_size_t) for name in ('PeakWorkingSetSize','WorkingSetSize','QuotaPeakPagedPoolUsage','QuotaPagedPoolUsage','QuotaPeakNonPagedPoolUsage','QuotaNonPagedPoolUsage','PagefileUsage','PeakPagefileUsage')]
    kernel=ctypes.WinDLL('kernel32',use_last_error=True)
    kernel.OpenProcess.restype=wintypes.HANDLE
    kernel.CloseHandle.argtypes=[wintypes.HANDLE]
    handle=kernel.OpenProcess(0x0400|0x0010,False,pid)
    if not handle:raise ctypes.WinError(ctypes.get_last_error())
    try:
        counters=Counters();counters.cb=ctypes.sizeof(counters)
        api=ctypes.WinDLL('psapi',use_last_error=True);api.GetProcessMemoryInfo.argtypes=[wintypes.HANDLE,ctypes.c_void_p,wintypes.DWORD]
        if not api.GetProcessMemoryInfo(handle,ctypes.byref(counters),counters.cb):raise ctypes.WinError(ctypes.get_last_error())
        return counters.WorkingSetSize
    finally:kernel.CloseHandle(handle)


def browser_memory(root_pid):
    class ProcessEntry(ctypes.Structure):
        _fields_=[('dwSize',wintypes.DWORD),('cntUsage',wintypes.DWORD),('th32ProcessID',wintypes.DWORD),
                  ('th32DefaultHeapID',ctypes.c_size_t),('th32ModuleID',wintypes.DWORD),('cntThreads',wintypes.DWORD),
                  ('th32ParentProcessID',wintypes.DWORD),('pcPriClassBase',wintypes.LONG),('dwFlags',wintypes.DWORD),('szExeFile',wintypes.WCHAR*260)]
    kernel=ctypes.WinDLL('kernel32',use_last_error=True)
    kernel.CreateToolhelp32Snapshot.restype=wintypes.HANDLE
    for name in ('Process32FirstW','Process32NextW'):
        getattr(kernel,name).argtypes=[wintypes.HANDLE,ctypes.POINTER(ProcessEntry)]
    kernel.CloseHandle.argtypes=[wintypes.HANDLE]
    handle=kernel.CreateToolhelp32Snapshot(2,0)
    if handle==wintypes.HANDLE(-1).value:raise ctypes.WinError(ctypes.get_last_error())
    processes=[]
    try:
        entry=ProcessEntry();entry.dwSize=ctypes.sizeof(entry)
        success=kernel.Process32FirstW(handle,ctypes.byref(entry))
        while success:
            processes.append((entry.th32ProcessID,entry.th32ParentProcessID))
            success=kernel.Process32NextW(handle,ctypes.byref(entry))
    finally:kernel.CloseHandle(handle)
    owned={root_pid}
    while True:
        children={pid for pid,parent in processes if parent in owned}
        if children<=owned:break
        owned|=children
    sizes=[]
    for pid in owned:
        try:sizes.append(working_set(pid))
        except OSError:pass  # A helper may exit between the snapshot and the query.
    return {'processes_measured':len(sizes),'working_set_bytes':sum(sizes)}


def click_revision(driver, selector):
    return driver.execute_async_script('''
      const control=document.querySelector(arguments[0]),done=arguments[arguments.length-1],root=control.closest('.stv-view');
      const before=root.dataset.stvRevision,start=performance.now();
      const timer=setTimeout(()=>{watcher.disconnect();done({error:root.querySelector('.stv-status').textContent});},20000);
      const watcher=new MutationObserver(()=>{if(root.dataset.stvRevision!==before){clearTimeout(timer);watcher.disconnect();done({ms:performance.now()-start});}});
      watcher.observe(root,{attributes:true,attributeFilter:['data-stv-revision']});control.click();
    ''',selector)


def measure_detail(driver):
    return driver.execute_async_script('''
      const done=arguments[arguments.length-1],start=performance.now();
      const observer=new MutationObserver(()=>{const panel=document.querySelector('.stv-detail');if(panel&&panel.textContent.includes('Deterministic rich detail text.')){observer.disconnect();clearTimeout(timer);done(performance.now()-start);}});
      const timer=setTimeout(()=>{observer.disconnect();done(null)},20000);
      observer.observe(document.body,{childList:true,subtree:true,characterData:true});
      document.querySelector('.stv-nodes>.stv-node [data-focus="details"]').click();
    ''')


@pytest.mark.browser
@pytest.mark.requirements('STV_SYS_008','STV_SWR_043','STV_SWR_044')
@pytest.mark.parametrize('protocol',['file','http'])
def test_large_project_at_visible_capacity(browser,protocol):
    output=Path(os.environ.get('STV_CAPACITY_OUTPUT','docs/_build/benchmark-v2/html')).resolve()
    assert (output/'index.html').is_file(),'Run scripts/benchmark.py before capacity verification'
    runs=[]
    browser.set_script_timeout(35)
    temporary=tempfile.TemporaryDirectory(prefix='stv-cap-') if protocol=='file' else None
    if temporary:
        assert Path(temporary.name).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
        # Full hash names need a short physical output root in Windows Firefox.
        short=Path(temporary.name)/'html';shutil.copytree(output,short);output=short
    try:
        _measure_capacity(browser,output,protocol,runs)
    finally:
        if temporary:
            assert Path(temporary.name).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
            temporary.cleanup()
    result={'browser':browser.capabilities['browserVersion'],'geckodriver':browser.capabilities.get('moz:geckodriverVersion'),
            'memory_scope':'Sum of working sets of the isolated Firefox process tree, including content/GPU helpers; shared pages may be counted more than once',
            'runs':runs,'startup_median_ms':statistics.median(r['startup_ms'] for r in runs),
            'startup_max_ms':max(r['startup_ms'] for r in runs),
            'expansion_median_ms':statistics.median(v for r in runs for v in r['expansion_ms']),
            'expansion_max_ms':max(v for r in runs for v in r['expansion_ms'])}
    target=Path(os.environ.get('STV_CAPACITY_METRICS','docs/_build/capacity-browser.json'));target.parent.mkdir(parents=True,exist_ok=True)
    aggregate=json.loads(target.read_text(encoding='utf-8')) if target.exists() else {}
    aggregate[protocol]=result
    target.write_text(json.dumps(aggregate,indent=2),encoding='utf-8')


def _measure_capacity(browser,output,protocol,runs):
    with published_url(output,protocol) as url:
        for repetition in range(3):
            start=time.perf_counter();browser.get(url)
            wait=WebDriverWait(browser,30)
            wait.until(lambda d:d.find_elements(By.CSS_SELECTOR,'.stv-view[data-stv-revision="0"]'))
            startup=(time.perf_counter()-start)*1000
            identity=browser.find_element(By.CSS_SELECTOR,'.stv-view').get_attribute('data-stv-build')
            count=browser.execute_script('return Object.keys(__STV_DATA__.graphs[arguments[0]].objects).length',identity)
            assert count==30000
            expansion=[]
            while len(browser.find_elements(By.CSS_SELECTOR,'.stv-nodes>.stv-node'))<200:
                selector=browser.execute_script('''
                  const graph=__STV_DATA__.graphs[arguments[0]],nodes=[...document.querySelectorAll('.stv-nodes>.stv-node')],ids=new Set(nodes.map(n=>n.querySelector('.stv-id').textContent));
                  for(const b of document.querySelectorAll('.stv-nodes>.stv-node .stv-groups button[aria-expanded="false"]')) {
                    const [id,r,d]=JSON.parse(b.dataset.focus),extra=graph.adjacency[id][d][r].filter(t=>!ids.has(t));
                    if(extra.length&&ids.size+extra.length<=200){b.id='capacity-action';return '#capacity-action';}
                  }return null;
                ''',identity)
                assert selector,'Fixture must reach exactly 200 nodes through complete groups'
                measured=click_revision(browser,selector);assert 'error' not in measured,measured
                expansion.append(measured['ms'])
                browser.execute_script("document.getElementById('capacity-action')?.removeAttribute('id')")
            root=browser.find_element(By.CSS_SELECTOR,'.stv-view');revision=root.get_attribute('data-stv-revision')
            browser.execute_script('''
              const g=__STV_DATA__.graphs[arguments[0]],ids=new Set([...document.querySelectorAll('.stv-id')].map(e=>e.textContent));
              const control=[...document.querySelectorAll('.stv-groups button[aria-expanded="false"]')].find(b=>{const [id,r,d]=JSON.parse(b.dataset.focus);return g.adjacency[id][d][r].some(t=>!ids.has(t));});control.click();
            ''',identity)
            wait.until(lambda d:'200-node limit' in root.find_element(By.CSS_SELECTOR,'.stv-status').text)
            assert root.get_attribute('data-stv-revision')==revision
            assert len(browser.find_elements(By.CSS_SELECTOR,'.stv-nodes>.stv-node'))==200
            first_detail=measure_detail(browser);assert first_detail is not None
            browser.find_element(By.CSS_SELECTOR,'.stv-detail button').click()
            cached_detail=measure_detail(browser);assert cached_detail is not None
            browser.find_element(By.CSS_SELECTOR,'.stv-detail button').click()
            control=browser.find_element(By.CSS_SELECTOR,'.stv-nodes>.stv-node .stv-groups button[aria-expanded="true"]')
            browser.execute_script("arguments[0].id='collapse-action'",control)
            collapse=click_revision(browser,'#collapse-action');assert 'error' not in collapse,collapse
            memory=browser_memory(browser.capabilities['moz:processID'])
            runs.append({'startup_ms':startup,'expansion_ms':expansion,'collapse_ms':collapse['ms'],
                         'first_detail_ms':first_detail,'cached_detail_ms':cached_detail,'browser_memory':memory})
