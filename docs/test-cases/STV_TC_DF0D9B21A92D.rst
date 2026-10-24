host default directional labels are used
========================================

.. test_case:: host default directional labels are used
   :id: STV_TC_DF0D9B21A92D
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_host_default_directional_labels_are_used
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_045, STV_SWR_045
   :executed_by: STV_TE_379307EDD1A87108, STV_TE_45E5FFF9B4722E84
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_host_default_directional_labels_are_used``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_host_default_directional_labels_are_used" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_host_default_directional_labels_are_used(tmp_path):
          source=tmp_path/'source';shutil.copytree(FIXTURE,source)
          with (source/'conf.py').open('a',encoding='utf-8') as stream:
              stream.write('\nneeds_links={"traces":{}}\n')
          output=tmp_path/'html';result=build(source,output)
          assert result.returncode==0,result.stderr
          assert manifest(output)['model']['relations']['traces']=={'incoming':'traces incoming','outgoing':'traces'}

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
