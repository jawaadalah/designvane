# Extraction harvest — useful commands

Colors (CSS/SCSS):
  grep -rhoE '#[0-9a-fA-F]{3,8}' src/ | tr 'A-F' 'a-f' | sort | uniq -c | sort -rn
Tailwind arbitrary values (drift hotspots):
  grep -rnE '\[(#[0-9a-fA-F]+|[0-9]+px)\]' src/ | head -50
Font sizes:
  grep -rhoE 'font-size:[^;]+' src/ | sort | uniq -c | sort -rn
Spacing values:
  grep -rhoE '(padding|margin|gap):[^;]+' src/ | sort | uniq -c | sort -rn
Component census:
  ls src/components/ and count variant props per component.

Always record the command and the date with the harvest — values drift.
