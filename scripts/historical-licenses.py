"""Inventory retained historical STV archives without rewriting their bytes or Git history."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import subprocess
import tarfile
import zipfile

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'docs/licensing/historical'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def inventory():
    found={}
    def inspect(data,location,oid=None):
        if not (data.startswith(b'PK\x03\x04') or data.startswith(b'\x1f\x8b')):
            return
        if data.startswith(b'PK'):
            with zipfile.ZipFile(io.BytesIO(data)) as archive:
                members={n:archive.read(n) for n in archive.namelist() if not n.endswith('/')}
        else:
            with tarfile.open(fileobj=io.BytesIO(data),mode='r:gz') as archive:
                members={m.name:archive.extractfile(m).read() for m in archive.getmembers() if m.isfile()}
        elk=[(n,b) for n,b in members.items() if n.endswith('/vendor/elk.bundled.js')]
        if not elk:
            return  # Not an STV archive; toolchains and unrelated archives are outside scope.
        expected=json.loads((ROOT/'frontend/legal/elk-inventory.json').read_text())['elkjs']['sha256']
        assert all(digest(b)==expected for _,b in elk),'Unreviewed historical ELK binary: '+location
        key=digest(data)
        item=found.setdefault(key,{'sha256':key,'bytes':len(data),'locations':[],'git_objects':[],
            'elk_sha256':expected,'supplement':'LICENSE.txt + THIRD_PARTY_NOTICES.txt + ELK-SOURCE.txt + ELK-INVENTORY.json',
            'archive_unchanged':True})
        if location not in item['locations']:item['locations'].append(location)
        if oid and oid not in item['git_objects']:item['git_objects'].append(oid)
    names={}
    for line in subprocess.check_output(['git','rev-list','--objects','--all'],cwd=ROOT,text=True).splitlines():
        oid,_,name=line.partition(' ')
        if name:names.setdefault(oid,name)
    objects=subprocess.check_output(['git','cat-file','--batch-all-objects','--batch-check=%(objectname) %(objecttype)'],cwd=ROOT,text=True)
    for line in objects.splitlines():
        oid,kind=line.split()
        if kind=='blob':
            data=subprocess.check_output(['git','cat-file','blob',oid],cwd=ROOT)
            inspect(data,names.get(oid,'Git object '+oid),oid)
    for folder in (ROOT/'docs/test-execution',ROOT/'dist'):
        for pattern in ('*.whl','*.tar.gz'):
            for path in folder.rglob(pattern):inspect(path.read_bytes(),path.relative_to(ROOT).as_posix())
    for item in found.values():
        item['locations'].sort();item['git_objects'].sort()
    return sorted(found.values(),key=lambda i:i['sha256'])


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--write',action='store_true');args=parser.parse_args()
    current=inventory();target=DEST/'artifacts.json'
    if args.write:
        target.write_text(json.dumps({'scope':'Historical STV archives available at remediation; includes unreachable local Git objects',
            'artifacts':current},indent=2)+'\n',encoding='utf-8')
    else:
        retained={x['sha256']:x for x in json.loads(target.read_text())['artifacts']}
        for item in current:
            assert item['sha256'] in retained,'Unreviewed retained historical archive: '+str(item['locations'])
            assert item['elk_sha256']==retained[item['sha256']]['elk_sha256']
    for source,dest in [('LICENSE','LICENSE.txt'),('src/sphinx_traceability_view/static/THIRD_PARTY_NOTICES.txt','THIRD_PARTY_NOTICES.txt'),('src/sphinx_traceability_view/static/vendor/ELK-SOURCE.txt','ELK-SOURCE.txt'),('frontend/legal/elk-inventory.json','ELK-INVENTORY.json')]:
        assert (ROOT/source).read_bytes()==(DEST/dest).read_bytes(),'Supplement drift: '+dest
    print(f'{len(current)} distinct historical archives verified; original bytes and Git history retained.')


if __name__=='__main__':main()
