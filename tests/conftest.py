"""Collect stable executable identities and put requirement IDs in JUnit output."""
import json
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption('--requirement-map', default=None, help='Write collected requirement/test metadata as JSON')


def pytest_collection_finish(session):
    target=session.config.getoption('--requirement-map')
    if target:
        cases=[]
        for item in session.items:
            ids=sorted({identity for marker in item.iter_markers('requirements') for identity in marker.args})
            cases.append({'test':item.nodeid,'requirements':ids})
        path=Path(target);path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(cases,indent=2),encoding='utf-8')


def pytest_runtest_setup(item):
    ids=sorted({identity for marker in item.iter_markers('requirements') for identity in marker.args})
    item.user_properties.append(('requirement_ids',','.join(ids)))
