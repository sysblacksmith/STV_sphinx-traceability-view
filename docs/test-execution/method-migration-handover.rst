Method migration qualification handover
================================================================================

Scope
-----

This is documentation/test-record maintenance for existing v0.2.0, not a new
product version. The owner invoked concept creation/review and full release
testing on 2026-10-19. The owner subsequently authorized the documentation
browser-test expectation update to account for the new incoming ``verifies``
control between upward derivation and downward allocation controls. Product
implementation, public requirements and architecture remain unchanged.

Concept design and acceptance are recorded in
:doc:`../concept-reviews/round-7`. Actual attempts, corrections and final
publication checks are retained under :doc:`index` without rewriting historical
release records. The original v0.2.0 tag remains untouched.

Actual outcomes
--------------------------------------------------------------------------------

The full rerun :doc:`0.2.0-method-2/index` passed 58 Python/browser and
18 JavaScript cases with no failures/errors/skips. The fresh 30,000-Need,
90,000-edge fixture built successfully; its product/dependency/input identity
was checked before reuse in the rerun. The wheel is byte-identical to the
previously qualified v0.2.0 wheel. Both file and static HTTP browser workflows,
isolated offline wheel installation and publication gates are retained.

The initial :doc:`0.2.0-method-1/index` retains 74 passes and the two obsolete
documentation-control assertions, plus its initial heading-format warning.
Both attempts supply 152 canonical per-case execution records. The 81 reviewed
designs have 76 latest passes and five unexecuted planned cases. Final publication,
shared-model and traceability gate evidence is in the rerun's
``qualification.json`` and retained logs; cleanup scope/approval and outcome
are in ``cleanup-proposal.json`` and ``cleanup-results.json``. No evidence or
virtual environment is included in the approved deletion scope.

Release readiness boundary
--------------------------

Problem :need:`STV_PR_006` remains analyzed. Its nested-Windows local-detail
loading acceptance criteria are not resolved by a passing existing regression
suite. The owner requested documentation and execution maintenance, so product
fixes and new long-path regression implementation are outside this increment.
No new product-release readiness or publication is claimed. Occurrence mode,
additional platforms, numeric performance budgets and external-distribution
licensing retain their existing documented deferrals.

Proposed commit message
-----------------------

.. code-block:: text

   Document explicit test coverage and requalify the method migration

       - Make requirement coverage and actual test execution history traceable.
       - Add canonical test cases and link per-case execution records and results.
       - Publish and review the new trace paths using the renamed shared method.
       - Update the documentation browser assertion for the added test relation.
       - Retain full qualification evidence and disclose the known long-path issue.
       - Verify all 76 executable cases while preserving five planned coverage gaps.

Tagging template
----------------

No new tag is recommended for this documentation maintenance increment.
``v0.2.0`` already exists; do not recreate or move it. If a subsequent product
release is qualified and authorized, substitute its new version and final
committed revision in this PowerShell template:

.. code-block:: powershell

   git tag -a <new-version-tag> <qualified-release-commit> -m "<new-version> release"

This is a template, not a command executed by this workflow. A future release
commit and resolution of its readiness gates are prerequisites.

Draft release-note text
-----------------------

.. code-block:: markdown

   # v0.2.0 documentation method migration — draft qualification notes

   Adds explicit requirement-to-test-case and test-case-to-execution links,
   reviewed verification procedures and latest recorded test results.
   Product behavior and the v0.2.0 product wheel remain unchanged.

   The full rerun passed 58 Python/browser and 18 JavaScript tests, plus the
   existing packaging, capacity and publication gates. Both file and static
   HTTP workflows were exercised on Windows/Firefox 158.0 with Python 3.10.9.

   Qualification attempts, environment identities and per-case results are
   retained under docs/test-execution/. These notes do not announce a release.
   The nested-Windows detail-loading issue STV_PR_006 remains unresolved.
   Existing occurrence-mode, platform, performance-budget and licensing
   deferrals remain in effect.
