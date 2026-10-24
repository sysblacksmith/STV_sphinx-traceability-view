1.0.0-candidate-2 execution
===================================

Execution: 2026-10-24T20:26:45.338117+00:00 to 2026-10-24T20:46:36.829986+00:00 (UTC).
Outcome: **required executable suites passed**.

Input Git revision: ``9d3b793928eef76c0043185d0ee2aff3968b5fb5``; dirty source/test identity:
``7a32f3997d3567898119a56fef6fc743c1f00f5540e1757b4b036d3107337235``. Full file hashes and dirty-worktree state are retained below.
Wheel SHA-256: ``1905bebe38f24df37531004915f7b252489039df7e8e7ead5306880c8643a839``. Python 3.13.17; Windows-11-10.0.26300-SP0; Node v24.21.0.
Firefox and geckodriver versions are retained in the browser metrics and candidate metadata.
This records execution, not owner release approval, deployment, licensing or agreed performance budgets.

Test totals: 158 passed; 0 failed; 0 errors; 0 skipped.

Suite results
-------------

.. list-table:: Commands and outcomes
   :header-rows: 1

   * - Suite
     - Exit
     - Retained log
   * - browser-assets
     - 0
     - :download:`browser-assets.log <browser-assets.log>`
   * - python-package
     - 0
     - :download:`python-package.log <python-package.log>`
   * - coverage
     - 0
     - :download:`coverage.log <coverage.log>`
   * - diagram-links-source
     - 0
     - :download:`diagram-links-source.log <diagram-links-source.log>`
   * - documentation
     - 0
     - :download:`documentation.log <documentation.log>`
   * - capacity-build
     - 0
     - :download:`capacity-build.log <capacity-build.log>`
   * - pytest
     - 0
     - :download:`pytest.log <pytest.log>`
   * - node-tests
     - 0
     - :download:`node-tests.log <node-tests.log>`
   * - traceability
     - 0
     - :download:`traceability.log <traceability.log>`
   * - diagram-links-published
     - 0
     - :download:`diagram-links-published.log <diagram-links-published.log>`

Requirement execution results
-----------------------------

.. list-table:: Per-case result and mapped criteria
   :header-rows: 1
   :widths: 55 10 35

   * - Executable case
     - Outcome
     - Requirement criteria exercised
   * - ``src.sphinx_traceability_view.bundle.tests.test_bundle::test_classic_registration_treats_prototype_keys_and_script_text_as_data``
     - passed
     - :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_027`
   * - ``src.sphinx_traceability_view.bundle.tests.test_bundle::test_detail_assets_preserve_full_identity_with_compact_deduplicated_paths``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`
   * - ``src.sphinx_traceability_view.detail_build.tests.test_details::test_static_details_and_remote_fallback``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_048`, :need:`STV_SWR_049`
   * - ``src.sphinx_traceability_view.detail_build.tests.test_details::test_portable_paths_preserve_queries_and_fragments``
     - passed
     - :need:`STV_SWR_018`
   * - ``src.sphinx_traceability_view.detail_build.tests.test_details::test_srcset_data_images_and_css_resources``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`
   * - ``src.sphinx_traceability_view.detail_build.tests.test_details::test_active_embed_urls_are_not_retained_as_navigation``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_049`
   * - ``src.sphinx_traceability_view.detail_build.tests.test_details::test_reserved_transport_attributes_are_never_copied_from_authored_html``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`
   * - ``src.sphinx_traceability_view.directive.tests.test_lifecycle::test_failed_finalization_retains_pending_page_and_previous_assets``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_027`
   * - ``src.sphinx_traceability_view.directive.tests.test_lifecycle::test_prior_fatal_exception_is_not_replaced_by_bundle_generation``
     - passed
     - :need:`STV_SWR_027`
   * - ``src.sphinx_traceability_view.graph.tests.test_graph::test_hidden_parts_external_and_missing_targets``
     - passed
     - :need:`STV_SWR_013`, :need:`STV_SWR_027`, :need:`STV_SWR_047`, :need:`STV_SWR_048`
   * - ``src.sphinx_traceability_view.graph.tests.test_graph::test_external_original_url_rejects_executable_or_nonportable_navigation[javascript:bad()]``
     - passed
     - :need:`STV_SWR_047`
   * - ``src.sphinx_traceability_view.graph.tests.test_graph::test_external_original_url_rejects_executable_or_nonportable_navigation[data:text/html,bad]``
     - passed
     - :need:`STV_SWR_047`
   * - ``src.sphinx_traceability_view.graph.tests.test_graph::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]``
     - passed
     - :need:`STV_SWR_047`
   * - ``src.sphinx_traceability_view.graph.tests.test_graph::test_classification_is_complete_graph_based_portable_and_deterministic``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.graph.tests.test_graph::test_unclassified_records_without_fallback_fail_with_need_identity[records0]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.graph.tests.test_graph::test_unclassified_records_without_fallback_fail_with_need_identity[records1]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.graph.tests.test_graph::test_outgoing_owner_mapping_and_malformed_tags_use_defined_policy``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.graph.tests.test_graph::test_large_classified_graph_resolves_every_execution_from_its_case``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_host_normalization``
     - passed
     - :need:`STV_SWR_014`, :need:`STV_SWR_030`, :need:`STV_SWR_032`, :need:`STV_SWR_036`, :need:`STV_SWR_045`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_invalid_model[change0-levels]``
     - passed
     - :need:`STV_SWR_036`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_invalid_model[change1-types.goal]``
     - passed
     - :need:`STV_SWR_036`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_invalid_model[change2-types]``
     - passed
     - :need:`STV_SWR_036`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_invalid_model[change3-accepted_statuses]``
     - passed
     - :need:`STV_SWR_036`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_invalid_directional_labels[]``
     - passed
     - :need:`STV_SWR_036`, :need:`STV_SWR_045`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_invalid_directional_labels[ ]``
     - passed
     - :need:`STV_SWR_036`, :need:`STV_SWR_045`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_invalid_directional_labels[None]``
     - passed
     - :need:`STV_SWR_036`, :need:`STV_SWR_045`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_invalid_directional_labels[1]``
     - passed
     - :need:`STV_SWR_036`, :need:`STV_SWR_045`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_is_portable_and_does_not_mutate_input``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement0-levels_by_tag]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement1-levels_by_tag]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement2-levels_by_tag]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement3-types.case]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement4-types.case]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement5-types.case]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement6-fallback_level]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement7-level_from.relation]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement8-level_from]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement9-level_from]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement10-level_from.levels]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_classified_model_rejects_invalid_selectors[placement11-fixed level]``
     - passed
     - :need:`STV_SWR_061`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_details_limit_defaults_and_exact_bounds``
     - passed
     - :need:`STV_SWR_065`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_details_limit_rejects_invalid_author_values[0]``
     - passed
     - :need:`STV_SWR_065`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_details_limit_rejects_invalid_author_values[-1]``
     - passed
     - :need:`STV_SWR_065`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_details_limit_rejects_invalid_author_values[True]``
     - passed
     - :need:`STV_SWR_065`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_details_limit_rejects_invalid_author_values[False]``
     - passed
     - :need:`STV_SWR_065`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_details_limit_rejects_invalid_author_values[3]``
     - passed
     - :need:`STV_SWR_065`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_details_limit_rejects_invalid_author_values[1.0]``
     - passed
     - :need:`STV_SWR_065`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_details_limit_rejects_invalid_author_values[None]``
     - passed
     - :need:`STV_SWR_065`
   * - ``src.sphinx_traceability_view.model.tests.test_model::test_details_limit_rejects_invalid_author_values[9007199254740992]``
     - passed
     - :need:`STV_SWR_065`
   * - ``docs.test-scripts.test_browser::test_usability_smoke[file]``
     - passed
     - :need:`STV_SWR_050`, :need:`STV_SWR_054`, :need:`STV_SYS_006`
   * - ``docs.test-scripts.test_browser::test_usability_smoke[http]``
     - passed
     - :need:`STV_SWR_050`, :need:`STV_SWR_054`, :need:`STV_SYS_006`
   * - ``docs.test-scripts.test_browser::test_offline_exploration[file]``
     - passed
     - :need:`STV_SWR_004`, :need:`STV_SWR_008`, :need:`STV_SWR_015`, :need:`STV_SWR_016`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_029`, :need:`STV_SWR_031`, :need:`STV_SWR_033`, :need:`STV_SWR_034`, :need:`STV_SWR_035`, :need:`STV_SWR_038`, :need:`STV_SWR_039`, :need:`STV_SWR_040`, :need:`STV_SWR_050`, :need:`STV_SYS_003`, :need:`STV_SYS_007`
   * - ``docs.test-scripts.test_browser::test_offline_exploration[http]``
     - passed
     - :need:`STV_SWR_004`, :need:`STV_SWR_008`, :need:`STV_SWR_015`, :need:`STV_SWR_016`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_029`, :need:`STV_SWR_031`, :need:`STV_SWR_033`, :need:`STV_SWR_034`, :need:`STV_SWR_035`, :need:`STV_SWR_038`, :need:`STV_SWR_039`, :need:`STV_SWR_040`, :need:`STV_SWR_050`, :need:`STV_SYS_003`, :need:`STV_SYS_007`
   * - ``docs.test-scripts.test_browser::test_project_paging[file]``
     - passed
     - :need:`STV_SWR_051`, :need:`STV_SWR_052`
   * - ``docs.test-scripts.test_browser::test_project_paging[http]``
     - passed
     - :need:`STV_SWR_051`, :need:`STV_SWR_052`
   * - ``docs.test-scripts.test_browser::test_interactive_seed_smoke[file]``
     - passed
     - :need:`STV_SWR_038`, :need:`STV_SWR_056`, :need:`STV_SWR_057`
   * - ``docs.test-scripts.test_browser::test_interactive_seed_smoke[http]``
     - passed
     - :need:`STV_SWR_038`, :need:`STV_SWR_056`, :need:`STV_SWR_057`
   * - ``docs.test-scripts.test_browser::test_async_layout_failure_and_stale_completion[file]``
     - passed
     - :need:`STV_SWR_044`, :need:`STV_SWR_052`, :need:`STV_SWR_058`
   * - ``docs.test-scripts.test_browser::test_async_layout_failure_and_stale_completion[http]``
     - passed
     - :need:`STV_SWR_044`, :need:`STV_SWR_052`, :need:`STV_SWR_058`
   * - ``docs.test-scripts.test_browser::test_alternate_model_geometry_details_and_external[file]``
     - passed
     - :need:`STV_SWR_008`, :need:`STV_SWR_012`, :need:`STV_SWR_015`, :need:`STV_SWR_029`, :need:`STV_SWR_031`, :need:`STV_SWR_033`, :need:`STV_SWR_037`, :need:`STV_SWR_041`, :need:`STV_SWR_047`, :need:`STV_SWR_048`, :need:`STV_SWR_049`, :need:`STV_SWR_050`, :need:`STV_SYS_004`, :need:`STV_SYS_005`, :need:`STV_SYS_006`, :need:`STV_SYS_010`
   * - ``docs.test-scripts.test_browser::test_alternate_model_geometry_details_and_external[http]``
     - passed
     - :need:`STV_SWR_008`, :need:`STV_SWR_012`, :need:`STV_SWR_015`, :need:`STV_SWR_029`, :need:`STV_SWR_031`, :need:`STV_SWR_033`, :need:`STV_SWR_037`, :need:`STV_SWR_041`, :need:`STV_SWR_047`, :need:`STV_SWR_048`, :need:`STV_SWR_049`, :need:`STV_SWR_050`, :need:`STV_SYS_004`, :need:`STV_SYS_005`, :need:`STV_SYS_006`, :need:`STV_SYS_010`
   * - ``docs.test-scripts.test_browser::test_missing_placeholder_and_detail_error[file]``
     - passed
     - :need:`STV_SWR_027`, :need:`STV_SWR_028`, :need:`STV_SWR_029`, :need:`STV_SYS_004`
   * - ``docs.test-scripts.test_browser::test_missing_placeholder_and_detail_error[http]``
     - passed
     - :need:`STV_SWR_027`, :need:`STV_SWR_028`, :need:`STV_SWR_029`, :need:`STV_SYS_004`
   * - ``docs.test-scripts.test_browser::test_documentation_visuals``
     - passed
     - Publication/build infrastructure
   * - ``docs.test-scripts.test_browser::test_control_order_smoke[file]``
     - passed
     - :need:`STV_SWR_055`
   * - ``docs.test-scripts.test_browser::test_control_order_smoke[http]``
     - passed
     - :need:`STV_SWR_055`
   * - ``docs.test-scripts.test_build::test_cross_page_bundle``
     - passed
     - :need:`STV_SWR_001`, :need:`STV_SWR_002`, :need:`STV_SWR_013`, :need:`STV_SWR_026`, :need:`STV_SYS_001`
   * - ``docs.test-scripts.test_build::test_invalid_seed_source_location[UNKNOWN]``
     - passed
     - :need:`STV_SWR_026`, :need:`STV_SWR_048`, :need:`STV_SYS_001`
   * - ``docs.test-scripts.test_build::test_invalid_seed_source_location[ROOT_A UNKNOWN]``
     - passed
     - :need:`STV_SWR_026`, :need:`STV_SWR_048`, :need:`STV_SYS_001`
   * - ``docs.test-scripts.test_build::test_invalid_seed_source_location[HIDDEN_A]``
     - passed
     - :need:`STV_SWR_026`, :need:`STV_SWR_048`, :need:`STV_SYS_001`
   * - ``docs.test-scripts.test_build::test_host_owns_broken_trace_failure``
     - passed
     - :need:`STV_SWR_027`, :need:`STV_SWR_028`
   * - ``docs.test-scripts.test_build::test_incremental_body_change_hidden_and_deleted_objects``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_018`, :need:`STV_SWR_048`
   * - ``docs.test-scripts.test_build::test_seed_capacity_at_directive[200-True]``
     - passed
     - :need:`STV_SWR_001`, :need:`STV_SWR_026`, :need:`STV_SWR_043`
   * - ``docs.test-scripts.test_build::test_seed_capacity_at_directive[201-False]``
     - passed
     - :need:`STV_SWR_001`, :need:`STV_SWR_026`, :need:`STV_SWR_043`
   * - ``docs.test-scripts.test_build::test_alternate_host_schema_external_metadata_and_parts``
     - passed
     - :need:`STV_SWR_014`, :need:`STV_SWR_036`, :need:`STV_SWR_045`, :need:`STV_SWR_047`, :need:`STV_SWR_048`, :need:`STV_SYS_002`
   * - ``docs.test-scripts.test_build::test_invalid_mapping_has_entry_path_and_location``
     - passed
     - :need:`STV_SWR_036`
   * - ``docs.test-scripts.test_build::test_unsupported_builder_fails_clearly``
     - passed
     - :need:`STV_SWR_001`
   * - ``docs.test-scripts.test_build::test_host_default_directional_labels_are_used``
     - passed
     - :need:`STV_SWR_045`
   * - ``docs.test-scripts.test_capacity::test_large_project_at_visible_capacity[file]``
     - passed
     - :need:`STV_SWR_043`, :need:`STV_SWR_044`, :need:`STV_SYS_008`
   * - ``docs.test-scripts.test_capacity::test_large_project_at_visible_capacity[http]``
     - passed
     - :need:`STV_SWR_043`, :need:`STV_SWR_044`, :need:`STV_SYS_008`
   * - ``docs.test-scripts.test_ci_security::test_workflow_policy_accepts_reviewed_files_and_rejects_privilege_drift``
     - passed
     - :need:`STV_SWR_042`, :need:`STV_SYS_009`
   * - ``docs.test-scripts.test_ci_security::test_candidate_checksums_detect_changed_artifact_bytes``
     - passed
     - :need:`STV_SWR_042`, :need:`STV_SYS_009`
   * - ``docs.test-scripts.test_classified_rows::test_published_classified_rows_and_fallback_navigation[file]``
     - passed
     - :need:`STV_SWR_012`, :need:`STV_SWR_037`, :need:`STV_SWR_055`, :need:`STV_SWR_058`, :need:`STV_SWR_061`, :need:`STV_SYS_002`, :need:`STV_SYS_005`
   * - ``docs.test-scripts.test_classified_rows::test_published_classified_rows_and_fallback_navigation[http]``
     - passed
     - :need:`STV_SWR_012`, :need:`STV_SWR_037`, :need:`STV_SWR_055`, :need:`STV_SWR_058`, :need:`STV_SWR_061`, :need:`STV_SYS_002`, :need:`STV_SYS_005`
   * - ``docs.test-scripts.test_detail_transport::test_authored_transport_markers_stay_inert[file]``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_049`
   * - ``docs.test-scripts.test_detail_transport::test_authored_transport_markers_stay_inert[http]``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_049`
   * - ``docs.test-scripts.test_legal_guard::test_build_rejects_unaudited_elk_and_missing_notices``
     - passed
     - :need:`STV_SWR_042`, :need:`STV_SYS_009`
   * - ``docs.test-scripts.test_package::test_clean_wheel_host``
     - passed
     - :need:`STV_SWR_042`, :need:`STV_SWR_046`, :need:`STV_SYS_009`
   * - ``docs.test-scripts.test_persistent_details::test_persistent_limit_is_published_by_real_host[None]``
     - passed
     - :need:`STV_SWR_065`
   * - ``docs.test-scripts.test_persistent_details::test_persistent_limit_is_published_by_real_host[1]``
     - passed
     - :need:`STV_SWR_065`
   * - ``docs.test-scripts.test_persistent_details::test_persistent_limit_is_published_by_real_host[3]``
     - passed
     - :need:`STV_SWR_065`
   * - ``docs.test-scripts.test_persistent_details::test_persistent_stack_fifo_scope_navigation_and_responsive_layout[None-file]``
     - passed
     - :need:`STV_SWR_050`, :need:`STV_SWR_063`, :need:`STV_SWR_064`, :need:`STV_SWR_065`
   * - ``docs.test-scripts.test_persistent_details::test_persistent_stack_fifo_scope_navigation_and_responsive_layout[None-http]``
     - passed
     - :need:`STV_SWR_050`, :need:`STV_SWR_063`, :need:`STV_SWR_064`, :need:`STV_SWR_065`
   * - ``docs.test-scripts.test_persistent_details::test_persistent_stack_fifo_scope_navigation_and_responsive_layout[3-file]``
     - passed
     - :need:`STV_SWR_050`, :need:`STV_SWR_063`, :need:`STV_SWR_064`, :need:`STV_SWR_065`
   * - ``docs.test-scripts.test_persistent_details::test_persistent_stack_fifo_scope_navigation_and_responsive_layout[3-http]``
     - passed
     - :need:`STV_SWR_050`, :need:`STV_SWR_063`, :need:`STV_SWR_064`, :need:`STV_SWR_065`
   * - ``docs.test-scripts.test_persistent_details::test_persistent_completion_identity_eviction_and_retry[file]``
     - passed
     - :need:`STV_SWR_063`, :need:`STV_SWR_064`
   * - ``docs.test-scripts.test_persistent_details::test_persistent_completion_identity_eviction_and_retry[http]``
     - passed
     - :need:`STV_SWR_063`, :need:`STV_SWR_064`
   * - ``docs.test-scripts.test_persistent_details::test_detail_metadata_controls_width_and_artifact_navigation[file]``
     - passed
     - :need:`STV_SWR_016`, :need:`STV_SWR_018`, :need:`STV_SWR_064`
   * - ``docs.test-scripts.test_persistent_details::test_detail_metadata_controls_width_and_artifact_navigation[http]``
     - passed
     - :need:`STV_SWR_016`, :need:`STV_SWR_018`, :need:`STV_SWR_064`
   * - ``docs.test-scripts.test_position_stability::test_group_navigation_keeps_existing_nodes_still[file]``
     - passed
     - :need:`STV_SWR_058`
   * - ``docs.test-scripts.test_position_stability::test_group_navigation_keeps_existing_nodes_still[http]``
     - passed
     - :need:`STV_SWR_058`
   * - ``docs.test-scripts.test_position_stability::test_arrow_viewport_covers_negative_routes[down-file]``
     - passed
     - :need:`STV_SWR_059`
   * - ``docs.test-scripts.test_position_stability::test_arrow_viewport_covers_negative_routes[down-http]``
     - passed
     - :need:`STV_SWR_059`
   * - ``docs.test-scripts.test_position_stability::test_arrow_viewport_covers_negative_routes[up-file]``
     - passed
     - :need:`STV_SWR_059`
   * - ``docs.test-scripts.test_position_stability::test_arrow_viewport_covers_negative_routes[up-http]``
     - passed
     - :need:`STV_SWR_059`
   * - ``docs.test-scripts.test_position_stability::test_initial_numeric_seed_order[file]``
     - passed
     - :need:`STV_SWR_060`
   * - ``docs.test-scripts.test_position_stability::test_initial_numeric_seed_order[http]``
     - passed
     - :need:`STV_SWR_060`
   * - ``docs.test-scripts.test_position_stability::test_project_root_preserves_anchor[file]``
     - passed
     - :need:`STV_SWR_058`
   * - ``docs.test-scripts.test_position_stability::test_project_root_preserves_anchor[http]``
     - passed
     - :need:`STV_SWR_058`
   * - ``docs.test-scripts.test_publication::test_clean_publication_removes_obsolete_assets``
     - passed
     - :need:`STV_SWR_042`, :need:`STV_SYS_009`
   * - ``docs.test-scripts.test_publication::test_failed_build_preserves_published_tree``
     - passed
     - :need:`STV_SWR_042`, :need:`STV_SYS_009`
   * - ``docs.test-scripts.test_publication::test_failed_promotion_restores_previous_tree``
     - passed
     - :need:`STV_SWR_042`, :need:`STV_SYS_009`
   * - ``docs.test-scripts.test_release_seeds::test_seed_selection_release[file]``
     - passed
     - :need:`STV_SWR_003`, :need:`STV_SWR_038`, :need:`STV_SWR_048`, :need:`STV_SWR_051`, :need:`STV_SWR_052`, :need:`STV_SWR_056`, :need:`STV_SWR_057`
   * - ``docs.test-scripts.test_release_seeds::test_seed_selection_release[http]``
     - passed
     - :need:`STV_SWR_003`, :need:`STV_SWR_038`, :need:`STV_SWR_048`, :need:`STV_SWR_051`, :need:`STV_SWR_052`, :need:`STV_SWR_056`, :need:`STV_SWR_057`
   * - ``docs.test-scripts.test_release_seeds::test_empty_seed_catalog[file]``
     - passed
     - :need:`STV_SWR_051`, :need:`STV_SWR_052`, :need:`STV_SWR_057`
   * - ``docs.test-scripts.test_release_seeds::test_empty_seed_catalog[http]``
     - passed
     - :need:`STV_SWR_051`, :need:`STV_SWR_052`, :need:`STV_SWR_057`
   * - ``docs.test-scripts.test_release_seeds::test_seed_layout_replacement_failure_and_staleness[file]``
     - passed
     - :need:`STV_SWR_044`, :need:`STV_SWR_057`
   * - ``docs.test-scripts.test_release_seeds::test_seed_layout_replacement_failure_and_staleness[http]``
     - passed
     - :need:`STV_SWR_044`, :need:`STV_SWR_057`
   * - ``docs.test-scripts.test_sdist::test_sdist_excludes_local_evidence_and_rebuilds_wheel``
     - passed
     - :need:`STV_SWR_042`, :need:`STV_SWR_046`, :need:`STV_SYS_009`
   * - ``docs.test-scripts.test_viewport_boundary::test_viewport_boundary_tracks_clipping_and_controls[file]``
     - passed
     - :need:`STV_SWR_062`
   * - ``docs.test-scripts.test_viewport_boundary::test_viewport_boundary_tracks_clipping_and_controls[http]``
     - passed
     - :need:`STV_SWR_062`
   * - ``docs.test-scripts.test_windows_paths::test_nested_windows_detail_loading_and_retry``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SYS_003`, :need:`STV_SYS_006`
   * - ``test::STV_SWR_063: persistent collection reuses identity without refreshing FIFO age``
     - passed
     - :need:`STV_SWR_063`
   * - ``test::STV_SWR_063: default, one-slot and independent detail collections enforce their own capacity``
     - passed
     - :need:`STV_SWR_063`
   * - ``test::STV_SWR_015 STV_SWR_017: concurrent detail requests share one load and retain build identity``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`
   * - ``test::STV_SWR_015 STV_SWR_017: failed local detail loading can retry without a stale rejection``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`
   * - ``test::STV_SWR_017 STV_SWR_018: restored detail paths stay inside the output root``
     - passed
     - :need:`STV_SWR_017`, :need:`STV_SWR_018`
   * - ``test::STV_SWR_015 STV_SWR_017: restored CSS rejects noncanonical and remote resource paths``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`
   * - ``test::STV_SWR_012 STV_SWR_037 STV_SWR_058: classified rows align and stay stable during navigation``
     - passed
     - :need:`STV_SWR_012`, :need:`STV_SWR_037`, :need:`STV_SWR_058`
   * - ``test::STV_SWR_055: controls use resolved case and execution rows``
     - passed
     - :need:`STV_SWR_055`
   * - ``test::STV_SWR_012 STV_SWR_037: 200 classified nodes keep row alignment and safe cyclic routes``
     - passed
     - :need:`STV_SWR_012`, :need:`STV_SWR_037`
   * - ``test::STV_SWR_056: competing parents do not displace a separate centered parent``
     - passed
     - :need:`STV_SWR_056`
   * - ``test::STV_SWR_056: cyclic shared geometry with isolated nodes remains deterministic and separated``
     - passed
     - :need:`STV_SWR_056`
   * - ``test::STV_SWR_056: parent and project center over five visible children``
     - passed
     - :need:`STV_SWR_056`
   * - ``test::STV_SWR_056: shared children keep unique nodes and conflicting parents do not overlap``
     - passed
     - :need:`STV_SWR_056`
   * - ``test::STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037 STV_SWR_053: semantic bands and shared test lane``
     - passed
     - :need:`STV_SWR_009`, :need:`STV_SWR_010`, :need:`STV_SWR_011`, :need:`STV_SWR_012`, :need:`STV_SWR_037`, :need:`STV_SWR_053`
   * - ``test::STV_SWR_053: clear facing ports and fan-in avoid outer detours``
     - passed
     - :need:`STV_SWR_053`
   * - ``test::STV_SWR_053: blocked skipped-level edges retain safe detours``
     - passed
     - :need:`STV_SWR_053`
   * - ``test::STV_SWR_058: expand and collapse preserve existing primary slots``
     - passed
     - :need:`STV_SWR_058`
   * - ``test::STV_SWR_058: existing test lane is stable while new primary nodes fit beside it``
     - passed
     - :need:`STV_SWR_058`
   * - ``test::STV_SWR_058: a growing earlier band makes room above the clicked lower band``
     - passed
     - :need:`STV_SWR_058`
   * - ``test::STV_SWR_060: initial seed and project rows use natural numeric ID order``
     - passed
     - :need:`STV_SWR_060`
   * - ``test::STV_SWR_058: reranked shared tests remain unique and honor either anchor role``
     - passed
     - :need:`STV_SWR_058`
   * - ``test::STV_SWR_058: project root stays anchored through collapse and reopening``
     - passed
     - :need:`STV_SWR_058`
   * - ``test::STV_SWR_058: 200-node incremental geometry remains finite and stable``
     - passed
     - :need:`STV_SWR_058`
   * - ``test::STV_SWR_059: SVG bounds include negative routes, detours and node boxes``
     - passed
     - :need:`STV_SWR_059`
   * - ``test::STV_SWR_059: an empty edge scene still has a finite SVG viewport``
     - passed
     - :need:`STV_SWR_059`
   * - ``test::STV_SWR_055: upward controls precede neutral and downward controls regardless of authorship``
     - passed
     - :need:`STV_SWR_055`
   * - ``test::STV_SWR_055: replacement level mappings drive ordering without relation-name assumptions``
     - passed
     - :need:`STV_SWR_055`
   * - ``test::STV_SWR_057: local suggestions match IDs and titles and bound results``
     - passed
     - :need:`STV_SWR_057`
   * - ``test::STV_SWR_003 STV_SWR_007 STV_SWR_020 STV_SWR_024 STV_SWR_025: rooted diamond and isolated cycle``
     - passed
     - :need:`STV_SWR_003`, :need:`STV_SWR_007`, :need:`STV_SWR_020`, :need:`STV_SWR_024`, :need:`STV_SWR_025`
   * - ``test::STV_SWR_005 STV_SWR_043 STV_SWR_044: 199/200/201 atomic capacity``
     - passed
     - :need:`STV_SWR_005`, :need:`STV_SWR_043`, :need:`STV_SWR_044`
   * - ``test::STV_SWR_006 STV_SWR_013: reverse traversal has no depth cutoff``
     - passed
     - :need:`STV_SWR_006`, :need:`STV_SWR_013`
   * - ``test::STV_SWR_024: self-loop terminates and collapse restores the only seed``
     - passed
     - :need:`STV_SWR_024`
   * - ``test::STV_SWR_051 STV_SWR_052: project pages preserve independent expansion and collapsed root``
     - passed
     - :need:`STV_SWR_051`, :need:`STV_SWR_052`
   * - ``test::STV_SWR_051 STV_SWR_052: cross-page targets do not acquire synthetic root edges``
     - passed
     - :need:`STV_SWR_051`, :need:`STV_SWR_052`
   * - ``test::STV_SWR_051 STV_SWR_052 STV_SWR_043 STV_SWR_044: page boundaries, root capacity and independent views``
     - passed
     - :need:`STV_SWR_051`, :need:`STV_SWR_052`, :need:`STV_SWR_043`, :need:`STV_SWR_044`
   * - ``test::STV_SWR_057: runtime reseeding is atomic and clears exploration``
     - passed
     - :need:`STV_SWR_057`

Retained evidence
-----------------

* :download:`candidate.json <candidate.json>`
* :download:`source-hashes.json <source-hashes.json>`
* :download:`commands.json <commands.json>`
* :download:`environment.txt <environment.txt>`
* :download:`runtime-wheel-hashes.json <runtime-wheel-hashes.json>`
* :download:`test-map.json <test-map.json>`
* :download:`pytest.xml <pytest.xml>`
* :download:`node.xml <node.xml>`
* :download:`results.json <results.json>`
* :download:`capacity-build.json <capacity-build.json>`
* :download:`capacity-browser.json <capacity-browser.json>`
* :download:`capacity-host.log <capacity-host.log>`
* :download:`traceability.csv <traceability.csv>`
* :download:`Tested wheel <artifacts/sphinx_traceability_view-1.0.0-py3-none-any.whl>`

Browser screenshots
-------------------

* :download:`consumer/build.log <consumer/build.log>`
* :download:`consumer/environment.txt <consumer/environment.txt>`
* :download:`consumer/identity.txt <consumer/identity.txt>`
* :download:`architecture-software-page.png <screenshots/architecture-software-page.png>`
* :download:`architecture-system-page.png <screenshots/architecture-system-page.png>`
* :download:`file-example.png <screenshots/file-example.png>`
* :download:`http-example.png <screenshots/http-example.png>`
* :download:`project-demo.png <screenshots/project-demo.png>`
* :download:`software-architecture.png <screenshots/software-architecture.png>`
* :download:`state-diagram.png <screenshots/state-diagram.png>`
* :download:`state-page.png <screenshots/state-page.png>`
* :download:`system-architecture.png <screenshots/system-architecture.png>`

Canonical candidate results
-----------------------------

.. toctree::
   :maxdepth: 1

   cases

Release assessment
----------------------------

.. toctree::
   :maxdepth: 1

   qualification

Hosted release outcome
------------------------

.. toctree::
   :maxdepth: 1

   post-release
