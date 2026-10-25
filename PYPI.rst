STV: Sphinx Traceability View
========================================

STV adds interactive traceability graphs to Sphinx documentation built with
Sphinx-Needs. Explore relationships between requirements and architecture,
expand links, inspect rendered Need details, and save the visible view as SVG.
Generated HTML works offline, including when opened directly from disk.

Installation
------------

Install in the Python environment used to build your documentation::

   python -m pip install sphinx-traceability-view

Browser assets are included; documentation authors do not need Node.js.

Minimal example
---------------

Create ``docs/conf.py`` with the following content. This example explicitly maps
its two Need types; existing projects must map all their own types instead of
replacing their schema::

   project = "Traceability example"
   extensions = ["sphinx_traceability_view"]
   needs_types = [
       {"directive": "shr", "title": "Stakeholder requirement", "prefix": "SH_",
        "color": "#ddeeff", "style": "node"},
       {"directive": "swr", "title": "Software requirement", "prefix": "SW_",
        "color": "#eeffdd", "style": "node"},
   ]
   needs_links = {"traces": {"incoming": "Traced by", "outgoing": "Traces"}}
   traceability_view_model = {
       "levels": ["stakeholder", "software"],
       "types": {
           "shr": {"level": "stakeholder", "role": "stakeholder"},
           "swr": {"level": "software"},
       },
   }

STV loads Sphinx-Needs automatically. Create ``docs/index.rst``::

   Traceability example
   ====================

   .. shr:: Explore requirements
      :id: SH_001
      :traces: SW_001

      Readers can explore related requirements.

   .. swr:: Render an interactive graph
      :id: SW_001

      The documentation contains a traceability view.

   .. traceability-view:: SH_001

Build and open ``docs/_build/html/index.html`` in your browser::

   python -m sphinx -W -b html docs docs/_build/html

Compatibility
-------------

* Python: declared minimum 3.10; recorded development verification uses 3.13.17.
* Sphinx 8.1.3 and Sphinx-Needs 8.2.0 are the pinned host dependencies.
  Compatibility with other versions has not been established.
* Recorded automated browser verification uses Windows 11 and desktop Firefox
  158.0.1. Other operating systems have not been qualified.
* Manual checks were also reported for desktop Edge, Android Chrome and iPhone Safari,
  without recorded browser versions. These are supplementary checks rather than
  a versioned support guarantee. Complex graphs benefit from a larger screen;
  touch interaction is not separately qualified.

Links and license
-----------------

* `Documentation and demo <https://sysblacksmith.github.io/STV_sphinx-traceability-view/>`_
* `Source repository <https://github.com/sysblacksmith/STV_sphinx-traceability-view>`_
* `Issue tracker <https://github.com/sysblacksmith/STV_sphinx-traceability-view/issues>`_

STV's own code is licensed under the
`MIT License <https://github.com/sysblacksmith/STV_sphinx-traceability-view/blob/main/LICENSE>`_.
Bundled browser components retain their MIT, ISC, BSD-3-Clause, Apache-2.0,
EPL-1.0 and EPL-2.0 terms. Distributions include the required notices and source
references; see the
`licensing documentation <https://sysblacksmith.github.io/STV_sphinx-traceability-view/licensing.html>`_.
