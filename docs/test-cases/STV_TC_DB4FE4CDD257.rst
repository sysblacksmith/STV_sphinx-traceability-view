host owns broken trace failure
==============================

.. test_case:: host owns broken trace failure
   :id: STV_TC_DB4FE4CDD257
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_build.py :: docs/test-scripts/test_build.py::test_host_owns_broken_trace_failure
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_027, STV_SHR_028, STV_SWR_027, STV_SWR_028
   :executed_by: STV_TE_89DB9F0DFA6EBD36, STV_TE_DC50B0D40735701B
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_build.py::test_host_owns_broken_trace_failure``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_build.py::test_host_owns_broken_trace_failure" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_host_owns_broken_trace_failure(tmp_path):
          source = tmp_path / "source"
          shutil.copytree(FIXTURE, source)
          with (source / "conf.py").open("a", encoding="utf-8") as stream:
              stream.write('\nneeds_report_dead_links = True\n')
          path = source / "requirements.rst"
          path.write_text(path.read_text(encoding="utf-8").replace(":traces: LEAF_B", ":traces: MISSING_A"), encoding="utf-8")
          output = tmp_path / "html"
          result = build(source, output)
          assert result.returncode != 0
          assert "MISSING_A" in result.stderr
          assert "STV_PENDING" not in (output / "index.html").read_text(encoding="utf-8")
          data = manifest(output)
          assert ["ROOT_A", "traces", "MISSING_A"] in data["edges"]
          assert "MISSING_A" not in data["objects"]

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
