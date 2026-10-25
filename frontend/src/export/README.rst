SVG export
==========

Captures committed view presentation synchronously into detached inert SVG.
resources.js loads local content-addressed resource records; download.js owns
temporary Blob URL leases. No runtime fetch, network service or live DOM mutation.
Component tests are colocated under tests; browser integration lives in docs/test-scripts.
