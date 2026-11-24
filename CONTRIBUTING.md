# Contributing to designvane

Thanks for helping. designvane is a content library, so most
contributions are new or improved skills.

## Rules for skills

1. **Name = folder = kebab-case.** The frontmatter `name` must be
   pure kebab-case and identical to the folder name.
2. **Self-contained.** A skill must work on its own: `SKILL.md`
   (>= 60 lines, substantive), one gold-standard file in
   `examples/`, one checklist/template in `resources/`.
3. **Vendor-neutral.** Skills must not require a vendor account, a
   hosted server, or an API key. Work from the brief, the repo, and
   DESIGN.md.
4. **Specific, not templated.** Workflows, rules, and checklists must
   be written for the skill's actual topic.
5. **Original writing.** Do not copy text from other skill libraries;
   the Agent Skills format is a standard, the words must be ours.

## Before you open a PR

```bash
python3 designvane.py validate
python3 selftest.py
```

Both must pass — CI runs the same commands.

## Adding a skill

1. Create `plugins/<plugin>/skills/<your-skill>/` with the three
   required parts.
2. Register the skill path in that plugin's `plugin.json`.
3. Add a row to the catalog tables in `README.md`.
4. Run the validation commands above.

## Style

- Write instructions in the imperative, aimed at the agent doing
  the work.
- Every rule should be checkable; ban vague adjectives unless they
  are defined.
- Examples must be realistic: real copy, real data shapes, real
  edge cases (longest names, empty states, failures).
