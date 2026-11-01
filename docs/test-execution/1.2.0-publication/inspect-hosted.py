"""Read hosted state without exposing existing Git credentials."""
import json
import os
import subprocess
import sys
import urllib.request
context = dict(os.environ, GIT_TERMINAL_PROMPT='0', GCM_INTERACTIVE='never')
result = subprocess.run(['git','credential','fill'], input='protocol=https\nhost=github.com\n\n', capture_output=True, text=True, env=context, timeout=20, check=True)
fields = dict(line.split('=',1) for line in result.stdout.splitlines() if '=' in line)
base = 'https://api.github.com/repos/sysblacksmith/STV_sphinx-traceability-view'
headers = {'Authorization':'Bearer '+fields['password'], 'Accept':'application/vnd.github+json', 'X-GitHub-Api-Version':'2022-11-28'}
def request(path):
    with urllib.request.urlopen(urllib.request.Request(base+path, headers=headers), timeout=30) as response:
        return json.load(response)
if sys.argv[1] == 'runs':
    data = request('/actions/runs?per_page=20'+('&head_sha='+sys.argv[2] if len(sys.argv)>2 else ''))
    print(json.dumps([dict(id=item['id'], name=item['name'], status=item['status'], conclusion=item['conclusion'], event=item['event'], head_sha=item['head_sha'], url=item['html_url']) for item in data['workflow_runs']], indent=2))
elif sys.argv[1] == 'release':
    data=request('/releases/tags/v1.2.0')
    print(json.dumps({key:data[key] for key in ('id','tag_name','html_url','draft','published_at','assets')},indent=2))
