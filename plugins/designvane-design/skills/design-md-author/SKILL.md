---
name: design-md-author
description: >-
  Write a DESIGN.md from scratch for a product: brand foundations, tokens, component rules, voice, and do/don't guidance that coding agents can follow when building any screen. Use at project start or when no design documentation exists.
---

# DESIGN.md Author

A DESIGN.md is the single file an agent reads before designing anything in a project. This skill authors one that is specific enough to constrain real decisions — values, not vibes — and short enough to actually be read end to end.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A project has code but no written design direction
- Agent-generated screens keep coming back inconsistent
- A team wants one canonical reference instead of scattered screenshots
- A rebrand needs its rules captured before implementation starts

## Inputs you work from

- Product facts: what it is, who uses it, the feeling it must give (3 words max)
- Any existing assets: logo, current app screenshots, brand colors, fonts in use
- Hard constraints: platforms, accessibility target, performance budget
- Anti-goals: competitors or styles the product must NOT resemble

## Workflow

1. Interview from evidence: mine the repo and existing screens for colors, fonts, and patterns actually in use before asking the user anything.
2. Write the Foundations section: palette (with roles), type scale, spacing, radius, elevation, motion — values, not adjectives.
3. Write Component rules for the 8–12 components the product actually has: anatomy, variants, states, spacing inside the component.
4. Write Layout rules: page max-widths, grid, breakpoints, and how density changes between marketing and app surfaces.
5. Write Voice & content: tone, capitalization, button label style, error message style, with 3 rewritten examples.
6. Add a Do / Don't table with at least 8 pairs drawn from real mistakes or risks in this product.
7. Close with a Decision log section (dated entries) so future changes have a home.

## Rules

- Every rule must be testable: 'headings are sentence case' passes; 'keep it clean' fails.
- If a value is unknown, write the default you chose and mark it (default) — never leave TBD holes.
- Keep the file under ~400 lines; link out for deep dives instead of growing it forever.
- Name the anti-goals explicitly; 'not playful, not crypto-neon' prevents whole classes of drift.
- Examples beat descriptions: show one correct button label, one correct error message.

## Output

- A complete DESIGN.md ready to commit at the repo root
- A summary of defaults chosen where evidence was missing
- Suggested first three screens to rebuild as reference implementations

## Common pitfalls

- Writing a brand book (history, mission poetry) instead of an implementation contract
- Documenting the aspirational design while the shipped product looks different, with no note of which wins
- No decision log — six months later nobody knows why the radius changed

## Quality checklist

- [ ] Foundations contain numeric values for color, type, space, radius
- [ ] Component rules cover anatomy, variants, and states
- [ ] Voice section includes rewritten before/after examples
- [ ] Do/Don't table has >= 8 concrete pairs
- [ ] File is <= ~400 lines and readable in one sitting

## Bundled files

- `examples/design-md-excerpt.md` — a gold-standard example to imitate
- `resources/design-md-outline.md` — checklist / template / reference for this skill
