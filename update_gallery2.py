# -*- coding: utf-8 -*-
with open("gallery.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace everything between <div class="gallery-grid"> and </div>\n</div>\n</section>
import re

start_marker = '<div class="gallery-grid">'
end_marker = '</div>\n</div>\n</section>'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_grid = start_marker + """
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
    
    <!-- New 5 Images -->
    <div class="gal-item" data-aos="fade-up" data-aos-delay="300" onclick="openLB(this)">
      <img src="gal6.jpg" alt="Soft Glam Look">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="350" onclick="openLB(this)">
      <img src="gal7.jpg" alt="Full Bridal Look">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="400" onclick="openLB(this)">
      <img src="gal8.jpg" alt="Bridal Jewellery">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="450" onclick="openLB(this)">
      <img src="gal9.jpg" alt="Elegant Bridal">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="500" onclick="openLB(this)">
      <img src="gal10.jpg" alt="Party Makeup Glitter">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
"""
    html = html[:start_idx] + new_grid + html[end_idx:]
    with open("gallery.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Gallery updated with all 10 images!")
else:
    print("Could not find grid markers.")
