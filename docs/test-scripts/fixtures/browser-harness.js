// Test-only dependency control. This file is not included in the product bundle.
import {mount} from '../../frontend/src/view.js';
import {compute} from '../../frontend/src/layout.js';
globalThis.stvHarness={mount,compute};
