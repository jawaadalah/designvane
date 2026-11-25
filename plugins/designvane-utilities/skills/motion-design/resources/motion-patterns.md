# Motion patterns (job -> spec)

- Feedback (press/toggle): 120ms, scale 0.98 or bg shift, ease-standard
- Tooltip/popover: 120ms fade + 4px rise, ease-enter; exit 80ms fade
- Menu/dropdown: 160ms, scale from trigger corner (transform-origin set)
- Sheet/drawer: 200ms slide from its edge, ease-enter; exit 160ms ease-exit
- Page transition: 320ms shared-element or crossfade+8px drift, ease-enter
- List insert: 200ms fade+rise, stagger 24ms, cap 8 items, rest appear at once
- List remove: 160ms fade+collapse (height via grid-template-rows trick or FLIP)
- Loading: skeleton shimmer 1200ms loop (pauses off-screen) or spinner
- Success: 320ms check draw or scale-pop once — never confetti by default

Reduced motion: slides -> crossfades, staggers off, loops off, durations
collapse to 0-80ms fades. Content and order never change.
