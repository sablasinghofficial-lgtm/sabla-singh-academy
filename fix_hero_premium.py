# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

premium_hero_css = """
/* ==== ULTIMATE PREMIUM HERO LOOK ==== */
.hero-content { 
    margin-top: -100px !important; /* Move the whole text block higher up */
}

/* Add beautiful text-shadows and rich colors to everything for a luxury feel */
.hero-tagline { 
    color: #E5C158 !important; 
    text-shadow: 0 2px 15px rgba(0,0,0,0.9) !important; 
    letter-spacing: 6px !important;
}

.hero-sub { 
    color: #FFFFFF !important; 
    text-shadow: 0 4px 25px rgba(0,0,0,0.8) !important; 
    margin-bottom: -5px !important; 
}

.hero-main { 
    color: #F3CB5D !important; /* Rich Gold */
    text-shadow: 0 5px 30px rgba(0,0,0,0.9) !important; 
    padding-bottom: 15px !important; /* Space it out from 'Meets Career' */
}

.hero-meet { 
    color: #FFFFFF !important; 
    text-shadow: 0 4px 25px rgba(0,0,0,0.8) !important; 
    margin-bottom: 35px !important;
}
.hero-meet em {
    color: #E5C158 !important;
}

.hero-academy-name { 
    color: #F3CB5D !important; 
    text-shadow: 0 2px 10px rgba(0,0,0,0.9) !important; 
    letter-spacing: 8px !important; 
    border-left-color: #F3CB5D !important;
}

.hero-brief, .hero-desc { 
    color: #F0F0F0 !important; 
    text-shadow: 0 3px 15px rgba(0,0,0,0.9) !important; 
}

.hero-trust {
    text-shadow: 0 2px 10px rgba(0,0,0,0.9) !important;
}
"""

css = css + "\n" + premium_hero_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Premium colors and spacing applied!")
