// Test-only dependency control. This file is not included in the product bundle.
import {mount} from '../../../frontend/src/render/view.js';
import {compute} from '../../../frontend/src/layout/layout.js';
globalThis.stvHarness={mount,compute};
