# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace <section class="hero" id="home">
#   <div class="hero-overlay"></div>
# with the slideshow divs included.

old_str = """<section class="hero" id="home">
  <div class="hero-overlay"></div>"""

new_str = """<section class="hero" id="home">
  <div class="hero-slideshow">
    <div class="hero-slide slide-1"></div>
    <div class="hero-slide slide-2"></div>
    <div class="hero-slide slide-3"></div>
  </div>
  <div class="hero-overlay"></div>"""

if old_str in html:
    html = html.replace(old_str, new_str)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Hero slideshow HTML added!")
else:
    print("Could not find hero string. Trying fallback...")
    import re
    html = re.sub(
        r'(<section class="hero" id="home">\s*<div class="hero-overlay"></div>)',
        new_str,
        html
    )
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Fallback executed!")
