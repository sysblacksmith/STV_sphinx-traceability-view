"""Project documentation using the live shared requirements method."""
from importlib import import_module
from copy import deepcopy
import os
from pathlib import Path
import sys

project = "STV Sphinx Traceability View"
version = release = "0.1"
root_doc = "index"
exclude_patterns = ["_build", "test-execution/0.1.0-candidate-1/index.rst"]

# Select the shared reverse-engineering skill without storing a machine path.
configured = os.environ.get("REQUIREMENTS_SKILL_DIR")
candidates = [Path(configured)] if configured else [
    parent / "#agents" / "skills" / "reverse-engineer-requirements"
    for parent in Path(__file__).resolve().parents
] + [Path.home() / ".agents" / "skills" / "reverse-engineer-requirements"]
skill_dir = next((p for p in candidates if
                 (p / "scripts" / "traceability_model.py").is_file()
                 and (p.parent.parent / "method.md").is_file()), None)
if skill_dir is None:
    raise RuntimeError("Set REQUIREMENTS_SKILL_DIR to the shared reverse-engineer-requirements skill directory (with its central method.md).")

sys.path.insert(0, str(skill_dir / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
# The selected shared skill is resolved at runtime, outside this workspace.
traceability_model = import_module("traceability_model")

extensions = ["sphinx_needs", "sphinx_rtd_theme", "myst_parser", "status_charts", "sphinx_traceability_view"]
needs_types = traceability_model.NEEDS_TYPES
needs_links = traceability_model.NEEDS_LINKS
needs_fields = traceability_model.NEEDS_FIELDS
needs_build_json = True
# Reports extend this documentation's host schema. The extension's default
# five-level preset remains unchanged for existing consumer projects.
traceability_view_model = deepcopy(import_module('sphinx_traceability_view.model').DEFAULT)
traceability_view_model['levels'].append('problems')
traceability_view_model['types']['problem_report'] = {'level': 'problems'}
html_theme = "sphinx_rtd_theme"
html_static_path = [str(skill_dir / "assets" / "sphinx" / "_static")]
html_css_files = ["wide-layout.css"]
# Publish linked Draw.io SVGs as standalone interactive documents.
html_extra_path = ["architecture/diagrams"]


def include_shared_method(app, docname, source):
    if docname == "method":
        master = skill_dir.parent.parent / "method.md"
        relative = os.path.relpath(master, app.srcdir).replace(os.sep, "/")
        source[0] = source[0].replace("@SHARED_REQUIREMENTS_METHOD@", relative)


def setup(app):
    app.connect("source-read", include_shared_method)
