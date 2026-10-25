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
   :maxdepth: 1

   STV_CR_001_initial-project-request
   STV_CR_002_starting-nodes
   STV_CR_003_usability-problems
   STV_CR_004_problem-report-handover
   STV_CR_005_control-order
   STV_CR_006_centered-layout-and-interactive-seeds
   STV_CR_007_record-folder-layout
   STV_CR_008_component-directories
   STV_CR_009_requirement-filenames-and-test-levels
   STV_CR_010_consolidated-test-specifications
   STV_CR_011_mit-license
   STV_CR_012_release-cancellation-and-cleanup
   STV_CR_013_artifact_vertical_target_position
   STV_CR_014_persistent-right-side-details
   STV_CR_015_collapse-all-nodes
   STV_CR_016_save-current-view-as-svg
   STV_CR_017_configurable-detail-font-size
   STV_CR_018_page-wide-need-attribute-controls
