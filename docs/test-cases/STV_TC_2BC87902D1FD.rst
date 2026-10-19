clear facing ports and fan-in avoid outer detours
=================================================

.. test_case:: clear facing ports and fan-in avoid outer detours
   :id: STV_TC_2BC87902D1FD
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/layout.test.js :: frontend/test/layout.test.js :: STV_SWR_053: clear facing ports and fan-in avoid outer detours
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_050, STV_SWR_053
   :executed_by: STV_TE_2DAA1D42C7C13397, STV_TE_F3BAE266CA6E561A
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/layout.test.js :: STV_SWR_053: clear facing ports and fan-in avoid outer detours``.

   **Invocation:** ``node --test "frontend/test/layout.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_053: clear facing ports and fan-in avoid outer detours', async()=> {
        const graph={model:{levels:['parent','child'],types:{p:{level:'parent'},c:{level:'child'}}},
          objects:{P:{type:'p'},A:{type:'c'},B:{type:'c'},C:{type:'c'}}};
        const result=await compute(graph,{ids:['P','A','B','C'],edges:[['A','r','P'],['B','r','P'],['P','r','C']]},new Map());
        for(const edge of result.edges) {
          assert.equal(edge.points.length,2);
          const a=result.nodes.get(edge.source),b=result.nodes.get(edge.target);
          if(a.y>b.y)assert.deepEqual(edge.points,[[a.x+140,a.y],[b.x+140,b.y+b.height]]);
          else assert.deepEqual(edge.points,[[a.x+140,a.y+a.height],[b.x+140,b.y]]);
        }
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
