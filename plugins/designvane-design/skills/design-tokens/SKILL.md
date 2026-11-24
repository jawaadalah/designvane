---
name: design-tokens
description: >-
  Create or repair a design token system: color, typography, spacing, radius, elevation, and motion scales with semantic naming, delivered as CSS variables, JSON, and Tailwind-ready values. Use when starting a design system or taming one-off values.
---

# Design Tokens

Tokens are the contract between design and code. This skill builds a small, strict scale — primitive values first, semantic aliases second — so every screen built afterwards stays consistent without a design tool in the loop.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A project has scattered hex codes and arbitrary pixel values
- A new product needs a foundation before screens are designed
- Dark mode is planned and raw color values would make it painful
- Two platforms (web + native) must share one visual language

## Inputs you work from

- Existing brand colors/fonts if any (even a logo is enough to seed a palette)
- Target outputs: CSS variables, Tailwind config, JSON for native, or all three
- Surfaces the product uses: app UI, marketing, email — scales differ
- Accessibility target: WCAG AA is the default floor

## Workflow

1. Inventory what exists: grep the codebase or spec for raw colors, font sizes, and spacing values; list the duplicates and near-duplicates.
2. Define primitives: a neutral ramp (50–950), one primary ramp, and semantic hues (success, warning, danger, info) each with 9–11 steps.
3. Define the type scale on a ratio (1.25 or 1.333): caption, body-sm, body, body-lg, heading-sm/md/lg, display.
4. Define spacing on a 4pt base: 4, 8, 12, 16, 24, 32, 48, 64, 96. No other values are legal in UI code.
5. Define radius (none/sm/md/lg/full), elevation (3 shadow levels), and motion (durations 120/200/320ms, standard easings).
6. Create semantic aliases (surface, surface-raised, ink, ink-muted, accent, border) that point at primitives — components may only use aliases.
7. Check every text/background alias pair for WCAG AA contrast; adjust the primitive, never the pair.
8. Emit all requested formats from the single source and add a usage note per alias.

## Rules

- Components consume semantic aliases only; primitives are for the token file itself.
- A new token needs a use case in two places, or it does not get added.
- Names describe role, not appearance: `ink-muted`, never `grey-600-text` in component code.
- One source of truth: other formats are generated, never hand-edited copies.
- Deprecate before deleting: mark tokens deprecated for one release so usages can migrate.

## Output

- Token source (JSON) plus generated CSS variables and/or Tailwind values
- A contrast report for all text-on-surface pairs
- A short usage guide: which alias for which situation

## Common pitfalls

- Copying a giant token set from a big design system — 200 unused tokens are worse than 40 used ones
- Semantic names that leak appearance (`blue-button`) and break under rebranding
- Skipping the contrast check and discovering it at audit time

## Quality checklist

- [ ] Every primitive belongs to a scale with consistent steps
- [ ] All component-facing names are semantic
- [ ] AA contrast verified for every text/background pair
- [ ] All output formats generated from one source file
- [ ] Usage guidance included, with at least one example per category

## Bundled files

- `examples/tokens.css` — a gold-standard example to imitate
- `resources/token-naming-guide.md` — checklist / template / reference for this skill
