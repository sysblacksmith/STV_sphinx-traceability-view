Implemented behavioral state machines
======================================

The machines below describe the implemented build, exploration and inspection
lifecycles. They coordinate through an immutable build identity and per-view
request tokens. Occurrence mode remains deferred. Implementation progress and
executed evidence are recorded in :doc:`maturity`; the accepted target contracts
remain in :doc:`internal-interfaces`.

.. raw:: html

   <object type="image/svg+xml" data="state-machine.svg" style="width:100%;height:auto;aspect-ratio:1300/1150" aria-label="Build, exploration and detail state transitions">
     <a href="state-machine.svg">Open behavioral state diagram</a>
   </object>

Editable source: ``architecture/diagrams/state-machine.drawio``; adjacent SVG
is exported with Draw.io and published interactively.

Build lifecycle
---------------

Owner: ``src/sphinx_traceability_view/__init__.py``, ``directives.py``,
``graph.py``, ``details.py`` and ``bundle.py``. Initial state is collected
invocations; terminal states are finalized output or failed build. Hidden Needs
and their incident edges never enter the snapshot. Published detail fragments
are keyed by content hash; manifests name the required revision explicitly.
Copied host relationship wrappers lose hidden-target references; deliberately
published prose and ordinary author links are preserved. Executable URL schemes
are rejected, including active data URLs in replaced embeds; permitted data
images remain static resources.

.. list-table:: Build transitions
   :header-rows: 1
   :widths: 18 25 37 20

   * - From / event
     - Guard
     - Action / destination
     - Coverage
   * - Collection / directive
     - At most 200 distinct seeds
     - ``TraceabilityView.run`` saves serializable invocation with location;
       remain in collection. Excess seeds produce a directive error.
     - :need:`STV_SWR_001`, :need:`STV_SWR_026`; ``tests/test_build.py``
   * - Collection / write-started
     - HTML builder, valid model, visible seeds and portable original URLs
     - ``prepare`` builds snapshot and copies assets; pending output.
       Invalid input fails before writing views.
     - :need:`STV_SYS_001`, :need:`STV_SYS_002`; ``test_cross_page_bundle``, ``test_invalid_seed_source_location``
   * - Pending / build-finished
     - No fatal exception; every local rendered Need exists
     - ``finish`` extracts safe portable fragments, emits immutable files, then patches
       STV-owned identity attributes; finalized output.
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`; ``test_cross_page_bundle``
   * - Pending / extraction or write failure
     - Missing page/body or filesystem error
     - Raise SphinxError; pending marker remains, no finalized view is claimed.
       Existing content-addressed files remain immutable.
     - :need:`STV_SWR_027`; ``test_failed_finalization_retains_pending_page_and_previous_assets``, ``test_prior_fatal_exception_is_not_replaced_by_bundle_generation``
   * - Existing environment / purge or rebuild
     - Document reread/deleted
     - ``purge`` removes old invocation. ``outdated`` requests full reread
       when views exist; rebuild follows the same collection path.
     - :need:`STV_SWR_018`; ``tests/test_build.py``

Exploration lifecycle
---------------------

Owner: ``frontend/src/state.js``, ``layout.js`` and ``view.js``. Initial state
contains all explicit seeds or the collapsed project root. Only seeds or the
open current project's entry page are reachability roots. Remembered expansions
of hidden descendants and inactive pages do not create visibility roots.
The 200-node cap includes missing objects and the synthetic project root.

.. list-table:: Exploration transitions
   :header-rows: 1
   :widths: 18 25 37 20

   * - From / event
     - Guard
     - Action / destination
     - Coverage
   * - Committed / toggle group or project root
     - Available group; nonempty entries for root
     - ``transition`` clones state; ``visible`` traverses open groups from
       active roots; candidate state. Descendant expansion memory survives collapse.
     - :need:`STV_SWR_003`, :need:`STV_SWR_007`, :need:`STV_SWR_025`; ``frontend/test/state.test.js``
   * - Committed / Previous or Next
     - Root open; valid page index
     - Save outgoing page's expansions into candidate map; restore target
       page's expansions; candidate state.
     - :need:`STV_SWR_052`; project pages Node case
   * - Candidate / capacity validation
     - At most 200 visible nodes
     - ``view.update`` measures staged nodes and calls ``compute``; laying out.
       Over-limit/invalid command returns original state and diagnostic.
     - :need:`STV_SWR_043`, :need:`STV_SWR_044`; capacity Node case
   * - Laying out / successful completion
     - Current request token; valid finite nonoverlapping geometry
     - Commit scene, page and expansion state together; close old details;
       restore focus; committed state.
       Preserve the current control within the view; fall back to the initiating
       surviving control if its focused descendant disappears. A late completion
       does not pull focus back after the user has moved outside that view.
     - :need:`STV_SWR_008`, :need:`STV_SWR_037`; layout Node case and browser case
   * - Laying out / stale completion
     - Newer request exists
     - Discard geometry; remove staged measurement elements; newer request owns state.
     - :need:`STV_SWR_044`; ``test_async_layout_failure_and_stale_completion``
   * - Laying out / failure
     - Solver or geometry error
     - Preserve committed scene and state; announce failure. On first layout,
       retain starting summaries; expose Retry. Retry reuses committed state.
     - :need:`STV_SWR_044`; ``test_async_layout_failure_and_stale_completion``
   * - Committed / zoom or pan
     - Within view; pointer background or toolbar control
     - D3 transforms edges and nodes together; exploration state unchanged;
       dismiss details. Focus navigation pans off-screen controls into view.
       Initial layout and Reset align the first occupied band with the viewport;
       native focus scrolling is folded into the same D3 transform.
     - :need:`STV_SWR_038`, :need:`STV_SWR_039`, :need:`STV_SWR_040`; browser cases

Inspection lifecycle
--------------------

Owner: ``frontend/src/inspect.js``. Initial and terminal state is closed.
Each open increments a token; late fragment/position completions cannot insert
into a different inspection. Promises cache by build identity and Need ID.
The project root and missing targets never request details.

.. list-table:: Inspection transitions
   :header-rows: 1
   :widths: 18 25 37 20

   * - From / event
     - Guard
     - Action / destination
     - Coverage
   * - Closed / hover or Details activation
     - Resolved real Need
     - ``open`` creates labeled nonmodal panel and loading message;
       Floating UI owns position/listeners; loading state.
     - :need:`STV_SWR_033`, :need:`STV_SWR_050`; ``test_offline_exploration``
   * - Loading / script registered
     - Current inspection token
     - Rebase URLs, namespace IDs and IDREFs, insert static host fragment;
       open state. Local resource scripts require no fetch or service.
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`; detail and browser cases
   * - Loading / asset failure
     - Current token
     - Show explicit local-asset error; error state. Failed script requests
       are evicted from cache for retry on next open.
     - :need:`STV_SWR_033`; ``test_missing_placeholder_and_detail_error``
   * - Loading, open or error / Escape or Close
     - Panel exists
     - ``close(true)`` invalidates token, removes panel and position listeners,
       restores trigger focus; closed.
     - :need:`STV_SWR_034`, :need:`STV_SWR_050`; browser case
   * - Loading, open or error / pointer departure
     - Grace period elapsed; neither panel nor trigger hovered/focused
     - ``schedule`` calls ``close``; closed. Pointer/focus return cancels dismissal.
     - :need:`STV_SWR_033`; ``test_offline_exploration``
   * - Loading, open or error / new object, scene commit, pan or zoom
     - New inspection or changed scene
     - Close previous panel, invalidate async completion, release listeners;
       closed or new loading state.
     - :need:`STV_SWR_038`; browser cases

Source entry points
-------------------

* :download:`Lifecycle <../src/sphinx_traceability_view/__init__.py>`
* :download:`Directive <../src/sphinx_traceability_view/directives.py>`
* :download:`Graph <../src/sphinx_traceability_view/graph.py>`
* :download:`Detail extraction <../src/sphinx_traceability_view/details.py>`
* :download:`Bundle emission <../src/sphinx_traceability_view/bundle.py>`
* :download:`Exploration state <../frontend/src/state.js>`
* :download:`Layout <../frontend/src/layout.js>`
* :download:`View and async commit <../frontend/src/view.js>`
* :download:`Inspection <../frontend/src/inspect.js>`

Transition tables distinguish code behavior from executed verification. A linked
requirement or test source is not itself a passing result; consult the coverage
and release execution records from :doc:`maturity`.
