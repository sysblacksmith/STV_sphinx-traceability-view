Interactive traceability view
=============================

Sphinx Traceability View (STV) adds interactive graphs to your Sphinx-Needs
documentation. Follow relationships between requirements, architecture and
tests, expand connections, search by ID or title, and inspect Need details
beside the graph.

The generated HTML works offline or on static hosting, without a backend.
Readers do not need to install STV.

* `Live demo <https://sysblacksmith.github.io/STV_sphinx-traceability-view/demo.html>`_
* `Documentation <https://sysblacksmith.github.io/STV_sphinx-traceability-view/>`_

Installation
------------

Install STV in the Python environment used to build your documentation::

   python -m pip install sphinx-traceability-view

.. stv-compatibility-start

The current package requires Python 3.10 or newer and pins Sphinx 8.1.3,
Sphinx-Needs 8.2.0 and Beautiful Soup 4.13.5. Check compatibility with the host's
documentation dependencies before installation. Only the ``html`` builder is
supported when a traceability view is present. Each view supports up to 200
visible graph nodes. On Windows, use a short HTML output path when opening
files directly in Firefox.

.. stv-compatibility-end

Quick start
-----------

1. Add STV to the existing ``extensions`` list in your ``conf.py``::

      extensions = [
          # Keep your existing extensions here.
          "sphinx_traceability_view",
      ]

   STV loads Sphinx-Needs automatically and uses your existing Needs and
   relationships. If your Need types differ from the defaults below,
   configure the model before building.

2. Add a view to an RST page included in your documentation's toctree.
   Start with specific existing Need IDs::

      .. traceability-view:: MY_REQ_001 MY_COMPONENT

   Replace these IDs with IDs from your project. For a project overview, omit
   the IDs (requires a type with the ``stakeholder`` role)::

      .. traceability-view::

3. Build your documentation with the HTML builder::

      python -m sphinx -b html docs docs/_build/html

   Adapt the paths to your project. Open the generated page directly from disk
   or publish the complete HTML output directory on static hosting.

Host model configuration
------------------------

The default mapping expects exactly the five Need types ``shr``, ``sysr``,
``syse``, ``swr`` and ``swe``. For other schemas, set
``traceability_view_model`` in your ``conf.py``. For example, a project with
``goal``, ``requirement`` and ``component`` types can use::

   traceability_view_model = {
       "levels": ["goals", "requirements", "components"],
       "types": {
           "goal": {"level": "goals", "role": "stakeholder"},
           "requirement": {"level": "requirements"},
           "component": {"level": "components"},
       },
       "accepted_statuses": ["accepted"],
   }

Map every configured Need type using its directive name as the key, and adapt
``accepted_statuses`` to your status vocabulary. Relationships come from your
``needs_links`` configuration and require incoming and outgoing labels.

See the `configuration reference
<https://sysblacksmith.github.io/STV_sphinx-traceability-view/internal-interfaces.html>`_
for test types, row placement and further options.

Using a view
------------

Expand incoming or outgoing relationships to follow connections. Use
**Starting Need** to search by ID or title and **Details** to keep information
beside the graph. Multiple views on a page work independently.

* **Collapse all nodes** clears expanded relationships while keeping your
  starting objects and open detail cards.
* **Close all details** clears the detail cards.
* **Save as SVG** exports the currently visible graph and detail area.
* **Remember my current view** saves starting objects, expanded connections,
  detail cards, positions and pan/zoom across reloads in the same browser.
  Disable it to clear the saved state.

Remembered views stay local to the browser; clearing site data removes them.
Persistence when opening files directly depends on browser storage support.

See `Getting Started
<https://sysblacksmith.github.io/STV_sphinx-traceability-view/getting-started.html>`_
for further usage instructions.

Support
-------

Report problems through `GitHub Issues
<https://github.com/sysblacksmith/STV_sphinx-traceability-view/issues>`_.
Include the STV, Sphinx and Sphinx-Needs versions, steps to reproduce, and any
relevant error messages or screenshots.

Licensing
---------

Copyright (c) 2026 Henning Heikes. STV-owned code and documentation are licensed
under the MIT License; see `LICENSE <LICENSE>`_. Bundled third-party components
retain their own licenses. See the `licensing documentation
<https://sysblacksmith.github.io/STV_sphinx-traceability-view/licensing.html>`_
for notices and source information.
