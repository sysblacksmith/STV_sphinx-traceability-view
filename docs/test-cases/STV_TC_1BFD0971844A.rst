replacement level mappings drive ordering without relation-name assumptions
===========================================================================

.. test_case:: replacement level mappings drive ordering without relation-name assumptions
   :id: STV_TC_1BFD0971844A
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/groups.test.js :: frontend/test/groups.test.js :: STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_051, STV_SWR_055
   :executed_by: STV_TE_9194AED2292281DA, STV_TE_53D40C67F7FFB70F
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/groups.test.js :: STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions``.

   **Invocation:** ``node --test "frontend/test/groups.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions',()=> {
        const graph={model:{levels:['hardware','software'],types:{h:{level:'hardware'},s:{level:'software'}}},
          objects:{A:{type:'s'},B:{type:'h'}},adjacency:{A:{outgoing:{custom:['B']},incoming:{same:['A']}}}};
        assert.deepEqual(orderedGroups(graph,'A').map(g=>g.relation),['custom','same']);
        graph.model.levels.reverse();
        assert.deepEqual(orderedGroups(graph,'A').map(g=>g.relation),['same','custom']);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
