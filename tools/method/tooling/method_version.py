"""Render the imported method identity from its manifest at build time."""
import json
import re
from pathlib import Path
from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class MethodVersion(SphinxDirective):
    has_content = False

    def run(self):
        root = Path(__file__).resolve().parents[1]
        manifest = root / '.method-package.json'
        if not manifest.is_file():
            manifest = root.parent / 'manifest.json'
        self.env.note_dependency(str(manifest))
        try:
            version = json.loads(manifest.read_text(encoding='utf-8'))['version']
            if not isinstance(version, str) or not re.fullmatch(r'\d+\.\d+\.\d+', version):
                raise ValueError('invalid version')
        except (OSError, ValueError, KeyError, TypeError) as error:
            raise self.error(f'Cannot read method version from {manifest}: {error}')
        paragraph = nodes.paragraph(classes=['method-version'])
        paragraph += nodes.strong(text='Method version: ')
        paragraph += nodes.Text(version)
        return [paragraph]

def setup(app):
    app.add_directive('method-version', MethodVersion)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
