---
name: generate-screen
description: >-
  Generate a complete, build-ready screen specification from a text brief, a screenshot description, or an existing DESIGN.md. Produces layout structure, component inventory, content, and states — no design tool or vendor account required.
---

# Generate Screen

Turn a rough idea ("a pricing page for a coffee subscription") into a screen specification precise enough that a developer or a build skill can implement it without asking questions. You work only from the brief, any attached image description, and the project's DESIGN.md if one exists.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- The user describes a new screen, page, or view in words and wants it designed
- A screenshot or mockup description needs to become a structured spec
- A flow needs an additional state screen (empty, error, loading, success)
- The user says "design me a …" without naming components or layout

## Inputs you work from

- The brief: purpose of the screen, primary user, primary action
- DESIGN.md or token file if present (colors, type scale, spacing, radius)
- Content realities: real labels, real data shapes, longest plausible strings
- Target surface: mobile, desktop, or responsive web; app or marketing page

## Workflow

1. Restate the goal in one sentence: who arrives here, what they must do, what success looks like. If the primary action is ambiguous, pick the most likely one and state the assumption.
2. Choose a layout skeleton first (single column, split, sidebar + content, grid of cards) based on content density — not on taste.
3. Define the visual hierarchy: one dominant element, then supporting groups in reading order. Name the heading, subheading, primary CTA, and secondary actions.
4. Inventory every component with its content: header, hero, cards, lists, forms, footers. Write the actual copy, not lorem ipsum.
5. Specify all states for interactive elements: default, hover/focus, loading, empty, error, disabled, success.
6. Attach tokens to every visual decision (spacing steps, type sizes, colors) using the project scale or the default 4pt scale.
7. End with a build order: which components to implement first and what can be stubbed.

## Rules

- One primary action per screen. If everything is emphasized, nothing is.
- Use real content lengths: design for the 40-character product name, not the 8-character demo one.
- Every screen must define its empty state and its error state — they are part of the design, not afterthoughts.
- Stay on the token scale: no arbitrary 13px gaps or one-off hex colors when a token exists.
- Mobile layout is a re-stack with re-prioritization, not a squeezed desktop layout.
- Never invent brand assets (logos, product photos). Mark them as placeholders with required dimensions.

## Output

- A screen spec with sections: Goal, Layout, Hierarchy, Components (with copy), States, Tokens used, Build order
- Component names in kebab-case so build skills can map them 1:1 to files
- Open questions listed separately — never silently resolved

## Common pitfalls

- Designing only the happy path and forgetting loading/empty/error states
- Copying a famous app's layout when the content model is completely different
- Specifying pixel-perfect visuals but no behavior (what happens on click, submit, failure)

## Quality checklist

- [ ] Primary action is identifiable within 2 seconds of reading the spec
- [ ] All interactive elements have all relevant states defined
- [ ] Copy is real, complete, and fits the longest plausible data
- [ ] Every visual value references a token or a scale step
- [ ] Empty and error states are designed, not omitted
- [ ] Build order is given and matches component dependencies

## Bundled files

- `examples/pricing-screen-spec.md` — a gold-standard example to imitate
- `resources/screen-spec-template.md` — checklist / template / reference for this skill
