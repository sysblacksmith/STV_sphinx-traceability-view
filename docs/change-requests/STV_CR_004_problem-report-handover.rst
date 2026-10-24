.. _STV_CR_004:

Problem-report model and folder handover
==================================================

.. change_request:: Problem-report model and folder handover
   :id: STV_CR_004
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_004_problem-report-handover.rst
   :priority: unassigned
   :verification_state: not_assessed

   Record: ``STV_CR_004``. Sequence follows the originating request.

   .. rubric:: Owner request and scope

   On 2026-10-18 the owner moved the reports and screenshots directly into
   ``docs/problem-tickets/`` and requested that this be the future user issue handover
   folder. The owner also requested the ``problem_report`` Need type with states
   such as new, analyzed and fixed, applied here and in the shared model, method,
   skills and folder template. This is documentation/workflow infrastructure;
   it does not approve the previous draft product changes or start a release.

   .. rubric:: Model and lifecycle

   ``problem_report`` is the sixth shared Need type. Requirements and architecture
   elements retain draft/reviewed/accepted. Reports instead use new/analyzed/fixed.
   The common Sphinx status enum serializes the union; the shared validator enforces
   the allowed states by type, including rejecting report states on requirements
   and acceptance states on reports. The existing three typed relations retain
   their allowed pairs and mandatory coverage rules. Reports are optional and
   outside that hierarchy: body Need/doc links connect reports to affected work.

   New means awaiting analysis; analyzed means diagnosis, impacts and disposition
   are recorded; fixed means the authorized implementation and agreed checks have
   evidence. A smoke-tested draft may be fixed with partial verification while
   owner review and full release work remain pending. Reopen a recurrence to
   analyzed without deleting its history. Report state does not accept or verify
   linked requirements.

   .. rubric:: Applied repository changes

   * :doc:`/problem-tickets/index` is the intake/return index, with its own lifecycle chart,
     all-status table, report navigation and downloadable starter template.
   * :need:`STV_PR_001`, :need:`STV_PR_002`, :need:`STV_PR_003` and
     :need:`STV_PR_004` retain the owner's current wording and adjacent screenshots.
     Their existing fixes are fixed with partial smoke verification; review remains
     pending. Relative image paths now resolve within the canonical folder.
   * ``docs/conf.py`` maps reports to an additional problem-report band for this
     site's embedded traceability views. Consumer projects retain the extension's
     existing default preset; hosts adding types supply their own complete mapping.
   * There is no repository-root problems folder or open_problems handover copy.
     Reports remain in place after resolution; informal text is valid user intake
     and is normalized by the solver rather than duplicated into a second tree.

   .. rubric:: Shared handover

   The agents repository maintains the extended model, type-aware validator and
   charts, the method, and ``reverse-engineer-requirements/assets/sphinx/problem-tickets/``.
   The folder template includes intake instructions and a non-instantiated report
   starter. New project navigation includes its index under Miscellaneous.
   ``problem-solver`` consumes and updates the same report records; requirements,
   concept, review and implementation skills consume their linked impacts and
   return decisions and actual evidence without changing phase authority.

   .. rubric:: Validation

   Checks executed on 2026-10-18 (Europe/Berlin):

   * Shared ``python -m unittest discover -s <shared-scripts>
     -p test_validate_traceability.py -v``: 11 passed. Cases cover optional reports,
     all three report states, rejecting cross-lifecycle states, and preventing a
     report from replacing requirement derivation. An obsolete test that rejected
     valid direct software-to-stakeholder channeling now tests an actually illegal
     software-to-element derivation instead; supported channeling is unchanged.
   * ``.venv/Scripts/python.exe -m sphinx -E -a -W --keep-going -q -b html docs
     docs/_build/html``: passed after replacing unsupported nested section headings
     inside report Needs with bold labels and correcting a title underline.
   * Shared ``validate_traceability.py docs/_build/html/needs.json --version 0.1
     --repo-root .``: passed, including evidence paths; export contains four problem
     reports alongside the existing 50 stakeholder, 12 system and 54 software
     requirements, two system elements and nine software elements.
   * Export/render inspection confirmed exactly STV_PR_001 through STV_PR_004 with
     fixed status and partial verification, both local screenshots resolving to
     output files, and report chart legends New 0 / Analyzed 0 / Fixed 4. The five
     review charts retain only their own review-state legends.
   * ``quick_validate.py`` passed for all seven updated engineering skills.
     Project/shared ``git diff --check`` passed.
   * Temporary-project Sphinx smoke builds passed for both the empty shared
     problem folder and a new report instantiated from its starter template.
     No fabricated report or unmatched glob is needed to initialize the folder.

   These are model/documentation checks. Product runtime code and release scope
   were not changed in this handover update; previous draft smoke results retain
   their original scope and owner review is still pending.
