Traceability
============

Derived records are draft design obligations, not implemented coverage. The
accepted stakeholder baseline is unchanged. System-boundary concerns derive
through system requirements; local interaction obligations channel directly
from software to stakeholder requirements with rationale in each SWR.

Requirement refinement and backlinks
------------------------------------

.. needtable::
   :filter: type in ['shr', 'sysr', 'swr']
   :columns: id;title;type;status;derives_from;derives_from_back;allocated_to

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
