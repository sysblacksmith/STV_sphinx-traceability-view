static details and remote fallback
==================================

.. test_case:: static details and remote fallback
   :id: STV_TC_D43DE71AF846
   :status: accepted
   :tags: release_initial
   :basis: documented
   :evidence: docs/test-scripts/test_details.py :: docs/test-scripts/test_details.py::test_static_details_and_remote_fallback
   :priority: unassigned
   :verification_state: not_assessed
   :verifies: STV_SHR_014, STV_SHR_015, STV_SHR_017, STV_SHR_018, STV_SHR_026, STV_SHR_047, STV_SHR_048, STV_SWR_015, STV_SWR_017, STV_SWR_018, STV_SWR_048, STV_SWR_049
   :executed_by: STV_TE_9154BFB3C32BE8B9, STV_TE_3CD78CD1E4C013B1
   :last_result: passed

   **Level:** Unit/host integration.

   **Preconditions and inputs:** Use the pinned implementation environment,
   fixture setup and parameter variant identified by the executable selector.
   Browser cases require provisioned Firefox/geckodriver and both file/HTTP
   variants where parameterized. Capacity cases require a freshly generated
   30,000-Need/90,000-edge fixture; packaging requires the candidate wheel and
   offline wheelhouse. The procedure below specifies test-specific inputs.

   **Executable selector:** ``docs/test-scripts/test_details.py::test_static_details_and_remote_fallback``.

   **Invocation:** ``.venv-implementation/Scripts/python.exe -m pytest "docs/test-scripts/test_details.py::test_static_details_and_remote_fallback" -q``.

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
