graph (STV_SWE_GRAPH)
=====================

NeedsView adaptation, canonical object/relationship indexes and hidden/external object policy. Consumes the normalized model.

Implementation
--------------

* ``__init__.py``
* ``placement.py``

Unit tests
----------

* ``tests/test_graph.py``

Host integration, browser interaction and release packaging checks are in
``docs/test-scripts/`` at the repository root. Detailed design may be added
here when needed; this boundary record is not a fabricated detailed design.

Placement is resolved from published tags/owner links before exploration;
configured fallback retains ambiguous evidence without exposing hidden owners.
