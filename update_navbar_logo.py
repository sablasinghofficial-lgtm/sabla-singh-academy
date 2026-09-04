# -*- coding: utf-8 -*-
import glob

for fname in glob.glob("*.html"):
    with open(fname, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace brand with just the logo img (bigger) since name is IN the logo itself
    # Remove the brand-text div since logo already has "SABLA SINGH ACADEMY" text
    old1 = """<a href="index.html" class="nav-brand">
    <img src="logo.png" alt="Sabla Singh Academy">
    <div class="brand-text">
      <span class="brand-title">Sabla Singh</span>
      <span class="brand-sub">Academy</span>
    </div>
  </a>"""
    new1 = '<a href="index.html" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>'

    old2 = """<a href="#" class="nav-brand">
    <img src="logo.png" alt="Sabla Singh Academy">
    <div class="brand-text">
      <span class="brand-title">Sabla Singh</span>
      <span class="brand-sub">Academy</span>
    </div>
  </a>"""
    new2 = '<a href="index.html" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>'

    html = html.replace(old1, new1)
    html = html.replace(old2, new2)

    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)

print("All navbar logos updated!")
