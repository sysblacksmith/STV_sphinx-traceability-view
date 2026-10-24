CI validation and candidate provenance
================================================================================

Scope and trust boundary
--------------------------------------------------------------------------------

``.github/workflows/validation.yml`` checks pushes to main, pull requests and
manual runs. ``Core validation`` runs on a hosted Windows runner with Python
3.13 and Node 22: it checks workflow policy, regenerates browser assets from the
lockfile, rejects asset drift, runs JavaScript tests, builds the sdist/wheel,
provisions the offline runtime wheelhouse and runs non-browser Python integration
checks. A separate ``Python 3.10 runtime`` job installs the package and builds the
minimal Sphinx fixture with its installed extension. Runtime dependencies come
from package metadata rather than a duplicated CI list. Reports retain resolved
versions and JUnit evidence.

Actions are pinned to full upstream commit hashes. Both workflows default to a
read-only contents token, disable persisted checkout credentials, bound job
runtimes and use hosted runners. Pull requests never receive OIDC/attestation
permissions. There are no user secrets, pull_request_target/workflow_run triggers,
release creation or package-publishing steps. Weekly Dependabot proposals keep
pinned action updates reviewable; they do not auto-merge.

Validation scope is development assurance, not release acceptance. Browser and
capacity cases remain in the separately authorized release qualification. The
project's full engineering Sphinx build/traceability checks require the private
shared method repository. CI does not fetch it or introduce a credential for it;
those checks remain local using the established shared-method configuration.

Checksums and manual provenance
--------------------------------------------------------------------------------

``.github/workflows/provenance.yml`` is manual-only and runs only for main. Its
build job repeats core validation and retains candidate wheel/source bytes,
``SHA256SUMS`` and ``build-info.json`` for 14 days. Metadata identifies the source
commit, dirty-worktree state, Python and GitHub run context. Checksums are emitted
with LF bytes so GNU verification works across Windows builds and Linux consumers.
Checksums detect changed bytes; they do not by themselves authenticate origin.

Once the repository is public, a separate Ubuntu job downloads the same artifact,
verifies its checksums and uses GitHub's build-provenance attestation action. Only
that job has OIDC and attestation-write permissions. It does not check out source,
install packages or execute repository code; its sole shell command is the fixed
checksum verification command. Attestation subjects are the wheel/source archives.
Private-repository runs explicitly report that attestation is skipped by this
workflow. No run creates a GitHub Release, changes a version or publishes a package.

`GitHub's attestation availability and verification guidance <https://docs.github.com/en/actions/how-tos/secure-your-work/use-artifact-attestations/use-artifact-attestations>`_
explains the public/private plan restrictions. After an actual successful hosted
run, download the retained archives and verify them before any future publication::

   sha256sum --strict --check SHA256SUMS
   gh attestation verify <archive> --repo sysblacksmith/STV_sphinx-traceability-view

Compare the attestation's source commit and workflow identity with the approved
candidate. Later release preparation must retain the exact qualified bytes,
checksums, provenance and qualification evidence; rebuilding the same filename
is not evidence of the same artifact. No attestation exists until a hosted job
actually generates one. A locally generated build-info file is not a signature.

Branch-protection proposal and remaining owner steps
--------------------------------------------------------------------------------

The current main branch is unprotected. GitHub rejects ruleset access for the
present private-plan combination; detailed protection access is also denied to
the integration. No remote setting was changed.

``.github/main-protection.json`` is a concrete, unapplied owner-review proposal:
require both named CI checks on an up-to-date branch, require a pull request and
resolved conversations, enforce protections for administrators, and prohibit
force pushes/deletion. It specifies zero peer approvals so a solo maintainer can
merge after checks; it does not claim an independent-review barrier. The owner
can increase the approval count if another reviewer is available.

After changing visibility/plan and obtaining successful hosted status checks,
review the profile and actual check names before applying it through GitHub's
settings/API. No visibility/plan change, hosted workflow dispatch or protection
mutation is authorized by this preparation alone. PRSA-006 remains partially
remediated until those hosted checks, actual provenance and chosen remote
protections can be confirmed. See :need:`STV_PR_012` and
:doc:`test-execution/prsa-006-fix/index` for local evidence and remaining limits.
