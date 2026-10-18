0.1.0-candidate-1 execution
===========================

Execution: 2026-10-18T14:43:19.288240+00:00 to 2026-10-18T14:52:11.478463+00:00 (UTC).
Outcome: **candidate has unresolved verification failures**.

Input Git revision: ``30aaba98776ecbe648558d278a985691d81bccb4``; dirty source/test identity:
``4268dc1ffec99573e958fda2a1cf243bca51888b83d2a1906ae685eccd1f1ce4``. Full file hashes and dirty-worktree state are retained below.
Wheel SHA-256: ``03dc6ab7caa5d1c0c5cde0b3c3d354a881dc37380f5d03bfc14360e3360b8370``. Python 3.10.9; Windows-10-10.0.26300-SP0; Node v24.21.0.
Firefox and geckodriver versions are retained in the browser metrics and candidate metadata.
This records execution, not owner release approval, deployment, licensing or agreed performance budgets.

Test totals: 46 passed; 0 failed; 0 errors; 0 skipped.

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
   * - candidate-source-stability
     - 1
     - See results.json

Requirement execution results
-----------------------------

.. list-table:: Per-case result and mapped criteria
   :header-rows: 1
   :widths: 55 10 35

   * - Executable case
     - Outcome
     - Requirement criteria exercised
   * - ``tests.test_browser::test_offline_exploration[file]``
     - passed
     - :need:`STV_SWR_004`, :need:`STV_SWR_008`, :need:`STV_SWR_015`, :need:`STV_SWR_016`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_029`, :need:`STV_SWR_031`, :need:`STV_SWR_033`, :need:`STV_SWR_034`, :need:`STV_SWR_035`, :need:`STV_SWR_038`, :need:`STV_SWR_039`, :need:`STV_SWR_040`, :need:`STV_SWR_050`, :need:`STV_SYS_003`, :need:`STV_SYS_007`
   * - ``tests.test_browser::test_offline_exploration[http]``
     - passed
     - :need:`STV_SWR_004`, :need:`STV_SWR_008`, :need:`STV_SWR_015`, :need:`STV_SWR_016`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_029`, :need:`STV_SWR_031`, :need:`STV_SWR_033`, :need:`STV_SWR_034`, :need:`STV_SWR_035`, :need:`STV_SWR_038`, :need:`STV_SWR_039`, :need:`STV_SWR_040`, :need:`STV_SWR_050`, :need:`STV_SYS_003`, :need:`STV_SYS_007`
   * - ``tests.test_browser::test_project_paging[file]``
     - passed
     - :need:`STV_SWR_051`, :need:`STV_SWR_052`
   * - ``tests.test_browser::test_project_paging[http]``
     - passed
     - :need:`STV_SWR_051`, :need:`STV_SWR_052`
   * - ``tests.test_browser::test_async_layout_failure_and_stale_completion[file]``
     - passed
     - :need:`STV_SWR_044`, :need:`STV_SWR_052`
   * - ``tests.test_browser::test_async_layout_failure_and_stale_completion[http]``
     - passed
     - :need:`STV_SWR_044`, :need:`STV_SWR_052`
   * - ``tests.test_browser::test_alternate_model_geometry_details_and_external[file]``
     - passed
     - :need:`STV_SWR_008`, :need:`STV_SWR_012`, :need:`STV_SWR_015`, :need:`STV_SWR_029`, :need:`STV_SWR_031`, :need:`STV_SWR_033`, :need:`STV_SWR_037`, :need:`STV_SWR_041`, :need:`STV_SWR_047`, :need:`STV_SWR_048`, :need:`STV_SWR_049`, :need:`STV_SWR_050`, :need:`STV_SYS_004`, :need:`STV_SYS_005`, :need:`STV_SYS_006`, :need:`STV_SYS_010`
   * - ``tests.test_browser::test_alternate_model_geometry_details_and_external[http]``
     - passed
     - :need:`STV_SWR_008`, :need:`STV_SWR_012`, :need:`STV_SWR_015`, :need:`STV_SWR_029`, :need:`STV_SWR_031`, :need:`STV_SWR_033`, :need:`STV_SWR_037`, :need:`STV_SWR_041`, :need:`STV_SWR_047`, :need:`STV_SWR_048`, :need:`STV_SWR_049`, :need:`STV_SWR_050`, :need:`STV_SYS_004`, :need:`STV_SYS_005`, :need:`STV_SYS_006`, :need:`STV_SYS_010`
   * - ``tests.test_browser::test_missing_placeholder_and_detail_error[file]``
     - passed
     - :need:`STV_SWR_027`, :need:`STV_SWR_028`, :need:`STV_SWR_029`, :need:`STV_SYS_004`
   * - ``tests.test_browser::test_missing_placeholder_and_detail_error[http]``
     - passed
     - :need:`STV_SWR_027`, :need:`STV_SWR_028`, :need:`STV_SWR_029`, :need:`STV_SYS_004`
   * - ``tests.test_browser::test_documentation_visuals``
     - passed
     - :need:``
   * - ``tests.test_build::test_cross_page_bundle``
     - passed
     - :need:`STV_SWR_001`, :need:`STV_SWR_002`, :need:`STV_SWR_013`, :need:`STV_SWR_026`, :need:`STV_SYS_001`
   * - ``tests.test_build::test_invalid_seed_source_location[UNKNOWN]``
     - passed
     - :need:`STV_SWR_026`, :need:`STV_SWR_048`, :need:`STV_SYS_001`
   * - ``tests.test_build::test_invalid_seed_source_location[ROOT_A UNKNOWN]``
     - passed
     - :need:`STV_SWR_026`, :need:`STV_SWR_048`, :need:`STV_SYS_001`
   * - ``tests.test_build::test_invalid_seed_source_location[HIDDEN_A]``
     - passed
     - :need:`STV_SWR_026`, :need:`STV_SWR_048`, :need:`STV_SYS_001`
   * - ``tests.test_build::test_host_owns_broken_trace_failure``
     - passed
     - :need:`STV_SWR_027`, :need:`STV_SWR_028`
   * - ``tests.test_build::test_incremental_body_change_hidden_and_deleted_objects``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_018`, :need:`STV_SWR_048`
   * - ``tests.test_build::test_seed_capacity_at_directive[200-True]``
     - passed
     - :need:`STV_SWR_001`, :need:`STV_SWR_026`, :need:`STV_SWR_043`
   * - ``tests.test_build::test_seed_capacity_at_directive[201-False]``
     - passed
     - :need:`STV_SWR_001`, :need:`STV_SWR_026`, :need:`STV_SWR_043`
   * - ``tests.test_build::test_alternate_host_schema_external_metadata_and_parts``
     - passed
     - :need:`STV_SWR_014`, :need:`STV_SWR_036`, :need:`STV_SWR_045`, :need:`STV_SWR_047`, :need:`STV_SWR_048`, :need:`STV_SYS_002`
   * - ``tests.test_build::test_invalid_mapping_has_entry_path_and_location``
     - passed
     - :need:`STV_SWR_036`
   * - ``tests.test_build::test_unsupported_builder_fails_clearly``
     - passed
     - :need:`STV_SWR_001`
   * - ``tests.test_bundle::test_classic_registration_treats_prototype_keys_and_script_text_as_data``
     - passed
     - :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_027`
   * - ``tests.test_capacity::test_large_project_at_visible_capacity``
     - passed
     - :need:`STV_SWR_043`, :need:`STV_SWR_044`, :need:`STV_SYS_008`
   * - ``tests.test_details::test_static_details_and_remote_fallback``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`, :need:`STV_SWR_048`, :need:`STV_SWR_049`
   * - ``tests.test_details::test_portable_paths_preserve_queries_and_fragments``
     - passed
     - :need:`STV_SWR_018`
   * - ``tests.test_details::test_srcset_data_images_and_css_resources``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_018`
   * - ``tests.test_details::test_active_embed_urls_are_not_retained_as_navigation``
     - passed
     - :need:`STV_SWR_015`, :need:`STV_SWR_017`, :need:`STV_SWR_049`
   * - ``tests.test_graph::test_hidden_parts_external_and_missing_targets``
     - passed
     - :need:`STV_SWR_013`, :need:`STV_SWR_027`, :need:`STV_SWR_047`, :need:`STV_SWR_048`
   * - ``tests.test_graph::test_external_original_url_rejects_executable_or_nonportable_navigation[javascript:bad()]``
     - passed
     - :need:`STV_SWR_047`
   * - ``tests.test_graph::test_external_original_url_rejects_executable_or_nonportable_navigation[data:text/html,bad]``
     - passed
     - :need:`STV_SWR_047`
   * - ``tests.test_graph::test_external_original_url_rejects_executable_or_nonportable_navigation[file:///private.html]``
     - passed
     - :need:`STV_SWR_047`
   * - ``tests.test_model::test_host_normalization``
     - passed
     - :need:`STV_SWR_014`, :need:`STV_SWR_030`, :need:`STV_SWR_032`, :need:`STV_SWR_036`, :need:`STV_SWR_045`
   * - ``tests.test_model::test_invalid_model[change0-levels]``
     - passed
     - :need:`STV_SWR_036`
   * - ``tests.test_model::test_invalid_model[change1-types.goal]``
     - passed
     - :need:`STV_SWR_036`
   * - ``tests.test_model::test_invalid_model[change2-types]``
     - passed
     - :need:`STV_SWR_036`
   * - ``tests.test_model::test_invalid_model[change3-accepted_statuses]``
     - passed
     - :need:`STV_SWR_036`
   * - ``tests.test_package::test_clean_wheel_host``
     - passed
     - :need:`STV_SWR_042`, :need:`STV_SWR_046`, :need:`STV_SYS_009`
   * - ``test::STV_SWR_009 STV_SWR_010 STV_SWR_011 STV_SWR_012 STV_SWR_037: semantic bands and shared test lane``
     - passed
     - :need:`STV_SWR_009`, :need:`STV_SWR_010`, :need:`STV_SWR_011`, :need:`STV_SWR_012`, :need:`STV_SWR_037`
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
* :download:`Tested wheel <artifacts/sphinx_traceability_view-0.1.0-py3-none-any.whl>`

Browser screenshots
-------------------

* :download:`file-example.png <screenshots/file-example.png>`
* :download:`http-example.png <screenshots/http-example.png>`
* :download:`project-demo.png <screenshots/project-demo.png>`
* :download:`state-diagram.png <screenshots/state-diagram.png>`
* :download:`state-page.png <screenshots/state-page.png>`
