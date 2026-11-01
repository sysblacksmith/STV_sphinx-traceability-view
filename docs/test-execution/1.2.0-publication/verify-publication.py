"""Verify public release receipts, PyPI hashes and the deployed documentation."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.request
from bs4 import BeautifulSoup

ROOT=Path.cwd()
STAGE=ROOT/'docs/_build/release-publication'
RECORD=ROOT/'docs/test-execution/1.2.0-publication'
context=dict(os.environ,GIT_TERMINAL_PROMPT='0',GCM_INTERACTIVE='never')
credential=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',capture_output=True,text=True,env=context,timeout=20,check=True)
fields=dict(line.split('=',1) for line in credential.stdout.splitlines() if '=' in line)
headers={'Authorization':'Bearer '+fields['password'],'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
base='https://api.github.com/repos/sysblacksmith/STV_sphinx-traceability-view'
def api(path):
    with urllib.request.urlopen(urllib.request.Request(base+path,headers=headers),timeout=30) as response:return json.load(response)
def public(url):
    with urllib.request.urlopen(urllib.request.Request(url,headers={'Cache-Control':'no-cache'}),timeout=60) as response:return response.read()
commit='c75dbbe84481bf0c319daf09151b6330d6f99c9d'
release=api('/releases/tags/v1.2.0')
assert not release['draft'] and not release['prerelease']
ref=api('/git/ref/tags/v1.2.0')
assert ref['object']['type']=='tag'
tag=api('/git/tags/'+ref['object']['sha'])
assert tag['object']['sha']==commit
workflow=api('/actions/runs/41316712011')
assert workflow['head_sha']==commit and workflow['conclusion']=='success'
jobs=api('/actions/runs/41316712011/jobs?per_page=100')['jobs']
assert all(job['conclusion']=='success' for job in jobs),[(j['name'],j['conclusion']) for j in jobs]
assets=[]
qualified=ROOT/'docs/test-execution/1.2.0-candidate-1/artifacts'
for asset in release['assets']:
    path=qualified/asset['name']
    assert path.is_file(),asset['name']
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    assert hashlib.sha256(public(asset['browser_download_url'])).hexdigest()==digest
    assets.append(dict(name=asset['name'],sha256=digest,url=asset['browser_download_url'],size=asset['size']))
assert len(assets)==3
pypi=json.loads(public('https://pypi.org/pypi/sphinx-traceability-view/1.2.0/json'))
expected={a['name']:a['sha256'] for a in assets if a['name']!='SHA256SUMS'}
assert {item['filename']:item['digests']['sha256'] for item in pypi['urls']}==expected
docs_url='https://sysblacksmith.github.io/STV_sphinx-traceability-view/'
html=public(docs_url+'?release=1.2.0')
assert 'STV version: 1.2.0' in BeautifulSoup(html,'html.parser').get_text(' ',strip=True)
runtime=public(docs_url+'_static/stv/stv.js')
assert hashlib.sha256(runtime).hexdigest()==hashlib.sha256((ROOT/'src/sphinx_traceability_view/static/stv.js').read_bytes()).hexdigest()
RECORD.mkdir(exist_ok=True)
receipt=dict(verified_at=datetime.now(timezone.utc).isoformat(),release=release['html_url'],published_at=release['published_at'],commit=commit,annotated_tag='v1.2.0',tag_object=ref['object']['sha'],workflow=workflow['html_url'],workflow_conclusion=workflow['conclusion'],assets=assets,pypi='https://pypi.org/project/sphinx-traceability-view/1.2.0/',pypi_hashes_match=True,documentation=docs_url,documentation_version='1.2.0',documentation_runtime_sha256=hashlib.sha256(runtime).hexdigest())
(RECORD/'publication-verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
(RECORD/'workflow-jobs.json').write_text(json.dumps([dict(name=j['name'],conclusion=j['conclusion'],started_at=j['started_at'],completed_at=j['completed_at'],url=j['html_url']) for j in jobs],indent=2)+'\n')
print(json.dumps(receipt,indent=2))
