.. _STV_CR_008:

STV_CR_008: Trace software elements to component code and tests
===============================================================

Owner request and provenance
----------------------------

Date: 2026-10-24. Source: owner prompts in this conversation.

**Language-corrected owner request:**

It is hard to trace the software architecture elements to the implementation.
For each element, I expect a folder with the same name containing its source
code and unit tests, with detailed design added later if needed. Reworking
parts of the architecture is acceptable; the result should be a clean setup.

Scope and decision
------------------

No behavioral requirement or acceptance criterion changes. The existing nine
software elements remain the responsibility boundaries and retain their IDs
and allocations. :ref:`STV_ADR_007` defines their matching directory names.
:doc:`../elements-software` records component, source and unit-test
naming conventions. Host integration/browser/release checks stay in ``docs/test-scripts/``;
unit tests now live under their owning component. Test metadata is collected
at repository root. Runtime packaging excludes component tests.

The browser harness import path left over from its earlier move is corrected.
Inspector unit regressions cover concurrent build-scoped loading and retry
after a failed local asset load. No product feature or dependency is added.

Historical evidence
-------------------

Canonical requirement and test-case IDs remain stable. Existing case selectors
and current coverage point to moved procedures; archived logs, hashes, review
inventories and historical results are unchanged. This structural refactor
requires new checks; previous release results are not relabeled as fresh runs.
New inspector cases and the structural ADR remain draft/proposed pending review.
See :doc:`../maturity` for this increment's actual checks and limitations.

Checks for the component refactor
---------------------------------

Executed on 2026-10-24, Windows, Python 3.10, Node 24.21.0 and Firefox 158.0.1:

* Python unit/host suite excluding browser tests: 33 passed, 25 deselected.
* Colocated frontend unit suite: 20 passed, including two inspector regressions.
* Rebuilt source archive and wheel: passed. Fresh wheel installation into an
  isolated host: 1 passed; runtime wheel contains no component test sources.
* Offline browser exploration: 2 passed (file and HTTP).
* Browser async-layout and reseeding regression checks: 4 passed (file and HTTP).
  Their first attempt exposed the outdated harness-relative import path;
  correcting it produced the passing rerun above.
* Strict coverage: 67 system/software requirements, 78 executable cases,
  no unmapped active requirements or unknown requirement IDs.
* Sphinx warnings-as-errors and shared traceability validation: passed.

The generated runtime JavaScript remains byte-for-byte unchanged by the source
moves. The pre-existing broken architecture-export symlink, left pointing to
an old shared-checkout name, is repaired to a portable relative shared-tool path.
These are development checks, not a new full release qualification. Capacity
benchmarks and the complete browser/release suite were not rerun. Requirements,
canonical case latest-results and historical execution records are not relabeled.
