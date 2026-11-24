#!/usr/bin/env python3
"""designvane — vendor-neutral design-to-code Agent Skills installer & validator.

Zero dependencies (Python 3.9+ standard library only). No account, no API key.

Commands:
  list       List all plugins and skills in this repository.
  validate   Validate every skill (frontmatter, kebab-case name == folder,
             description present, examples/ and resources/ present, length).
  install    Copy skills into an agent's skills directory.
  selftest   Run the built-in smoke tests.
"""
import argparse
import json
import os
import re
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
PLUGINS_DIR = os.path.join(ROOT, "plugins")
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MIN_SKILL_LINES = 60

# agent -> (project-scope dir, global-scope dir) relative paths
TARGETS = {
    "claude-code": (".claude/skills", ".claude/skills"),
    "codex": (".codex/skills", ".codex/skills"),
    "cursor": (".cursor/skills", ".cursor/skills"),
    "opencode": (".opencode/skills", ".config/opencode/skills"),
    "agents": (".agents/skills", ".agents/skills"),
}


def iter_skills():
    """Yield (plugin_name, skill_name, skill_dir) for every skill."""
    if not os.path.isdir(PLUGINS_DIR):
        return
    for plugin in sorted(os.listdir(PLUGINS_DIR)):
        skills_dir = os.path.join(PLUGINS_DIR, plugin, "skills")
        if not os.path.isdir(skills_dir):
            continue
        for skill in sorted(os.listdir(skills_dir)):
            sdir = os.path.join(skills_dir, skill)
            if os.path.isdir(sdir):
                yield plugin, skill, sdir


def parse_frontmatter(text):
    """Parse the small YAML subset used by SKILL.md files.

    Supports `key: value` and folded scalars (`key: >-` / `key: >` followed by
    indented lines). Returns dict or None when there is no frontmatter block.
    """
    if not text.startswith("---"):
        return None
    lines = text.splitlines()
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None
    data, key, buf = {}, None, []
    def flush():
        if key is not None:
            data[key] = " ".join(buf).strip()
    for raw in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", raw)
        if m and not raw.startswith((" ", "\t")):
            flush()
            key, val = m.group(1), m.group(2).strip()
            buf = [] if val in (">-", ">", "|-", "|") else [val]
        elif key is not None:
            buf.append(raw.strip())
    flush()
    return data


def validate_skill(plugin, name, sdir):
    """Return a list of problems for one skill (empty list = valid)."""
    problems = []
    skill_md = os.path.join(sdir, "SKILL.md")
    if not os.path.isfile(skill_md):
        return [f"{plugin}/{name}: SKILL.md missing"]
    with open(skill_md, encoding="utf-8") as f:
        text = f.read()
    fm = parse_frontmatter(text)
    if fm is None:
        problems.append(f"{plugin}/{name}: frontmatter block missing/invalid")
    else:
        fname = fm.get("name", "")
        if not fname:
            problems.append(f"{plugin}/{name}: frontmatter 'name' missing")
        elif not KEBAB.match(fname):
            problems.append(f"{plugin}/{name}: name '{fname}' is not kebab-case")
        elif fname != name:
            problems.append(
                f"{plugin}/{name}: frontmatter name '{fname}' != folder '{name}'")
        desc = fm.get("description", "")
        if len(desc) < 40:
            problems.append(f"{plugin}/{name}: description missing or too short")
    nlines = text.count("\n") + 1
    if nlines < MIN_SKILL_LINES:
        problems.append(
            f"{plugin}/{name}: SKILL.md has {nlines} lines (< {MIN_SKILL_LINES})")
    for sub in ("examples", "resources"):
        d = os.path.join(sdir, sub)
        if not os.path.isdir(d) or not any(
                os.path.isfile(os.path.join(d, x)) for x in os.listdir(d)):
            problems.append(f"{plugin}/{name}: {sub}/ missing or empty")
    return problems


def validate_all():
    problems = []
    skills = list(iter_skills())
    if not skills:
        problems.append("no skills found under plugins/")
    for plugin, name, sdir in skills:
        problems.extend(validate_skill(plugin, name, sdir))
    # plugin.json files parse and reference real skills
    for plugin in sorted(os.listdir(PLUGINS_DIR)) if os.path.isdir(PLUGINS_DIR) else []:
        pj = os.path.join(PLUGINS_DIR, plugin, "plugin.json")
        if not os.path.isfile(pj):
            problems.append(f"{plugin}: plugin.json missing")
            continue
        try:
            data = json.load(open(pj, encoding="utf-8"))
            for ref in data.get("skills", []):
                if not os.path.isdir(os.path.join(PLUGINS_DIR, plugin, ref)):
                    problems.append(f"{plugin}: plugin.json skill ref '{ref}' not found")
        except json.JSONDecodeError as e:
            problems.append(f"{plugin}: plugin.json invalid JSON ({e})")
    # marketplace registers every plugin
    mkt = os.path.join(ROOT, ".agents", "plugins", "marketplace.json")
    if not os.path.isfile(mkt):
        problems.append(".agents/plugins/marketplace.json missing")
    else:
        try:
            listed = {p["name"] for p in json.load(open(mkt, encoding="utf-8"))["plugins"]}
            have = {p for p, _, _ in skills}
            if listed != have:
                problems.append(
                    f"marketplace plugins {sorted(listed)} != plugin folders {sorted(have)}")
        except (json.JSONDecodeError, KeyError) as e:
            problems.append(f"marketplace.json invalid ({e})")
    return skills, problems


def cmd_list(_args):
    by_plugin = {}
    for plugin, name, _ in iter_skills():
        by_plugin.setdefault(plugin, []).append(name)
    total = 0
    for plugin in sorted(by_plugin):
        print(f"{plugin} ({len(by_plugin[plugin])} skills)")
        for name in by_plugin[plugin]:
            print(f"  - {name}")
            total += 1
    print(f"Total: {total} skills in {len(by_plugin)} plugins")
    return 0


def cmd_validate(_args):
    skills, problems = validate_all()
    if problems:
        print(f"INVALID — {len(problems)} problem(s) across {len(skills)} skills:")
        for p in problems:
            print(f"  ✗ {p}")
        return 1
    print(f"OK — {len(skills)} skills valid "
          f"(frontmatter, kebab name == folder, description, examples, resources, >= {MIN_SKILL_LINES} lines)")
    return 0


def cmd_install(args):
    if args.target not in TARGETS:
        print(f"unknown target '{args.target}'; choose from {sorted(TARGETS)}")
        return 2
    proj_rel, glob_rel = TARGETS[args.target]
    if args.dest:
        dest_root = args.dest
    elif args.scope == "global":
        dest_root = os.path.join(os.path.expanduser("~"), glob_rel)
    else:
        dest_root = os.path.join(os.getcwd(), proj_rel)
    installed = []
    for plugin, name, sdir in iter_skills():
        if args.plugin and plugin != args.plugin:
            continue
        if args.skill and name != args.skill:
            continue
        dest = os.path.join(dest_root, name)
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(sdir, dest)
        installed.append(name)
    if not installed:
        print("nothing matched the given filters")
        return 2
    print(f"Installed {len(installed)} skill(s) -> {dest_root}")
    for n in installed:
        print(f"  - {n}")
    return 0


def cmd_selftest(_args):
    tests = []
    def check(label, fn):
        try:
            ok, detail = fn()
        except Exception as e:  # noqa: BLE001
            ok, detail = False, f"exception: {e}"
        tests.append((label, ok, detail))

    def t_count():
        n = len(list(iter_skills()))
        return n == 18, f"{n} skills found (expected 18)"
    check("skill count == 18", t_count)

    def t_validate():
        _, problems = validate_all()
        return not problems, "; ".join(problems) if problems else "all valid"
    check("validate_all passes", t_validate)

    def t_frontmatter():
        fm = parse_frontmatter("---\nname: demo-skill\ndescription: >-\n  hello\n  world\n---\nbody\n")
        return fm == {"name": "demo-skill", "description": "hello world"}, str(fm)
    check("frontmatter parser (folded scalar)", t_frontmatter)

    def t_install():
        with tempfile.TemporaryDirectory() as td:
            class A: pass
            a = A(); a.target = "claude-code"; a.scope = "project"
            a.plugin = None; a.skill = "dark-mode"; a.dest = td
            cwd = os.getcwd()
            try:
                rc = cmd_install(a)
            finally:
                os.chdir(cwd)
            ok = rc == 0 and os.path.isfile(os.path.join(td, "dark-mode", "SKILL.md"))
            return ok, f"rc={rc}"
    check("install single skill to temp dir", t_install)

    def t_kebab():
        good = KEBAB.match("generate-screen") and KEBAB.match("html-export")
        bad = KEBAB.match("stitch::generate") or KEBAB.match("Bad_Name")
        return bool(good) and not bad, "kebab regex behaves"
    check("kebab-case rules", t_kebab)

    failed = 0
    for label, ok, detail in tests:
        print(f"  {'✓' if ok else '✗'} {label} — {detail}")
        failed += 0 if ok else 1
    print(f"selftest: {len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


def main(argv=None):
    ap = argparse.ArgumentParser(prog="designvane", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    sub.add_parser("validate")
    sub.add_parser("selftest")
    ins = sub.add_parser("install")
    ins.add_argument("--target", required=True, choices=sorted(TARGETS))
    ins.add_argument("--scope", default="project", choices=["project", "global"])
    ins.add_argument("--plugin", default=None)
    ins.add_argument("--skill", default=None)
    ins.add_argument("--dest", default=None, help="override destination directory (testing)")
    args = ap.parse_args(argv)
    return {"list": cmd_list, "validate": cmd_validate,
            "install": cmd_install, "selftest": cmd_selftest}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
