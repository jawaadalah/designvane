# Icon construction rules

Canvas: 24x24, live area 20x20 (2px padding), pixel-aligned strokes.
Keyshapes: circle Ø20, square 18x18, rect 20x16 / 16x20 — draw inside them
so all icons share optical weight.
Stroke: 2px everywhere (1.5px only in a dedicated small set), round caps
and joins, corners 2px radius unless the brand is sharp (then 0, everywhere).
Fill: none by default; solid only for active/selected states of the same glyph.
Optical rules: circles drawn 1px larger than squares to match perceived size;
at 16px, remove inner detail before reducing stroke.
Export: SVG with stroke as strokes (not outlined) for web; currentColor so
icons inherit text color and themes for free.
