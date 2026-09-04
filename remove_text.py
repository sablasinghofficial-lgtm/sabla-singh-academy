# -*- coding: utf-8 -*-
with open("gallery.html", "r", encoding="utf-8") as f:
    html = f.read()

text_to_remove = "<p>A glimpse into our premium bridal makeovers, beauty transformations, and behind-the-scenes magic at Studio S.</p>"
html = html.replace(text_to_remove, "")

with open("gallery.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Paragraph removed from gallery.html")
