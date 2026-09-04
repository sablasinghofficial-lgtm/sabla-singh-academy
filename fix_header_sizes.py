# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# Fix Navbar container height so logo isn't choked
css = css.replace(".navbar .container{display:flex;align-items:center;justify-content:space-between;height:75px}", 
                  ".navbar .container{display:flex;align-items:center;justify-content:space-between;min-height:95px; padding-top:10px; padding-bottom:10px;}")

# Increase font size for nav links
css = css.replace("font-size:.73rem;font-weight:600;letter-spacing:1.2px;", 
                  "font-size:0.95rem;font-weight:600;letter-spacing:1px;")

# Increase Book Appointment button size
css = css.replace("padding:11px 22px;border-radius:6px;font-size:.72rem;", 
                  "padding:14px 28px;border-radius:6px;font-size:0.9rem;")

# Increase Top Bar font size
css = css.replace(".tb-left a,.tb-left \nspan{display:inline-flex;align-items:center;gap:5px;color:#111;font-weight:500;transition:opacity .3s}", 
                  ".tb-left a,.tb-left span{display:inline-flex;align-items:center;gap:6px;color:#111;font-weight:600;font-size:0.9rem;transition:opacity .3s}")

# Just in case the newline was missed
css = css.replace(".tb-left a,.tb-left span{display:inline-flex;align-items:center;gap:5px;color:#111;font-weight:500;transition:opacity .3s}", 
                  ".tb-left a,.tb-left span{display:inline-flex;align-items:center;gap:6px;color:#111;font-weight:600;font-size:0.9rem;transition:opacity .3s}")

# Increase container max-width to allow more spread on big monitors
css = css.replace(".container{max-width:1280px;", ".container{max-width:1440px;")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Header sizes fixed!")
