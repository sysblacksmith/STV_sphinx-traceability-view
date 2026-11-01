"""Consolidate successful observations without claiming publication or acceptance."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
result = json.loads((HERE/'results.json').read_text())
mapping = json.loads((HERE/'mapping-review.json').read_text())
assert mapping['canonical_cases'] == 122 and not mapping['missing']
assert not any(result['outcomes'][key] for key in ('failed', 'error', 'skipped'))
assert all(item['returncode'] == 0 for item in result['attempts'] if item['suite'] != 'documentation')
assert (HERE/'manual-observations.rst').is_file()
targets = {
    'requirements-stakeholder.rst': {'STV_SHR_003', 'STV_SHR_057', *(f'STV_SHR_{i:03}' for i in range(62, 66))},
    'requirements-software.rst': {'STV_SWR_003', 'STV_SWR_063', 'STV_SWR_073', 'STV_SWR_074', 'STV_SWR_075'},
    'change-requests/STV_CR_019_remember-current-view.rst': {'STV_CR_019'},
    'test-cases/system-tests.rst': {'STV_TC_SY_070'},
    'test-cases/software-tests.rst': {'STV_TC_SW_056'},
}
assessments = []
criteria = {}
for name, identities in targets.items():
    path = ROOT/'docs'/name
    before = path.read_text()
    strip = lambda text: re.sub(r'(?m)^   :verification_state: [a-z_]+$', '   :verification_state: <assessed>', text)
    criteria['docs/'+name] = hashlib.sha256(strip(before).encode()).hexdigest()
    lines = before.splitlines()
    current = None
    seen = set()
    for index, line in enumerate(lines):
        if line.startswith('   :id: '):
            current = line.split(':id: ', 1)[1]
        if current in identities and line.startswith('   :verification_state: '):
            assessments.append(dict(id=current, before=line.split()[-1], after='passed'))
            lines[index] = '   :verification_state: passed'
            seen.add(current)
    assert seen == identities, (name, identities-seen)
    after = '\n'.join(lines)+'\n'
    assert strip(before) == strip(after)
    path.write_text(after)
(HERE/'verification-assessment.json').write_text(json.dumps(dict(recorded_at=datetime.now(timezone.utc).isoformat(), basis='Complete Windows/Firefox file/HTTP selection, fresh minimum runtime, six CR019 browser supplements, 200-node/ten-card and real-hover exports, semantic criterion review and owner native observations; acceptance statuses unchanged', changes=assessments, unchanged_criteria_sha256=criteria), indent=2)+'\n')
for name in ('sphinx_traceability_view-1.2.0-py3-none-any.whl', 'sphinx_traceability_view-1.2.0.tar.gz'):
    source = HERE/'artifacts'/name
    destination = ROOT/'dist'/name
    if destination.exists():
        assert destination.read_bytes() == source.read_bytes(), destination
    else:
        shutil.copyfile(source, destination)
    assert hashlib.sha256(destination.read_bytes()).hexdigest() == hashlib.sha256(source.read_bytes()).hexdigest()
checksum = ROOT/'dist/SHA256SUMS-1.2.0'
if checksum.exists():
    assert checksum.read_bytes() == (HERE/'artifacts/SHA256SUMS').read_bytes()
else:
    shutil.copyfile(HERE/'artifacts/SHA256SUMS', checksum)
python_count = len(__import__('xml.etree.ElementTree', fromlist=['parse']).parse(HERE/'pytest.xml').findall('.//testcase'))
node_count = result['outcomes']['passed']-python_count
title = 'STV 1.2.0 release qualification'
text = f'''{title}
{'='*len(title)}

Candidate: **1.2.0-candidate-1**, based on Git revision
``{result['revision']}`` plus the retained worktree/source identity.
The owner authorized 1.2.0 workspace preparation and full release qualification
on 2026-11-01. No commit, tag, push, publication or deployment is performed.

Observed qualification
----------------------

* One complete main selection: **{result['outcomes']['passed']} passed**,
  **{python_count} Python / {node_count} JavaScript**, no failures, errors or skips.
  The Python reset wrapper also executes two Node command-sequence checks;
  those nested checks are not counted again.
* Six separate final CR019 browser supplements passed on file and HTTP.
  The earlier four-case supplement is retained; its repeated cases are not
  added to the final six-case supplement total.
* All **122 delivered canonical procedures** have fresh mapped observations.
  Four occurrence-mode procedures remain explicitly deferred. Acceptance
  statuses and ADR lifecycle are unchanged; only assessed verification fields
  and latest case/execution links advance.
* Windows 11, Python 3.13.17, installed Firefox 159.0, geckodriver 0.37.1,
  Node 24.21.0; direct-file and static HTTP browser workflows.
* A fresh offline Python 3.10.9 consumer passes installation, dependency checks,
  installed-runtime import and clean host builds against this exact wheel.
* Fresh 30,000-Need / 90,000-link host generation and current browser capacity
  measurements passed. Timings are observed measurements, with no invented
  performance threshold. No older fixture/result was substituted.
* Four maximum-size SVG exports passed: 200 visible nodes, ten open cards,
  1600/900px, file/HTTP. Real visible-hover exports reopened successfully on
  both transports. Representative source/reopened/narrow screenshots were
  visually inspected; raw SVGs are preserved losslessly with hash manifests.
* The owner confirmed native automatic/prompted saving, cancellation and
  browser zoom behavior; see :doc:`manual-observations`.
* Fresh retained-archive inspection verified 47 archive identities and the
  complete licensing supplement. Original archives and Git history are unchanged.

CR019 criterion assessment
--------------------------

Pure snapshot tests cover schema/context validation, current-graph authority,
hidden/removed IDs, seeded/project state, page memories, card age/order,
200/201-node bounds, independent storage keys, quota/getter/removal errors and
geometry reuse. Real browser checks cover keyboard opt-in/out, reload/restart,
expansion and stable placement, FIFO/card closing, independent saved views and
pages, last-save-wins tabs, safe untrusted content, reduced card capacity,
blocked storage, pending/stale/failed layouts, back/forward navigation and
changed/narrow viewport behavior without startup focus theft. Current source
contracts and requirement-to-case assertions were reviewed against these
observations. No stored HTML is used as content authority.

Retained attempts and corrections
---------------------------------

The initial runner records a Windows permission error during final HTML
promotion, after strict Sphinx and publication audits passed. The fresh
documentation retry succeeded without product changes. The original failed
runner/log remains intact; final consolidated documentation/evidence checks
are recorded separately.

The first Python 3.10 install lacked its Python-version-specific tomli wheel.
That provisioning failure is retained; a fresh environment with the completed
offline wheelhouse passed. The historical helper initially omitted retained
development archives and the compressed cleanup evidence archive from its
known checksums. Prior preservation-manifest checksums reconcile those inputs;
the audited ELK fingerprint and complete supplement checks remain enforced.

The release runner now reports individual Node checks with process isolation
disabled and runs local/published method-package gates. These are runner
corrections, with no new product behavior beyond the already merged CR019.

Disposition and boundaries
--------------------------

Local executable qualification passed; final consolidated gates are retained
in ``final-validation.json``. Release approval and successful hosted checks
remain required before publication. Do not infer an existing release/tag from
these local observations. The final release commit does not exist yet.

Qualified scope remains Windows/Firefox on file and HTTP. Other operating
systems/browsers, mobile/touch optimization, occurrence mode and universal
SVG-editor support remain deferred. The existing owner-authorized PR012
branch-protection/provenance hardening disposition is unchanged.

All distributions, including older versions, remain in ``dist/``. The owner
approved only the concrete cleanup list in :doc:`cleanup-review` after testing.
Post-release workspace review remains due when publication completes.

Evidence
--------

* :download:`Canonical observations <case-results.json>`
* :download:`Verification assessment <verification-assessment.json>`
* :download:`Exact distribution checksums <artifacts/SHA256SUMS>`
* :download:`Final CR019 supplemental report <remember-supplement-final.xml>`
* :download:`Fresh minimum-runtime commands <supplement-commands-retry.json>`
* :download:`Historical licensing assessment <historical-check.json>`
* :download:`Supplemental commands and attempts <supplemental-attempts.json>`
* :download:`Maximum-size export results <export-capacity.json>`
* :download:`Visible-hover export results <hover-export.json>`
* :download:`Raw SVG observations <retained-exports.zip>`
* :download:`SVG preservation manifest <export-preservation.json>`

.. toctree::
   :maxdepth: 1

   cases
   manual-observations
   cleanup-review
'''
(HERE/'qualification.rst').write_text(text)
index = HERE/'index.rst'
content = index.read_text()
if '   qualification\n' not in content:
    index.write_text(content+'\n.. toctree::\n   :maxdepth: 1\n\n   qualification\n')
maturity = ROOT/'docs/maturity.rst'
content = maturity.read_text()
heading = '1.2.0 release qualification, 2026-11-01'
entry = f'''{heading}
{'-'*len(heading)}

The owner authorized version 1.2.0 and complete qualification on current main.
CR019 is already accepted and implemented. Candidate 1 passed {result['outcomes']['passed']}
main automated cases ({python_count} Python / {node_count} JavaScript), six separate
CR019 browser supplements, a fresh Python 3.10 consumer, fresh capacity host and
browser checks, maximum-size/hover SVG supplements and licensing checks. The
owner confirmed native save/cancel and browser zoom behavior. Scoped CR019
verification advances without changing acceptance or earlier release records.

:doc:`test-execution/1.2.0-candidate-1/qualification` records the candidate,
exact artifacts, failed provisioning/publication attempts and successful retests,
semantic coverage, cleanup approval and limits. Final consolidated gates are
retained separately; hosted checks and owner release approval remain before
publication. No commit, tag, push, release or deployment is claimed. Other
platforms/browsers and occurrence mode remain deferred.

'''
assert heading not in content
anchor = 'CR019 implemented development increment, 2026-10-28'
assert anchor in content
maturity.write_text(content.replace(anchor, entry+anchor, 1))
print(json.dumps(dict(main_passed=result['outcomes']['passed'], python=python_count, javascript=node_count, canonical_cases=mapping['canonical_cases']), indent=2))
