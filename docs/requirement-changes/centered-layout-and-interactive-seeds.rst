Centered parents and interactive seed selection
============================================================

Owner request and workflow
---------------------------

On 2026-10-18 the owner requested two additions before resuming release work:
parents centered above their child nodes, and a seedless overview with five
stakeholder requirements per page plus an interactive seed-ID input matching
existing Needs. The owner explicitly requested stakeholder clarification first,
then automated concept creation, review and implementation of a new MVP for
owner inspection. That inspection is now complete; the dated acceptance decision is recorded below.

Confirmed intent
----------------

* A single stakeholder parent connected to five equally spaced system children
  should align above the middle (third) child, rather than the leftmost child.
* Seedless stakeholder entry pages should contain at most five stakeholders,
  replacing the current internal page size of 50.
* Readers should be able to type a Need ID, receive matching existing Needs,
  and choose a specific starting object without editing RST and rebuilding.
* Existing hidden-object exclusion, semantic levels, shared-node identity and
  the 200-visible-node limit remain applicable unless explicitly amended.

Clarified MVP scope and authority
---------------------------------

The owner confirmed child-span centering with collision avoidance and shared
nodes retained; initially show the project plus its first five stakeholders;
provide the picker in every view, match ID/title and require confirmation of
an exact existing Need. Confirmation replaces only its own view; invalid input
preserves it. Project overview restores the initial overview. The owner
authorized this concept/implementation increment as an MVP for inspection.
At that point, the new wording and downstream artifacts remained drafts;
confirmation of intent and prototype authority did not constitute acceptance.
The earlier round-4 acceptance applies to its historical artifact identities.

Impact and handover
-------------------------

Stakeholder changes affect :need:`STV_SHR_047` (seedless overview),
:need:`STV_SHR_003` (initial collapse exception), :need:`STV_SHR_052`
(centering) and :need:`STV_SHR_053` (interactive selection).
Retain :need:`STV_SHR_002`, :need:`STV_SHR_048`,
:need:`STV_SHR_043` and :need:`STV_SHR_044` where their existing scope applies.

Revised software requirements :need:`STV_SWR_003`, :need:`STV_SWR_051` and
:need:`STV_SWR_052` implement the initialization/page change. New requirements
:need:`STV_SWR_056` and :need:`STV_SWR_057` channel the software-local layout
and selection obligations directly, without artificial system requirements.
Existing :need:`STV_SWR_038` isolation still applies. The responsibilities remain
:need:`STV_SWE_LAYOUT`, :need:`STV_SWE_RENDER` and :need:`STV_SWE_STATE`.
Contracts and focused verification are in :doc:`/internal-interfaces`,
:doc:`/implementation-plan`, :doc:`/verification-plan` and :ref:`STV_ADR_006`.

Review checks resolve entry-path interactions: the overview counts its project
node toward the 200-node cap; all five entries start with ordinary traces
collapsed; the picker catalog excludes hidden objects and synthetic roots;
confirmation atomically replaces prior state after successful layout; ordinary
page changes restore page exploration while explicit overview return starts
fresh. Failed input/layout preserves the previous scene, page and viewport.
Shared identity and finite semantic ranks take precedence over exact centering.
No new dependency, graph payload, server or supported platform is required.

MVP verification on 2026-10-18
----------------------------------------------

The authorized MVP is implemented. Executed checks against the current
worktree passed:

* ``node --test frontend/test/*.test.js``: 16 passed, including five-child
  centering, shared-child collision avoidance, five-entry page boundaries,
  atomic reseeding and bounded ID/title matching.
* ``pytest tests -q -m 'not browser' --tb=short``: 33 passed, 19 deselected.
  Pytest reported two sandbox cache-write warnings; executable checks passed.
* Firefox ``interactive_seed_smoke or project_paging or offline_exploration``:
  6 passed, 11 deselected, using both file and HTTP transport. Paging traversed
  all 201 entries in 41 pages; selection covered title matching, keyboard
  confirmation, invalid-input preservation, independent views and overview return.
* Firefox ``documentation_visuals or usability_smoke or control_order_smoke``:
  5 passed, 12 deselected. Published demo and exported state diagram were also
  visually inspected; screenshots are generated under ``docs/_build/browser``.
* Sphinx full HTML rebuild with ``-E -a -W --keep-going``: passed.
  Shared traceability validation: passed. Source and published diagram links:
  passed. Strict executable coverage inventory: 67 requirements, 68 cases,
  no unmapped active requirements or unknown IDs.

Browser checks used the implementation virtual environment, installed Firefox
and GeckoDriver 0.37.1. Generated runtime JavaScript was rebuilt with
``node build.js`` in ``frontend``. The preview is :doc:`/demo`; these are
development checks, not qualification of a new release distribution. Verification fields remain not_assessed pending criterion review and full
release validation. Full qualification and release approval remain separate
from the completed owner inspection and concept acceptance.

Preserve the complete failed ``0.2.0-candidate-1`` execution. Its four browser
test failures and passing suites remain actual historical evidence, independent
of this new feature request. Further full release qualification is deferred.

Owner approval and accepted concept
------------------------------------------------------------------------------------------

On 2026-10-18 the owner approved the inspected MVP, explicitly released the
current stakeholder requirements and requested completion of concept acceptance.
:doc:`/concept-reviews/round-6` accepts the four stakeholder revisions, five
software revisions, ADR 006 and affected design contracts. The provisional
review history above and round 5 are preserved. No verification state is
promoted by this acceptance; the failed release record is retained unchanged.
