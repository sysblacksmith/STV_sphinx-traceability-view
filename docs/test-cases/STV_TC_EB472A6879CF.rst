local suggestions match IDs and titles and bound results
========================================================

.. test_case:: local suggestions match IDs and titles and bound results
   :id: STV_TC_EB472A6879CF
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/seeds.test.js :: frontend/test/seeds.test.js :: STV_SWR_057: local suggestions match IDs and titles and bound results
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_053, STV_SWR_057
   :executed_by: STV_TE_8B87A6B6D7C31F3B, STV_TE_E31F5DC01B22D239
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/seeds.test.js :: STV_SWR_057: local suggestions match IDs and titles and bound results``.

   **Invocation:** ``node --test "frontend/test/seeds.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_057: local suggestions match IDs and titles and bound results',()=>{
       const catalog=seedCatalog({objects:Object.fromEntries(Array.from({length:15},(_,i)=>['ID_'+i,{title:'Example '+i}]))});
       assert.equal(seedMatches(catalog,' example ').total,15);
       assert.equal(seedMatches(catalog,'example').items.length,10);
       assert.equal(seedMatches(catalog,'id_14').items[0].id,'ID_14');
       assert.equal(seedMatches(catalog,'').total,0);
       assert.equal(seedMatches(catalog,'hidden').total,0);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
