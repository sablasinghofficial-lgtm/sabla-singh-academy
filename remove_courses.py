# -*- coding: utf-8 -*-
with open("about.html", "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

import re

# Find the start of the courses section
start_tag = '<!-- --- COURSES FULL --- -->'
end_tag = '<!--  CTA  -->'

# Also handle if emoji got mangled, use regex with section tag
pattern = r'(<!-- --- COURSES FULL --- -->.*?)(?=<!-- [^\n]*CTA [^\n]* -->|<section class="cta">)'

new_html = re.sub(pattern, '', html, flags=re.DOTALL)

with open("about.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Courses section removed from about.html!")
