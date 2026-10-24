"""Atomic finalization and prior-error ownership at the Sphinx boundary."""
import pytest

@pytest.mark.requirements('STV_SWR_015','STV_SWR_017','STV_SWR_027')
def test_failed_finalization_retains_pending_page_and_previous_assets(tmp_path):
    from types import SimpleNamespace
    from sphinx.errors import SphinxError
    from sphinx_traceability_view.directive.lifecycle import finish
    pending='<section data-stv-build="STV_PENDING"></section>'
    (tmp_path/'index.html').write_text(pending,encoding='utf-8')
    (tmp_path/'requirements.html').write_text('<p>Expected Need body missing</p>',encoding='utf-8')
    previous=tmp_path/'_static/stv/graph-old.js';previous.parent.mkdir(parents=True);previous.write_text('previous complete asset',encoding='utf-8')
    graph={'model':{'relations':{}},'objects':{'A':{'url':'requirements.html#A','external':False,'parent':None}}}
    app=SimpleNamespace(_stv_graph=graph,_stv_hidden=set(),outdir=str(tmp_path),env=SimpleNamespace(stv_views={'index':[{}]}))
    with pytest.raises(SphinxError,match='Rendered Need.*missing'):
        finish(app,None)
    assert (tmp_path/'index.html').read_text(encoding='utf-8')==pending
    assert previous.read_text(encoding='utf-8')=='previous complete asset'
    assert list(previous.parent.glob('graph-*.js'))==[previous]


@pytest.mark.requirements('STV_SWR_027')
def test_prior_fatal_exception_is_not_replaced_by_bundle_generation(tmp_path):
    from types import SimpleNamespace
    from sphinx_traceability_view.directive.lifecycle import finish
    page=tmp_path/'index.html';page.write_text('previous complete page',encoding='utf-8')
    app=SimpleNamespace(_stv_graph={},outdir=str(tmp_path))
    finish(app,RuntimeError('Earlier fatal failure'))
    assert page.read_text(encoding='utf-8')=='previous complete page'
    assert not (tmp_path/'_static').exists()
