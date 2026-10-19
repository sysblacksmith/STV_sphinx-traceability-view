invalid seed source location
============================

.. test_case:: invalid seed source location
   :id: STV_TC_6C7A64E533AC
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_build.py :: tests/test_build.py::test_invalid_seed_source_location[ROOT_A UNKNOWN]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_026, STV_SHR_047, STV_SHR_048, STV_SWR_026, STV_SWR_048, STV_SYS_001
   :executed_by: STV_TE_97AA7EB41C45F077, STV_TE_39301A83113F7C7D
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_build.py::test_invalid_seed_source_location[ROOT_A UNKNOWN]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_build.py::test_invalid_seed_source_location[ROOT_A UNKNOWN]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_seed_source_location(tmp_path, seed):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          (source / "index.rst").write_text(f"Invalid\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view:: {seed}\n", encoding="utf-8")
          with (source / "requirements.rst").open("a", encoding="utf-8") as stream:
              stream.write("\n.. shr:: Hidden\n   :id: HIDDEN_A\n   :hide:\n")
          result = build(source, tmp_path / "html")
          assert result.returncode != 0
          assert "index.rst:8" in result.stderr
          assert "unknown or hidden starting ID" in result.stderr

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
