"""Deterministic real-host capacity fixture; timings are measurements, not budgets."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--count',type=int,default=30000)
    parser.add_argument('--directory',type=Path,default=Path('docs/_build/benchmark'))
    args=parser.parse_args()
    directory=args.directory.resolve();source=directory/'source';output=directory/'html'
    source.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(Path(__file__).parents[1]/'docs/test-scripts/fixtures/minimal/conf.py',source/'conf.py')
    with (source/'conf.py').open('a',encoding='utf-8') as stream:
        stream.write('\nneeds_types.append({"directive":"check","title":"Test","prefix":"TC_","color":"#eeeeff","style":"node"})\ntraceability_view_model["types"]["check"]={"role":"test"}\n')
    # Fixed topology version 1: three forward modular edges, including wraparound
    # cycles. Shared type identities and long detail bodies are deterministic.
    with (source/'requirements.rst').open('w',encoding='utf-8') as stream:
        stream.write('Capacity fixture\n================\n\n')
        for i in range(args.count):
            targets='; '.join(f'BENCHMARK_LONG_IDENTIFIER_{(i+step)%args.count:05}' for step in (1,7,101))
            directive='check' if i%10==9 else 'shr'
            stream.write(f'.. {directive}:: Benchmark item {i}\n   :id: BENCHMARK_LONG_IDENTIFIER_{i:05}\n   :status: accepted\n   :traces: {targets}\n\n   '+('Deterministic rich detail text. '*12)+'\n\n')
    (source/'index.rst').write_text('Benchmark\n=========\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: BENCHMARK_LONG_IDENTIFIER_00000\n',encoding='utf-8')
    command=[sys.executable,'-m','sphinx','-b','html','-W',str(source),str(output)]
    start=time.perf_counter()
    env=dict(os.environ,PYTHONPATH=str(Path(__file__).parents[1]/'src'))
    with (directory/'build.log').open('w',encoding='utf-8') as log:
        result=subprocess.run(command,env=env,stdout=log,stderr=subprocess.STDOUT)
    duration=time.perf_counter()-start
    files=list(output.rglob('*'))
    metrics={'fixture_version':1,'needs':args.count,'authored_edges':args.count*3,
             'seconds':duration,'returncode':result.returncode,'command':command,
             'platform':platform.platform(),'python':platform.python_version(),
             'graph_bytes':sum(p.stat().st_size for p in output.glob('_static/stv/graph-*.js')),
             'detail_bytes':sum(p.stat().st_size for p in output.glob('_static/stv/details/*.js')),
             'total_bytes':sum(p.stat().st_size for p in files if p.is_file())}
    (directory/'metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
    print(json.dumps(metrics,indent=2));return result.returncode


if __name__=='__main__':
    raise SystemExit(main())
