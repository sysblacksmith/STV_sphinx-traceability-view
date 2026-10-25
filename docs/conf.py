"""Project documentation using a versioned local requirements method."""
from importlib import import_module
from copy import deepcopy
import os
from pathlib import Path
import sys
import runpy

project = "STV Sphinx Traceability View"
release = runpy.run_path(str(Path(__file__).resolve().parents[1] / "src/sphinx_traceability_view/_version.py"))["__version__"]
version = ".".join(release.split(".")[:2])
root_doc = "index"
exclude_patterns = ["test-scripts/fixtures/**", "_build", "test-execution/0.1.0-candidate-1/index.rst"]

# All engineering tooling is versioned in this checkout.
method_dir = Path(__file__).resolve().parents[1] / 'tools' / 'method'
sys.path.insert(0, str(method_dir / 'tooling'))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
traceability_model = import_module('traceability_model')

sys.path.insert(0, str(Path(__file__).resolve().parent))
html_copy_source = False
html_show_sourcelink = False
extensions = ["_publication", "sphinx_needs", "sphinx_rtd_theme", "myst_parser", "status_charts", "need_controls", "method_version", "sphinx_traceability_view"]
needs_types = traceability_model.NEEDS_TYPES
needs_links = traceability_model.NEEDS_LINKS
needs_fields = traceability_model.NEEDS_FIELDS
needs_build_json = True
# Project evidence rows; the reusable default/legacy models remain available.
traceability_view_model = deepcopy(import_module('sphinx_traceability_view.model').DEFAULT)
traceability_view_model['levels'] = [
    'stakeholder', 'system', 'system_tests', 'system_executions', 'system_arch',
    'software', 'software_tests', 'software_executions', 'software_arch',
    'unclassified_tests', 'problems', 'changes',
]
traceability_view_model['types']['problem_report'] = {'level': 'problems'}
traceability_view_model['types']['change_request'] = {'level': 'changes'}
traceability_view_model['types']['test_case'] = {
    'levels_by_tag': {'test_system': 'system_tests', 'test_software': 'software_tests'},
    'fallback_level': 'unclassified_tests',
}
traceability_view_model['types']['test_execution'] = {
    'level_from': {'relation': 'executed_by', 'direction': 'incoming',
                   'levels': {'system_tests': 'system_executions', 'software_tests': 'software_executions'}},
    'fallback_level': 'unclassified_tests',
}
html_theme = "sphinx_rtd_theme"
html_static_path = [str(method_dir / "static")]
html_css_files = ["wide-layout.css"]
# Publish linked Draw.io SVGs as standalone interactive documents.
html_extra_path = ["architecture/diagrams"]

