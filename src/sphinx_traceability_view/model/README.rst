model (STV_SWE_MODEL)
=====================

Host-schema normalization and supplemental view-model validation. Exports normalize and DEFAULT; does not own host Need collection.

Implementation
--------------

* ``__init__.py``

Unit tests
----------

* ``tests/test_model.py``

Host integration, browser interaction and release packaging checks are in
``docs/test-scripts/`` at the repository root. Detailed design may be added
here when needed; this boundary record is not a fabricated detailed design.

Type placement accepts a fixed level, legacy test role, levels_by_tag or
one-hop level_from mapping, with optional classifier fallback_level.
