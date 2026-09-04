# -*- coding: utf-8 -*-
css = open("style.css", "r", encoding="utf-8").read()

# Make the logo a bit smaller so it balances well with the text
css = css.replace("height: 65px !important;", "height: 55px !important; margin-right: 5px;")
css = css.replace("height:65px !important;", "height: 55px !important; margin-right: 5px;")

# Ensure text colors look premium on white navbar
if ".brand-title" in css:
    css = css.replace("color: var(--gold);", "color: var(--gold);") # Already good
    # Make brand-sub a bit darker for better readability on white
    css = css.replace("color: #888;", "color: #555;")
    css = css.replace("color:#888;", "color: #555;")

open("style.css", "w", encoding="utf-8").write(css)
print("Logo CSS adjusted for text!")
