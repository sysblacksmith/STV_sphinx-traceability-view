.. _STV_CR_009:

STV_CR_009: Requirement filenames and verification levels
=========================================================

Owner request and provenance
----------------------------

Date: 2026-10-24. Source: owner prompt in this conversation.

**Language-corrected owner prompt:** Rename the software, system and stakeholder
requirement files so their filenames contain "requirements", update their paths,
and separate test cases properly into system and software tests.

Changes and retained semantics
------------------------------

The requirement documents are now ``requirements-stakeholder.rst``,
``requirements-system.rst`` and ``requirements-software.rst``. Document links,
source/evidence paths, scripts and diagram targets follow the renamed files.
Canonical requirement IDs and acceptance criteria are unchanged.

Test cases are partitioned into ``test-cases/system/`` and
``test-cases/software/`` according to the boundary exercised. Sphinx-host,
browser and installation checks are integrated system tests. Isolated
component checks are software tests. Existing cross-level ``verifies`` links
remain valid and no case is duplicated or given a replacement ID. The
``test_system`` and ``test_software`` tags support separate overview tables.

Historical review inventories, source hashes and execution selectors retain
their original paths; their live document navigation follows the renamed pages.
This migration changes no latest-result or requirement-verification states.

Counts after migration: 45 system test cases and
38 software test cases, including existing planned cases.

Checks
------

* Strict executable coverage: 67 system/software requirements, 78 executable
  cases, no unmapped active requirements or unknown requirement IDs.
* Sphinx warnings-as-errors: passed after the requirement and case moves.
* State-machine SVG re-exported through Draw.io; all three diagram sources
  retain portable links to their published targets.

Runtime code and executable test procedures are unchanged by this document
reorganization; no runtime release qualification is claimed.
