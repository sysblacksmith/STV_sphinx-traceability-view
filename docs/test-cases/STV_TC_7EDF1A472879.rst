large project at visible capacity
=================================

.. test_case:: large project at visible capacity
   :id: STV_TC_7EDF1A472879
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_capacity.py :: tests/test_capacity.py::test_large_project_at_visible_capacity[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_043, STV_SHR_044, STV_SWR_043, STV_SWR_044, STV_SYS_008
   :executed_by: STV_TE_010F955390602276, STV_TE_5FEC76D970E683E5
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_capacity.py::test_large_project_at_visible_capacity[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_capacity.py::test_large_project_at_visible_capacity[file]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_large_project_at_visible_capacity(browser,protocol):
          output=Path(os.environ.get('STV_CAPACITY_OUTPUT','docs/_build/benchmark-v2/html')).resolve()
          assert (output/'index.html').is_file(),'Run scripts/benchmark.py before capacity verification'
          runs=[]
          browser.set_script_timeout(35)
          temporary=tempfile.TemporaryDirectory(prefix='stv-cap-') if protocol=='file' else None
          if temporary:
              assert Path(temporary.name).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
              # Full hash names need a short physical output root in Windows Firefox.
              short=Path(temporary.name)/'html';shutil.copytree(output,short);output=short
          try:
              _measure_capacity(browser,output,protocol,runs)
          finally:
              if temporary:
                  assert Path(temporary.name).resolve().is_relative_to(Path(tempfile.gettempdir()).resolve())
                  temporary.cleanup()
          result={'browser':browser.capabilities['browserVersion'],'geckodriver':browser.capabilities.get('moz:geckodriverVersion'),
                  'memory_scope':'Sum of working sets of the isolated Firefox process tree, including content/GPU helpers; shared pages may be counted more than once',
                  'runs':runs,'startup_median_ms':statistics.median(r['startup_ms'] for r in runs),
                  'startup_max_ms':max(r['startup_ms'] for r in runs),
                  'expansion_median_ms':statistics.median(v for r in runs for v in r['expansion_ms']),
                  'expansion_max_ms':max(v for r in runs for v in r['expansion_ms'])}
          target=Path(os.environ.get('STV_CAPACITY_METRICS','docs/_build/capacity-browser.json'));target.parent.mkdir(parents=True,exist_ok=True)
          aggregate=json.loads(target.read_text(encoding='utf-8')) if target.exists() else {}
          aggregate[protocol]=result
          target.write_text(json.dumps(aggregate,indent=2),encoding='utf-8')

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
