invalid model
=============

.. test_case:: invalid model
   :id: STV_TC_5D3C07D3C5DE
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_model.py :: tests/test_model.py::test_invalid_model[change2-types]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_2D9B53D73A5690DD, STV_TE_0AA4273D7D0FBA0D
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_model.py::test_invalid_model[change2-types]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_model.py::test_invalid_model[change2-types]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_model(change, path):
          with pytest.raises(ValueError, match=path):
              normalize(TYPES, LINKS, dict(MODEL, **change))

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
