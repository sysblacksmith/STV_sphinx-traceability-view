Documentation organization and migrated history
=================================================

2026-10-18: The project owner requested one central maturity page and a
separate RST record for each concept-review round, with links to assessed Needs.
This is a documentation-only reorganization. Canonical Need/ADR statuses,
requirement obligations, derivation, allocation, containment and verification
states are preserved. Origin evidence remains on artifacts; review authority,
per-artifact outcomes, findings and dated progress are central records.

Historical review hashes identify the content before this relocation and are
not silently rewritten. This organization update does not constitute another
technical concept review or runtime verification.

Migrated ADR lifecycle history
-------------------------------

The following entries were moved verbatim from the ADRs. Their dates and
historical proposed/held outcomes do not describe current status.

:ref:`STV_ADR_001`
~~~~~~~~~~~~~~~~~~~~


2026-10-18: Proposed in response to the owner request for internal specification and architecture. No implementation or formal ADR acceptance is claimed.


2026-10-18: Accepted as a concept decision under the recorded review delegation.
Runtime verification remains pending; deferred occurrence-mode policy is
outside MVP implementation acceptance.


Validation/scope notes migrated from :ref:`STV_ADR_001`:


Build hook ordering and complete rendered-content extraction require a vertical slice. Package registry availability is unverified. Owner: implementation/design team; resolve through prototype evidence and owner review where obligations change.


:ref:`STV_ADR_002`
~~~~~~~~~~~~~~~~~~~~


2026-10-18: Proposed in response to the owner request for internal specification and architecture. No implementation or formal ADR acceptance is claimed.


2026-10-18: Refined the still-proposed bundle design to lazy local detail scripts and selected Beautiful Soup under STV_ADR_004.

2026-10-18: Concept review corrected publication ordering: hash final fragments,
write the content-addressed manifest, then finalize STV-owned view attributes.
Acceptance remains held for STV_REVIEW_007.

2026-10-18: Round 2 accepted this revision under owner-delegated concept
review after the owner approved the remote-media fallback. Uncached remote
embedded resources become unavailable-offline indications and explicit links;
local media remains usable and no automatic remote retrieval occurs. See
:doc:`../implementation-plan` and :doc:`../concept-review`. Earlier
proposed/held statements above record historical decisions. Runtime verification
remains not_assessed.


Validation/scope notes migrated from :ref:`STV_ADR_002`:


Validate final-render capture across themes, cross-page media and custom fields. Static widget content and the external-object fallback are owner-approved;
remote embedded media follows the owner-approved unavailable-offline
indication and explicit-link fallback. Performance budgets
are deliberately scheduled after first MVP measurements. Owner: implementation/design team; resolve through prototype evidence and owner review where obligations change.


:ref:`STV_ADR_003`
~~~~~~~~~~~~~~~~~~~~


2026-10-18: Proposed in response to the owner request for internal specification and architecture. No implementation or formal ADR acceptance is claimed.


2026-10-18: Refined this proposed decision with ELK/D3/Floating UI boundaries and the implementation algorithm in STV_ADR_004; no accepted decision was rewritten.

2026-10-18: Accepted as a concept decision under the recorded review delegation.
Runtime verification remains pending; deferred occurrence-mode policy is
outside MVP implementation acceptance.


Validation/scope notes migrated from :ref:`STV_ADR_003`:


Prototype crossing/spacing quality and accessible overlay behavior. Define later shared-mode edits before occurrence-mode delivery; do not silently discard independent branch state. Owner: implementation/design team; resolve through prototype evidence and owner review where obligations change.


:ref:`STV_ADR_004`
~~~~~~~~~~~~~~~~~~~~


2026-10-18: Proposed concrete versions, boundaries and verification plan in
response to the owner's implementation-ready concept request. Verified npm
resolution, cyclic ELK layout and IIFE bundling in a temporary environment;
these smoke checks do not establish product acceptance.

2026-10-18: Owner confirmed external metadata/link fallback without downloading
or caching pages as sufficient for the MVP. Other decisions remain proposed.

2026-10-18: Owner confirmed host-hidden Need exclusion and hidden-seed
rejection; filtering precedes published graph/detail generation.

2026-10-18: Owner confirmed static third-party widget content as sufficient
for MVP details, deferring widget-specific JavaScript behavior.

2026-10-18: Owner deferred project license selection and agreed to set
performance budgets after first MVP measurements. No numeric budget or project
license is assigned; library decisions remain proposed.

2026-10-18: Round 2 accepted this revision under owner-delegated concept
review after the owner approved the remote-media fallback. Uncached remote
embedded resources become unavailable-offline indications and explicit links;
local media remains usable and no automatic remote retrieval occurs. See
:doc:`../implementation-plan` and :doc:`../concept-review`. Earlier
proposed/held statements above record historical decisions. Runtime verification
remains not_assessed.


Validation/scope notes migrated from :ref:`STV_ADR_004`:


No library selection is left open for MVP implementation. Validation tasks
remain: real browser execution, final geometry, incremental-build coherence
and the measured large-project cost. External objects without local full rendering use the owner-confirmed
metadata/link fallback. Hidden objects and incident links are excluded by owner decision. Static widget content is sufficient for MVP details; widget-specific
JavaScript remains on the original page by owner agreement;
they must not be reported as full offline-detail parity without evidence.
Owner: implementation team; release exceptions require project-owner review.





Migrated readiness and validation notes
-----------------------------------------

The following is historical progress commentary moved from the scope register.
Current maturity is maintained in :doc:`../maturity`.

Implementation readiness and validation gates
----------------------------------------------

The owner requested a complete implementation concept after the initial
architecture left library selection implicit. The selected stack, exact npm
lock, module/lifecycle contracts, layout algorithm, detail extraction/loading,
packaging boundaries and implementation sequence are now in
:doc:`../technology-stack`, :doc:`../implementation-plan` and :doc:`../verification-plan`.
No further MVP technology-selection step is required.

Completed design checks: exact npm dependencies resolved; ELK handled a cyclic
three-node fixture; esbuild produced a self-contained IIFE; Beautiful Soup
extracted all 113 current Need renderings across five pages. These are design
feasibility checks, not product runtime verification. Python transitive hash
locking remains an explicit packaging task, not a completed artifact.

Remaining work is implementation and verification. The remote embedded-media
policy is resolved in STV_REVIEW_007; the planned implementation gates are:


* Implement and test final-body extraction, link/media/ID rebasing, Need parts
  and lazy local detail scripts against rich-content fixtures.
* Execute full pointer/keyboard workflows in installed Firefox/Windows from
  file and HTTP URLs; verify focus, hover retention and independent views.
* Exercise ELK ordering followed by authoritative semantic projection and final
  routing with cycles, direct channeling and shared tests.
* Measure the defined 30,000-object/90,000-edge benchmark. Numeric response-time
  and memory acceptance budgets remain unassigned; report measured results.
* Verify Python 3.10 wheel installation, included assets/notices, changed/deleted
  source rebuilds and the conservative serial-build lifecycle.
* The owner accepted metadata/link fallback for external Needs without local
  bodies. Hidden Needs are excluded; widget-specific JavaScript in details is deferred. Verify the owner-agreed external, hidden-object and static-widget scope
  against STV_SWR_047 through STV_SWR_049 before claiming STV_SHR_015 coverage.
* Review round 1 applied independent concept acceptance where clean.
  No product implementation or successful product runtime tests exist yet.

The implementation handover has concrete stages and completion gates; do not
start later occurrence mode or silently broaden compatibility in the MVP.


- 2026-10-18: Conducted concept review round 1, corrected seven findings,
  added STV_SWR_050 and recorded an open remote-media decision (007).
  Applied partial acceptance with verification states unchanged.


Post-relocation artifact identities
-----------------------------------

These identify the reorganized artifact sources, not a new technical review.

* ``docs/architecture-decisions.rst``: ``42c7d20a9ccd9f5bf14634d7a114704cb320738b0072a0ae19f2ebe2c8f56855``.
* ``docs/architecture-software.rst``: ``f1eb77fda735f24cc3415e0bad7ec4132cb08fde793db9376729596404cc5e01``.
* ``docs/architecture-system.rst``: ``8962eb822058a272beeac4c909e6f9f1708b31d3e89504fa0a5389f05ee14a42``.
* ``docs/elements-software.rst``: ``dde9172e703500c26fc11ac39d84286227845a56dc6847428218a813e88bcbbb``.
* ``docs/elements-system.rst``: ``0a272985e0155f9b96a3f62103b6f4e05c718c7d4071f88ff82fc723f3760aff``.
* ``docs/implementation-plan.rst``: ``42f0f5860d708aced6bb4b1d2f976518c8e421ca94cadf2d1d2f86f5551f98b3``.
* ``docs/index.rst``: ``4f82d22011ced973c34c38f89f27c60477175445400bff6c3b16a66e1d291940``.
* ``docs/internal-interfaces.rst``: ``d6d576fd60b23ce9dc487f6d812768b1c998763e336652b81dcf716eff9cb0d8``.
* ``docs/method.rst``: ``2d5230399c6e535193791f44b34724e4c59b53a1b1bfcfe3d4d855440f1fcdc3``.
* ``docs/software.rst``: ``65c33e96a6ca2c47f53de7dc5ea143aa399b21b953c1154ac0e2a63166055f20``.
* ``docs/stakeholder.rst``: ``112645a533fa4d3ad02d0f48abfc644bfd6b560c0f8c84fd57594a2a7ea7bf08``.
* ``docs/system.rst``: ``efba275ab09cc621344aa1d805ddafe074ade5caaab2038a0a0809894d6b93e6``.
* ``docs/technology-stack.rst``: ``f8f4fcb3cc74e50c9e20e8d23fc30bb2a622a8a7d05b7e3c44d472099c0bd9db``.
* ``docs/traceability.rst``: ``684b96d372e2dcd7642126225d7be9ea339411a979029036915e3ec168230bfb``.
* ``docs/verification-plan.rst``: ``35b95a3216a429594a6c6121abcb5e68c4492dbbebe3b19f35024c2351700553``.
* ``docs/architecture/decisions/STV_ADR_001_static_extension.rst``: ``df61e6a0507bf2ca1f2a3da03bab841de2293323f91c6daf4d52f9c66ad41e91``.
* ``docs/architecture/decisions/STV_ADR_002_portable_bundle.rst``: ``4a5e396b61e42daae49a976c6d9eb995ad04aceb6cdaae5badd77e397802f66d``.
* ``docs/architecture/decisions/STV_ADR_003_state_layout.rst``: ``61bac0b6ed73d7440c44ff86e49a33696f4af373c438649a0a16190d3d4a1dc5``.
* ``docs/architecture/decisions/STV_ADR_004_dependencies.rst``: ``03fc636b6ae2dbbba9e6393f8a481485a87867adfa630d90b5d0e0524bcb47b6``.
