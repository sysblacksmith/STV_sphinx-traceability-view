"""Link one retained release run's actual JUnit cases to canonical RST cases.

Usage: implementation-python docs/test-execution/import-case-results.py RECORD
This adds immutable execution records; it never manufactures missing results.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record')
    args = parser.parse_args()
    if Path(args.record).name != args.record:
        parser.error('record must be a directory name')
    record = ROOT/'docs/test-execution'/args.record
    target = record/'cases.rst'
    if target.exists():
        parser.error('execution records already exist; do not overwrite history')
    metadata = json.loads((record/'candidate.json').read_text(encoding='utf-8'))
    commands = {item['suite']: item for item in json.loads((record/'commands.json').read_text(encoding='utf-8'))}
    # Current consolidated specifications own selectors; historical review maps
    # retain their original paths and must not drive a new release import.
    by_selector = {}
    case_sources = {}
    for source in (ROOT/'docs/test-cases').glob('*.rst'):
        for block in re.split(r'(?=^\.\. test_case::)', source.read_text(encoding='utf-8'), flags=re.M)[1:]:
            identity = re.search(r'^   :id: (\S+)', block, re.M)[1]
            match = re.search(r'\*\*Executable selector:\*\* ``([^`]+)``(?: in\s+``([^`]+)``)?', block)
            if not match:
                continue  # Planned/manual cases have no executable result to import.
            selector = match[1] if not match[2] else match[2]+' :: '+match[1]
            if selector in by_selector:
                raise RuntimeError('Duplicate executable selector: '+selector)
            by_selector[selector] = {'id': identity}
            case_sources[identity] = source
    imported = []
    lines = ['Per-case execution records', '='*80, '',
             'Results below come from this run\'s retained JUnit reports. Timestamps are',
             'the enclosing suite completion time (per-case finish times were not emitted).',
             'Candidate/test/environment identity and exact commands are retained in',
             ':download:`candidate.json <candidate.json>` and',
             ':download:`commands.json <commands.json>`. Results do not resolve unrelated',
             'known issues or demonstrate full acceptance-criterion coverage by themselves.', '']
    for report, suite in (('pytest.xml','pytest'), ('node.xml','node-tests')):
        for case in ET.parse(record/report).findall('.//testcase'):
            if suite == 'pytest':
                selector = case.get('classname').replace('.', '/')+'.py::'+case.get('name')
            else:
                source = Path(case.get('file')).relative_to(ROOT).as_posix()
                selector = source+' :: '+case.get('name')
            if selector not in by_selector:
                raise RuntimeError('Unmodeled executable: '+selector)
            design = by_selector[selector]
            identity = 'STV_TE_'+hashlib.sha256((args.record+':'+selector).encode()).hexdigest()[:16].upper()
            result = ('failed' if case.find('failure') is not None else
                      'error' if case.find('error') is not None else
                      'skipped' if case.find('skipped') is not None else 'passed')
            timestamp = commands[suite]['finished']
            lines += ['.. test_execution:: '+selector, '   :id: '+identity,
                      '   :status: recorded', '   :basis: observed',
                      f'   :evidence: docs/test-execution/{args.record}/{report} :: {selector}',
                      '   :priority: unassigned', '   :verification_state: not_assessed',
                      '   :result: '+result, '   :executed_at: '+timestamp, '',
                      '   **Case:** :need:`'+design['id']+'`.', '',
                      '   **Candidate:** ``'+metadata['revision']+'`` plus the recorded',
                      '   worktree/source identity; wheel SHA-256',
                      '   ``'+metadata['wheel_sha256']+'``.', '',
                      '   **Report:** :download:`'+report+' <'+report+'>`, case',
                      '   ``'+selector+'``. Full suite invocation and environment are retained',
                      '   in commands.json and candidate.json. Suite-completion timestamp',
                      '   granularity is used consistently for this attempt.', '']
            imported.append(dict(case_id=design['id'], execution_id=identity,
                                 selector=selector, result=result, executed_at=timestamp))
    if len(imported) != len(by_selector) or len({x['case_id'] for x in imported}) != len(by_selector):
        raise RuntimeError('Expected exactly one actual result for every modeled executable')
    target.write_text('\n'.join(lines), encoding='utf-8')
    for item in imported:
        source = case_sources[item['case_id']]
        text = source.read_text(encoding='utf-8')
        blocks = re.split(r'(?=^\.\. test_case::)', text, flags=re.M)
        for index, block in enumerate(blocks):
            if re.search(r'^   :id: '+re.escape(item['case_id'])+r'$', block, re.M):
                block = re.sub(r'(:last_result:) \S+', r'\1 '+item['result'], block)
                if ':executed_by:' in block:
                    block = re.sub(r'(:executed_by: [^\n]+)', r'\1, '+item['execution_id'], block)
                else:
                    block = block.replace('   :last_result:', '   :executed_by: '+item['execution_id']+'\n   :last_result:')
                blocks[index] = block
                break
        else:
            raise RuntimeError('Canonical case missing: '+item['case_id'])
        source.write_text(''.join(blocks), encoding='utf-8')
    (record/'case-results.json').write_text(json.dumps(imported,indent=2)+'\n',encoding='utf-8')
    with (record/'index.rst').open('a',encoding='utf-8') as stream:
        stream.write('\nCanonical case results\n'+('-'*80)+'\n\n.. toctree::\n   :maxdepth: 1\n\n   cases\n\n* :download:`Case-result mapping <case-results.json>`\n')
    print(f'Imported {len(imported)} actual per-case results; planned cases remain unexecuted.')


if __name__ == '__main__':
    main()
