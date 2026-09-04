# -*- coding: utf-8 -*-
with open("gallery.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to insert 5 new images before the closing </div> of <div class="gallery-grid">
insert_marker = '</div>\n</div>\n</section>'
idx = html.find(insert_marker)

if idx != -1:
    new_items = """
    <!-- Batch 3 Images -->
    <div class="gal-item" data-aos="fade-up" data-aos-delay="550" onclick="openLB(this)">
      <img src="gal11.jpg" alt="Bridal Transformation">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="600" onclick="openLB(this)">
      <img src="gal12.jpg" alt="Airbrush Bridal">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="650" onclick="openLB(this)">
      <img src="gal13.jpg" alt="HD Bridal Makeup">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="700" onclick="openLB(this)">
      <img src="gal14.jpg" alt="Premium Bridal Look">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="750" onclick="openLB(this)">
      <img src="gal15.jpg" alt="Luxury Bridal Style">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
"""
    html = html[:idx] + new_items + html[idx:]
    with open("gallery.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Gallery updated with total 15 images!")
else:
    print("Could not find insert marker.")
