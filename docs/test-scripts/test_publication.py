"""Real Sphinx publication boundaries and rollback under failed promotion."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import pytest
from test_build import FIXTURE

ROOT=Path(__file__).parents[2]
spec=importlib.util.spec_from_file_location('stv_docs_builder',ROOT/'scripts/build_docs.py')
builder=importlib.util.module_from_spec(spec);spec.loader.exec_module(builder)


@pytest.fixture(autouse=True)
def source_extension(monkeypatch):
    # pytest's import path does not automatically reach Sphinx subprocesses.
    monkeypatch.setenv('PYTHONPATH',str(ROOT/'src'))


def snapshot(root):
    return {p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


def retain(name,value):
    target=os.environ.get('STV_PUBLICATION_RECORD')
    if target:
        path=Path(target);path.mkdir(parents=True,exist_ok=True)
        (path/(name+'.json')).write_text(json.dumps(value,indent=2),encoding='utf-8')


@pytest.mark.requirements('STV_SYS_009','STV_SWR_042')
def test_clean_publication_removes_obsolete_assets(tmp_path):
    source=tmp_path/'docs';shutil.copytree(FIXTURE,source)
    (source/'retired.rst').write_text('Retired\n=======\n\nFORMER_PUBLICATION_SENTINEL\n')
    (source/'old.txt').write_text('OLD_DOWNLOAD_SENTINEL')
    with (source/'index.rst').open('a') as stream:
        stream.write('\n:download:`Former download <old.txt>`\n\n.. toctree::\n\n   retired\n')
    assert builder.build_docs(source)==0
    output=source/'_build/html'
    old_graphs={p.name for p in (output/'_static/stv').glob('graph-*.js')}
    old_graph_text=''.join(p.read_text(encoding='utf-8') for p in (output/'_static/stv').glob('graph-*.js'))
    assert 'LEAF_B' in old_graph_text
    assert list((output/'_downloads').rglob('old.txt'))
    (output/'obsolete-private.html').write_text('STALE_OUTPUT_SENTINEL')
    (source/'index.rst').write_text('Current\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: ROOT_A\n')
    text=(source/'requirements.rst').read_text().split('.. swr::')[0].replace('   :traces: LEAF_B\n','')
    (source/'requirements.rst').write_text(text)
    (source/'retired.rst').unlink()
    assert builder.build_docs(source)==0
    manifest=json.loads((output/builder.MANIFEST).read_text())['files']
    actual=snapshot(output);assert set(actual)==set(manifest)|{builder.MANIFEST}
    assert all(actual[name]==item['sha256'] for name,item in manifest.items())
    assert not old_graphs & {p.name for p in (output/'_static/stv').glob('graph-*.js')}
    assert not (output/'retired.html').exists() and not (output/'obsolete-private.html').exists()
    assert not list((output/'_downloads').rglob('old.txt'))
    assert not (output/'.doctrees').exists()
    assert 'LEAF_B' not in ''.join(p.read_text(encoding='utf-8') for p in (output/'_static/stv').glob('graph-*.js'))
    assert len(list((output/'_static/stv').glob('graph-*.js')))==1
    assert {p.name for p in (source/'_build').iterdir()}=={'html'}
    retain('clean-rebuild',{'manifest':manifest,'obsolete_pages_downloads_graphs_absent':True,'graph_count':1})


@pytest.mark.requirements('STV_SYS_009','STV_SWR_042')
def test_failed_build_preserves_published_tree(tmp_path):
    source=tmp_path/'docs';shutil.copytree(FIXTURE,source)
    assert builder.build_docs(source)==0
    output=source/'_build/html';before=snapshot(output)
    with (source/'index.rst').open('a') as stream:stream.write('\n.. nonexistent-directive::\n')
    assert builder.build_docs(source)!=0
    assert snapshot(output)==before
    assert {p.name for p in (source/'_build').iterdir()}=={'html'}
    retain('failed-build',{'published_files_unchanged':len(before),'result':'passed'})


@pytest.mark.requirements('STV_SYS_009','STV_SWR_042')
def test_failed_promotion_restores_previous_tree(tmp_path,monkeypatch):
    source=tmp_path/'docs';shutil.copytree(FIXTURE,source)
    assert builder.build_docs(source)==0
    output=source/'_build/html';before=snapshot(output)
    rename=Path.rename
    def fail_stage(path,target):
        if path.name.startswith('.html-stage-') and Path(target)==output:
            raise OSError('Injected promotion failure')
        return rename(path,target)
    monkeypatch.setattr(Path,'rename',fail_stage)
    with pytest.raises(OSError,match='Injected promotion failure'):builder.build_docs(source)
    assert snapshot(output)==before
    assert {p.name for p in (source/'_build').iterdir()}=={'html'}
    retain('failed-promotion',{'published_files_restored':len(before),'result':'passed'})


@pytest.mark.requirements('STV_SYS_009','STV_SWR_042')
@pytest.mark.parametrize('existing',[False,True])
def test_failed_audit_cleans_temporary_output(tmp_path,monkeypatch,existing):
    source=tmp_path/'docs';shutil.copytree(FIXTURE,source)
    if existing:assert builder.build_docs(source)==0
    output=source/'_build/html';before=snapshot(output) if existing else None
    run=builder.subprocess.run
    def reject_audit(command,*args,**kwargs):
        if 'check-method-package.py' in str(command[1]):
            return builder.subprocess.CompletedProcess(command,1)
        return run(command,*args,**kwargs)
    monkeypatch.setattr(builder.subprocess,'run',reject_audit)
    assert builder.build_docs(source)==1
    assert {p.name for p in (source/'_build').iterdir()}==({'html'} if existing else set())
    if existing:assert snapshot(output)==before


@pytest.mark.requirements('STV_SYS_009','STV_SWR_042')
def test_failed_rollback_preserves_recoverable_backup(tmp_path,monkeypatch):
    source=tmp_path/'docs';shutil.copytree(FIXTURE,source)
    assert builder.build_docs(source)==0
    output=source/'_build/html';before=snapshot(output);rename=Path.rename
    def fail_promotion_and_rollback(path,target):
        if Path(target)==output and path.name.startswith(('.html-stage-','.html-previous-')):
            raise OSError('Injected rename failure')
        return rename(path,target)
    monkeypatch.setattr(Path,'rename',fail_promotion_and_rollback)
    with pytest.raises(RuntimeError,match='recover previous HTML'):
        builder.build_docs(source)
    backups=list((source/'_build').glob('.html-previous-*'))
    assert len(backups)==1 and snapshot(backups[0])==before
    assert {p.name for p in (source/'_build').iterdir()}=={backups[0].name}
