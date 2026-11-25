# Mapping DESIGN.md tokens to Tailwind

- Colors: register semantic names (surface, ink, ink-muted, accent, border,
  danger, success) pointing at the primitive palette. Components use the
  semantic names only.
- Type: extend fontSize with the scale steps (caption, body, body-lg,
  heading-sm/md/lg, display) including line-height pairs.
- Spacing: Tailwind's default scale is already 4pt-based — do not extend it
  with odd values; the constraint is the feature.
- Radius: map none/sm/md/lg/full from tokens; delete unused defaults if the
  team keeps reaching for them.
- v4: define in @theme { --color-accent: ...; --text-heading-md: ...; }.
- v3: define in theme.extend of tailwind.config.js.
