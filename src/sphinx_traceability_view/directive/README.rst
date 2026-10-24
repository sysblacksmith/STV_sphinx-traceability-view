directive (STV_SWE_DIRECTIVE)
=============================

Sphinx setup, directive parsing and build lifecycle coordination. Depends on model, graph, detail_build and bundle; owns hook/failure ordering.

Implementation
--------------

* ``lifecycle.py``
* ``directives.py``
* ``__init__.py``

Unit tests
----------

* ``tests/test_lifecycle.py``

Host integration, browser interaction and release packaging checks are in
``docs/test-scripts/`` at the repository root. Detailed design may be added
here when needed; this boundary record is not a fabricated detailed design.
