competing parents do not displace a separate centered parent
============================================================

.. test_case:: competing parents do not displace a separate centered parent
   :id: STV_TC_2EE2AB9ECAE3
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/layout.test.js :: frontend/test/layout.test.js :: STV_SWR_056: competing parents do not displace a separate centered parent
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_9CD13938265B5C9A, STV_TE_9DE4CCD94806C011
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/layout.test.js :: STV_SWR_056: competing parents do not displace a separate centered parent``.

   **Invocation:** ``node --test "frontend/test/layout.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_056: competing parents do not displace a separate centered parent',async()=>{
       const objects={P:{type:'p'},Q:{type:'p'},R:{type:'p'},...Object.fromEntries(['A','B','C','D','E','F'].map(id=>[id,{type:'c'}]))};
       const graph={objects,model:{levels:['p','c'],types:{p:{level:'p'},c:{level:'c'}}}};
       const edges=[['P','r','A'],...['Q','R'].flatMap(p=>['B','C','D','E','F'].map(c=>[p,'r',c]))];
       const result=await compute(graph,{ids:Object.keys(objects),edges},new Map());
       const center=id=>result.nodes.get(key(id)).x+140;
       assert.equal(center('P'),center('A'),'a noncompeting parent can remain exactly centered');
       const desired=(Math.min(...['B','C','D','E','F'].map(center))+Math.max(...['B','C','D','E','F'].map(center)))/2;
       assert.equal((center('Q')+center('R'))/2,desired,'shared-parent displacement balances locally');
       assert.equal(Math.abs(center('Q')-center('R')),328);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
