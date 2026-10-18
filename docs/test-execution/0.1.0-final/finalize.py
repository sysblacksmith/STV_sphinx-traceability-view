"""Consolidate the stable software execution and its publication-only retests.

This retained one-off script never overwrites the issued candidate records.
"""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[3]
RECORD = Path(__file__).resolve().parent
CANDIDATE = RECORD.parent / "0.1.0-candidate-4"


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_blocks(text):
    blocks = re.split(r"(?m)(?=^\.\. (?:sysr|swr)::)", text)[1:]
    return {re.search(r":id: (STV_(?:SYS|SWR)_\d+)", block)[1]:
            re.sub(r"(?m)^   :verification_state:.*\n", "", block).strip()
            for block in blocks}


def main():
    output = RECORD / "publication-results.json"
    if output.exists():
        raise SystemExit("Issued publication result exists; retain it and use a new retest record.")
    candidate = json.loads((CANDIDATE / "results.json").read_text(encoding="utf-8"))
    assert candidate["cases"] and all(case["outcome"] == "passed" for case in candidate["cases"])
    assert all(item["returncode"] == 0 for item in candidate["attempts"] if item["suite"] != "documentation")
    frozen = json.loads((CANDIDATE / "source-hashes.json").read_text(encoding="utf-8"))
    assert all(sha(ROOT / name) == digest for name, digest in frozen.items()), "Frozen candidate inputs changed"
    wheel = CANDIDATE / "artifacts" / candidate["wheel"]
    assert sha(wheel) == candidate["wheel_sha256"]
    with zipfile.ZipFile(wheel) as archive:
        for name in archive.namelist():
            if name.startswith("sphinx_traceability_view/") and not name.endswith("/"):
                assert archive.read(name) == (ROOT / "src" / name).read_bytes(), name
    report = {"started": now(), "candidate": "0.1.0-candidate-4",
              "revision": candidate["revision"], "source_identity": candidate["source_identity"],
              "wheel_sha256": candidate["wheel_sha256"], "outcomes": candidate["outcomes"],
              "publication_only_changes": "Need verification fields, chapter evidence links, central maturity, execution records and an RST heading underline; no product/test changes",
              "commands": [], "requirements": {}}
    for name, expected_count in (("system.rst", 10), ("software.rst", 48)):
        path = ROOT / "docs" / name
        before = path.read_text(encoding="utf-8")
        baseline = subprocess.run(["git", "show", "HEAD:docs/" + name], cwd=ROOT,
                                  capture_output=True, text=True, encoding="utf-8", check=True).stdout
        assert canonical_blocks(before) == canonical_blocks(baseline), "Accepted requirement content changed"
        count = 0
        def verified(match):
            nonlocal count
            block = match[0]
            if re.search(r"(?m)^   :tags: release_initial\s*$", block):
                assert ":verification_state: not_assessed" in block
                block = block.replace(":verification_state: not_assessed", ":verification_state: passed")
                count += 1
            return block
        after = re.sub(r"(?ms)^\.\. (?:sysr|swr)::.*?(?=^\.\. (?:sysr|swr)::|\Z)", verified, before)
        assert count == expected_count, (name, count)
        assert canonical_blocks(after) == canonical_blocks(before)
        first_need = re.search(r"(?m)^\.\. (?:sysr|swr)::", after).start()
        after = after[:first_need] + "Executable criteria and retained results: :doc:`test-coverage` and\n:doc:`test-execution/0.1.0-final/index`.\n\n" + after[first_need:]
        report["requirements"][name] = {"before_sha256": sha(path), "verified_initial": count,
                                         "accepted_blocks_unchanged": True}
        path.write_text(after, encoding="utf-8")
        report["requirements"][name]["after_sha256"] = sha(path)
    maturity = ROOT / "docs/maturity.rst"
    text = maturity.read_text(encoding="utf-8")
    start = text.index("Implementation is in progress")
    end = text.index("Project licensing", start)
    replacement = (
        "The initial shared-identity MVP is implemented from clean input revision\n"
        "``30aaba98776ecbe648558d278a985691d81bccb4`` under the owner's implementation\n"
        "instruction on 2026-10-18. It includes the installable extension, offline\n"
        "classic-script bundle, multiple seeds, paged project roots, semantic layout,\n"
        "rich static details, original links and independent accessible viewports.\n\n"
        "The stable candidate's executable suites passed. Its publication-only\n"
        "documentation retest is being finalized in\n"
        ":doc:`test-execution/0.1.0-final/index`. Initial system/software verification\n"
        "fields are updated against those actual results and the criterion review in\n"
        ":doc:`implementation-review`. Stakeholder verification and concept acceptance\n"
        "remain independent; no owner release approval or external publication is implied.\n"
    )
    text = text[:start] + replacement + text[end:]
    text += ("\nImplementation verification dashboard\n"
             "------------------------------------------------------------\n\n"
             "The table reads canonical fields; deferred occurrence-mode criteria remain\n"
             "not_assessed. Executable definitions and results are linked from\n"
             ":doc:`test-coverage` and :doc:`test-execution/0.1.0-final/index`.\n\n"
             ".. needtable::\n   :filter: type in ['sysr', 'swr']\n"
             "   :columns: id;title;verification_state;tags\n")
    maturity.write_text(text, encoding="utf-8")
    env = dict(os.environ, STV_GECKODRIVER=candidate["driver"], STV_SCREENSHOTS=str(RECORD / "screenshots"))
    documentation_python = str(ROOT / ".venv/Scripts/python.exe")
    implementation_python = str(ROOT / ".venv-implementation/Scripts/python.exe")

    def run(name, command):
        entry = {"name": name, "command": command, "cwd": str(ROOT), "started": now(), "log": name + ".log"}
        with (RECORD / entry["log"]).open("w", encoding="utf-8") as stream:
            result = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT)
        entry.update(finished=now(), returncode=result.returncode)
        report["commands"].append(entry)
        print(name + ": " + str(result.returncode), flush=True)
        return result.returncode

    run("coverage-final", [implementation_python, "scripts/check-coverage.py", "--strict"])
    run("documentation-final", [documentation_python, "-m", "sphinx", "-b", "html", "-W", "--keep-going", "docs", "docs/_build/html"])
    run("visual-publication", [implementation_python, "-m", "pytest", "tests/test_browser.py::test_documentation_visuals", "-q", "--junitxml=" + str(RECORD / "visual-publication.xml")])
    shared = ROOT.parent / "#agents/skills/reverse-engineer-requirements/scripts/validate_traceability.py"
    run("traceability-final", [documentation_python, str(shared), "docs/_build/html/needs.json", "--version", "0.1", "--repo-root", str(ROOT), "--csv", str(RECORD / "traceability.csv")])
    run("diagram-publication-final", [documentation_python, "scripts/normalize-diagram-links.py", "--diagram-dir", "docs/architecture/diagrams", "--published-dir", "docs/_build/html"])
    unchanged = [name for name, digest in frozen.items() if not name.startswith("docs/") and sha(ROOT / name) != digest]
    report["product_and_test_inputs_unchanged"] = not unchanged
    report["changed_non_documentation_inputs"] = unchanged
    report["finished"] = now()
    passed = not unchanged and all(entry["returncode"] == 0 for entry in report["commands"])
    report["passed"] = passed
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    metrics = json.loads((CANDIDATE / "capacity-browser.json").read_text(encoding="utf-8"))
    build = json.loads((CANDIDATE / "capacity-build.json").read_text(encoding="utf-8"))
    lines = ["Initial MVP consolidated verification", "=" * 65, "",
             "Outcome: **" + ("all required gates passed after the documented publication retest" if passed else "publication checks remain incomplete") + "**.", "",
             "The software execution is :doc:`../0.1.0-candidate-4/index`. Its product and",
             "test inputs remained stable throughout all executable suites. The first",
             "documentation attempt failed on an RST heading underline in the operating",
             "notes; the failed log is retained there. The first auxiliary retest found",
             "another short underline in this record's draft heading. Both publication",
             "formatting failures and the subsequent passing checks remain available below.", "",
             f"The stable execution recorded **{candidate['outcomes']['passed']} passed, 0 failed, 0 errors, 0 skipped**",
             "across pytest and Node. The supplemental visual publication case is recorded",
             "separately, without inflating that stable-suite total. Initial SYS/SWR",
             "criteria are marked passed after the criterion review in",
             ":doc:`../../implementation-review`; four later occurrence-mode SWRs remain",
             "not_assessed. Stakeholder verification, release approval and project licensing",
             "are not inferred from these results.", "",
             "Candidate identity", "-" * 65, "",
             f"Git input: ``{candidate['revision']}`` plus the retained dirty source/test identity",
             f"``{candidate['source_identity']}``.",
             f"Wheel SHA-256: ``{candidate['wheel_sha256']}``.",
             "The tested wheel is retained in the candidate's artifacts directory. Package",
             "contents were compared byte-for-byte with the final product sources. Accepted",
             "SYS/SWR blocks were compared with the input Git baseline; only their independent",
             "verification metadata changed. No product or executable test changed during",
             "publication retesting.", "",
             "Measurements", "-" * 65, "",
             f"Real host fixture: 30,000 Needs, 90,000 authored edges; build {build['seconds']:.2f} s.",
             f"Graph script {build['graph_bytes']:,} bytes; detail scripts {build['detail_bytes']:,} bytes.",
             "Three browser repetitions per deployment mode, including 200-node scenes:", "",
             ".. list-table:: Observed timings on the recorded Windows machine", "   :header-rows: 1", "",
             "   * - Mode", "     - Startup median / maximum", "     - Expansion median / maximum"]
    for protocol in ("file", "http"):
        m = metrics[protocol]
        lines += ["   * - " + protocol,
                  f"     - {m['startup_median_ms']:.1f} / {m['startup_max_ms']:.1f} ms",
                  f"     - {m['expansion_median_ms']:.1f} / {m['expansion_max_ms']:.1f} ms"]
    lines += ["", "Raw results include collapse, first/cached detail timings and process-tree",
              "working-set measurements. File fixture copying/cleanup is preparation time,",
              "outside the browser timing intervals. Memory can double-count shared pages.",
              "No numeric latency/memory budget has been agreed; the 200-node limit is an",
              "independently passing acceptance criterion. Windows file paths must remain",
              "short enough for Firefox's local loader; see :doc:`../../implementation-review`.", "",
              "Publication attempts and evidence", "-" * 65, "",
              "* :download:`First auxiliary retest (failed draft heading) <documentation-retest.log>`",
              "* :download:`Second auxiliary retest (passed) <documentation-retest-2.log>`",
              "* :download:`Exact publication commands, UTC times and outcomes <publication-results.json>`",
              "* :download:`Retained consolidation/check script <finalize.py>`",
              "* :download:`Visual publication JUnit <visual-publication.xml>`", ""]
    for entry in report["commands"]:
        lines += [f"* {entry['name']}: exit {entry['returncode']}; :download:`log <{entry['log']}>`"]
    lines += ["", "Intermediate attempts", "-" * 65, "",
              "The earlier attempts retain their source-stability failures and passing case",
              "outcomes. They do not verify the final frozen input:", "",
              "* :doc:`../0.1.0-candidate-1/publication` (original report retained with its publication erratum)",
              "* :doc:`../0.1.0-candidate-2/index`", "* :doc:`../0.1.0-candidate-3/index`", ""]
    (RECORD / "index.rst").write_text("\n".join(lines), encoding="utf-8")
    if passed:
        text = maturity.read_text(encoding="utf-8")
        text = text.replace("Its publication-only\ndocumentation retest is being finalized in", "Its publication-only\ndocumentation retest passed; the consolidated record is")
        maturity.write_text(text, encoding="utf-8")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
