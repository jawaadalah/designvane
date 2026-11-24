---
name: prompt-polish
description: >-
  Rewrite a vague UI or image-generation prompt into a precise design prompt: subject, layout, style vocabulary, color, typography, constraints, and negative instructions. Use before generating any screen, hero, or visual asset.
---

# Prompt Polish

Most bad generated designs come from bad prompts, not bad models. This skill expands a fuzzy request ("make it look premium") into an explicit brief any agent or image model can execute consistently: concrete nouns, measurable style terms, and explicit exclusions.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- The user gives a one-line or adjective-only design request
- A generated result came back 'not what I meant' and the prompt needs sharpening
- The same visual must be regenerated consistently across several screens
- The user wants a reusable prompt template for a brand or product

## Inputs you work from

- The original prompt, verbatim
- Where the output will live: hero, app screen, icon, social card, print
- Brand constraints if any: colors, fonts, tone words the user already uses
- What went wrong last time, if this is a retry

## Workflow

1. Extract the hard facts from the original prompt: subject, audience, format, any named colors or styles. Never drop a fact while polishing.
2. Replace every vague adjective with observable properties: 'premium' -> 'matte surfaces, generous whitespace, thin 1px borders, no gradients'.
3. Add structure: composition (rule of thirds, centered, split), foreground/background, and the single focal point.
4. Specify the palette by role (background, surface, ink, accent) with hex values or named swatches.
5. Specify typography: typeface class (geometric sans, serif display), weights, and relative sizes — even for image prompts.
6. Add a negative list: what must NOT appear (stock-photo smiles, purple gradients, drop shadows, watermark, extra text).
7. Return the polished prompt plus a one-line note of what you changed and why.

## Rules

- Polish, don't replace: the user's subject and intent survive untouched.
- Every adjective in the output must be checkable ('flat', 'high-contrast') — ban 'nice', 'cool', 'modern' unless defined.
- Text in images: state the exact string, its placement, and its case; models garble unspecified text.
- Keep the final prompt under ~120 words; long prompts dilute the constraints that matter.
- If the user's request conflicts with their own brand constraints, flag it instead of silently choosing.

## Output

- The polished prompt as a single copy-paste block
- A short 'changes' list mapping vague term -> concrete replacement
- Optional variant: a stricter version for regeneration consistency

## Common pitfalls

- Over-specifying until the prompt contradicts itself (minimalist + ornate + playful)
- Adding a style the user never asked for because it is fashionable
- Forgetting the negative list — the highest-leverage part of the prompt

## Quality checklist

- [ ] Original facts all preserved; nothing invented about the product
- [ ] No undefined adjectives remain
- [ ] Palette and typography are named, not implied
- [ ] Negative list present and relevant to past failures
- [ ] Exact strings specified wherever text appears

## Bundled files

- `examples/prompt-before-after.md` — a gold-standard example to imitate
- `resources/style-vocabulary.md` — checklist / template / reference for this skill
