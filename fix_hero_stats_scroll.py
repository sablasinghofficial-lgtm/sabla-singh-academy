# -*- coding: utf-8 -*-
import re
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# I will replace the rule that forces it to be 100vw width and instead give it a natural alignment
# Existing bad rule:
# .hero-stats-scroll { max-width: 100% !important; margin-top: 40px !important; overflow: hidden !important; width: 100vw !important; margin-left: calc(-50vw + 50%) !important; }

# New rule:
override = """
/* ==== FIX ALIGNMENT OF HERO SCROLLING PILLS ==== */
.hero-stats-scroll { 
    width: 100% !important; 
    max-width: 100% !important; 
    margin-left: 0 !important; /* Removes the negative margin */
    margin-top: 50px !important; 
    overflow: hidden !important; 
}
"""

css = css + "\n" + override

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Hero stats scroll alignment fixed!")
