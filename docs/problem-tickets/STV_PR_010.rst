Problem 10: Source archives include execution logs despite exclusion
================================================================================

.. problem_report:: Source archives include execution logs despite exclusion
   :id: STV_PR_010
   :status: fixed
   :basis: observed
   :evidence: docs/problem-tickets/STV_PR_010.rst
   :priority: unassigned
   :verification_state: partial

   **Source and authority:** Audit finding PRSA-004. The owner authorized the
   next fix after committing PRSA-001 through PRSA-003; baseline ``82448c9``.
   This authorizes packaging remediation, not a release or later findings.

   **Cause:** Hatch combines archive excludes with VCS ignores. The root rule
   retaining execution logs negated the intended test-execution exclusion.
   Actual old archives contain logs; the initial new regression fails against
   the previous configuration. No exposed credential was reported by the audit.

   **Expected outcome and fix:** Select source-package inputs explicitly and
   independently of VCS negations. Keep implementation/browser sources, built
   assets, full legal materials and build inputs. Engineering history, local
   tools and execution evidence stay in Git/local storage. Exclude bytecode and
   caches within selected directories. Original test records and archives are
   unchanged. See :doc:`../technology-stack` for the boundary.

   **Traceability:** Existing distribution obligations :need:`STV_SYS_009`,
   :need:`STV_SWR_042`, :need:`STV_SWR_046`; packaging configuration and the
   existing build hook own this boundary. No requirement, component allocation,
   browser asset, version or state-machine transition changes.

   **Regression and review:** :need:`STV_TC_SDIST_BOUNDARY` inspects actual tar
   members with root/nested ignore negations and local-only sentinels. It checks
   a wheel rebuilt from the archive. The existing installed-wheel case checks
   the real development build in an isolated offline Sphinx host. Evidence and
   exact commands: :doc:`../test-execution/prsa-004-fix/index`. The refined
   packaging policy and new case design await owner review; requirement
   verification and prior concept acceptance are not promoted.

   **Disposition:** Fixed with scoped actual-archive and offline installed-wheel
   verification (two passing cases). The expected old-configuration failure is
   retained. Owner review and eventual release qualification remain separate.
