---
name: vue-components
description: >-
  Build Vue 3 components from a screen spec or DESIGN.md: Composition API with script setup, typed props and emits, token-driven scoped styles, slots for composition, and all interactive states. Use for Vue or Nuxt codebases.
---

# Vue Components

The Vue counterpart of disciplined component building: Composition API, explicit props/emits contracts, and styling that comes from tokens — so a Vue codebase gets the same design fidelity as any other stack.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A screen spec needs implementing in Vue 3 or Nuxt
- Options API components need modernizing to script setup
- A design must be shared between a Vue app and other stacks via tokens
- The user provides a design or screenshot description and asks for Vue code

## Inputs you work from

- The screen spec or DESIGN.md (tokens, component rules)
- Project setup: Vue 3 + script setup assumed; note if Nuxt modules or a UI kit are in play
- Real data shapes for props and the events parents must handle
- States the design defines (loading, empty, error, disabled)

## Workflow

1. Map spec components to Single-File Components 1:1; name files in PascalCase, folders by feature.
2. Declare the contract first: defineProps with types and defaults, defineEmits with payload types. No untyped props.
3. Use slots for composition (header, default, footer, empty) instead of prop-drilling markup or v-html.
4. Style with scoped CSS driven by token variables; variant classes computed from a single `variant` prop via a lookup object.
5. Implement all states, including the empty slot fallback and loading skeleton with aria-busy on the region.
6. Handle keyboard and focus the Vue way: template refs for focus management in overlays, @keydown handlers per ARIA pattern.
7. Provide a small demo page or story showing variants, states, and slot usage.

## Rules

- Composition API with <script setup> only; no Options API in new components.
- Props down, events up — never mutate a prop; emit or use a model.
- v-model only for true two-way form-like bindings, with defineModel where available.
- No global CSS leakage: scoped styles or CSS modules; tokens via CSS variables.
- Lists always keyed by stable ids, never by index for mutable data.

## Output

- SFC files with typed props/emits and complete states
- A demo/story showing variants and slot composition
- Notes on token or spec gaps encountered

## Common pitfalls

- Prop mutation hidden inside a computed setter — parents lose track of state
- Using v-html for content slots (XSS risk and unstyleable markup)
- Forgetting the empty state because the API 'always returns data' — until it doesn't

## Quality checklist

- [ ] defineProps/defineEmits fully typed; defaults sensible
- [ ] Slots used for composition; no v-html for user content
- [ ] All spec states implemented, empty state included
- [ ] Scoped styles, token variables only
- [ ] Keyboard/focus behavior matches the ARIA pattern for the widget type

## Bundled files

- `examples/TierCard.vue` — a gold-standard example to imitate
- `resources/vue-component-checklist.md` — checklist / template / reference for this skill
