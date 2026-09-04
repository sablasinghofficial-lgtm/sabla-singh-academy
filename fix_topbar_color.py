# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

topbar_fix_css = """
/* ==== TOPBAR NEW YELLOW GOLD COLOR ==== */
.topbar { 
    background: #F5C71A !important; /* The bright yellow/gold from the image */
    box-shadow: 0 4px 15px rgba(245, 199, 26, 0.2) !important; 
    padding: 10px 0 !important;
}
.tb-left a, .tb-left span, .tb-right span {
    color: #000000 !important; /* Pitch black for premium contrast against bright yellow */
}
.tb-left i {
    color: #000000 !important;
    opacity: 0.8 !important;
}
.tb-right a {
    background: #000000 !important;
    color: #F5C71A !important;
}
.tb-right a:hover {
    background: #222222 !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
}
"""

css = css + "\n" + topbar_fix_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Topbar color fixed!")
