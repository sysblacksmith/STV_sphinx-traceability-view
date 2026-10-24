.. _STV_CR_011:

STV_CR_011: MIT license and author attribution
==============================================

.. change_request:: STV_CR_011: MIT license and author attribution
   :id: STV_CR_011
   :status: implemented
   :basis: owner
   :evidence: docs/change-requests/STV_CR_011_mit-license.rst
   :priority: unassigned
   :verification_state: not_assessed

   .. rubric:: Owner decision and provenance

   Date: 2026-10-24. Source: owner prompts in this conversation.

   **Language-corrected decision:** Use the MIT license for STV and include my
   personal name, Henning Heikes, in the copyright notice.

   The owner wants broad reuse, including use in corporate work, while retaining
   author attribution. The decision grants no additional rights to third-party
   code and is not employer/IP approval. No revenue restriction or mandatory
   prominent-credit condition is added to the standard MIT terms.

   .. rubric:: Implementation and distribution

   The repository-root ``LICENSE`` contains the MIT text and
   ``Copyright (c) 2026 Henning Heikes``. Package metadata identifies the author,
   the combined bundled-code SPDX expression and legal files. STV-owned code and
   documentation are MIT; bundled libraries retain MIT/ISC/BSD-3-Clause/EPL-2.0.

   The browser build preserves the license and corrected ELK source notice.
   The extension copies legal materials with generated views. :doc:`../licensing`
   publishes the MIT text, third-party notices, source availability and the
   remaining transitive-source audit limitation. Existing release artifacts and
   historical results are unchanged; the prepared materials apply to future builds.

   .. rubric:: Verification

   The package-installation regression checks the wheel and source archive for
   legal files and the installed extension's generated HTML for license/notices
   and source availability. Fresh checks and their limitations are recorded in
   :doc:`../maturity`; no historical results are retroactively changed.

   .. rubric:: Checks executed on 2026-10-24

   * Wheel and source archive rebuilt successfully with declared legal files.
   * Expanded clean-install/package regression: 1 passed. License and source
     notices are checked in the archive and generated HTML of the installed wheel.
   * Affected lifecycle and public-host integration checks: 14 passed.
   * Sphinx warnings-as-errors: passed; the Licensing page renders the MIT text,
     third-party notices and upstream source-availability information.

   The package-case procedure is synchronized with its actual executable. These
   checks do not constitute a completed audit of ELK/GWT's embedded dependencies
   or employer approval, and do not rewrite historical release results.
