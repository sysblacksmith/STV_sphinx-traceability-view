Getting Started
===============

What is STV?
------------

STV (Sphinx Traceability View) is a Sphinx extension for exploring the
relationships already recorded in a Sphinx-Needs project. It turns those
links into an interactive graph inside your published documentation, helping
you follow a requirement through its related specifications, architecture
and tests and inspect the original information as you go.

Key features
------------

* **Follow the connections that matter:** expand incoming or outgoing
  relationships and collapse branches as you explore.
* **Choose your starting point:** browse a paged project overview, start from
  specific Needs, or search locally by ID or title.
* **Keep the context:** read rich published details in the view, or open the
  original Need page in a new tab.
* **Explore independently:** use multiple views, keyboard controls, zoom and
  pan without changing another view's exploration.
* **Share static documentation:** readers use the generated HTML offline or
  through static HTTP hosting without installing STV or running a backend.

See STV in action
-----------------

**Open the live demonstration:** :doc:`Explore this project's traces <demo>`.

The demonstration uses this project's own requirements, architecture and test
traceability data. Try the project overview or the software-entry view, expand
a relationship group, and use Details to inspect a Need. Use Starting Need to
search for another ID or title. Each view retains its own exploration.

Installation
------------

Install STV in the Python environment used to build your Sphinx documentation.

.. include:: ../README.rst
   :start-after: .. stv-compatibility-start
   :end-before: .. stv-compatibility-end

Obtain the wheel (``.whl``) for the version you intend to use from
`GitHub Releases <https://github.com/sysblacksmith/STV_sphinx-traceability-view/releases>`_
or from a maintainer-provided development build. From its download directory,
install it with your documentation environment's Python::

   python -m pip install ./sphinx_traceability_view-<version>-py3-none-any.whl

Replace ``<version>`` with the actual wheel version; the placeholder is not a
literal shell argument. For repeatable CI builds, use a specific wheel version.
The published package is also available from PyPI::

   python -m pip install sphinx-traceability-view

For a candidate not yet published, use its qualified wheel instead. See
:doc:`maturity` for the current release-preparation state.

Consumers need the wheel and its Python dependencies. Node, Draw.io and the
shared requirements-tooling checkout used to build STV's own engineering
records are not needed to use the extension in another project.

Quick start
-----------

1. Add STV to the existing ``extensions`` list in your project's ``conf.py``::

      extensions = [
          # Keep your existing extensions here.
          "sphinx_traceability_view",
      ]

   STV loads Sphinx-Needs automatically. Keep your existing Need types and
   relationships: they remain authoritative.

   The default STV mapping expects exactly the five types ``shr``, ``sysr``,
   ``syse``, ``swr`` and ``swe`` used by this project's model. **If your host uses
   other types**, configure ``traceability_view_model`` before building; every
   host type needs a mapping. The examples in
   :doc:`internal-interfaces` explain type levels, project-overview entry types
   and test roles without changing your host schema.

2. Create a page such as ``traceability.rst`` and add it to your existing
   documentation toctree. For a project overview, use::

      Traceability
      ============

      .. traceability-view::

   Alternatively, start from specific existing, visible Need IDs::

      .. traceability-view:: MY_SHR_001 MY_SWE_BACKEND

   Replace the example IDs with IDs from your project. Project overview mode
   requires a type mapped to the ``stakeholder`` role. Multiple directives
   can appear on the same page.

3. Build the documentation with Sphinx's HTML builder::

      python -m sphinx -b html docs docs/_build/html

   Adapt the source and output paths if your project uses a different layout.

4. Open the resulting page directly from the output directory, or serve the
   complete output directory through static HTTP hosting. Keep the entire
   generated output together so local graph data, detail scripts and assets
   remain available.

Separate-occurrence mode is deferred; see :doc:`maturity` for the current
delivery and verification scope.

Further documentation
---------------------

* :doc:`internal-interfaces`: directive syntax, host-model configuration and
  supported integration contracts.
* :doc:`technology-stack`: selected dependencies and compatibility boundaries.
* :doc:`licensing`: STV's MIT license and bundled third-party notices.
* :doc:`requirements-stakeholder` and :doc:`traceability`: the tool's scope and
  its requirements/allocation relationships.
* :doc:`architecture-system` and :doc:`architecture-software`: system and
  software architecture.
* :doc:`verification-plan`, :doc:`test-execution/index` and :doc:`maturity`:
  planned checks, actual evidence and current project status.

The existing Requirements, Architecture, Verification and Validation,
Miscellaneous and Utilities chapters remain available in the navigation.

Classified evidence rows
--------------------------

The project's own demo separates system/software test cases and executions.
For another host, configure ordered levels and per-type placement in
``traceability_view_model``; see :doc:`internal-interfaces`. A test-case type
can select a row by tags, and an execution type can inherit from its case::

   "case": {
       "levels_by_tag": {"test_system": "system_tests", "test_software": "software_tests"},
       "fallback_level": "unclassified_tests",
   },
   "run": {
       "level_from": {
           "relation": "executed_by", "direction": "incoming",
           "levels": {"system_tests": "system_executions", "software_tests": "software_executions"},
       },
       "fallback_level": "unclassified_tests",
   },

These entries belong in the model's ``types`` mapping; use your actual host type,
tag and relationship names. Declare every referenced row in ``levels`` in the
desired order. The project orders stakeholder, system, system tests, system
executions, system architecture, software, software tests, software executions,
software architecture, then unclassified evidence and problems. Classification
uses all published relationships, so navigation never changes a test's boundary.
Fallback nodes are labelled and retain normal links/details. Existing fixed-level
mappings and explicitly selected ``role: test`` side lanes remain supported.

Keep details beside the graph
-------------------------------

Details opens a persistent box in that view's right-hand stack (below the graph
on narrow screens). Reopening an artifact focuses its existing box. Close a box
individually or use Close all details at the right of the control row. Graph
navigation does not clear the stack; hover inspection remains temporary.

Authors can configure capacity in conf.py::

   traceability_view_details_limit = 10

The positive integer limit applies independently to every view. A new artifact
at capacity replaces the oldest open box; focusing/reusing it does not renew age.


Detail boxes target a width of 720 px. Metadata such as status and tags starts
folded; use the little arrow (or focus it and press Enter/Space) to reveal it.
The artifact ID in the copied heading opens the original artifact in a new tab.

Exploration and detail controls
--------------------------------

**Collapse all nodes** clears opened graph relationships while retaining your
current starting objects and open detail cards. **Close all details** remains a
separate operation. On pages with rendered Needs, **Collapse all** and **Expand
all** control their detailed attributes without changing embedded graphs.

**Save as SVG** captures the currently visible graph and detail area, including
its current pan, zoom, clipping and attribute state. It excludes off-screen
content and toolbar controls. Open the resulting self-contained SVG in a browser;
vector editors differ in their support for embedded HTML. Export errors leave
your exploration intact and can be retried after the indicated issue is resolved.

The browser controls file name/location and cancellation. In Firefox, enable
**Settings > General > Files and Applications > Downloads > Always ask you where
to save files** when you want a location dialog. Otherwise the browser can save
to its configured download folder. STV reports that a download was requested;
it cannot confirm that the file was saved.

Authors can independently configure detail text in ``conf.py``::

   traceability_view_tooltip_font_scale = 0.7
   traceability_view_details_font_scale = 0.7

Both defaults are approximately 70% of the previous detail typography. Use 1.0
to restore the previous size. Values must be finite positive numbers. Ordinary
graph labels and original Need page text keep their existing sizes.
