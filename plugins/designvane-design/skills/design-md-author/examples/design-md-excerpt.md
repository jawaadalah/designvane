# Gold standard — DESIGN.md excerpt

## Foundations
- Palette roles: surface #FAFAF9, ink #1C1917, accent #C2410C (burnt orange).
  Accent is for actions and highlights only — never for large background areas.
- Type: Inter, scale 1.25. Headings sentence case, weight 600. Body 16/24.
- Spacing: 4pt scale. Cards pad 16, sections pad 24 (mobile) / 48 (desktop).
- Radius: 8px controls, 12px cards, full for pills/avatars. No other radii.

## Buttons
- Primary: accent bg, white ink, one per screen section.
- Labels are verb + object: "Save changes", "Add card" — never "OK" or "Submit".
- Loading state keeps the label and adds a spinner; width must not change.

## Don't
- Don't use gradients on surfaces. Don't use shadows heavier than elevation-2.
- Don't center body text. Don't use emoji as icons.
