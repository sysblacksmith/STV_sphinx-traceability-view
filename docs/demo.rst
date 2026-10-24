Explore this project's traces
=============================

This page uses the implementation against the project's current Needs.
Open stakeholder entry pages from the project root, or follow relationships
from the software requirement below. Each view keeps its own exploration and
viewport. Details show the final published Need body; the summary link opens
its original page in a new tab.

MVP exploration
------------------------------

The :doc:`change-requests/STV_CR_006_centered-layout-and-interactive-seeds` increment
has completed owner inspection and concept acceptance. The project overview immediately shows five stakeholder
requirements; Previous and Next browse the remaining pages. Initial ordinary
rows use numeric ID order. Fresh layouts center parents over visible children;
expanding/collapsing links keeps existing horizontal positions and the clicked
level stationary. Other levels move only when more vertical room is needed.
Reset viewport fits the current scene without rearranging it.
Use Starting Need in either view to search IDs or titles, select a suggestion
with the arrow keys and Enter, or confirm an exact existing ID. Project overview
returns that view to its first page. Invalid input keeps the current graph.

In Software entry below, expand ``derives from`` to inspect the upward link
to STV_SYS_001, then ``allocated to`` for the downward link to
STV_SWE_DIRECTIVE. Expand the latter's incoming allocated requirements for a
fan-in example. Clear links should take direct paths between facing box edges.
Each viewport is now 975 CSS pixels high. Brief pointer crossings should leave
details closed; continuous hover should open them after about one second.
The Details button opens immediately. Check these behaviors before progressing
to full release verification.

Project entry
-------------

.. traceability-view::

Software entry
--------------

.. traceability-view:: STV_SWR_001

Evidence category rows
-----------------------

The project model follows :ref:`STV_CR_013`: system/software tests and their
executions each have their own row between requirements and architecture.
Tests keep their verification-boundary row even when they verify several
requirement levels. Unclassified evidence uses a labelled fallback row beneath
Software Architecture; Problem Tickets remain below it. Expand verified-by and
executed-by links to explore these records, then Reset viewport to fit new content.

Viewport boundary
-------------------

A thin grey line below the controls and node count marks the upper edge of the
visible graph region. Nodes remain clipped there during pan/zoom; use pan or
Reset viewport to bring clipped content back into view.
