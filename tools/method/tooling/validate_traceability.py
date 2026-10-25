"""Validate a Sphinx-Needs JSON export against the small recovery model."""
import argparse
from collections import Counter, defaultdict
from datetime import datetime
import csv
import json
from pathlib import Path
import sys

from traceability_model import NEEDS_STATUSES_BY_TYPE, TEST_RESULTS

ALLOWED = {
    'verifies': {('test_case', kind) for kind in ('shr', 'sysr', 'swr')},
    'executed_by': {('test_case', 'test_execution')},
    'derives_from': {('sysr', 'shr'), ('swr', 'sysr'), ('swr', 'shr')},
    'allocated_to': {('sysr', 'syse'), ('swr', 'swe')},
    'part_of': {('swe', 'syse')},
}


def validate(needs, require_test_coverage=False):
    errors = []
    incoming = {link: defaultdict(set) for link in ALLOWED}
    required = {
        'problem_report': (),
        'change_request': (),
        'test_case': ('verifies',),
        'test_execution': ('executed_by_back',),
        'shr': ('derives_from_back',),
        'sysr': ('derives_from', 'derives_from_back', 'allocated_to'),
        'swr': ('derives_from', 'allocated_to'),
        'syse': (),
        'swe': ('allocated_to_back', 'part_of'),
    }
    for ident, need in needs.items():
        kind = need.get('type')
        if kind not in required:
            errors.append(f'{ident}: unsupported type {kind}')
            continue
        if need.get('id') != ident:
            errors.append(f'{ident}: ID differs from JSON key')
        for field in ('title', 'status', 'basis', 'evidence', 'priority', 'verification_state'):
            if not need.get(field):
                errors.append(f'{ident}: missing {field}')
        if need.get('basis') not in ('observed', 'documented', 'owner', 'inferred'):
            errors.append(f'{ident}: invalid basis')
        if need.get('status') not in NEEDS_STATUSES_BY_TYPE[kind]:
            errors.append(f'{ident}: invalid status')
        if need.get('priority') not in ('unassigned', 'high', 'medium', 'low'):
            errors.append(f'{ident}: invalid priority')
        if need.get('verification_state') not in ('not_assessed', 'passed', 'failed', 'partial'):
            errors.append(f'{ident}: invalid verification state')
        if kind in ('shr', 'sysr', 'swr') and 'Acceptance criterion' not in need.get('content', ''):
            errors.append(f'{ident}: missing acceptance criterion')
        if kind == 'test_case' and need.get('last_result') not in TEST_RESULTS:
            errors.append(f'{ident}: invalid or missing last_result')
        if kind == 'test_execution':
            if need.get('result') not in TEST_RESULTS[1:]:
                errors.append(f'{ident}: invalid or missing execution result')
            try:
                date = datetime.fromisoformat(need.get('executed_at', '').replace('Z', '+00:00'))
                if date.tzinfo is None:
                    raise ValueError('timezone required')
            except (ValueError, TypeError):
                errors.append(f'{ident}: executed_at must be an ISO timestamp with timezone')
        if need.get('links'):
            errors.append(f'{ident}: untyped default links are outside this model')
        for link, types in ALLOWED.items():
            targets = need.get(link, [])
            if not isinstance(targets, list):
                errors.append(f'{ident}: {link} must be a list')
                continue
            if len(targets) != len(set(targets)):
                errors.append(f'{ident}: duplicate {link} target')
            for target in targets:
                if target not in needs:
                    errors.append(f'{ident}: dangling {link} target {target}')
                    continue
                incoming[link][target].add(ident)
                if (kind, needs[target].get('type')) not in types:
                    errors.append(f'{ident}: illegal {link} target {target}')

    for ident, need in needs.items():
        for field in required.get(need.get('type'), ()):
            if not need.get(field):
                errors.append(f'{ident}: missing coverage/allocation {field}')
        for link in ALLOWED:
            if set(need.get(link + '_back', [])) != incoming[link][ident]:
                errors.append(f'{ident}: inconsistent generated inverse {link}_back')
        if require_test_coverage and need.get('type') in ('shr', 'sysr', 'swr') and not incoming['verifies'][ident]:
            errors.append(f'{ident}: missing test-case coverage')
        if need.get('type') == 'test_execution' and len(incoming['executed_by'][ident]) != 1:
            errors.append(f'{ident}: execution must belong to exactly one test case')
        if need.get('type') == 'test_case':
            records = [needs[target] for target in need.get('executed_by', [])
                       if target in needs and needs[target].get('type') == 'test_execution']
            if not records and need.get('last_result') != 'not_run':
                errors.append(f'{ident}: last_result requires linked execution evidence')
            if records:
                try:
                    dated = [(datetime.fromisoformat(record.get('executed_at', '').replace('Z', '+00:00')), record) for record in records]
                    latest_time = max(date for date, _ in dated)
                    latest = [record for date, record in dated if date == latest_time]
                    if len(latest) != 1:
                        errors.append(f'{ident}: latest execution timestamp is ambiguous')
                    elif need.get('last_result') != latest[0].get('result'):
                        errors.append(f'{ident}: last_result differs from latest execution')
                except (ValueError, TypeError):
                    pass  # Invalid execution timestamps are reported above.
        if need.get('type') == 'syse':
            if not need.get('allocated_to_back') and not any(
                needs.get(child, {}).get('allocated_to_back')
                for child in incoming['part_of'][ident]
            ):
                errors.append(f'{ident}: system element has no allocated requirements or allocated software children')
        if need.get('type') == 'swr':
            containers = {container for element in need.get('allocated_to', [])
                          for container in needs.get(element, {}).get('part_of', [])}
            for parent in need.get('derives_from', []):
                if needs.get(parent, {}).get('type') != 'sysr':
                    continue
                if not containers.intersection(needs.get(parent, {}).get('allocated_to', [])):
                    errors.append(f'{ident}: software allocation inconsistent with parent {parent}')
    counts = Counter(n.get('type') for n in needs.values())
    for kind in required:
        # A fully channeled scope legitimately has no system requirements.
        if kind in ('sysr', 'problem_report', 'change_request', 'test_case', 'test_execution'):
            continue
        if not counts[kind]:
            errors.append(f'No items of required type {kind}')
    return errors


def export_paths(needs, target):
    """One row per complete derivation/allocation path; no second source database."""
    with target.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(('stakeholder_requirement', 'system_requirement', 'software_requirement',
                         'system_element', 'software_element'))
        for swid, sw in sorted(needs.items()):
            if sw['type'] != 'swr':
                continue
            for sysid in sw['derives_from']:
                if needs[sysid]['type'] == 'shr':
                    for element in sw['allocated_to']:
                        for container in needs[element]['part_of']:
                            writer.writerow((sysid, '', swid, container, element))
                    continue
                for shrid in needs[sysid]['derives_from']:
                    for element in sw['allocated_to']:
                        for container in needs[element]['part_of']:
                            if container in needs[sysid]['allocated_to']:
                                writer.writerow((shrid, sysid, swid, container, element))


def export_test_paths(needs, target):
    """Export explicit requirement/case/attempt paths, including coverage gaps."""
    with target.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(('requirement', 'test_case', 'last_result', 'test_execution',
                         'result', 'executed_at', 'evidence'))
        for identity, requirement in sorted(needs.items()):
            if requirement.get('type') not in ('shr', 'sysr', 'swr'):
                continue
            cases = sorted(key for key, value in needs.items()
                           if value.get('type') == 'test_case' and identity in value.get('verifies', []))
            if not cases:
                writer.writerow((identity, '', '', '', '', '', ''))
            for case in cases:
                test = needs[case]
                records = test.get('executed_by', [])
                if not records:
                    writer.writerow((identity, case, test['last_result'], '', '', '', ''))
                for record in sorted(records):
                    run = needs[record]
                    writer.writerow((identity, case, test['last_result'], record,
                                     run['result'], run['executed_at'], run['evidence']))


def validate_evidence_paths(needs, repo_root):
    """Check referenced files exist without importing product code or reading secrets."""
    errors = []
    for ident, need in needs.items():
        for reference in need.get('evidence', '').split(';'):
            reference = reference.strip()
            if reference.startswith('owner:'):
                continue
            path = reference.split(' :: ', 1)[0].strip()
            candidate = Path(path)
            if candidate.is_absolute() or '..' in candidate.parts:
                errors.append(f'{ident}: evidence path must stay repository-relative: {path}')
            elif not path or not (repo_root / candidate).exists():
                errors.append(f'{ident}: evidence path does not exist: {path}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('needs_json', type=Path)
    parser.add_argument('--version', required=True)
    parser.add_argument('--require-test-coverage', action='store_true', help='Require an explicit test case for every exported requirement (release gate)')
    parser.add_argument('--test-csv', type=Path, help='Derived requirement/test/execution matrix')
    parser.add_argument('--csv', type=Path, help='Optional derived end-to-end trace matrix')
    parser.add_argument('--repo-root', type=Path, help='Also check repository-relative evidence files exist')
    args = parser.parse_args()
    try:
        document = json.loads(args.needs_json.read_text(encoding='utf-8'))
        needs = document['versions'][args.version]['needs']
        errors = validate(needs, require_test_coverage=args.require_test_coverage)
        if args.repo_root:
            errors.extend(validate_evidence_paths(needs, args.repo_root.resolve()))
        if errors:
            print('\n'.join(errors), file=sys.stderr)
            return 1
        if args.csv:
            export_paths(needs, args.csv)
        if args.test_csv:
            export_test_paths(needs, args.test_csv)
        print('Traceability valid: ' + ', '.join(f'{k}={v}' for k, v in sorted(Counter(n['type'] for n in needs.values()).items())))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'Cannot validate requirements export: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())

