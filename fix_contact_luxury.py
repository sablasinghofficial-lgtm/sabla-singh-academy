# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

luxury_contact_css = """
/* =========================================================
   CONTACT PAGE - ULTRA LUXURY REDESIGN
   Theme: Soft Ivory / Warm Grey + Gold Glow (No pure black)
========================================================= */

/* 1. Overall Contact Section Background */
.contact {
    background: linear-gradient(135deg, #f8f5f0 0%, #ede9e4 40%, #f2efe9 100%) !important;
    padding: 100px 0 !important;
    position: relative !important;
    overflow: hidden !important;
}

/* Ambient golden decorative glow behind the form */
.contact::before {
    content: '' !important;
    position: absolute !important;
    top: -100px !important;
    right: -100px !important;
    width: 600px !important;
    height: 600px !important;
    background: radial-gradient(circle, rgba(245,199,26,0.12) 0%, transparent 70%) !important;
    pointer-events: none !important;
    z-index: 0 !important;
}
.contact::after {
    content: '' !important;
    position: absolute !important;
    bottom: -80px !important;
    left: -80px !important;
    width: 400px !important;
    height: 400px !important;
    background: radial-gradient(circle, rgba(245,199,26,0.08) 0%, transparent 70%) !important;
    pointer-events: none !important;
    z-index: 0 !important;
}
.contact .container { position: relative !important; z-index: 1 !important; }

/* 2. Contact Grid */
.contact-grid {
    display: grid !important;
    grid-template-columns: 1fr 1.4fr !important;
    gap: 60px !important;
    align-items: start !important;
}

/* 3. Left Info Panel */
.contact-info h2 {
    font-size: 3.5rem !important;
    font-family: var(--hd) !important;
    color: #1a1a1a !important;
    margin-bottom: 15px !important;
    line-height: 1.1 !important;
}
.contact-info h2 span {
    color: var(--gold) !important;
    font-style: italic !important;
    position: relative !important;
}
.contact-info > p {
    font-size: 1.15rem !important;
    color: #5a5a5a !important;
    line-height: 1.8 !important;
    margin-bottom: 45px !important;
}

/* Info Items */
.c-item {
    display: flex !important;
    gap: 20px !important;
    align-items: flex-start !important;
    margin-bottom: 28px !important;
    padding: 20px !important;
    background: rgba(255,255,255,0.7) !important;
    border-radius: 12px !important;
    border: 1px solid rgba(245,199,26,0.2) !important;
    backdrop-filter: blur(10px) !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06) !important;
}
.c-item:hover {
    transform: translateX(5px) !important;
    box-shadow: 0 8px 30px rgba(245,199,26,0.2), -3px 0 0 var(--gold) !important;
    background: rgba(255,255,255,0.9) !important;
}
.c-icon {
    width: 54px !important;
    height: 54px !important;
    border-radius: 50% !important;
    background: linear-gradient(135deg, var(--gold), #D4A911) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
    box-shadow: 0 6px 20px rgba(245,199,26,0.4) !important;
}
.c-icon i { color: #000000 !important; font-size: 1.3rem !important; }
.c-detail h4 { font-size: 1.15rem !important; color: #1a1a1a !important; font-weight: 700 !important; margin-bottom: 5px !important; }
.c-detail p { font-size: 1.05rem !important; color: #666 !important; line-height: 1.6 !important; }
.c-detail a { color: #555 !important; }
.c-detail a:hover { color: var(--gold) !important; }

/* Social Links */
.c-socials { display: flex !important; gap: 14px !important; margin-top: 30px !important; }
.c-socials a {
    width: 48px !important;
    height: 48px !important;
    border-radius: 50% !important;
    background: #fff !important;
    border: 2px solid rgba(245,199,26,0.3) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: #666 !important;
    font-size: 1.1rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
}
.c-socials a:hover {
    background: var(--gold) !important;
    border-color: var(--gold) !important;
    color: #000 !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 8px 20px rgba(245,199,26,0.5) !important;
}

/* 4. Right Form Panel */
.contact-form {
    background: linear-gradient(145deg, #ffffff, #fdf9f2) !important;
    border-radius: 20px !important;
    padding: 50px !important;
    border: 1px solid rgba(245,199,26,0.25) !important;
    box-shadow:
        0 20px 60px rgba(0,0,0,0.1),
        0 0 0 1px rgba(255,255,255,0.8) inset,
        0 2px 0 rgba(245,199,26,0.5) inset !important; /* Golden top edge */
    position: relative !important;
}

/* 3D Decorative gold corner line */
.contact-form::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important;
    left: 50px !important;
    right: 50px !important;
    height: 3px !important;
    background: linear-gradient(90deg, transparent, var(--gold), transparent) !important;
    border-radius: 0 0 3px 3px !important;
}

.contact-form h3 {
    font-size: 2rem !important;
    font-family: var(--hd) !important;
    color: #1a1a1a !important;
    margin-bottom: 35px !important;
    padding-bottom: 20px !important;
    border-bottom: 1px solid rgba(245,199,26,0.2) !important;
}

/* Form inputs */
.form-group label {
    color: #555 !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
}
.form-group input,
.form-group select,
.form-group textarea {
    background: #f8f8f8 !important;
    border: 1.5px solid #e8e0d0 !important;
    color: #1a1a1a !important;
    font-size: 1.05rem !important;
    padding: 15px 18px !important;
    border-radius: 10px !important;
    transition: all 0.3s ease !important;
}
.form-group input::placeholder,
.form-group textarea::placeholder { color: #aaa !important; }
.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    background: #fff !important;
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 4px rgba(245,199,26,0.15), 0 5px 15px rgba(0,0,0,0.08) !important;
    outline: none !important;
}
.form-group select { color: #777 !important; }
.form-group textarea { min-height: 130px !important; resize: vertical !important; }

/* Send Enquiry Button */
.form-submit {
    background: linear-gradient(135deg, #1a1a1a 0%, #333 100%) !important;
    color: var(--gold) !important;
    font-size: 1.1rem !important;
    font-weight: 800 !important;
    letter-spacing: 2.5px !important;
    padding: 18px !important;
    border-radius: 10px !important;
    border: 1px solid rgba(245,199,26,0.3) !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2), 0 1px 0 rgba(245,199,26,0.3) inset !important;
    transition: all 0.3s ease !important;
}
.form-submit:hover {
    background: linear-gradient(135deg, var(--gold) 0%, #D4A911 100%) !important;
    color: #000 !important;
    border-color: var(--gold) !important;
    box-shadow: 0 15px 40px rgba(245,199,26,0.4) !important;
    transform: translateY(-2px) !important;
}
"""

css = css + "\n" + luxury_contact_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Luxury contact section applied!")
