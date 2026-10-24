"""Package prepared browser assets; consumers never need Node."""
from pathlib import Path
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version, build_data):
        static = Path(self.root) / "src/sphinx_traceability_view/static"
        for name in ("stv.js", "stv.css", "THIRD_PARTY_NOTICES.txt", "LICENSE.txt", "vendor/elk.bundled.js", "vendor/ELK-SOURCE.txt"):
            if not (static / name).is_file():
                raise RuntimeError(f"Missing browser asset {name}. Maintainers: run npm ci and node build.js in frontend first.")

        if (static / "LICENSE.txt").read_bytes() != (Path(self.root) / "LICENSE").read_bytes():
            raise RuntimeError("Packaged MIT license is stale; rebuild frontend assets")
