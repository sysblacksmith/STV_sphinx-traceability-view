incremental body change hidden and deleted objects
==================================================

.. test_case:: incremental body change hidden and deleted objects
   :id: STV_TC_D1A17B11B9C1
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_incremental_body_change_hidden_and_deleted_objects
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_015, STV_SHR_018, STV_SHR_026, STV_SHR_047, STV_SHR_048, STV_SWR_015, STV_SWR_018, STV_SWR_048
   :executed_by: STV_TE_A7840F205B45812E, STV_TE_1FEF2B44838D4155
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_incremental_body_change_hidden_and_deleted_objects``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_incremental_body_change_hidden_and_deleted_objects" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_incremental_body_change_hidden_and_deleted_objects(tmp_path):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          with (source / "requirements.rst").open("a", encoding="utf-8") as stream:
              stream.write('\n.. shr:: Initially visible\n   :id: HIDDEN_LATER\n')
          output = tmp_path / "html"
          assert build(source, output).returncode == 0
          old = manifest(output)
          path = source / "requirements.rst"
          path.write_text(path.read_text(encoding="utf-8").replace("formatted body", "changed rich body").replace(":id: HIDDEN_LATER", ":id: HIDDEN_LATER\n   :hide:"), encoding="utf-8")
          assert build(source, output).returncode == 0
          new = manifest(output)
          assert new["identity"] != old["identity"]
          assert new["details"]["ROOT_A"]["digest"] != old["details"]["ROOT_A"]["digest"]
          assert "HIDDEN_LATER" not in new["objects"]
          assert "HIDDEN_LATER" not in new["details"]
          assert build(source, output).returncode == 0
          assert manifest(output)["identity"] == new["identity"]

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
