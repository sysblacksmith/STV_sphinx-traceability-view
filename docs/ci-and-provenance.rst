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
full engineering Sphinx build, graph validation and diagram-link checks use the
versioned tools/method package in this checkout and run in CI without a private
method checkout or credentials.

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



Public evidence presentation
--------------------------------------------------------------------------------

Canonical requirement, case and execution records remain visible in the website.
Historical records are rendered with private tooling repository locations omitted.
Logs, inventories, screenshots and binary
attachments remain unchanged in the engineering checkout. Historical raw downloads and execution
screenshots are excluded from the website; source-copy downloads are disabled.
This publication policy does not rewrite previous hashes, outcomes or acceptance.
It does not remove any material from Git history or qualify a public repository
visibility change. The final HTML tree and downloadable archives are scanned before
publication; a private tooling reference fails the check.


GitHub Pages publication
--------------------------------------------------------------------------------

``.github/workflows/pages.yml`` is manual-only and builds main with read-only
repository permissions. It installs the pinned documentation dependencies, runs
the staged publication builder and validates the requirement graph and published
diagram targets. Only ``docs/_build/html`` is uploaded as the Pages artifact;
previous builds, diagnostics and local audit reports are outside that tree.

The ``publish`` input defaults to false: this prepares a downloadable preview
artifact without deployment. When explicitly selected, deployment additionally
requires a public repository and main. A separate job uses the ``github-pages``
environment with Pages/OIDC write permissions; it only deploys the artifact and
does not check out or execute project code. Actions are pinned to full commits.

First-publication procedure:

#. Merge the preparation and obtain successful Validation checks for main.
#. Run **Documentation Pages** on main with ``publish`` unchecked. Download its
   artifact and review the site, including the demo and detail navigation.
#. Confirm the final repository/history disclosure review, then make the
   repository public in its GitHub settings.
#. Apply the reviewed ``.github/main-protection.json`` profile after confirming
   the required check names. Set Pages **Source** to **GitHub Actions** and
   restrict the ``github-pages`` deployment environment to main.
#. Run **Documentation Pages** on main with ``publish`` checked. Verify the
   deployed site while signed out, including nested pages, STV details, diagrams
   and downloads. Add the verified URL to the repository website field.

The expected site is
`STV documentation <https://sysblacksmith.github.io/STV_sphinx-traceability-view/>`_.
These instructions describe the prepared workflow; they do not claim that remote
settings have been applied or that deployment has succeeded. Publishing docs
does not create a software release. Candidate attestations remain a separate
manual provenance operation.

For GitHub's settings and deployment requirements, see
`configuring a publishing source <https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site>`_
and `custom Pages workflows <https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages>`_.
