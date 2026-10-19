invalid directional labels
==========================

.. test_case:: invalid directional labels
   :id: STV_TC_D31601FDD080
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_model.py :: tests/test_model.py::test_invalid_directional_labels[1]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SHR_045, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_1F3FC164F20CBC3B, STV_TE_BA7C0491342D931D
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_model.py::test_invalid_directional_labels[1]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_model.py::test_invalid_directional_labels[1]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_directional_labels(incoming):
          with pytest.raises(ValueError,match='needs_links.verifies'):
              normalize(TYPES,[dict(LINKS[0],incoming=incoming)],MODEL)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
