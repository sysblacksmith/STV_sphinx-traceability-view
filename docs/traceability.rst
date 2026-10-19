Traceability
============

System-boundary concerns derive through system requirements; software-local
interaction obligations channel directly to stakeholder requirements with
rationale in each SWR.

Requirement refinement and backlinks
------------------------------------

.. needtable::
   :filter: type in ['shr', 'sysr', 'swr']
   :columns: id;title;type;status;derives_from;derives_from_back;allocated_to;verifies_back

System allocations
------------------

.. needtable::
   :filter: type in ['sysr', 'syse']
   :columns: id;title;allocated_to;allocated_to_back

Software allocations and containment
------------------------------------

.. needtable::
   :filter: type in ['swr', 'swe']
   :columns: id;title;derives_from;allocated_to;allocated_to_back;part_of;part_of_back

End-to-end paths
----------------

The shared validator exports the complete derived matrix to
``docs/_build/traceability.csv``. Direct channeled paths have an empty system
requirement cell; conventional paths include SHR, SYS, SWR, system element and
software element. The canonical authored source remains RST, not the CSV.

Requirement verification and execution paths
--------------------------------------------------------------------------------

The canonical :doc:`test-cases/index` records use ``verifies`` to link each
procedure to its requirements and ``executed_by`` to retain individual attempts.
The case's ``last_result`` summarizes its latest linked execution, independently
of design acceptance and requirement verification. Deferred occurrence-mode
cases remain planned and unexecuted.

.. needtable::
   :filter: type == 'test_case'
   :columns: id;title;verifies;last_result;executed_by

.. needtable::
   :filter: type == 'test_execution'
   :columns: id;executed_by_back;result;executed_at;evidence

Run the shared validator with ``--require-test-coverage`` and
``--test-csv docs/_build/test-traceability.csv`` to check and export these paths.
The CSV is derived; the RST case and execution records remain authoritative.
