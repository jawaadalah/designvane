#!/usr/bin/env python3
"""Standalone test suite for designvane. Run: python3 selftest.py"""
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("designvane", os.path.join(ROOT, "designvane.py"))
dv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dv)

EXPECTED = {
    "designvane-design": ["generate-screen", "prompt-polish", "design-tokens",
                          "design-md-author", "design-critique", "responsive-layout"],
    "designvane-build": ["react-components", "vue-components", "html-tailwind",
                         "react-native-ui", "dashboard-charts", "form-patterns"],
    "designvane-utilities": ["design-md-extract", "html-export", "accessibility-audit",
                             "dark-mode", "icon-system", "motion-design"],
}

results = []
def test(label):
    def deco(fn):
        try:
            fn()
            results.append((label, True, ""))
        except AssertionError as e:
            results.append((label, False, str(e)))
        except Exception as e:  # noqa: BLE001
            results.append((label, False, f"error: {e}"))
        return fn
    return deco

@test("catalog matches the expected 18 skills / 3 plugins")
def _():
    found = {}
    for plugin, name, _ in dv.iter_skills():
        found.setdefault(plugin, []).append(name)
    expected = {k: sorted(v) for k, v in EXPECTED.items()}
    assert found == expected, f"found={found}"

@test("validate_all reports zero problems")
def _():
    _, problems = dv.validate_all()
    assert not problems, "; ".join(problems)

@test("every SKILL.md >= 60 lines with all required sections")
def _():
    for plugin, name, sdir in dv.iter_skills():
        text = open(os.path.join(sdir, "SKILL.md"), encoding="utf-8").read()
        assert text.count("\n") + 1 >= 60, f"{name} too short"
        for section in ("## When to use", "## Workflow", "## Rules",
                        "## Quality checklist", "## Bundled files"):
            assert section in text, f"{name} missing {section}"

@test("frontmatter name is kebab-case and equals folder for all skills")
def _():
    for plugin, name, sdir in dv.iter_skills():
        fm = dv.parse_frontmatter(open(os.path.join(sdir, "SKILL.md"), encoding="utf-8").read())
        assert fm and fm.get("name") == name, f"{plugin}/{name}: {fm}"
        assert dv.KEBAB.match(name), name

@test("each skill ships >=1 example and >=1 resource")
def _():
    for plugin, name, sdir in dv.iter_skills():
        for sub in ("examples", "resources"):
            files = os.listdir(os.path.join(sdir, sub))
            assert files, f"{name}/{sub} empty"

@test("plugin.json files parse and reference existing skills")
def _():
    for plugin, names in EXPECTED.items():
        data = json.load(open(os.path.join(ROOT, "plugins", plugin, "plugin.json"), encoding="utf-8"))
        refs = [r.split("/")[-1] for r in data["skills"]]
        assert sorted(refs) == sorted(names), f"{plugin}: {refs}"

@test("marketplace.json registers exactly the 3 plugins")
def _():
    data = json.load(open(os.path.join(ROOT, ".agents", "plugins", "marketplace.json"), encoding="utf-8"))
    assert sorted(p["name"] for p in data["plugins"]) == sorted(EXPECTED), data

@test("install copies all 18 skills for every target")
def _():
    for target in dv.TARGETS:
        with tempfile.TemporaryDirectory() as td:
            rc = dv.main(["install", "--target", target, "--dest", td])
            assert rc == 0, f"{target} rc={rc}"
            got = sorted(os.listdir(td))
            assert len(got) == 18, f"{target}: {len(got)} installed"
            assert os.path.isfile(os.path.join(td, "dark-mode", "SKILL.md"))

@test("install --plugin installs only that plugin's 6 skills")
def _():
    with tempfile.TemporaryDirectory() as td:
        rc = dv.main(["install", "--target", "opencode", "--plugin",
                      "designvane-design", "--dest", td])
        assert rc == 0 and len(os.listdir(td)) == 6, os.listdir(td)

@test("validator catches a name/folder mismatch (tamper test)")
def _():
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(ROOT, "plugins", "designvane-utilities", "skills", "dark-mode")
        dst = os.path.join(td, "renamed-skill")
        shutil.copytree(src, dst)
        problems = dv.validate_skill("designvane-utilities", "renamed-skill", dst)
        assert problems, "tampered skill was not flagged"

@test("validator catches a missing examples/ folder (tamper test)")
def _():
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(ROOT, "plugins", "designvane-design", "skills", "prompt-polish")
        dst = os.path.join(td, "prompt-polish")
        shutil.copytree(src, dst)
        shutil.rmtree(os.path.join(dst, "examples"))
        problems = dv.validate_skill("designvane-design", "prompt-polish", dst)
        assert any("examples" in p for p in problems), problems

@test("CLI list/validate exit 0 via subprocess")
def _():
    for cmd in ("list", "validate"):
        r = subprocess.run([sys.executable, os.path.join(ROOT, "designvane.py"), cmd],
                           capture_output=True, text=True)
        assert r.returncode == 0, f"{cmd}: {r.stdout} {r.stderr}"

@test("no forbidden words anywhere in the repo")
def _():
    needle = "evo" + "lv"  # built dynamically so this file stays clean itself
    bad = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8", errors="ignore") as f:
                    if needle in f.read().lower():
                        bad.append(p)
            except OSError:
                pass
    assert not bad, f"forbidden word in: {bad}"

def main():
    failed = 0
    for label, ok, detail in results:
        print(f"  {'✓' if ok else '✗'} {label}" + (f" — {detail}" if detail and not ok else ""))
        failed += 0 if ok else 1
    print(f"selftest.py: {len(results) - failed}/{len(results)} passed")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
