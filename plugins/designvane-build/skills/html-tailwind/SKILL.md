---
name: html-tailwind
description: >-
  Build static or server-rendered pages with semantic HTML and Tailwind utility classes mapped to design tokens: consistent spacing, typography, and color without a component framework. Use for landing pages, docs, emails templates, and prototypes.
---

# HTML + Tailwind

Framework-free does not mean system-free. This skill builds pages where Tailwind utilities are constrained by the token scale — extended theme values, no arbitrary magic numbers — so plain HTML stays as consistent as a component library.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A landing page, docs page, or prototype needs building without React/Vue
- A design must be delivered as portable HTML (handoff, email, embed)
- Tailwind classes in a project have drifted into arbitrary values everywhere
- A quick page must still obey the product's tokens and type scale

## Inputs you work from

- The screen spec or DESIGN.md, with tokens to map into the Tailwind theme
- Tailwind version in use (v4 CSS-first config or v3 tailwind.config)
- What the page must contain: sections, real copy, real links
- Constraints: single-file deliverable or multi-file; any no-JS requirement

## Workflow

1. Map tokens into the theme first: colors as semantic names, spacing (already 4pt in Tailwind), font sizes from the type scale, radii. Forbid arbitrary values from this point on.
2. Write the semantic skeleton: header/nav/main/section/footer, heading order h1->h2->h3, skip link first.
3. Build section by section with utilities, grouping repeated patterns; when a class string repeats 3+ times, extract a component class (@apply in v3 / @utility or plain CSS in v4) or a partial.
4. Apply responsive prefixes deliberately per the layout spec (stack -> grid at md, etc.), not by shrinking text.
5. Add interaction states: hover, focus-visible (never remove the outline without a replacement), active, disabled.
6. Check the no-JS experience: content readable, nav usable, forms submittable where required.
7. Validate: headings, landmarks, alt text, contrast of utility color pairs.

## Rules

- No arbitrary values (w-[347px], text-[#3a3a3a]) unless documented as a one-off exception.
- Semantic HTML first; utilities never change element meaning (a <div> with cursor-pointer is not a button).
- One h1 per page; heading order never skips for visual size — use classes for size.
- Focus-visible styling is mandatory on every interactive element.
- Repeated class strings get extracted at the third repetition.

## Output

- HTML file(s) with theme-mapped Tailwind classes and full states
- The theme/config snippet that encodes the tokens
- A note of any extracted component classes and why

## Common pitfalls

- Arbitrary-value sprawl that silently forks the design system
- Div-soup with utility classes replacing landmarks and headings
- Removing focus outlines for aesthetics and stranding keyboard users

## Quality checklist

- [ ] Theme encodes tokens; arbitrary values absent or justified
- [ ] Landmarks + single h1 + ordered headings
- [ ] Responsive behavior matches the layout spec at each breakpoint
- [ ] Focus-visible visible on all interactive elements
- [ ] Page works with JS disabled (where required)

## Bundled files

- `examples/hero-section.html` — a gold-standard example to imitate
- `resources/tailwind-token-mapping.md` — checklist / template / reference for this skill
