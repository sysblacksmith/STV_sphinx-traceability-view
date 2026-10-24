Software test cases
===================

Canonical specifications at the software verification level. Each case retains
its own Need ID, requirement links and execution history. See :doc:`index`
for classification and evidence semantics.

.. needtable::
   :filter: type == 'test_case' and 'test_software' in tags
   :columns: id;title;status;verifies;last_result;executed_by

STV_TC_SW_001: reverse traversal has no depth cutoff
----------------------------------------------------

.. test_case:: reverse traversal has no depth cutoff
   :id: STV_TC_SW_001
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_006, STV_SHR_013, STV_SWR_006, STV_SWR_013
   :executed_by: STV_TE_9AAE7A231EC567CE, STV_TE_0FC214543C57C70A, STV_TE_E0CF04631EACB0BB, STV_TE_99108B0AAB32B836, STV_TE_1BA0A2DFA0FC176E, STV_TE_A99C0537EBFB3E44, STV_TE_020C3B30CB3CE490, STV_TE_391A0D0EE4993EEB
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

STV_TC_SW_002: parent and project center over five visible children
-------------------------------------------------------------------

.. test_case:: parent and project center over five visible children
   :id: STV_TC_SW_002
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: parent and project center over five visible children
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_6F0E729E437E98D5, STV_TE_CBC21862BB4E7279, STV_TE_038FB86D0B4FF754, STV_TE_5F793CB29D9FD1EA, STV_TE_ED6D5DD283C93A17, STV_TE_8CE9DC71E7170B2D, STV_TE_1EAD6D9A30EAD9F8, STV_TE_A5E1B09FBC4A967E
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

STV_TC_SW_003: page boundaries, root capacity and independent views
-------------------------------------------------------------------

.. test_case:: page boundaries, root capacity and independent views
   :id: STV_TC_SW_003
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_043, STV_SHR_044, STV_SHR_047, STV_SWR_043, STV_SWR_044, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_E9F99C0B9172AA5A, STV_TE_F98D479E1C9FFFB9, STV_TE_784AE4C8A06E13DD, STV_TE_3CDAC35C33F90156, STV_TE_85864291E80152CE, STV_TE_75F7B5B1B8A24F7C, STV_TE_2D2817DF277C9979, STV_TE_9DAC38836EB4651A
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

STV_TC_SW_004: semantic bands and shared test lane
--------------------------------------------------

.. test_case:: semantic bands and shared test lane
   :id: STV_TC_SW_004
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_009, STV_SHR_010, STV_SHR_011, STV_SHR_012, STV_SHR_037, STV_SHR_050, STV_SWR_009, STV_SWR_010, STV_SWR_011, STV_SWR_012, STV_SWR_037, STV_SWR_053
   :executed_by: STV_TE_22893BEF95C2D437, STV_TE_7BEDB835EBAB2E01, STV_TE_5449E1B08D8C1283, STV_TE_40219C3E9A991A6B, STV_TE_94927250063F593D, STV_TE_C3C1C771EE9D26B9, STV_TE_0D73FDC39BF5822B, STV_TE_F6DBC705819A1073
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

STV_TC_SW_005: external original url rejects executable or nonportable navigation
---------------------------------------------------------------------------------

.. test_case:: external original url rejects executable or nonportable navigation
   :id: STV_TC_SW_005
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/graph/tests/test_graph.py :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[javascript:bad()]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_047
   :executed_by: STV_TE_815863A689BE2AD9, STV_TE_94297309B20E6054, STV_TE_0685322F3437B886, STV_TE_9586EC686DEFABC6, STV_TE_4FBBD38466D17B71, STV_TE_202280EDFAD4F542, STV_TE_FCE56232BA68A4C2
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

STV_TC_SW_006: self-loop terminates and collapse restores the only seed
-----------------------------------------------------------------------

.. test_case:: self-loop terminates and collapse restores the only seed
   :id: STV_TC_SW_006
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_024: self-loop terminates and collapse restores the only seed
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_024, STV_SWR_024
   :executed_by: STV_TE_BDF4F05162263B81, STV_TE_1F7FB1C9CC36B859, STV_TE_E7F108DBEC658BCC, STV_TE_813CCAABA945A63F, STV_TE_8C80497400903584, STV_TE_2185D0E31034EC5C, STV_TE_AA55B3794C88D185, STV_TE_5F9C0FEC8133DAB9
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

STV_TC_SW_007: replacement level mappings drive ordering without relation-name assumptions
------------------------------------------------------------------------------------------

.. test_case:: replacement level mappings drive ordering without relation-name assumptions
   :id: STV_TC_SW_007
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/render/tests/groups.test.js :: frontend/src/render/tests/groups.test.js :: STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_051, STV_SWR_055
   :executed_by: STV_TE_9194AED2292281DA, STV_TE_53D40C67F7FFB70F, STV_TE_41AA85A0707188AB, STV_TE_BE7CCBCF64651401, STV_TE_21B8D1B032B99F13, STV_TE_4E83B95FAB51F5FD, STV_TE_FC53F9487FB40B92, STV_TE_455B791035DDC9DC
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

STV_TC_SW_008: runtime reseeding is atomic and clears exploration
-----------------------------------------------------------------

.. test_case:: runtime reseeding is atomic and clears exploration
   :id: STV_TC_SW_008
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_057: runtime reseeding is atomic and clears exploration
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_053, STV_SWR_057
   :executed_by: STV_TE_AEF4AE7CB966E22D, STV_TE_221D15B62302934C, STV_TE_54BD88CB892D57F4, STV_TE_F0CDBA310548A24A, STV_TE_64346932C3231DE0, STV_TE_A93FAE7B77F15130, STV_TE_FA447EECFF1794BC, STV_TE_5B35EA56DCD6E94D
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

STV_TC_SW_009: host normalization
---------------------------------

.. test_case:: host normalization
   :id: STV_TC_SW_009
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_host_normalization
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_030, STV_SHR_032, STV_SHR_036, STV_SHR_045, STV_SWR_014, STV_SWR_030, STV_SWR_032, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_A60F3752BE7FF7A8, STV_TE_10A7B4170F40F4B9, STV_TE_4922233CB5454C2F, STV_TE_BA00F16C25D5FA7C, STV_TE_AD6CCF7B6E0C5551, STV_TE_20992D9E40B311E8, STV_TE_9333DCB199439104
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

STV_TC_SW_010: clear facing ports and fan-in avoid outer detours
----------------------------------------------------------------

.. test_case:: clear facing ports and fan-in avoid outer detours
   :id: STV_TC_SW_010
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_053: clear facing ports and fan-in avoid outer detours
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_050, STV_SWR_053
   :executed_by: STV_TE_2DAA1D42C7C13397, STV_TE_F3BAE266CA6E561A, STV_TE_17CA6B7FD2946014, STV_TE_93C98F38340108D0, STV_TE_593A1688E0921F1A, STV_TE_3D1F57656A674B4E, STV_TE_7F6D309D996C7031, STV_TE_60900E66F33E5858, STV_TE_E9D48EE5D838F9F2
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

STV_TC_SW_011: competing parents do not displace a separate centered parent
---------------------------------------------------------------------------

.. test_case:: competing parents do not displace a separate centered parent
   :id: STV_TC_SW_011
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: competing parents do not displace a separate centered parent
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_9CD13938265B5C9A, STV_TE_9DE4CCD94806C011, STV_TE_FEE74F31B67BCA39, STV_TE_E62A5652646F52FB, STV_TE_8E323BAA20BAF0D0, STV_TE_A5D2097C40E4EB52, STV_TE_B9DC9334C4473799, STV_TE_836634DA96409E2F, STV_TE_112EF87FDDCC77C1
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

STV_TC_SW_012: project pages preserve independent expansion and collapsed root
------------------------------------------------------------------------------

.. test_case:: project pages preserve independent expansion and collapsed root
   :id: STV_TC_SW_012
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: project pages preserve independent expansion and collapsed root
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_1A1C394699F9D584, STV_TE_F28DB7D6EB428CD7, STV_TE_55E2928A35CA955C, STV_TE_E5C4BDFF76CA4A30, STV_TE_270215C9234DEAE2, STV_TE_6E98FFB410840842, STV_TE_8A336D6F387B8287, STV_TE_DA4895B7E284B9F5
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

STV_TC_SW_013: invalid directional labels
-----------------------------------------

.. test_case:: invalid directional labels
   :id: STV_TC_SW_013
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SHR_045, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_2047EEEFB40ABA89, STV_TE_070D31B0EE50B234, STV_TE_161477ADA8E2E117, STV_TE_595FE00110891E59, STV_TE_8C969A3CE4BCED2E, STV_TE_783116895D10AE43, STV_TE_31FE40E2189F1B55
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

STV_TC_SW_014: classic registration treats prototype keys and script text as data
---------------------------------------------------------------------------------

.. test_case:: classic registration treats prototype keys and script text as data
   :id: STV_TC_SW_014
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/bundle/tests/test_bundle.py :: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_017, STV_SHR_018, STV_SHR_027, STV_SWR_017, STV_SWR_018, STV_SWR_027
   :executed_by: STV_TE_8527B889B584DDFF, STV_TE_99F2816427D87384, STV_TE_A82455C6EA4E4D5B, STV_TE_1B628A5DEFCC6526, STV_TE_0D638C0275A29724, STV_TE_B2F8E983806B9CD9, STV_TE_38CF9E1899DC5318, STV_TE_4F2B3421FBA924B3
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

STV_TC_SW_015: rooted diamond and isolated cycle
------------------------------------------------

.. test_case:: rooted diamond and isolated cycle
   :id: STV_TC_SW_015
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_003 STV_SWR_007 STV_SWR_020 STV_SWR_024 STV_SWR_025: rooted diamond and isolated cycle
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_003, STV_SHR_007, STV_SHR_020, STV_SHR_024, STV_SHR_025, STV_SWR_003, STV_SWR_007, STV_SWR_020, STV_SWR_024, STV_SWR_025
   :executed_by: STV_TE_D1CE8AF2895E7ACF, STV_TE_D9F3EFAD94A6631B, STV_TE_4BF1F510953BAB2C, STV_TE_807FE5FC51606B02, STV_TE_E21E322E82331DFB, STV_TE_441CB825C7FE0BBB, STV_TE_B08C52330F47E710, STV_TE_B0755CB190EC9291
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

STV_TC_SW_016: invalid model
----------------------------

.. test_case:: invalid model
   :id: STV_TC_SW_016
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change0-levels]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_DF127AF868F08300, STV_TE_5D000FDBD5095F74, STV_TE_165E497AE726E67B, STV_TE_49642C98E5C0FA07, STV_TE_38A0BC9FB7E3018E, STV_TE_D33195EAFF0408E6, STV_TE_4562F726B41C7DBD
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

STV_TC_SW_017: invalid model
----------------------------

.. test_case:: invalid model
   :id: STV_TC_SW_017
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change2-types]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_2D9B53D73A5690DD, STV_TE_0AA4273D7D0FBA0D, STV_TE_D13BBDBFFAD6771A, STV_TE_0984B66A1B7BF510, STV_TE_A64FA138919CCC6A, STV_TE_C57164A163856B97, STV_TE_0695178C4E8BEFF4
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

STV_TC_SW_018: 199/200/201 atomic capacity
------------------------------------------

.. test_case:: 199/200/201 atomic capacity
   :id: STV_TC_SW_018
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_005, STV_SHR_043, STV_SHR_044, STV_SWR_005, STV_SWR_043, STV_SWR_044
   :executed_by: STV_TE_C6A6C8EBC162B1F5, STV_TE_DCC7C845C33BEC31, STV_TE_7E6053F382882EBE, STV_TE_B199E3E92412F17A, STV_TE_66A1FC1A7161CC09, STV_TE_31D3B03D0367496F, STV_TE_E72AFB5739B13BD0, STV_TE_0119607E64B6B308
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

STV_TC_SW_019: external original url rejects executable or nonportable navigation
---------------------------------------------------------------------------------

.. test_case:: external original url rejects executable or nonportable navigation
   :id: STV_TC_SW_019
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/graph/tests/test_graph.py :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_047
   :executed_by: STV_TE_BDAB8D43008687EA, STV_TE_6997C226C3551E52, STV_TE_8B7F9A6C49E172E8, STV_TE_F73049B2F90A96A6, STV_TE_4B417BD0E17F324D, STV_TE_028E02DEDC7258F4, STV_TE_D06F45C7C3BF9F11
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

STV_TC_SW_020: external original url rejects executable or nonportable navigation
---------------------------------------------------------------------------------

.. test_case:: external original url rejects executable or nonportable navigation
   :id: STV_TC_SW_020
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/graph/tests/test_graph.py :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[data:text/html,bad]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_047
   :executed_by: STV_TE_55945317445CADCF, STV_TE_DBC98E1C3F428FD5, STV_TE_C9C094F9DC4456D6, STV_TE_58267D1CD6C96C16, STV_TE_8A2AC8817B3CDC3B, STV_TE_AAA90D8FBEB56A28, STV_TE_1D71FE672824800E
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

STV_TC_SW_021: portable paths preserve queries and fragments
------------------------------------------------------------

.. test_case:: portable paths preserve queries and fragments
   :id: STV_TC_SW_021
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/detail_build/tests/test_details.py :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_portable_paths_preserve_queries_and_fragments
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_018, STV_SWR_018
   :executed_by: STV_TE_F70474F79A404DAF, STV_TE_AF1BE3C13C2A4CCF, STV_TE_FEC5F73D3E70860C, STV_TE_3E753C0867424736, STV_TE_6F94CA59B5459021, STV_TE_5C6FE68502161476, STV_TE_3A60B1F873470A44, STV_TE_F9ABEC97919C212A
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

STV_TC_SW_022: shared children keep unique nodes and conflicting parents do not overlap
---------------------------------------------------------------------------------------

.. test_case:: shared children keep unique nodes and conflicting parents do not overlap
   :id: STV_TC_SW_022
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_E8DFFB544A7B6399, STV_TE_AF727DC17FAA905E, STV_TE_90A435895DB5B8A7, STV_TE_053CFF28DE8DA59B, STV_TE_64AE754BAA3C5AC3, STV_TE_EE6BD832CBF41732, STV_TE_21CB8B718DAE13F0, STV_TE_C6175C120B189720
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

STV_TC_SW_023: invalid directional labels
-----------------------------------------

.. test_case:: invalid directional labels
   :id: STV_TC_SW_023
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[ ]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SHR_045, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_B108463658646910, STV_TE_AF99E6C634F37385, STV_TE_AA244AF9DE24C294, STV_TE_106F45573009D68A, STV_TE_2B855283A53F6516, STV_TE_D0957B2B3C06A9F1, STV_TE_63586A04E847DD91
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

STV_TC_SW_024: blocked skipped-level edges retain safe detours
--------------------------------------------------------------

.. test_case:: blocked skipped-level edges retain safe detours
   :id: STV_TC_SW_024
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_053: blocked skipped-level edges retain safe detours
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_050, STV_SWR_053
   :executed_by: STV_TE_8D4E22707578AAA4, STV_TE_0423659C27E9D570, STV_TE_4FCE6C0AB09DA55B, STV_TE_15036384B14F8D9D, STV_TE_370AE80A6C4B4504, STV_TE_FB192B11A499439D, STV_TE_DA5A739EFD317147, STV_TE_F034263A0679FE7B
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

STV_TC_SW_025: srcset data images and css resources
---------------------------------------------------

.. test_case:: srcset data images and css resources
   :id: STV_TC_SW_025
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/detail_build/tests/test_details.py :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_srcset_data_images_and_css_resources
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SHR_018, STV_SWR_015, STV_SWR_017, STV_SWR_018
   :executed_by: STV_TE_367E43ED7CBDD4CE, STV_TE_40FEA9EAFED075AB, STV_TE_A530D2F64C21F5AD, STV_TE_F974F952B4BAF9DF, STV_TE_B76640E82BB4B08E, STV_TE_9652606E21AC4D8A, STV_TE_4DE02A883601481D, STV_TE_EC301D358EEA10F0
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

STV_TC_SW_026: cross-page targets do not acquire synthetic root edges
---------------------------------------------------------------------

.. test_case:: cross-page targets do not acquire synthetic root edges
   :id: STV_TC_SW_026
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/state/tests/state.test.js :: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_94B6CEC834B13181, STV_TE_B25D7DAF9A7087F9, STV_TE_E1663EE6C8753590, STV_TE_7C87AC31B6F3DFD0, STV_TE_7DC9B129D46082C8, STV_TE_061C58577036E92B, STV_TE_6C91B93B2A6D5E1D, STV_TE_1CC74F8CD2A408D0
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

STV_TC_SW_027: upward controls precede neutral and downward controls regardless of authorship
---------------------------------------------------------------------------------------------

.. test_case:: upward controls precede neutral and downward controls regardless of authorship
   :id: STV_TC_SW_027
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/render/tests/groups.test.js :: frontend/src/render/tests/groups.test.js :: STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_051, STV_SWR_055
   :executed_by: STV_TE_11785768416ABA6F, STV_TE_E359F9744218B058, STV_TE_00DD9E3EE6863E8F, STV_TE_66DFBB4B6CD7B08E, STV_TE_6AB41CB66F1E96FF, STV_TE_02EDB97F9594F220, STV_TE_90C30CA9FE8D9650, STV_TE_83803524656349F4
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

STV_TC_SW_028: invalid model
----------------------------

.. test_case:: invalid model
   :id: STV_TC_SW_028
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change1-types.goal]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_BF297B5EC0FB0880, STV_TE_6E19373786A4491D, STV_TE_09BC3D1A4FC558CB, STV_TE_FF8A5C765D35F850, STV_TE_101E140BDA36EB7B, STV_TE_9BBAA9D45D95C3F2, STV_TE_9CCC9143DB78FAE3
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

STV_TC_SW_029: hidden parts external and missing targets
--------------------------------------------------------

.. test_case:: hidden parts external and missing targets
   :id: STV_TC_SW_029
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/graph/tests/test_graph.py :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_hidden_parts_external_and_missing_targets
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_013, STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_026, STV_SHR_027, STV_SHR_047, STV_SHR_048, STV_SWR_013, STV_SWR_027, STV_SWR_047, STV_SWR_048
   :executed_by: STV_TE_23341FA7B89F3170, STV_TE_CCFEC1B7BFDE5043, STV_TE_94153BE8C066BF21, STV_TE_814A1F12A1BBC13A, STV_TE_25FD90EB28AF9B7D, STV_TE_03AB7BD50ECCF139, STV_TE_DD58B958296DDE45
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

STV_TC_SW_030: cyclic shared geometry with isolated nodes remains deterministic and separated
---------------------------------------------------------------------------------------------

.. test_case:: cyclic shared geometry with isolated nodes remains deterministic and separated
   :id: STV_TC_SW_030
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/layout.test.js :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: cyclic shared geometry with isolated nodes remains deterministic and separated
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_052, STV_SWR_056
   :executed_by: STV_TE_2335851ACD891F20, STV_TE_B1A1720DB22526B3, STV_TE_8B2F8D37BF18C51C, STV_TE_D95EABFECD32D345, STV_TE_5B622E47C33C1574, STV_TE_DCF27FF589806452, STV_TE_BDF8CA9BFA785D2B, STV_TE_204B71204C472F19
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

STV_TC_SW_031: invalid directional labels
-----------------------------------------

.. test_case:: invalid directional labels
   :id: STV_TC_SW_031
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[1]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SHR_045, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_1F3FC164F20CBC3B, STV_TE_BA7C0491342D931D, STV_TE_7DBBDB40959A3B42, STV_TE_B9734B73BC2CD60C, STV_TE_434ADF15C9FA9DDF, STV_TE_AF9987C5F4285B93, STV_TE_892859F0D615CB67
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

STV_TC_SW_032: static details and remote fallback
-------------------------------------------------

.. test_case:: static details and remote fallback
   :id: STV_TC_SW_032
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/detail_build/tests/test_details.py :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_static_details_and_remote_fallback
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_018, STV_SHR_026, STV_SHR_047, STV_SHR_048, STV_SWR_015, STV_SWR_017, STV_SWR_018, STV_SWR_048, STV_SWR_049
   :executed_by: STV_TE_9154BFB3C32BE8B9, STV_TE_3CD78CD1E4C013B1, STV_TE_A4B2E03C91E03A13, STV_TE_B4CE8AA762593317, STV_TE_8536695936990C4C, STV_TE_1DD447D8A1A200A6, STV_TE_8C9014B7C5188921, STV_TE_8E50F836351971F4
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

STV_TC_SW_033: Concurrent build-scoped detail loading
-----------------------------------------------------

.. test_case:: Concurrent build-scoped detail loading
   :id: STV_TC_SW_033
   :status: accepted
   :tags: test_software
   :basis: documented
   :evidence: frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: concurrent detail requests share one load and retain build identity
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_015, STV_SWR_017
   :executed_by: STV_TE_BABAA403FE6F654E, STV_TE_7A6933AA0FFCDB59, STV_TE_D8968AC012EF26E9, STV_TE_54618A700ADB6B55, STV_TE_7B9D9F2F86330B46, STV_TE_DE06191D129E0084
   :last_result: passed

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

STV_TC_SW_034: Retry local detail loading after failure
-------------------------------------------------------

.. test_case:: Retry local detail loading after failure
   :id: STV_TC_SW_034
   :status: accepted
   :tags: test_software
   :basis: documented
   :evidence: frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: failed local detail loading can retry without a stale rejection
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_015, STV_SWR_017
   :executed_by: STV_TE_F1DDDEB16B95B513, STV_TE_69B410A9F2C8E6AF, STV_TE_0B8617656709E9E7, STV_TE_D22AA25460E8FD80, STV_TE_633EFAD44950664B, STV_TE_B8F4FED902D9D0A5
   :last_result: passed

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

STV_TC_SW_035: active embed urls are not retained as navigation
---------------------------------------------------------------

.. test_case:: active embed urls are not retained as navigation
   :id: STV_TC_SW_035
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/detail_build/tests/test_details.py :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_active_embed_urls_are_not_retained_as_navigation
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SWR_015, STV_SWR_017, STV_SWR_049
   :executed_by: STV_TE_03DA151E5608D061, STV_TE_0AD15AF696631D27, STV_TE_8FBDA9692228CD04, STV_TE_4B5C6B8F24B1A098, STV_TE_53E7284FA72B47C2, STV_TE_3870729E09E7A2C0, STV_TE_FB69E2423AB1C174, STV_TE_2FF91B9EDA5379AF
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

STV_TC_SW_036: local suggestions match IDs and titles and bound results
-----------------------------------------------------------------------

.. test_case:: local suggestions match IDs and titles and bound results
   :id: STV_TC_SW_036
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/render/tests/seeds.test.js :: frontend/src/render/tests/seeds.test.js :: STV_SWR_057: local suggestions match IDs and titles and bound results
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_053, STV_SWR_057
   :executed_by: STV_TE_8B87A6B6D7C31F3B, STV_TE_E31F5DC01B22D239, STV_TE_3369468B8AA5C219, STV_TE_69D755969013BB9F, STV_TE_6B60D25F47A795F4, STV_TE_27F7F5B6ABA85945, STV_TE_54AF91BF9501000B, STV_TE_10CEAF25E43BA3BC
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

STV_TC_SW_037: invalid directional labels
-----------------------------------------

.. test_case:: invalid directional labels
   :id: STV_TC_SW_037
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[None]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SHR_045, STV_SWR_036, STV_SWR_045
   :executed_by: STV_TE_C452883EA129E707, STV_TE_58457F28951040F2, STV_TE_B89B43AAD8E09B63, STV_TE_F0B33AD9A3EDBAB8, STV_TE_D4A0B3CA1B38153F, STV_TE_EC569D5FF7A1D7F9, STV_TE_36FBFA138C34D49B
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

STV_TC_SW_038: invalid model
----------------------------

.. test_case:: invalid model
   :id: STV_TC_SW_038
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change3-accepted_statuses]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_036, STV_SWR_036
   :executed_by: STV_TE_D04E415D80AE0EE6, STV_TE_538006C1339D10B4, STV_TE_C8516CEEDA5EE7D1, STV_TE_8E482B9F158BC396, STV_TE_045367B31AEFC102, STV_TE_B012FAD76628F114, STV_TE_3A10BC05D1705C22
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

STV_TC_SW_039: Compact immutable detail assets
----------------------------------------------

.. test_case:: Compact immutable detail assets
   :id: STV_TC_SW_039
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/bundle/tests/test_bundle.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_015, STV_SWR_017, STV_SWR_018
   :executed_by: STV_TE_B2B66F9BDF1CFFBB, STV_TE_228B20B2EF813704, STV_TE_6077E221F6B32476, STV_TE_4467BF4C79FB88C1, STV_TE_CF267118DF42EA21
   :last_result: passed

   **Level:** Software component unit test.

   **Executable selector:** ``src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_detail_assets_preserve_full_identity_with_compact_deduplicated_paths``.

   **Preconditions/inputs:** Three object identities; two identical rich
   fragments and one different fragment. Use a fresh output directory.

   **Procedure and expected outcomes:** Emit the actual graph/detail assets.
   Require exactly two detail files, full 64-character digest stems, identical
   manifest records for equal fragments, a different record for changed
   content, and registration of each full digest in the referenced asset.
   Inspect the graph by parsing its generated JSON registration payload.

   **Evidence:** Actual JUnit outcome, source identity and maintenance log;
   the system Windows-path case covers real browser/path/retry behavior.

STV_TC_SW_040: Reserved authored transport attributes are discarded
-------------------------------------------------------------------

.. test_case:: Reserved authored transport attributes are discarded
   :id: STV_TC_SW_040
   :status: draft
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/detail_build/tests/test_details.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_015, STV_SWR_017, STV_SWR_018
   :executed_by: STV_TE_CCA62B765D254F7C, STV_TE_3515D99967A15219, STV_TE_5BEC37D601E2262B, STV_TE_AE7337922FF27B67
   :last_result: passed

   **Level:** Software component unit regression.

   **Preconditions and inputs:** Existing implementation environment; Node for
   frontend tests and provisioned Firefox/geckodriver for browser cases.
   Use a fresh isolated build; the test controls only harmless marker values
   and loopback resources. No external requests are needed.

   **Executable selector:** ``src/sphinx_traceability_view/detail_build/tests/test_details.py::test_reserved_transport_attributes_are_never_copied_from_authored_html``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "src/sphinx_traceability_view/detail_build/tests/test_details.py::test_reserved_transport_attributes_are_never_copied_from_authored_html" -q``.

   **Procedure and expected outcomes:** Transform forged href, image, srcset and CSS markers alongside genuine local attributes. Require forged values absent and valid markers regenerated.

   **Evidence:** Retain actual JUnit results, commands and source identities in
   :doc:`../test-execution/prsa-002-fix/index`. Design review remains pending.

STV_TC_SW_041: Restored URLs obey the output-local policy
---------------------------------------------------------

.. test_case:: Restored URLs obey the output-local policy
   :id: STV_TC_SW_041
   :status: draft
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/inspect/tests/urls.test.js
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_017, STV_SWR_018
   :executed_by: STV_TE_0207DD89AED15B7F, STV_TE_0E031214B42EB5BB, STV_TE_B232FBE287C5D112, STV_TE_DD7FBEE3BAF1D877
   :last_result: passed

   **Level:** Software component unit regression.

   **Preconditions and inputs:** Existing implementation environment; Node for
   frontend tests and provisioned Firefox/geckodriver for browser cases.
   Use a fresh isolated build; the test controls only harmless marker values
   and loopback resources. No external requests are needed.

   **Executable selector:** ``frontend/src/inspect/tests/urls.test.js :: STV_SWR_017 STV_SWR_018: restored detail paths stay inside the output root``.

   **Invocation:** ``node --test src/inspect/tests/urls.test.js (working directory: frontend)``.

   **Procedure and expected outcomes:** Resolve local image paths under file and HTTP roots. Reject active schemes, remote, absolute, escaping and encoded-separator paths. Permit raster data images only for image resources.

   **Evidence:** Retain actual JUnit results, commands and source identities in
   :doc:`../test-execution/prsa-002-fix/index`. Design review remains pending.

STV_TC_SW_042: Restored CSS rejects unchecked resources
-------------------------------------------------------

.. test_case:: Restored CSS rejects unchecked resources
   :id: STV_TC_SW_042
   :status: draft
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/inspect/tests/urls.test.js
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_015, STV_SWR_017
   :executed_by: STV_TE_2CC2981234F683C2, STV_TE_315D6F81502F3C44, STV_TE_D13E427016FE3E74, STV_TE_020EAACCA6F3FE37
   :last_result: passed

   **Level:** Software component unit regression.

   **Preconditions and inputs:** Existing implementation environment; Node for
   frontend tests and provisioned Firefox/geckodriver for browser cases.
   Use a fresh isolated build; the test controls only harmless marker values
   and loopback resources. No external requests are needed.

   **Executable selector:** ``frontend/src/inspect/tests/urls.test.js :: STV_SWR_015 STV_SWR_017: restored CSS rejects noncanonical and remote resource paths``.

   **Invocation:** ``node --test src/inspect/tests/urls.test.js (working directory: frontend)``.

   **Procedure and expected outcomes:** Require canonical local CSS URLs to resolve; remote URLs become none. Imports, unquoted URLs and escaped syntax are rejected.

   **Evidence:** Retain actual JUnit results, commands and source identities in
   :doc:`../test-execution/prsa-002-fix/index`. Design review remains pending.

STV_TC_SW_043: Stable navigation geometry and boundary cases
------------------------------------------------------------

.. test_case:: Stable navigation geometry and boundary cases
   :id: STV_TC_SW_043
   :status: accepted
   :tags: release_initial, test_software, navigation_stability
   :basis: documented
   :evidence: frontend/src/layout/tests/stability.test.js
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_054, STV_SWR_058
   :executed_by: STV_TE_5D39F79D9C4AC4CD
   :last_result: passed

   **Level/environment:** Software component: pinned frontend dependencies and Node built-in test runner.

   **Preconditions:** Rebuilt local browser asset and isolated fixtures. Current
   development identity is retained separately from historical PoC evidence.

   **Selector:** All stable-navigation cases in ``stability.test.js`` except the
   natural-order case. Run ``node --test src/layout/tests/stability.test.js`` from
   ``frontend``.

   **Inputs/procedure:** P/Q parent seeds and A-F children; expand P, expand Q,
   collapse P; repeat identical inputs. Add a shared test lane before inserting
   ordinary nodes. Grow an earlier band with an 800 px test while anchoring the
   lower band. Reassociate a shared test from a leaf to a parent/leaf median rank.
   Exercise root collapse/reopen and a 200-node shared scene with mixed heights.

   **Expected:** Surviving ordinary x slots and anchor position are identical;
   same-band ordinary y is identical. Repeated inputs are deterministic. Lane x
   stays fixed, tests stay unique, reranked tests join the correct band without
   overlap and ordinary boxes remain at least 96 px left. Taller earlier bands
   move upward without moving the anchor. Finite coordinates, safe route ports
   and nonoverlap are enforced by compute's validation. Fresh centering is checked
   separately by STV_TC_SW_010/011; no global freeze of all bands is expected.

STV_TC_SW_044: Complete finite SVG bounds
-----------------------------------------

.. test_case:: Complete finite SVG bounds
   :id: STV_TC_SW_044
   :status: accepted
   :tags: release_initial, test_software, navigation_stability
   :basis: documented
   :evidence: frontend/src/render/tests/edge-viewport.test.js
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_059
   :executed_by: STV_TE_9660E9FDD3E534BF
   :last_result: passed

   **Level/environment:** Software component: pinned frontend dependencies and Node built-in test runner.

   **Preconditions:** Rebuilt local browser asset and isolated fixtures. Current
   development identity is retained separately from historical PoC evidence.

   **Selector/invocation:** Both ``edge-viewport.test.js`` cases;
   ``node --test src/render/tests/edge-viewport.test.js`` from ``frontend``.

   **Inputs/procedure:** Nodes and outer routes with negative x/y, positive extents,
   and an empty scene. Compute the viewport and compare every point/corner against
   its padded bounds; verify equal CSS/viewBox origins retain world coordinates.

   **Expected:** All extents lie inside 24 px padding, origin cancellation is exact,
   and empty bounds have finite positive width/height. Browser endpoint alignment
   and reset behavior are independently covered by STV_TC_SY_059.

STV_TC_SW_045: Natural ID ordering for fresh scenes
---------------------------------------------------

.. test_case:: Natural ID ordering for fresh scenes
   :id: STV_TC_SW_045
   :status: accepted
   :tags: release_initial, test_software, navigation_stability
   :basis: documented
   :evidence: frontend/src/layout/tests/stability.test.js
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_055, STV_SWR_060
   :executed_by: STV_TE_4ADD571D9D48391C
   :last_result: passed

   **Level/environment:** Software component: pinned frontend dependencies and Node built-in test runner.

   **Preconditions:** Rebuilt local browser asset and isolated fixtures. Current
   development identity is retained separately from historical PoC evidence.

   **Selector:** The natural numeric ID order case in ``stability.test.js``;
   run that file with Node as above.

   **Inputs/procedure:** Supply shuffled REQ_20, REQ_10, REQ_3, REQ_2, REQ_1 in both
   seeded and synthetic project modes without authored visible edges. Compare
   left-to-right order, then expand REQ_2 to CHILD_A with committed context.

   **Expected:** Both modes produce 1,2,3,10,20 within the ordinary rank; synthetic
   root stays in its own band. Expansion preserves every original node position
   and does not insert-sort discovered nodes into occupied slots.

STV_TC_SW_046: Validate classified placement configuration
----------------------------------------------------------------

.. test_case:: Validate classified placement configuration
   :id: STV_TC_SW_046
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/model/tests/test_model.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_061
   :executed_by: STV_TE_D8595800FE3E197A
   :last_result: passed

   **Level/environment:** Software component; pinned Python implementation venv.
   **Procedure:** Normalize renamed types with tag maps, owner maps, fixed levels
   and legacy role. Mutate unknown/empty levels, conflicting selectors, relation
   names, malformed tag/owner maps and fallback values; compare original inputs.
   **Expected:** Valid models normalize without mutation; invalid configuration
   fails with its field path. Owner maps only reference fixed/tag-resolved source
   levels. Run pytest for model/tests/test_model.py.

STV_TC_SW_047: Resolve stable classification and fallback records
-----------------------------------------------------------------------

.. test_case:: Resolve stable classification and fallback records
   :id: STV_TC_SW_047
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: src/sphinx_traceability_view/graph/tests/test_graph.py
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SWR_061
   :executed_by: STV_TE_B40FEC4881589859
   :last_result: passed

   **Level/environment:** Graph component, pinned Python venv.
   **Procedure:** Classify tagged system/software cases, cross-level verifies links,
   multiple executions, renamed host types, conflicting/absent tags, no owners,
   multiple same/mixed owners and hidden owners. Resolve 30,000 case/execution
   records with 15,000 owner links. Compare reordered input records
   and untouched original data. Repeat without configured fallback.
   **Expected:** Fixed row per case/record, fallback with indication for ambiguity,
   strict Need-located failure without fallback, deterministic output and no hidden
   owner leakage. Classification uses the complete graph rather than visible paths.
   Run pytest for graph/tests/test_graph.py.

STV_TC_SW_048: Align classified rows through navigation
-------------------------------------------------------------

.. test_case:: Align classified rows through navigation
   :id: STV_TC_SW_048
   :status: accepted
   :tags: release_initial, test_software
   :basis: documented
   :evidence: frontend/src/layout/tests/classified-rows.test.js
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SYS_005, STV_SWR_012, STV_SWR_037, STV_SWR_055, STV_SWR_058
   :executed_by: STV_TE_D249590313C5FFA4
   :last_result: passed

   **Level/environment:** Software component; pinned Node/frontend environment.
   **Procedure:** Lay out all nine categories, two cases and executions in each
   boundary, fallback and custom rows, plus a shared case verifying both requirement
   levels. Expand/collapse from software/case/execution anchors; reorder input and
   compare target-level control ordering. Exercise cycles, empty rows, 200 nodes and
   existing legacy-role fixtures.
   **Expected:** Declared row order and identical same-row y, finite nonoverlap and
   safe ports, single shared identities, fixed classification across visible-set
   changes, unchanged anchor/peer slots and semantic control ordering. Legacy tests
   still use the right-hand lane. Run all frontend Node tests.
