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
Affected system/software revisions remain draft pending concept refinement
and review. This decision does not accept the downstream concept changes.
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

:need:`STV_SWR_001`, :need:`STV_SWR_003`, :need:`STV_SWR_007`, :need:`STV_SWR_025`, :need:`STV_SWR_026`, :need:`STV_SWR_051`.

Downstream impact awaiting concept refinement
----------------------------------------------

Architecture/ADR/interface/implementation and verification-plan changes are
deliberately pending. Existing single-seed directive syntax and mandatory-seed
contracts in those artifacts describe the prior baseline, not the revised
target. Next concept work must reconcile the directive input contract,
multi-root visibility, project-name source, model-driven stakeholder selection,
synthetic-node presentation and seed/root capacity validation. No list syntax
or empty-project user-interface design is prescribed by this requirements step.
The existing atomic group-expansion limit remains; handling projects with more
stakeholder roots than fit in one expansion needs design consideration.
