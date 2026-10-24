inspect (STV_SWE_INSPECT)
=========================

Lazy detail loading, safe content restoration, independent hover overlays and persistent per-view collections. Owns Floating UI integration for transient hover only.

Implementation
--------------

* ``inspect.js`` (hover)
* ``content.js`` (shared transport and safe restoration)
* ``collection.js`` (bounded insertion-ordered identities)
* ``persistent.js`` (persistent DOM and focus lifecycle)

Unit tests
----------

* ``tests/inspect.test.js``
* ``tests/collection.test.js``

Host integration, browser interaction and release packaging checks are in
``docs/test-scripts/`` at the repository root. Detailed design may be added
here when needed; this boundary record is not a fabricated detailed design.
