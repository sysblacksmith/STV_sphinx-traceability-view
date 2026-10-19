upward controls precede neutral and downward controls regardless of authorship
==============================================================================

.. test_case:: upward controls precede neutral and downward controls regardless of authorship
   :id: STV_TC_B2EF591B7F1E
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/groups.test.js :: frontend/test/groups.test.js :: STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_051, STV_SWR_055
   :executed_by: STV_TE_11785768416ABA6F, STV_TE_E359F9744218B058
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/groups.test.js :: STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship``.

   **Invocation:** ``node --test "frontend/test/groups.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship',()=> {
        const graph={model:{levels:['upper','middle','lower'],types:{
          p:{level:'upper'},m:{level:'middle'},c:{level:'lower'},t:{role:'test'}}},
          objects:{P:{type:'p'},M:{type:'m'},C:{type:'c'},T:{type:'t'}},
          adjacency:{M:{outgoing:{down:['C'],mixed:['P','C'],side:['M'],test:['T'],missing:['X'],empty:[]},
            incoming:{up:['P'],down2:['C'],up2:['P']}}}};
        const before=JSON.stringify(graph);
        assert.deepEqual(orderedGroups(graph,'M').map(g=>g.relation),
          ['up','up2','mixed','side','test','missing','down','down2']);
        assert.equal(JSON.stringify(graph),before,'ordering must not mutate graph data');
        assert.deepEqual(orderedGroups(graph,'X'),[]);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
