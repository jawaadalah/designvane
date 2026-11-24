# Breakpoint playbook

Default breakpoints: 360 (small phone), 768 (tablet portrait), 1024 (tablet
landscape / small laptop), 1440 (desktop). Content max-width 1200–1280 for
reading surfaces; app surfaces may run wider.

Strategies, in preference order:
1. Re-stack (grid -> single column, order by task priority)
2. Collapse (accordion, tabs, disclosure) — content stays reachable
3. Transform (table -> cards, sidebar -> bottom sheet)
4. Scroll region (chips, tab bars) — only for peer items, never for the page
5. Hide with alternate access (menu, search) — last resort, always documented

Always specify: sticky elements budget, media aspect behavior, and the
500px / 900px in-between states.
