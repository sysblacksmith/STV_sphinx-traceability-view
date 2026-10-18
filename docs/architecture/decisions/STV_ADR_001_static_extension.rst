.. _STV_ADR_001:

STV_ADR_001: Static build integration and browser runtime
=========================================================

Status: **accepted**. Date: 2026-10-18. Scope: solution architecture.
Decision owner: project owner.
Supersedes: none. Superseded by: none.

Related specifications and elements: :need:`STV_SYS_002`, :need:`STV_SYS_003`, :need:`STV_SYS_009`, :need:`STV_SHR_045`, :need:`STV_SHR_046`.

Context
-------

Offline file use and static hosting exclude a required live service. The host owns its model and dangling-link validation.

Decision
--------

Use a Python Sphinx extension with a build integration and locally bundled browser runtime. Reuse host definitions with one supplemental model mapping. Start with shared-node mode; keep later occurrence behavior isolated.

Rationale
---------

A static boundary fits the accepted delivery constraints and avoids maintaining a second model. It costs build-time snapshot generation and browser payload size.

Logical components and interfaces
---------------------------------

:need:`STV_SE_BUILD` exchanges a generated bundle with :need:`STV_SE_BROWSER`; :need:`STV_SWE_MODEL` normalizes host input. See :doc:`../../internal-interfaces`.

Consequences and constraints
----------------------------

No runtime server is needed. Source changes require rebuilding. Serial builds are the first implementation target; parallel behavior must be demonstrated before being advertised.

Alternatives considered
-----------------------

A server-backed query API conflicts with required offline use. An independent duplicate model increases synchronization burden. Both are rejected in this proposal.
