"""Adapt the reviewed publisher without altering qualified inputs."""
from pathlib import Path
ROOT = Path.cwd()
HERE = ROOT/'docs/_build/release-publication'
text = (ROOT/'docs/test-execution/1.1.0-candidate-4/publish-release.py').read_text().replace('1.1.0', '1.2.0')
text = text.replace('HERE=Path(__file__).resolve().parent', "HERE=Path.cwd()/'docs/test-execution/1.2.0-candidate-1'")
text = text.replace("notes=(HERE/'github-release-notes.md.txt').read_text(encoding='utf-8')", "notes=(ROOT/'docs/_build/release-publication/release-notes.md').read_text(encoding='utf-8')")
(HERE/'publish.py').write_text(text)
notes = (ROOT/'docs/test-execution/1.2.0-candidate-1/github-release-notes.md.txt').read_text()
(HERE/'release-notes.md').write_text(notes.split('\nAttach the exact qualified', 1)[0].strip()+'\n')
