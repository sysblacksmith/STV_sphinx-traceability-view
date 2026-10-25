"""Read-only size inventory and optional cleanup proposal; deletes nothing."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
totals={};previous={}
for parent,dirs,files in os.walk(ROOT,followlinks=False):
    path=Path(parent);relative=path.relative_to(ROOT)
    dirs[:]=[d for d in dirs if not (path/d).is_symlink()]
    group=relative.parts[0] if relative.parts else '[root files]'
    size=sum((path/name).stat().st_size for name in files if not (path/name).is_symlink())
    totals[group]=totals.get(group,0)+size
    if len(relative.parts)>=3 and relative.parts[:2]==('docs','_build') and relative.parts[2].startswith('.html-previous-'):
        name=Path(*relative.parts[:3]).as_posix();previous[name]=previous.get(name,0)+size
proposal=[{'path':name,'bytes':size,'reason':'Previous successful generated documentation tree; current HTML and evidence retained','consequence':'Rebuild documentation if needed'} for name,size in sorted(previous.items())]
record={'recorded_at':datetime.now(timezone.utc).isoformat(),'git_status':subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True),
        'top_level_bytes':totals,'optional_removal_proposal':proposal,'proposed_bytes':sum(p['bytes'] for p in proposal),
        'deleted':False,'retained':'All dist archives, all candidate evidence, active/current builds and capacity fixtures, dependency environments and wheelhouse; uncertain staging trees retained'}
(HERE/'workspace-inventory.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
lines=['Workspace cleanup review','=========================','','Read-only inventory; nothing was deleted. All distributions, candidate evidence,',
       'current/active builds, capacity fixtures, dependency environments and wheelhouse',
       'are retained. Failed staging trees remain uncertain and are not proposed.','',
       'The following generated backup trees are optional removals, pending explicit',
       'owner approval of these exact paths. Each can be recreated by a documentation',
       'build; none is the current build or an active runner output.','',
       '.. list-table:: Optional cleanup proposal','   :header-rows: 1','','   * - Project-relative path','     - MiB']
for item in proposal:lines+=['   * - ``'+item['path']+'``',f'     - {item["bytes"]/1024**2:.2f}']
lines+=['',f'Total proposed: {record["proposed_bytes"]/1024**3:.3f} GiB. No deletion authorization',
        'is inferred from release authorization. The post-release review remains due',
        'when publication completes. Full sizes and status are retained in',
        ':download:`workspace-inventory.json <workspace-inventory.json>`.','']
(HERE/'cleanup-review.rst').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps({'optional_paths':len(proposal),'proposed_bytes':record['proposed_bytes'],'deleted':False},indent=2))
