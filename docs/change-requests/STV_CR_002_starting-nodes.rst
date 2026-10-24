.. _STV_CR_002:

Starting-node requirement amendment
=====================================

Owner request and requirement amendment
---------------------------------------

2026-10-18: The project owner requested that a view with no seed ID start at an
artificial project-named node linked to stakeholder requirements, and that a
list of seed IDs be supported instead of only one. The owner explicitly asked
to update requirements first. This record amends the existing concept baseline;
it is not a new concept review or approval of the revised requirement wording.

The previous missing-seed failure obligation is replaced by project-root mode.
Unknown and host-hidden explicitly supplied IDs remain errors. Single-seed
behavior remains supported. Collapsed initialization, model replacement,
visibility exclusions and the 200-visible-node limit are retained. The project
entry node is artificial and is not another stakeholder/architecture Need.

The project owner explicitly reviewed and accepted the stakeholder amendment
on 2026-10-18 in this conversation: "i have reviewd the new stakeholder req.
and accept them. please update the status accrodingyl". Acceptance covers
:need:`STV_SHR_003`, :need:`STV_SHR_025`, :need:`STV_SHR_026`,
:need:`STV_SHR_047` and :need:`STV_SHR_048`. Their status is accepted.
That stakeholder decision did not accept downstream concept changes. The
subsequent owner-authorized concept-creation and delegated review are now
complete; see :doc:`../concept-reviews/round-3` for the accepted revisions.
Previous acceptance and content identities remain historical in
:doc:`../concept-reviews/round-1` and :doc:`../concept-reviews/round-2`.
Verification remains not_assessed.

Affected requirement objects
-----------------------------

stakeholder.rst:

:need:`STV_SHR_003`, :need:`STV_SHR_025`, :need:`STV_SHR_026`, :need:`STV_SHR_047`, :need:`STV_SHR_048`.

system.rst:

:need:`STV_SYS_001`.

software.rst:

:need:`STV_SWR_001`, :need:`STV_SWR_003`, :need:`STV_SWR_007`, :need:`STV_SWR_025`, :need:`STV_SWR_026`, :need:`STV_SWR_051`, :need:`STV_SWR_014`,
:need:`STV_SWR_043`, :need:`STV_SWR_052`.

Project-root pagination decision
---------------------------------

2026-10-18: Asked whether projects with more than 199 stakeholder requirements
should page root links or reject oversized expansion. The owner explicitly
selected "Page the project-root links (Recommended)". This supplies the paging
scope clarification in :need:`STV_SHR_047`; ordinary authored trace groups keep
their all-or-nothing capacity rule. Fixed page size 50 and independent page
exploration are internal design choices in :ref:`STV_ADR_005`.

Downstream concept refinement
------------------------------

2026-10-18: After the assistant proposed concept-creation followed by
concept-review, the owner instructed "thats right. go for it!". This authorizes
the concept workflow and delegated acceptance of substantively reviewed clean
concept artifacts. It does not authorize runtime verification claims or a Git
commit. :doc:`../concept-reviews/round-3` records review scope and evidence.

Reconciled optional/list syntax, project-name source, model stakeholder roles,
synthetic identity/presentation, multi-root visibility, root pages and capacity
validation across requirements, interfaces, architecture and plans. Added
:need:`STV_SWR_052` and accepted :ref:`STV_ADR_005`, partially superseding
:ref:`STV_ADR_003`. Product implementation remains pending.
