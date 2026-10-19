"""Reproduce the initial method migration from existing executable metadata.

Run once before new execution records are linked; refuses to overwrite cases.
"""
import ast
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT/'docs/test-cases'


def digest(value):
    return hashlib.sha256(value.encode()).hexdigest()[:12].upper()


def main():
    if TARGET.exists():
        raise SystemExit('Test-case sources already exist; preserve their history.')
    TARGET.mkdir()
    requirements = {}
    for name in ('stakeholder', 'system', 'software'):
        text = (ROOT/f'docs/{name}.rst').read_text(encoding='utf-8')
        for block in re.split(r'\n(?=\.\. (?:shr|sysr|swr)::)', '\n'+text):
            match = re.search(r':id: (STV_(?:SHR|SYS|SWR)_\d+)', block)
            if match:
                requirements[match[1]] = block
    cases = json.loads((ROOT/'docs/_build/test-map.json').read_text(encoding='utf-8'))
    for source in sorted((ROOT/'frontend/test').glob('*.test.js')):
        for match in re.finditer(r"test\('([^']+)'", source.read_text(encoding='utf-8')):
            cases.append(dict(test=source.relative_to(ROOT).as_posix()+' :: '+match[1],
                              requirements=re.findall(r'STV_(?:SYS|SWR)_\d+', match[1])))
    registry = []
    # These are criterion mappings, not automatic ancestry-based pass claims.
    stakeholder = {i: [i] for i in range(1, 47)}
    stakeholder.update({47: [15,17], 48: [14,26,47,48], 49: [15], 50: [15],
                        51: [47], 52: [47], 53: [50], 54: [49], 55: [51],
                        56: [52], 57: [53]})
    for case in cases:
        identity = 'STV_TC_'+digest(case['test'])
        linked = set(case['requirements'])
        for requirement in case['requirements']:
            if requirement.startswith('STV_SWR_'):
                linked.update(f'STV_SHR_{i:03}' for i in stakeholder[int(requirement[-3:])])
        if any(x in case['test'] for x in ('cross_page_bundle', 'seed_capacity', 'seed_selection_release')):
            linked.add('STV_SHR_048')
        source_name = case['test'].split(' :: ')[0].split('::')[0]
        source = ROOT/source_name
        text = source.read_text(encoding='utf-8')
        if source.suffix == '.py':
            function_name = case['test'].split('::')[1].split('[')[0]
            function = next(node for node in ast.walk(ast.parse(text)) if isinstance(node, ast.FunctionDef) and node.name == function_name)
            procedure = ast.get_source_segment(text, function)
            title = function_name.removeprefix('test_').replace('_', ' ')
            level = 'Browser/system' if 'browser' in text[:text.find('def '+function_name)] and source.name in ('test_browser.py','test_capacity.py','test_release_seeds.py') else 'Unit/host integration'
            command = f'.venv-implementation/Scripts/python.exe -m pytest "{case["test"]}" -q'
        else:
            name = case['test'].split(' :: ')[1]
            start = text.index("test('"+name+"'")
            next_test = text.find("test('", start+6)
            procedure = text[start:next_test if next_test >= 0 else len(text)].strip()
            title = name.split(': ',1)[-1]
            level = 'JavaScript unit/state/geometry'
            command = f'node --test "{source_name}" (select the named subtest in the report)'
        if not linked:
            # The documentation-visuals case checks this actual published site.
            linked.update(['STV_SYS_003','STV_SHR_017','STV_SHR_018'])
        linked &= requirements.keys()
        lines = [title, '='*len(title), '', '.. test_case:: '+title,
                 '   :id: '+identity, '   :status: draft', '   :tags: release_initial',
                 '   :basis: documented', '   :evidence: '+source_name+' :: '+case['test'],
                 '   :priority: unassigned', '   :verification_state: not_assessed',
                 '   :verifies: '+', '.join(sorted(linked)), '   :last_result: not_run', '',
                 '   **Level:** '+level+'.', '',
                 '   **Preconditions and inputs:** Use the pinned implementation environment,',
                 '   fixture setup and parameter variant identified by the executable selector.',
                 '   Browser cases require provisioned Firefox/geckodriver and both file/HTTP',
                 '   variants where parameterized. Capacity cases require a freshly generated',
                 '   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and',
                 '   offline wheelhouse. The procedure below specifies test-specific inputs.', '',
                 '   **Executable selector:** ``'+case['test']+'``.', '',
                 '   **Invocation:** ``'+command+'``.', '',
                 '   **Procedure and expected outcomes:** Execute the following existing test',
                 '   procedure with its fixture helpers. Every assertion is a required observable',
                 '   outcome; expected error cases must assert the specified diagnostic/state.',
                 '   Links identify criterion portions exercised by this case, not a claim that',
                 '   this individual case alone verifies every linked requirement in full.',
                 '   Review the full case set and the release criterion assessment together.', '',
                 '   .. code-block:: '+('python' if source.suffix == '.py' else 'javascript'), '']
        lines += ['      '+line if line else '' for line in procedure.splitlines()]
        lines += ['', '   **Evidence to retain:** Per-case execution result and timestamp, candidate',
                  '   and test identities, environment, invocation and linked JUnit/log evidence.', '']
        (TARGET/(identity+'.rst')).write_text('\n'.join(lines), encoding='utf-8')
        registry.append(dict(id=identity, selector=case['test'], requirements=sorted(linked)))
    deferred = {
        19: ('Select separate occurrences', 'Open a two-parent graph sharing one child. Select separate-occurrence mode, then shared mode.', 'Separate mode shows two child occurrences; shared mode shows one. The selector and visible mode agree.'),
        21: ('Restore occurrence exploration', 'In separate mode expand different groups in each occurrence. Switch to shared mode and back.', 'Each occurrence recovers its own expanded and collapsed groups without losing prior exploration.'),
        22: ('Isolate occurrence expansion', 'In separate mode show two occurrences of one child through different parents. Expand a group on only the first.', 'Only the first occurrence changes; the other retains its original graph and expansion state.'),
        23: ('Merge shared expansion sets', 'In separate mode expand disjoint groups on two copies. Switch to shared mode.', 'One shared object remains with the union of both expanded groups and no duplicate canonical edges.'),
    }
    for number, (title, steps, expected) in deferred.items():
        identity = f'STV_TC_OCC_{number:03}'
        linked = [f'STV_SHR_{number:03}', f'STV_SWR_{number:03}']
        lines = [title, '='*len(title), '', '.. test_case:: '+title,
                 '   :id: '+identity, '   :status: draft', '   :tags: release_later',
                 '   :basis: documented', '   :evidence: docs/stakeholder.rst; docs/software.rst',
                 '   :priority: unassigned', '   :verification_state: not_assessed',
                 '   :verifies: '+', '.join(linked), '   :last_result: not_run', '',
                 '   **Level/environment:** Planned browser acceptance, Windows/Firefox,',
                 '   file and nested static HTTP output, network blocked.', '',
                 '   **Preconditions/inputs:** Future occurrence-mode implementation; two',
                 '   parents sharing one child with two disjoint nonempty relationship groups.', '',
                 '   **Procedure:** '+steps, '', '   **Expected outcomes:** '+expected, '',
                 '   Repeat with a cycle and a missing target to verify termination and visible',
                 '   placeholder identity. Start at 199 visible occurrences and request two more:',
                 '   the transition must be rejected atomically with the node-limit explanation.',
                 '   A transition to exactly 200 succeeds. Attempt a mode switch producing 201:',
                 '   retain mode, graph and exploration state and explain the limit.', '',
                 '   **Execution/evidence:** No executable implementation exists in v0.2.0.',
                 '   Retain per-case results, candidate identity and file/HTTP screenshots when',
                 '   the future release implements this scope; no execution record is invented.', '']
        (TARGET/(identity+'.rst')).write_text('\n'.join(lines), encoding='utf-8')
        registry.append(dict(id=identity, selector=None, requirements=linked))
    index = ['Test-case specification', '=======================', '',
             'Canonical cases link executable procedures and planned acceptance checks to',
             'requirements. Review status, latest result and requirement verification are',
             'independent. Existing release evidence is preserved without retroactive runs.', '',
             '.. needtable::', "   :filter: type == 'test_case'",
             '   :columns: id;title;status;verifies;last_result;executed_by', '',
             '.. toctree::', '   :maxdepth: 1', '   :glob:', '', '   STV_TC_*', '']
    (TARGET/'index.rst').write_text('\n'.join(index), encoding='utf-8')
    (ROOT/'docs/concept-reviews/round-7-test-map.json').write_text(json.dumps(registry,indent=2)+'\n',encoding='utf-8')
    covered = {r for case in registry for r in case['requirements']}
    print(f'{len(registry)} modeled cases; uncovered requirements: {sorted(requirements.keys()-covered)}')


if __name__ == '__main__':
    main()
