# Vue component checklist

Contract
- [ ] defineProps typed, defaults declared; defineEmits payloads typed
- [ ] No prop mutation; v-model via defineModel for form controls

Composition
- [ ] Slots for header/default/footer/empty; no v-html for content
- [ ] Computed variant classes from a lookup, not template ternaries

States & a11y
- [ ] loading (aria-busy), empty, error, disabled all reachable
- [ ] Focus management for overlays via template refs
- [ ] Lists keyed by stable id

Styling
- [ ] Scoped styles; token CSS variables only; no global leakage
