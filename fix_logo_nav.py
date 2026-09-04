# -*- coding: utf-8 -*-
import glob

for fname in glob.glob("*.html"):
    with open(fname, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace simple logo img with logo + company name
    old_brand = '<a href="index.html" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>'
    new_brand = '''<a href="index.html" class="nav-brand">
    <img src="logo.png" alt="Sabla Singh Academy">
    <div class="brand-text">
      <span class="brand-title">Sabla Singh</span>
      <span class="brand-sub">Academy</span>
    </div>
  </a>'''

    # Also handle the href="#" variant in some pages
    old_brand2 = '<a href="#" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>'

    html = html.replace(old_brand, new_brand)
    html = html.replace(old_brand2, new_brand)

    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)

print("Logo + name updated in all files!")
