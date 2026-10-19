cross-page targets do not acquire synthetic root edges
======================================================

.. test_case:: cross-page targets do not acquire synthetic root edges
   :id: STV_TC_AEF53EABA753
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/state.test.js :: frontend/test/state.test.js :: STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_94B6CEC834B13181, STV_TE_B25D7DAF9A7087F9
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/state.test.js :: STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges``.

   **Invocation:** ``node --test "frontend/test/state.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges',()=> {
        const g=graph([['000','r','050']],Array.from({length:51},(_,i)=>String(i).padStart(3,'0')));
        let s=initial();s=toggle(g,s,'000');
        const v=visible(g,s);assert.ok(v.ids.includes('050'));assert.ok(!v.entries.includes('050'));
        assert.equal(v.entries.length,5);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
