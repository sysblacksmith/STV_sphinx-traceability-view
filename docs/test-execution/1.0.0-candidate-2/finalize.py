"""Consolidate release evidence without changing product or runner inputs."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
result = json.loads((RECORD/'results.json').read_text())
assert all(x['returncode'] == 0 for x in result['attempts'])
assert result['outcomes']['failed'] == result['outcomes']['error'] == result['outcomes']['skipped'] == 0
assert all(x['returncode'] == 0 for x in json.loads((RECORD/'supplement-commands.json').read_text()))
mapped = json.loads((RECORD/'case-results.json').read_text())
counts = {name: sum(i['report']==name for i in mapped) for name in ('pytest.xml', 'node.xml')}
build = json.loads((RECORD/'capacity-build.json').read_text())
assert build['needs'] == 30000 and build['authored_edges'] == 90000
runtime = {}
import zipfile
with zipfile.ZipFile(RECORD/'artifacts/sphinx_traceability_view-1.0.0-py3-none-any.whl') as wheel:
    for name in wheel.namelist():
        if name.startswith('sphinx_traceability_view/') and not name.endswith('/'):
            source = ROOT/'src'/name
            assert source.read_bytes() == wheel.read(name), name
            runtime[name] = hashlib.sha256(wheel.read(name)).hexdigest()
(RECORD/'runtime-equivalence.json').write_text(json.dumps(runtime, indent=2), encoding='utf-8')

# The prior partial disposition was specifically the unqualified nested-path gap.
# This full run includes both transports and the nested-path/retry procedure.
assert any('test_nested_windows_detail_loading_and_retry' in i['selector'] and i['result']=='passed' for i in mapped)
for name, identities in [('requirements-system.rst', {'STV_SYS_003','STV_SYS_006'}),
                         ('requirements-software.rst', {'STV_SWR_015','STV_SWR_017','STV_SWR_018'})]:
    path = ROOT/'docs'/name
    blocks = re.split(r'(?=^\.\. (?:sysr|swr)::)', path.read_text(encoding='utf-8'), flags=re.M)
    for index, block in enumerate(blocks):
        match = re.search(r'^   :id: (\S+)', block, re.M)
        if match and match[1] in identities:
            blocks[index] = block.replace(':verification_state: partial', ':verification_state: passed')
    path.write_text(''.join(blocks), encoding='utf-8')

# Remove obsolete pending-review wording only in the newly accepted designs.
selected = {'STV_TC_SY_038', *[f'STV_TC_SY_{i:03}' for i in range(47,55)], *[f'STV_TC_SW_{i:03}' for i in range(40,43)]}
for path in (ROOT/'docs/test-cases').glob('*.rst'):
    blocks = re.split(r'(?=^\.\. test_case::)', path.read_text(encoding='utf-8'), flags=re.M)
    for index, block in enumerate(blocks):
        match = re.search(r'^   :id: (\S+)', block, re.M)
        if match and match[1] in selected:
            block = block.replace('Design review remains pending.', 'Design acceptance is recorded in :doc:`../concept-reviews/round-14`.')
            block = block.replace('Design review is pending.', 'Design acceptance is recorded in :doc:`../concept-reviews/round-14`.')
            block = block.replace('procedure awaits owner review.', 'procedure is owner-accepted under :doc:`../concept-reviews/round-14`.')
            block = block.replace('New design\n   review remains pending; these are not full release qualification cases.', 'Design acceptance is recorded in :doc:`../concept-reviews/round-14`;\n   complete release qualification remains separate from this individual case.')
            blocks[index] = block
    path.write_text(''.join(blocks), encoding='utf-8')

text = f'''v1.0.0 qualification
=============================

The owner authorized release in :ref:`release-1-0-0-authority` and accepted the
pending remediation/presentation in :doc:`../../concept-reviews/round-14`.
The canceled earlier candidate remains historical. This candidate is based on
``{result['revision']}`` plus the recorded worktree/source identity.

Actual executed scope
----------------------

* {counts['pytest.xml']} Python cases and {counts['node.xml']} JavaScript cases passed;
  zero failures, errors or skips. These are one full candidate run, not combined
  development passes. {len({i['case_id'] for i in mapped})} canonical procedures have new execution records.
* Windows, Python 3.13.17, Firefox/geckodriver and Node identities are retained in
  :download:`candidate.json <candidate.json>`. File and static HTTP transports,
  offline resource restrictions, Windows nested paths/retry, persistent details,
  classified rows and stable navigation are included.
* A fresh 30,000-Need/90,000-edge capacity fixture built in {build['seconds']:.2f}
  seconds. Each browser transport was measured three times; raw timings and
  process-tree memory observations are retained. No numeric performance budget
  is claimed because none is agreed.
* The exact wheel passed isolated offline installation/Sphinx usage under the
  main test environment and independently on Python 3.10.9. Python 3.10 version,
  installed-package identity and dependency consistency passed.
* Wheel and sdist come from the normal build frontend; the wheel is built from
  the sdist. Both exact archives, their SHA-256 checksums and member inventories
  are retained. All {len(runtime)} wheel runtime members match checkout inputs
  byte-for-byte. Source-level suites are not misrepresented as installed-wheel tests.
* Strict executable mapping, initial warnings-as-errors documentation, graph
  validation with required test coverage and source/published diagram links passed.
  Final staged documentation and evidence validation are recorded separately
  after consolidating these records.

Owner-accepted release deferrals
------------------------------------

Release-runner improvements, hosted CI confirmation, cryptographic attestation
and branch protections are deferred by the owner. :need:`STV_PR_012` remains
analyzed/partially verified, and its unrelated draft designs are unchanged.
These are owner-accepted nonblocking deferrals for v1.0.0. Repository
visibility is a separate setting and is not changed by this work.
Occurrence mode, touch and additional platform/browser qualification remain
later scope. Widget JavaScript parity is outside the static-detail contract.

The underlying runtime evidence is fresh. Criterion review closes the five
prior Windows-path partial dispositions: :need:`STV_SYS_003` (self-contained
file/HTTP use), :need:`STV_SYS_006` (cross-page, metadata/body/local media,
external fallback and original anchors), :need:`STV_SWR_015` (rendered details
and remote-resource fallback), :need:`STV_SWR_017` (offline classic assets), and
:need:`STV_SWR_018` (nested file/HTTP-prefix portable paths). The full set combines
the nested Windows/retry procedure, offline exploration, alternate-model rich
content/original navigation, transport-marker, persistent-details and component
URL/media checks. These five fields change to passed on actual full-run evidence;
acceptance and stakeholder verification remain independent. The initial
runner documentation build is a development build. The separate final staged
build supplies the prescribed publication tree without modifying the runner.

Retained supplementary evidence
--------------------------------

* :download:`Exact archive checksums <SHA256SUMS.txt>`
* :download:`Source archive member inventory <sdist-members.json>`
* :download:`Wheel member inventory <wheel-members.json>`
* :download:`Checkout/wheel equivalence <runtime-equivalence.json>`
* :download:`Supplement commands and times <supplement-commands.json>`
* :download:`Minimum-runtime installed identity <runtime310-identity.log>`
* :download:`Minimum-runtime Sphinx/dependency check <runtime310-host.log>`
* :download:`Preparation commit message <commit-message.txt>`
* :download:`Conditional tag template <tag-release.ps1.txt>`
* :download:`GitHub release notes <github-release-notes.md.txt>`

.. toctree::
   :maxdepth: 1

   cleanup-review
'''
(RECORD/'qualification.rst').write_text(text, encoding='utf-8')
with (RECORD/'index.rst').open('a', encoding='utf-8') as stream:
    stream.write('\nRelease assessment\n----------------------------\n\n.. toctree::\n   :maxdepth: 1\n\n   qualification\n')
message = '''Prepare the v1.0.0 release

    - Record owner acceptance so the current product can be released as v1.0.0.
    - Accept the scoped security remediation and final details presentation.
    - Set the canonical package version to 1.0.0 and retain fresh qualification evidence.
    - Keep release-runner improvements and hosted hardening explicitly deferred.
'''
(RECORD/'commit-message.txt').write_text(message, encoding='utf-8')
(RECORD/'tag-release.ps1.txt').write_text('# After the final preparation commit exists and all recorded gates pass:\n# Replace the placeholder with that exact commit hash.\ngit tag -a v1.0.0 <final-release-commit> -m "v1.0.0 release"\n', encoding='utf-8')
notes = f'''# v1.0.0

First official release of Sphinx Traceability View.

- Offline interactive Sphinx-Needs traceability views with shared graph identity,
  multiple starting nodes, project paging and interactive seed selection.
- Stable relationship navigation, classified test/evidence rows and a visible viewport boundary.
- Persistent per-view details with configurable capacity, folded metadata and original-object navigation.
- Hardened local detail resources, compact Windows asset paths, complete bundled notices,
  bounded source archives and clean documentation publication.

Install the attached wheel with Python 3.10 or newer. Maintainer documentation/test
tooling requires Python 3.11 or newer. Sphinx 8.1.3 and sphinx-needs 8.2.0 are pinned.
Preserve bundled third-party notices when redistributing generated HTML.

Validation: {counts['pytest.xml']} Python and {counts['node.xml']} JavaScript cases passed,
including Firefox file/HTTP and fresh 30,000-Need/90,000-edge capacity checks.
The exact release wheel also passed an isolated Python 3.10 install/Sphinx build.
[Qualification evidence](https://github.com/sysblacksmith/STV_sphinx-traceability-view/blob/v1.0.0/docs/test-execution/1.0.0-candidate-2/qualification.rst).
Archive hashes are in the attached SHA256SUMS.txt.

Known scope: occurrence mode, touch and additional platforms/browsers remain deferred;
numeric latency/memory budgets are unagreed. Hosted CI/provenance, branch protection
and release-runner improvements are owner-accepted follow-up work for v1.0.0.
Cryptographic attestation is not included.
'''
(RECORD/'github-release-notes.md.txt').write_text(notes, encoding='utf-8')
path = ROOT/'docs/maturity.rst'
text = path.read_text(encoding='utf-8').replace('New full local qualification is required; no completed release is claimed yet.',
    'Fresh local candidate suites passed; final consolidation checks and the\nrelease disposition are in :doc:`test-execution/1.0.0-candidate-2/qualification`.\nNo completed hosted release is inferred from local qualification.')
path.write_text(text, encoding='utf-8')
print('Consolidated exact candidate evidence and release handover drafts.')
