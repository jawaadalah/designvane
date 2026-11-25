---
name: form-patterns
description: >-
  Design and build forms that people finish: field grouping, labels, validation timing, error recovery, multi-step flows, and accessible semantics. Use for signup, checkout, settings, onboarding, and any data entry screen.
---

# Form Patterns

Forms are where products make or lose money, and where users feel either respected or interrogated. This skill applies the patterns that measurably raise completion: fewer fields, clear labels, forgiving validation, and errors that help instead of blame.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- Any form is being designed or rebuilt (signup, checkout, settings, onboarding)
- Users abandon a form or rage-submit it repeatedly
- Validation errors are the top support complaint
- A long form needs splitting into steps without losing people

## Inputs you work from

- Every field someone wants to collect — and the business reason for each
- Which fields are truly required vs nice-to-have (be honest)
- Error reality: server validations, formats, uniqueness checks
- Context: one-shot (checkout) vs repeated use (admin data entry)

## Workflow

1. Cut first: for each field ask 'what breaks if we ask later or never?' Move optional fields after the primary action or delete them.
2. Group the survivors into logical chunks (max ~5 per group) ordered by user familiarity, not database order.
3. Write labels as permanent visible text (never placeholder-as-label), with format hints where a format exists ('DD Mon YYYY', IBAN grouping).
4. Choose input types and autocomplete attributes deliberately (email, tel, cc-number, one-time-code) so browsers and password managers help instead of hinder.
5. Set validation timing: validate on blur for format, on submit for the whole form, inline success only where it reassures (password strength). Never yell while typing.
6. Design the error summary + per-field errors: plain language, exact fix, focus moves to the summary, aria-describedby wiring.
7. For multi-step: show progress honestly, allow back without data loss, and put the review step before any irreversible submit.

## Rules

- One column layout for forms (multi-column only for tiny related pairs like first/last name on desktop).
- Required markers: mark optional fields 'optional' when most are required, or required with * when most are optional — pick per form, be consistent.
- Never disable the submit button to 'prevent errors' — let people submit and learn from real errors.
- Placeholders show format examples, never repeat the label.
- Password rules are shown before typing, and paste/password-manager entry is never blocked.

## Output

- Form spec: field list with justification, grouping, labels, hints, autocomplete
- Validation and error-message copy for every rule, written in plain language
- Step map for multi-step flows with save/back behavior

## Common pitfalls

- Placeholder-as-label that vanishes and strands users mid-form
- Validating on every keystroke (red borders while still typing a valid email)
- Asking for data the business never uses 'just in case'

## Quality checklist

- [ ] Every field justified; optional ones marked or removed
- [ ] Labels permanent; hints show formats; autocomplete attributes set
- [ ] Errors: summary + per-field, plain language, focus managed, aria wired
- [ ] Submit never disabled; back preserves data in multi-step
- [ ] Works fully by keyboard and with a password manager

## Bundled files

- `examples/error-messages.md` — a gold-standard example to imitate
- `resources/form-field-checklist.md` — checklist / template / reference for this skill
