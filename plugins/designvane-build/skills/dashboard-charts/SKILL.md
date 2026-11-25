---
name: dashboard-charts
description: >-
  Design and build dashboards and data visualizations that answer questions: KPI cards with honest deltas, the right chart per data shape, accessible color use, and tables that back every chart. Use for analytics, admin, and reporting screens.
---

# Dashboard Charts

A dashboard is an argument: 'here is what changed and what to do about it'. This skill designs dashboards around the questions users actually ask, picks chart forms that don't lie, and makes every visual number traceable to a table.

This skill is vendor-neutral: it works entirely from the brief, the project
files, and any DESIGN.md in the repo. It needs no design-tool account, no
hosted MCP server, and no API key.

## When to use

- An analytics/admin screen needs designing or rebuilding
- Charts exist but users screenshot them into spreadsheets to get answers
- A KPI row needs defining for a new product area
- The user asks for 'a dashboard' with only data sources specified

## Inputs you work from

- The questions the dashboard must answer (top 3, in user language)
- Data available: metrics, dimensions, refresh cadence, typical ranges
- Audience and cadence: exec weekly glance vs operator all-day screen
- Existing tokens and the chart library (or CSS/SVG-only constraint)

## Workflow

1. Write the top-3 questions first. Every widget must serve one of them; anything else is cut or moved to a detail page.
2. Define KPIs with honest math: value, comparison period, delta with direction semantics (up is not always good — state it), and the exact definition in a tooltip/footnote.
3. Choose chart forms by data shape: trend -> line/area; comparison -> bars (never pies beyond 3 slices); part-of-whole -> stacked bars or treemap; distribution -> histogram; correlation -> scatter.
4. Lay out by reading priority: KPIs top, main trend, breakdowns, then the data table that sources every chart.
5. Design states: loading skeletons per widget, empty (no data yet) with the action that creates data, error per-widget (one failure never blanks the page).
6. Make color safe: no red/green-only encoding, direct labels over legends where possible, patterns/labels as backup channels.
7. Add the table view toggle for each chart — the accessible, exportable source of truth.

## Rules

- Axes start at zero for bars; truncated axes on lines must be visibly marked. No dual-axis charts unless the relationship is the point and it's labeled loudly.
- Every number shows its period and its definition on demand. 'Revenue' without a definition is a rumor.
- Deltas state the comparison ('vs previous 30 days') and whether up is good for this metric.
- Max ~6 widgets above the fold; density serves operators, whitespace serves executives — know which screen this is.
- Color is never the only channel: labels, icons, or patterns carry the same information.

## Output

- Dashboard layout spec with per-widget question, chart form, and states
- KPI definitions (formula, period, delta semantics) in writing
- A data-table counterpart spec for every chart

## Common pitfalls

- Pie charts with 9 slices and a legend — a bar chart would answer instantly
- Vanity KPIs (total signups, all-time anything) that can only go up
- One failed widget erroring the whole page

## Quality checklist

- [ ] Top-3 questions written; every widget maps to one
- [ ] Chart forms match data shapes; axis rules obeyed
- [ ] KPI definitions and delta semantics documented
- [ ] Per-widget loading/empty/error states designed
- [ ] Every chart has a table counterpart; color never the only channel

## Bundled files

- `examples/kpi-definitions.md` — a gold-standard example to imitate
- `resources/chart-selection-guide.md` — checklist / template / reference for this skill
