Executable test scripts
=======================

Component unit tests live next to their owning implementation; see
:doc:`../elements-software` for code, test and boundary naming conventions. Run all
Python unit and host checks from the repository root with ``python -m pytest``.
Run browser-component units with
``node --test frontend/src/*/tests/*.test.js``.

This folder contains cross-component host integration, real-browser, capacity
and clean-wheel installation checks. Fixture RST files are test inputs,
excluded from documentation discovery. Component unit tests are excluded from
the installed wheel. Canonical test-case identities remain in
:doc:`../test-cases/index`; archived execution selectors remain historical.

* ``test_browser.py``
* ``test_build.py``
* ``test_detail_transport.py``
* ``test_capacity.py``
* ``test_package.py``
* ``test_sdist.py``
* ``test_release_seeds.py``
