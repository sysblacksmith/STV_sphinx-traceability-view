page boundaries, root capacity and independent views
====================================================

.. test_case:: page boundaries, root capacity and independent views
   :id: STV_TC_0C2F9B7BE8A7
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/state.test.js :: frontend/test/state.test.js :: STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_043, STV_SHR_044, STV_SHR_047, STV_SWR_043, STV_SWR_044, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_E9F99C0B9172AA5A, STV_TE_F98D479E1C9FFFB9
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/state.test.js :: STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views``.

   **Invocation:** ``node --test "frontend/test/state.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views',()=> {
        for(const size of [0,1,5,6,199,200,201]) {
          const entries=Array.from({length:size},(_,i)=>String(i).padStart(3,'0')),g=graph([],entries),fresh=initial();
          const opened=transition(g,fresh,{type:'root'});
          if(!size){assert.equal(opened.state,fresh);assert.match(opened.error,/No stakeholder/);continue;}
          let s=fresh;const seen=[];
          for(let page=0;page<Math.ceil(size/5);page++) {s=transition(g,s,{type:'page',page}).state;seen.push(...visible(g,s).entries);assert.ok(visible(g,s).ids.length<=5);}
          assert.deepEqual(seen,entries);assert.equal(fresh.rootOpen,true);
          const rejected=transition(g,s,{type:'page',page:Math.ceil(size/5)});assert.equal(rejected.state,s);
        }
        for(const total of [199,200,201]) {
          const entries=['A'],g=graph(Array.from({length:total-2},(_,i)=>['A','r','child'+i]),entries);
          const s=initial();
          const result=transition(g,s,{type:'group',id:'A',relation:'r',direction:'outgoing'});
          if(total<=200)assert.equal(result.graph.ids.length+1,total);else assert.equal(result.state,s);
        }
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
