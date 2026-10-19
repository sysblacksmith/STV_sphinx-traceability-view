shared children keep unique nodes and conflicting parents do not overlap
========================================================================

.. test_case:: shared children keep unique nodes and conflicting parents do not overlap
   :id: STV_TC_880A2E13BCE9
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/layout.test.js :: frontend/test/layout.test.js :: STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_E8DFFB544A7B6399, STV_TE_AF727DC17FAA905E
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/layout.test.js :: STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap``.

   **Invocation:** ``node --test "frontend/test/layout.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap',async()=>{
       const graph={model:{levels:['p','c'],types:{p:{level:'p'},c:{level:'c'}}},objects:{P:{type:'p'},Q:{type:'p'},A:{type:'c'}}};
       const result=await compute(graph,{ids:['P','Q','A'],edges:[['P','r','A'],['Q','r','A']]},new Map());
       const p=result.nodes.get(key('P')),q=result.nodes.get(key('Q'));
       assert.equal(result.nodes.size,3);assert.ok(Math.abs(p.x-q.x)>=328);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
