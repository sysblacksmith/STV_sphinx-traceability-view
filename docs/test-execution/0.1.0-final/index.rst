Initial MVP consolidated verification
=================================================================

Outcome: **all required gates passed after the documented publication retest**.

The software execution is :doc:`../0.1.0-candidate-4/index`. Its product and
test inputs remained stable throughout all executable suites. The first
documentation attempt failed on an RST heading underline in the operating
notes; the failed log is retained there. The first auxiliary retest found
another short underline in this record's draft heading. Both publication
formatting failures and the subsequent passing checks remain available below.

The stable execution recorded **54 passed, 0 failed, 0 errors, 0 skipped**
across pytest and Node. The supplemental visual publication case is recorded
separately, without inflating that stable-suite total. Initial SYS/SWR
criteria are marked passed after the criterion review in
:doc:`../../implementation-review`; four later occurrence-mode SWRs remain
not_assessed. Stakeholder verification, release approval and project licensing
are not inferred from these results.

Candidate identity
-----------------------------------------------------------------

Git input: ``30aaba98776ecbe648558d278a985691d81bccb4`` plus the retained dirty source/test identity
``9867e11555574fedc0dd1ec7f67276e1e8b17e703237c476b180ba57e6e2d85a``.
Wheel SHA-256: ``8a31577baec118e32d697c00faef83f06b60dd9478cb0f791be64a0c867f1fdd``.
The tested wheel is retained in the candidate's artifacts directory. Package
contents were compared byte-for-byte with the final product sources. Accepted
SYS/SWR blocks were compared with the input Git baseline; only their independent
verification metadata changed. No product or executable test changed during
publication retesting.

Measurements
-----------------------------------------------------------------

Real host fixture: 30,000 Needs, 90,000 authored edges; build 331.95 s.
Graph script 34,897,944 bytes; detail scripts 147,393,890 bytes.
Three browser repetitions per deployment mode, including 200-node scenes:

.. list-table:: Observed timings on the recorded Windows machine
   :header-rows: 1

   * - Mode
     - Startup median / maximum
     - Expansion median / maximum
   * - file
     - 628.4 / 631.5 ms
     - 85.0 / 378.0 ms
   * - http
     - 665.3 / 701.1 ms
     - 72.5 / 222.0 ms

Raw results include collapse, first/cached detail timings and process-tree
working-set measurements. File fixture copying/cleanup is preparation time,
outside the browser timing intervals. Memory can double-count shared pages.
No numeric latency/memory budget has been agreed; the 200-node limit is an
independently passing acceptance criterion. Windows file paths must remain
short enough for Firefox's local loader; see :doc:`../../implementation-review`.

Publication attempts and evidence
-----------------------------------------------------------------

* :download:`First auxiliary retest (failed draft heading) <documentation-retest.log>`
* :download:`Second auxiliary retest (passed) <documentation-retest-2.log>`
* :download:`Exact publication commands, UTC times and outcomes <publication-results.json>`
* :download:`Retained consolidation/check script <finalize.py>`
* :download:`Visual publication JUnit <visual-publication.xml>`

* coverage-final: exit 0; :download:`log <coverage-final.log>`
* documentation-final: exit 0; :download:`log <documentation-final.log>`
* visual-publication: exit 0; :download:`log <visual-publication.log>`
* traceability-final: exit 0; :download:`log <traceability-final.log>`
* diagram-publication-final: exit 0; :download:`log <diagram-publication-final.log>`

Intermediate attempts
-----------------------------------------------------------------

The earlier attempts retain their source-stability failures and passing case
outcomes. They do not verify the final frozen input:

* :doc:`../0.1.0-candidate-1/publication` (original report retained with its publication erratum)
* :doc:`../0.1.0-candidate-2/index`
* :doc:`../0.1.0-candidate-3/index`
