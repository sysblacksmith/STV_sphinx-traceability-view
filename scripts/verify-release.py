"""Retain one complete, non-overwriting candidate verification execution."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]


def stamp():return datetime.now(timezone.utc).isoformat()


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def candidate_sources():
    files=[]
    for directory in ('src','frontend/src','docs/test-scripts','scripts'):
        files.extend(path for path in (ROOT/directory).rglob('*') if path.is_file() and '__pycache__' not in path.parts and not path.is_symlink())
    files.extend(ROOT/name for name in ('pyproject.toml','conftest.py','hatch_build.py','frontend/package.json','frontend/package-lock.json'))
    files.extend(ROOT/'docs'/name for name in ('requirements-stakeholder.rst','requirements-system.rst','requirements-software.rst','internal-interfaces.rst','implementation-plan.rst','verification-plan.rst'))
    files.extend((ROOT/'docs/architecture/decisions').glob('*.rst'))
    return {path.relative_to(ROOT).as_posix():sha(path) for path in sorted(set(files))}


def junit_cases(path):
    if not path.is_file():return []
    return [{'test':case.get('classname','')+'::'+case.get('name',''),
             'outcome':'failed' if case.find('failure') is not None else 'error' if case.find('error') is not None else 'skipped' if case.find('skipped') is not None else 'passed',
             'requirements':next(([identity for identity in prop.get('value','').split(',') if identity] for prop in case.findall('./properties/property') if prop.get('name')=='requirement_ids'),[])}
            for case in ET.parse(path).findall('.//testcase')]


def main():
    parser=argparse.ArgumentParser()
    version=re.search(r'^version = "([^"]+)"', (ROOT/'pyproject.toml').read_text(encoding='utf-8'), re.M)[1]
    parser.add_argument('--record',default=version+'-candidate-1')
    parser.add_argument('--driver',required=True,type=Path)
    parser.add_argument('--reuse-capacity-from',help='Reuse an unchanged, verified host fixture; browser capacity tests still run')
    args=parser.parse_args()
    if Path(args.record).name!=args.record:parser.error('record must be a directory name')
    if args.reuse_capacity_from and Path(args.reuse_capacity_from).name!=args.reuse_capacity_from:
        parser.error('reuse-capacity-from must be a record directory name')
    record=ROOT/'docs/test-execution'/args.record
    if record.exists():parser.error('record already exists; use a new candidate name to retain previous evidence')
    record.mkdir(parents=True)
    started=stamp();attempts=[]
    (record/'index.rst').write_text(f'{args.record} execution\n'+('='*(len(args.record)+10))+'\n\nExecution is running; no release result is claimed yet.\n',encoding='utf-8')
    index=record.parent/'index.rst'
    existing=index.read_text(encoding='utf-8') if index.exists() else 'Release test executions\n=======================\n\nHistorical candidate results; no deployment or release approval is implied.\n\n.. toctree::\n   :maxdepth: 2\n\n'
    index.write_text(existing+'   '+args.record+'/index\n',encoding='utf-8')
    wheel=ROOT/'dist'/f'sphinx_traceability_view-{version}-py3-none-any.whl'
    shared=Path(os.environ.get('REQUIREMENTS_SKILL_DIR',ROOT.parent/'-agents/skills/reverse-engineer-requirements'))
    env=dict(os.environ,STV_WHEEL=str(wheel),STV_GECKODRIVER=str(args.driver.resolve()),STV_SCREENSHOTS=str(record/'screenshots'),
             STV_CAPACITY_OUTPUT=str(ROOT/'docs/_build/release-benchmark'/args.record/'html'),
             STV_CAPACITY_METRICS=str(record/'capacity-browser.json'),STV_CONSUMER_RECORD=str(record/'consumer'))

    def run(name,command,cwd=ROOT,report=None):
        entry={'suite':name,'command':command,'cwd':str(cwd),'started':stamp(),'log':name+'.log'}
        print(f'{entry["started"]} {name}',flush=True)
        with (record/entry['log']).open('w',encoding='utf-8') as stream:
            result=subprocess.run(command,cwd=cwd,env=env,stdout=stream,stderr=subprocess.STDOUT,text=True)
        entry.update(finished=stamp(),returncode=result.returncode)
        if report:entry['report']=report
        attempts.append(entry)
        (record/'commands.json').write_text(json.dumps(attempts,indent=2),encoding='utf-8')
        print(f'{name}: exit {result.returncode}',flush=True)
        return result.returncode

    if run('browser-assets',['node','build.js'],ROOT/'frontend') or run('python-package',[sys.executable,'-m','build','--no-isolation']):
        (record/'index.rst').write_text(f'{args.record} execution\n'+('='*(len(args.record)+10))+'\n\nCandidate preparation failed; see commands.json and retained logs.\n',encoding='utf-8')
        return 2
    if not wheel.is_file():return 2
    sources=candidate_sources()
    source_identity=hashlib.sha256(json.dumps(sources,sort_keys=True).encode()).hexdigest()
    (record/'source-hashes.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
    artifact_dir=record/'artifacts';artifact_dir.mkdir()
    shutil.copyfile(wheel,artifact_dir/wheel.name)
    versions=subprocess.run([sys.executable,'-m','pip','freeze'],capture_output=True,text=True,check=True).stdout
    (record/'environment.txt').write_text(versions,encoding='utf-8')
    lock={p.name:sha(p) for p in (ROOT/'docs/_build/wheelhouse').glob('*.whl') if not p.name.startswith('sphinx_traceability_view-')}
    (record/'runtime-wheel-hashes.json').write_text(json.dumps(lock,indent=2),encoding='utf-8')
    metadata={'started':started,'revision':subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,capture_output=True,text=True,check=True).stdout.strip(),
              'dirty_worktree':subprocess.run(['git','status','--short'],cwd=ROOT,capture_output=True,text=True,check=True).stdout,
              'source_identity':source_identity,'wheel':wheel.name,'wheel_sha256':sha(wheel),'python':sys.version,
              'platform':platform.platform(),'host':platform.node(),'machine':platform.machine(),'processor':platform.processor(),'logical_cpus':os.cpu_count(),
              'node':subprocess.run(['node','--version'],capture_output=True,text=True,check=True).stdout.strip(),
              'driver':str(args.driver.resolve()),'driver_version':subprocess.run([str(args.driver.resolve()),'--version'],capture_output=True,text=True,check=True).stdout.splitlines()[0],
              'browser':'C:/Program Files/Mozilla Firefox/firefox.exe','offline_policy':'External HTTP/HTTPS proxy points at closed loopback port; local static HTTP bypasses proxy',
              'browser_mode':'Headless automation of the installed stable desktop Firefox binary',
              'benchmark_output':env['STV_CAPACITY_OUTPUT']}
    (record/'candidate.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    run('coverage',[sys.executable,'scripts/check-coverage.py','--strict'])
    run('diagram-links-source',[sys.executable,str(shared/'scripts/normalize-diagram-links.py'),'--diagram-dir','docs/architecture/diagrams'])
    run('documentation',[sys.executable,'-m','sphinx','-b','html','-W','--keep-going','docs','docs/_build/html'])
    benchmark_dir=ROOT/'docs/_build/release-benchmark'/args.record
    if args.reuse_capacity_from:
        previous=record.parent/args.reuse_capacity_from
        previous_metadata=json.loads((previous/'candidate.json').read_text(encoding='utf-8'))
        previous_sources=json.loads((previous/'source-hashes.json').read_text(encoding='utf-8'))
        metrics=json.loads((previous/'capacity-build.json').read_text(encoding='utf-8'))
        output=Path(previous_metadata['benchmark_output']).resolve()
        relevant=[name for name in sources if name.startswith('src/') or name in (
            'scripts/benchmark.py','docs/test-scripts/fixtures/minimal/conf.py','frontend/package-lock.json')]
        proof={'source_record':args.reuse_capacity_from,'output':str(output),
               'current_wheel_sha256':sha(wheel),'previous_wheel_sha256':previous_metadata['wheel_sha256'],
               'changed_fixture_inputs':[name for name in relevant if previous_sources.get(name)!=sources[name]]}
        proof['valid']=(proof['current_wheel_sha256']==proof['previous_wheel_sha256']
            and not proof['changed_fixture_inputs'] and previous_metadata['python']==sys.version
            and lock==json.loads((previous/'runtime-wheel-hashes.json').read_text(encoding='utf-8'))
            and metrics.get('returncode')==0 and metrics.get('needs')==30000
            and metrics.get('authored_edges')==90000 and metrics.get('fixture_version')==1
            and output.is_relative_to((ROOT/'docs/_build/release-benchmark').resolve())
            and (output/'index.html').is_file()
            and sha(output/'_static/stv/stv.js')==sha(ROOT/'src/sphinx_traceability_view/static/stv.js'))
        (record/'capacity-reuse.json').write_text(json.dumps(proof,indent=2),encoding='utf-8')
        (record/'capacity-fixture-reuse.log').write_text(json.dumps(proof,indent=2),encoding='utf-8')
        attempts.append({'suite':'capacity-fixture-reuse','returncode':0 if proof['valid'] else 1,
                         'log':'capacity-fixture-reuse.log','source_record':args.reuse_capacity_from})
        if not proof['valid']:
            (record/'index.rst').write_text(f'{args.record} execution\n'+('='*(len(args.record)+10))+
                '\n\nFixture reuse rejected; see capacity-reuse.json. No release pass is claimed.\n',encoding='utf-8')
            return 2
        env['STV_CAPACITY_OUTPUT']=str(output)
        metadata['benchmark_output']=str(output)
        metadata['capacity_fixture_reused_from']=args.reuse_capacity_from
        metrics['reused_from']=args.reuse_capacity_from
        (record/'capacity-build.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
        shutil.copyfile(previous/'capacity-host.log',record/'capacity-host.log')
    else:
        run('capacity-build',[sys.executable,'scripts/benchmark.py','--directory',str(benchmark_dir)])
        if (benchmark_dir/'metrics.json').is_file():
            shutil.copyfile(benchmark_dir/'metrics.json',record/'capacity-build.json')
            shutil.copyfile(benchmark_dir/'build.log',record/'capacity-host.log')
    # Fixture reuse changes the actual benchmark path; retain it in both records.
    (record/'candidate.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    run('pytest',[sys.executable,'-m','pytest','-q','--junitxml='+str(record/'pytest.xml'),'--requirement-map='+str(record/'test-map.json')],report='pytest.xml')
    run('node-tests',['node','--test','--test-reporter=junit','frontend/src/*/tests/*.test.js'],report='node-tests.log')
    shutil.copyfile(record/'node-tests.log',record/'node.xml')
    run('traceability',[sys.executable,str(shared/'scripts/validate_traceability.py'),'docs/_build/html/needs.json','--version','.'.join(version.split('.')[:2]),'--repo-root',str(ROOT),'--csv',str(record/'traceability.csv')])
    run('diagram-links-published',[sys.executable,str(shared/'scripts/normalize-diagram-links.py'),'--diagram-dir','docs/architecture/diagrams','--published-dir','docs/_build/html'])
    cases=junit_cases(record/'pytest.xml')+junit_cases(record/'node.xml')
    for case in cases:
        if not case['requirements']:case['requirements']=__import__('re').findall(r'STV_(?:SYS|SWR)_\d+',case['test'])
    changed={name for name,value in candidate_sources().items() if sources.get(name)!=value}
    if changed:attempts.append({'suite':'candidate-source-stability','returncode':1,'changed':sorted(changed)})
    outcomes={state:sum(case['outcome']==state for case in cases) for state in ('passed','failed','error','skipped')}
    metadata.update(finished=stamp(),outcomes=outcomes,attempts=attempts,cases=cases)
    (record/'results.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    passed=all(entry['returncode']==0 for entry in attempts) and cases and not any(outcomes[state] for state in ('failed','error','skipped'))
    lines=[f'{args.record} execution','='*(len(args.record)+10),'',
           f'Execution: {started} to {metadata["finished"]} (UTC).',
           f'Outcome: **{"required executable suites passed" if passed else "candidate has unresolved verification failures"}**.','',
           f'Input Git revision: ``{metadata["revision"]}``; dirty source/test identity:',
           f'``{source_identity}``. Full file hashes and dirty-worktree state are retained below.',
           f'Wheel SHA-256: ``{metadata["wheel_sha256"]}``. Python {platform.python_version()}; {platform.platform()}; Node {metadata["node"]}.',
           'Firefox and geckodriver versions are retained in the browser metrics and candidate metadata.',
           'This records execution, not owner release approval, deployment, licensing or agreed performance budgets.','',
           f'Test totals: {outcomes["passed"]} passed; {outcomes["failed"]} failed; {outcomes["error"]} errors; {outcomes["skipped"]} skipped.','',
           'Suite results','-------------','', '.. list-table:: Commands and outcomes','   :header-rows: 1','','   * - Suite','     - Exit','     - Retained log']
    for entry in attempts:
        lines+=['   * - '+entry['suite'],'     - '+str(entry['returncode']),'     - '+(':download:`'+entry['log']+' <'+entry['log']+'>`' if 'log' in entry else 'See results.json')]
    lines+=['','Requirement execution results','-----------------------------','','.. list-table:: Per-case result and mapped criteria','   :header-rows: 1','   :widths: 55 10 35','','   * - Executable case','     - Outcome','     - Requirement criteria exercised']
    for case in cases:
        lines+=['   * - ``'+case['test']+'``','     - '+case['outcome'],'     - '+(', '.join(':need:`'+identity+'`' for identity in case['requirements']) or 'Publication/build infrastructure')]
    lines+=['','Retained evidence','-----------------','']
    for name in ('candidate.json','source-hashes.json','commands.json','environment.txt','runtime-wheel-hashes.json','test-map.json','pytest.xml','node.xml','results.json','capacity-build.json','capacity-reuse.json','capacity-browser.json','capacity-host.log','traceability.csv'):
        if (record/name).exists():lines+=['* :download:`'+name+' <'+name+'>`']
    lines+=['* :download:`Tested wheel <artifacts/'+wheel.name+'>`','','Browser screenshots','-------------------','']
    for path in sorted((record/'consumer').glob('*')):
        relative=path.relative_to(record).as_posix();lines+=['* :download:`'+relative+' <'+relative+'>`']
    for path in sorted((record/'screenshots').glob('*.png')):lines+=['* :download:`'+path.name+' <screenshots/'+path.name+'>`']
    (record/'index.rst').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'Record: {record}; passed={bool(passed)}; totals={outcomes}',flush=True)
    return 0 if passed else 1


if __name__=='__main__':raise SystemExit(main())
