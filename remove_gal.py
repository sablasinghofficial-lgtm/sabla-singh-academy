import re

content = open('gallery.html', 'r', encoding='utf-8').read()

# Remove gal2.jpg entry
content = re.sub(r'\s*<div class="gal-item"[^>]*>\s*<img src="gal2\.jpg"[^>]*>\s*<div class="gal-overlay">.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# Remove gal3.jpg entry
content = re.sub(r'\s*<div class="gal-item"[^>]*>\s*<img src="gal3\.jpg"[^>]*>\s*<div class="gal-overlay">.*?</div>\s*</div>', '', content, flags=re.DOTALL)

# Remove gal10.jpg entry
content = re.sub(r'\s*<div class="gal-item"[^>]*>\s*<img src="gal10\.jpg"[^>]*>\s*<div class="gal-overlay">.*?</div>\s*</div>', '', content, flags=re.DOTALL)

open('gallery.html', 'w', encoding='utf-8').write(content)
print('Done - removed gal2, gal3, gal10')
