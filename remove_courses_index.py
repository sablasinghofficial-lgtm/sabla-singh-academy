# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

import re

# Find the start of the courses section. In index.html, it's right before <section class="about-premium" id="about">
pattern = r'(<section class="courses-full" id="courses">.*?</section>\s*)(?=<section class="about-premium" id="about">)'

new_html = re.sub(pattern, '', html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Courses section removed from index.html!")
