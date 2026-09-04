# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

import re

# We will append an absolute theme override to the bottom of the CSS.
theme_css = """
/* =========================================================
   ULTIMATE LUXURY THEME: EMERALD GREEN & VIBRANT GOLD
========================================================= */
:root {
    --gold: #F5C71A !important;      /* Vibrant Gold for text, icons, and highlights */
    --gold-h: #E0B312 !important;
    --green: #064E23 !important;     /* Emerald Green from uploaded image */
    --green-h: #0A6930 !important;
}

/* 1. TOPBAR (Emerald Green Background) */
.topbar { 
    background: var(--green) !important; 
    border-bottom: 2px solid var(--gold) !important;
    box-shadow: 0 4px 15px rgba(6,78,35,0.4) !important;
}
.tb-left a, .tb-left span, .tb-right span { color: #FFFFFF !important; }
.tb-left i { color: var(--gold) !important; opacity: 1 !important; }
.tb-right a { background: var(--gold) !important; color: var(--green) !important; }
.tb-right a:hover { background: #FFFFFF !important; color: var(--green) !important; transform: scale(1.1) !important; }

/* 2. PRIMARY BUTTONS & BADGES (Emerald Green Background) */
.hbtn-gold, .ab-btn, .crs-btn, .vg-btn, .form-submit, .nav-book, .hero-badge, .badge, .apm-exp-badge { 
    background: var(--green) !important; 
    color: #FFFFFF !important; 
    border: 1px solid rgba(245,199,26,0.3) !important; /* Subtle gold border */
    box-shadow: 0 4px 15px rgba(6,78,35,0.5) !important;
}
.hbtn-gold:hover, .ab-btn:hover, .crs-btn:hover, .vg-btn:hover, .form-submit:hover, .nav-book:hover {
    background: var(--green-h) !important;
    color: var(--gold) !important;
    border-color: var(--gold) !important;
    box-shadow: 0 6px 20px rgba(6,78,35,0.7) !important;
}

/* 3. OUTLINE BUTTONS */
.hbtn-outline { border-color: var(--gold) !important; color: var(--gold) !important; }
.hbtn-outline:hover { background: var(--green) !important; color: var(--gold) !important; border-color: var(--green) !important; }

/* 4. CTA SECTION */
.cta::before { background: var(--green) !important; }
.cta { border-top: 3px solid var(--gold) !important; border-bottom: 3px solid var(--gold) !important; }

/* 5. TEXT HIGHLIGHTS & ICONS (Vibrant Gold) */
/* (Since --gold is already updated in :root, most icons will automatically inherit #F5C71A. 
   But we ensure specific hero overrides match the new theme.) */

.hero-main { color: var(--gold) !important; text-shadow: 0 5px 30px rgba(245,199,26,0.3) !important; }
.hero-tagline { color: var(--gold) !important; }
.hero-meet em { color: var(--green) !important; text-shadow: 0 2px 10px rgba(255,255,255,0.2) !important; } /* Green text for Career on Hero */
.hero-academy-name { color: var(--gold) !important; border-left-color: var(--green) !important; }

/* Change hover color for nav links to green */
.nav-links > a.active { color: var(--green) !important; }
.nav-links > a.active::after { background: var(--green) !important; }
.nav-links > a:hover, .dd:hover > a { color: var(--green) !important; }

/* Make the dropdown menu match the theme */
.dd-menu { border-top: 3px solid var(--green) !important; }
.dd-menu a:hover { background: rgba(6,78,35,0.1) !important; color: var(--green) !important; }

/* Gallery / Lightbox */
.lb img { border-color: var(--green) !important; }
.lb-close { background: var(--green) !important; color: #FFF !important; }
.lb-close:hover { background: var(--gold) !important; color: var(--green) !important; }

/* Form inputs focus */
.form-group input:focus, .form-group select:focus, .form-group textarea:focus {
    border-color: var(--green) !important;
    box-shadow: 0 0 0 3px rgba(6,78,35,0.2) !important;
}

/* Some extra accenting "here and there" (or ek colour or kahi kahi) */
.sec-title h2 span, .split-left h2 em, .apm-heading em { color: var(--green) !important; }
"""

css = css + "\n" + theme_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Emerald Green & Vibrant Gold Theme Applied!")
