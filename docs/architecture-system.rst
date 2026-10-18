Architecture View for System
============================

Proposed architecture, not an implemented system. See :ref:`STV_ADR_001`.

.. raw:: html

   <object type="image/svg+xml" data="system-architecture.svg" style="width:100%;height:auto;aspect-ratio:800/570" aria-label="Interactive architecture diagram with links to Need objects">
     <a href="system-architecture.svg">Open linked architecture diagram</a>
   </object>

Boundary and deployment
-----------------------

The product consists of :need:`STV_SE_BUILD` and :need:`STV_SE_BROWSER`.
The author runs Sphinx on the host project. Readers open the generated files
locally or through a static server. No application server, database or remote
API belongs to this architecture. Runtime state lives in each page instance;
persistence across reloads is not required by the baseline.

The host remains authoritative for Needs and broken-link validation. The
extension rejects invalid invocations and model mappings but renders available
trace data even when host validation reports dangling targets. The generated
bundle is a build-time snapshot; rebuilding incorporates source changes.

System interfaces
-----------------

* Author input: RST invocation and host configuration; see :doc:`internal-interfaces`.
* Host input: completed Needs collection, relation definitions and rendered
  Need fragments. Adaptation is isolated behind the build integration.
* Build output: HTML, graph/data scripts, full-detail fragments and local runtime
  assets. Browser exploration needs no network fetch.
* Reader output: bounded interactive view, full-object overlays and original
  documentation links, with Firefox/Windows as the initial verification target.

Error ownership
---------------

Missing/unknown seed or invalid required model mapping: extension build error.
Missing trace target: retain identity in the graph; host validation owns failure.
Over-cap interaction: refuse the transition and announce why, without changing
view state. Offline external links remain external and cannot be guaranteed
available; see the design review gaps in :doc:`review`.

Diagram source: ``architecture/diagrams/system-architecture.drawio``.
Edit in Draw.io and export SVG; element boxes link to their Need records.

Selected external dependencies
-------------------------------

The host uses Python, Sphinx and Sphinx-Needs at the accepted baseline versions.
The build integration adds Beautiful Soup for HTML extraction. Its distributed
runtime contains ELK.js, D3 zoom/selection and Floating UI; all are locally
bundled. Node/npm, esbuild, Hatchling, pytest, Selenium and geckodriver are
maintainer or verification tools, not required reader services. Versions,
licenses and boundary allocations are in :doc:`technology-stack`.
The complete handover is :doc:`implementation-plan`.
