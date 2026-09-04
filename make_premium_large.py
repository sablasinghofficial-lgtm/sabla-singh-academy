# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

large_premium_css = """
/* ==== ULTIMATE PREMIUM & LARGE SIZING ==== */
/* Topbar - Phone, Email, Address, Socials */
.tb-left a, .tb-left span, .tb-right span, .tb-right a { 
    font-size: 1.05rem !important; 
    font-weight: 600 !important;
}
.tb-right a { 
    width: 32px !important; 
    height: 32px !important; 
    font-size: 1.1rem !important;
}
.tb-left i { font-size: 1.1rem !important; }

/* Navbar Container */
.navbar .container { 
    min-height: 115px !important; 
}

/* Logo & Brand Name */
.nav-brand { gap: 18px !important; }
.nav-brand img { 
    height: 90px !important; 
    min-width: 90px !important; 
}
.brand-title { 
    font-size: 2.6rem !important; 
    margin-bottom: 2px !important; 
}
.brand-sub { 
    font-size: 0.85rem !important; 
    letter-spacing: 6px !important; 
    font-weight: 800 !important; 
}

/* Navbar Links */
.nav-links { gap: 35px !important; }
.nav-links > a, .dd > a { 
    font-size: 1.05rem !important; 
    letter-spacing: 2px !important; 
    font-weight: 700 !important; 
}

/* Book Appointment Button */
.nav-book { 
    padding: 16px 32px !important; 
    font-size: 1rem !important; 
    letter-spacing: 1.5px !important;
}
"""

css = css + "\n" + large_premium_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Premium and Large sizing applied!")
