"""Enforce this repository's reviewed CI trust and publication boundary."""
from pathlib import Path
import re
import yaml

ROOT=Path(__file__).resolve().parents[1]
ALLOWED={'actions/checkout','actions/setup-python','actions/setup-node','actions/upload-artifact',
         'actions/download-artifact','actions/attest-build-provenance'}


def validate(name,workflow):
    if workflow.get('permissions')!={'contents':'read'}:raise ValueError('Workflow token must be read-only')
    expected={'push','pull_request','workflow_dispatch'} if name=='validation' else {'workflow_dispatch'}
    if set(workflow.get('on',{}))!=expected:raise ValueError('Unexpected workflow trigger')
    expected_jobs={'core','runtime'} if name=='validation' else {'build','attest'}
    if set(workflow.get('jobs',{}))!=expected_jobs:raise ValueError('Required CI/provenance jobs are missing or changed')
    for job_id,job in workflow['jobs'].items():
        privileged=name=='provenance' and job_id=='attest'
        if not 1<=job.get('timeout-minutes',0)<=30:raise ValueError('Job timeout must be bounded')
        if job.get('runs-on') not in ('windows-2025','ubuntu-24.04'):raise ValueError('Use hosted runners')
        if privileged:
            if job.get('permissions')!={'contents':'read','actions':'read','id-token':'write','attestations':'write'}:raise ValueError('Unexpected attestation permissions')
            if job.get('if')!="github.ref == 'refs/heads/main' && github.event.repository.visibility == 'public'":raise ValueError('Attestation must be gated to public main')
        elif 'permissions' in job:raise ValueError('Code-execution jobs cannot elevate token permissions')
        if name=='provenance' and job_id=='build' and job.get('if')!="github.ref == 'refs/heads/main'":raise ValueError('Candidate builds must be gated to main')
        for step in job['steps']:
            uses=step.get('uses')
            if uses:
                if not re.fullmatch(r'[^@]+@[0-9a-f]{40}',uses) or uses.split('@')[0] not in ALLOWED:raise ValueError('Use approved actions pinned to full commit hashes')
                if uses.startswith('actions/checkout@') and step.get('with',{}).get('persist-credentials') is not False:raise ValueError('Checkout must not persist credentials')
                if privileged and uses.startswith('actions/attest-build-provenance@') and step.get('with',{}).get('subject-path','').splitlines()!=['dist/*.whl','dist/*.tar.gz']:raise ValueError('Attest only the built distributions')
                if privileged and uses.split('@')[0] not in ('actions/download-artifact','actions/attest-build-provenance'):raise ValueError('Privileged job may not check out or execute repository code')
            if privileged and 'run' in step and (step.get('working-directory'),step['run'])!=('dist','sha256sum --strict --check SHA256SUMS'):raise ValueError('Only checksum verification may execute in privileged job')
    if 'secrets.' in yaml.safe_dump(workflow):raise ValueError('These workflows require no user secrets')


def main():
    for name in ('validation','provenance'):
        validate(name,yaml.safe_load((ROOT/'.github/workflows'/f'{name}.yml').read_text(encoding='utf-8')))
    print('Workflow trust policy valid: pinned actions, read-only builds, manual isolated attestation, no user secrets.')


if __name__=='__main__':main()
