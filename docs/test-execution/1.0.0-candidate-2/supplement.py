"""Retain exact release archives and independently exercise the minimum runtime."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
commands = []

def run(name, args, cwd=ROOT, env=None):
    entry = dict(suite=name, command=list(map(str, args)), started=datetime.now(timezone.utc).isoformat())
    result = subprocess.run(entry['command'], cwd=cwd, env=env, text=True, capture_output=True)
    (RECORD/(name+'.log')).write_text(result.stdout+result.stderr, encoding='utf-8')
    entry.update(returncode=result.returncode, finished=datetime.now(timezone.utc).isoformat())
    commands.append(entry)
    (RECORD/'supplement-commands.json').write_text(json.dumps(commands, indent=2), encoding='utf-8')
    assert result.returncode == 0, name+': '+result.stderr[-2000:]
    print(name+': passed', flush=True)

artifacts = RECORD/'artifacts'
for name in ('sphinx_traceability_view-1.0.0-py3-none-any.whl', 'sphinx_traceability_view-1.0.0.tar.gz'):
    source = ROOT/'dist'/name
    destination = artifacts/name
    if destination.exists():
        assert destination.read_bytes() == source.read_bytes()
    else:
        shutil.copyfile(source, destination)
files = sorted(artifacts.iterdir())
(RECORD/'SHA256SUMS.txt').write_bytes(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in files).encode())
with tarfile.open(artifacts/'sphinx_traceability_view-1.0.0.tar.gz') as archive:
    names = [m.name for m in archive.getmembers() if m.isfile()]
    assert not any('/docs/test-execution/' in n or n.endswith('.log') for n in names)
    (RECORD/'sdist-members.json').write_text(json.dumps(names, indent=2), encoding='utf-8')
with zipfile.ZipFile(artifacts/'sphinx_traceability_view-1.0.0-py3-none-any.whl') as archive:
    names = archive.namelist()
    assert not any('/tests/' in n for n in names)
    assert any(n.endswith('/vendor/ELK-INVENTORY.json') for n in names)
    (RECORD/'wheel-members.json').write_text(json.dumps(names, indent=2), encoding='utf-8')

environment = ROOT/'docs/_build/release-runtime310'
run('runtime310-venv', [r'C:/Users/fragg/AppData/Local/Programs/Python/Python310/python.exe', '-m', 'venv', environment])
python = environment/'Scripts/python.exe'
run('runtime310-tools', [python, '-m', 'pip', 'install', '--no-index', '--find-links', ROOT/'docs/_build/wheelhouse', '-r', ROOT/'requirements-tooling.txt'])
run('runtime310-install', [python, '-m', 'pip', 'install', '--no-index', '--find-links', ROOT/'docs/_build/wheelhouse', artifacts/'sphinx_traceability_view-1.0.0-py3-none-any.whl'])
env = dict(os.environ)
env.pop('PYTHONPATH', None)
env['PATH'] = str(environment/'Scripts')+os.pathsep+str(Path(os.environ['SystemRoot'])/'System32')
run('runtime310-host', [python, ROOT/'scripts/ci.py', 'runtime'], cwd=environment, env=env)
run('runtime310-identity', [python, '-c', 'import sys,importlib.metadata as m,sphinx_traceability_view as s;assert sys.version_info[:2]==(3,10);assert s.__version__==m.version("sphinx-traceability-view")=="1.0.0";print(sys.version);print(s.__file__);print(s.__version__)'], cwd=environment, env=env)
