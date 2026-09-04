import glob
import re

old_text = '<p>&copy; 2026 <a href="#">Sabla Singh Academy</a>. All Rights Reserved.</p>'
# Alternatively, I can use regex to match the exact paragraph since it might have been modified slightly in some files

new_text = '<p>&copy; 2026 Sabla Singh Academy. All Rights Reserved.<br>Designed & Developed by <a href="https://techup-digital.web.app" target="_blank" style="color:var(--gold); text-decoration:none; font-weight:700; letter-spacing:1px;">TechUp</a></p>'

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # We can use regex to replace the copyright paragraph
    # The paragraph is inside <div class="ft-bottom">
    html = re.sub(
        r'<p>&copy; 2026.*?All Rights Reserved\.</p>',
        new_text,
        html
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Updated {file}")
