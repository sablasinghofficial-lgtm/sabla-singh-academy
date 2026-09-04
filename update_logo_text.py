import glob

# HTML chunks to replace
nav_old = '<a href="index.html" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>'
nav_new = '''<a href="index.html" class="nav-brand">
  <img src="logo.png" alt="Logo">
  <div class="brand-text">
    <span class="brand-name">Sabla Singh</span>
    <span class="brand-sub">Academy</span>
  </div>
</a>'''

mob_old = '<img src="logo.png" alt="Logo">'
mob_new = '''<div class="mob-logo-container">
    <img src="logo.png" alt="Logo">
    <div class="brand-text">
      <span class="brand-name">Sabla Singh</span>
      <span class="brand-sub">Academy</span>
    </div>
  </div>'''

ft_old = '<img src="logo.png" alt="Sabla Singh Academy">'
ft_new = '''<div class="ft-logo-container">
    <img src="logo.png" alt="Logo">
    <div class="brand-text">
      <span class="brand-name">Sabla Singh</span>
      <span class="brand-sub">Academy</span>
    </div>
  </div>'''

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Nav brand
    if nav_old in html:
        html = html.replace(nav_old, nav_new)
    else:
        # Fallback if it had active class or slightly different spacing
        import re
        html = re.sub(r'<a href="index\.html" class="nav-brand[^>]*><img src="logo\.png"[^>]*></a>', nav_new, html)

    # Mobile menu logo
    html = html.replace('<div class="mob-menu" id="mobMenu">\n  <img src="logo.png" alt="Logo">', '<div class="mob-menu" id="mobMenu">\n  ' + mob_new)

    # Footer logo
    # Find the footer brand section
    html = html.replace('<div class="ft-brand">\n      <img src="logo.png" alt="Sabla Singh Academy">', '<div class="ft-brand">\n      ' + ft_new)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {file}")

# Update CSS
new_css = '''
/* --- BRAND LOGO TEXT --- */
.nav-brand { display: flex; align-items: center; gap: 10px; text-decoration: none !important; }
.nav-brand img { height: 48px !important; width: auto; border-radius: 50%; box-shadow: 0 0 10px rgba(201,149,26,0.2); }
.brand-text { display: flex; flex-direction: column; justify-content: center; }
.brand-name { font-family: var(--hd); font-size: 1.35rem; font-weight: 700; color: var(--gold); line-height: 1; letter-spacing: 1px; margin-bottom: 2px; }
.brand-sub { font-family: var(--bd); font-size: 0.55rem; font-weight: 600; color: var(--white); text-transform: uppercase; letter-spacing: 4.5px; opacity: 0.8; }

.ft-logo-container { display: flex; align-items: center; gap: 12px; margin-bottom: 18px; }
.ft-logo-container img { height: 55px; width: auto; border-radius: 50%; box-shadow: 0 0 15px rgba(201,149,26,0.3); }

.mob-logo-container { display: flex; align-items: center; gap: 12px; margin-bottom: 25px; }
.mob-logo-container img { height: 55px; width: auto; border-radius: 50%; box-shadow: 0 0 15px rgba(201,149,26,0.3); }
'''

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()
if '/* --- BRAND LOGO TEXT --- */' not in css:
    css += new_css
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated style.css")
