# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

import re

# 1. Remove the global scaling hacks from previous steps
css = re.sub(r'/\* Make everything physically larger on desktop \*/.*?\.hero \{', '.hero {', css, flags=re.DOTALL)

# 2. Add an override at the end of the file to fix the spacing and sizes perfectly
better_css = """
/* ==== NEW LAYOUT FIX (Spread out, Elegant but Readable) ==== */
.container { 
    max-width: 1800px !important; /* Extremely wide container to prevent middle-clumping */
    padding: 0 50px !important; 
}
@media (min-width: 1400px) {
    .container { max-width: 95% !important; } /* Uses 95% of screen width on ultrawide */
}

/* Re-adjust Header Sizes for Elegance + Readability */
.tb-left a, .tb-left span, .tb-right span, .tb-right a { font-size: 0.85rem !important; }
.tb-right a { width: 26px !important; height: 26px !important; }

.navbar .container { min-height: 90px !important; }
.nav-brand { gap: 14px !important; }
.nav-brand img { height: 65px !important; min-width: 65px !important; }
.brand-title { font-size: 1.8rem !important; margin-bottom: 0px !important; }
.brand-sub { font-size: 0.65rem !important; letter-spacing: 4px !important; }

.nav-links { gap: 30px !important; }
.nav-links > a, .dd > a { font-size: 0.85rem !important; letter-spacing: 1.5px !important; }

.nav-book { padding: 12px 26px !important; font-size: 0.85rem !important; }

/* Ensure hero text looks good and not too squished */
.hero-sub { font-size: 3.5rem !important; margin-bottom: -10px !important; }
.hero-main { font-size: 6rem !important; }
.hero-meet { font-size: 2.8rem !important; }
"""

css = css + "\n" + better_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Layout spacing and sizes fixed!")
