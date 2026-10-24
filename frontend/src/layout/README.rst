layout (STV_SWE_LAYOUT)
=======================

ELK-assisted ordering, semantic-band projection and final connection geometry. Consumes visible graphs without mutating their identities.

Implementation
--------------

* ``layout.js``

Unit tests
----------

* ``tests/layout.test.js``

Host integration, browser interaction and release packaging checks are in
``docs/test-scripts/`` at the repository root. Detailed design may be added
here when needed; this boundary record is not a fabricated detailed design.

Navigation uses the committed-geometry contract in docs/internal-interfaces.rst
and ADR 008; layout owns stable slots, rendering owns per-view snapshots and
padded SVG bounds. Unit tests remain colocated under tests/.
