# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

premium_3d_css = """
/* =========================================================
   HERO SECTION 3D PREMIUM FIXES (Trust Badge & Buttons)
========================================================= */

/* 1. Trust Badge (3D Glassmorphism) */
.hero-trust {
    display: inline-flex !important;
    align-items: center !important;
    gap: 15px !important;
    padding: 14px 28px !important;
    border-radius: 50px !important;
    background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(0,0,0,0.4)) !important;
    backdrop-filter: blur(15px) !important;
    -webkit-backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(245, 199, 26, 0.4) !important;
    border-top: 1px solid rgba(255, 255, 255, 0.4) !important; /* 3D light reflection */
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), inset 0 2px 5px rgba(255, 255, 255, 0.1) !important;
    margin-bottom: 40px !important;
    width: max-content !important;
}
.hero-trust .trust-icon i {
    font-size: 1.1rem !important;
    color: var(--gold) !important;
    text-shadow: 0 0 10px rgba(245, 199, 26, 0.8) !important;
}
.hero-trust .trust-text {
    font-size: 1.05rem !important;
    color: #F8F8F8 !important;
    letter-spacing: 0.5px !important;
}

/* 2. Hero Action Buttons Row */
.hero-cta-row {
    display: flex !important;
    gap: 20px !important;
    flex-wrap: wrap !important;
    align-items: center !important;
}

/* WhatsApp Button (3D Pill) */
.hero-btn-wa {
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    padding: 18px 40px !important;
    border-radius: 50px !important;
    background: linear-gradient(135deg, #25D366, #128C7E) !important;
    color: #FFFFFF !important;
    /* Massive 3D shadow: Outer drop shadow + Top inset light + Bottom inset dark */
    box-shadow: 
        0 15px 30px rgba(37, 211, 102, 0.4), 
        inset 0 4px 0 rgba(255, 255, 255, 0.4), 
        inset 0 -4px 0 rgba(0, 0, 0, 0.15) !important;
    border: none !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; /* Bouncy transition */
}
.hero-btn-wa i { font-size: 1.4rem !important; margin-right: 5px !important; }

.hero-btn-wa:hover {
    transform: translateY(-5px) scale(1.03) !important;
    box-shadow: 
        0 20px 40px rgba(37, 211, 102, 0.6), 
        inset 0 4px 0 rgba(255, 255, 255, 0.5), 
        inset 0 -4px 0 rgba(0, 0, 0, 0.2) !important;
}

/* Explore Courses Button (3D Dark Glass + Gold Edge) */
.hero-btn-outline {
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    padding: 16px 40px !important;
    border-radius: 50px !important;
    background: linear-gradient(135deg, rgba(20,20,20,0.9), rgba(0,0,0,0.9)) !important;
    backdrop-filter: blur(10px) !important;
    color: var(--gold) !important;
    /* 3D Border and Shadow */
    border: 2px solid var(--gold) !important;
    border-top: 2px solid #FFF !important; /* 3D Highlight */
    box-shadow: 
        0 15px 30px rgba(0, 0, 0, 0.5), 
        inset 0 4px 10px rgba(255, 255, 255, 0.1) !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    transition: all 0.3s ease !important;
}
.hero-btn-outline i { font-size: 1.1rem !important; margin-left: 5px !important; }

.hero-btn-outline:hover {
    background: var(--gold) !important;
    color: #000000 !important;
    border-color: var(--gold) !important;
    border-top-color: #FFFFFF !important;
    box-shadow: 
        0 20px 40px rgba(245, 199, 26, 0.4), 
        inset 0 4px 10px rgba(255, 255, 255, 0.4) !important;
    transform: translateY(-3px) !important;
}
"""

css = css + "\n" + premium_3d_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("3D buttons and trust badge applied!")
