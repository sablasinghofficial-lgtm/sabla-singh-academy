# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Revert Hero HTML
import re
# Remove the slideshow block
html = re.sub(
    r'<div class="hero-slideshow">.*?</div>\s*<div class="hero-overlay"></div>',
    '<div class="hero-overlay"></div>',
    html,
    flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Hero HTML reverted.")

with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# Remove the slideshow CSS
css = css.replace(".hero { background: transparent !important; }", "")
css = css.replace("html { font-size: 16px; }", "")
css = re.sub(r'/\* Hero Slideshow CSS \*/.*?.hero-overlay \{ z-index: 1; \}', '', css, flags=re.DOTALL)

# Restore Original Background but MUCH lighter
# In old CSS: .hero::before{content:"";position:absolute;inset:0;background:linear-gradient(105deg,rgba(10,10,10,0.93) 0%,rgba(10,10,10,0.72) 55%,rgba(10,10,10,0.25) 100%);z-index:1}
# Let's completely remove the .hero::before gradient that makes it black.
css = re.sub(r'\.hero::before\{.*?z-index:1\}', '', css)

# Make the hero overlay lighter
css = css.replace(
    ".hero-overlay { background: rgba(5,5,5,0.85); }",
    ".hero-overlay { background: rgba(0,0,0,0.3); } /* Lightened */"
)
css = css.replace(
    """background: linear-gradient(110deg,
    rgba(5,5,5,0.92) 0%,
    rgba(5,5,5,0.80) 45%,
    rgba(5,5,5,0.35) 75%,
    rgba(5,5,5,0.10) 100%);""",
    """background: linear-gradient(110deg,
    rgba(5,5,5,0.6) 0%,
    rgba(5,5,5,0.3) 45%,
    rgba(5,5,5,0.1) 75%,
    rgba(5,5,5,0.0) 100%);"""
)

# Apply global zoom/scale to literally make everything bigger on desktop
zoom_css = """
/* Make everything physically larger on desktop */
@media (min-width: 1024px) {
    html { font-size: 18px !important; } /* This increases all rem values by ~12.5% */
    .container { max-width: 1500px !important; }
}
@media (min-width: 1440px) {
    html { font-size: 20px !important; } /* Very large monitors scale up 25% */
    .container { max-width: 1700px !important; }
}
/* Original Photo Background */
.hero { background: url('hero-bg.jpg') center/cover no-repeat !important; }
"""

css = css + "\n" + zoom_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("CSS Fixed: Bright original background and Global Scale Up.")
