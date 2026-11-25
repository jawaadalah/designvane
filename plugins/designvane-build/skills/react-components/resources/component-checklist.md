# React component checklist

Structure
- [ ] One component per file, name matches spec component name
- [ ] Props interface exported; variants as string unions
- [ ] No data fetching inside presentational components

States
- [ ] default / hover / focus-visible / active / disabled
- [ ] loading (aria-busy) and error/empty where the spec defines them

Accessibility
- [ ] Semantic elements; heading order intact
- [ ] Icon-only buttons have aria-label; images have meaningful alt or alt=""
- [ ] Keyboard path tested: tab order, Escape, arrows where applicable

Styling
- [ ] Tokens/variables only; variant map instead of nested ternaries
