# Static export checklist

- [ ] Fidelity target chosen and written in the header comment
- [ ] No external requests (fonts/scripts/images) — verify offline
- [ ] Total size sane: single file < ~2MB or assets folder shipped
- [ ] Semantic pass: landmarks, one h1, ordered headings, alt text
- [ ] Interactions flattened honestly; dead controls removed/disabled
- [ ] Links: anchors resolve inside the file; external links are absolute
- [ ] Values frozen at export time are labeled as such (meters, counts)
- [ ] Opened from file:// and from a plain static server — both pass
