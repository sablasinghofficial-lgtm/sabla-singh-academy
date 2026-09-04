# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

upgrade_css = """
/* =========================================================
   CONTACT + FOOTER MEGA UPGRADE v2
========================================================= */

/* ---- CONTACT: BIGGER + BOLDER ---- */
.contact { padding: 130px 0 !important; }

.contact-info h2 {
    font-size: 5rem !important;
    font-weight: 700 !important;
    margin-bottom: 20px !important;
}
.contact-info > p {
    font-size: 1.35rem !important;
    font-weight: 500 !important;
    margin-bottom: 50px !important;
    color: #7a6555 !important;
}

/* Info Cards: bigger padding, bolder text */
.c-item { padding: 28px 30px !important; margin-bottom: 22px !important; border-radius: 24px !important; }
.c-icon { width: 68px !important; height: 68px !important; }
.c-icon i { font-size: 1.6rem !important; }
.c-detail h4 { font-size: 1.3rem !important; font-weight: 800 !important; margin-bottom: 6px !important; }
.c-detail p { font-size: 1.1rem !important; font-weight: 500 !important; }
.c-detail a { font-size: 1.1rem !important; font-weight: 500 !important; }

/* Social icons bigger */
.c-socials a { width: 56px !important; height: 56px !important; font-size: 1.25rem !important; }

/* Form heading bigger */
.contact-form h3 {
    font-size: 2.8rem !important;
    font-weight: 700 !important;
    margin-bottom: 40px !important;
}
.contact-form { padding: 60px !important; border-radius: 32px !important; }
.form-group label { font-size: 0.9rem !important; letter-spacing: 2.5px !important; }
.form-group input, .form-group select, .form-group textarea {
    font-size: 1.15rem !important;
    padding: 18px 22px !important;
    border-radius: 18px !important;
}
.form-submit {
    font-size: 1.2rem !important;
    letter-spacing: 3.5px !important;
    padding: 22px !important;
}

/* =========================================================
   FOOTER: VIBRANT LUXURY REDESIGN - Colourful & Premium
========================================================= */
.footer {
    background: linear-gradient(135deg, #1C1009 0%, #2E1A0A 40%, #1C1009 100%) !important;
    padding: 0 !important;
    position: relative !important;
    color: #F8F0E3 !important;
    overflow: hidden !important;
}

/* Rich gold bokeh orbs */
.footer::before {
    content: '' !important;
    position: absolute !important;
    top: -150px !important; right: -100px !important;
    width: 600px !important; height: 600px !important;
    background: radial-gradient(circle, rgba(201,162,75,0.18) 0%, transparent 65%) !important;
    pointer-events: none !important; z-index: 0 !important;
}
.footer::after {
    content: '' !important;
    position: absolute !important;
    bottom: 0 !important; left: -80px !important;
    width: 400px !important; height: 400px !important;
    background: radial-gradient(circle, rgba(139,46,60,0.15) 0%, transparent 65%) !important;
    pointer-events: none !important; z-index: 0 !important;
}

/* Gold divider strip at top of footer */
.footer > .container::before {
    content: '' !important;
    display: block !important;
    height: 4px !important;
    background: linear-gradient(90deg, transparent, #C9A24B, #F0D788, #C9A24B, transparent) !important;
    margin-bottom: 70px !important;
    border-radius: 4px !important;
}

.footer .container { position: relative !important; z-index: 1 !important; padding-top: 70px !important; }

.ft-grid {
    display: grid !important;
    grid-template-columns: 1.5fr 1fr 1.2fr 1.3fr !important;
    gap: 50px !important;
    padding-bottom: 60px !important;
    border-bottom: 1px solid rgba(201,162,75,0.2) !important;
    align-items: start !important;
}

/* Column Headings - Colourful serif gold italic */
.footer h4 {
    font-family: 'Cormorant Garamond', 'Playfair Display', Georgia, serif !important;
    font-style: italic !important;
    font-size: 1.8rem !important;
    font-weight: 700 !important;
    background: linear-gradient(135deg, #E8C874, #C9A24B, #F0D788) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
    margin-bottom: 28px !important;
    padding-bottom: 16px !important;
    border-bottom: 1px solid rgba(201,162,75,0.2) !important;
}
.footer h4::after { display: none !important; }

/* Footer Brand column */
.ft-brand > p {
    color: #C4A882 !important;
    font-size: 1.1rem !important;
    line-height: 1.8 !important;
    margin: 20px 0 30px !important;
    font-weight: 400 !important;
}

/* Footer Links */
.footer ul li a {
    color: #C4A882 !important;
    font-size: 1.1rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px !important;
    padding: 4px 0 !important;
}
.footer ul li a:hover { color: #F0D788 !important; transform: translateX(8px) !important; }
.footer ul li a::after { background: #E8C874 !important; }
.footer ul li { margin-bottom: 16px !important; }

/* Footer Contact items */
.ft-contact p {
    color: #C4A882 !important;
    font-size: 1.05rem !important;
    font-weight: 500 !important;
    margin-bottom: 18px !important;
    line-height: 1.7 !important;
    display: flex !important;
    gap: 12px !important;
    align-items: flex-start !important;
}
.ft-contact i { color: #C9A24B !important; font-size: 1.1rem !important; margin-top: 3px !important; }

/* Social Icons — Vibrant colour each */
.ft-socials { display: flex !important; gap: 14px !important; margin-top: 10px !important; }
.ft-socials a {
    width: 46px !important; height: 46px !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 1.1rem !important;
    text-decoration: none !important;
    transition: all 0.35s ease !important;
    box-shadow: 0 6px 18px rgba(0,0,0,0.4) !important;
}
/* Individual social colours */
.ft-socials a:nth-child(1) { background: linear-gradient(135deg, #1877F2, #0D5DB8) !important; color: #fff !important; }
.ft-socials a:nth-child(2) { background: linear-gradient(135deg, #E1306C, #833AB4, #F77737) !important; color: #fff !important; }
.ft-socials a:nth-child(3) { background: linear-gradient(135deg, #FF0000, #CC0000) !important; color: #fff !important; }
.ft-socials a:nth-child(4) { background: linear-gradient(135deg, #25D366, #128C7E) !important; color: #fff !important; }
.ft-socials a:hover { transform: translateY(-6px) scale(1.1) !important; box-shadow: 0 12px 30px rgba(0,0,0,0.5) !important; }

/* Footer Bottom Bar */
.ft-bottom {
    background: linear-gradient(90deg, #0D0804, #1A0F05, #0D0804) !important;
    padding: 28px 0 !important;
    border-top: 1px solid rgba(201,162,75,0.3) !important;
}
.ft-bottom .container {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    gap: 10px !important;
    flex-wrap: wrap !important;
}
.ft-bottom p {
    color: #9A8060 !important;
    font-size: 1rem !important;
    font-weight: 400 !important;
}
.ft-bottom p a {
    color: #E8C874 !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    text-decoration: none !important;
}
.ft-bottom p a:hover { color: #fff !important; }
"""

css = css + "\n" + upgrade_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Contact & Footer mega upgrade done!")
