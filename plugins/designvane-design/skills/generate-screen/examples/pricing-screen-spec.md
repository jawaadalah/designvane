# Gold standard — screen spec excerpt: Pricing screen

## Goal
A returning visitor compares three subscription tiers and starts checkout.
Primary action: choose the middle tier ("Roaster", highlighted as popular).

## Layout
- Desktop: centered column, max-width 1120px; header row, then 3-card grid.
- Mobile: single column stack, popular card first, sticky bottom CTA bar.

## Components
- `tier-card` x3: name, monthly price, 4 feature bullets (real copy), CTA button.
  - States: default, hover (border accent), selected (2px accent ring), disabled (sold-out tier).
- `billing-toggle`: Monthly / Yearly (-20%). State persists across cards.
- `faq-accordion`: 5 real questions, first expanded by default.

## States
- Loading: skeleton cards with shimmer, toggle disabled.
- Error (prices failed to load): inline alert + retry button, cached prices shown with "may be outdated" note.
- Empty: not applicable (static content), fallback copy defined anyway.

## Tokens used
space: 4/8/16/24/40 · radius: lg · type: display-md for price, body-md for features.
