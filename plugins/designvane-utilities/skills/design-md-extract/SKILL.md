---
name: design-md-extract
description: >-
  Reverse-engineer a DESIGN.md from an existing product: mine the codebase or live screens for the colors, type, spacing, and component patterns actually in use, then document them as the de-facto system. Use when a product exists but its design was never written down.
---

# DESIGN.md Extract

Most products already have a design system — it's just undocumented and inconsistent. This skill mines the evidence (CSS, components, screenshots), finds the patterns that actually recur, and writes the DESIGN.md the product has been following without knowing it.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A product exists but has no DESIGN.md and new work keeps drifting
- An audit needs the real (not intended) token values in use
- Onboarding an agent or developer who must match the existing style
- Before a redesign: document the baseline you are changing from

## Inputs you work from

- Access to the codebase (CSS/Tailwind/components) or detailed screen descriptions
- Where the truth lives: tokens file, theme, global CSS, or raw component styles
- Brand assets if any (logo colors are often the seed of the palette)
- Known problem areas the user already suspects (optional but valuable)

## Workflow

1. Harvest mechanically: collect every color value, font-size, spacing value, and radius in the codebase; count frequencies. Frequency is evidence of intent.
2. Cluster near-duplicates (e.g. #1C1917, #1D1A16, #201D1A) — propose the canonical value and list the strays as drift to fix.
3. Reconstruct the scales: sort spacing values and map them onto a 4pt grid; do the same for type sizes onto a ratio; mark off-scale values.
4. Inventory components as actually built: names, variants in use, states implemented (and missing).
5. Infer the unwritten rules from repetition: button label style, card padding, heading case — state them as rules with the evidence count.
6. Write the DESIGN.md in the standard outline, marking each section (observed) or (proposed) so readers know fact from recommendation.
7. End with a drift report: top inconsistencies ranked by frequency x visibility, each with the one-line fix.

## Rules

- Report what is, before prescribing what should be. Observed and proposed never blur.
- A pattern seen once is an anecdote; a pattern seen 10+ times is the system. Threshold your claims.
- Never silently 'fix' values during extraction — canonicalization proposals go in the drift report.
- Screenshots beat memory: where code and shipped UI disagree, shipped UI is the baseline and the disagreement is a finding.
- Keep raw harvest data out of the DESIGN.md; it belongs in the drift report appendix.

## Output

- A DESIGN.md marked (observed)/(proposed) per section
- A drift report: clusters, strays, and ranked fixes
- The frequency evidence behind each claimed pattern

## Common pitfalls

- Documenting the design the team wishes they had, presented as the current one
- Treating the newest screen as canonical just because it is newest
- Missing dark-mode or email surfaces where a second, shadow system lives

## Quality checklist

- [ ] Values harvested with frequencies, not eyeballed
- [ ] Near-duplicates clustered with a canonical proposal
- [ ] Scales reconstructed and off-scale values marked
- [ ] Observed vs proposed labeled in every section
- [ ] Drift report ranked with concrete fixes

## Bundled files

- `examples/drift-report-excerpt.md` — a gold-standard example to imitate
- `resources/extraction-commands.md` — checklist / template / reference for this skill
