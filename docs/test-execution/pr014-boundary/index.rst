PR014 viewport boundary: development verification
==================================================

Input commit ``baf629a7d0c927f20658801f114235abc8f3edb5`` plus owner-provided
PR014 RST/PNG. The owner requested analysis, a plan and the complete V-cycle.
This is a local presentation fix, not a release. Before/after execution and
scoped concept review are recorded here and in :doc:`../../concept-reviews/round-11`.

Before-fix reproduction
-------------------------

Firefox reproduced a node crossing the actual overflow edge in file/HTTP.
The marker has 0 px width/style none, while the node is absent above the edge
and visible just inside it. Both desired-marker assertions fail as expected.

* :download:`Baseline runner report <before.xml>`
* :download:`Baseline diagnostics <before.log>`
* :download:`Before geometry <before/file.json>`
* :download:`Before screenshot <before/file.png>`

.. toctree::
   :maxdepth: 1

   cases

After-fix development result
-----------------------------

The scoped fix passes 70 checks: two complete marker variants plus eight adjacent
Firefox usability/offline/negative-arrow cases and all 60 non-browser tests.
The explicit content-box top border remains fixed while the graph moves; actual
hit tests locate the clip edge. Narrow/wide resizing and a global border-box
host rule preserve the 975 px client area. Keyboard expansion and independent
views work. The rendered clipped-node screenshot was visually inspected.

The packaged CSS matches the source asset byte-for-byte; an isolated installed
wheel host without Node and the source-archive rebuild checks pass. JavaScript,
state, graph/layout algorithms, dependencies and version are unchanged. Full
capacity and complete release qualification were not rerun for this static
presentation fix; their older evidence is not claimed as a new result.

* :download:`After report <after.xml>`
* :download:`Non-browser/package report <python.xml>`
* :download:`After clipped-node screenshot <after/file.png>`
* :download:`After geometry <after/file.json>`
* :download:`Source/package identity <identity.json>`
* :download:`Exact commands <commands.json>`
* :download:`Summary and retained failed attempts <summary.json>`
* :download:`Clean installed consumer identity <consumer/identity.txt>`
* :download:`Source archive inventory <sdist/members.json>`
* :download:`Strict executable mapping <coverage.log>`

Environment: Windows 11, Python 3.13.17, Firefox 158.0.1 and geckodriver 0.37.1,
external browser requests blocked. Canonical executions use enclosing report
completion timestamps, not invented per-variant times. Baseline identity is
retained separately from the final CSS identity. No commit or release is made.

Final documentation checks
----------------------------

Warnings-as-errors Sphinx and full --require-test-coverage validation passed:
56 SHR, 10 SYS, 62 SWR, 110 canonical cases and 606 executions. Strict executable
mapping covers 72 system/software requirements and 136 executable cases, with
no unknown IDs or unmapped active requirements; this inventory is not a claim
that the entire 136-case release selection was rerun. The 70-check development
selection above covers this static viewport fix and its relevant regressions.

* :download:`Final build log <final-build.log>`
* :download:`Final evidence validation <final-traceability.log>`
* :download:`Requirement paths <final-traceability.csv>`
* :download:`Requirement-to-case paths <final-test-coverage.csv>`
