"""Stage only release work; preserve the separate pending chart-request intake."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
def git(*args, **kwargs):
    return subprocess.run(['git',*args],cwd=ROOT,check=True,**kwargs)

paths = ['docs/concept-reviews/round-13.rst','docs/concept-reviews/round-14.rst',
    'docs/requirements-system.rst','docs/requirements-software.rst','docs/review.rst',
    'docs/sources.rst','docs/test-cases/system-tests.rst','docs/test-cases/software-tests.rst',
    'docs/test-execution/index.rst','src/sphinx_traceability_view/_version.py',
    RECORD.relative_to(ROOT).as_posix()]
git('add','--',*paths)
path = ROOT/'docs/maturity.rst'
text = path.read_text(encoding='utf-8')
text, count = re.subn(r'CR_015 dashboard chart request recorded\n-+\n\n.*?(?=\.\. _release-1-0-0-authority:)', '', text, count=1, flags=re.S)
assert count == 1, 'Expected the known separate chart intake block'
blob = git('hash-object','-w','--stdin',input=text.encode('utf-8'),capture_output=True).stdout.decode().strip()
git('update-index','--add','--cacheinfo','100644,'+blob+',docs/maturity.rst')
snapshot = ROOT/'docs/_build/release-source/1.0.0'
snapshot.mkdir(parents=True,exist_ok=False)
git('checkout-index','--all','--prefix='+snapshot.as_posix()+'/')
assert not (snapshot/'docs/change-requests/STV_CR_015_test-case-maturity-and-chart-size.rst').exists()
assert 'CR_015 dashboard chart request recorded' not in (snapshot/'docs/maturity.rst').read_text(encoding='utf-8')
print('Staged exact release files and exported the index for final documentation validation:',snapshot)
