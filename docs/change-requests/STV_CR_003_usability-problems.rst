.. _STV_CR_003:

Draft usability problem resolution
====================================

.. change_request:: Draft usability problem resolution
   :id: STV_CR_003
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_003_usability-problems.rst
   :priority: unassigned
   :verification_state: not_assessed

   Record: ``STV_CR_003``. Sequence follows the originating request.

   .. rubric:: Authority and baseline

   On 2026-10-18 the owner requested conversion of the reports in ``problems`` to
   RST, analysis and fixes across the V-cycle including the MVP **as drafts**,
   smoke-only verification, and an owner check before the next full release.
   This explicitly authorizes provisional downstream work before acceptance of
   the exact requirement wording. No concept acceptance or release is delegated.
   Input revision: ``67f967c47b31a565c6800c32b3e615e5391c1acf``.
   The only pre-existing untracked content
   was the owner's ``problem-tickets/`` folder. Prior accepted records and release
   execution evidence remain historical snapshots.

   .. rubric:: Problem analysis and traceability

   .. list-table:: Draft disposition
      :header-rows: 1
      :widths: 15 25 35 25

      * - Report
        - Cause / intent
        - Requirements
        - Implementation / verification
      * - :doc:`/problem-tickets/STV_PR_001`
        - Router always left the bottom and entered the top, even upward.
        - New :need:`STV_SHR_050`, :need:`STV_SWR_053`.
        - ``frontend/src/layout/layout.js``; facing-port geometry smoke.
      * - :doc:`/problem-tickets/STV_PR_002`
        - Every edge used a far-right corridor regardless of obstacles.
        - Same routing requirements; no duplicate outcome for the same defect.
        - Clear direct segments; corridor fallback for blocked paths/self-links.
      * - :doc:`/problem-tickets/STV_PR_003`
        - Fixed viewport was 650 CSS pixels high.
        - New :need:`STV_SHR_049`, :need:`STV_SWR_054`.
        - ``static/stv.css`` now 975px; Firefox computed-height smoke.
      * - :doc:`/problem-tickets/STV_PR_004`
        - Mouse entry opened a panel immediately.
        - Revised :need:`STV_SHR_015`, :need:`STV_SWR_050`.
        - ``inspect.js`` timer, ``view.js`` hover/Escape; Firefox timing smoke.

   All new/revised requirements are draft and verification remains not assessed.
   System requirements retain their baseline wording and maturity. Routing, height
   and hover timing use direct stakeholder-to-software channeling; no new system
   or system-architecture obligation is needed.
   Existing unrelated obligations remain applicable, including semantic order,
   shared identity, test placement, box avoidance and accessible immediate Details.
   Smoke results cover selected observations only, not full requirement criteria.

   .. rubric:: Design and V-cycle impact

   The routing change is an implementation refinement within :ref:`STV_ADR_003`'s
   retained semantic projection/final-routing decision. No component, dependency,
   deployment or persistent-state boundary changes; no ADR replacement is needed.
   Layout uses facing ports and tests direct segments against open box interiors.
   Where a direct segment is blocked, the existing empty corridors remain. Arrow
   direction always follows the authored relation, independent of exploration.
   This does not claim an optimal crossing count or eliminate necessary detours.

   Inspection owns a cancellable 1000ms hover-pending state per view. Explicit
   Details activation bypasses the timer. Departure, Escape, scene commit and
   viewport movement cancel pending activation. Node-to-button movement preserves
   the timer. Existing dismissal grace, focus and stale-fragment protection remain.

   Contracts and allocation: :doc:`/internal-interfaces`,
   :doc:`/architecture-software`, :need:`STV_SWE_LAYOUT`, :need:`STV_SWE_RENDER`,
   :need:`STV_SWE_INSPECT`. Plans: :doc:`/implementation-plan` and
   :doc:`/verification-plan`. Behavioral transitions and editable diagram:
   :doc:`/state-machine`. Test definitions: ``frontend/src/layout/tests/layout.test.js`` and
   ``docs/test-scripts/test_browser.py::test_usability_smoke``. Coverage is supplemented in
   :doc:`/test-coverage`; no historical release record is rewritten.

   .. rubric:: Draft review and verification

   Owner review of behavior and exact draft wording is pending. Full regression,
   capacity/performance, consumer installation, packaging and release qualification
   are explicitly deferred until that review. No new release version is assigned.
   The generated local demo is the review artifact; the reusable ``problem-solver``
   skill is maintained in the sibling agents repository.

   Checks executed on 2026-10-18 (Europe/Berlin), dirty worktree based on the input
   revision above; Windows, Node 24.21.0, project Python 3.10 environment and
   installed desktop Firefox through geckodriver 0.37.1:

   * ``node --test test/layout.test.js`` from ``frontend``: 3 passed. This includes
     test-lane/self-link box avoidance, direct upward/downward fan-in and blocked
     skipped-level routes. Names map the new routing criteria to executable cases.
   * ``node build.js`` from ``frontend``: passed; regenerated the bundled MVP asset.
   * ``.venv-implementation/Scripts/python.exe -m pytest docs/test-scripts/test_browser.py -q
     -k usability_smoke`` with ``STV_GECKODRIVER`` set: 1 passed, 11 deselected.
     Observed 975px viewport height, brief-hover departure cancellation, sustained
     node-to-button hover, Escape cancellation and immediate keyboard activation
     with focus restoration. Viewport/scene cancellation is implemented but not
     separately exercised in this reduced smoke selection.
   * The same pytest command with ``-k documentation_visuals`` and
     ``STV_SCREENSHOTS=docs/_build/browser``: 1 passed, 11 deselected. Generated
     demo/state-page/diagram screenshots were visually inspected; diagram labels
     were shortened/repositioned after that inspection to remove overlap.
   * ``.venv-implementation/Scripts/python.exe scripts/check-coverage.py --strict``:
     66 system/software requirements, 57 executable cases, no unmapped active
     requirements or unknown references. Collection only; this is not a full run.
   * ``.venv/Scripts/python.exe -m sphinx -E -a -W --keep-going -q -b html docs
     docs/_build/html``: passed after correcting RST heading lengths and assigning
     unused draft IDs. The wrapper script could not run under the host execution
     policy; this is its equivalent Sphinx command.
   * Shared ``validate_traceability.py docs/_build/html/needs.json --version 0.1
     --repo-root .``: passed, including repository evidence paths. Export contains
     50 stakeholder, 12 system and 54 software requirements, 2 system elements
     and 9 software elements.
   * Draw.io regenerated the adjacent state-machine SVG from its editable source.
     ``quick_validate.py`` passed for the installed ``problem-solver`` skill.

   Initial sandbox attempts could not write generated assets/coverage/cache and
   Firefox lost its browsing context at startup. Authorized unsandboxed retries
   passed; these environment failures were not product test failures. No failed
   product assertion was omitted or classified as passed. Full criteria remain
   unverified, and no full release execution record was created for this draft.

   Review entry point: :doc:`/demo`. The source reports are canonical directly in
   ``docs/problem-tickets/``; there are no include-wrapper copies or separate intake tree.
   The user moved the reports and screenshots here. They are now first-class
   problem reports :need:`STV_PR_001`, :need:`STV_PR_002`, :need:`STV_PR_003` and
   :need:`STV_PR_004`, with fixed disposition and partial draft/smoke verification.
   The report model and folder handover update is tracked in
   :doc:`STV_CR_004_problem-report-handover`.

   .. rubric:: Traceability correction after owner review

   On 2026-10-18 the owner questioned unnecessary system-level refinement and
   authorized autonomous correction. Unaccepted draft IDs STV_SYS_011 and
   STV_SYS_012 were withdrawn and remain reserved, without reuse.
   STV_SWR_053 derives directly from STV_SHR_050, STV_SWR_054 from STV_SHR_049,
   and STV_SWR_050 additionally from STV_SHR_015 for hover timing while retaining
   its justified system/keyboard parents. STV_SYS_006 is restored to its baseline
   content and maturity. No system-architecture change is required. Earlier
   12-system export counts are historical draft results; current checks follow.

   Correction checks: coverage inventory regeneration passed with 64 system/software
   requirements and 57 executable cases, no unmapped active requirements or unknown
   IDs. The Sphinx warnings-as-errors build and shared traceability/evidence
   validator passed; the current export has 10 system requirements, 54 software
   requirements, 50 stakeholder requirements and four problem reports. Product
   behavior and test assertions are unchanged; only test-to-requirement metadata
   and generated coverage were corrected. Full release verification remains deferred.
