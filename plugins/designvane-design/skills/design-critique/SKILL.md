---
name: design-critique
description: >-
  Critique an existing screen, screenshot description, or UI code against hierarchy, spacing, typography, color, consistency, and accessibility heuristics. Returns prioritized, fixable findings — not opinions. Use for design reviews and pre-ship checks.
---

# Design Critique

A useful critique names the problem, shows the evidence, and states the fix. This skill reviews a design the way a senior designer would in a design review: heuristic by heuristic, severity-ranked, with every finding tied to something visible on the screen.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- The user asks 'what's wrong with this UI?' or wants a design review
- A screen is about to ship and needs a pre-flight check
- Users report a page 'feels off' but nobody can articulate why
- Two design variants need an evidence-based comparison

## Inputs you work from

- The screen: screenshot, image description, live URL notes, or the component code
- The screen's job: primary action and audience
- The project DESIGN.md/tokens if they exist (critique against the system, not taste)
- Known constraints: what cannot change (brand color, legacy layout)

## Workflow

1. State the screen's job in one line. Every finding is judged against that job.
2. First-impression pass (5 seconds): what is the eye drawn to? Is it the primary action? Note the gap.
3. Hierarchy pass: heading order, size contrast, grouping (Gestalt proximity), alignment grid breaks.
4. Consistency pass: spacing off the scale, one-off colors, mixed radius, inconsistent component variants.
5. Content pass: label clarity, error/empty copy, truncation risks with real data lengths.
6. Accessibility pass: contrast pairs, focus visibility, target sizes, color-only meaning, heading order.
7. Rank findings: P0 breaks the job, P1 hurts comprehension, P2 polish. Give each a concrete fix and the token/rule it maps to.

## Rules

- Critique the work against its job and its design system — never against your personal taste.
- Every finding needs evidence ('the CTA is the 4th most salient element') and a fix ('raise to accent, demote the banner').
- No finding without a severity. No severity inflation: most screens have zero or one P0.
- Praise is data too: name what works and must be protected during fixes (max 3 items).
- If the artifact is code, cite file/component names; if an image, cite regions (top-left card, footer).

## Output

- Findings list ranked P0/P1/P2, each with evidence + fix + rule reference
- A 'protect this' list of what already works
- A suggested fix order that respects dependencies (system fixes before local ones)

## Common pitfalls

- Aesthetic nitpicks presented as usability findings
- Twenty findings with no ranking — the team fixes the easy P2s and ships the P0
- Proposing a redesign when three token-level fixes solve the actual problems

## Quality checklist

- [ ] Screen's job stated and used as the yardstick throughout
- [ ] Every finding has evidence, severity, and a concrete fix
- [ ] Accessibility pass actually performed, with contrast numbers where relevant
- [ ] At least one strength identified and marked to protect
- [ ] Fix order respects system-before-local dependencies

## Bundled files

- `examples/critique-excerpt.md` — a gold-standard example to imitate
- `resources/critique-heuristics.md` — checklist / template / reference for this skill
