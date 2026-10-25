"""Reusable nine-type, five-link Sphinx-Needs model (8.2.0)."""

REVIEW_STATES = ['draft', 'reviewed', 'accepted']
PROBLEM_REPORT_STATES = ['new', 'analyzed', 'fixed']
CHANGE_REQUEST_STATES = ['draft', 'accepted', 'implemented']
NEEDS_STATUSES_BY_TYPE = {kind: REVIEW_STATES for kind in ('shr', 'sysr', 'swr', 'syse', 'swe')}
NEEDS_STATUSES_BY_TYPE['problem_report'] = PROBLEM_REPORT_STATES
NEEDS_STATUSES_BY_TYPE['change_request'] = CHANGE_REQUEST_STATES

TEST_RESULTS = ['not_run', 'passed', 'failed', 'error', 'skipped', 'blocked']
NEEDS_STATUSES_BY_TYPE['test_case'] = REVIEW_STATES
NEEDS_STATUSES_BY_TYPE['test_execution'] = ['recorded']

NEEDS_TYPES = [
    dict(directive='change_request', title='Change request', prefix='CR_', color='#E7EDF8', style='node'),
    dict(directive='test_case', title='Test case', prefix='TC_', color='#E2F2DA', style='node'),
    dict(directive='test_execution', title='Test execution', prefix='TE_', color='#DCEEF2', style='node'),
    dict(directive='shr', title='Stakeholder requirement', prefix='SHR_', color='#FFF0C2', style='node'),
    dict(directive='sysr', title='System requirement', prefix='SYS_', color='#DDECF9', style='node'),
    dict(directive='swr', title='Software requirement', prefix='SWR_', color='#E4F1ED', style='node'),
    dict(directive='syse', title='System element', prefix='SE_', color='#EAE5F4', style='node'),
    dict(directive='swe', title='Software element', prefix='SWE_', color='#F0F4F8', style='node'),
    dict(directive='problem_report', title='Problem report', prefix='PR_', color='#FCE4D6', style='node'),
]
NEEDS_LINKS = {
    'verifies': {'incoming': 'verified by', 'outgoing': 'verifies', 'copy': False},
    'executed_by': {'incoming': 'execution of', 'outgoing': 'executed by', 'copy': False},
    'derives_from': {'incoming': 'refined by', 'outgoing': 'derives from', 'copy': False},
    'allocated_to': {'incoming': 'allocated requirements', 'outgoing': 'allocated to', 'copy': False},
    'part_of': {'incoming': 'contains', 'outgoing': 'part of', 'copy': False},
}
NEEDS_FIELDS = {
    'last_result': {'schema': {'type': 'string', 'enum': TEST_RESULTS}},
    'result': {'schema': {'type': 'string', 'enum': TEST_RESULTS[1:]}},
    'executed_at': {'schema': {'type': 'string'}},
    'status': {'schema': {'type': 'string', 'enum': list(dict.fromkeys(REVIEW_STATES + PROBLEM_REPORT_STATES + CHANGE_REQUEST_STATES + ['recorded']))}},
    'basis': {'schema': {'type': 'string', 'enum': ['observed', 'documented', 'owner', 'inferred']}},
    'evidence': {'schema': {'type': 'string'}},
    'priority': {'schema': {'type': 'string', 'enum': ['unassigned', 'high', 'medium', 'low']}},
    'verification_state': {'schema': {'type': 'string', 'enum': ['not_assessed', 'passed', 'failed', 'partial']}},
}

