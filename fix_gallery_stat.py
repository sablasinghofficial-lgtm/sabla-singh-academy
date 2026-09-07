import re

# --- Gallery: Remove gal4 and gal5 ---
with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'\s*<div class="gal-item"[^>]*>\s*<img src="gal4\.jpg"[^>]*>\s*<div class="gal-overlay">.*?</div>\s*</div>', '', content, flags=re.DOTALL)
content = re.sub(r'\s*<div class="gal-item"[^>]*>\s*<img src="gal5\.jpg"[^>]*>\s*<div class="gal-overlay">.*?</div>\s*</div>', '', content, flags=re.DOTALL)

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Removed gal4 and gal5 from gallery")

# --- About/index: Update 500+ to 2500+ ---
for fname in ['index.html', 'about.html']:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            c = f.read()
        updated = c.replace('data-count="500"', 'data-count="2500"')
        updated = updated.replace('>500+<', '>2500+<')
        updated = updated.replace('500+ Happy', '2500+ Happy')
        if updated != c:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(updated)
            print(f"Updated 500+ to 2500+ in {fname}")
        else:
            print(f"No change needed in {fname}")
    except FileNotFoundError:
        print(f"Not found: {fname}")

print("Done!")
