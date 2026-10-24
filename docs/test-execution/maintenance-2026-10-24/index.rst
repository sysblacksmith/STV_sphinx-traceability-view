Maintenance regression evidence
===============================

Development fixes and acceptance review requested on 2026-10-24. This is not
a release candidate or a release qualification run. The previous release is
:doc:`../1.0.0-canceled`; its evidence/artifacts remain historical.

The initial Windows path regression failed as expected on the original
298-character asset path. Compact full hashes reduce it to 233 characters.
Root/nested pages and missing-asset retry pass over file and HTTP in Firefox.

The broad development run recorded 57 Python passes and one packaging-test
failure, plus 20 JavaScript passes. The first package retest exposed a missing
generated-site inventory copy. Both failures are preserved; the corrected
lifecycle/installation/path/guard retest is retained separately. Final case
outcomes, artifact identities and exact scope are consolidated after that run.

.. toctree::
   :maxdepth: 1

   dependency-audit

Retained evidence
-----------------

* :download:`Before-fix failure <before-path-fix.log>`
* :download:`Before-fix JUnit <before-path-fix.xml>`
* :download:`First path-fix pass <path-fix.log>`
* :download:`First path-fix JUnit <path-fix.xml>`
* :download:`Broad regression log <regression.log>`
* :download:`Broad regression JUnit <regression.xml>`
* :download:`JavaScript results <node-regression.log>`
* :download:`Initial package retest failure <package-retest.log>`
* :download:`Initial package retest JUnit <package-retest.xml>`
* :download:`Negative legal-input checks <legal-guard.log>`
* :download:`Negative legal-input JUnit <legal-guard.xml>`
* :download:`Commands and actual timestamps <commands.json>`
* :download:`Upstream source/archive hashes <upstream-downloads.json>`

Capacity measurements and full release qualification are intentionally not run.
All requirement verification fields remain independent of scoped development
results and concept acceptance.

Final development results
-------------------------

The latest result is passed for **79 distinct cases: 59 Python and 20 JavaScript**.
This consolidates the broad regression and affected corrections within this
maintenance scope; it is explicitly not an assembled full release run.
The two capacity cases are not rerun; four occurrence-mode cases remain planned.

History retains the expected old-path failure, a packaging-test expression
failure, the real missing generated-inventory failure, and the documentation
warning attempt. All corrected affected checks passed. Final artifact 3 has
verified installed-version metadata, packaged vendor identity and copied notices.

Final observations: Firefox 158.0.1/geckodriver 0.37.1 on Windows; old paths
298 characters, compact paths 233. All root/nested file/HTTP cases and recovery
checks passed. The complete source/content digests are not truncated.

.. toctree::
   :maxdepth: 1

   cases

* :download:`Suite totals and final case outcomes <results.json>`
* :download:`Per-case report mapping <case-results.json>`
* :download:`Corrected lifecycle/install/path/guard retest <affected-retest.log>`
* :download:`Corrected retest JUnit <affected-retest.xml>`
* :download:`Final notice package checks <package-final.log>`
* :download:`Final package JUnit <package-final.xml>`
* :download:`All development artifact identities <artifact-hashes.json>`
* :download:`Final source/test hashes <source-hashes.json>`
* :download:`Broad-run source hashes <source-hashes-at-regression.json>`
* :download:`Python dependency environment <environment.txt>`
* :download:`Final path observations <paths-final/observations.json>`

Acceptance and visual evidence
-------------------------------

The scoped acceptance decision is :doc:`../../concept-reviews/round-8`.
The three SVGs and their HTML object embeddings were inspected; the previous
state return-connector overlap was corrected in Draw.io and rechecked.
No state transition changed. :need:`STV_PR_006` is fixed for its scoped
Windows/Firefox/path/recovery criteria; requirement verification is not promoted.

* :download:`Final build-guard mapping result <legal-guard-final.xml>`
* :download:`System diagram in HTML <visual/architecture-system-embedded.png>`
* :download:`Software diagram in HTML <visual/architecture-software-embedded.png>`
* :download:`State diagram in HTML <visual/state-machine-embedded.png>`
* :download:`Earlier overlapping state routes <visual/state-machine-before.png>`
* :download:`Embedded object checks <visual/embedded-checks.json>`
* :download:`Pinned ELK build declaration <elkjs-build.gradle>`
* :download:`Pinned GWT module <ElkJs.gwt.xml>`
* :download:`Original ELK upstream notice <elk-NOTICE.md.txt>`
