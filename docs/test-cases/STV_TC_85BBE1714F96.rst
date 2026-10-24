invalid mapping has entry path and location
===========================================

.. test_case:: invalid mapping has entry path and location
   :id: STV_TC_85BBE1714F96
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_invalid_mapping_has_entry_path_and_location
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_25353B9B728085D0, STV_TE_386D5C547F786FC8
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_invalid_mapping_has_entry_path_and_location``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_invalid_mapping_has_entry_path_and_location" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_mapping_has_entry_path_and_location(tmp_path):
          source=tmp_path/'source';shutil.copytree(FIXTURE,source)
          with (source/'conf.py').open('a',encoding='utf-8') as stream:
              stream.write('\ntraceability_view_model["types"]["shr"]["level"]="unknown"\n')
          result=build(source,tmp_path/'html')
          assert result.returncode!=0
          assert 'index.rst:8' in result.stderr
          assert 'types.shr' in result.stderr

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
