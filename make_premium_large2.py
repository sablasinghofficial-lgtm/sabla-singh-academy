# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# Let's make sure it's VERY clear and big.
css = css.replace("font-size: 1.05rem !important;", "font-size: 1.15rem !important;")
css = css.replace("font-size: 2.6rem !important;", "font-size: 2.8rem !important;")
css = css.replace("height: 90px !important;", "height: 105px !important;")
css = css.replace("min-width: 90px !important;", "min-width: 105px !important;")
css = css.replace("min-height: 115px !important;", "min-height: 130px !important;")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Made even larger!")
