# Gold standard — critique excerpt: Checkout screen

Job: get a decided buyer to payment confirmation with zero hesitation.

## P0
- The primary action is outranked. The promo banner (accent bg, 20px bold)
  is more salient than the Pay button (neutral bg). On a 5-second view the
  eye lands on the banner. Fix: banner to surface-raised + border; Pay button
  to accent per DESIGN.md "one accent action per screen".

## P1
- Total price appears in 3 places with 2 different values (shipping added
  late). Fix: single totals block, shipping shown before the CTA.
- Form errors are color-only (red border). Fix: add icon + message text under
  each field (also an accessibility failure, see below).

## P2
- Card padding is 18px — off the 4pt scale. Fix: 16px (space-4).

## Protect
- The order-summary grouping is excellent; do not let the fixes disturb it.
