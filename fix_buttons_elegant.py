# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# I will append an override that strips away the "plasticky" inset shadows and harsh borders
# and replaces them with a highly polished, elegant, modern luxury aesthetic.

elegant_buttons_css = """
/* =========================================================
   ELEGANT LUXURY BUTTONS (Replacing the fake plastic 3D)
========================================================= */

/* Elegant WhatsApp Button */
.hero-btn-wa {
    background: linear-gradient(135deg, #25D366 0%, #1DA851 100%) !important;
    border: 1px solid rgba(255,255,255,0.15) !important; /* Soft crisp edge */
    box-shadow: 0 10px 25px rgba(29, 168, 81, 0.4) !important; /* Soft glow, no inset plastic */
    padding: 16px 36px !important;
}

.hero-btn-wa:hover {
    background: linear-gradient(135deg, #1DA851 0%, #158740 100%) !important;
    box-shadow: 0 15px 35px rgba(29, 168, 81, 0.5) !important;
    transform: translateY(-3px) !important; /* Smooth lift */
}

/* Elegant Explore Courses Button */
.hero-btn-outline {
    background: rgba(10,10,10, 0.5) !important; /* Sleek dark glass */
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
    border: 1.5px solid var(--gold) !important; /* Uniform luxury gold border */
    border-top: 1.5px solid var(--gold) !important; /* Remove the harsh white edge */
    box-shadow: 0 10px 25px rgba(0,0,0,0.4) !important;
    padding: 16px 36px !important;
}

.hero-btn-outline:hover {
    background: var(--gold) !important;
    color: #000000 !important;
    border-color: var(--gold) !important;
    box-shadow: 0 15px 35px rgba(245, 199, 26, 0.4) !important;
    transform: translateY(-3px) !important;
}
"""

css = css + "\n" + elegant_buttons_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Buttons made elegant and premium!")
