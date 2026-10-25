"""Publish the authorized final release, using only qualified immutable assets.

GitHub's connector cannot create releases/upload assets. This uses the existing
Git credential helper without printing or persisting credentials. No PyPI API
token is used: release.yml performs Trusted Publishing after this operation.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import runpy
import subprocess
import urllib.parse
import urllib.request

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
TAG='v1.1.0'
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--commit',required=True)
args=parser.parse_args()
def git(*arguments):
    return subprocess.check_output(['git',*arguments],cwd=ROOT,text=True).strip()
assert git('branch','--show-current')=='main'
assert git('rev-parse','HEAD')==git('rev-parse',TAG+'^{commit}')==args.commit
assert git('cat-file','-t',TAG)=='tag'
assert not git('status','--porcelain'),'Commit the final reviewed baseline first'
subprocess.run(['git','merge-base','--is-ancestor',args.commit,'origin/main'],cwd=ROOT,check=True)
final=json.loads((HERE/'final-validation.json').read_text(encoding='utf-8'))
assert final['passed'] is True
release_tools=runpy.run_path(str(ROOT/'scripts/release.py'))
release_tools['validate_artifacts'](HERE/'artifacts',TAG)
checksums={name:checksum for checksum,name in (line.split('  ',1) for line in (HERE/'artifacts/SHA256SUMS').read_text().splitlines())}
assert set(checksums)=={'sphinx_traceability_view-1.1.0-py3-none-any.whl','sphinx_traceability_view-1.1.0.tar.gz'}
paths=[HERE/'artifacts'/name for name in sorted(checksums)]+[HERE/'artifacts/SHA256SUMS']
for path in paths[:-1]:assert hashlib.sha256(path.read_bytes()).hexdigest()==checksums[path.name]
notes=(HERE/'github-release-notes.md.txt').read_text(encoding='utf-8')
assert not notes.startswith('Draft') and 'pending consolidation' not in notes
context=dict(os.environ,GIT_TERMINAL_PROMPT='0',GCM_INTERACTIVE='never')
credential=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',capture_output=True,text=True,env=context,timeout=20,check=True)
fields=dict(line.split('=',1) for line in credential.stdout.splitlines() if '=' in line)
headers={'Authorization':'Bearer '+fields['password'],'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28'}
base='https://api.github.com/repos/sysblacksmith/STV_sphinx-traceability-view'
receipt_path=ROOT/'docs/_build/release-1.1.0-publication.json'
def request(url,data=None,method=None,content_type='application/json'):
    body=data if isinstance(data,bytes) else json.dumps(data).encode() if data is not None else None
    req=urllib.request.Request(url,data=body,headers=dict(headers,**{'Content-Type':content_type}),method=method)
    with urllib.request.urlopen(req,timeout=120) as response:return json.load(response)
def tag_matches():
    remote=request(base+'/git/ref/tags/'+TAG)
    assert remote['object']['type']=='tag'
    assert request(base+'/git/tags/'+remote['object']['sha'])['object']['sha']==args.commit
assert request(base)['visibility']=='public'
tag_matches()
existing=[r for r in request(base+'/releases?per_page=100') if r['tag_name']==TAG]
if existing:
    prior=json.loads(receipt_path.read_text(encoding='utf-8')) if receipt_path.is_file() else {}
    assert len(existing)==1 and existing[0]['id']==prior.get('id'),'Never replace an existing release'
    release=existing[0]
    if not release['draft']:
        assert prior.get('published_at'),'An issued release cannot be modified'
        print(json.dumps(prior,indent=2));raise SystemExit(0)
else:
    release=request(base+'/releases',{'tag_name':TAG,'target_commitish':args.commit,'name':TAG,'body':notes,'draft':True,'prerelease':False},method='POST')
receipt={'id':release['id'],'tag':TAG,'commit':args.commit,'url':release['html_url'],'stage':'draft','assets':[]}
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
available={a['name']:a for a in request(base+'/releases/'+str(release['id'])+'/assets?per_page=100')}
assert set(available)<={p.name for p in paths},'Unexpected draft asset; inspect before continuing'
for path in paths:
    expected=hashlib.sha256(path.read_bytes()).hexdigest()
    asset=available.get(path.name)
    if asset is None:
        upload=release['upload_url'].split('{',1)[0]+'?'+urllib.parse.urlencode({'name':path.name})
        asset=request(upload,path.read_bytes(),method='POST',content_type='application/octet-stream')
    assert asset['size']==path.stat().st_size and asset.get('digest')=='sha256:'+expected
    receipt['assets'].append({'name':path.name,'sha256':expected,'size':asset['size'],'url':asset['browser_download_url']})
    receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
tag_matches()
release=request(base+'/releases/'+str(release['id']),{'draft':False,'prerelease':False,'make_latest':'true'},method='PATCH')
assert release['draft'] is False and release['tag_name']==TAG
receipt.update(stage='published',published_at=release['published_at'],url=release['html_url'])
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
