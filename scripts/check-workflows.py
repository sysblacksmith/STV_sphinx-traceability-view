"""Enforce this repository's reviewed CI trust and publication boundary."""
from pathlib import Path
import re
import yaml

ROOT=Path(__file__).resolve().parents[1]
ALLOWED={'actions/checkout','actions/setup-python','actions/setup-node','actions/upload-artifact',
         'actions/download-artifact','actions/attest-build-provenance',
         'actions/upload-pages-artifact','actions/deploy-pages'}


def validate_release(workflow):
    if workflow.get('permissions') != {'contents': 'read'} or workflow.get('on') != {'release': {'types': ['published']}}:
        raise ValueError('Release publication requires a published-release event and read-only default token')
    jobs = workflow.get('jobs', {})
    if set(jobs) != {'build', 'publish-pypi', 'deploy-docs'}:
        raise ValueError('Release publication jobs changed')
    build = jobs['build']
    if build.get('if') != "github.event.repository.visibility == 'public' && !github.event.release.prerelease && !github.event.release.draft":
        raise ValueError('Only final public releases may publish')
    steps = build['steps']
    checkout = steps[0]
    if (checkout.get('with', {}).get('ref') != '${{ github.event.release.tag_name }}'
            or checkout['with'].get('fetch-depth') != 0):
        raise ValueError('Release build requires the tag and full ancestry')
    commands = [s.get('run') for s in steps]
    if not {'python scripts/release.py prepare', 'python scripts/ci.py validate'} <= set(commands):
        raise ValueError('Release inputs and documentation must be validated')
    if commands.index('python scripts/release.py prepare') >= commands.index('python scripts/ci.py validate'):
        raise ValueError('Validate release assets before running consumer tests')
    test_step = next(s for s in steps if s.get('run') == 'python scripts/ci.py validate')
    if test_step.get('env') != {'STV_RELEASE_DIR': 'docs/_build/release-publish/packages'}:
        raise ValueError('Consumer tests must use exact release assets')
    for identity, job in jobs.items():
        if not 1 <= job.get('timeout-minutes', 0) <= 30:
            raise ValueError('Release job timeout must be bounded')
        privileged = identity != 'build'
        if job.get('runs-on') != ('ubuntu-24.04' if privileged else 'windows-2025'):
            raise ValueError('Use reviewed hosted release runners')
        if privileged:
            expected = {'contents': 'read', 'id-token': 'write'}
            if identity == 'deploy-docs':
                expected['pages'] = 'write'
            if job.get('permissions') != expected:
                raise ValueError('Unexpected release publication permissions')
            environment = 'pypi' if identity == 'publish-pypi' else 'github-pages'
            dependencies = 'build' if identity == 'publish-pypi' else ['build', 'publish-pypi']
            if job.get('environment', {}).get('name') != environment or job.get('needs') != dependencies:
                raise ValueError('Publication environments and dependency gates must be preserved')
        elif 'permissions' in job:
            raise ValueError('Release code execution must remain read-only')
        for step in job['steps']:
            action = step.get('uses', '')
            if action:
                allowed = (ALLOWED - {'actions/deploy-pages', 'actions/attest-build-provenance'}) if not privileged else (
                    {'actions/download-artifact', 'pypa/gh-action-pypi-publish'} if identity == 'publish-pypi' else {'actions/deploy-pages'})
                if not re.fullmatch(r'[^@]+@[0-9a-f]{40}', action) or action.split('@')[0] not in allowed:
                    raise ValueError('Unapproved or unpinned release action')
                if action.startswith('actions/checkout@') and step.get('with', {}).get('persist-credentials') is not False:
                    raise ValueError('Release checkout must not persist credentials')
            if privileged and 'run' in step:
                if identity != 'publish-pypi' or (step.get('working-directory'), step['run']) != ('release', 'sha256sum --strict --check SHA256SUMS'):
                    raise ValueError('No repository code may execute with publication credentials')
    publish = jobs['publish-pypi']['steps']
    if len(publish) != 3 or not publish[-1].get('uses', '').startswith('pypa/gh-action-pypi-publish@'):
        raise ValueError('PyPI publication must follow download and checksum verification')
    if publish[0].get('with') != {'name': 'release-distributions', 'path': 'release'}:
        raise ValueError('Download only the qualified release artifact')
    if publish[-1].get('with') != {'packages-dir': 'release/packages/', 'attestations': True}:
        raise ValueError('Publish only the verified packages with attestations')
    if len(jobs['deploy-docs']['steps']) != 1:
        raise ValueError('Pages deployment must only deploy the validated artifact')
    uploads = [s for s in steps if s.get('uses', '').startswith('actions/upload-pages-artifact@')]
    if len(uploads) != 1 or uploads[0].get('with', {}).get('path') != 'docs/_build/html':
        raise ValueError('Publish only the clean HTML tree')
    if 'secrets.' in yaml.safe_dump(workflow):
        raise ValueError('Release publishing uses Trusted Publishing, not stored secrets')


def validate(name,workflow):
    if name == 'release':
        return validate_release(workflow)
    if workflow.get('permissions')!={'contents':'read'}:raise ValueError('Workflow token must be read-only')
    expected={'push','pull_request','workflow_dispatch'} if name=='validation' else {'workflow_dispatch'}
    if set(workflow.get('on',{}))!=expected:raise ValueError('Unexpected workflow trigger')
    expected_jobs={'core','runtime'} if name=='validation' else ({'build','deploy'} if name=='pages' else {'build','attest'})
    if set(workflow.get('jobs',{}))!=expected_jobs:raise ValueError('Required CI/provenance jobs are missing or changed')
    for job_id,job in workflow['jobs'].items():
        privileged=name=='provenance' and job_id=='attest'
        deploying=name=='pages' and job_id=='deploy'
        if not 1<=job.get('timeout-minutes',0)<=30:raise ValueError('Job timeout must be bounded')
        if job.get('runs-on') not in ('windows-2025','ubuntu-24.04'):raise ValueError('Use hosted runners')
        if privileged:
            if job.get('permissions')!={'contents':'read','actions':'read','id-token':'write','attestations':'write'}:raise ValueError('Unexpected attestation permissions')
            if job.get('if')!="github.ref == 'refs/heads/main' && github.event.repository.visibility == 'public'":raise ValueError('Attestation must be gated to public main')
        elif deploying:
            if job.get('permissions')!={'contents':'read','pages':'write','id-token':'write'}:raise ValueError('Unexpected Pages permissions')
            if job.get('if')!="inputs.publish && github.ref == 'refs/heads/main' && github.event.repository.visibility == 'public'":raise ValueError('Pages deployment must require explicit public-main publication')
            if job.get('needs')!='build' or job.get('environment',{}).get('name')!='github-pages':raise ValueError('Pages must deploy its build through the Pages environment')
            if len(job['steps'])!=1:raise ValueError('Pages deploy job must only deploy the artifact')
        elif 'permissions' in job:raise ValueError('Code-execution jobs cannot elevate token permissions')
        if name=='pages' and job_id=='build' and job.get('if')!="github.ref == 'refs/heads/main'":raise ValueError('Pages builds must use main')
        if name=='provenance' and job_id=='build' and job.get('if')!="github.ref == 'refs/heads/main'":raise ValueError('Candidate builds must be gated to main')
        for step in job['steps']:
            uses=step.get('uses')
            if uses:
                if not re.fullmatch(r'[^@]+@[0-9a-f]{40}',uses) or uses.split('@')[0] not in ALLOWED:raise ValueError('Use approved actions pinned to full commit hashes')
                if uses.startswith('actions/checkout@') and step.get('with',{}).get('persist-credentials') is not False:raise ValueError('Checkout must not persist credentials')
                if deploying and uses.split('@')[0]!='actions/deploy-pages':raise ValueError('Pages deploy job may not execute repository code')
                if uses.startswith('actions/upload-pages-artifact@') and step.get('with',{}).get('path')!='docs/_build/html':raise ValueError('Pages may upload only the validated HTML tree')
                if not deploying and uses.startswith('actions/deploy-pages@'):raise ValueError('Pages deployment requires an isolated job')
                if privileged and uses.startswith('actions/attest-build-provenance@') and step.get('with',{}).get('subject-path','').splitlines()!=['dist/*.whl','dist/*.tar.gz']:raise ValueError('Attest only the built distributions')
                if privileged and uses.split('@')[0] not in ('actions/download-artifact','actions/attest-build-provenance'):raise ValueError('Privileged job may not check out or execute repository code')
            if privileged and 'run' in step and (step.get('working-directory'),step['run'])!=('dist','sha256sum --strict --check SHA256SUMS'):raise ValueError('Only checksum verification may execute in privileged job')
            if deploying and ('run' in step or not uses):raise ValueError('Pages deploy job may only use the deployment action')
    if name=='pages':
        publish=workflow['on']['workflow_dispatch']['inputs']['publish']
        if publish.get('type')!='boolean' or publish.get('default') is not False:raise ValueError('Pages publication must be opt-in')
        steps=workflow['jobs']['build']['steps']
        commands=[step.get('run') for step in steps]
        if 'python scripts/build_docs.py docs' not in commands:raise ValueError('Pages requires the clean publication builder')
        uploads=[i for i,step in enumerate(steps) if step.get('uses','').startswith('actions/upload-pages-artifact@')]
        if len(uploads)!=1 or uploads[0]!=len(steps)-1:raise ValueError('Pages must upload once after validation')
    if 'secrets.' in yaml.safe_dump(workflow):raise ValueError('These workflows require no user secrets')


def main():
    for name in ('validation','provenance','pages','release'):
        validate(name,yaml.safe_load((ROOT/'.github/workflows'/f'{name}.yml').read_text(encoding='utf-8')))
    print('Workflow trust policy valid: pinned actions, read-only builds, isolated publication, no user secrets.')


if __name__=='__main__':main()
