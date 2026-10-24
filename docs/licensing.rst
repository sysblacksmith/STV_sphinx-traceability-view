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

The package combines STV-owned MIT code with MIT, ISC, BSD-3-Clause,
Apache-2.0, EPL-1.0 and EPL-2.0 browser components. Its SPDX expression describes the combined archive;
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

The engineering redistribution audit is recorded in
:doc:`test-execution/maintenance-2026-10-24/dependency-audit`. It verifies the
exact upstream bundle against npm integrity, identifies the compiled dependency
families, retains source/notice evidence and includes missing Apache-2.0 and
EPL-1.0 material. ``vendor/ELK-INVENTORY.json`` travels with generated views.
The build rejects a changed ELK binary/version or changed audited legal inputs
until the inventory is deliberately renewed. This scope covers STV's shipped
browser assets; it does not assert a bit-for-bit rebuild of upstream ELK.

Historical versions
--------------------------------------------------------------------------------

.. toctree::
   :maxdepth: 1

   licensing/historical/index

The supplement supplies missing license/source context for retained historical
archives by exact hash. Keep it with those archives when redistributing them.
Historical binary download links have been retired without changing their
original test results or stored bytes.
