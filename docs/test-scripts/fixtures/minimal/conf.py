project = "STV <Example>"
extensions = ["sphinx_traceability_view"]
needs_types = [
    {"directive": "shr", "title": "Stakeholder", "prefix": "SH_", "color": "#ddeeff", "style": "node"},
    {"directive": "swr", "title": "Software", "prefix": "SW_", "color": "#eeffdd", "style": "node"},
]
needs_links = {"traces": {"incoming": "Traced by", "outgoing": "Traces"}}
traceability_view_model = {"levels": ["stakeholder", "software"], "types": {
    "shr": {"level": "stakeholder", "role": "stakeholder"}, "swr": {"level": "software"}}}
html_theme = "alabaster"
