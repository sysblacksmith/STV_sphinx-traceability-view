"""Adapt retained supplemental procedures to this candidate without changing history."""
from pathlib import Path

HERE = Path(__file__).resolve().parent
records = HERE.parent
text = (records / '1.1.0-candidate-2/export-capacity.py').read_text()
text = text.replace('1.1.0-candidate-2', HERE.name)
text = text.replace('docs/_build/release-benchmark/1.1.0-candidate-1/html',
                    'docs/_build/release-benchmark/' + HERE.name + '/html')
text = text.replace("out=root/'docs/_build/export-capacity-1.1.0-fixed'", "out=record/'export-capacity'")
text = text.replace("fixture='Unchanged candidate-1 host data in temporary copy with exact candidate-2 runtime bundle'",
                    "fixture='Fresh 1.2.0 capacity host in a temporary copy with the exact candidate runtime bundle'")
(HERE / 'export-capacity.py').write_text(text)
(HERE / 'check-hover-export.py').write_text((records / '1.1.0-candidate-3/check-hover-export.py').read_text())
text = (records / '1.1.0-candidate-4/check-runtime310.py').read_text().replace('1.1.0', '1.2.0')
(HERE / 'check-runtime310.py').write_text(text)
