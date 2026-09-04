# -*- coding: utf-8 -*-
import glob
import re

for fname in glob.glob("*.html"):
    with open(fname, "r", encoding="utf-8") as f:
        html = f.read()

    # Search for the nav-brand block. 
    # It might be <a href="index.html" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>
    
    old_brand_1 = '<a href="index.html" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>'
    old_brand_2 = '<a href="#" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>'
    
    new_brand = """<a href="index.html" class="nav-brand">
        <img src="logo.png" alt="Sabla Singh Academy">
        <div class="brand-text">
          <span class="brand-title">Sabla Singh</span>
          <span class="brand-sub">Academy</span>
        </div>
      </a>"""
      
    if old_brand_1 in html:
        html = html.replace(old_brand_1, new_brand)
    elif old_brand_2 in html:
        html = html.replace(old_brand_2, new_brand)
    else:
        # Fallback regex just in case
        html = re.sub(r'<a href="[^"]*" class="nav-brand">\s*<img src="logo\.png"[^>]*>\s*</a>', new_brand, html)

    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)

print("Brand text added to all HTML files!")
