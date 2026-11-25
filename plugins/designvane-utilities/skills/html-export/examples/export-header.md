# Gold standard — export header + flattening notes

<!--
  EXPORT: billing-settings screen
  Source: src/pages/BillingSettings.tsx (commit a1b2c3d)
  Date: 2026-11-25 · Fidelity: clean semantic rebuild
  Assets: embedded (2 images, total file 412 KB) · No external requests.
  Known losses:
    - Plan comparison tabs -> stacked sections with anchor links.
    - "Upgrade" modal -> separate section #upgrade at page end.
    - Save button disabled: export is read-only by design.
-->

Flattening log (for the recipient):
1. Tabs flattened — content identical, order preserved.
2. Live usage meter replaced by its value at export time (78%).
3. All form fields rendered with their saved values, disabled.
