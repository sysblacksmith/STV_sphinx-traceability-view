Software test cases
===================

Canonical specifications at the software verification level. Each case retains
its own Need ID, requirement links and execution history. See :doc:`index`
for classification and evidence semantics.

.. needtable::
   :filter: type == 'test_case' and 'test_software' in tags
   :columns: id;title;status;verifies;last_result;executed_by

STV_TC_07D369AD0A2F: reverse traversal has no depth cutoff
----------------------------------------------------------

.. test_case:: reverse traversal has no depth cutoff
   :id: STV_TC_07D369AD0A2F
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_006, STV_SHR_013, STV_SWR_006, STV_SWR_013
   :executed_by: STV_TE_9AAE7A231EC567CE, STV_TE_0FC214543C57C70A
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/state/tests/state.test.js :: STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff``.

   **Invocation:** ``node --test "frontend/src/state/tests/state.test.js"``.

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

STV_TC_08AC936D55F9: parent and project center over five visible children
-------------------------------------------------------------------------

.. test_case:: parent and project center over five visible children
   :id: STV_TC_08AC936D55F9
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: parent and project center over five visible children
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_6F0E729E437E98D5, STV_TE_CBC21862BB4E7279
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/layout/tests/layout.test.js :: STV_SWR_056: parent and project center over five visible children``.

   **Invocation:** ``node --test "frontend/src/layout/tests/layout.test.js"``.

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

STV_TC_0C2F9B7BE8A7: page boundaries, root capacity and independent views
-------------------------------------------------------------------------

.. test_case:: page boundaries, root capacity and independent views
   :id: STV_TC_0C2F9B7BE8A7
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_043, STV_SHR_044, STV_SHR_047, STV_SWR_043, STV_SWR_044, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_E9F99C0B9172AA5A, STV_TE_F98D479E1C9FFFB9
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views``.

   **Invocation:** ``node --test "frontend/src/state/tests/state.test.js"``.

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

STV_TC_0CAAF47BBD14: semantic bands and shared test lane
--------------------------------------------------------

.. test_case:: semantic bands and shared test lane
   :id: STV_TC_0CAAF47BBD14
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_009, STV_SHR_010, STV_SHR_011, STV_SHR_012, STV_SHR_037, STV_SHR_050, STV_SWR_009, STV_SWR_010, STV_SWR_011, STV_SWR_012, STV_SWR_037, STV_SWR_053
   :executed_by: STV_TE_22893BEF95C2D437, STV_TE_7BEDB835EBAB2E01
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/layout/tests/layout.test.js :: STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane``.

   **Invocation:** ``node --test "frontend/src/layout/tests/layout.test.js"``.

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

STV_TC_11FDDB8E8864: external original url rejects executable or nonportable navigation
---------------------------------------------------------------------------------------

.. test_case:: external original url rejects executable or nonportable navigation
   :id: STV_TC_11FDDB8E8864
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/graph/tests/test_graph.py :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[javascript:bad()]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_047
   :executed_by: STV_TE_815863A689BE2AD9, STV_TE_94297309B20E6054
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[javascript:bad()]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[javascript:bad()]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_external_original_url_rejects_executable_or_nonportable_navigation(url):
          model=normalize(TYPES,LINKS,MODEL)
          needs=Needs([dict(id='EXTERNAL',type='goal',is_external=True,external_url=url)])
          with pytest.raises(ValueError,match='EXTERNAL.*original documentation URL'):
              snapshot(needs,model,lambda name:name+'.html','Project')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_156E45252AF4: self-loop terminates and collapse restores the only seed
-----------------------------------------------------------------------------

.. test_case:: self-loop terminates and collapse restores the only seed
   :id: STV_TC_156E45252AF4
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_024: self-loop terminates and collapse restores the only seed
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_024, STV_SWR_024
   :executed_by: STV_TE_BDF4F05162263B81, STV_TE_1F7FB1C9CC36B859
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/state/tests/state.test.js :: STV_SWR_024: self-loop terminates and collapse restores the only seed``.

   **Invocation:** ``node --test "frontend/src/state/tests/state.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_024: self-loop terminates and collapse restores the only seed',()=> {
        const g=graph([['A','r','A']]);let s=toggle(g,initial(['A']),'A');
        assert.deepEqual(visible(g,s).ids,['A']);assert.equal(visible(g,s).edges.length,1);
        s=toggle(g,s,'A');assert.equal(visible(g,s).edges.length,0);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_1BFD0971844A: replacement level mappings drive ordering without relation-name assumptions
------------------------------------------------------------------------------------------------

.. test_case:: replacement level mappings drive ordering without relation-name assumptions
   :id: STV_TC_1BFD0971844A
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/render/tests/groups.test.js :: frontend/src/render/tests/groups.test.js :: STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_051, STV_SWR_055
   :executed_by: STV_TE_9194AED2292281DA, STV_TE_53D40C67F7FFB70F
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/render/tests/groups.test.js :: STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions``.

   **Invocation:** ``node --test "frontend/src/render/tests/groups.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions',()=> {
        const graph={model:{levels:['hardware','software'],types:{h:{level:'hardware'},s:{level:'software'}}},
          objects:{A:{type:'s'},B:{type:'h'}},adjacency:{A:{outgoing:{custom:['B']},incoming:{same:['A']}}}};
        assert.deepEqual(orderedGroups(graph,'A').map(g=>g.relation),['custom','same']);
        graph.model.levels.reverse();
        assert.deepEqual(orderedGroups(graph,'A').map(g=>g.relation),['same','custom']);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_1E00212E164D: runtime reseeding is atomic and clears exploration
-----------------------------------------------------------------------

.. test_case:: runtime reseeding is atomic and clears exploration
   :id: STV_TC_1E00212E164D
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_057: runtime reseeding is atomic and clears exploration
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_053, STV_SWR_057
   :executed_by: STV_TE_AEF4AE7CB966E22D, STV_TE_221D15B62302934C
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/state/tests/state.test.js :: STV_SWR_057: runtime reseeding is atomic and clears exploration``.

   **Invocation:** ``node --test "frontend/src/state/tests/state.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_057: runtime reseeding is atomic and clears exploration',()=>{
       const g=graph([['A','r','B']],['A','B']);g.objects={A:{},B:{}};
       let s=toggle(g,initial(),'A');assert.equal(transition(g,s,{type:'seed',id:'unknown'}).state,s);
       s=transition(g,s,{type:'seed',id:' B '}).state;assert.deepEqual(visible(g,s).ids,['B']);assert.equal(s.expanded.size,0);
       s=transition(g,s,{type:'overview'}).state;assert.equal(s.page,0);assert.deepEqual(visible(g,s).entries,['A','B']);
       });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_287ABDA90FE3: host normalization
---------------------------------------

.. test_case:: host normalization
   :id: STV_TC_287ABDA90FE3
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_host_normalization
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_030, STV_SHR_032, STV_SHR_036, STV_SHR_045, STV_SWR_014, STV_SWR_030, STV_SWR_032, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_A60F3752BE7FF7A8, STV_TE_10A7B4170F40F4B9
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/model/tests/test_model.py::test_host_normalization``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/model/tests/test_model.py::test_host_normalization" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_host_normalization():
          source = deepcopy(MODEL)
          model = normalize(TYPES, LINKS, source, True)
          assert source == MODEL
          assert model["types"]["goal"]["color"] == "#abc"
          assert model["types"]["case"]["color"]
          assert model["relations"]["verifies"]["incoming"] == "Verified by"
          assert model["accepted_statuses"] == ["accepted"]
          source["accepted_statuses"] = ["approved"]
          assert normalize(TYPES, LINKS, source)["accepted_statuses"] == ["approved"]
          assert normalize(list(reversed(TYPES)), LINKS, source)['types']['case']['color']==model['types']['case']['color']

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_2BC87902D1FD: clear facing ports and fan-in avoid outer detours
----------------------------------------------------------------------

.. test_case:: clear facing ports and fan-in avoid outer detours
   :id: STV_TC_2BC87902D1FD
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_053: clear facing ports and fan-in avoid outer detours
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_050, STV_SWR_053
   :executed_by: STV_TE_2DAA1D42C7C13397, STV_TE_F3BAE266CA6E561A
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/layout/tests/layout.test.js :: STV_SWR_053: clear facing ports and fan-in avoid outer detours``.

   **Invocation:** ``node --test "frontend/src/layout/tests/layout.test.js"``.

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

STV_TC_2EE2AB9ECAE3: competing parents do not displace a separate centered parent
---------------------------------------------------------------------------------

.. test_case:: competing parents do not displace a separate centered parent
   :id: STV_TC_2EE2AB9ECAE3
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: competing parents do not displace a separate centered parent
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_9CD13938265B5C9A, STV_TE_9DE4CCD94806C011
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/layout/tests/layout.test.js :: STV_SWR_056: competing parents do not displace a separate centered parent``.

   **Invocation:** ``node --test "frontend/src/layout/tests/layout.test.js"``.

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

STV_TC_35E510D6991A: project pages preserve independent expansion and collapsed root
------------------------------------------------------------------------------------

.. test_case:: project pages preserve independent expansion and collapsed root
   :id: STV_TC_35E510D6991A
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: project pages preserve independent expansion and collapsed root
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_1A1C394699F9D584, STV_TE_F28DB7D6EB428CD7
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: project pages preserve independent expansion and collapsed root``.

   **Invocation:** ``node --test "frontend/src/state/tests/state.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_051 STV_SWR_052: project pages preserve independent expansion and collapsed root', () => {
        const entries=Array.from({length:201},(_,i)=>String(i).padStart(3,'0'));
        const g=graph([['000','r','child'],['005','r','other']],entries);
        let s=initial(); assert.equal(visible(g,s).ids.length,5);
        s=toggle(g,s,'000');
        s=transition(g,s,{type:'page',page:1}).state; assert.ok(!visible(g,s).ids.includes('child'));
        s=toggle(g,s,'005'); s=transition(g,s,{type:'page',page:0}).state;
        assert.ok(visible(g,s).ids.includes('child')); assert.ok(!visible(g,s).ids.includes('other'));
        s=transition(g,s,{type:'root'}).state; assert.equal(visible(g,s).ids.length,0);
        s=transition(g,s,{type:'root'}).state; assert.ok(visible(g,s).ids.includes('child'));
        const all=[]; for(let page=0;page<41;page++) {s=transition(g,s,{type:'page',page}).state; all.push(...visible(g,s).ids.filter(i=>entries.includes(i)));}
        assert.equal(new Set(all).size,201);
        assert.notEqual(groupKey('a,b','c','incoming'),groupKey('a','b,c','incoming'));
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_3DF9A4D8CF8D: invalid directional labels
-----------------------------------------------

.. test_case:: invalid directional labels
   :id: STV_TC_3DF9A4D8CF8D
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SHR_045, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_2047EEEFB40ABA89, STV_TE_070D31B0EE50B234
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_directional_labels(incoming):
          with pytest.raises(ValueError,match='needs_links.verifies'):
              normalize(TYPES,[dict(LINKS[0],incoming=incoming)],MODEL)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_4594B1E01BC7: classic registration treats prototype keys and script text as data
---------------------------------------------------------------------------------------

.. test_case:: classic registration treats prototype keys and script text as data
   :id: STV_TC_4594B1E01BC7
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/bundle/tests/test_bundle.py :: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_017, STV_SHR_018, STV_SHR_027, STV_SWR_017, STV_SWR_018, STV_SWR_027
   :executed_by: STV_TE_8527B889B584DDFF, STV_TE_99F2816427D87384
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_classic_registration_treats_prototype_keys_and_script_text_as_data(tmp_path):
          graph={'schema':1,'objects':{'__proto__':{'id':'__proto__','title':'</script>\u2028'}},'adjacency':{'__proto__':{'incoming':{},'outgoing':{}}}}
          identity,path=emit(graph,{'__proto__':'<p>Published body</p>'},tmp_path)
          script=(tmp_path/path).read_text(encoding='utf-8')
          assert '</script>' not in script
          result=subprocess.run(['node','-e','require(process.argv[1]);const g=Object.values(globalThis.__STV_DATA__.graphs)[0];process.stdout.write(JSON.stringify({ids:Object.keys(g.objects),prototype:Object.getPrototypeOf(g.objects),missing:typeof g.objects.constructor,title:g.objects.__proto__.title}));',str(tmp_path/path)],capture_output=True,text=True,encoding='utf-8')
          assert result.returncode==0,result.stderr
          data=json.loads(result.stdout)
          assert data=={'ids':['__proto__'],'prototype':None,'missing':'undefined','title':graph['objects']['__proto__']['title']}

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_4E68C09504E8: rooted diamond and isolated cycle
------------------------------------------------------

.. test_case:: rooted diamond and isolated cycle
   :id: STV_TC_4E68C09504E8
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_003 STV_SWR_007 STV_SWR_020 STV_SWR_024 STV_SWR_025: rooted diamond and isolated cycle
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_003, STV_SHR_007, STV_SHR_020, STV_SHR_024, STV_SHR_025, STV_SWR_003, STV_SWR_007, STV_SWR_020, STV_SWR_024, STV_SWR_025
   :executed_by: STV_TE_D1CE8AF2895E7ACF, STV_TE_D9F3EFAD94A6631B
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/state/tests/state.test.js :: STV_SWR_003 STV_SWR_007 STV_SWR_020 STV_SWR_024 STV_SWR_025: rooted diamond and isolated cycle``.

   **Invocation:** ``node --test "frontend/src/state/tests/state.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_003 STV_SWR_007 STV_SWR_020 STV_SWR_024 STV_SWR_025: rooted diamond and isolated cycle', () => {
        const g = graph([['A','r','B'],['A','r','C'],['B','r','D'],['C','r','D'],['D','r','B']]);
        let s = initial(['A', 'A', 'Z']);
        assert.deepEqual(visible(g,s).ids, ['A','Z']);
        for (const id of ['A','B','C','D']) s = toggle(g,s,id);
        assert.equal(visible(g,s).ids.filter(i=>i==='D').length,1);
        s = toggle(g,s,'B'); assert.ok(visible(g,s).ids.includes('D'));
        s = toggle(g,s,'C'); assert.deepEqual(new Set(visible(g,s).ids),new Set(['A','Z','B','C']));
        s = toggle(g,s,'A'); assert.deepEqual(visible(g,s).ids,['A','Z']);
        s = toggle(g,s,'A'); assert.ok(visible(g,s).ids.includes('B'));
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_51B932282614: invalid model
----------------------------------

.. test_case:: invalid model
   :id: STV_TC_51B932282614
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change0-levels]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_DF127AF868F08300, STV_TE_5D000FDBD5095F74
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change0-levels]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change0-levels]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_model(change, path):
          with pytest.raises(ValueError, match=path):
              normalize(TYPES, LINKS, dict(MODEL, **change))

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_5D3C07D3C5DE: invalid model
----------------------------------

.. test_case:: invalid model
   :id: STV_TC_5D3C07D3C5DE
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change2-types]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_2D9B53D73A5690DD, STV_TE_0AA4273D7D0FBA0D
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change2-types]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change2-types]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_model(change, path):
          with pytest.raises(ValueError, match=path):
              normalize(TYPES, LINKS, dict(MODEL, **change))

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_6FE4CFC63C95: 199/200/201 atomic capacity
------------------------------------------------

.. test_case:: 199/200/201 atomic capacity
   :id: STV_TC_6FE4CFC63C95
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_005, STV_SHR_043, STV_SHR_044, STV_SWR_005, STV_SWR_043, STV_SWR_044
   :executed_by: STV_TE_C6A6C8EBC162B1F5, STV_TE_DCC7C845C33BEC31
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/state/tests/state.test.js :: STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity``.

   **Invocation:** ``node --test "frontend/src/state/tests/state.test.js"``.

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

STV_TC_734CF1BFE372: external original url rejects executable or nonportable navigation
---------------------------------------------------------------------------------------

.. test_case:: external original url rejects executable or nonportable navigation
   :id: STV_TC_734CF1BFE372
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/graph/tests/test_graph.py :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_047
   :executed_by: STV_TE_BDAB8D43008687EA, STV_TE_6997C226C3551E52
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_external_original_url_rejects_executable_or_nonportable_navigation(url):
          model=normalize(TYPES,LINKS,MODEL)
          needs=Needs([dict(id='EXTERNAL',type='goal',is_external=True,external_url=url)])
          with pytest.raises(ValueError,match='EXTERNAL.*original documentation URL'):
              snapshot(needs,model,lambda name:name+'.html','Project')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_7D1212345072: external original url rejects executable or nonportable navigation
---------------------------------------------------------------------------------------

.. test_case:: external original url rejects executable or nonportable navigation
   :id: STV_TC_7D1212345072
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/graph/tests/test_graph.py :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[data:text/html,bad]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_047
   :executed_by: STV_TE_55945317445CADCF, STV_TE_DBC98E1C3F428FD5
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[data:text/html,bad]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[data:text/html,bad]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_external_original_url_rejects_executable_or_nonportable_navigation(url):
          model=normalize(TYPES,LINKS,MODEL)
          needs=Needs([dict(id='EXTERNAL',type='goal',is_external=True,external_url=url)])
          with pytest.raises(ValueError,match='EXTERNAL.*original documentation URL'):
              snapshot(needs,model,lambda name:name+'.html','Project')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_8023D1B4838C: portable paths preserve queries and fragments
------------------------------------------------------------------

.. test_case:: portable paths preserve queries and fragments
   :id: STV_TC_8023D1B4838C
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/detail_build/tests/test_details.py :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_portable_paths_preserve_queries_and_fragments
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_018, STV_SWR_018
   :executed_by: STV_TE_F70474F79A404DAF, STV_TE_AF1BE3C13C2A4CCF
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/detail_build/tests/test_details.py::test_portable_paths_preserve_queries_and_fragments``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/detail_build/tests/test_details.py::test_portable_paths_preserve_queries_and_fragments" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_portable_paths_preserve_queries_and_fragments():
          assert portable_url("../images/a.png?v=1#part", "nested/page.html") == "images/a.png?v=1#part"
          assert portable_url("#section", "nested/page.html") == "nested/page.html#section"
          assert portable_url("../../outside.png", "page.html") is None

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_880A2E13BCE9: shared children keep unique nodes and conflicting parents do not overlap
---------------------------------------------------------------------------------------------

.. test_case:: shared children keep unique nodes and conflicting parents do not overlap
   :id: STV_TC_880A2E13BCE9
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_E8DFFB544A7B6399, STV_TE_AF727DC17FAA905E
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/layout/tests/layout.test.js :: STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap``.

   **Invocation:** ``node --test "frontend/src/layout/tests/layout.test.js"``.

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

STV_TC_9316CE9A1843: invalid directional labels
-----------------------------------------------

.. test_case:: invalid directional labels
   :id: STV_TC_9316CE9A1843
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[ ]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SHR_045, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_B108463658646910, STV_TE_AF99E6C634F37385
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[ ]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[ ]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_directional_labels(incoming):
          with pytest.raises(ValueError,match='needs_links.verifies'):
              normalize(TYPES,[dict(LINKS[0],incoming=incoming)],MODEL)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_97667EB28A11: blocked skipped-level edges retain safe detours
--------------------------------------------------------------------

.. test_case:: blocked skipped-level edges retain safe detours
   :id: STV_TC_97667EB28A11
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_053: blocked skipped-level edges retain safe detours
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_050, STV_SWR_053
   :executed_by: STV_TE_8D4E22707578AAA4, STV_TE_0423659C27E9D570
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/layout/tests/layout.test.js :: STV_SWR_053: blocked skipped-level edges retain safe detours``.

   **Invocation:** ``node --test "frontend/src/layout/tests/layout.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_053: blocked skipped-level edges retain safe detours', async()=> {
        const graph={model:{levels:['top','middle','bottom'],types:{t:{level:'top'},m:{level:'middle'},b:{level:'bottom'}}},
          objects:{T:{type:'t'},M:{type:'m'},B:{type:'b'}}};
        const result=await compute(graph,{ids:['T','M','B'],edges:[['B','r','T'],['T','r','B']]},new Map());
        const middle=result.nodes.get(key('M'));
        for(const edge of result.edges) {
          assert.ok(edge.points.length>2);
          for(let i=1;i<edge.points.length;i++) {
            const p=edge.points[i-1],q=edge.points[i];
            assert.ok(p[0]===q[0]||p[1]===q[1]);
            for(let t=.001;t<1;t+=.001) {
              const x=p[0]+t*(q[0]-p[0]),y=p[1]+t*(q[1]-p[1]);
              assert.ok(!(x>middle.x&&x<middle.x+middle.width&&y>middle.y&&y<middle.y+middle.height));
            }
          }
        }
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_ABB4E85E5F66: srcset data images and css resources
---------------------------------------------------------

.. test_case:: srcset data images and css resources
   :id: STV_TC_ABB4E85E5F66
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/detail_build/tests/test_details.py :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_srcset_data_images_and_css_resources
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SHR_018, STV_SWR_015, STV_SWR_017, STV_SWR_018
   :executed_by: STV_TE_367E43ED7CBDD4CE, STV_TE_40FEA9EAFED075AB
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/detail_build/tests/test_details.py::test_srcset_data_images_and_css_resources``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/detail_build/tests/test_details.py::test_srcset_data_images_and_css_resources" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_srcset_data_images_and_css_resources():
          markup='''<div style="color:red;background-image:url(../images/local.png)"><img srcset="data:image/png;base64,AAAA 1x, ../images/two.png 2x, https://example.org/three.png 3x"><style>@import "https://example.org/remote.css"; .image {background: url(//example.org/remote.png)}</style></div>'''
          result=BeautifulSoup(transform(markup,'nested/page.html',set()),'html.parser')
          assert result.div['data-stv-style']=='color:red;background-image:url("images/local.png")'
          assert result.img['data-stv-srcset']=='data:image/png;base64,AAAA 1x, images/two.png 2x'
          assert '@import' not in result.style.text
          assert 'https:' not in result.style.text
          assert result.find('a',href='https://example.org/three.png')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_AEF53EABA753: cross-page targets do not acquire synthetic root edges
---------------------------------------------------------------------------

.. test_case:: cross-page targets do not acquire synthetic root edges
   :id: STV_TC_AEF53EABA753
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_94B6CEC834B13181, STV_TE_B25D7DAF9A7087F9
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges``.

   **Invocation:** ``node --test "frontend/src/state/tests/state.test.js"``.

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

STV_TC_B2EF591B7F1E: upward controls precede neutral and downward controls regardless of authorship
---------------------------------------------------------------------------------------------------

.. test_case:: upward controls precede neutral and downward controls regardless of authorship
   :id: STV_TC_B2EF591B7F1E
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/render/tests/groups.test.js :: frontend/src/render/tests/groups.test.js :: STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_051, STV_SWR_055
   :executed_by: STV_TE_11785768416ABA6F, STV_TE_E359F9744218B058
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/render/tests/groups.test.js :: STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship``.

   **Invocation:** ``node --test "frontend/src/render/tests/groups.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship',()=> {
        const graph={model:{levels:['upper','middle','lower'],types:{
          p:{level:'upper'},m:{level:'middle'},c:{level:'lower'},t:{role:'test'}}},
          objects:{P:{type:'p'},M:{type:'m'},C:{type:'c'},T:{type:'t'}},
          adjacency:{M:{outgoing:{down:['C'],mixed:['P','C'],side:['M'],test:['T'],missing:['X'],empty:[]},
            incoming:{up:['P'],down2:['C'],up2:['P']}}}};
        const before=JSON.stringify(graph);
        assert.deepEqual(orderedGroups(graph,'M').map(g=>g.relation),
          ['up','up2','mixed','side','test','missing','down','down2']);
        assert.equal(JSON.stringify(graph),before,'ordering must not mutate graph data');
        assert.deepEqual(orderedGroups(graph,'X'),[]);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_C747492F203E: invalid model
----------------------------------

.. test_case:: invalid model
   :id: STV_TC_C747492F203E
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change1-types.goal]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_BF297B5EC0FB0880, STV_TE_6E19373786A4491D
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change1-types.goal]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change1-types.goal]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_model(change, path):
          with pytest.raises(ValueError, match=path):
              normalize(TYPES, LINKS, dict(MODEL, **change))

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_D00DA9F2CD10: hidden parts external and missing targets
--------------------------------------------------------------

.. test_case:: hidden parts external and missing targets
   :id: STV_TC_D00DA9F2CD10
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/graph/tests/test_graph.py :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_hidden_parts_external_and_missing_targets
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_013, STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_026, STV_SHR_027, STV_SHR_047, STV_SHR_048, STV_SWR_013, STV_SWR_027, STV_SWR_047, STV_SWR_048
   :executed_by: STV_TE_23341FA7B89F3170, STV_TE_CCFEC1B7BFDE5043
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/graph/tests/test_graph.py::test_hidden_parts_external_and_missing_targets``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/graph/tests/test_graph.py::test_hidden_parts_external_and_missing_targets" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_hidden_parts_external_and_missing_targets():
          model = normalize(TYPES, LINKS, MODEL)
          base = dict(type="goal", title="Title", status="accepted", docname="nested/requirements")
          needs = Needs([
              dict(base, id="A", verifies=["B", "HIDDEN", "MISSING", "HIDDEN.part", "A.part"]),
              dict(base, id="B", is_external=True, docname=None, external_url="https://example.org/B", constraints_results={'rule':{'passed':True}}),
              dict(base, id="HIDDEN", hide=True),
              dict(base, id="part", id_complete="HIDDEN.part", id_parent="HIDDEN", is_part=True),
              dict(base, id="part", id_complete="A.part", id_parent="A", is_part=True),
          ])
          def uri(docname):
              assert docname is not None
              return docname + ".html"
          graph, hidden = snapshot(needs, model, uri, "Project")
          assert set(graph["objects"]) == {"A", "A.part", "B"}
          assert hidden == {"HIDDEN", "HIDDEN.part"}
          assert graph["entries"] == ["A", "B"]
          assert graph["objects"]["B"]["url"] == "https://example.org/B"
          assert graph["objects"]["B"]["metadata"]['constraints_results']=={'rule':{'passed':True}}
          assert graph["objects"]["A.part"]["url"].endswith("#A.part")
          assert graph["adjacency"]["A"]["outgoing"]["verifies"] == ["A.part", "B", "MISSING"]
          assert graph["adjacency"]["B"]["incoming"]["verifies"] == ["A"]
          assert "MISSING" not in graph["objects"]

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_D22785EE6859: cyclic shared geometry with isolated nodes remains deterministic and separated
---------------------------------------------------------------------------------------------------

.. test_case:: cyclic shared geometry with isolated nodes remains deterministic and separated
   :id: STV_TC_D22785EE6859
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: cyclic shared geometry with isolated nodes remains deterministic and separated
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_2335851ACD891F20, STV_TE_B1A1720DB22526B3
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/layout/tests/layout.test.js :: STV_SWR_056: cyclic shared geometry with isolated nodes remains deterministic and separated``.

   **Invocation:** ``node --test "frontend/src/layout/tests/layout.test.js"``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: javascript

      test('STV_SWR_056: cyclic shared geometry with isolated nodes remains deterministic and separated',async()=>{
       const graph={model:{levels:['top','middle','bottom'],types:{p:{level:'top'},a:{level:'middle'},b:{level:'bottom'},t:{role:'test'}}},
        objects:{P:{type:'p'},Q:{type:'p'},A:{type:'a'},B:{type:'b'},Z:{type:'b'},T:{type:'t'}}};
       const visible={ids:Object.keys(graph.objects),edges:[['P','r','A'],['A','r','P'],['Q','r','A'],['A','r','B'],['B','r','P'],['T','r','A'],['T','r','B']]};
       const sizes=new Map(Object.keys(graph.objects).map((id,i)=>[key(id),100+i*31]));
       const result=await compute(graph,visible,sizes),again=await compute(graph,visible,sizes);
       assert.deepEqual([...result.nodes],[...again.nodes]);
       assert.equal(result.nodes.size,6);
       for(const [id,a] of result.nodes) {
        assert.ok([a.x,a.y,a.width,a.height].every(Number.isFinite));
        for(const [other,b] of result.nodes)if(id!==other)
         assert.ok(a.x+a.width<=b.x||b.x+b.width<=a.x||a.y+a.height<=b.y||b.y+b.height<=a.y);
       }
       const t=result.nodes.get(key('T'));
       assert.ok(t.x>=Math.max(...['P','Q','A','B','Z'].map(id=>result.nodes.get(key(id)).x+280))+96);
       assert.ok(result.nodes.get(key('P')).y<result.nodes.get(key('A')).y);
       assert.ok(result.nodes.get(key('A')).y<result.nodes.get(key('B')).y);
      });

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_D31601FDD080: invalid directional labels
-----------------------------------------------

.. test_case:: invalid directional labels
   :id: STV_TC_D31601FDD080
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[1]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SHR_045, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_1F3FC164F20CBC3B, STV_TE_BA7C0491342D931D
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[1]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[1]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_directional_labels(incoming):
          with pytest.raises(ValueError,match='needs_links.verifies'):
              normalize(TYPES,[dict(LINKS[0],incoming=incoming)],MODEL)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_D43DE71AF846: static details and remote fallback
-------------------------------------------------------

.. test_case:: static details and remote fallback
   :id: STV_TC_D43DE71AF846
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/detail_build/tests/test_details.py :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_static_details_and_remote_fallback
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_018, STV_SHR_026, STV_SHR_047, STV_SHR_048, STV_SWR_015, STV_SWR_017, STV_SWR_018, STV_SWR_048, STV_SWR_049
   :executed_by: STV_TE_9154BFB3C32BE8B9, STV_TE_3CD78CD1E4C013B1
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/detail_build/tests/test_details.py::test_static_details_and_remote_fallback``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/detail_build/tests/test_details.py::test_static_details_and_remote_fallback" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_static_details_and_remote_fallback():
          markup = '''<table id="NEED"><tr><td><b>Rich text</b><script>bad()</script>
          <img src="../images/local.png" onerror="bad()"><img src="//example.org/picture.png">
          <video poster="https://example.org/poster.png"><source src="https://example.org/movie.mp4"></video>
          <svg><use href="https://example.org/symbol.svg#x"/></svg>
          <iframe src="https://example.org/widget"></iframe><object data="https://example.org/document"></object>
          <span style="background:url(https://example.org/background)">Static widget</span>
          <span class="traces"><a href="../other.html#HIDDEN">hidden reference</a></span><a href="javascript:bad()">unsafe</a>
          <a href="https://example.org/other.html#HIDDEN">Deliberately published prose reference</a>
          <a href="https://example.org/original">Original</a><label for="field">Name</label><input id="field">
          </td></tr></table>'''
          result = BeautifulSoup(transform(markup, "nested/needs.html", {"HIDDEN"}, {"traces"}), "html.parser")
          assert result.find("b").text == "Rich text"
          assert "Static widget" in result.text
          assert not result.find_all(["script", "iframe", "object"])
          assert not result.select("[onerror]")
          assert 'https:' not in ''.join(tag.get('style','') for tag in result.find_all(True))
          assert "hidden reference" not in result.text
          assert 'Deliberately published prose reference' in result.text
          assert result.find("img")["data-stv-src"] == "images/local.png"
          assert not result.find_all(src=lambda s: s and s.startswith("http"))
          assert "Resource unavailable offline" in result.text
          assert result.find("a", string="Original")["href"] == "https://example.org/original"
          assert not result.find("a", string="unsafe").has_attr("href")

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_DETAIL_CACHE: Concurrent build-scoped detail loading
-----------------------------------------------------------

.. test_case:: Concurrent build-scoped detail loading
   :id: STV_TC_DETAIL_CACHE
   :status: draft
   :tags: test_software
   :basis: documented
   :evidence: frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: concurrent detail requests share one load and retain build identity
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_015, STV_SWR_017
   :last_result: not_run

   **Level:** Software component unit test.

   **Preconditions:** Pinned frontend dependencies and Node; a controlled
   document/script stub supplies local asset load events and fragment registration.

   **Executable selector:** ``STV_SWR_015 STV_SWR_017: concurrent detail requests share one load and retain build identity`` in
   ``frontend/src/inspect/tests/inspect.test.js``.

   **Invocation:** ``node --test frontend/src/inspect/tests/inspect.test.js``.

   **Procedure and expected outcomes:** One script is appended for concurrent requests. Both calls share a promise and return the registered HTML. A new build identity loads its own fragment rather than reusing stale HTML.

   **Evidence:** Retain per-case Node output and candidate identity for release
   qualification. Routine refactor checks do not create a release record or
   change this canonical latest-result field.

STV_TC_DETAIL_RETRY: Retry local detail loading after failure
-------------------------------------------------------------

.. test_case:: Retry local detail loading after failure
   :id: STV_TC_DETAIL_RETRY
   :status: draft
   :tags: test_software
   :basis: documented
   :evidence: frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: failed local detail loading can retry without a stale rejection
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_015, STV_SWR_017
   :last_result: not_run

   **Level:** Software component unit test.

   **Preconditions:** Pinned frontend dependencies and Node; a controlled
   document/script stub supplies local asset load events and fragment registration.

   **Executable selector:** ``STV_SWR_015 STV_SWR_017: failed local detail loading can retry without a stale rejection`` in
   ``frontend/src/inspect/tests/inspect.test.js``.

   **Invocation:** ``node --test frontend/src/inspect/tests/inspect.test.js``.

   **Procedure and expected outcomes:** A failed asset rejects and removes its script. Retrying creates a fresh script/promise and resolves the newly registered fragment.

   **Evidence:** Retain per-case Node output and candidate identity for release
   qualification. Routine refactor checks do not create a release record or
   change this canonical latest-result field.

STV_TC_E6FA25320A8F: active embed urls are not retained as navigation
---------------------------------------------------------------------

.. test_case:: active embed urls are not retained as navigation
   :id: STV_TC_E6FA25320A8F
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/detail_build/tests/test_details.py :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_active_embed_urls_are_not_retained_as_navigation
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_015, STV_SWR_017, STV_SWR_049
   :executed_by: STV_TE_03DA151E5608D061, STV_TE_0AD15AF696631D27
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/detail_build/tests/test_details.py::test_active_embed_urls_are_not_retained_as_navigation``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/detail_build/tests/test_details.py::test_active_embed_urls_are_not_retained_as_navigation" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_active_embed_urls_are_not_retained_as_navigation():
          markup='''<iframe src="data:text/html,&lt;script&gt;bad()&lt;/script&gt;"></iframe><script src="data:text/javascript,bad()"></script><object data="javascript:bad()"></object><img src="data:image/png;base64,AAAA">'''
          result=BeautifulSoup(transform(markup,'page.html',set()),'html.parser')
          assert not result.find_all(['iframe','script','object','a'])
          assert result.img['src']=='data:image/png;base64,AAAA'

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_EB472A6879CF: local suggestions match IDs and titles and bound results
-----------------------------------------------------------------------------

.. test_case:: local suggestions match IDs and titles and bound results
   :id: STV_TC_EB472A6879CF
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/render/tests/seeds.test.js :: frontend/src/render/tests/seeds.test.js :: STV_SWR_057: local suggestions match IDs and titles and bound results
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_053, STV_SWR_057
   :executed_by: STV_TE_8B87A6B6D7C31F3B, STV_TE_E31F5DC01B22D239
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``frontend/src/render/tests/seeds.test.js :: STV_SWR_057: local suggestions match IDs and titles and bound results``.

   **Invocation:** ``node --test "frontend/src/render/tests/seeds.test.js"``.

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

STV_TC_F549DE4D0BF4: invalid directional labels
-----------------------------------------------

.. test_case:: invalid directional labels
   :id: STV_TC_F549DE4D0BF4
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[None]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SHR_045, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_C452883EA129E707, STV_TE_58457F28951040F2
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[None]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[None]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_directional_labels(incoming):
          with pytest.raises(ValueError,match='needs_links.verifies'):
              normalize(TYPES,[dict(LINKS[0],incoming=incoming)],MODEL)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.

STV_TC_FBDDCC607412: invalid model
----------------------------------

.. test_case:: invalid model
   :id: STV_TC_FBDDCC607412
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change3-accepted_statuses]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_D04E415D80AE0EE6, STV_TE_538006C1339D10B4
   :last_result: passed

   **Level:** Software component unit test.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change3-accepted_statuses]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change3-accepted_statuses]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_invalid_model(change, path):
          with pytest.raises(ValueError, match=path):
              normalize(TYPES, LINKS, dict(MODEL, **change))

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
