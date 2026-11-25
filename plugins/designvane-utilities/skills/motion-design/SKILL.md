---
name: motion-design
description: >-
  Define motion that means something: durations, easings, and choreography for transitions, feedback, and state changes, with reduced-motion alternatives for everything. Use when adding animations, page transitions, or micro-interactions to a product.
---

# Motion Design

Motion is information: it shows where things came from, what changed, and what the system is doing. This skill sets a small motion vocabulary — a few durations, a few easings, clear jobs for each — so animation across a product feels like one system instead of confetti.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- Animations feel random: every component eases differently
- A redesign adds page transitions, sheet/drawer motion, or list choreography
- Users find the UI 'janky' or 'distracting' but nobody can specify why
- Reduced-motion support is required and nothing has an alternative yet

## Inputs you work from

- The product's interactive surfaces: overlays, navigation, lists, feedback moments
- Platform realities: web (CSS/JS), React Native (Reanimated/native), or both
- Brand tone from DESIGN.md: snappy and utilitarian, or soft and expressive
- Performance budget: low-end Android in the matrix? (usually yes)

## Workflow

1. Assign every animation a job from the closed list: feedback (press, toggle), spatial (where did this come from/go to), continuity (shared element, list change), or status (loading, progress). No job = no animation.
2. Fix the duration scale: micro 120ms, standard 200ms, emphasis 320ms; entrances slightly slower than exits (things leaving should not linger).
3. Fix the easing set: standard (ease-out for entrances), decelerate for elements arriving, accelerate for elements leaving, spring only for direct manipulation (drag).
4. Choreograph groups: stagger list items by 20–30ms with a cap (max ~8 staggered), never cascade a whole page.
5. Prefer transform and opacity only; layout-property animation is a performance bug on low-end devices.
6. Define the reduced-motion alternative for every pattern: crossfade or instant change, parallax removed, auto-playing motion stopped.
7. Document the vocabulary in the token file (motion tokens) with one example per pattern.

## Rules

- Every animation names its job; decoration is not a job.
- Durations come from the scale. A 437ms ease is a typo, not a style.
- Exits are faster than entrances; users dismissing something are in a hurry.
- Nothing animates in a loop except status indicators, and those pause off-screen.
- prefers-reduced-motion gets a designed alternative, not a broken half-animation.

## Output

- Motion tokens: duration scale, easing set, per-pattern specs
- A choreography spec for grouped content (stagger rules and caps)
- Reduced-motion alternative defined for every pattern

## Common pitfalls

- Bouncing/springing everything until the app feels like a toy
- Animating width/height/top and shipping jank to low-end phones
- Long exit animations that make the whole product feel slow

## Quality checklist

- [ ] Every pattern has a named job from the closed list
- [ ] Durations/easings drawn only from the token scale
- [ ] Only transform/opacity animated (exceptions justified)
- [ ] Stagger capped; loops limited to status and pausable
- [ ] Reduced-motion alternative designed for every pattern

## Bundled files

- `examples/motion-tokens.css` — a gold-standard example to imitate
- `resources/motion-patterns.md` — checklist / template / reference for this skill
