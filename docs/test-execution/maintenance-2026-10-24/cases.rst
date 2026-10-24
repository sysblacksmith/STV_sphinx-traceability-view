Per-case maintenance executions
========================================

These are development attempts, not a new release qualification. Completion
timestamps below are retained report file completion times in UTC (per-case
finish timestamps were not emitted). Earlier failures and source/artifact
identities remain visible. Latest case results are synchronized independently
of concept acceptance or requirement verification.

.. test_execution:: docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry
   :id: STV_TE_1EA0D25151D74A7C
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/before-path-fix.xml :: docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T12:25:22.452189+00:00

   **Case:** :need:`STV_TC_WINDOWS_PATH`.

   **Inputs:** Original base implementation plus the new regression; expected failure, 298-character asset path.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`before-path-fix.xml <before-path-fix.xml>`, ``docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry``.

.. test_execution:: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data
   :id: STV_TE_1B628A5DEFCC6526
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/path-fix.xml :: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:27:03.318712+00:00

   **Case:** :need:`STV_TC_4594B1E01BC7`.

   **Inputs:** First compact-path component/system verification; before final inventory-copy integration.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`path-fix.xml <path-fix.xml>`, ``src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data``.

.. test_execution:: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_detail_assets_preserve_full_identity_with_compact_deduplicated_paths
   :id: STV_TE_B2B66F9BDF1CFFBB
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/path-fix.xml :: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_detail_assets_preserve_full_identity_with_compact_deduplicated_paths
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:27:03.318712+00:00

   **Case:** :need:`STV_TC_COMPACT_PATHS`.

   **Inputs:** First compact-path component/system verification; before final inventory-copy integration.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`path-fix.xml <path-fix.xml>`, ``src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_detail_assets_preserve_full_identity_with_compact_deduplicated_paths``.

.. test_execution:: docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry
   :id: STV_TE_8691313C00B21F3E
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/path-fix.xml :: docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:27:03.318712+00:00

   **Case:** :need:`STV_TC_WINDOWS_PATH`.

   **Inputs:** First compact-path component/system verification; before final inventory-copy integration.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`path-fix.xml <path-fix.xml>`, ``docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry``.

.. test_execution:: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data
   :id: STV_TE_0D638C0275A29724
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_4594B1E01BC7`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_classic_registration_treats_prototype_keys_and_script_text_as_data``.

.. test_execution:: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_detail_assets_preserve_full_identity_with_compact_deduplicated_paths
   :id: STV_TE_228B20B2EF813704
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_detail_assets_preserve_full_identity_with_compact_deduplicated_paths
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_COMPACT_PATHS`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/bundle/tests/test_bundle.py::test_detail_assets_preserve_full_identity_with_compact_deduplicated_paths``.

.. test_execution:: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_static_details_and_remote_fallback
   :id: STV_TE_B4CE8AA762593317
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_static_details_and_remote_fallback
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_D43DE71AF846`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/detail_build/tests/test_details.py::test_static_details_and_remote_fallback``.

.. test_execution:: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_portable_paths_preserve_queries_and_fragments
   :id: STV_TE_3E753C0867424736
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_portable_paths_preserve_queries_and_fragments
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_8023D1B4838C`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/detail_build/tests/test_details.py::test_portable_paths_preserve_queries_and_fragments``.

.. test_execution:: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_srcset_data_images_and_css_resources
   :id: STV_TE_F974F952B4BAF9DF
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_srcset_data_images_and_css_resources
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_ABB4E85E5F66`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/detail_build/tests/test_details.py::test_srcset_data_images_and_css_resources``.

.. test_execution:: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_active_embed_urls_are_not_retained_as_navigation
   :id: STV_TE_4B5C6B8F24B1A098
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/detail_build/tests/test_details.py::test_active_embed_urls_are_not_retained_as_navigation
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_E6FA25320A8F`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/detail_build/tests/test_details.py::test_active_embed_urls_are_not_retained_as_navigation``.

.. test_execution:: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_failed_finalization_retains_pending_page_and_previous_assets
   :id: STV_TE_AB3AB31683DE7C64
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_failed_finalization_retains_pending_page_and_previous_assets
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_136FE8B1A097`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_failed_finalization_retains_pending_page_and_previous_assets``.

.. test_execution:: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_prior_fatal_exception_is_not_replaced_by_bundle_generation
   :id: STV_TE_10081046B1450184
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_prior_fatal_exception_is_not_replaced_by_bundle_generation
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_B5D550F17384`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_prior_fatal_exception_is_not_replaced_by_bundle_generation``.

.. test_execution:: src/sphinx_traceability_view/graph/tests/test_graph.py::test_hidden_parts_external_and_missing_targets
   :id: STV_TE_814A1F12A1BBC13A
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_hidden_parts_external_and_missing_targets
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_D00DA9F2CD10`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/graph/tests/test_graph.py::test_hidden_parts_external_and_missing_targets``.

.. test_execution:: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[javascript:bad()]
   :id: STV_TE_9586EC686DEFABC6
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[javascript:bad()]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_11FDDB8E8864`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[javascript:bad()]``.

.. test_execution:: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[data:text/html,bad]
   :id: STV_TE_58267D1CD6C96C16
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[data:text/html,bad]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_7D1212345072`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[data:text/html,bad]``.

.. test_execution:: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]
   :id: STV_TE_F73049B2F90A96A6
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_734CF1BFE372`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/graph/tests/test_graph.py::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]``.

.. test_execution:: src/sphinx_traceability_view/model/tests/test_model.py::test_host_normalization
   :id: STV_TE_BA00F16C25D5FA7C
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/model/tests/test_model.py::test_host_normalization
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_287ABDA90FE3`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/model/tests/test_model.py::test_host_normalization``.

.. test_execution:: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change0-levels]
   :id: STV_TE_49642C98E5C0FA07
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change0-levels]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_51B932282614`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change0-levels]``.

.. test_execution:: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change1-types.goal]
   :id: STV_TE_FF8A5C765D35F850
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change1-types.goal]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_C747492F203E`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change1-types.goal]``.

.. test_execution:: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change2-types]
   :id: STV_TE_0984B66A1B7BF510
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change2-types]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_5D3C07D3C5DE`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change2-types]``.

.. test_execution:: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change3-accepted_statuses]
   :id: STV_TE_8E482B9F158BC396
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change3-accepted_statuses]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_FBDDCC607412`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_model[change3-accepted_statuses]``.

.. test_execution:: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[]
   :id: STV_TE_595FE00110891E59
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_3DF9A4D8CF8D`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[]``.

.. test_execution:: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[ ]
   :id: STV_TE_106F45573009D68A
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[ ]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_9316CE9A1843`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[ ]``.

.. test_execution:: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[None]
   :id: STV_TE_F0B33AD9A3EDBAB8
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[None]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_F549DE4D0BF4`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[None]``.

.. test_execution:: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[1]
   :id: STV_TE_B9734B73BC2CD60C
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[1]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_D31601FDD080`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``src/sphinx_traceability_view/model/tests/test_model.py::test_invalid_directional_labels[1]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_usability_smoke[file]
   :id: STV_TE_281973898519845F
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_usability_smoke[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_7441DB459B14`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_usability_smoke[file]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_usability_smoke[http]
   :id: STV_TE_8791048E05CC01B1
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_usability_smoke[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_025DB3F44E8E`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_usability_smoke[http]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_offline_exploration[file]
   :id: STV_TE_4A72E96BA6DE2E1E
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_offline_exploration[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_E0AB07ABA378`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_offline_exploration[file]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_offline_exploration[http]
   :id: STV_TE_F0C2845AEA49F292
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_offline_exploration[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_F6E0695BB399`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_offline_exploration[http]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_project_paging[file]
   :id: STV_TE_92C56796616E739A
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_project_paging[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_E23001FBE2A5`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_project_paging[file]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_project_paging[http]
   :id: STV_TE_21BB65233C33EB7E
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_project_paging[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_CFE6B0377595`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_project_paging[http]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_interactive_seed_smoke[file]
   :id: STV_TE_E7F31A178D716764
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_interactive_seed_smoke[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_5652621CFF4A`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_interactive_seed_smoke[file]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_interactive_seed_smoke[http]
   :id: STV_TE_633C7D44A74AC0EC
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_interactive_seed_smoke[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_A1747C52BC63`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_interactive_seed_smoke[http]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[file]
   :id: STV_TE_DDA147A234F1EB90
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_9E5477EFE2F1`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[file]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[http]
   :id: STV_TE_9D6EBF6A6F0743F7
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_E2A064F091BE`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_async_layout_failure_and_stale_completion[http]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[file]
   :id: STV_TE_FFFF8323BE7629F1
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_7016FADA6FBA`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[file]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[http]
   :id: STV_TE_5479348C2D1ACE13
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_E66A443619C6`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_alternate_model_geometry_details_and_external[http]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[file]
   :id: STV_TE_98FA5AFD1CF5BE75
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_0EBE5120F168`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[file]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[http]
   :id: STV_TE_C907D3DAAB33A698
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_59C06D617036`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_missing_placeholder_and_detail_error[http]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_documentation_visuals
   :id: STV_TE_8D236D778E5397B0
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_documentation_visuals
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_3B2659FB2D0A`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_documentation_visuals``.

.. test_execution:: docs/test-scripts/test_browser.py::test_control_order_smoke[file]
   :id: STV_TE_97A2EA6B2A2DFFD8
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_control_order_smoke[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_535022565896`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_control_order_smoke[file]``.

.. test_execution:: docs/test-scripts/test_browser.py::test_control_order_smoke[http]
   :id: STV_TE_3EA3780EE4C691D4
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_browser.py::test_control_order_smoke[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_06CC5EE46517`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_browser.py::test_control_order_smoke[http]``.

.. test_execution:: docs/test-scripts/test_build.py::test_cross_page_bundle
   :id: STV_TE_226A0A5469B1E2C8
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_cross_page_bundle
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_5C902A5F732E`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_cross_page_bundle``.

.. test_execution:: docs/test-scripts/test_build.py::test_invalid_seed_source_location[UNKNOWN]
   :id: STV_TE_C6840C674379E70A
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_invalid_seed_source_location[UNKNOWN]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_41F176801699`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_invalid_seed_source_location[UNKNOWN]``.

.. test_execution:: docs/test-scripts/test_build.py::test_invalid_seed_source_location[ROOT_A UNKNOWN]
   :id: STV_TE_D18E0A7F3567D77B
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_invalid_seed_source_location[ROOT_A UNKNOWN]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_6C7A64E533AC`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_invalid_seed_source_location[ROOT_A UNKNOWN]``.

.. test_execution:: docs/test-scripts/test_build.py::test_invalid_seed_source_location[HIDDEN_A]
   :id: STV_TE_72C2FBE6E1A2D120
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_invalid_seed_source_location[HIDDEN_A]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_A221103BC26C`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_invalid_seed_source_location[HIDDEN_A]``.

.. test_execution:: docs/test-scripts/test_build.py::test_host_owns_broken_trace_failure
   :id: STV_TE_C22DE139B2E5DF52
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_host_owns_broken_trace_failure
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_DB4FE4CDD257`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_host_owns_broken_trace_failure``.

.. test_execution:: docs/test-scripts/test_build.py::test_incremental_body_change_hidden_and_deleted_objects
   :id: STV_TE_8447E3E24802A7A4
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_incremental_body_change_hidden_and_deleted_objects
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_D1A17B11B9C1`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_incremental_body_change_hidden_and_deleted_objects``.

.. test_execution:: docs/test-scripts/test_build.py::test_seed_capacity_at_directive[200-True]
   :id: STV_TE_BE6098AB231764A5
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_seed_capacity_at_directive[200-True]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_59537D3F286A`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_seed_capacity_at_directive[200-True]``.

.. test_execution:: docs/test-scripts/test_build.py::test_seed_capacity_at_directive[201-False]
   :id: STV_TE_649684CCAC6F8A53
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_seed_capacity_at_directive[201-False]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_A953C70E70B1`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_seed_capacity_at_directive[201-False]``.

.. test_execution:: docs/test-scripts/test_build.py::test_alternate_host_schema_external_metadata_and_parts
   :id: STV_TE_8105F93F757B5B04
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_alternate_host_schema_external_metadata_and_parts
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_3B0D9F21166C`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_alternate_host_schema_external_metadata_and_parts``.

.. test_execution:: docs/test-scripts/test_build.py::test_invalid_mapping_has_entry_path_and_location
   :id: STV_TE_62AC4B0AB9B248F8
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_invalid_mapping_has_entry_path_and_location
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_85BBE1714F96`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_invalid_mapping_has_entry_path_and_location``.

.. test_execution:: docs/test-scripts/test_build.py::test_unsupported_builder_fails_clearly
   :id: STV_TE_5D5D6764322F0A1B
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_unsupported_builder_fails_clearly
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_FC50F6627767`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_unsupported_builder_fails_clearly``.

.. test_execution:: docs/test-scripts/test_build.py::test_host_default_directional_labels_are_used
   :id: STV_TE_CFF8782DE1D60572
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_build.py::test_host_default_directional_labels_are_used
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_DF0D9B21A92D`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_build.py::test_host_default_directional_labels_are_used``.

.. test_execution:: docs/test-scripts/test_package.py::test_clean_wheel_host
   :id: STV_TE_23CFB2E2F59258A0
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_package.py::test_clean_wheel_host
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_F988267D01C9`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_package.py::test_clean_wheel_host``.

.. test_execution:: docs/test-scripts/test_release_seeds.py::test_seed_selection_release[file]
   :id: STV_TE_AD1513DB7BEF1B53
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_release_seeds.py::test_seed_selection_release[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_DE0C60E0BB97`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_release_seeds.py::test_seed_selection_release[file]``.

.. test_execution:: docs/test-scripts/test_release_seeds.py::test_seed_selection_release[http]
   :id: STV_TE_E78BA064DCE82BD6
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_release_seeds.py::test_seed_selection_release[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_9A67DAACB2A4`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_release_seeds.py::test_seed_selection_release[http]``.

.. test_execution:: docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[file]
   :id: STV_TE_0055C4B135295D6D
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_FB72ADBCAE29`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[file]``.

.. test_execution:: docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[http]
   :id: STV_TE_DA00E9FE56E5A125
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_EB0F95BABF84`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_release_seeds.py::test_empty_seed_catalog[http]``.

.. test_execution:: docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[file]
   :id: STV_TE_938B27916A316D0E
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[file]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_25803A2B9F90`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[file]``.

.. test_execution:: docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[http]
   :id: STV_TE_F0A444E2D30EB34A
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[http]
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_F3892D8A1C98`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_release_seeds.py::test_seed_layout_replacement_failure_and_staleness[http]``.

.. test_execution:: docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry
   :id: STV_TE_3E9F0CC9AE6D1527
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/regression.xml :: docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:53.834522+00:00

   **Case:** :need:`STV_TC_WINDOWS_PATH`.

   **Inputs:** Broad development run; source-hashes-at-regression.json and first development artifact.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`regression.xml <regression.xml>`, ``docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry``.

.. test_execution:: frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: concurrent detail requests share one load and retain build identity
   :id: STV_TE_7A6933AA0FFCDB59
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: concurrent detail requests share one load and retain build identity
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_DETAIL_CACHE`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: concurrent detail requests share one load and retain build identity``.

.. test_execution:: frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: failed local detail loading can retry without a stale rejection
   :id: STV_TE_69B410A9F2C8E6AF
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: failed local detail loading can retry without a stale rejection
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_DETAIL_RETRY`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/inspect/tests/inspect.test.js :: STV_SWR_015 STV_SWR_017: failed local detail loading can retry without a stale rejection``.

.. test_execution:: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: competing parents do not displace a separate centered parent
   :id: STV_TE_E62A5652646F52FB
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: competing parents do not displace a separate centered parent
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_2EE2AB9ECAE3`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/layout/tests/layout.test.js :: STV_SWR_056: competing parents do not displace a separate centered parent``.

.. test_execution:: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: cyclic shared geometry with isolated nodes remains deterministic and separated
   :id: STV_TE_D95EABFECD32D345
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: cyclic shared geometry with isolated nodes remains deterministic and separated
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_D22785EE6859`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/layout/tests/layout.test.js :: STV_SWR_056: cyclic shared geometry with isolated nodes remains deterministic and separated``.

.. test_execution:: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: parent and project center over five visible children
   :id: STV_TE_5F793CB29D9FD1EA
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: parent and project center over five visible children
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_08AC936D55F9`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/layout/tests/layout.test.js :: STV_SWR_056: parent and project center over five visible children``.

.. test_execution:: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap
   :id: STV_TE_053CFF28DE8DA59B
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/layout/tests/layout.test.js :: STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_880A2E13BCE9`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/layout/tests/layout.test.js :: STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap``.

.. test_execution:: frontend/src/layout/tests/layout.test.js :: STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane
   :id: STV_TE_40219C3E9A991A6B
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/layout/tests/layout.test.js :: STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_0CAAF47BBD14`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/layout/tests/layout.test.js :: STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane``.

.. test_execution:: frontend/src/layout/tests/layout.test.js :: STV_SWR_053: clear facing ports and fan-in avoid outer detours
   :id: STV_TE_93C98F38340108D0
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/layout/tests/layout.test.js :: STV_SWR_053: clear facing ports and fan-in avoid outer detours
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_2BC87902D1FD`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/layout/tests/layout.test.js :: STV_SWR_053: clear facing ports and fan-in avoid outer detours``.

.. test_execution:: frontend/src/layout/tests/layout.test.js :: STV_SWR_053: blocked skipped-level edges retain safe detours
   :id: STV_TE_15036384B14F8D9D
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/layout/tests/layout.test.js :: STV_SWR_053: blocked skipped-level edges retain safe detours
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_97667EB28A11`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/layout/tests/layout.test.js :: STV_SWR_053: blocked skipped-level edges retain safe detours``.

.. test_execution:: frontend/src/render/tests/groups.test.js :: STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship
   :id: STV_TE_66DFBB4B6CD7B08E
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/render/tests/groups.test.js :: STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_B2EF591B7F1E`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/render/tests/groups.test.js :: STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship``.

.. test_execution:: frontend/src/render/tests/groups.test.js :: STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions
   :id: STV_TE_BE7CCBCF64651401
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/render/tests/groups.test.js :: STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_1BFD0971844A`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/render/tests/groups.test.js :: STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions``.

.. test_execution:: frontend/src/render/tests/seeds.test.js :: STV_SWR_057: local suggestions match IDs and titles and bound results
   :id: STV_TE_69D755969013BB9F
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/render/tests/seeds.test.js :: STV_SWR_057: local suggestions match IDs and titles and bound results
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_EB472A6879CF`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/render/tests/seeds.test.js :: STV_SWR_057: local suggestions match IDs and titles and bound results``.

.. test_execution:: frontend/src/state/tests/state.test.js :: STV_SWR_003 STV_SWR_007 STV_SWR_020 STV_SWR_024 STV_SWR_025: rooted diamond and isolated cycle
   :id: STV_TE_807FE5FC51606B02
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/state/tests/state.test.js :: STV_SWR_003 STV_SWR_007 STV_SWR_020 STV_SWR_024 STV_SWR_025: rooted diamond and isolated cycle
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_4E68C09504E8`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/state/tests/state.test.js :: STV_SWR_003 STV_SWR_007 STV_SWR_020 STV_SWR_024 STV_SWR_025: rooted diamond and isolated cycle``.

.. test_execution:: frontend/src/state/tests/state.test.js :: STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity
   :id: STV_TE_B199E3E92412F17A
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/state/tests/state.test.js :: STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_6FE4CFC63C95`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/state/tests/state.test.js :: STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity``.

.. test_execution:: frontend/src/state/tests/state.test.js :: STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff
   :id: STV_TE_99108B0AAB32B836
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/state/tests/state.test.js :: STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_07D369AD0A2F`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/state/tests/state.test.js :: STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff``.

.. test_execution:: frontend/src/state/tests/state.test.js :: STV_SWR_024: self-loop terminates and collapse restores the only seed
   :id: STV_TE_813CCAABA945A63F
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/state/tests/state.test.js :: STV_SWR_024: self-loop terminates and collapse restores the only seed
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_156E45252AF4`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/state/tests/state.test.js :: STV_SWR_024: self-loop terminates and collapse restores the only seed``.

.. test_execution:: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: project pages preserve independent expansion and collapsed root
   :id: STV_TE_E5C4BDFF76CA4A30
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: project pages preserve independent expansion and collapsed root
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_35E510D6991A`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: project pages preserve independent expansion and collapsed root``.

.. test_execution:: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges
   :id: STV_TE_7C87AC31B6F3DFD0
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_AEF53EABA753`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges``.

.. test_execution:: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views
   :id: STV_TE_3CDAC35C33F90156
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_0C2F9B7BE8A7`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/state/tests/state.test.js :: STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views``.

.. test_execution:: frontend/src/state/tests/state.test.js :: STV_SWR_057: runtime reseeding is atomic and clears exploration
   :id: STV_TE_F0CDBA310548A24A
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/node-regression.log :: frontend/src/state/tests/state.test.js :: STV_SWR_057: runtime reseeding is atomic and clears exploration
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:34:54.482527+00:00

   **Case:** :need:`STV_TC_1E00212E164D`.

   **Inputs:** Broad JavaScript run; frontend source inputs unchanged since the broad-run hash snapshot.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`node-regression.log <node-regression.log>`, ``frontend/src/state/tests/state.test.js :: STV_SWR_057: runtime reseeding is atomic and clears exploration``.

.. test_execution:: docs/test-scripts/test_package.py::test_clean_wheel_host
   :id: STV_TE_7BEB3B1B6625A5DC
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/package-retest.xml :: docs/test-scripts/test_package.py::test_clean_wheel_host
   :priority: unassigned
   :verification_state: not_assessed
   :result: failed
   :executed_at: 2026-10-24T12:36:04.221647+00:00

   **Case:** :need:`STV_TC_F988267D01C9`.

   **Inputs:** Corrected test expression against first development artifact; missing generated inventory found.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`package-retest.xml <package-retest.xml>`, ``docs/test-scripts/test_package.py::test_clean_wheel_host``.

.. test_execution:: docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices
   :id: STV_TE_7F0E0FAA905ACCA8
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/legal-guard.xml :: docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:36:51.922277+00:00

   **Case:** :need:`STV_TC_LEGAL_GUARD`.

   **Inputs:** Negative build-input checks against the actual frontend build.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`legal-guard.xml <legal-guard.xml>`, ``docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices``.

.. test_execution:: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_failed_finalization_retains_pending_page_and_previous_assets
   :id: STV_TE_35ACFC65C5B99B80
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/affected-retest.xml :: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_failed_finalization_retains_pending_page_and_previous_assets
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:38:25.263283+00:00

   **Case:** :need:`STV_TC_136FE8B1A097`.

   **Inputs:** Development artifact 2; corrected lifecycle copy, component/installed/path/guard regressions.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`affected-retest.xml <affected-retest.xml>`, ``src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_failed_finalization_retains_pending_page_and_previous_assets``.

.. test_execution:: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_prior_fatal_exception_is_not_replaced_by_bundle_generation
   :id: STV_TE_05C8C8194E3C5F0D
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/affected-retest.xml :: src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_prior_fatal_exception_is_not_replaced_by_bundle_generation
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:38:25.263283+00:00

   **Case:** :need:`STV_TC_B5D550F17384`.

   **Inputs:** Development artifact 2; corrected lifecycle copy, component/installed/path/guard regressions.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`affected-retest.xml <affected-retest.xml>`, ``src/sphinx_traceability_view/directive/tests/test_lifecycle.py::test_prior_fatal_exception_is_not_replaced_by_bundle_generation``.

.. test_execution:: docs/test-scripts/test_package.py::test_clean_wheel_host
   :id: STV_TE_01F92BEF833F1EDE
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/affected-retest.xml :: docs/test-scripts/test_package.py::test_clean_wheel_host
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:38:25.263283+00:00

   **Case:** :need:`STV_TC_F988267D01C9`.

   **Inputs:** Development artifact 2; corrected lifecycle copy, component/installed/path/guard regressions.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`affected-retest.xml <affected-retest.xml>`, ``docs/test-scripts/test_package.py::test_clean_wheel_host``.

.. test_execution:: docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry
   :id: STV_TE_ADB1B05CE41E118B
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/affected-retest.xml :: docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:38:25.263283+00:00

   **Case:** :need:`STV_TC_WINDOWS_PATH`.

   **Inputs:** Development artifact 2; corrected lifecycle copy, component/installed/path/guard regressions.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`affected-retest.xml <affected-retest.xml>`, ``docs/test-scripts/test_windows_paths.py::test_nested_windows_detail_loading_and_retry``.

.. test_execution:: docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices
   :id: STV_TE_FA10CBBD5A653BBA
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/affected-retest.xml :: docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:38:25.263283+00:00

   **Case:** :need:`STV_TC_LEGAL_GUARD`.

   **Inputs:** Development artifact 2; corrected lifecycle copy, component/installed/path/guard regressions.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`affected-retest.xml <affected-retest.xml>`, ``docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices``.

.. test_execution:: docs/test-scripts/test_package.py::test_clean_wheel_host
   :id: STV_TE_E9C945EDF4A0769F
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/package-final.xml :: docs/test-scripts/test_package.py::test_clean_wheel_host
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:43:31.831802+00:00

   **Case:** :need:`STV_TC_F988267D01C9`.

   **Inputs:** Development artifact 3; final normalized notices and installed-package/legal-guard checks.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`package-final.xml <package-final.xml>`, ``docs/test-scripts/test_package.py::test_clean_wheel_host``.

.. test_execution:: docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices
   :id: STV_TE_B143FA7927D35E75
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/package-final.xml :: docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:43:31.831802+00:00

   **Case:** :need:`STV_TC_LEGAL_GUARD`.

   **Inputs:** Development artifact 3; final normalized notices and installed-package/legal-guard checks.
   Source revision before maintenance: ``17cafd9``. Exact retained commands,
   source snapshots, wheel/source checksums and environment are in :doc:`index`.
   The reports preserve failures rather than treating the final pass as a new release.

   **Report:** :download:`package-final.xml <package-final.xml>`, ``docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices``.

.. test_execution:: docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices
   :id: STV_TE_506DA5166F4226E8
   :status: recorded
   :basis: observed
   :evidence: docs/test-execution/maintenance-2026-10-24/legal-guard-final.xml :: docs/test-scripts/test_legal_guard.py::test_build_rejects_unaudited_elk_and_missing_notices
   :priority: unassigned
   :verification_state: not_assessed
   :result: passed
   :executed_at: 2026-10-24T12:47:51.787779+00:00

   **Case:** :need:`STV_TC_LEGAL_GUARD`.

   **Inputs:** The scoped acceptance review removed an irrelevant SWR_046
   link from the negative build guard. No product behavior changed. This
   focused rerun confirms the final test/marker revision; source identity is
   retained in source-hashes.json. Report completion time is used consistently.

   **Report:** :download:`legal-guard-final.xml <legal-guard-final.xml>`.
