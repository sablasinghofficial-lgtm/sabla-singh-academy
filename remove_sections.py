import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove Gallery section
# Starts with: <!-- --- GALLERY + TESTIMONIALS --- -->
# Ends before: <!-- --- VLOGS --- --> (or whatever is next)
html = re.sub(r'<!-- --- GALLERY \+ TESTIMONIALS --- -->.*?<!-- --- VLOGS --- -->', '<!-- --- VLOGS --- -->', html, flags=re.DOTALL)

# Remove Vlogs section
# Starts with: <!-- --- VLOGS --- -->
# Ends before: <!-- --- CTA --- -->
html = re.sub(r'<!-- --- VLOGS --- -->.*?<!-- --- CTA --- -->', '<!-- --- CTA --- -->', html, flags=re.DOTALL)

# Remove Contact section
# Starts with: <!-- --- CONTACT --- -->
# Ends before: <!-- --- FOOTER --- -->
html = re.sub(r'<!-- --- CONTACT --- -->.*?<!-- --- FOOTER --- -->', '<!-- --- FOOTER --- -->', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Sections removed from Home Page")
