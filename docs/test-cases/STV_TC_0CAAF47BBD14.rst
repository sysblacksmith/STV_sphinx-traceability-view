semantic bands and shared test lane
===================================

.. test_case:: semantic bands and shared test lane
   :id: STV_TC_0CAAF47BBD14
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: frontend/test/layout.test.js :: frontend/test/layout.test.js :: STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_009, STV_SHR_010, STV_SHR_011, STV_SHR_012, STV_SHR_037, STV_SHR_050, STV_SWR_009, STV_SWR_010, STV_SWR_011, STV_SWR_012, STV_SWR_037, STV_SWR_053
   :executed_by: STV_TE_22893BEF95C2D437, STV_TE_7BEDB835EBAB2E01
   :last_result: passed

   **Level:** JavaScript unit/state/geometry.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/test/layout.test.js :: STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane``.

   **Invocation:** ``node --test "frontend/test/layout.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane', async()=> {
        const model={levels:['stakeholder','hardware','system_arch','software','software_arch'],types:{
          goal:{level:'stakeholder'},hardware:{level:'hardware'},system:{level:'system_arch'},software:{level:'software'},module:{level:'software_arch'},test:{role:'test'}}};
        const objects=Object.fromEntries(['goal','hardware','system','software','module','test'].map(type=>[type,{type}]));
        const edges=[['software','r','goal'],['test','r','goal'],['test','r','software'],['module','r','module'],['test','r','test']];
        const result=await compute({objects,model,entries:['goal']},{ids:Object.keys(objects),edges,project:true},new Map(Object.keys(objects).map(id=>[key(id),160])));
        let previous=result.nodes.get(JSON.stringify(['project']));
        for(const id of ['goal','hardware','system','software','module']) {const node=result.nodes.get(key(id));assert.ok(node.y>previous.y+previous.height);previous=node;}
        const testNode=result.nodes.get(key('test'));
        const loop=result.edges.find(e=>e.edge[0]==='test'&&e.edge[2]==='test');
        assert.notDeepEqual(loop.points[0],loop.points.at(-1),'self-link needs distinct ports');
        assert.ok(new Set(loop.points.map(p=>p[1])).size>1,'self-link needs a visible loop');
        assert.ok(testNode.x>=Math.max(...['goal','hardware','system','software','module'].map(id=>result.nodes.get(key(id)).x+280))+96);
        for(const edge of result.edges) {
          const a=result.nodes.get(edge.source),b=result.nodes.get(edge.target);
          const onBoundary=(p,n)=>((p[0]===n.x||p[0]===n.x+n.width)&&p[1]>=n.y&&p[1]<=n.y+n.height)||((p[1]===n.y||p[1]===n.y+n.height)&&p[0]>=n.x&&p[0]<=n.x+n.width);
          assert.ok(onBoundary(edge.points[0],a));assert.ok(onBoundary(edge.points.at(-1),b));
          for(let i=1;i<edge.points.length;i++)for(const n of result.nodes.values()) {
            const p=edge.points[i-1],q=edge.points[i];
            // Independent sampling also handles diagonal direct routes.
            const crosses=Array.from({length:999},(_,j)=>(j+1)/1000).some(t=> {
              const x=p[0]+t*(q[0]-p[0]),y=p[1]+t*(q[1]-p[1]);
              return x>n.x&&x<n.x+n.width&&y>n.y&&y<n.y+n.height;
            });
            assert.equal(crosses,false,'edge cannot pass through a node');
          }
        }
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
