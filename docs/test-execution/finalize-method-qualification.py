"""Retain final publication/traceability gates for the documentation migration."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record')
    args = parser.parse_args()
    if Path(args.record).name != args.record:
        parser.error('record must be a directory name')
    record = ROOT/'docs/test-execution'/args.record
    output = record/'qualification.json'
    if output.exists():
        parser.error('final evidence exists; retain it and use a new finalization record')
    shared = Path(os.environ['REQUIREMENTS_SKILL_DIR'])
    commands = [
        ('shared-model-tests', [sys.executable,'-B','-m','unittest','discover','-s',str(shared/'scripts'),'-p','test_*.py']),
        ('final-documentation', [sys.executable,'-m','sphinx','-E','-a','-W','--keep-going','-q','-b','html','docs','docs/_build/html']),
        ('final-traceability', [sys.executable,str(shared/'scripts/validate_traceability.py'),'docs/_build/html/needs.json','--version','0.2','--repo-root',str(ROOT),'--require-test-coverage','--csv',str(record/'allocation-traces.csv'),'--test-csv',str(record/'test-execution-traces.csv')]),
        ('final-published-diagrams', [sys.executable,str(shared/'scripts/normalize-diagram-links.py'),'--diagram-dir','docs/architecture/diagrams','--published-dir','docs/_build/html']),
    ]
    attempts = []
    for name, command in commands:
        started = datetime.now(timezone.utc).isoformat()
        with (record/(name+'.log')).open('w',encoding='utf-8') as stream:
            result = subprocess.run(command,cwd=ROOT,stdout=stream,stderr=subprocess.STDOUT,text=True)
        attempts.append(dict(suite=name,command=command,started=started,
                             finished=datetime.now(timezone.utc).isoformat(),returncode=result.returncode,log=name+'.log'))
        print(f'{name}: {result.returncode}',flush=True)
    results = json.loads((record/'results.json').read_text(encoding='utf-8'))
    source_hashes = json.loads((record/'source-hashes.json').read_text(encoding='utf-8'))
    changed = [name for name, expected in source_hashes.items() if sha(ROOT/name) != expected]
    publication_changes = []
    disposition_file = record/'verification-disposition.json'
    if disposition_file.exists():
        dispositions = json.loads(disposition_file.read_text(encoding='utf-8'))
        for item in dispositions['files']:
            name = item['path']
            before_path = record/item['before_snapshot']
            before = before_path.read_text(encoding='utf-8')
            after = (ROOT/name).read_text(encoding='utf-8')
            normalize = lambda value: re.sub(r'^   :verification_state:.*$', '', value, flags=re.M)
            if (name in changed and sha(before_path) == source_hashes[name]
                    and sha(ROOT/name) == item['after_sha256'] and normalize(before) == normalize(after)):
                publication_changes.append(name)
                changed.remove(name)
    needs = json.loads((ROOT/'docs/_build/html/needs.json').read_text(encoding='utf-8'))['versions']['0.2']['needs']
    cases = [need for need in needs.values() if need['type'] == 'test_case']
    counts = {result:sum(need.get('last_result') == result for need in cases)
              for result in ('not_run','passed','failed','error','skipped','blocked')}
    docs = {path.relative_to(ROOT).as_posix():sha(path) for path in sorted((ROOT/'docs').rglob('*'))
            if path.is_file() and '_build' not in path.parts and 'test-execution' not in path.parts and '__pycache__' not in path.parts}
    relevant_shared = [shared.parent.parent/'method.md', shared/'scripts/traceability_model.py',
                       shared/'scripts/validate_traceability.py']
    clean_suites = bool(results['cases']) and all(attempt['returncode'] == 0 for attempt in results['attempts'])
    document = dict(record=args.record,finished=datetime.now(timezone.utc).isoformat(),
                    source_revision=results['revision'],wheel_sha256=results['wheel_sha256'],
                    suites=results['outcomes'],final_gates=attempts,changed_candidate_inputs=changed,
                    verification_metadata_publication_changes=publication_changes,
                    latest_case_results=counts,documentation_sha256=docs,
                    shared_sha256={str(path):sha(path) for path in relevant_shared},
                    regression_and_method_gates_passed=clean_suites and not changed and all(a['returncode'] == 0 for a in attempts),
                    known_issue='STV_PR_006 remains analyzed: nested-Windows detail paths are not fixed or fully qualified by this documentation migration',
                    release_ready=False,
                    readiness_reason='Known unresolved in-scope detail-loading problem STV_PR_006; no new product release approval or publication is claimed')
    output.write_text(json.dumps(document,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:document[key] for key in ('suites','latest_case_results','regression_and_method_gates_passed','release_ready')},indent=2))
    return int(not document['regression_and_method_gates_passed'])


if __name__ == '__main__':
    raise SystemExit(main())
