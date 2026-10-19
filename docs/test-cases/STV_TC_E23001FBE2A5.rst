project paging
==============

.. test_case:: project paging
   :id: STV_TC_E23001FBE2A5
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_browser.py :: tests/test_browser.py::test_project_paging[file]
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_047, STV_SWR_051, STV_SWR_052
   :executed_by: STV_TE_CBBC2FACA177EA6A, STV_TE_8F519B08D780D32F
   :last_result: passed

   **Level:** Browser/system.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_browser.py::test_project_paging[file]``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_browser.py::test_project_paging[file]" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_project_paging(browser,short_output,protocol):
          import shutil
          source=short_output/'source';shutil.copytree(FIXTURE,source)
          (source/'requirements.rst').write_text('Requirements\n============\n\n'+'\n'.join(f'.. shr:: Stakeholder {i}\n   :id: GOAL_{i:03}\n' for i in range(201)),encoding='utf-8')
          (source/'index.rst').write_text('Project\n=======\n\n.. toctree::\n\n   requirements\n\n.. traceability-view::\n',encoding='utf-8')
          output=short_output/'html';result=build(source,output);assert result.returncode==0,result.stderr
          with published_url(output,protocol) as url:
              browser.get(url)
              _assert_project_pages(browser)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
