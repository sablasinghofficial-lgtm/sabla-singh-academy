# -*- coding: utf-8 -*-
import glob
import re

# 1. Fix duplicate class attributes in HTML files (like class="active" class="side-btn sb-enq")
for html_file in glob.glob("*.html"):
    with open(html_file, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()
    
    # Fix double class attributes
    fixed_html = re.sub(r'class="active"\s+class="side-btn sb-enq"', r'class="side-btn sb-enq active"', html)
    fixed_html = re.sub(r'class="active"\s+class="([^"]+)"', r'class="\1 active"', fixed_html)
    
    if fixed_html != html:
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(fixed_html)
        print(f"Fixed double class in {html_file}")

# 2. Fix the CSS for the side buttons to ensure they are universally premium and visible
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# Add a guaranteed override at the very bottom for all side buttons
premium_side_btns = """
/* =========================================================
   GUARANTEED PREMIUM SIDE BUTTONS OVERRIDE
========================================================= */
.side-btns { gap: 15px !important; z-index: 9999 !important; }

.side-btn {
    padding: 18px 25px !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    border-radius: 12px 0 0 12px !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
    box-shadow: -5px 5px 20px rgba(0,0,0,0.5) !important;
    border-right: none !important;
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    text-decoration: none !important;
    transition: all 0.3s ease !important;
}

.side-btn i { font-size: 1.4rem !important; }
.side-btn:hover { transform: translateX(-10px) !important; padding-right: 35px !important; }

.sb-wa { 
    background: linear-gradient(135deg, #25D366, #128C7E) !important; 
    color: white !important; 
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-left: 3px solid #fff !important; 
}
.sb-call { 
    background: linear-gradient(135deg, var(--gold), #D4A911) !important; 
    color: #000000 !important; 
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-left: 3px solid #000 !important; 
}
.sb-enq { 
    background: linear-gradient(135deg, #e52d27, #b31217) !important; /* Premium Red/Crimson */
    color: white !important; 
    border: 1px solid rgba(255,255,255,0.2) !important;
    border-left: 3px solid #fff !important; 
}

/* Hover effects */
.sb-wa:hover { box-shadow: -5px 5px 25px rgba(37,211,102,0.6) !important; }
.sb-call:hover { box-shadow: -5px 5px 25px rgba(245, 199, 26, 0.6) !important; }
.sb-enq:hover { box-shadow: -5px 5px 25px rgba(229, 45, 39, 0.6) !important; }
"""

css = css + "\n" + premium_side_btns

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Side buttons universally fixed!")
