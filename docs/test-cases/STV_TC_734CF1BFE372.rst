external original url rejects executable or nonportable navigation
==================================================================

.. test_case:: external original url rejects executable or nonportable navigation
   :id: STV_TC_734CF1BFE372
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_graph.py :: docs/test-scripts/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_047
   :executed_by: STV_TE_BDAB8D43008687EA, STV_TE_6997C226C3551E52
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_external_original_url_rejects_executable_or_nonportable_navigation(url):
          model=normalize(TYPES,LINKS,MODEL)
          needs=Needs([dict(id='EXTERNAL',type='goal',is_external=True,external_url=url)])
          with pytest.raises(ValueError,match='EXTERNAL.*original documentation URL'):
              snapshot(needs,model,lambda name:name+'.html','Project')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
