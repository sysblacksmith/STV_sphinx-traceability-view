"""Exercise build rejection using an isolated frontend, never installed inputs."""
import json
from pathlib import Path
import shutil
import subprocess
import pytest

ROOT=Path(__file__).parents[2]

@pytest.mark.requirements('STV_SYS_009','STV_SWR_042')
def test_build_rejects_unaudited_elk_and_missing_notices(tmp_path):
    frontend=tmp_path/'frontend';frontend.mkdir()
    shutil.copytree(ROOT/'frontend/legal',frontend/'legal')
    dependency=frontend/'node_modules/elkjs';dependency.mkdir(parents=True)
    shutil.copyfile(ROOT/'frontend/node_modules/elkjs/package.json',dependency/'package.json')
    (dependency/'lib').mkdir()
    binary=(ROOT/'frontend/node_modules/elkjs/lib/elk.bundled.js').read_bytes()
    (dependency/'lib/elk.bundled.js').write_bytes(binary)
    command=['node','--input-type=module','-e','await import(process.argv[1]);',(ROOT/'frontend/build.js').as_uri()]
    # ESM resolves build-tool dependencies beside the original script, while
    # its legal/data inputs resolve inside this isolated working directory.
    metadata=json.loads((dependency/'package.json').read_text())
    changed=dict(metadata,version='unaudited')
    (dependency/'package.json').write_text(json.dumps(changed))
    result=subprocess.run(command,cwd=frontend,capture_output=True,text=True)
    assert result.returncode!=0 and 'renew the compiled-dependency audit' in result.stderr
    (dependency/'package.json').write_text(json.dumps(metadata))
    (dependency/'lib/elk.bundled.js').write_bytes(binary+b'\n// unexpected change')
    result=subprocess.run(command,cwd=frontend,capture_output=True,text=True)
    assert result.returncode!=0 and 'renew the compiled-dependency audit' in result.stderr
    (dependency/'lib/elk.bundled.js').write_bytes(binary)
    notice=frontend/'legal/EPL-1.0.txt';original=notice.read_bytes()
    notice.write_bytes(original+b'\nchanged')
    result=subprocess.run(command,cwd=frontend,capture_output=True,text=True)
    assert result.returncode!=0 and 'Audited legal input changed: EPL-1.0.txt' in result.stderr
    notice.unlink()
    result=subprocess.run(command,cwd=frontend,capture_output=True,text=True)
    assert result.returncode!=0 and 'EPL-1.0.txt' in result.stderr and 'ENOENT' in result.stderr
