# -*- coding: utf-8 -*-
import re
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# Replace the hero-main color
old_hero_main = r"\.hero-main \{ color: var\(--gold\) !important; text-shadow: 0 5px 30px rgba\(245,199,26,0\.3\) !important; \}"
new_hero_main = """
/* Typewriter text in a Dark Charcoal (Not pure black) with a subtle light glow for readability */
.hero-main { 
    color: #2b2b2b !important; 
    text-shadow: 
        0 0 10px rgba(255,255,255,0.5), 
        0 0 20px rgba(255,255,255,0.3) !important; 
}
"""

if re.search(old_hero_main, css):
    css = re.sub(old_hero_main, new_hero_main, css)
else:
    # Fallback if exact match fails
    css += "\n" + new_hero_main

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Typewriter color changed to dark charcoal!")
