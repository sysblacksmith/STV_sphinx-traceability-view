cross page bundle
=================

.. test_case:: cross page bundle
   :id: STV_TC_5C902A5F732E
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: tests/test_build.py :: tests/test_build.py::test_cross_page_bundle
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_001, STV_SHR_002, STV_SHR_013, STV_SHR_026, STV_SHR_048, STV_SWR_001, STV_SWR_002, STV_SWR_013, STV_SWR_026, STV_SYS_001
   :executed_by: STV_TE_764956AD4834A5CE, STV_TE_7BF04875B87C2A7D
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``tests/test_build.py::test_cross_page_bundle``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "tests/test_build.py::test_cross_page_bundle" -q``.

   **Procedure and expected outcomes:** Execute the following existing test
   procedure with its fixture helpers. Every assertion is a required observable
   outcome; expected error cases must assert the specified diagnostic/state.
   Links identify criterion portions exercised by this case, not a claim that
   this individual case alone verifies every linked requirement in full.
   Review the full case set and the release criterion assessment together.

   .. code-block:: python

      def test_cross_page_bundle(tmp_path):
          result = build(FIXTURE, tmp_path)
          assert result.returncode == 0, result.stdout + result.stderr
          html = (tmp_path / "index.html").read_text(encoding="utf-8")
          assert "STV_PENDING" not in html
          soup = BeautifulSoup(html, "html.parser")
          roots = soup.select(".stv-view")
          assert len(roots) == 2
          assert json.loads(roots[0]["data-stv-seeds"]) == ["ROOT_A", "LEAF_B"]
          assert json.loads(roots[1]["data-stv-seeds"]) == []
          script = soup.select_one("script[data-stv-graph]")
          assert (tmp_path / script["src"]).is_file()
          fragments = list((tmp_path / "_static/stv/details").glob("*.js"))
          assert len(fragments) == 2
          assert any("formatted body" in p.read_text() for p in fragments)

   **Evidence to retain:** Per-case execution result and timestamp, candidate
   and test identities, environment, invocation and linked JUnit/log evidence.
