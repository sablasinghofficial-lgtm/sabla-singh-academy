import glob
import re

nav_old = '''<a href="index.html" class="nav-brand">
  <img src="logo.png" alt="Logo">
  <div class="brand-text">
    <span class="brand-name">Sabla Singh</span>
    <span class="brand-sub">Academy</span>
  </div>
</a>'''
nav_new = '<a href="index.html" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>'

mob_old = '''<div class="mob-logo-container">
    <img src="logo.png" alt="Logo">
    <div class="brand-text">
      <span class="brand-name">Sabla Singh</span>
      <span class="brand-sub">Academy</span>
    </div>
  </div>'''
mob_new = '<img src="logo.png" alt="Logo">'

ft_old = '''<div class="ft-logo-container">
    <img src="logo.png" alt="Logo">
    <div class="brand-text">
      <span class="brand-name">Sabla Singh</span>
      <span class="brand-sub">Academy</span>
    </div>
  </div>'''
ft_new = '<img src="logo.png" alt="Sabla Singh Academy">'

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace(nav_old, nav_new)
    
    # Check for active nav state
    active_nav = nav_old.replace('href="index.html"', 'href="index.html" class="active"')
    active_nav_new = '<a href="index.html" class="nav-brand"><img src="logo.png" alt="Sabla Singh Academy"></a>'
    html = html.replace(active_nav, active_nav_new)

    html = html.replace(mob_old, mob_new)
    html = html.replace(ft_old, ft_new)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()
if '/* --- BRAND LOGO TEXT --- */' in css:
    css = css.split('/* --- BRAND LOGO TEXT --- */')[0]
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)

print("Undo HTML/CSS done")
