# -*- coding: utf-8 -*-
import re
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# I will append overrides for the Hero position and Marquee color
marquee_fix_css = """
/* =========================================================
   HERO POSITION & LUXURY MARQUEE FIX
========================================================= */

/* 1. Pull the Hero Content further up to show marquee above the fold */
.hero-content {
    margin-top: -160px !important; 
}
.hero {
    min-height: 90vh !important; /* Slightly reduce height if it was 100vh */
    padding-bottom: 20px !important; 
}

/* 2. Premium Marquee (Not Yellow) */
.marquee-bar { 
    background: linear-gradient(90deg, #050505, #151515, #050505) !important; 
    border-top: 1.5px solid rgba(245, 199, 26, 0.5) !important;
    border-bottom: 1.5px solid rgba(245, 199, 26, 0.5) !important;
    padding: 22px 0 !important;
    box-shadow: 0 -10px 30px rgba(0,0,0,0.6), 0 10px 30px rgba(0,0,0,0.6) !important;
    position: relative !important;
    z-index: 10 !important;
}

.marquee-track span { 
    color: #FFFFFF !important; 
    font-size: 1.15rem !important; 
    font-weight: 500 !important; 
    letter-spacing: 3px !important;
}

.marquee-track span i { 
    color: var(--gold) !important; /* Keep the diamonds gold for luxury contrast */
    font-size: 0.75rem !important;
    margin: 0 10px !important;
}
"""

css = css + "\n" + marquee_fix_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Hero moved up and Marquee made premium dark!")
