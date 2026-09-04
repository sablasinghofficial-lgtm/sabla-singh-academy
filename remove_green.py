# -*- coding: utf-8 -*-
import re
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# We will completely strip the Emerald Green section and replace it with a Pure Vibrant Yellow theme.

yellow_theme_css = """
/* =========================================================
   ULTIMATE LUXURY THEME: VIBRANT YELLOW & PITCH BLACK
========================================================= */
:root {
    --gold: #F5C71A !important;      /* Vibrant Yellow Gold */
    --gold-h: #D4A911 !important;    /* Slightly darker for hover */
}

/* 1. TOPBAR (Yellow Background) */
.topbar { 
    background: var(--gold) !important; 
    border-bottom: 2px solid rgba(0,0,0,0.2) !important;
    box-shadow: 0 4px 15px rgba(245,199,26,0.3) !important;
}
.tb-left a, .tb-left span, .tb-right span { color: #000000 !important; font-weight: 700 !important; }
.tb-left i { color: #000000 !important; opacity: 0.8 !important; }
.tb-right a { background: #000000 !important; color: var(--gold) !important; }
.tb-right a:hover { background: #222222 !important; color: #FFFFFF !important; transform: scale(1.1) !important; }

/* 2. PRIMARY BUTTONS & BADGES (Yellow Background, Black Text) */
.hbtn-gold, .ab-btn, .crs-btn, .vg-btn, .form-submit, .nav-book, .hero-badge, .badge, .apm-exp-badge { 
    background: var(--gold) !important; 
    color: #000000 !important; 
    border: 1px solid var(--gold-h) !important; 
    box-shadow: 0 4px 15px rgba(245,199,26,0.4) !important;
    font-weight: 800 !important;
}
.hbtn-gold:hover, .ab-btn:hover, .crs-btn:hover, .vg-btn:hover, .form-submit:hover, .nav-book:hover {
    background: #000000 !important;
    color: var(--gold) !important;
    border-color: var(--gold) !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.8) !important;
}

/* 3. OUTLINE BUTTONS */
.hbtn-outline { border-color: var(--gold) !important; color: var(--gold) !important; }
.hbtn-outline:hover { background: var(--gold) !important; color: #000 !important; }

/* 4. CTA SECTION */
.cta::before { background: var(--gold) !important; }
.cta { border-top: 3px solid var(--gold) !important; border-bottom: 3px solid var(--gold) !important; }

/* 5. TEXT HIGHLIGHTS & ICONS */
.hero-main { color: var(--gold) !important; text-shadow: 0 5px 30px rgba(245,199,26,0.3) !important; }
.hero-tagline { color: var(--gold) !important; }
.hero-meet em { color: var(--gold) !important; text-shadow: 0 2px 10px rgba(255,255,255,0.2) !important; } 
.hero-academy-name { color: var(--gold) !important; border-left-color: var(--gold) !important; }

/* Change hover color for nav links */
.nav-links > a.active { color: var(--gold) !important; }
.nav-links > a.active::after { background: var(--gold) !important; }
.nav-links > a:hover, .dd:hover > a { color: var(--gold) !important; }

/* Make the dropdown menu match the theme */
.dd-menu { border-top: 3px solid var(--gold) !important; }
.dd-menu a:hover { background: rgba(245,199,26,0.1) !important; color: var(--gold) !important; }

/* Gallery / Lightbox */
.lb img { border-color: var(--gold) !important; }
.lb-close { background: var(--gold) !important; color: #000 !important; }
.lb-close:hover { background: #000 !important; color: var(--gold) !important; }

/* Form inputs focus */
.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(245,199,26,0.2) !important;
}

/* Some extra accenting */
.sec-title h2 span, .split-left h2 em, .apm-heading em { color: var(--gold) !important; }
"""

# Replace the old Emerald block with the new Yellow block
css = re.sub(r'/\* =========================================================\s*ULTIMATE LUXURY THEME: EMERALD GREEN.*?/\* Some extra accenting "here and there".*?\}', yellow_theme_css, css, flags=re.DOTALL)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

# Also fix about.html where I might have hardcoded var(--green)
with open("about.html", "r", encoding="utf-8", errors="replace") as f:
    about = f.read()

about = about.replace("var(--green)", "var(--gold)")
with open("about.html", "w", encoding="utf-8") as f:
    f.write(about)

print("Green removed, Vibrant Yellow applied everywhere!")
