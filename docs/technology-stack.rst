Technology stack and dependency decisions
=============================================

Selected dependencies, responsibilities and delivery constraints.

.. _browser-runtime:

Browser runtime
-------------------

.. list-table:: Selected browser dependencies
   :header-rows: 1
   :widths: 24 14 16 46

   * - Dependency
     - Version
     - License
     - Responsibility and boundary
   * - ELK.js
     - 0.10.0
     - EPL-2.0
     - Initial node ordering suggestions for STV_SWE_LAYOUT; STV enforces final semantic bands and routes final edges.
   * - d3-zoom
     - 3.0.0
     - ISC
     - Pointer pan/zoom and programmatic keyboard transforms in STV_SWE_RENDER.
   * - d3-selection
     - 3.0.0
     - ISC
     - Bind the D3 zoom behavior to a view root; not a framework for application state.
   * - @floating-ui/dom
     - 1.7.4
     - MIT
     - Position and resize the full-detail overlay in STV_SWE_INSPECT.
   * - Browser DOM, SVG, CSS and Pointer Events
     - Firefox stable
     - Browser platform
     - Semantic HTML nodes/controls, SVG edges, keyboard focus and overlay content.

Load ``elkjs/lib/elk.bundled.js`` without ``workerUrl``. Its algorithm runs
locally; do not introduce worker loading or runtime module requests for the MVP.
The pinned package and API are documented by the
`ELK.js project <https://github.com/kieler/elkjs>`_. ELK positions are advisory:
the final level and test-placement rules are defined in
:doc:`implementation-plan`. Generic graph layers are not the semantic model.

`D3 zoom <https://d3js.org/d3-zoom>`_ owns only the viewport transform. Native
DOM controls remain keyboard reachable. Do not attach node navigation to drag
gestures or let control clicks propagate into the original-object anchor.

Use Floating UI ``computePosition``, ``offset``, ``flip``, ``shift``, ``size``
and ``autoUpdate`` for geometry and cleanup. STV owns hover retention,
keyboard activation, dismissal and focus restoration; positioning alone does
not implement these interactions. See the official
`positioning API <https://floating-ui.com/docs/computeposition>`_ and
`size middleware <https://floating-ui.com/docs/size>`_.

No React, Cytoscape, D3 force simulation, external graph service or Graphviz
executable is required. Native HTML is chosen to retain focusable controls and
full rendered Need content. ELK avoids writing a general graph-ordering solver;
STV still owns the domain-specific constraints that a generic solver does not
guarantee. These are considered choices, not unspecified future candidates.

.. _build-runtime:

Python build-time dependencies
----------------------------------

.. list-table:: Host and extension dependencies
   :header-rows: 1
   :widths: 24 14 16 46

   * - Dependency
     - Version
     - License
     - Responsibility
   * - Python
     - 3.10+
     - PSF
     - Build extension and portable path/JSON processing.
   * - Sphinx
     - 8.1.3
     - BSD-2-Clause
     - Host extension lifecycle, directives and HTML builder.
   * - Sphinx-Needs
     - 8.2.0
     - MIT
     - Host model, resolved Needs and original rendered objects.
   * - Beautiful Soup (beautifulsoup4)
     - 4.13.5
     - MIT
     - Parse final HTML with the standard-library html.parser; extract Need fragments and rebase attributes.

The host versions remain the accepted initial compatibility baseline.
Beautiful Soup is the only new Python library needed by the product build
path; no lxml binary dependency is needed. Its parser selection is explicit,
so developer machines cannot silently choose different installed parsers.
The official `Beautiful Soup documentation
<https://www.crummy.com/software/BeautifulSoup/bs4/doc/>`_ describes this API.

Use the pinned Sphinx-Needs ``SphinxNeedsData.get_needs_view()`` interface only
inside the write phase. Confine this version-sensitive dependency to the ``graph/`` component
(:need:`STV_SWE_GRAPH`).
The installed 8.2.0 source confirms that calling it resolves and freezes data;
calling it during read/collection would be incorrect. Public host references:
`Sphinx application API <https://www.sphinx-doc.org/en/master/extdev/appapi.html>`_
and `Sphinx-Needs Python API
<https://sphinx-needs.readthedocs.io/en/8.2.0/api.html>`_.

Maintainer and verification tools
-------------------------------------

.. list-table:: Tools not needed by readers
   :header-rows: 1
   :widths: 24 14 16 46

   * - Tool
     - Version
     - License
     - Use
   * - Node.js / npm
     - Node 22+; lockfile v3
     - Upstream notices
     - Maintainer-only dependency installation, tests and asset bundling.
   * - esbuild
     - 0.25.12
     - MIT
     - Produce one classic IIFE runtime and preserve dependency notices.
   * - Hatchling
     - 1.27.0
     - MIT
     - Build the Python wheel with prebuilt JS/CSS assets.
   * - build
     - 1.3.0
     - MIT
     - Standard Python wheel/sdist build frontend.
   * - pytest
     - 8.4.2
     - MIT
     - Python, Sphinx integration and browser acceptance checks.
   * - Selenium
     - 4.35.0
     - Apache-2.0
     - Drive installed release Firefox on Windows.
   * - geckodriver
     - Compatible with tested Firefox
     - MPL-2.0
     - Firefox WebDriver bridge; record the exact version per release run.
   * - Node test runner / assert
     - Included with Node
     - Node upstream notices
     - Pure JavaScript state and geometry checks without another test framework.
   * - Draw.io desktop
     - Existing authoring tool
     - Upstream distribution
     - Editable architecture sources and SVG exports via shared tooling.

Use Selenium with an explicit Firefox binary and pre-provisioned geckodriver.
Do not depend on driver downloads during offline verification. Driver selection
follows Mozilla's `compatibility table
<https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html>`_.
Record actual Firefox, Windows and driver versions; do not freeze the browser
to an old release to simplify tests. Selenium supports the
`Firefox WebDriver workflow
<https://www.selenium.dev/documentation/webdriver/browsers/firefox/>`_.
Playwright is not selected for release-browser verification because its Firefox
requires patches rather than using the branded release binary, as documented
in `Playwright browser support <https://playwright.dev/python/docs/browsers>`_.

Packaging and reproducibility
---------------------------------

Selected manifests live under ``docs/architecture/implementation/``:
``package.json``, ``package-lock.json`` and
``requirements-implementation.txt``. They are implementation inputs, not a
claim that an STV package already exists. Copy the npm manifests into the new
frontend directory unchanged before the first ``npm ci``. The lock captures
exact transitive versions and integrity hashes, not just direct pins.

Python direct versions are pinned for the implementation environment. Capture
a transitive Python lock with hashes when the first wheel is assembled; do not
mistake the direct requirements list for such a lock. Node and npm are needed
by maintainers only. The published wheel and sdist include built JS/CSS and
license notices, so documentation authors install and build with Python alone.
Do not run npm during a Sphinx build or an ordinary wheel installation.

Use esbuild with ``bundle: true``, ``format: 'iife'``, ``platform: 'browser'``,
``target: 'firefox128'``, ``splitting: false`` and ``legalComments: 'eof'``.
The target is a conservative syntax target, not an additional promised browser
version. Maintainer build.js must reject missing source entries and package
stale/missing bundle output as a build failure. See
`esbuild output formats <https://esbuild.github.io/api/#format>`_ and
`Hatch build artifacts <https://hatch.pypa.io/1.13/config/build/#artifacts>`_.

Dependency notices accompany both the wheel and generated documentation.
The owner selected MIT for STV-owned code and documentation on 2026-10-24,
with copyright attributed to Henning Heikes. Bundled libraries retain their
MIT/ISC/BSD-3-Clause/Apache-2.0/EPL-1.0/EPL-2.0 terms. See :doc:`licensing` for the license text,
notices, source availability and the completed pinned-bundle audit scope.
The package metadata uses a combined SPDX expression for these bundled
components and explicitly includes their legal files. Source-availability
notices identify both ELK.js and the underlying Java ELK project; the generated
JavaScript is not described as the preferred source form. No legal or employer
approval is inferred from selecting the project license.

Feasibility evidence and limits
-----------------------------------

On 2026-10-18, a temporary environment installed the exact npm pins and lock.
A Node smoke check laid out an A-B-C-A graph with ELK and produced finite
positions for all three nodes. esbuild bundled all four browser libraries
into an IIFE with 150 inputs, 1,508,230 minified bytes and no dynamic import
expression. Node v24.21.0 and npm 11.19.0 were used. This verifies package/API
availability and bundling, not browser functionality or geometry acceptance.

The roughly 1.5 MB JS cost is explicit. Full project graph and detail data add
to that cost. Use the measurement plan rather than asserting that 200 visible
nodes makes total load size independent of project size. No product runtime,
full Firefox workflow or performance threshold has passed at this design step.

Reproduce the dependency check
----------------------------------

In a temporary copy of ``docs/architecture/implementation/``, run ``npm ci``
then ``node check-stack.mjs``. The check validates cyclic ELK positions and
bundles all selected browser libraries in memory without unresolved imports.
It does not open a browser or install an STV runtime. The committed stdin-entry
check also passed: 150 bundled inputs, 1,508,228 minified bytes and no unresolved
output imports.

Beautiful Soup 4.13.5 was also installed in the temporary check environment;
html.parser located all 113 current rendered Need objects across five output
pages and retained their ID text and requirement acceptance-criterion content.
This is evidence for extraction on this document set, not proof of every
cross-page resource rewrite or third-party layout.

Compiled ELK dependency notices
-------------------------------

ELK's own EPL-2.0 declaration does not describe all of its generated code.
The pinned upstream build compiles GWT/Guava (Apache-2.0), EMF-GWT (EPL-1.0)
and Xbase/Xtend (EPL-2.0); Babel/Browserify wrappers and the browser Worker shim
have separate notices. See :doc:`licensing` and the source/hash inventory in
``frontend/legal/elk-inventory.json``. Frontend notices derive npm dependencies
from actual esbuild inputs and append maintained compiled-dependency notices.

Patched maintainer tooling
--------------------------------------------------------------------------------

Package runtime remains Python 3.10+. Documentation and implementation tooling
use Python 3.11+ so the patched Pillow release can be installed. Direct versions
are maintained in ``requirements-docs.txt``, the implementation requirements,
and shared ``requirements-tooling.txt``. The latter pins patched pip,
setuptools and certifi for both environments and offline consumer bootstrap.
Pillow is a documentation/plotting dependency, not a base runtime dependency.
The Python 3.10-compatible runtime wheelhouse is refreshed separately and
checked through an offline installed-wheel host. Historical environment logs
remain evidence rather than being updated to the new package versions.

Source distribution boundary
--------------------------------------------------------------------------------

The sdist allowlist in ``pyproject.toml`` selects implementation and browser
sources, prepared runtime assets, audited notices, lockfiles and build inputs.
Hatch ignores VCS file-selection rules for this target, so log-retention
negations cannot widen the archive. Python caches/bytecode are excluded within
selected directories. Engineering documentation and execution evidence remain
in the repository; source packages are for rebuilding the installable extension.
Hatch's generated package metadata and standard metadata files may accompany
these inputs. :need:`STV_PR_010` and :need:`STV_TC_SY_051` retain the
cause and actual archive/rebuilt-wheel regression evidence. Runtime behavior,
state-machine transitions and accepted requirement meanings are unchanged.

Navigation projection policy
-----------------------------

The existing pinned ELK.js supplies ordering suggestions. STV owns deterministic
slot stabilization, semantic-band spacing and final route generation; native
SVG viewBox/CSS origins cover negative extents. Natural numeric ID ordering uses
the browser's English ``Intl.Collator`` with numeric comparison and variant
sensitivity. No dependency or runtime network request is added. See
:ref:`STV_ADR_008` for alternatives and constraints.
