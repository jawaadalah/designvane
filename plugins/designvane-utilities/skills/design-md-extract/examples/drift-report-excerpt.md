# Gold standard — drift report excerpt

## Color clusters (harvested: 214 color declarations)
- Ink: #1C1917 x96 (canonical) · #1D1A16 x7 · #201D1A x3 · black x5
  -> adopt #1C1917; 15 declarations to migrate.
- Accent: #C2410C x61 (canonical) · #EA580C x22 — both used for primary
  buttons on different screens. -> buttons standardize on #C2410C;
  #EA580C remains the hover step. 22 usages to re-map.
- One-off: #7C3AED x1 (a purple badge on the billing page — no token,
  no other usage). -> replace with accent or remove.

## Spacing
- 87% of spacing values sit on the 4pt grid. Strays: 18px (x14, all card
  padding on marketing pages), 13px (x3), 22px (x2). -> card padding
  standardizes to 16px; marketing cards migrate in one pass.
