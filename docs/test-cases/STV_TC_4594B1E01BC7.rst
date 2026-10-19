classic registration treats prototype keys and script text as data
==================================================================

.. test_case:: classic registration treats prototype keys and script text as data
   :id: STV_TC_4594B1E01BC7
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_bundle.py :: tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_017, STV_SHR_018, STV_SHR_027, STV_SWR_017, STV_SWR_018, STV_SWR_027
   :executed_by: STV_TE_8527B889B584DDFF, STV_TE_99F2816427D87384
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data" -q``.

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
