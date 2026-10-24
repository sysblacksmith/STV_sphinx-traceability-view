CR_013 classified evidence rows: development verification
==========================================================

Scope and identity
--------------------

Development increment from ``0cecafb4836ab252d9e30e4553ab901cbd8660b7`` plus
recorded worktree; Windows 11, Python 3.13.17, Node 24.21.0, Firefox 158.0.1 and
geckodriver 0.37.1. :doc:`../../concept-reviews/round-10` records scoped acceptance
and the owner's fallback choice. :ref:`STV_CR_013` retains the request/diagram.
No release, tag, commit or publication is performed.

* :download:`Exact commands and report times <commands.json>`
* :download:`Source/package identities and phase notes <identity.json>`
* :download:`Outcome summary <summary.json>`

Results
---------

134 distinct tests passed, with no failures/errors/skips: 34 frontend Node tests,
59 full non-browser tests, one additional 30,000-record classification test,
two new published-row variants, 36 existing browser variants and two capacity
variants. Complementary development selections use unchanged runtime bytes;
these are not results from earlier release candidates. The large classification
case and import-only test cleanup followed the initial Python/browser suites;
its actual additional run is retained separately. Every current runtime
Python/JS/CSS member was compared byte-for-byte with the tested development wheel.

* :download:`Frontend report <node.xml>`
* :download:`Full non-browser report <python.xml>`
* :download:`30,000-record classifier report <classification-scale.xml>`
* :download:`New published-row file/HTTP report <first-browser.xml>`
* :download:`Existing Firefox regression report <browser.xml>`
* :download:`Capacity file/HTTP report <capacity.xml>`

Criterion assessment
----------------------

The new Sphinx fixture uses renamed host types/tags/relations and three starting
views (software, case, execution). Each reaches all nine category rows, multiple
cases/executions, a shared cross-level case and three fallback records. Assertions
cover same-row top alignment, immutable classification during navigation,
anchor/peer stability, independent views, resolved control ordering, visible
fallback labels, unchanged world coordinates on Reset and screen-space edge
ports. Model/graph cases cover invalid configurations, strict mode, absent or
conflicting tags, orphan/mixed/hidden owners, outgoing owner mapping, cycles,
record-order determinism and input immutability. The separate 30,000-record test
resolves 15,000 cases and executions with their actual owner links.

* :download:`File geometry observations <geometry/file.json>`
* :download:`HTTP geometry observations <geometry/http.json>`
* :download:`File rendering <geometry/file.png>`
* :download:`HTTP rendering <geometry/http.png>`

All existing legacy-role, PR013 navigation/arrow/order, picker/paging, hover/focus,
missing-target, detail transport and alternate-model browser cases passed.
The rebuilt 30,000-Need/90,000-edge fixture runs three repetitions per transport,
reaches exactly 200 visible nodes, rejects overflow, loads/caches details and
collapses successfully. Maximum measured expansion was 214 ms/file and
204 ms/HTTP; observations do not introduce new performance guarantees.
The clean source-free wheel host has no Node on PATH. Source archive checks
rebuild the wheel and compare shipped assets; package members match current
runtime source. No dependency or version pin changed.

* :download:`Browser capacity measurements <capacity-browser.json>`
* :download:`Large fixture build metrics <benchmark-metrics.json>`
* :download:`Installed consumer identity <consumer/identity.txt>`
* :download:`Consumer environment <consumer/environment.txt>`
* :download:`Source archive inventory <sdist/members.json>`
* :download:`Source archive checksums <sdist/artifacts.json>`
* :download:`Development package build <package-final.log>`

Concept and documentation checks
---------------------------------

The initial concept build exposed an ADR link outside its toctree. The index
was corrected and warnings-as-errors validation passed before acceptance.
Standalone and embedded system/software/state diagrams were visually inspected;
classification labels refine existing flows without new topology or unreadable
routing. Final warnings-as-errors documentation and complete traceability/evidence
validation passed after recording the four canonical executions (109 cases and
604 historical/current executions). Strict executable
mapping covers all 71 system/software requirements, with no unknown IDs or
unmapped active requirement. Unrelated security/hosted gates and later
occurrence-mode requirements retain their previous states.

* :download:`Initial concept navigation diagnostic <cr013-concept-build.log>`
* :download:`Corrected concept build <cr013-concept-build-recheck.log>`
* :download:`Concept test-coverage validation <cr013-concept-traceability.log>`
* :download:`Draw.io export log <cr013-diagram-export.log>`
* :download:`Executable mapping <executable-coverage.log>`
* :download:`Final documentation build <final-build.log>`
* :download:`Final traceability check <final-traceability.log>`

Canonical executions
---------------------

:need:`STV_TC_SW_046`, :need:`STV_TC_SW_047`, :need:`STV_TC_SW_048` and
:need:`STV_TC_SY_061` each have one actual aggregate execution of the complete
procedure. Runner subtests, including relevant legacy regression in the full
frontend selection, remain individually identified in the mapping. Report
completion timestamps are disclosed; no individual finish times are invented.

.. toctree::
   :maxdepth: 1

   cases

* :download:`Canonical procedure/subtest mapping <case-results.json>`

* :download:`Final requirement trace paths <traceability.csv>`
* :download:`Final test coverage paths <test-coverage.csv>`
* :download:`Published diagram target check <diagram-links.log>`
