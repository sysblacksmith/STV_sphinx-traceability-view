0.2.0-candidate-3 execution
===========================

Execution was interrupted by the reviewer after reproducing a layout defect:
collision balancing moved an unrelated parent 109.33 pixels away from its
child despite sufficient space. No complete-suite result is claimed.

Interruption was recorded at 2026-10-18T22:23:05+02:00. The original candidate
metadata, source hashes, completed command records and partial pytest log are
retained. The Ctrl+C interruption returned exit code 1. Candidate 4 tests the
corrected algorithm; candidate 3 does not verify that changed product.

* :download:`Candidate identity <candidate.json>`
* :download:`Source identities <source-hashes.json>`
* :download:`Completed commands <commands.json>`
* :download:`Partial pytest log <pytest.log>`
* :download:`Capacity reuse proof <capacity-reuse.json>`
