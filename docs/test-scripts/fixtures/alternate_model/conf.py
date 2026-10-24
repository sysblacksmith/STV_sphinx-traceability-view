project = "Alternate host schema"
extensions = ["sphinx_traceability_view"]
needs_types = [
    {"directive": name, "title": name.title(), "prefix": name.upper()+"_", "color": color, "style": "node"}
    for name, color in [("goal", "#ddeeff"), ("hardware", "#eeeedd"), ("system", "#eeeeff"),
                        ("software", "#ddffee"), ("component", "#ffeedd"), ("check", "#ffffff")]
]
needs_links = {"traces": {"incoming": "Traced from", "outgoing": "Traces to"}}
needs_fields = {"owner": {"description": "Fixture owner", "schema": {"type": "string"}}}
traceability_view_model = {
    "levels": ["goals", "hardware", "system", "software", "modules"],
    "types": {"goal": {"level": "goals", "role": "stakeholder"},
              "hardware": {"level": "hardware"}, "system": {"level": "system"},
              "software": {"level": "software"}, "component": {"level": "modules"}, "check": {"role": "test"}},
    "accepted_statuses": ["approved", ""],
}
html_theme = "alabaster"
html_extra_path = ["pixel.svg"]


def external(app, env, docnames):
    from sphinx_needs.api import add_external_need
    add_external_need(app, "goal", id="EXTERNAL_A", title="External goal", status="approved",
                      external_url="https://example.invalid/original.html#EXTERNAL_A", owner="External owner")


def setup(app):
    app.connect("env-before-read-docs", external, priority=900)
