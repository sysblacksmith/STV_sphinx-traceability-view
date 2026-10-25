Workspace cleanup review
========================

No files were deleted. The following previous successful documentation trees and
temporary local clone are optional cleanup candidates. The current HTML site,
active benchmark, all distributions, release evidence, dependency environments
and offline wheelhouse are retained. Failed diagnostic staging directories are
retained as uncertain evidence. This review is not deletion authorization.

.. list-table:: Optional removal proposal
   :header-rows: 1

   * - Path
     - MiB
     - Consequence
   * - ``docs/_build/.html-previous-0588b5bcde034db28ec2ff36fed12e03``
     - 48.38
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-05e9f0c2a4024fc8bbbd2c2f2b6c455a``
     - 48.41
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-0850c52b0fd247d39364266d747ecfbb``
     - 40.66
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-0d83f8bc9c25474e9cd7720c66ca0a4a``
     - 64.42
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-10e7a9a3e2a442a5b462f5770b548e47``
     - 41.49
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-27b3fe4e4682494cbc871f987bfe3900``
     - 64.40
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-2c8efb2a93614c31bb440e33392ec31a``
     - 48.41
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-3490a11dd0644494bdcb251ad09deeb8``
     - 41.55
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-404a6eb1c325491ead5f964188ea71fc``
     - 64.41
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-4ce947313d4647268d9430ef522b4bd4``
     - 48.36
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-533615533421426a9e570d56ad7e5188``
     - 64.68
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-673ce3ed5e024c5d8ea1a4d5a711c27a``
     - 41.55
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-69212351acad4c0cac4ac71a47bc6a74``
     - 40.65
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-77ce03126c324e549f255d7aca638a5d``
     - 48.41
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-8083e788aa294fdf8d2998a9ccc9df37``
     - 64.39
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-8d6c4d77dffe4338b4d591a53928a914``
     - 40.89
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-905f230925274b5ca5713601bef66d4c``
     - 40.89
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-c45b5609b1414c63ab3f2b7c14edcc87``
     - 64.68
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-d330a83316aa4f5e8b48eb8cf008a4a3``
     - 41.49
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-dd3ae66afacb4e00b562805f311d0ffb``
     - 64.68
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-e441c34099044591af900c4b80b6b8b7``
     - 48.38
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/.html-previous-fb1accdfb6594b2782e107e96ecb69bf``
     - 40.65
     - Rebuild documentation or recreate the verification clone if needed.
   * - ``docs/_build/pr3-clean-checkout``
     - 106.24
     - Rebuild documentation or recreate the verification clone if needed.

Total proposed: 1.190 GiB across 23 directories.

Full initial inventory: :download:`cleanup-inventory.json <cleanup-inventory.json>`.
Post-release cleanup review remains due if publication proceeds.
