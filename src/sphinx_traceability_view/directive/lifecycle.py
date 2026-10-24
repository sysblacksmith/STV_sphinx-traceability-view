"""Sphinx entry point; the host owns Needs collection and trace diagnostics."""
from copy import deepcopy
from hashlib import sha256
import shutil
from html import escape
from pathlib import Path
from sphinx.errors import SphinxError
from sphinx.util.osutil import relative_uri
from sphinx_needs.data import SphinxNeedsData
from .directives import TraceabilityView, ViewNode, visit_html
from .._version import __version__
from ..model import normalize, validate_details_limit, DETAILS_LIMIT_DEFAULT
from ..graph import snapshot
from ..detail_build import extract
from ..bundle import emit, atomic


def initialize(app):
    # The host later injects unused GitHub service types unconditionally. Validate
    # the author's schema plus types actually used by service-produced objects.
    app._stv_declared_types = deepcopy(app.config.needs_types)


def purge(app, env, docname):
    getattr(env, "stv_views", {}).pop(docname, None)


def outdated(app, env, added, changed, removed):
    return sorted(env.found_docs) if getattr(env, "stv_views", {}) else []


def prepare(app, builder):
    views = getattr(app.env, "stv_views", {})
    app._stv_graph = None
    if not any(views.values()):
        return
    if builder.name != "html":
        raise SphinxError("traceability-view supports only the html builder")
    records = [record for entries in views.values() for record in entries]
    location = f'{records[0]["source"]}:{records[0]["line"]}'
    try:
        details_limit = validate_details_limit(app.config.traceability_view_details_limit)
        needs = SphinxNeedsData(app.env).get_needs_view()
        declared = {t["directive"] for t in app._stv_declared_types}
        used = {n["type"] for n in needs.values()}
        host_types = [t for t in app.config.needs_types if t["directive"] in declared | used]
        model = normalize(host_types, app.config.needs_links,
                          app.config.traceability_view_model,
                          any(not r["seeds"] for r in records))
        graph, hidden = snapshot(needs, model,
                                 builder.get_target_uri, app.config.project)
        graph["details_limit"] = details_limit
        for record in records:
            for seed in record["seeds"]:
                if seed not in graph["objects"]:
                    raise SphinxError(f'{record["source"]}:{record["line"]}: traceability-view: unknown or hidden starting ID {seed!r}')
        app._stv_graph, app._stv_hidden = graph, hidden
    except ValueError as error:
        raise SphinxError(f"{location}: traceability-view: {error}") from error
    target = Path(app.outdir) / "_static" / "stv"
    target.mkdir(parents=True, exist_ok=True)
    for name in ("stv.js", "stv.css", "LICENSE.txt", "THIRD_PARTY_NOTICES.txt", "vendor/ELK-SOURCE.txt", "vendor/ELK-INVENTORY.json"):
        source = Path(__file__).parents[1] / "static" / name
        if not source.is_file():
            raise SphinxError(f"Missing packaged STV asset {name}; maintainers must build frontend assets")
        (target / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target / name)


def context(app, pagename, templatename, context, doctree):
    if not getattr(app.env, "stv_views", {}).get(pagename):
        return
    page = app.builder.get_target_uri(pagename)
    root = relative_uri(page, "index.html").removesuffix("index.html") or "./"
    static = Path(__file__).parents[1] / "static"
    css = escape(root + "_static/stv/stv.css?v=" + sha256((static / "stv.css").read_bytes()).hexdigest(), quote=True)
    runtime = escape(root + "_static/stv/stv.js?v=" + sha256((static / "stv.js").read_bytes()).hexdigest(), quote=True)
    context["metatags"] += f'<link rel="stylesheet" href="{css}"><script data-stv-graph src="STV_PENDING"></script><script defer src="{runtime}" data-stv-root="{escape(root, quote=True)}"></script>'


def finish(app, exception):
    graph = getattr(app, "_stv_graph", None)
    if graph is None or exception is not None:
        return
    output = Path(app.outdir)
    try:
        fragments = extract(graph, output, app._stv_hidden)
        identity, graph_path = emit(graph, fragments, output)
        for docname in getattr(app.env, "stv_views", {}):
            page = app.builder.get_target_uri(docname)
            path = output / page
            content = path.read_text(encoding="utf-8")
            content = content.replace('data-stv-build="STV_PENDING"', f'data-stv-build="{identity}"')
            content = content.replace('data-stv-graph src="STV_PENDING"', f'data-stv-graph src="{escape(relative_uri(page, graph_path), quote=True)}"')
            atomic(path, content)
    except (OSError, ValueError) as error:
        raise SphinxError(f"traceability-view bundle finalization failed: {error}") from error


def setup(app):
    app.setup_extension("sphinx_needs")
    app.add_config_value("traceability_view_model", None, "env", types=[dict, type(None)])
    app.add_config_value("traceability_view_details_limit", DETAILS_LIMIT_DEFAULT, "env", types=[int])
    app.add_directive("traceability-view", TraceabilityView)
    app.add_node(ViewNode, html=(visit_html, None))
    app.connect("builder-inited", initialize)
    app.connect("env-purge-doc", purge)
    app.connect("env-get-outdated", outdated)
    app.connect("write-started", prepare, priority=800)
    app.connect("html-page-context", context)
    app.connect("build-finished", finish, priority=900)
    return {"version": __version__, "parallel_read_safe": False, "parallel_write_safe": False}
