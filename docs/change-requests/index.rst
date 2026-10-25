Change Requests
===============

Records use stable project-prefixed sequence numbers in original request order,
not retrospective file creation time. The initial request is reconstructed from
available evidence; see its provenance. Canonical requirement IDs and historical
acceptance records remain unchanged.

Each request is a ``change_request`` Need with Draft / Accepted / Implemented
status. Implementation status describes completed agreed scope; requirement
acceptance, verification and release approval remain separate.

.. needtable::
   :filter: type == 'change_request'
   :columns: id;title;status

.. toctree::
   :glob:
   :maxdepth: 1

   STV_CR_*
