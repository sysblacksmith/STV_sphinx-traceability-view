Concept review round 4: v0.2.0 implementation release
================================================================

Authority and baseline
----------------------

On 2026-10-18 the owner formally released the changed/new stakeholder
requirements and delegated concept-review acceptance and complete final
implementation/verification for v0.2.0. See :doc:`/sources`. Reviewer: Codex,
with an independent read-only concept-review agent. Input Git revision:
``e7a561cbf1e8706c784980eff8d24e299d4a9885``; subsequent changes comprise
review corrections, versioning and verification. No commit, tag, push or
publication authority is inferred.

Review inventory
----------------

All 51 stakeholder, 10 system and 55 software requirements, two system and nine
software elements were read, including every authored derivation/allocation/
containment path. Individual Need IDs and current file identities are retained
in the adjacent ``round-4-inventory.json``. Assessed current artifacts:

* :doc:`/stakeholder`, :doc:`/system`, :doc:`/software`,
  :doc:`/elements-system`, :doc:`/elements-software`, :doc:`/traceability`.
* :doc:`/architecture-system`, :doc:`/architecture-software`,
  :doc:`/state-machine`, :doc:`/internal-interfaces`,
  :doc:`/technology-stack`, :doc:`/implementation-plan`,
  :doc:`/verification-plan`, :doc:`/test-coverage`.
* :ref:`STV_ADR_001`, :ref:`STV_ADR_002`, :ref:`STV_ADR_003`,
  :ref:`STV_ADR_004`, :ref:`STV_ADR_005`. ADR 003 retains its partial
  supersession history and unaffected decisions.
* Both architecture Draw.io/SVG pairs and the behavioral state-machine pair;
  source mappings, manifests, build/packaging commands, :doc:`/problems/index`
  and the current requirement-change records.

Findings and resolution
----------------------------------------

.. list-table:: Review closure
   :header-rows: 1
   :widths: 15 40 45

   * - Finding
     - Evidence and impact
     - Resolution / closure
   * - STV_REVIEW_010
     - Test-role self-links retraced a single segment; final routing lacked
       postconditions required by the plan.
     - Distinct right-side ports form a visible loop. Runtime checks enforce
       finite coordinates, boundary endpoints and no box-interior crossings.
       Geometry regression checks loop visibility and avoidance invariants.
   * - STV_REVIEW_011
     - Root-only Escape missed pending hover with focus outside the view;
       synthetic-key smoke did not cover that real entry path.
     - Document-scope Escape cancels pending hover; local controls retain focus
       restoration. File/HTTP browser cases exercise real outside-focus Escape,
       scene/viewport cancellation and retained node-to-button hover timing.
   * - STV_REVIEW_012
     - Current architecture prose claimed the product was unimplemented and
       the plan still presented smoke-only verification as current.
     - Stable execution references and explicit full v0.2.0 qualification;
       historical smoke-only evidence remains historical.
   * - STV_REVIEW_013
     - Runner/package checks hard-coded old versions and absent local shared
       tool paths, risking stale-wheel or missing verification evidence.
     - Derive version from pyproject, select that exact wheel, inspect its actual
       metadata, use shared tools directly and stop on preparation errors.

Corrections were re-reviewed against related obligations and contracts. Geometry
and ordering checks pass; full runtime execution remains the implementation gate.
No new boundary, dependency or ADR supersession is needed.

Visual and semantic assessment
------------------------------

Every exported SVG and embedded page was rendered in installed Firefox and
visually inspected, including the full hover region of the state diagram.
Deployment, component data/control flow and behavioral transitions are readable;
connectors avoid unrelated boxes, arrowheads and labels are visible, and
common-state junctions are unambiguous. Publication link checks remain required.
Screenshots are retained with the release execution.

All initial-scope child sets and component allocations are coherent, including
the mixed-parent paths of :need:`STV_SWR_050` and :need:`STV_SWR_052`.
Direct channeling of :need:`STV_SWR_053` from :need:`STV_SHR_050`,
:need:`STV_SWR_054` from :need:`STV_SHR_049` and :need:`STV_SWR_055` from
:need:`STV_SHR_051` is appropriate: these changes add no system responsibility.

Acceptance and implementation handover
--------------------------------------

Under the owner's delegation, the corrected current internal concept is
accepted for v0.2.0 final implementation. This accepts the revised
:need:`STV_SWR_050` and new :need:`STV_SWR_053`, :need:`STV_SWR_054`,
:need:`STV_SWR_055`, and the current ordinary artifacts identified in the
inventory. Unchanged acceptance and historical ADR/review records are preserved.
The owner separately accepts the four stakeholder revisions. Implementation
verification is independent; a complete retained release execution is required.

Existing deferrals remain: separate-occurrence mode (:need:`STV_SWR_019`,
:need:`STV_SWR_021`, :need:`STV_SWR_022`, :need:`STV_SWR_023`), touch,
additional platforms, widget-specific scripting, numeric performance budgets
and the project license decision before external distribution. v0.2.0 finalizes
the five fixes on the shared-identity product; those deferred features are not
silently included.
