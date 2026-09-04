import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove Gallery & Testimonials
# <section class="gt" id="gallery"> ... </section>
html = re.sub(r'<section class="gt".*?</section>', '', html, flags=re.DOTALL)

# Remove Vlogs
# <section class="vlogs" id="vlogs"> ... </section>
html = re.sub(r'<section class="vlogs".*?</section>', '', html, flags=re.DOTALL)

# Remove Contact
# <section class="contact" id="contact"> ... </section>
html = re.sub(r'<section class="contact".*?</section>', '', html, flags=re.DOTALL)

# Also remove the mangled comments
html = re.sub(r'<!--[^>]*GALLERY[^>]*-->', '', html)
html = re.sub(r'<!--[^>]*VLOGS[^>]*-->', '', html)
html = re.sub(r'<!--[^>]*CONTACT[^>]*-->', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done via python")
