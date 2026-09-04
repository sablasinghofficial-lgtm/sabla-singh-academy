# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# Replace the small logo size with a much bigger and prominent size
css = css.replace("height: 50px !important;", "height: 85px !important; min-width: 85px !important;")

# Just in case there are other constraints
extra = """
/* Make logo prominently visible */
.nav-brand { gap: 12px !important; }
.nav-brand img { height: 85px !important; min-width: 85px !important; margin-right: 5px; object-fit: contain; }
.brand-title { font-size: 1.8rem !important; }
.brand-sub { font-size: 0.6rem !important; letter-spacing: 4px !important; }
.navbar .container { align-items: center; }
"""
css = css + "\n" + extra

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Logo size fixed!")
