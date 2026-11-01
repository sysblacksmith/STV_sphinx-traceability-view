"""Map actual reports to reviewed canonical procedures, retaining prior evidence."""
from collections import defaultdict
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
result = json.loads((HERE/'results.json').read_text())
assert not any(result['outcomes'][state] for state in ('failed', 'error', 'skipped'))
assert all(item['returncode'] == 0 for item in result['attempts'] if item['suite'] != 'documentation')
known = defaultdict(set)
for item in json.loads((HERE.parent/'1.1.0-candidate-4/case-results.json').read_text()):
    known[item['selector']].add(item['case_id'])
groups = defaultdict(list)
unmapped = []
for report in ('pytest.xml', 'node.xml', 'remember-supplement-final.xml'):
    tree = ET.parse(HERE/report)
    if report == 'remember-supplement-final.xml':
        suite = tree.find('.//testsuite')
        completed_at = (datetime.fromisoformat(suite.get('timestamp'))+timedelta(seconds=float(suite.get('time')))).astimezone(timezone.utc).isoformat()
    else:
        completed_at = next(item['finished'] for item in result['attempts'] if item['suite'] == ('pytest' if report == 'pytest.xml' else 'node-tests'))
    for case in tree.findall('.//testcase'):
        outcome = 'failed' if case.find('failure') is not None else 'error' if case.find('error') is not None else 'skipped' if case.find('skipped') is not None else 'passed'
        assert outcome == 'passed', (report, case.attrib)
        selector = case.get('classname', '')+'::'+case.get('name', '')
        identities = set(known.get(selector, set()))
        if 'test_remembered_view::' in selector or report == 'remember-supplement-final.xml':
            identities = {'STV_TC_SY_070'}
        elif selector.startswith('test::') and re.search(r'STV_SWR_07[345]', selector):
            identities = {'STV_TC_SW_056'}
        elif 'test_publication::test_failed_audit_cleans_temporary_output' in selector:
            identities = {'STV_TC_SY_053'}
        elif 'test_publication::test_failed_rollback_preserves_recoverable_backup' in selector:
            identities = {'STV_TC_SY_054'}
        row = dict(selector=selector, report=report, result=outcome, report_completed_at=completed_at, mapping_source='Reviewed candidate-4 selector allocation retained; explicit CR019, failed-audit and failed-rollback criterion allocation')
        if not identities:
            unmapped.append(row)
        for identity in identities:
            groups[identity].append(dict(row, case_id=identity))

runtime = json.loads((HERE/'supplement-commands-retry.json').read_text())
assert all(item['returncode'] == 0 for item in runtime)
historical = json.loads((HERE/'historical-check.json').read_text())
assert historical['result'] == 'passed'
for identity, report, selector, completed in [
    ('STV_TC_SY_049', 'historical-check.json', 'Fresh Git/retained-archive inventory and complete licensing supplement', historical['finished']),
    ('STV_TC_SY_050', 'supplement-commands-retry.json', 'Fresh offline Python 3.10 install, dependency check and clean host', runtime[-1]['finished']),
    ('STV_TC_SY_057', 'supplement-commands-retry.json', 'scripts/ci.py runtime against the installed 1.2.0 wheel', runtime[-1]['finished']),
    ('STV_TC_SY_067', 'export-capacity.json', '200 nodes / ten cards, file/HTTP, 1600/900px SVG exports', json.loads((HERE/'export-capacity.json').read_text())['finished']),
    ('STV_TC_SY_067', 'hover-export.json', 'Real visible-hover capture/reopen on file and HTTP', json.loads((HERE/'hover-export.json').read_text())['recorded_at']),
]:
    groups[identity].append(dict(case_id=identity, selector=selector, report=report, result='passed', report_completed_at=completed, mapping_source='Fresh supplemental procedure'))
expected = {f'STV_TC_SY_{i:03}' for i in range(1, 71)} | {f'STV_TC_SW_{i:03}' for i in range(1, 57)}
deferred = set()
for path in (ROOT/'docs/test-cases').glob('*-tests.rst'):
    for block in re.split(r'(?=^\.\. test_case::)', path.read_text(), flags=re.M):
        match = re.search(r'^   :id: (STV_TC_\w+)$', block, re.M)
        if match and 'occurrence' in block.lower() and ':last_result: not_run' in block:
            deferred.add(match[1])
summary = dict(canonical_cases=len(groups), missing=sorted(expected-set(groups)-deferred), deferred=sorted(deferred), infrastructure=unmapped)
(HERE/'mapping-review.json').write_text(json.dumps(summary, indent=2)+'\n')
print(json.dumps(summary, indent=2))
if '--write' not in sys.argv:
    sys.exit(0)
assert not summary['missing']
assert len(unmapped) == 7, 'Review newly unmapped executable checks before recording executions'
lines = ['Canonical candidate executions', '===============================', '',
    'Actual current-candidate automated observations. These records preserve prior',
    'executions and acceptance states. Criterion assessment and owner native checks',
    'are reported separately in :doc:`qualification` and :doc:`manual-observations`.', '',
    'The complete main selection and CR019 supplements are separate runs; repeated',
    'supplemental checks are not added again to the main-suite total.', '']
rows = []
for identity, items in sorted(groups.items()):
    execution = 'STV_TE_'+hashlib.sha256((HERE.name+':'+identity).encode()).hexdigest()[:16].upper()
    completed = max(item['report_completed_at'] for item in items)
    evidence = '; '.join('docs/test-execution/'+HERE.name+'/'+name for name in sorted({item['report'] for item in items}))
    lines += [f'.. test_execution:: {identity} current candidate observations', f'   :id: {execution}', '   :status: recorded', '   :basis: observed', f'   :evidence: {evidence}', '   :priority: unassigned', '   :verification_state: not_assessed', '   :result: passed', f'   :executed_at: {completed}', '', f'   :need:`{identity}`: {len(items)} mapped current-candidate observations passed.', '   Selectors, reports and exact candidate identity are retained in', '   :download:`case-results.json <case-results.json>` and :doc:`index`.', '']
    path = ROOT/'docs/test-cases'/('system-tests.rst' if '_SY_' in identity else 'software-tests.rst')
    text = path.read_text()
    pattern = r'(:id: '+identity+r'\n)(.*?)(?=\n\.\. test_case::|\Z)'
    match = re.search(pattern, text, re.S)
    assert match, identity
    block = match[0]
    if execution not in block:
        if ':executed_by:' in block:
            block = re.sub(r'(:executed_by: [^\n]+)', r'\g<1>, '+execution, block)
        else:
            block = block.replace('   :last_result:', f'   :executed_by: {execution}\n   :last_result:')
    block = re.sub(r':last_result: \w+', ':last_result: passed', block)
    path.write_text(text[:match.start()]+block+text[match.end():])
    rows += [dict(item, execution_id=execution) for item in items]
(HERE/'cases.rst').write_text('\n'.join(lines)+'\n')
(HERE/'case-results.json').write_text(json.dumps(rows, indent=2)+'\n')
(HERE/'infrastructure-results.json').write_text(json.dumps(unmapped, indent=2)+'\n')
