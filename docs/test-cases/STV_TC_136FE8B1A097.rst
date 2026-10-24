failed finalization retains pending page and previous assets
============================================================

.. test_case:: failed finalization retains pending page and previous assets
   :id: STV_TC_136FE8B1A097
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_failed_finalization_retains_pending_page_and_previous_assets
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SHR_027, STV_SWR_015, STV_SWR_017, STV_SWR_027
   :executed_by: STV_TE_2FE927B84AC573F5, STV_TE_5428B57695F57556
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_failed_finalization_retains_pending_page_and_previous_assets``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_failed_finalization_retains_pending_page_and_previous_assets" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_failed_finalization_retains_pending_page_and_previous_assets(tmp_path):
          from types import SimpleNamespace
          from sphinx.errors import SphinxError
          from sphinx_traceability_view import finish
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

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
