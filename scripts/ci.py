"""Read-only CI validation and checksummed development artifacts; never publishes."""
import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]


def run(command,cwd=ROOT,env=None):
    subprocess.run(command,cwd=cwd,env=env,check=True)


def write_checksums(directory):
    directory=Path(directory)
    wheels=list(directory.glob('*.whl'));sources=list(directory.glob('*.tar.gz'))
    files=sorted(wheels+sources)
    if len(wheels)!=1 or len(sources)!=1:raise ValueError('Expected exactly one wheel and one source archive')
    (directory/'SHA256SUMS').write_bytes(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files).encode('utf-8'))
    metadata={'source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
              'dirty_worktree':bool(subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True).strip()),
              'run_id':os.environ.get('GITHUB_RUN_ID'),'run_attempt':os.environ.get('GITHUB_RUN_ATTEMPT'),
              'repository':os.environ.get('GITHUB_REPOSITORY'),'python':sys.version,
              'qualification':'development checks only; no release approval, capacity/browser qualification or publication'}
    (directory/'build-info.json').write_text(json.dumps(metadata,indent=2)+'\n',encoding='utf-8')


def validate():
    import tomllib  # Maintainer CI uses Python 3.11+; runtime subcommand supports 3.10.
    base=ROOT/'docs/_build/ci';reports=base/'reports';reports.mkdir(parents=True,exist_ok=True)
    distributions=base/'distributions'
    run([sys.executable,'scripts/check-workflows.py'])
    run(['npm.cmd' if os.name=='nt' else 'npm','ci'],ROOT/'frontend')
    run(['node','build.js'],ROOT/'frontend')
    run(['git','diff','--exit-code','--','src/sphinx_traceability_view/static'])
    run(['node','--test','--test-reporter=junit','--test-reporter-destination='+str(reports/'node.xml'),'src/*/tests/*.test.js'],ROOT/'frontend')
    run([sys.executable,'-m','build','--no-isolation','--outdir',str(distributions)])
    config=tomllib.loads((ROOT/'pyproject.toml').read_text(encoding='utf-8'))
    run([sys.executable,'-m','pip','download','--only-binary=:all:','--dest',str(ROOT/'docs/_build/wheelhouse'),
         '-r','requirements-tooling.txt',*config['project']['dependencies']])
    wheels=list(distributions.glob('*.whl'))
    if len(wheels)!=1:raise ValueError('CI requires a fresh dist directory with exactly one wheel')
    env=dict(os.environ,STV_WHEEL=str(wheels[0]),STV_CONSUMER_RECORD=str(reports/'consumer'))
    run([sys.executable,'-m','pytest','-m','not browser','--ignore=docs/test-scripts/test_capacity.py',
         '--junitxml='+str(reports/'pytest.xml'),'-q'],env=env)
    run([sys.executable,'scripts/check-coverage.py','--strict'])
    run([sys.executable,'scripts/check-method-package.py'])
    run([sys.executable,'-m','sphinx','-E','-a','-W','--keep-going','-b','html','docs','docs/_build/html'])
    from runpy import run_path
    version=run_path(str(ROOT/'src/sphinx_traceability_view/_version.py'))['__version__']
    run([sys.executable,'tools/method/tooling/validate_traceability.py','docs/_build/html/needs.json',
         '--version','.'.join(version.split('.')[:2]),'--repo-root',str(ROOT),'--require-test-coverage',
         '--csv',str(reports/'traceability.csv'),'--test-csv',str(reports/'test-traceability.csv')])
    run([sys.executable,'tools/method/tooling/normalize-diagram-links.py',
         '--diagram-dir','docs/architecture/diagrams','--published-dir','docs/_build/html'])
    run([sys.executable,'scripts/check-method-package.py','--published','docs/_build/html'])
    write_checksums(distributions)
    frozen=subprocess.check_output([sys.executable,'-m','pip','freeze'],text=True)
    (reports/'environment.txt').write_text(frozen,encoding='utf-8')


def runtime():
    import sphinx_traceability_view as stv
    location=Path(stv.__file__).resolve()
    if location.is_relative_to(ROOT/'src'):raise ValueError('Runtime check must import the installed package')
    assert stv.__version__==importlib.metadata.version('sphinx-traceability-view')
    run([sys.executable,'-m','pip','check'])
    env=dict(os.environ);env.pop('PYTHONPATH',None)
    run([sys.executable,'-m','sphinx','-W','-b','html',str(ROOT/'docs/test-scripts/fixtures/minimal'),
         str(ROOT/'docs/_build/ci-runtime')],env=env)
    print('Installed runtime:',location,stv.__version__)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('command',choices=['validate','runtime','checksums']);args=parser.parse_args()
    if args.command=='validate':validate()
    elif args.command=='runtime':runtime()
    else:write_checksums(ROOT/'docs/_build/ci/distributions')


if __name__=='__main__':main()

