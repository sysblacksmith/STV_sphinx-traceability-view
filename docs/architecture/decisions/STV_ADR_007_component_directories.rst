.. _STV_ADR_007:

STV_ADR_007: Architecture-owned component directories
=====================================================

Status: **accepted**. Date: 2026-10-24. Scope: software source organization.
Decision owner: project owner, under the scoped review authority in
:doc:`../../concept-reviews/round-8`.

Owner request: :doc:`../../change-requests/STV_CR_008_component-directories`.
Supersedes: none. Refines source mappings without changing product behavior.

Context
-------

The owner could not easily trace software architecture elements to their code
and expects a matching directory containing implementation and unit tests.
The existing nine responsibility boundaries are cohesive; flat files and
separate unit-test folders obscure their ownership.

Decision
--------

Retain all nine canonical software element IDs and requirement allocations.
Use the lowercase ID suffix as the component directory name. Python build
components are ``directive``, ``model``, ``graph``, ``detail_build`` and
``bundle`` under ``src/sphinx_traceability_view/``. Browser components are
``state``, ``layout``, ``render`` and ``inspect`` under ``frontend/src/``.

Each directory owns its implementation, ``tests/`` and a boundary README.
Architecture elements identify those files through the component naming convention. The public package entry
point exports Sphinx setup from directive and the canonical version.
The lifecycle component owns the package-root version shim; Hatch, Sphinx and
the release runner read that one maintained value. Renderer owns bootstrap,
controls, seed picking and source CSS. Packaged ``static/`` contains generated
delivery assets; it is not a separately invented software element.

Cross-component host, browser, capacity and wheel-installation checks remain
in ``docs/test-scripts/``. Root ``conftest.py`` supplies pytest requirement
metadata to both unit and integration suites. The runtime wheel excludes
component tests and READMEs; the source archive retains development sources.
Detailed design can be added within the component when needed.

Alternatives and consequences
-----------------------------

Keeping flat files with a separate mapping table requires readers to infer
ownership. Combining Python and JavaScript into one component source tree
would complicate both toolchains without improving the existing boundaries.
The selected structure preserves language boundaries and makes ownership
visible in both architecture records and the working tree.

Internal module import paths and test selectors change; the public Sphinx
extension name and directive syntax remain unchanged. This organization
decision does not prescribe detail-asset filenames; their compact immutable
content-hash contract is specified in :doc:`../../internal-interfaces`.
Canonical test-case IDs and archived execution results remain historical.
This ADR records the implemented decision; acceptance of the revised design
is tracked separately in :doc:`../../maturity`.

Rationale and interfaces
------------------------

The directory suffix makes source ownership inspectable without a parallel
mapping table. The public Python shim delegates setup to the lifecycle
component; cross-component data structures and browser/build boundaries stay
as specified in :doc:`../../internal-interfaces`. The shared version value is
read without importing Sphinx when Hatch/docs/build tools need metadata.
No new runtime service or architecture element is introduced.

Open questions and lifecycle evidence
-------------------------------------

Review findings, scoped decisions and exact assessed artifact identities are
centralized in :doc:`../../concept-reviews/round-8` and :doc:`../../maturity`.
There is no new open interface/design decision for this source-organization
scope. Historical release/runtime evidence is preserved independently of
acceptance of this ADR.
