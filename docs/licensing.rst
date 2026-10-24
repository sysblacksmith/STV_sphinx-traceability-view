Licensing
=========

STV-owned code and documentation
--------------------------------

The project owner selected MIT on 2026-10-24 and identified the copyright
holder as Henning Heikes. Third-party code retains its own license terms.
Attribution to the author and project is appreciated, without adding a
condition to the standard MIT license.

.. literalinclude:: ../LICENSE
   :language: text

Bundled third-party code
------------------------

The package combines STV-owned MIT code with MIT, ISC, BSD-3-Clause and
EPL-2.0 browser components. Its SPDX expression describes the combined archive;
it does not relicense the third-party components. Python dependencies installed
separately by pip retain their own licenses.

Generated views carry ``LICENSE.txt``, ``THIRD_PARTY_NOTICES.txt`` and
``vendor/ELK-SOURCE.txt`` beside the browser assets. Keep these materials when
redistributing HTML output. The following notices are included in distributions.

.. literalinclude:: ../src/sphinx_traceability_view/static/THIRD_PARTY_NOTICES.txt
   :language: text

ELK source availability
-----------------------

.. literalinclude:: ../src/sphinx_traceability_view/static/vendor/ELK-SOURCE.txt
   :language: text

Source/build provenance and transitive dependencies of the generated ELK/GWT
code still warrant a dedicated redistribution audit before external rollout;
this page is not a claim of completed legal or employer approval. Historical
release artifacts retain the licensing materials present when they were built.
