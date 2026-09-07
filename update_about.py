import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the about-slideshow div entirely
content = re.sub(
    r'\s*<!-- Dynamic Gallery Slideshow to fill empty space -->\s*<div class="about-slideshow">.*?</div>',
    '',
    content,
    flags=re.DOTALL
)

# Also replace the founder.jpg with the new bigger portrait
content = content.replace(
    '<img src="founder.jpg" alt="Sabla Singh - Founder &amp; Director">',
    '<img src="about_portrait.jpg" alt="Sabla Singh - Founder &amp; Director" style="width:100%;height:100%;object-fit:cover;object-position:center top;">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Removed slideshow, added portrait photo.")
