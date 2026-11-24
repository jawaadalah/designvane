# Token naming guide

Layers:
1. Primitive: `neutral-500`, `primary-600` — raw values, token file only.
2. Semantic: `surface`, `ink`, `ink-muted`, `accent`, `accent-ink`, `border`,
   `danger`, `success` — the only names components may reference.
3. Component (rare): `button-bg`, `card-border` — only when a component truly
   diverges from the semantic layer across the whole product.

Rules of thumb:
- If the name would be wrong after a rebrand, it is in the wrong layer.
- Pairs travel together: every `x` background that carries text needs `x-ink`.
- Steps: color ramps use 50..950; spacing uses the pixel value / 4.
