host normalization
==================

.. test_case:: host normalization
   :id: STV_TC_287ABDA90FE3
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_model.py :: docs/test-scripts/test_model.py::test_host_normalization
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_030, STV_SHR_032, STV_SHR_036, STV_SHR_045, STV_SWR_014, STV_SWR_030, STV_SWR_032, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_A60F3752BE7FF7A8, STV_TE_10A7B4170F40F4B9
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_model.py::test_host_normalization``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_model.py::test_host_normalization" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_host_normalization():
          source = deepcopy(MODEL)
          model = normalize(TYPES, LINKS, source, True)
          assert source == MODEL
          assert model["types"]["goal"]["color"] == "#abc"
          assert model["types"]["case"]["color"]
          assert model["relations"]["verifies"]["incoming"] == "Verified by"
          assert model["accepted_statuses"] == ["accepted"]
          source["accepted_statuses"] = ["approved"]
          assert normalize(TYPES, LINKS, source)["accepted_statuses"] == ["approved"]
          assert normalize(list(reversed(TYPES)), LINKS, source)['types']['case']['color']==model['types']['case']['color']

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
