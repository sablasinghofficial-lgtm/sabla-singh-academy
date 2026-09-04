# -*- coding: utf-8 -*-
import re
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# 1. Hero Content & Sizes
hero_css = """
/* ==== HERO SECTION BIGGER ==== */
@media (min-width: 992px) {
    .hero-content { max-width: 1000px !important; margin-top: 40px !important; }
    .hero-tagline { font-size: 1.1rem !important; letter-spacing: 5px !important; margin-bottom: 30px !important; }
    .hero-sub { font-size: 5.5rem !important; margin-bottom: -15px !important; }
    .hero-main { font-size: 8.5rem !important; line-height: 1.1 !important; }
    .hero-meet { font-size: 4.5rem !important; margin-bottom: 25px !important;}
    .hero-academy-name { font-size: 1rem !important; padding-left: 20px !important; margin-bottom: 25px !important; }
    .hero-desc, .hero-brief { font-size: 1.4rem !important; max-width: 800px !important; line-height: 1.8 !important; }
}

/* Remove Marquee Dark Gradients so it's fully visible */
.hero-stats-scroll::before, .hero-stats-scroll::after { display: none !important; }
.hero-stats-scroll { max-width: 100% !important; margin-top: 40px !important; overflow: visible !important; }
.hs-pill { padding: 12px 24px !important; font-size: 1rem !important; background: rgba(255,255,255,0.1) !important; border: 1px solid rgba(201,149,26,0.5) !important; box-shadow: 0 5px 15px rgba(0,0,0,0.3) !important; }
.hs-pill strong { font-size: 1.1rem !important; color: var(--gold) !important; }

/* ==== PREMIUM RIGHT SIDE BUTTONS ==== */
.side-btns { gap: 15px !important; }
.side-btn {
    padding: 18px 25px !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    border-radius: 12px 0 0 12px !important;
    box-shadow: -5px 5px 20px rgba(0,0,0,0.4) !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
}
.side-btn i { font-size: 1.4rem !important; }
.side-btn:hover { transform: translateX(-10px) !important; padding-right: 35px !important; }

.sb-wa { background: linear-gradient(135deg, #25D366, #128C7E) !important; color: white !important; border-left: 3px solid #fff !important; }
.sb-call { background: linear-gradient(135deg, var(--gold-l), var(--gold-h)) !important; color: #111 !important; border-left: 3px solid #111 !important; }
.sb-enq { background: linear-gradient(135deg, #e52d27, #b31217) !important; color: white !important; border-left: 3px solid #fff !important; }
"""

css = css + "\n" + hero_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Hero and Side Buttons Fixed!")
