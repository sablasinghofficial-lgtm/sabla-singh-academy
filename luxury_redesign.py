# -*- coding: utf-8 -*-

luxury_css = """
/* =================================================================
   LUXURY EDITORIAL THEME - CONTACT, CTA, FOOTER
   Palette: Ivory + Warm Cream + Champagne Gold + Burgundy accents
   NO DARK BACKGROUNDS - Premium Beauty Academy Look
================================================================= */

/* Google Font Import for Cormorant Garamond */
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

/* ---- CONTACT SECTION ---- */
.contact {
    background: linear-gradient(135deg, #FFFDF8 0%, #FBF3E7 40%, #F5ECD8 100%) !important;
    padding: 110px 0 !important;
    position: relative !important;
    overflow: hidden !important;
}

/* Bokeh gold orbs in background */
.contact::before {
    content: '' !important;
    position: absolute !important;
    top: -120px !important; right: -80px !important;
    width: 550px !important; height: 550px !important;
    background: radial-gradient(circle, rgba(201,162,75,0.13) 0%, transparent 70%) !important;
    filter: blur(60px) !important;
    pointer-events: none !important;
    z-index: 0 !important;
    animation: bokehFloat1 8s ease-in-out infinite !important;
}
.contact::after {
    content: '' !important;
    position: absolute !important;
    bottom: -100px !important; left: -60px !important;
    width: 400px !important; height: 400px !important;
    background: radial-gradient(circle, rgba(232,200,116,0.1) 0%, transparent 70%) !important;
    filter: blur(50px) !important;
    pointer-events: none !important;
    z-index: 0 !important;
    animation: bokehFloat2 10s ease-in-out infinite !important;
}
@keyframes bokehFloat1 { 0%,100%{transform:translate(0,0)} 50%{transform:translate(-20px,20px)} }
@keyframes bokehFloat2 { 0%,100%{transform:translate(0,0)} 50%{transform:translate(20px,-20px)} }

.contact .container { position: relative !important; z-index: 1 !important; }

.contact-grid {
    display: grid !important;
    grid-template-columns: 1fr 1.5fr !important;
    gap: 70px !important;
    align-items: start !important;
}

/* Left Info */
.contact-info h2 {
    font-family: 'Playfair Display', 'Cormorant Garamond', Georgia, serif !important;
    font-size: 4rem !important;
    font-weight: 700 !important;
    color: #3A2E24 !important;
    line-height: 1.1 !important;
    margin-bottom: 18px !important;
}
.contact-info h2 span {
    font-style: italic !important;
    background: linear-gradient(135deg, #C9A24B, #E8C874, #C9A24B) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
    background-clip: text !important;
}
.contact-info > p {
    font-size: 1.15rem !important;
    color: #8a7566 !important;
    line-height: 1.8 !important;
    margin-bottom: 45px !important;
    font-family: 'Poppins', sans-serif !important;
}

/* Info Cards - Glassmorphism */
.c-item {
    display: flex !important;
    gap: 20px !important;
    align-items: center !important;
    margin-bottom: 18px !important;
    padding: 22px 24px !important;
    background: rgba(255,253,248,0.78) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border-radius: 20px !important;
    border: 1px solid rgba(201,162,75,0.22) !important;
    box-shadow:
        0 20px 60px rgba(200,160,80,0.1),
        0 2px 8px rgba(0,0,0,0.04) !important;
    transition: all 0.4s cubic-bezier(0.175,0.885,0.32,1.275) !important;
    cursor: default !important;
}
.c-item:hover {
    transform: translateY(-8px) !important;
    box-shadow:
        0 30px 80px rgba(201,162,75,0.22),
        0 4px 15px rgba(0,0,0,0.06),
        0 0 0 1px rgba(201,162,75,0.4) !important;
    background: rgba(255,253,248,0.95) !important;
}

/* Embossed Gold Icon Badge */
.c-icon {
    width: 58px !important; height: 58px !important;
    border-radius: 50% !important;
    background: linear-gradient(145deg, #E8C874, #C9A24B) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
    box-shadow:
        4px 4px 10px rgba(150,100,30,0.35),
        -3px -3px 8px rgba(255,245,200,0.7),
        inset 0 2px 4px rgba(255,250,220,0.5),
        inset 0 -2px 4px rgba(150,100,30,0.3) !important;
}
.c-icon i { color: #3A2E24 !important; font-size: 1.3rem !important; }

.c-detail h4 {
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    color: #3A2E24 !important;
    margin-bottom: 4px !important;
    letter-spacing: 0.5px !important;
}
.c-detail p { font-size: 1rem !important; color: #8a7566 !important; line-height: 1.5 !important; }
.c-detail a { color: #8a7566 !important; text-decoration: none !important; }
.c-detail a:hover { color: #C9A24B !important; }

/* Social Links */
.c-socials { display: flex !important; gap: 14px !important; margin-top: 35px !important; }
.c-socials a {
    width: 50px !important; height: 50px !important;
    border-radius: 50% !important;
    background: rgba(255,253,248,0.9) !important;
    border: 1.5px solid rgba(201,162,75,0.3) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: #8a7566 !important;
    font-size: 1.1rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(201,162,75,0.15), inset 0 1px 2px rgba(255,255,255,0.9) !important;
    text-decoration: none !important;
}
.c-socials a:hover {
    background: linear-gradient(135deg, #C9A24B, #E8C874) !important;
    border-color: #C9A24B !important;
    color: #3A2E24 !important;
    transform: translateY(-4px) !important;
    box-shadow: 0 12px 25px rgba(201,162,75,0.4) !important;
}

/* Right Form Card */
.contact-form {
    background: rgba(255,253,248,0.85) !important;
    backdrop-filter: blur(30px) !important;
    -webkit-backdrop-filter: blur(30px) !important;
    border-radius: 28px !important;
    padding: 52px !important;
    border: 1px solid rgba(201,162,75,0.2) !important;
    box-shadow:
        0 30px 80px rgba(200,160,80,0.14),
        0 4px 20px rgba(0,0,0,0.05),
        inset 0 1px 0 rgba(255,255,255,0.95) !important;
    position: relative !important;
    overflow: hidden !important;
}
/* Gold foil shimmer top strip */
.contact-form::before {
    content: '' !important;
    position: absolute !important;
    top: 0 !important; left: 0 !important; right: 0 !important;
    height: 4px !important;
    background: linear-gradient(90deg, transparent 0%, #C9A24B 20%, #F0D788 50%, #C9A24B 80%, transparent 100%) !important;
    border-radius: 28px 28px 0 0 !important;
}

.contact-form h3 {
    font-family: 'Cormorant Garamond', 'Playfair Display', Georgia, serif !important;
    font-size: 2.2rem !important;
    font-weight: 700 !important;
    color: #3A2E24 !important;
    margin-bottom: 35px !important;
    padding-bottom: 22px !important;
    border-bottom: 1px solid rgba(201,162,75,0.2) !important;
    letter-spacing: 0.5px !important;
}

.form-group { margin-bottom: 20px !important; }
.form-group label {
    font-size: 0.78rem !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    color: #8a7566 !important;
    margin-bottom: 8px !important;
    display: block !important;
    font-family: 'Poppins', sans-serif !important;
}
.form-group input,
.form-group select,
.form-group textarea {
    width: 100% !important;
    background: #FBF3E7 !important;
    border: 1.5px solid rgba(201,162,75,0.2) !important;
    border-radius: 16px !important;
    padding: 16px 20px !important;
    font-size: 1.05rem !important;
    color: #3A2E24 !important;
    transition: all 0.3s ease !important;
    outline: none !important;
    font-family: 'Poppins', sans-serif !important;
    box-shadow: inset 0 2px 6px rgba(0,0,0,0.04) !important;
}
.form-group input::placeholder,
.form-group textarea::placeholder { color: #bfb0a0 !important; }
.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    background: #FFFDF8 !important;
    border-color: #C9A24B !important;
    box-shadow:
        0 0 0 4px rgba(201,162,75,0.15),
        inset 0 2px 6px rgba(0,0,0,0.02) !important;
}
.form-group select { color: #8a7566 !important; }
.form-group textarea { min-height: 140px !important; resize: vertical !important; }

/* Submit Button - Raised Gold Pill */
.form-submit {
    width: 100% !important;
    background: linear-gradient(135deg, #C9A24B 0%, #E8C874 50%, #C9A24B 100%) !important;
    background-size: 200% 100% !important;
    color: #3A2E24 !important;
    font-size: 1.05rem !important;
    font-weight: 800 !important;
    letter-spacing: 3px !important;
    text-transform: uppercase !important;
    padding: 18px !important;
    border-radius: 50px !important;
    border: none !important;
    margin-top: 10px !important;
    cursor: pointer !important;
    font-family: 'Poppins', sans-serif !important;
    box-shadow:
        0 8px 25px rgba(201,162,75,0.4),
        0 4px 0 #a07a28,
        inset 0 1px 0 rgba(255,255,255,0.5) !important;
    transition: all 0.35s ease !important;
    position: relative !important;
    overflow: hidden !important;
}
.form-submit::after {
    content: '' !important;
    position: absolute !important;
    top: 0 !important; left: -100% !important;
    width: 60% !important; height: 100% !important;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.35), transparent) !important;
    transform: skewX(-20deg) !important;
    transition: left 0.6s ease !important;
}
.form-submit:hover {
    background-position: 100% 0 !important;
    transform: translateY(-2px) scale(1.02) !important;
    box-shadow:
        0 15px 40px rgba(201,162,75,0.5),
        0 4px 0 #a07a28,
        inset 0 1px 0 rgba(255,255,255,0.5) !important;
}
.form-submit:hover::after { left: 140% !important; }

/* ---- CTA BANNER ---- */
.cta {
    background: linear-gradient(135deg, #F3E6CE 0%, #EDD5A0 35%, #F3E6CE 70%, #FBF3E7 100%) !important;
    padding: 90px 0 !important;
    position: relative !important;
    overflow: hidden !important;
    border: none !important;
    border-top: 2px solid rgba(201,162,75,0.3) !important;
}
.cta::before {
    content: '' !important;
    position: absolute !important;
    inset: 0 !important;
    background: 
        radial-gradient(circle at 20% 50%, rgba(201,162,75,0.15) 0%, transparent 50%),
        radial-gradient(circle at 80% 50%, rgba(232,200,116,0.1) 0%, transparent 50%) !important;
    pointer-events: none !important;
}
.cta .container {
    position: relative !important;
    z-index: 1 !important;
    display: flex !important;
    align-items: center !important;
    gap: 50px !important;
    flex-wrap: wrap !important;
}
.cta-left h2 {
    font-family: 'Playfair Display', 'Cormorant Garamond', Georgia, serif !important;
    font-size: 3.2rem !important;
    font-weight: 700 !important;
    color: #3A2E24 !important;
    line-height: 1.25 !important;
    text-shadow: 0 4px 15px rgba(150,100,30,0.12), 0 1px 3px rgba(0,0,0,0.08) !important;
}
.cta-mid {
    font-size: 1.15rem !important;
    color: #6B5540 !important;
    line-height: 1.8 !important;
    flex: 1 !important;
    min-width: 220px !important;
}
.cta-btns { display: flex !important; gap: 18px !important; flex-wrap: wrap !important; align-items: center !important; }
.cta-btn-gold {
    background: linear-gradient(135deg, #C9A24B, #E8C874, #C9A24B) !important;
    color: #3A2E24 !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    padding: 18px 38px !important;
    border-radius: 50px !important;
    border: none !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    box-shadow:
        0 10px 30px rgba(201,162,75,0.45),
        0 4px 0 #a07a28,
        inset 0 1px 0 rgba(255,255,255,0.5) !important;
    transition: all 0.3s ease !important;
    text-decoration: none !important;
    display: inline-block !important;
}
.cta-btn-gold:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 18px 45px rgba(201,162,75,0.55), 0 4px 0 #a07a28 !important;
}
.cta-btn-outline {
    background: rgba(255,253,248,0.7) !important;
    backdrop-filter: blur(10px) !important;
    color: #3A2E24 !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    padding: 16px 36px !important;
    border-radius: 50px !important;
    border: 2px solid #C9A24B !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
    transition: all 0.3s ease !important;
    text-decoration: none !important;
    display: inline-block !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.06) !important;
}
.cta-btn-outline:hover {
    background: linear-gradient(135deg, #C9A24B, #E8C874) !important;
    color: #3A2E24 !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 12px 30px rgba(201,162,75,0.4) !important;
}

/* ---- FOOTER ---- */
.footer {
    background: #FBF3E7 !important;
    padding: 80px 0 0 !important;
    position: relative !important;
    color: #3A2E24 !important;
}
/* Subtle grain texture overlay */
.footer::before {
    content: '' !important;
    position: absolute !important;
    inset: 0 !important;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E") !important;
    pointer-events: none !important;
    opacity: 0.4 !important;
    z-index: 0 !important;
}
.footer .container { position: relative !important; z-index: 1 !important; }

/* Footer grid */
.ft-grid {
    display: grid !important;
    grid-template-columns: 1.4fr 1fr 1fr 1.2fr !important;
    gap: 50px !important;
    padding-bottom: 60px !important;
    border-bottom: 1px solid rgba(201,162,75,0.25) !important;
}
.footer h4 {
    font-family: 'Cormorant Garamond', 'Playfair Display', Georgia, serif !important;
    font-style: italic !important;
    font-size: 1.5rem !important;
    font-weight: 700 !important;
    color: #C9A24B !important;
    margin-bottom: 25px !important;
    position: relative !important;
    padding-bottom: 15px !important;
}
.footer h4::after {
    content: '' !important;
    position: absolute !important;
    bottom: 0 !important; left: 0 !important;
    width: 40px !important; height: 2px !important;
    background: linear-gradient(90deg, #C9A24B, transparent) !important;
}
.footer ul { list-style: none !important; padding: 0 !important; margin: 0 !important; }
.footer ul li { margin-bottom: 12px !important; }
.footer ul li a {
    color: #7a6555 !important;
    font-size: 1.05rem !important;
    text-decoration: none !important;
    transition: all 0.3s ease !important;
    display: inline-block !important;
    position: relative !important;
}
.footer ul li a::after {
    content: '' !important;
    position: absolute !important;
    bottom: -2px !important; left: 0 !important;
    width: 0 !important; height: 1px !important;
    background: #C9A24B !important;
    transition: width 0.3s ease !important;
}
.footer ul li a:hover { color: #C9A24B !important; transform: translateX(5px) !important; }
.footer ul li a:hover::after { width: 100% !important; }

/* Footer contact details */
.ft-contact p {
    display: flex !important;
    align-items: flex-start !important;
    gap: 12px !important;
    color: #7a6555 !important;
    font-size: 1.05rem !important;
    margin-bottom: 14px !important;
    line-height: 1.6 !important;
}
.ft-contact i { color: #C9A24B !important; font-size: 1rem !important; margin-top: 3px !important; flex-shrink: 0 !important; }
.ft-brand > p { color: #8a7566 !important; font-size: 1.05rem !important; line-height: 1.7 !important; margin: 15px 0 25px !important; }

/* Footer social badges - embossed gold */
.ft-socials { display: flex !important; gap: 12px !important; margin-top: 20px !important; }
.ft-socials a {
    width: 42px !important; height: 42px !important;
    border-radius: 50% !important;
    background: linear-gradient(145deg, #E8C874, #C9A24B) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    color: #3A2E24 !important;
    font-size: 0.95rem !important;
    text-decoration: none !important;
    box-shadow:
        3px 3px 8px rgba(150,100,30,0.3),
        -2px -2px 6px rgba(255,245,200,0.7),
        inset 0 1px 3px rgba(255,250,220,0.5) !important;
    transition: all 0.3s ease !important;
}
.ft-socials a:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 10px 20px rgba(201,162,75,0.45) !important;
}

/* Footer logo */
.ft-brand img { height: 70px !important; }

/* Footer Bottom Bar */
.ft-bottom {
    background: #3A2E24 !important;
    padding: 22px 0 !important;
    margin-top: 0 !important;
    position: relative !important;
    z-index: 1 !important;
}
.ft-bottom .container {
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    flex-wrap: wrap !important;
    gap: 10px !important;
}
.ft-bottom p { color: #c9a24b !important; font-size: 0.95rem !important; }
.ft-bottom strong { color: #E8C874 !important; }

"""

with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

css = css + "\n" + luxury_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Luxury redesign CSS applied!")
