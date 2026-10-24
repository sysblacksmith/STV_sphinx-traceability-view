"""Import actual full-run results using retained, explicit canonical selector maps."""
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
assert not (RECORD/'cases.rst').exists(), 'Do not overwrite execution history'
metadata = json.loads((RECORD/'results.json').read_text())
commands = {c['suite']: c for c in metadata['attempts']}
mapping = {}
provenance = {}
# Newest complete development mappings supersede earlier maps for identical selectors.
for folder in ('maintenance-2026-10-24', 'prsa-002-fix', 'prsa-001-003-fix',
               'prsa-004-fix', 'prsa-005-fix', 'prsa-006-fix', 'pr013-final',
               'cr013-rows', 'pr014-boundary', 'cr014-details', 'pr015-details'):
    source = RECORD.parent/folder/'case-results.json'
    if not source.exists():
        continue
    data = json.loads(source.read_text(encoding='utf-8'))
    if not isinstance(data, list):
        continue
    for item in data:
        if 'selector' in item and 'case_id' in item:
            mapping[item['selector']] = item['case_id']
            provenance[item['selector']] = source.relative_to(ROOT).as_posix()

case_sources = {}
for source in (ROOT/'docs/test-cases').glob('*.rst'):
    for block in re.split(r'(?=^\.\. test_case::)', source.read_text(encoding='utf-8'), flags=re.M)[1:]:
        identity = re.search(r'^   :id: (\S+)', block, re.M)[1]
        case_sources[identity] = source
        match = re.search(r'\*\*Executable selector:\*\*\s*``([^`]+)``', block)
        if match:
            selector = match[1].replace(' :: ', '::')
            if selector.startswith('frontend/'):
                selector = 'test :: '+selector.split('::', 1)[1]
            else:
                path, sep, test = selector.partition('::')
                if path.endswith('.py'):
                    selector = path[:-3].replace('/', '.')+sep+test
            mapping.setdefault(selector, identity)
            provenance.setdefault(selector, source.relative_to(ROOT).as_posix())

grouped = defaultdict(list)
for report, suite in (('pytest.xml', 'pytest'), ('node.xml', 'node-tests')):
    for case in ET.parse(RECORD/report).findall('.//testcase'):
        raw = case.get('classname', '')+'::'+case.get('name', '')
        variants = [raw, raw.replace('::', ' :: ', 1)]
        selector = next((s for s in variants if s in mapping), None)
        assert selector, 'Unmapped actual selector: '+raw
        outcome = 'failed' if case.find('failure') is not None else 'error' if case.find('error') is not None else 'skipped' if case.find('skipped') is not None else 'passed'
        grouped[mapping[selector]].append(dict(selector=raw, report=report, result=outcome,
            report_completed_at=commands[suite]['finished'], mapping_source=provenance[selector]))

historical = json.loads((RECORD/'historical-check.json').read_text())
grouped['STV_TC_SY_049'].append(dict(selector='historical archive and complete supplement check',
    report='historical-check.json', result=historical['result'],
    report_completed_at=historical['finished'], mapping_source='docs/test-cases/system-tests.rst'))
supplement = json.loads((RECORD/'supplement-commands.json').read_text())
for identity, suites in [('STV_TC_SY_050', {c['suite'] for c in supplement}),
                         ('STV_TC_SY_057', {'runtime310-host'})]:
    selected = [c for c in supplement if c['suite'] in suites]
    assert selected and all(c['returncode']==0 for c in selected)
    grouped[identity].append(dict(selector='; '.join(c['suite'] for c in selected),
        report='supplement-commands.json', result='passed',
        report_completed_at=max(c['finished'] for c in selected),
        mapping_source='docs/test-cases/system-tests.rst'))

lines = ['Candidate canonical executions', '='*45, '',
         'Each execution aggregates all actual runner variants mapped to its canonical',
         'procedure. Suite completion timestamps are used; individual finish times',
         'are not invented. Candidate identity and commands are in :doc:`index`.', '']
all_items = []
for identity, items in sorted(grouped.items()):
    result = next((state for state in ('error', 'failed', 'skipped') if any(i['result']==state for i in items)), 'passed')
    execution = 'STV_TE_'+hashlib.sha256((RECORD.name+':'+identity).encode()).hexdigest()[:16].upper()
    timestamp = max(i['report_completed_at'] for i in items)
    reports = sorted({i['report'] for i in items})
    lines += ['.. test_execution:: '+identity+' release procedure', '   :id: '+execution,
              '   :status: recorded', '   :basis: observed',
              '   :evidence: '+(RECORD/reports[0]).relative_to(ROOT).as_posix(),
              '   :priority: unassigned', '   :verification_state: not_assessed',
              '   :result: '+result, '   :executed_at: '+timestamp, '',
              f'   **Case:** :need:`{identity}`. {len(items)} actual runner variants; {result}.',
              '   Exact selectors, mapping provenance and report times are retained in',
              '   :download:`case-results.json <case-results.json>`. Wheel SHA-256:',
              '   ``'+metadata['wheel_sha256']+'``.', '',
              '   Reports: '+', '.join(':download:`'+r+' <'+r+'>`' for r in reports)+'.', '']
    source = case_sources[identity]
    text = source.read_text(encoding='utf-8')
    blocks = re.split(r'(?=^\.\. test_case::)', text, flags=re.M)
    for index, block in enumerate(blocks):
        if re.search(r'^   :id: '+identity+r'$', block, re.M):
            block = re.sub(r'(:last_result:) \S+', r'\1 '+result, block)
            block = re.sub(r'(:executed_by: [^\n]+)', r'\1, '+execution, block)
            blocks[index] = block
            break
    source.write_text(''.join(blocks), encoding='utf-8')
    all_items.extend(dict(i, case_id=identity, execution_id=execution) for i in items)
(RECORD/'cases.rst').write_text('\n'.join(lines), encoding='utf-8')
(RECORD/'case-results.json').write_text(json.dumps(all_items, indent=2), encoding='utf-8')
with (RECORD/'index.rst').open('a', encoding='utf-8') as stream:
    stream.write('\nCanonical candidate results\n-----------------------------\n\n.. toctree::\n   :maxdepth: 1\n\n   cases\n')
print(f'Imported {len(all_items)} actual variants into {len(grouped)} canonical executions.')
