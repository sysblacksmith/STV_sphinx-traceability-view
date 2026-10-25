from pathlib import Path
import json,re,hashlib,xml.etree.ElementTree as ET
from collections import defaultdict
root=Path.cwd();record=root/'docs/test-execution/1.1.0-candidate-2';assert not(record/'cases.rst').exists()
results=json.loads((record/'results.json').read_text());assert results['outcomes']==dict(passed=196,failed=0,error=0,skipped=0)
commands={c['suite']:c for c in results['attempts']};mapping={};provenance={}
for p in sorted((root/'docs/test-execution').glob('*/case-results.json')):
 try:items=json.loads(p.read_text())
 except (ValueError,UnicodeError):continue
 if not isinstance(items,list):continue
 for i in items:
  if 'selector'in i and 'case_id'in i:
   key=i['selector'].replace(' :: ','::');mapping[key]=i['case_id'];provenance[key]=p.relative_to(root).as_posix()
def new_mapping(s):
 if '.test_export_resources::' in s:return 'STV_TC_SW_055'
 if '.test_font_scale::' in s:return 'STV_TC_SW_052'
 if '.test_view_controls::test_standalone_svg_' in s:return 'STV_TC_SY_067'
 if '.test_view_controls::test_collapse_all_' in s:return 'STV_TC_SY_066'
 if '.test_view_controls::test_font_scales_' in s:return 'STV_TC_SY_068'
 if '.test_view_controls::test_page_' in s:return 'STV_TC_SY_069'
 if s.startswith('test::'):
  for req,case in [('066','051'),('068','052'),('070','053'),('071','053'),('069','054'),('072','055')]:
   if 'STV_SWR_'+req in s:return 'STV_TC_SW_'+case
 return None
groups=defaultdict(list);infra=[]
for report,suite in [('pytest.xml','pytest'),('node.xml','node-tests')]:
 for c in ET.parse(record/report).findall('.//testcase'):
  assert c.find('failure') is None and c.find('error') is None and c.find('skipped') is None
  selector=c.get('classname','')+'::'+c.get('name','');identity=mapping.get(selector) or new_mapping(selector)
  item=dict(selector=selector,report=report,result='passed',report_completed_at=commands[suite]['finished'],mapping_source=provenance.get(selector,'explicit CR015-018 selector review in record-results.py'))
  if identity:groups[identity].append(item)
  else:infra.append(item)
supp=json.loads((record/'supplement-commands.json').read_text());assert all(c['returncode']==0 for c in supp)
for identity in ['STV_TC_SY_050','STV_TC_SY_057']:
 groups[identity].append(dict(selector='scripts/ci.py runtime (clean installed Python 3.10)',report='supplement-commands.json',result='passed',report_completed_at=max(c['finished'] for c in supp),mapping_source='explicit installed-runtime procedure'))
lines=['Canonical automated candidate executions','========================================','','These records report the actual mapped automated variants, using their suite','completion timestamps. Requirement verification remains a separate assessment.','For CR015-018, extended/manual scenarios in the accepted designs are not all','covered by this automated selection; their verification state remains partial.','Native Save As dialogs and additional browsers are not claimed as automated','qualification. Candidate identity, totals and scope are in :doc:`index`.',''];all_items=[]
for identity,items in sorted(groups.items()):
 execution='STV_TE_'+hashlib.sha256((record.name+':'+identity).encode()).hexdigest()[:16].upper();timestamp=max(i['report_completed_at'] for i in items)
 lines+=['.. test_execution:: '+identity+' automated candidate variants','   :id: '+execution,'   :status: recorded','   :basis: observed','   :evidence: docs/test-execution/1.1.0-candidate-2/'+items[0]['report'],'   :priority: unassigned','   :verification_state: not_assessed','   :result: passed','   :executed_at: '+timestamp,'',f'   :need:`{identity}`: {len(items)} observed automated variants passed.','   Exact selectors and timestamps are in','   :download:`case-results.json <case-results.json>`. Candidate wheel SHA-256:','   ``'+results['wheel_sha256']+'``.','']
 found=False
 for p in (root/'docs/test-cases').glob('*.rst'):
  blocks=re.split(r'(?=^\.\. test_case::)',p.read_text(encoding='utf-8'),flags=re.M)
  for i,b in enumerate(blocks):
   if re.search(r'^   :id: '+identity+'$',b,re.M):
    b=re.sub(r'(:last_result:) \S+',r'\1 passed',b)
    if ':executed_by:' in b:b=re.sub(r'(:executed_by: [^\n]+)',r'\1, '+execution,b)
    else:b=b.replace('   :last_result:', '   :executed_by: '+execution+'\n   :last_result:')
    if identity in {*(f'STV_TC_SY_{n:03}' for n in range(66,70)),*(f'STV_TC_SW_{n:03}' for n in range(51,56))}:
     b=b.replace(':verification_state: not_assessed',':verification_state: partial')
    blocks[i]=b;p.write_text(''.join(blocks),encoding='utf-8');found=True;break
  if found:break
 assert found,identity
 all_items += [dict(item,case_id=identity,execution_id=execution) for item in items]
(record/'cases.rst').write_text('\n'.join(lines),encoding='utf-8');(record/'case-results.json').write_text(json.dumps(all_items,indent=2),encoding='utf-8');(record/'infrastructure-results.json').write_text(json.dumps(infra,indent=2),encoding='utf-8')
print(len(groups),'canonical automated execution aggregates;',len(infra),'infrastructure checks retained separately')
