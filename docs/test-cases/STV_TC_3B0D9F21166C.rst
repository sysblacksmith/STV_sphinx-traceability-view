alternate host schema external metadata and parts
=================================================

.. test_case:: alternate host schema external metadata and parts
   :id: STV_TC_3B0D9F21166C
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_alternate_host_schema_external_metadata_and_parts
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_026, STV_SHR_036, STV_SHR_045, STV_SHR_047, STV_SHR_048, STV_SWR_014, STV_SWR_036, STV_SWR_045, STV_SWR_047, STV_SWR_048, STV_SYS_002
   :executed_by: STV_TE_19C8684FFE688A1D, STV_TE_CECCD71A1F7BD48C
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_alternate_host_schema_external_metadata_and_parts``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_alternate_host_schema_external_metadata_and_parts" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_alternate_host_schema_external_metadata_and_parts(tmp_path):
          result=build(FIXTURE.parent/'alternate_model',tmp_path)
          assert result.returncode==0,result.stdout+result.stderr
          data=manifest(tmp_path)
          assert data['model']['types']['hardware']['level']=='hardware'
          assert data['model']['relations']['traces']['outgoing']=='Traces to'
          assert data['objects']['EXTERNAL_A']['metadata']['owner']=='External owner'
          assert data['objects']['EXTERNAL_A']['docname'] is None
          assert 'GOAL_A.fragment' in data['objects']
          assert 'GOAL_A.fragment' not in data['entries']
          assert 'HIDDEN_A' not in data['objects']
          assert not any('HIDDEN_A' in edge for edge in data['edges'])

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
