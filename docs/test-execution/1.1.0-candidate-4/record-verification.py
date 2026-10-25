"""Update only the scoped verification metadata after full observed coverage."""
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
results=json.loads((HERE/'results.json').read_text(encoding='utf-8'))
assert results['outcomes']=={'passed':229,'failed':0,'error':0,'skipped':0}
targets={
 'requirements-stakeholder.rst':{f'STV_SHR_{i:03}' for i in range(58,62)},
 'requirements-system.rst':{'STV_SYS_011'},
 'requirements-software.rst':{f'STV_SWR_{i:03}' for i in range(66,73)},
 'test-cases/system-tests.rst':{f'STV_TC_SY_{i:03}' for i in range(66,70)},
 'test-cases/software-tests.rst':{f'STV_TC_SW_{i:03}' for i in range(51,56)}}
changes=[]
for relative,identities in targets.items():
    path=ROOT/'docs'/relative;lines=path.read_text(encoding='utf-8').splitlines();current=None;seen=set()
    for index,line in enumerate(lines):
        if line.startswith('   :id: '):current=line.split(':id: ',1)[1]
        if current in identities and line.startswith('   :verification_state: '):
            assert line.split()[-1] in ['partial','passed'],(current,line)
            changes.append({'id':current,'before':line.split()[-1],'after':'passed'});seen.add(current)
            lines[index]='   :verification_state: passed'
    assert seen==identities,(relative,seen,identities)
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
(HERE/'verification-assessment.json').write_text(json.dumps({'basis':'Full candidate-4 execution plus criterion assessment and owner native/zoom observations; acceptance statuses unchanged','changes':changes},indent=2)+'\n',encoding='utf-8')
print(len(changes),'scoped verification states assessed from full coverage')
