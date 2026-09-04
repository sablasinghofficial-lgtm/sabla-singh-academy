# -*- coding: utf-8 -*-
with open("gallery.html", "r", encoding="utf-8") as f:
    html = f.read()

# We need to insert 3 new images before the closing </div> of <div class="gallery-grid">
insert_marker = '</div>\n</div>\n</section>'
idx = html.find(insert_marker)

if idx != -1:
    new_items = """
    <!-- Batch 4 Images -->
    <div class="gal-item" data-aos="fade-up" data-aos-delay="800" onclick="openLB(this)">
      <img src="gal16.jpg" alt="Traditional Bridal Look">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="850" onclick="openLB(this)">
      <img src="gal17.jpg" alt="Bridal Eye Makeup">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
    <div class="gal-item" data-aos="fade-up" data-aos-delay="900" onclick="openLB(this)">
      <img src="gal18.jpg" alt="Gorgeous Bridal Avatar">
      <div class="gal-overlay"><i class="fas fa-search-plus"></i></div>
    </div>
"""
    html = html[:idx] + new_items + html[idx:]
    with open("gallery.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Gallery updated with total 18 images!")
else:
    print("Could not find insert marker.")
