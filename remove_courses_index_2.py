# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

import re

# Match from <section class="courses-full" up to (but not including) <section class="about-premium"
pattern = r'<section class="courses-full" id="courses">.*?(?=<section class="about-premium" id="about">)'

new_html = re.sub(pattern, '', html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Courses section removed using robust pattern!")
