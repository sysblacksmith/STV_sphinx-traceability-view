"""Publish validated fresh HTML and clean up this build's temporary output."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import uuid

MANIFEST='_stv-publication.json'


def build_docs(source):
    source=Path(source).resolve()
    build=(source/'_build').resolve()
    if not build.is_relative_to(source):
        raise ValueError('Documentation build directory must stay within the source directory')
    build.mkdir(parents=True,exist_ok=True)
    output=build/'html'
    # Reject redirected paths before moving any existing tree.
    if output.is_symlink() or output.resolve()!=output:
        raise ValueError('HTML output must be a direct directory below the build directory')
    if output.exists() and not output.is_dir():
        raise ValueError('HTML output must be a directory')
    with tempfile.TemporaryDirectory(prefix='.html-stage-',dir=build) as stage, \
         tempfile.TemporaryDirectory(prefix='.html-doctrees-',dir=build) as doctrees:
        return publish(source,build,output,Path(stage),Path(doctrees))


def publish(source,build,output,stage,doctrees):
    result=subprocess.run([sys.executable,'-m','sphinx','-E','-a','-W','--keep-going',
                           '-b','html','-d',str(doctrees),str(source),str(stage)])
    if result.returncode:
        print('Build failed; published output retained.',file=sys.stderr)
        return result.returncode
    audit=subprocess.run([sys.executable,str(Path(__file__).with_name('check-method-package.py')),'--published',str(stage)])
    if audit.returncode:
        print('Publication audit failed; published output retained.',file=sys.stderr)
        return audit.returncode
    if (stage/MANIFEST).exists():
        raise ValueError('Source output collides with the reserved publication manifest')
    files={}
    for path in sorted(stage.rglob('*')):
        if path.is_symlink():
            raise ValueError('Publication staging must not contain symbolic links')
        if path.is_file():
            data=path.read_bytes()
            files[path.relative_to(stage).as_posix()]={'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    (stage/MANIFEST).write_text(json.dumps({'files':files},indent=2)+'\n',encoding='utf-8')
    previous=build/('.html-previous-'+uuid.uuid4().hex)
    # All rename targets are resolved, direct children of this build directory.
    for path in (stage,output,previous):
        if path.resolve().parent!=build:
            raise ValueError('Publication rename target escaped the build directory')
    had_previous=output.exists()
    if had_previous:output.rename(previous)
    try:
        stage.rename(output)
    except OSError:
        if had_previous:
            try:
                previous.rename(output)
            except OSError as error:
                # Never delete the only surviving published tree when rollback
                # itself fails (for example, because another process locks it).
                raise RuntimeError(f'Promotion and rollback failed; recover previous HTML from {previous}') from error
        raise
    if had_previous:
        shutil.rmtree(previous)
    print(f'Documentation built: {output / "index.html"}')
    print(f'Publication inventory: {output / MANIFEST}')
    return 0


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',nargs='?',type=Path,default=Path(__file__).resolve().parents[1]/'docs')
    args=parser.parse_args()
    return build_docs(args.source)


if __name__=='__main__':sys.exit(main())

