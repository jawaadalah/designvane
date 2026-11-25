---
name: react-components
description: >-
  Build React components from a screen spec or DESIGN.md: typed props, variant maps, token-driven styling, all interactive states, and accessible markup. Use when implementing UI in a React or Next.js codebase.
---

# React Components

This skill turns a settled design into React components that a design review would pass and a maintainer would enjoy: small, typed, token-driven, and complete with the states most implementations forget.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A screen spec needs implementing in React/Next.js
- Existing components are inconsistent and need rebuilding to the system
- A one-off page element must become a reusable component
- The user pastes a design (or its description) and asks for React code

## Inputs you work from

- The screen spec or DESIGN.md (tokens, component rules)
- Project conventions: styling approach (CSS modules, Tailwind, styled), file layout, TypeScript or not
- Data shapes the component receives — real props, not invented ones
- Which states the design defines: loading, empty, error, disabled

## Workflow

1. Map spec components to files 1:1 (kebab-case spec name -> PascalCase component). No mega-components.
2. Define the props interface first: required vs optional, variant unions as string literals, no `any`, no boolean soup (use a `variant` union instead of `isPrimary/isLarge`).
3. Build the static structure with semantic HTML (button, nav, h2 in order) before any styling.
4. Style exclusively from tokens/CSS variables; variants via a variant map object, not nested ternaries in class strings.
5. Implement every state: hover, focus-visible, active, disabled, loading (with aria-busy), plus data states (empty, error) where the spec defines them.
6. Wire keyboard behavior: focus order, Escape closes overlays, arrow keys in menus/tabs per the ARIA pattern the component follows.
7. Add a usage example (story or example file) showing each variant and state.

## Rules

- One component per file; subcomponents used once stay in the same file.
- No inline hex/px values — tokens only. If a value is missing, flag it; don't invent silently.
- Interactive elements are real <button>/<a> elements, never clickable <div>s.
- Props carry data and callbacks; components never fetch their own data unless the project pattern says so.
- Class strings are built from variant maps so invalid combinations are impossible.

## Output

- Component files with typed props and all states implemented
- An examples/story file demonstrating variants and states
- A note listing any token or spec gaps found while building

## Common pitfalls

- Building the default state beautifully and shipping loading/error as an afterthought
- Boolean prop soup (isPrimary, isLarge, isGhost) creating impossible combinations
- Div-onClick instead of buttons — breaks keyboard, screen readers, and the critique checklist

## Quality checklist

- [ ] Props are typed, variant unions used, no `any`
- [ ] All states from the spec exist and are reachable
- [ ] Semantic HTML and correct heading order
- [ ] Focus-visible style present and visible
- [ ] No raw color/px values outside the token layer
- [ ] Example file shows every variant

## Bundled files

- `examples/TierCard.tsx` — a gold-standard example to imitate
- `resources/component-checklist.md` — checklist / template / reference for this skill
