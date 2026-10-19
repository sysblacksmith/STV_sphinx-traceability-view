reverse traversal has no depth cutoff
=====================================

.. test_case:: reverse traversal has no depth cutoff
   :id: STV_TC_07D369AD0A2F
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/state.test.js :: frontend/test/state.test.js :: STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_006, STV_SHR_013, STV_SWR_006, STV_SWR_013
   :executed_by: STV_TE_9AAE7A231EC567CE, STV_TE_0FC214543C57C70A
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/state.test.js :: STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff``.

   **Invocation:** ``node --test "frontend/test/state.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff', () => {
        const g = graph(Array.from({length:8},(_,i)=>[String(i),'r',String(i+1)]));
        let s=initial(['8']); for(let i=8;i>0;i--) s=toggle(g,s,String(i),'incoming');
        assert.equal(visible(g,s).ids.length,9); assert.equal(visible(g,s).edges.length,8);
        s=initial(['0']);for(let i=0;i<8;i++)s=toggle(g,s,String(i));
        assert.equal(visible(g,s).ids.length,9);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
