# -*- coding: utf-8 -*-
import re

with open("gallery.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the entire <section class="gt" id="gallery"> block up to <section class="cta">
old_start = html.find('<!-- --- GALLERY + TESTIMONIALS --- -->')
if old_start == -1:
    old_start = html.find('<!-- --- GALLERY + TESTIMONIALS --- -->')
if old_start == -1:
    old_start = html.find('<section class="gt"')

cta_start = html.find('<!-- --- CTA --- -->')
if cta_start == -1:
    cta_start = html.find('<!-- --- CTA --- -->')
if cta_start == -1:
    cta_start = html.find('<section class="cta">')

new_gallery = """<!-- --- FULL GALLERY --- -->
<section class="gallery-page" id="gallery">
<div class="container">
  <div class="sec-title" data-aos="fade-up">
    <h2>Our <span>Portfolio</span></h2>
    <div class="deco"><div class="line"></div><i class="fas fa-camera"></i><div class="line"></div></div>
    <p>A glimpse into our premium bridal makeovers, beauty transformations, and behind-the-scenes magic at Studio S.</p>
  </div>
  
  <div class="gallery-grid">
    <div class="gal-item" data-aos="fade-up" data-aos-delay="50" onclick="openLB(this)">
      <img src="gal1.jpg" alt="Bridal Makeup">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="100" onclick="openLB(this)">
      <img src="gal2.jpg" alt="Party Makeup">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="150" onclick="openLB(this)">
      <img src="gal3.jpg" alt="Bridal Look">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="200" onclick="openLB(this)">
      <img src="gal4.jpg" alt="Makeup Academy">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="250" onclick="openLB(this)">
      <img src="gal5.jpg" alt="Premium Service">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="300" onclick="openLB(this)">
      <img src="https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=600&q=80" alt="Makeup Setup">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="350" onclick="openLB(this)">
      <img src="https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=600&q=80" alt="Bridal Details">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="400" onclick="openLB(this)">
      <img src="https://images.unsplash.com/photo-1515377905703-c4788e51af15?w=600&q=80" alt="Professional Tools">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
  </div>
</div>
</section>

"""

if old_start != -1 and cta_start != -1:
    html = html[:old_start] + new_gallery + html[cta_start:]
    with open("gallery.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("gallery.html updated successfully!")
else:
    print(f"Could not find markers. old_start: {old_start}, cta_start: {cta_start}")
