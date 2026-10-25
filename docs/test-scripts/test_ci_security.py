"""CI trust-boundary policy and real checksum-verifier tamper detection."""
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import pytest
import yaml

ROOT=Path(__file__).parents[2]

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,ROOT/path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

policy=load('stv_workflow_policy','scripts/check-workflows.py')
ci=load('stv_ci','scripts/ci.py')


@pytest.mark.requirements('STV_SYS_009','STV_SWR_042')
def test_workflow_policy_accepts_reviewed_files_and_rejects_privilege_drift():
    ordinary=yaml.safe_load((ROOT/'.github/workflows/validation.yml').read_text())
    provenance=yaml.safe_load((ROOT/'.github/workflows/provenance.yml').read_text())
    policy.validate('validation',ordinary);policy.validate('provenance',provenance)
    bad=copy.deepcopy(ordinary);bad['permissions']['contents']='write'
    with pytest.raises(ValueError):policy.validate('validation',bad)
    bad=copy.deepcopy(ordinary);bad['on']['pull_request_target']={}
    with pytest.raises(ValueError):policy.validate('validation',bad)
    bad=copy.deepcopy(ordinary);bad['jobs']['core']['steps'][0]['uses']='actions/checkout@main'
    with pytest.raises(ValueError):policy.validate('validation',bad)
    bad=copy.deepcopy(provenance);bad['jobs']['attest']['steps'].append({'run':'python untrusted.py'})
    with pytest.raises(ValueError):policy.validate('provenance',bad)
    bad=copy.deepcopy(provenance);del bad['jobs']['attest']
    with pytest.raises(ValueError):policy.validate('provenance',bad)
    bad=copy.deepcopy(provenance);bad['jobs']['attest']['steps'][-1]['with']['subject-path']='other/*'
    with pytest.raises(ValueError):policy.validate('provenance',bad)
    bad=copy.deepcopy(provenance);bad['jobs']['attest']['if']='always()'
    with pytest.raises(ValueError):policy.validate('provenance',bad)


@pytest.mark.requirements('STV_SYS_009','STV_SWR_042')
def test_candidate_checksums_detect_changed_artifact_bytes(tmp_path):
    wheel=tmp_path/'example-1-py3-none-any.whl';wheel.write_bytes(b'wheel bytes')
    source=tmp_path/'example-1.tar.gz';source.write_bytes(b'source bytes')
    ci.write_checksums(tmp_path)
    assert json.loads((tmp_path/'build-info.json').read_text())['source_commit']==subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    expected={hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name for p in (wheel,source)}
    assert set((tmp_path/'SHA256SUMS').read_text().splitlines())==expected
    verifier=shutil.which('sha256sum') or str(Path(os.environ.get('ProgramFiles','C:/Program Files'))/'Git/usr/bin/sha256sum.exe')
    assert Path(verifier).is_file(),'Provision GNU sha256sum (included with Git for Windows)'
    assert subprocess.run([verifier,'--strict','--check','SHA256SUMS'],cwd=tmp_path,capture_output=True).returncode==0
    wheel.write_bytes(wheel.read_bytes()+b' altered')
    assert subprocess.run([verifier,'--strict','--check','SHA256SUMS'],cwd=tmp_path,capture_output=True).returncode!=0
    (tmp_path/'extra-2.whl').write_bytes(b'extra')
    with pytest.raises(ValueError):ci.write_checksums(tmp_path)


def test_pages_policy_rejects_publication_and_permission_drift():
    pages=yaml.safe_load((ROOT/'.github/workflows/pages.yml').read_text())
    policy.validate('pages',pages)
    mutations=[
        lambda w: w['on']['workflow_dispatch']['inputs']['publish'].update(default=True),
        lambda w: w['jobs']['deploy'].update({'if': 'always()'}),
        lambda w: w['jobs']['deploy']['steps'].append({'run': 'python project.py'}),
        lambda w: w['jobs']['build'].update(permissions={'contents': 'write'}),
        lambda w: w['jobs']['build']['steps'][-1]['with'].update(path='.'),
        lambda w: w['jobs']['deploy'].update(needs='unrelated'),
    ]
    for mutate in mutations:
        bad=copy.deepcopy(pages);mutate(bad)
        with pytest.raises(ValueError):policy.validate('pages',bad)


def test_release_policy_rejects_untrusted_triggers_and_publication_code():
    release = yaml.safe_load((ROOT/'.github/workflows/release.yml').read_text())
    policy.validate('release', release)
    mutations = [
        lambda w: w['on'].update(pull_request={}),
        lambda w: w['jobs']['build'].update({'if': 'always()'}),
        lambda w: w['jobs']['build']['steps'][0]['with'].update(ref='main'),
        lambda w: w['jobs']['publish-pypi']['steps'].append({'run': 'python project.py'}),
        lambda w: w['jobs']['deploy-docs'].update(needs='build'),
        lambda w: w['jobs']['publish-pypi']['steps'][-1]['with'].update({'skip-existing': True}),
        lambda w: w['jobs']['publish-pypi']['steps'][-1]['with'].update({'packages-dir': '.'}),
        lambda w: w['jobs']['build'].update(permissions={'id-token': 'write'}),
    ]
    for mutate in mutations:
        bad = copy.deepcopy(release)
        mutate(bad)
        with pytest.raises(ValueError):
            policy.validate('release', bad)
