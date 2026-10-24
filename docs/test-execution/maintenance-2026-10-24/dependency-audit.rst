Pinned ELK redistribution audit
===============================

Scope and source identity
-------------------------

This engineering audit covers the exact ELK.js browser code shipped by STV,
not the whole upstream Java SDK or a rebuilt ELK distribution. It compares the
installed ``elk.bundled.js`` byte-for-byte with the verified npm archive, whose
integrity is pinned in ``frontend/package-lock.json``. Both STV's esbuild output
and its unmodified vendor copy contain that upstream code. The maintained
``frontend/legal/elk-inventory.json`` pins its SHA-256 and the legal inputs.

The pinned `ELK.js build.gradle <https://github.com/kieler/elkjs/blob/0.10.0/build.gradle>`_
and `GWT module <https://github.com/kieler/elkjs/blob/0.10.0/src/java/org/eclipse/elk/js/ElkJs.gwt.xml>`_
identify the selected source families and versions. Their original metadata,
POMs, source samples, downloads and hashes are retained here. Source archives
remain at the exact Maven URLs carried in the delivered source notice.

Findings and corrections
------------------------

The previous notices represented the npm-level EPL-2.0 declaration but omitted
compiled dependency licenses and attribution. This was a concrete packaging
finding, not evidence that ELK cannot be redistributed. The corrected inventory
and combined notice include:

.. list-table:: Compiled and generated contributions
   :header-rows: 1

   * - Family
     - Version / provenance
     - License and evidence
   * - ELK / ELK.js
     - Exact npm ELK.js bundle and selected ELK sources
     - EPL-2.0; upstream source headers and npm license
   * - Guava / Guava-GWT
     - Build declaration and Maven 31.1-jre source archives
     - Apache-2.0; parent POM and source headers
   * - GWT runtime / emulation
     - Build declaration and Maven 2.11.0 runtime/source archives
     - Apache-2.0; packaged COPYING and source headers
   * - EMF-GWT common / ecore
     - Build declaration and Maven 2.12.4 source archives
     - EPL-1.0; parent POM and source headers
   * - Xbase / Xtend runtime
     - Build declaration and Maven 2.28.0 source archives
     - EPL-2.0; POM and source headers
   * - Babel inline helpers / Browserify runtime prelude
     - Recognizable helper/prelude code in npm bundle; upstream package licenses
     - MIT; retained license texts (exact resolved upstream compiler versions are not supplied)
   * - web-worker browser shim
     - Four-module Browserify bundle, browser shim; npm package 1.4.1
     - Apache-2.0; npm license and browser entry implementation

There are 172 distinct retained source attribution headers across the selected
Java dependency source archives. The notice conservatively retains attribution
for selected sources eliminated by GWT optimization as well; it does not claim
that all those classes execute in STV. The complete Apache-2.0/EPL-1.0 texts
and upstream MIT notices are included. Package SPDX metadata now represents
Apache-2.0 and EPL-1.0 alongside the existing licenses. STV-owned code remains MIT.

ELK's general NOTICE also mentions libavoid and demo models. The selected
Java-only source roots in ELK.js's build do not include those native/demo/model
distributions. The browser bundle's fourth module exports the native Worker;
it does not include web-worker's Node worker_threads implementation. Build-only
Gradle/compiler dependencies, servlet/validation APIs and Java annotations are
not asserted to be distributed merely because they occur in a build POM.

Limitations of provenance
-------------------------

The npm package supplies generated JavaScript but no exact resolved compiler
lock or complete GWT symbol/source map. Therefore this audit does not claim a
bit-for-bit upstream compiler rebuild or exact attribution of every optimized
statement to one Java source file. It verifies the immutable upstream binary,
reviews the explicit GWT module/build inputs and retains their source/licenses.
This is the completed engineering scope requested for STV redistribution;
it does not assign rights to the owner's unrelated employer materials.

Regression protection and disposition
-------------------------------------

``frontend/build.js`` derives npm attributions from actual esbuild inputs,
adds the compiled-dependency inventory and source/license notices, and rejects
an ELK binary/version or audited legal input that no longer matches. The runtime
wheel and generated HTML include ``vendor/ELK-INVENTORY.json``. The installed
consumer case checks the delivered notice families and the vendor hash.

Disposition: the missing-notice/inventory engineering finding is corrected.
Any change to the pinned upstream ELK bundle requires renewing this audit;
passing runtime tests alone cannot renew it. Acceptance and actual check
results are recorded in :doc:`../../concept-reviews/round-8` and :doc:`index`.
