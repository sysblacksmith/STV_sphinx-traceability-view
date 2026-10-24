Alternate requirements
======================

.. goal:: This is a deliberately long title spanning more than two lines in the fixed summary box while remaining fully available in the original rendered details
   :id: GOAL_A
   :status: approved
   :owner: Fixture owner
   :traces: HARDWARE_A, SYSTEM_A, SOFTWARE_A, MODULE_A, CHECK_A, HIDDEN_A

   This **rich body** has a :need_part:`(fragment)published part`.

   .. list-table:: Rich table

      * - Alpha
        - Beta

   .. image:: pixel.svg
      :alt: Local fixture picture

   `Cross-page link <index.html>`__ and `same object <#GOAL_A>`__.

   .. raw:: html

      <div class="fixture-widget" id="widget"><b>Static widget text</b><img src="pixel.svg" alt="Widget picture"><script>globalThis.STV_WIDGET_EXECUTED = true;</script><label for="widget-field">Widget field</label><input id="widget-field"></div>
      <img src="https://example.invalid/remote.png" srcset="https://example.invalid/remote2.png 2x" alt="Remote media">
      <video poster="//example.invalid/poster.png"><source src="https://example.invalid/movie.mp4"></video>
      <iframe src="https://example.invalid/frame"></iframe>
      <style>.fixture-widget { background-image: url(https://example.invalid/background.png) }</style>

.. hardware:: Hardware node
   :id: HARDWARE_A
   :status: approved
   :traces: CHECK_A

.. system:: System node
   :id: SYSTEM_A
   :status: approved

.. software:: Software node
   :id: SOFTWARE_A
   :status: approved
   :traces: GOAL_A, CHECK_A

.. component:: Module node
   :id: MODULE_A
   :status: approved

.. check:: Shared test
   :id: CHECK_A
   :status: approved

.. goal:: Isolated unaccepted node
   :id: ISOLATED_A

   Isolated body.

.. goal:: Hidden object
   :id: HIDDEN_A
   :hide:

   Hidden body.

.. goal:: Reviewed object with a complete wrapped identifier
   :id: LONG_IDENTIFIER_WITH_MANY_SEGMENTS_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789_ABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789
   :status: reviewed

   Long identity body.
