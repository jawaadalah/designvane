---
name: accessibility-audit
description: >-
  Audit a screen or flow against WCAG 2.2 AA: contrast, keyboard paths, focus management, semantics, labels, target sizes, and motion. Returns violations with exact fixes and the criterion each maps to. Use before shipping any UI.
---

# Accessibility Audit

Accessibility failures are specific and fixable — 'the site isn't accessible' is neither. This skill audits methodically, criterion by criterion, and reports each violation with its location, the user it blocks, and the exact remediation.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A screen or flow is about to ship and needs an AA check
- A user reports being unable to complete a task with keyboard or screen reader
- A redesign needs proof it didn't regress accessibility
- Procurement or regulation requires a WCAG statement

## Inputs you work from

- The artifact: code, URL notes, or detailed screen descriptions
- Scope: single screen, a flow (e.g. checkout end-to-end), or a component set
- The DESIGN.md/tokens (contrast pairs come from tokens, not pixels)
- Target: WCAG 2.2 AA (default); note if AAA or a regional law applies

## Workflow

1. Inventory interactive elements and the keyboard path: tab order, visible focus, traps in overlays, Escape behavior, skip links.
2. Check semantics: landmarks, heading order, lists as lists, tables with headers, buttons vs links used correctly.
3. Check names: every control has an accessible name (label, aria-label); icon-only controls are the usual suspects.
4. Measure contrast for every text/background and UI-component pair from the token values; record ratios, not impressions.
5. Check forms: labels associated, errors identified in text (not color alone), instructions before the field, aria-describedby wiring.
6. Check motion and timing: prefers-reduced-motion respected, no auto-playing content without pause, timeouts warned and extendable.
7. Check target sizes (>= 24px AA minimum, 44px recommended) and reflow at 320px width / 400% zoom without horizontal scrolling.
8. Report per violation: criterion (e.g. 1.4.3), location, who is blocked, evidence (ratio/order), and the concrete fix.

## Rules

- Contrast is measured from values, never eyeballed from a screenshot.
- Color-only information is always a violation, whatever the contrast ratio.
- 'The screen reader experience' is tested via semantics and names — if the markup is right, say what you verified and what needs a live SR pass.
- Severity by user impact: blocked task > degraded task > inconvenience. A missing label on the Pay button outranks ten contrast nits in the footer.
- Positives are recorded too: passing areas are stated so teams don't 'fix' what works.

## Output

- Violation list: criterion, location, impact, evidence, fix — ranked by user impact
- A pass list of verified-good areas
- A retest checklist scoped to the fixes

## Common pitfalls

- Reporting 'needs alt text' without naming which images and what the alt should convey
- Treating automated-scan output as the audit (scanners catch ~30% of issues)
- Fixing contrast by lightening text until it passes math but fails readability in glare — check both directions

## Quality checklist

- [ ] Keyboard path walked end-to-end, focus always visible
- [ ] All controls have accessible names; headings/landmarks correct
- [ ] Contrast ratios recorded for every pair, from token values
- [ ] Form errors in text, associated, and announced
- [ ] Reduced motion, target size, and 320px reflow checked
- [ ] Every violation cites its WCAG criterion and a concrete fix

## Bundled files

- `examples/audit-finding.md` — a gold-standard example to imitate
- `resources/wcag-aa-quick-map.md` — checklist / template / reference for this skill
