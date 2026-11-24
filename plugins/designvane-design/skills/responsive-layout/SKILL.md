---
name: responsive-layout
description: >-
  Define how a screen adapts across breakpoints: what stacks, what hides, what changes priority, and what must never shrink. Produces breakpoint rules and per-component behavior tables for web and app layouts.
---

# Responsive Layout

Responsive is not 'the same design, narrower'. This skill decides, component by component, what changes at each breakpoint — and protects the things that must never be sacrificed: the primary action, readable line length, and touch targets.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A desktop design needs its mobile behavior defined (or vice versa)
- A layout breaks at some in-between width nobody designed for
- A data table, dashboard, or nav must survive small screens
- The user asks 'how should this look on mobile?'

## Inputs you work from

- The screen spec or existing layout, with its component inventory
- Breakpoints in force (default: 360 / 768 / 1024 / 1440)
- Content priorities: what the user must accomplish on a phone vs a desktop
- Non-negotiables: legal text, primary CTA, key data columns

## Workflow

1. Rank every component by importance to the screen's job on the smallest screen. The ranking drives everything else.
2. Define the grid per breakpoint: columns, gutters, max content width, and where the reading line-length lands (45–75 characters).
3. Write the behavior table: per component — full, stacked, collapsed (accordion/tabs), horizontal-scroll, hidden-with-access, or replaced (e.g. table -> cards).
4. Re-order for mobile by task priority, not by desktop visual order; state the new order explicitly.
5. Set the untouchables: min touch target 44px, min body text 16px, primary CTA always visible or sticky.
6. Handle the in-between widths: specify what happens at 500px and 900px, not only at the named breakpoints.
7. Define media behavior: aspect ratios held, art direction crops, and when an image is decorative enough to drop.

## Rules

- Hiding content on mobile is a last resort; collapsing and re-ordering come first. Whatever is hidden needs another path to reach it.
- Tables never just 'scroll sideways' by default — choose: card transform, priority columns, or sticky first column, and say why.
- Type does not shrink below 16px body to 'make it fit'. Layout changes; legibility doesn't.
- Sticky elements (headers, CTA bars) cost vertical space — budget them, max one per screen edge.
- Design the 360px experience with the longest real content, not the demo content.

## Output

- Breakpoint grid definitions
- A per-component behavior table across breakpoints
- Mobile reading order and the list of untouchables verified

## Common pitfalls

- Designing 1440 and 360 and leaving 768–1100 (where most tablet/laptop users live) to chance
- Desktop order preserved on mobile, burying the primary action under hero decoration
- Hover-dependent interactions with no touch equivalent

## Quality checklist

- [ ] Every component has an explicit behavior at every breakpoint
- [ ] Mobile order follows task priority and is written down
- [ ] Touch targets >= 44px and body text >= 16px at all sizes
- [ ] Tables have a chosen small-screen strategy with reasoning
- [ ] In-between widths (500/900) are specified, not implied

## Bundled files

- `examples/behavior-table.md` — a gold-standard example to imitate
- `resources/breakpoint-playbook.md` — checklist / template / reference for this skill
