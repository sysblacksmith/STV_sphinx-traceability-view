srcset data images and css resources
====================================

.. test_case:: srcset data images and css resources
   :id: STV_TC_ABB4E85E5F66
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_details.py :: docs/test-scripts/test_details.py::test_srcset_data_images_and_css_resources
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_015, STV_SHR_017, STV_SHR_018, STV_SWR_015, STV_SWR_017, STV_SWR_018
   :executed_by: STV_TE_367E43ED7CBDD4CE, STV_TE_40FEA9EAFED075AB
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_details.py::test_srcset_data_images_and_css_resources``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_details.py::test_srcset_data_images_and_css_resources" -q``.

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
