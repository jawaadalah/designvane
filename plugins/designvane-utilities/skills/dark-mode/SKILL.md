---
name: dark-mode
description: >-
  Add or repair dark mode: token remapping (not inversion), surface elevation in the dark, image and shadow treatment, and a theme toggle that respects system preference. Use when a product with a token system needs a credible dark theme.
---

# Dark Mode

Dark mode is a second design, not a filter. This skill builds it at the token layer — semantic aliases get dark values, elevation gets lighter instead of more shadowed, and brand colors are re-tuned for dark surfaces instead of pasted across.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A token-based product needs dark mode added
- An existing dark mode looks washed out, inverted, or inconsistent
- Users toggle to dark and images/logos/charts break visually
- A new surface (mobile app, dashboard) must ship with both themes

## Inputs you work from

- The token file with semantic aliases (dark mode is impossible to do well without them)
- Brand colors and their roles — which must survive, which may be re-tuned
- Imagery in use: logos, photos, charts, illustrations (each needs a dark decision)
- Platform targets: prefers-color-scheme, in-app toggle, or both

## Workflow

1. Freeze the semantic layer: if components use primitives anywhere, fix that first — dark values can only attach to aliases.
2. Build the dark surface scale: base background darker than any card; elevation RAISES lightness (surface +4%, raised +8%) because shadows vanish on dark.
3. Re-tune the palette: saturated brand colors usually need lightening/desaturating one step for dark backgrounds; verify accent-on-dark contrast separately.
4. Re-check every text pair in dark values (ink becomes near-white but never pure #FFF on pure #000 — soften both).
5. Treat imagery: logos with dark variants or a light chip behind them; photos get a slight brightness reduction; charts re-mapped with the dark palette, gridlines dimmed.
6. Implement the toggle logic: system preference by default, manual override stored, no flash of wrong theme on load (inline script / native splash handling).
7. Walk the top 5 screens in dark and photograph the failures: pure-black smearing on OLED, invisible borders, glowing shadows.

## Rules

- Never invert, never just swap black/white. Every semantic alias gets a deliberate dark value.
- Pure #000 backgrounds + pure #FFF text cause halation and OLED smear; use near-black surfaces and off-white ink.
- Elevation in the dark = lighter surface + border, not bigger shadows.
- Brand recognition survives: the accent may be re-tuned but must still read as the same brand next to the light version.
- The toggle respects the OS first; a manual choice persists and wins until changed.

## Output

- Dark values for every semantic alias (token file addition)
- An imagery treatment list (per asset: keep, dim, variant, chip)
- Toggle behavior spec: default, override, persistence, no-flash method

## Common pitfalls

- Shipping 'dark mode' that is the light palette with a black background slapped on
- Forgetting charts and third-party embeds — the two places dark mode visibly dies
- Theme flash on load because the preference is read after first paint

## Quality checklist

- [ ] Every semantic alias has a deliberate dark value
- [ ] Elevation reads correctly without shadows
- [ ] All text pairs re-measured in dark; accent contrast verified
- [ ] Logos/photos/charts each have an explicit treatment
- [ ] System default + persisted override + no flash on load

## Bundled files

- `examples/dark-tokens.css` — a gold-standard example to imitate
- `resources/dark-mode-checklist.md` — checklist / template / reference for this skill
