# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# Fix the dark green text on dark background issue
css = css.replace(".hero-meet em { color: var(--green) !important;", ".hero-meet em { color: var(--gold) !important;")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Hero text contrast fixed!")
