Test-case specification
=======================

Cases are organized by the verification boundary they exercise. System tests
exercise the integrated tool through Sphinx, the browser or package installation.
Software tests exercise individual implementation components. Classify by the
procedure, not merely by the prefixes of linked requirements: one system test
may also provide evidence for software requirements without being duplicated.

Canonical IDs, requirement links, latest results and historical execution
records are retained. A folder move does not imply a new run or acceptance.
Software unit scripts live with their owning components; integrated system
scripts remain under :doc:`../test-scripts/index`.

.. toctree::
   :maxdepth: 2

   system-tests
   software-tests
