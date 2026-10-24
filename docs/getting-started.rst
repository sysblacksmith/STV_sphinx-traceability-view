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
`GitHub Releases <https://github.com/sysforger/STV_sphinx-traceability-view/releases>`_
or from a maintainer-provided development build. From its download directory,
install it with your documentation environment's Python::

   python -m pip install ./sphinx_traceability_view-<version>-py3-none-any.whl

Replace ``<version>`` with the actual wheel version; the placeholder is not a
literal shell argument. For repeatable CI builds, use a specific wheel version.
The first stable release is still being prepared; these instructions do not
imply that a stable release has already been published.

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
