"""Status charts with readable fonts and consistent count/percentage legends."""
from collections import Counter
from hashlib import sha256
from traceability_model import NEEDS_STATUSES_BY_TYPE

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx_needs.data import SphinxNeedsData
from sphinx_needs.utils import save_matplotlib_figure


class StatusPie(nodes.General, nodes.Element):
    pass


class StatusPieDirective(SphinxDirective):
    required_arguments = 1
    option_spec = {'tag': directives.unchanged_required}

    def run(self):
        kind = self.arguments[0]
        if kind not in NEEDS_STATUSES_BY_TYPE:
            raise self.error(f'Unsupported status chart type: {kind}')
        node = StatusPie(kind=kind, tag=self.options.get('tag'))
        self.set_source_info(node)
        return [node]


def render_status_charts(app, doctree, docname):
    charts = list(doctree.findall(StatusPie))
    if not charts:
        return
    import matplotlib
    matplotlib.use('Agg')
    from matplotlib import pyplot as plt

    needs = SphinxNeedsData(app.env).get_needs_view()
    palette = {'draft': '#E9AD42', 'reviewed': '#4C91C7', 'accepted': '#56A477',
               'new': '#E9AD42', 'analyzed': '#4C91C7', 'fixed': '#56A477'}
    for node in charts:
        kind = node['kind']
        tag = node.get('tag')
        statuses = NEEDS_STATUSES_BY_TYPE[kind]
        counts = Counter(need['status'] for need in needs.values()
                         if need['type'] == kind
                         and (tag is None or tag in need.get('tags', [])))
        total = sum(counts.values())
        if not total:
            node.replace_self(nodes.paragraph(text='No elements in this category.'))
            continue
        values = [counts[state] for state in statuses]
        active_palette = dict(palette, accepted='#4C91C7', implemented='#56A477') if kind == 'change_request' else palette
        colors = [active_palette.get(state, '#888888') for state in statuses]
        labels = [f'{state.capitalize()}: {counts[state]} ({100*counts[state]/total:.1f}%)'
                  for state in statuses]
        with plt.rc_context({'font.size': 16, 'svg.fonttype': 'none'}):
            fig, axes = plt.subplots(figsize=(6.4, 5.8))
            fig.subplots_adjust(left=0.06, right=0.94, top=0.98, bottom=0.27)
            try:
                wedges, _, _ = axes.pie(
                    values, colors=colors, startangle=90,
                    autopct=lambda pct: f'{pct:.1f}%' if pct >= 5 else '',
                    pctdistance=0.68,
                    textprops={'fontsize': 15, 'fontweight': 'bold'},
                    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5},
                )
                axes.set_aspect('equal')
                fig.legend(wedges, labels, loc='lower center', bbox_to_anchor=(0.5, 0.015),
                           frameon=False, fontsize=16)
                # Distinct tag populations must not overwrite each other's SVG.
                figure_name = f'status_{kind}'
                if tag is not None:
                    figure_name += '_' + sha256(tag.encode('utf-8')).hexdigest()
                image = save_matplotlib_figure(app, fig, figure_name, docname)
                image['alt'] = '; '.join(labels)
                image['classes'].append('status-pie-image')
                node.replace_self(image)
            finally:
                plt.close(fig)


def setup(app):
    app.add_directive('status-pie', StatusPieDirective)
    # Sphinx-Needs has collected and resolved its items before this callback.
    app.connect('doctree-resolved', render_status_charts, priority=600)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': False}

