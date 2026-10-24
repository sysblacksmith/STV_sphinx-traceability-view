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

Numeric case identity
----------------------

Canonical test cases use independent category sequences:

* System cases: ``STV_TC_SY_001`` onward.
* Software cases: ``STV_TC_SW_001`` onward.

Allocate the next unused number within the case's verification category; never
recycle numbers or renumber cases merely for sorting or moving a document.
A change of verification category requires an explicit mapped ID migration.

The owner authorized replacing the hash/descriptive IDs on 2026-10-24, then
refined the convention to category prefixes and separate counters. All 99 cases
and live RST references were migrated. Procedures, selectors, requirement links,
statuses, results and execution IDs are unchanged. Numbers follow existing
order within each category. This editorial migration implies no new execution,
acceptance or release qualification. The map retains both original IDs and the
intermediate project-wide numeric IDs.

Original logs, XML/CSV/JSON reports, archived source/artifacts and historical
content hashes retain their original bytes and IDs. Use the mapping to resolve
those historical IDs to current cases; earlier review hashes continue to identify
the original revisions. Current rendered execution references use the new IDs.

* :download:`Old-to-new case IDs and executable selectors <id-migration.json>`
