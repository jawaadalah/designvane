---
name: icon-system
description: >-
  Build or clean up an icon system: a consistent grid, stroke and corner rules, a naming convention, semantic coverage for the product's real actions, and accessible usage rules. Use when icons are inconsistent, missing, or mixed from multiple sets.
---

# Icon System

Icons fail quietly: three stroke widths, five visual metaphors for 'settings', and an emoji standing in for a warning. This skill defines one grid, one style, and a governed inventory so every icon in the product looks like family and means one thing.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- Icons come from multiple sets and visibly clash
- Designers/agents keep drawing one-offs for the same concept
- A new product needs its icon foundation defined
- Accessibility review flags icon-only buttons with unclear meaning

## Inputs you work from

- The product's real action inventory (from its screens, not a generic list)
- Current icon sources in use and the license of each set
- Rendering constraints: SVG in web/native, sizes actually displayed (16/20/24)
- Brand personality constraints from DESIGN.md (rounded vs sharp, playful vs strict)

## Workflow

1. Inventory: list every icon in use with its concept, source set, size, and stroke width. Duplicates of concept (two 'settings' glyphs) are findings on sight.
2. Fix the construction rules: one canvas (24px), one keyline grid (circle/square/rect keyshapes), one stroke width (1.5 or 2px), one corner radius, one cap/join style.
3. Define the core set from the product's actions: navigation, actions (add/edit/delete/share), status (success/warning/error/info), and domain icons — usually 40–70 icons, not 400.
4. Write naming: kebab-case concept names (trash, not delete-bin-2), with aliases documented for synonyms users search by.
5. Set usage rules: icon + label by default; icon-only only for the universally learned set (search, close, menu) and always with an accessible name and tooltip.
6. Specify optical sizing: how icons behave at 16 vs 24 (detail reduction, stroke stays constant), and the minimum display size.
7. Create the governance rule: new icon requests check the inventory first; additions follow the construction rules and get reviewed against the core set.

## Rules

- One concept, one icon, everywhere. Synonym glyphs are merged, not kept 'for variety'.
- Icons are drawn on the grid with the house stroke — importing a foreign set wholesale restarts the problem.
- Never use an icon as the only carrier of critical meaning without a text label or accessible name.
- Status icons never rely on color alone: shape differs too (check, triangle, octagon, i).
- Emoji are not icons. Not for status, not for bullets, not 'temporarily'.

## Output

- Construction rules (grid, stroke, corners, keyshapes)
- The core inventory: concept names, aliases, sizes, status assignments
- Usage and governance rules, including the icon-only shortlist

## Common pitfalls

- A 1,000-icon library where the 30 real actions are still inconsistent
- Metaphor drift: a floppy disk 'save' for users who have never seen one, with no label
- Mixed fill and outline styles on the same screen

## Quality checklist

- [ ] Construction rules fixed: canvas, keylines, stroke, corners
- [ ] Core set derived from real product actions; duplicates merged
- [ ] Naming kebab-case with documented aliases
- [ ] Icon-only shortlist defined, each with accessible name rule
- [ ] Status icons differ by shape, not color alone

## Bundled files

- `examples/icon-inventory.md` — a gold-standard example to imitate
- `resources/icon-construction.md` — checklist / template / reference for this skill
