199/200/201 atomic capacity
===========================

.. test_case:: 199/200/201 atomic capacity
   :id: STV_TC_6FE4CFC63C95
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/state.test.js :: frontend/test/state.test.js :: STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_005, STV_SHR_043, STV_SHR_044, STV_SWR_005, STV_SWR_043, STV_SWR_044
   :executed_by: STV_TE_C6A6C8EBC162B1F5, STV_TE_DCC7C845C33BEC31
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/state.test.js :: STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity``.

   **Invocation:** ``node --test "frontend/test/state.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity', () => {
        for (const size of [199,200,201]) {
          const g = graph(Array.from({length:size-1},(_,i)=>['A','r',String(i)]));
          const s = initial(['A']), result = transition(g,s,{type:'group',id:'A',relation:'r',direction:'outgoing'});
          if (size <= 200) assert.equal(result.graph.ids.length,size);
          else { assert.equal(result.state,s); assert.match(result.error,/200-node/); assert.equal(s.expanded.size,0); }
        }
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
