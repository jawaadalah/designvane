---
name: html-export
description: >-
  Export a design or app screen to clean, self-contained static HTML: inline or single-file CSS, no framework runtime, semantic markup, and assets embedded or referenced predictably. Use for handoffs, embeds, archives, and email-safe pages.
---

# HTML Export

Sometimes the deliverable is one portable HTML file that must render anywhere, forever, with no build step. This skill produces exports that are faithful to the design and honest about what static HTML cannot do (interactivity becomes links, anchors, or documented stubs).

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- A stakeholder needs a design as a shareable file, not a running app
- A page must be embedded in another system (docs, CMS, help center)
- An archive/snapshot of a screen is needed for review or compliance
- A prototype must work offline or from a file:// open

## Inputs you work from

- The source: component code, screen spec, or running page to capture
- Fidelity target: pixel-faithful snapshot or clean semantic rebuild
- Asset policy: embed images (base64) for a true single file, or relative assets folder
- What interactivity must survive: nav links, anchors, form to nowhere, or pure display

## Workflow

1. Decide the fidelity target with the user — snapshot vs rebuild changes everything downstream. Default: clean semantic rebuild.
2. Extract the content and structure first (headings, landmarks, text) — content survives even if styling is stripped later.
3. Compile the styling into one <style> block or one CSS file using token values; remove framework-only selectors and dead utilities.
4. Handle assets: inline critical images as base64 only if total file stays reasonable (< ~2MB); otherwise ship an assets/ folder with relative paths and say so.
5. Replace JS interactions honestly: tabs become stacked sections or anchor links, modals become linked sections, dead buttons are removed or disabled with a note.
6. Add the export header comment: source, date, fidelity target, and known losses.
7. Verify by opening the file standalone (no server, no network): layout holds, images load, links resolve.

## Rules

- The export must render correctly with network disabled — no CDN fonts or scripts unless the user explicitly accepts them.
- Never fake interactivity: a button that does nothing in the export is removed or visibly disabled.
- Semantic structure is non-negotiable even in snapshot mode (headings and landmarks fixed during export).
- State the losses in the header comment; silent fidelity loss is the worst outcome.
- File naming: <screen>-export.html, assets in <screen>-assets/ when not embedded.

## Output

- The static HTML file (plus assets folder if chosen)
- Header comment documenting source, date, and known losses
- A short list of interactions that were flattened and how

## Common pitfalls

- Exporting with CDN dependencies that break offline or in six months
- Base64-ing 8MB of images into an unusable monster file
- Shipping dead buttons that erode trust in every future handoff

## Quality checklist

- [ ] Renders standalone with network off
- [ ] Headings/landmarks semantic; single h1
- [ ] All assets resolve from the delivered package
- [ ] Flattened interactions listed; no fake controls
- [ ] Header comment states source, date, fidelity target, losses

## Bundled files

- `examples/export-header.md` — a gold-standard example to imitate
- `resources/export-checklist.md` — checklist / template / reference for this skill
