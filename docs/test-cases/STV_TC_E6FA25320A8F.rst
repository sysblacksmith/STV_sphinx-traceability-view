active embed urls are not retained as navigation
================================================

.. test_case:: active embed urls are not retained as navigation
   :id: STV_TC_E6FA25320A8F
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_details.py :: docs/test-scripts/test_details.py::test_active_embed_urls_are_not_retained_as_navigation
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_015, STV_SWR_017, STV_SWR_049
   :executed_by: STV_TE_03DA151E5608D061, STV_TE_0AD15AF696631D27
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_details.py::test_active_embed_urls_are_not_retained_as_navigation``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_details.py::test_active_embed_urls_are_not_retained_as_navigation" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_active_embed_urls_are_not_retained_as_navigation():
          markup='''<iframe src="data:text/html,&lt;script&gt;bad()&lt;/script&gt;"></iframe><script src="data:text/javascript,bad()"></script><object data="javascript:bad()"></object><img src="data:image/png;base64,AAAA">'''
          result=BeautifulSoup(transform(markup,'page.html',set()),'html.parser')
          assert not result.find_all(['iframe','script','object','a'])
          assert result.img['src']=='data:image/png;base64,AAAA'

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
