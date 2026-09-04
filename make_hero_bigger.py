# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# Make hero-content wider
css = css.replace("max-width: 620px;", "max-width: 800px;")

# Make hero fonts bigger
css = css.replace("font-size: 2.8rem;", "font-size: 4.5rem;") # hero-sub
css = css.replace("font-size: clamp(3.5rem,6vw,5.5rem);", "font-size: clamp(4.5rem,8vw,7.5rem);") # hero-main
css = css.replace("font-size: 2.2rem;", "font-size: 3.5rem;") # hero-meet (Wait, let me check what it is)
css = css.replace("font-size: 0.9rem;", "font-size: 1.1rem;") # hero-desc
css = css.replace("font-size: 0.88rem;", "font-size: 1.1rem;")

extra = """
/* Hero text overrides to make it HUGE */
.hero-sub { font-size: 4.5rem !important; margin-bottom: -15px !important; }
.hero-main { font-size: clamp(4.5rem, 8vw, 7.5rem) !important; line-height: 1.1 !important; }
.hero-meet { font-size: 3.5rem !important; }
.hero-desc { font-size: 1.15rem !important; max-width: 600px !important; line-height: 1.8 !important; }
"""

css = css + "\n" + extra

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Hero made bigger!")
