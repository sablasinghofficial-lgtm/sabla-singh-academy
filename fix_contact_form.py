# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

contact_sizing_css = """
/* =========================================================
   9. Contact Form & Info Section (Query Section Fix)
========================================================= */
/* Contact Left Panel */
.contact-info h2 { font-size: 3.2rem !important; margin-bottom: 20px !important; }
.contact-info > p { font-size: 1.25rem !important; line-height: 1.8 !important; margin-bottom: 40px !important; }

.c-item { gap: 20px !important; margin-bottom: 30px !important; }
.c-icon { width: 56px !important; height: 56px !important; }
.c-icon i { font-size: 1.4rem !important; }

.c-detail h4 { font-size: 1.3rem !important; margin-bottom: 5px !important; }
.c-detail p, .c-detail a { font-size: 1.1rem !important; line-height: 1.6 !important; }

.c-socials { gap: 15px !important; margin-top: 35px !important; }
.c-socials a { width: 48px !important; height: 48px !important; font-size: 1.2rem !important; }

/* Contact Right Panel (The Form) */
.contact-form { padding: 45px !important; }
.contact-form h3 { font-size: 2.2rem !important; margin-bottom: 30px !important; }

.form-group { margin-bottom: 22px !important; }
.form-group label { font-size: 0.95rem !important; margin-bottom: 8px !important; letter-spacing: 1.5px !important; }
.form-group input, .form-group select, .form-group textarea { 
    font-size: 1.1rem !important; 
    padding: 16px 20px !important; 
}
.form-group textarea { min-height: 130px !important; }

.form-submit { 
    font-size: 1.15rem !important; 
    padding: 18px !important; 
    margin-top: 10px !important;
}
"""

css = css + "\n" + contact_sizing_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Contact form sizing fixed!")
