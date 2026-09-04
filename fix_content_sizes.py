# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# I will append a comprehensive sizing override block to fix the root cause.
content_sizing_css = """
/* =========================================================
   ROOT CAUSE FIX: GLOBAL CONTENT SIZING OVERRIDES
   Problem: Original base design used 0.7rem to 0.85rem for content which is tiny on wide screens.
   Solution: Upscale paragraphs, dropdowns, card texts, and headings to modern readable standards (1rem - 1.2rem+).
========================================================= */

/* 1. Navbar Dropdowns */
.dd-menu { 
    min-width: 240px !important; 
    padding: 10px 0 !important;
}
.dd-menu a { 
    font-size: 1.05rem !important; 
    padding: 12px 24px !important; 
    font-weight: 500 !important;
    letter-spacing: 0.5px !important;
}

/* 2. Section Titles & Descriptions */
.sec-title h2, .sec-header h2 { 
    font-size: 3.2rem !important; 
}
.sec-title p { 
    font-size: 1.2rem !important; 
    max-width: 800px !important; 
    line-height: 1.8 !important; 
}

/* 3. About Section Texts */
.about-p { 
    font-size: 1.15rem !important; 
    line-height: 1.8 !important; 
}
.about-features li { 
    font-size: 1.1rem !important; 
    padding: 12px 0 !important;
}
.about-features li i { 
    font-size: 1.2rem !important; 
}

/* 4. Service Cards */
.srv-card h3 { 
    font-size: 1.4rem !important; 
    margin-bottom: 12px !important;
}
.srv-card p { 
    font-size: 1.05rem !important; 
    line-height: 1.6 !important;
}

/* 5. Course Cards */
.crs-card-body { 
    padding: 25px !important; 
}
.crs-card-body h4 { 
    font-size: 1.4rem !important; 
    margin-bottom: 10px !important;
}
.crs-card-body .meta, .crs-card-body .dur { 
    font-size: 1rem !important; 
    margin-bottom: 8px !important;
}
.crs-btn { 
    font-size: 1.05rem !important; 
    padding: 14px !important; 
    margin-top: 15px !important;
}

/* 6. Vlog Cards & Premium Elements */
.vg-body h3 { 
    font-size: 1.4rem !important; 
    margin-bottom: 20px !important;
}
.vg-btn { 
    font-size: 0.95rem !important; 
    padding: 14px 20px !important; 
}

/* 7. Call To Action (CTA) Section */
.cta { padding: 80px 0 !important; }
.cta-left h2 { 
    font-size: 3.2rem !important; 
    line-height: 1.3 !important;
}
.cta-mid { 
    font-size: 1.2rem !important; 
    max-width: 450px !important; 
    line-height: 1.8 !important; 
}
.cta-btn { 
    font-size: 1.05rem !important; 
    padding: 18px 32px !important; 
}

/* 8. Footer */
.footer { padding: 70px 0 20px !important; }
.ft-brand p, .ft-contact p { 
    font-size: 1.1rem !important; 
    line-height: 1.8 !important;
}
.footer h4 { 
    font-size: 1.5rem !important; 
    margin-bottom: 25px !important;
}
.footer ul li a { 
    font-size: 1.1rem !important; 
    padding: 8px 0 !important;
}
.ft-bottom p { 
    font-size: 1.05rem !important; 
}
"""

css = css + "\n" + content_sizing_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Comprehensive content sizing fix applied!")
