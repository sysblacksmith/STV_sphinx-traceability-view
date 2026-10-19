parent and project center over five visible children
====================================================

.. test_case:: parent and project center over five visible children
   :id: STV_TC_08AC936D55F9
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/layout.test.js :: frontend/test/layout.test.js :: STV_SWR_056: parent and project center over five visible children
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_6F0E729E437E98D5, STV_TE_CBC21862BB4E7279
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/layout.test.js :: STV_SWR_056: parent and project center over five visible children``.

   **Invocation:** ``node --test "frontend/test/layout.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_056: parent and project center over five visible children',async()=>{
       const ids=['P','A','B','C','D','E'];
       const graph={model:{levels:['parent','child'],types:{p:{level:'parent'},c:{level:'child'}}},objects:Object.fromEntries(ids.map(id=>[id,{type:id==='P'?'p':'c'}]))};
       const result=await compute(graph,{ids,edges:ids.slice(1).map(id=>[id,'r','P']),project:true,entries:['P']},new Map());
       const parent=result.nodes.get(key('P')),children=ids.slice(1).map(id=>result.nodes.get(key(id)));
       const middle=(Math.min(...children.map(n=>n.x))+Math.max(...children.map(n=>n.x+n.width)))/2;
       assert.equal(parent.x+parent.width/2,middle);
       const project=result.nodes.get(JSON.stringify(['project']));assert.equal(project.x,parent.x);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
