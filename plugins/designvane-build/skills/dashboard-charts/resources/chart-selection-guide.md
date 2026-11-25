# Chart selection guide

- Change over time -> line (1-4 series) or area (1-2 series, totals matter)
- Compare categories -> vertical bars; many/long labels -> horizontal bars
- Part of whole -> stacked bar (<=5 parts); pie only for <=3 slices, rough read
- Distribution -> histogram; spread + outliers -> box plot
- Two numeric variables -> scatter; add trend line only if it means something
- Ranking -> sorted horizontal bars, values labeled directly
- Single number that matters -> KPI card with delta + sparkline

Never: dual axes by default, 3D anything, rainbow categorical palettes
beyond 6 categories (group the tail as "Other" with a drill-down).
