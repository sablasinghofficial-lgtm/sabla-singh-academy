import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract CSS
css_match = re.search(r'<style>(.*?)</style>', html, re.DOTALL)
css = css_match.group(1) if css_match else ''
css += '''
/* ═══ INNER PAGE HEADER ═══ */
.page-header {
  padding: 120px 0 80px;
  background: linear-gradient(rgba(10,10,10,0.8), rgba(10,10,10,0.95)), url('https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=1920&q=80') center/cover;
  text-align: center;
  border-bottom: 2px solid var(--gold);
}
.page-header h1 {
  font-family: var(--hd);
  font-size: 3.5rem;
  color: var(--white);
  margin-bottom: 12px;
}
.page-header h1 span { color: var(--gold); font-style: italic; }
.breadcrumb {
  font-size: 0.8rem;
  color: var(--gold);
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 600;
}
.breadcrumb a { color: var(--white); transition: color 0.3s; }
.breadcrumb a:hover { color: var(--gold); }
.breadcrumb i { font-size: 0.6rem; margin: 0 8px; color: var(--gray); }
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Extract JS
js_match = re.search(r'<script>\s*(AOS.*?)\s*</script>', html, re.DOTALL)
js = js_match.group(1) if js_match else ''
js = re.sub(r'// Smooth scroll.*?\}\);\}\);', '', js, flags=re.DOTALL)
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Prepare Base HTML by removing styles and inline scripts, linking to external
base_html = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="style.css">', html, flags=re.DOTALL)
base_html = re.sub(r'<script>\s*AOS.*?</script>', '<script src="script.js"></script>', base_html, flags=re.DOTALL)

# Update Navigation Links
nav_map = {
    'href="#home"': 'href="index.html"',
    'href="#about"': 'href="about.html"',
    'href="#services"': 'href="services.html"',
    'href="#courses"': 'href="courses.html"',
    'href="#gallery"': 'href="gallery.html"',
    'href="#vlogs"': 'href="vlogs.html"',
    'href="#contact"': 'href="contact.html"'
}
for old, new in nav_map.items():
    base_html = base_html.replace(old, new)
base_html = base_html.replace('class="active"', '')

# Extract components using a generic split based on sections
sections = [
    'HERO', 'SERVICES', 'ABOUT + COURSES SPLIT', 'WHY CHOOSE US', 
    'STATS BAR', 'GALLERY + TESTIMONIALS', 'VLOGS', 'CTA', 'CONTACT', 'FOOTER'
]

# A safe extraction function
def get_sec(name):
    # Find start
    idx = base_html.find(f'<!-- ═══ {name} ═══ -->')
    if idx == -1: return ''
    # Find next section start to determine end
    end_idx = len(base_html)
    for s in sections:
        s_idx = base_html.find(f'<!-- ═══ {s} ═══ -->', idx + 10)
        if s_idx != -1 and s_idx < end_idx:
            end_idx = s_idx
    return base_html[idx:end_idx]

head_top = base_html[:base_html.find('<!-- ═══ HERO ═══ -->')]
footer_bottom = base_html[base_html.find('<!-- ═══ FOOTER ═══ -->'):]

hero = get_sec('HERO')
services = get_sec('SERVICES')
about = get_sec('ABOUT + COURSES SPLIT')
why = get_sec('WHY CHOOSE US')
stats = get_sec('STATS BAR')
gallery = get_sec('GALLERY + TESTIMONIALS')
vlogs = get_sec('VLOGS')
cta = get_sec('CTA')
contact = get_sec('CONTACT')

# Fix index.html Home active state
idx_html = base_html.replace('href="index.html"', 'href="index.html" class="active"', 1)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_html)

# Helper to generate page
def make_page(filename, title, content):
    header = f"""
<!-- ═══ PAGE HEADER ═══ -->
<section class="page-header">
  <div class="container" data-aos="fade-up">
    <h1>{title.split(' ')[0]} <span>{' '.join(title.split(' ')[1:])}</span></h1>
    <div class="breadcrumb">
      <a href="index.html">Home</a> <i class="fas fa-chevron-right"></i> {title}
    </div>
  </div>
</section>
"""
    page_head = head_top.replace(f'href="{filename}"', f'href="{filename}" class="active"')
    full_html = page_head + header + content + cta + footer_bottom
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)

# Generate inner pages
make_page('about.html', 'About Us', about + why + stats)
make_page('services.html', 'Our Services', services)
make_page('courses.html', 'Professional Courses', about + why)
make_page('gallery.html', 'Our Gallery', gallery)
make_page('vlogs.html', 'Latest Vlogs', vlogs)
make_page('contact.html', 'Contact Us', contact)

print("Pages created successfully")
