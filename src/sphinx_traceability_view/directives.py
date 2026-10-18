"""Serializable directive records and a small page-local initialization node."""
import json
from hashlib import sha256
from html import escape
from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class ViewNode(nodes.General, nodes.Element):
    pass


class TraceabilityView(SphinxDirective):
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = False

    def run(self):
        seeds = list(dict.fromkeys(self.arguments[0].split())) if self.arguments else []
        if len(seeds) > 200:
            raise self.error("traceability-view: at most 200 distinct starting IDs are permitted")
        records = getattr(self.env, "stv_views", {})
        entries = records.setdefault(self.env.docname, [])
        document_key = sha256(self.env.docname.encode("utf-8")).hexdigest()
        record = {"id": f"stv-{document_key}-{len(entries)}", "seeds": seeds,
                  "source": self.get_source_info()[0], "line": self.lineno}
        entries.append(record)
        self.env.stv_views = records
        return [ViewNode("", **record)]


def visit_html(translator, node):
    data = escape(json.dumps(node["seeds"]), quote=True)
    translator.body.append(f'<section class="stv-view" id="{escape(node["id"], quote=True)}" data-stv-seeds="{data}" data-stv-build="STV_PENDING" aria-label="Interactive traceability view"></section>')
    raise nodes.SkipNode
