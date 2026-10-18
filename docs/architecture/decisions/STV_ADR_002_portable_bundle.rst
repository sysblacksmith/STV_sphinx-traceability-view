.. _STV_ADR_002:

STV_ADR_002: Portable graph and rendered-detail bundle
======================================================

Status: **accepted**. Date: 2026-10-18. Scope: software architecture.
Decision owner: project owner.
Supersedes: none. Superseded by: none.

Related specifications and elements: :need:`STV_SYS_003`, :need:`STV_SYS_006`, :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`.

Context
-------

The graph spans host documents; details must match full Need rendering even when pages are opened through file URLs.

Decision
--------

Use one build-level classic-script graph registry and a lazily populated full-detail registry with per-object local scripts captured from final host output. Page-relative references make both available to nested views without runtime fetch. Beautiful Soup extraction and the exact lifecycle are defined in :doc:`../../implementation-plan` and :ref:`STV_ADR_004`.

Rationale
---------

Classic local scripts avoid file-origin fetch restrictions. Capturing final output preserves displayed metadata better than reconstructing templates, at the cost of HTML rebasing and larger bundles.

Logical components and interfaces
---------------------------------

:need:`STV_SWE_GRAPH`, :need:`STV_SWE_DETAIL_BUILD` and :need:`STV_SWE_BUNDLE` produce the versioned contract consumed by :need:`STV_SWE_INSPECT`.

Consequences and constraints
----------------------------

Copied fragment IDs, relative media and original anchors need normalization. Exclude executable scripts; do not expose hidden host data. Host trusted content remains the publishing boundary.

Alternatives considered
-----------------------

Fetching page HTML at hover time would put file-origin behavior at risk. Re-rendering fields from JSON could lose template-specific displayed information. Neither is selected.
