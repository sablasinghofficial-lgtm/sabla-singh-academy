# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# I set overflow: visible !important, which is bad for a scrolling marquee (causes scrollbars).
css = css.replace("overflow: visible !important;", "overflow: hidden !important; width: 100vw !important; margin-left: calc(-50vw + 50%) !important;")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Marquee overflow fixed!")
