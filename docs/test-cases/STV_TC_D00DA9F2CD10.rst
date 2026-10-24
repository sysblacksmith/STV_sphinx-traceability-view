hidden parts external and missing targets
=========================================

.. test_case:: hidden parts external and missing targets
   :id: STV_TC_D00DA9F2CD10
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_graph.py :: docs/test-scripts/test_graph.py::test_hidden_parts_external_and_missing_targets
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_013, STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_026, STV_SHR_027, STV_SHR_047, STV_SHR_048, STV_SWR_013, STV_SWR_027, STV_SWR_047, STV_SWR_048
   :executed_by: STV_TE_23341FA7B89F3170, STV_TE_CCFEC1B7BFDE5043
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_graph.py::test_hidden_parts_external_and_missing_targets``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_graph.py::test_hidden_parts_external_and_missing_targets" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_hidden_parts_external_and_missing_targets():
          model = normalize(TYPES, LINKS, MODEL)
          base = dict(type="goal", title="Title", status="accepted", docname="nested/requirements")
          needs = Needs([
              dict(base, id="A", verifies=["B", "HIDDEN", "MISSING", "HIDDEN.part", "A.part"]),
              dict(base, id="B", is_external=True, docname=None, external_url="https://example.org/B", constraints_results={'rule':{'passed':True}}),
              dict(base, id="HIDDEN", hide=True),
              dict(base, id="part", id_complete="HIDDEN.part", id_parent="HIDDEN", is_part=True),
              dict(base, id="part", id_complete="A.part", id_parent="A", is_part=True),
          ])
          def uri(docname):
              assert docname is not None
              return docname + ".html"
          graph, hidden = snapshot(needs, model, uri, "Project")
          assert set(graph["objects"]) == {"A", "A.part", "B"}
          assert hidden == {"HIDDEN", "HIDDEN.part"}
          assert graph["entries"] == ["A", "B"]
          assert graph["objects"]["B"]["url"] == "https://example.org/B"
          assert graph["objects"]["B"]["metadata"]['constraints_results']=={'rule':{'passed':True}}
          assert graph["objects"]["A.part"]["url"].endswith("#A.part")
          assert graph["adjacency"]["A"]["outgoing"]["verifies"] == ["A.part", "B", "MISSING"]
          assert graph["adjacency"]["B"]["incoming"]["verifies"] == ["A"]
          assert "MISSING" not in graph["objects"]

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
