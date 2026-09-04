# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the broken question marks in the tagline with premium diamonds
html = html.replace("? Ranchi's Most Trusted Beauty &amp; Academy ?", "? Ranchi's Most Trusted Beauty &amp; Academy ?")
html = html.replace("? Ranchi's Most Trusted Beauty & Academy ?", "? Ranchi's Most Trusted Beauty & Academy ?")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Hero HTML fixed!")
