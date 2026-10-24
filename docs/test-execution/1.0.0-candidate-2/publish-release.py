"""Publish the explicitly authorized v1.0.0 release using existing Git authentication.

Run only after creating and pushing the reviewed release commit and annotated tag.
No visibility, branch protection or workflow settings are changed.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--commit', required=True)
args = parser.parse_args()
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
tag = subprocess.check_output(['git', 'rev-parse', 'v1.0.0^{commit}'], cwd=ROOT, text=True).strip()
assert head == tag == args.commit
status = subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True)
allowed_intake = {'docs/maturity.rst', 'docs/change-requests/index.rst',
    'docs/change-requests/STV_CR_015_test-case-maturity-and-chart-size.rst'}
assert all(line[3:] in allowed_intake for line in status.splitlines()), 'Unexpected changes after qualification'
final = json.loads((RECORD/'final-validation.json').read_text())
assert final['passed'] is True
checksums = dict(line.split('  ', 1)[::-1] for line in (RECORD/'SHA256SUMS.txt').read_text().splitlines())
files = [RECORD/'artifacts'/name for name in checksums] + [RECORD/'SHA256SUMS.txt']
for path in files[:-1]:
    assert hashlib.sha256(path.read_bytes()).hexdigest() == checksums[path.name]
context = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
credential = subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',capture_output=True,text=True,env=context,timeout=20,check=True)
fields = dict(line.split('=',1) for line in credential.stdout.splitlines() if '=' in line)
secret = fields['password']
base = 'https://api.github.com/repos/sysblacksmith/STV_sphinx-traceability-view'
headers = {'Authorization':'Bearer '+secret,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}

def request(url, data=None, method=None, content_type='application/json', binary=False):
    body = data if isinstance(data,bytes) else json.dumps(data).encode() if data is not None else None
    req = urllib.request.Request(url,data=body,headers=dict(headers,**{'Content-Type':content_type}),method=method)
    with urllib.request.urlopen(req,timeout=120) as response:
        return response.read() if binary else json.load(response)

repo = request(base)
original_visibility = repo['visibility']
remote = request(base+'/git/ref/tags/v1.0.0')
assert remote['object']['type'] == 'tag'
assert request(base+'/git/tags/'+remote['object']['sha'])['object']['sha'] == args.commit
existing = request(base+'/releases')
assert not any(r['tag_name']=='v1.0.0' for r in existing), 'Existing release must be inspected; never overwrite'
release = request(base+'/releases',dict(tag_name='v1.0.0',target_commitish=args.commit,
    name='v1.0.0',body=(RECORD/'github-release-notes.md.txt').read_text(encoding='utf-8'),draft=True,prerelease=False),method='POST')
uploaded = []
for path in files:
    url = release['upload_url'].split('{',1)[0]+'?'+urllib.parse.urlencode({'name':path.name})
    asset = request(url,path.read_bytes(),method='POST',content_type='application/octet-stream')
    assert asset['size'] == path.stat().st_size
    expected = hashlib.sha256(path.read_bytes()).hexdigest()
    assert asset.get('digest') == 'sha256:'+expected, 'Hosted asset digest differs or is missing'
    uploaded.append(dict(name=asset['name'],sha256=expected,size=asset['size'],url=asset['browser_download_url']))
assert request(base)['visibility'] == original_visibility
release = request(base+'/releases/'+str(release['id']),dict(draft=False,make_latest='true'),method='PATCH')
assert release['draft'] is False and release['tag_name']=='v1.0.0'
assert request(base)['visibility'] == original_visibility
receipt = dict(url=release['html_url'],id=release['id'],tag=release['tag_name'],commit=args.commit,
    published_at=release['published_at'],repository_visibility_unchanged=True,assets=uploaded,
    limits='Hosted CI, attestation, protection activation and runner improvements remain explicitly deferred.')
destination = ROOT/'docs/_build/release-publication.json'
destination.write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
