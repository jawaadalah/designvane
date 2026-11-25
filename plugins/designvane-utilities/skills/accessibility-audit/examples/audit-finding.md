# Gold standard — audit finding format

## A-03 · 1.4.3 Contrast (Minimum) — High impact
Location: Pricing page, tier-card feature list.
Evidence: feature text uses ink-muted (#78716C) on surface-raised (#FFFFFF)
at 14px = 4.48:1 — just under the 4.5:1 required for small text, and the
same pair at 12px in the footnote is clearly failing in bright light.
Who is blocked: low-vision users reading plan details — the exact content
the page exists to communicate.
Fix: switch feature text to ink (#1C1917, 15.9:1); keep ink-muted only for
>= 16px secondary labels. Token change: tier-card maps feature text to
--ink effective next release. Retest: re-measure this pair + footnote.

## A-04 · 2.1.1 Keyboard — Critical
Location: billing-toggle (Monthly/Yearly). Implemented as clickable divs;
not focusable, not operable by keyboard or switch devices.
Fix: rebuild as a radio group (real inputs, styled) — pattern in the
form-patterns skill. Retest: full keyboard purchase path.
