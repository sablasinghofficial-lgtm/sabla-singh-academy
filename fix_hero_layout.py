# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace mini stats in hero-img-panel with empty panel
old_panel = '''  <div class="hero-img-panel" data-aos="fade-left" data-aos-duration="1100">
    <div class="hero-mini-stats">
      <div class="mini-stat"><i class="fas fa-award"></i><span class="mini-num"><span class="counter" data-count="5">0</span>+ Yrs</span><span class="mini-lbl">Excellence</span></div>
      <div class="mini-stat"><i class="fas fa-heart"></i><span class="mini-num"><span class="counter" data-count="500">0</span>+</span><span class="mini-lbl">Happy Clients</span></div>
      <div class="mini-stat"><i class="fas fa-graduation-cap"></i><span class="mini-num"><span class="counter" data-count="200">0</span>+</span><span class="mini-lbl">Students</span></div>
    </div>
  </div>'''

html = html.replace(old_panel, '')

# 2. Add mini stats as horizontal scrolling pills BELOW cta-row
old_cta = '''    <div class="hero-cta-row">
      <a href="https://wa.me/918603388406" target="_blank" class="hero-btn-wa"><i class="fab fa-whatsapp"></i> Book Now on WhatsApp</a>
      <a href="courses.html" class="hero-btn-outline">Explore Courses <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>'''

new_cta = '''    <div class="hero-cta-row">
      <a href="https://wa.me/918603388406" target="_blank" class="hero-btn-wa"><i class="fab fa-whatsapp"></i> Book Now on WhatsApp</a>
      <a href="courses.html" class="hero-btn-outline">Explore Courses <i class="fas fa-arrow-right"></i></a>
    </div>

    <!-- Mini Stats Marquee -->
    <div class="hero-stats-scroll">
      <div class="hs-track">
        <div class="hs-pill"><i class="fas fa-award"></i> <strong><span class="counter" data-count="5">5</span>+</strong> Years Excellence</div>
        <div class="hs-pill"><i class="fas fa-heart"></i> <strong><span class="counter" data-count="500">500</span>+</strong> Happy Clients</div>
        <div class="hs-pill"><i class="fas fa-graduation-cap"></i> <strong><span class="counter" data-count="200">200</span>+</strong> Students</div>
        <div class="hs-pill"><i class="fas fa-star"></i> <strong>Trusted</strong> by 500+ Members</div>
        <div class="hs-pill"><i class="fas fa-award"></i> <strong><span class="counter" data-count="5">5</span>+</strong> Years Excellence</div>
        <div class="hs-pill"><i class="fas fa-heart"></i> <strong><span class="counter" data-count="500">500</span>+</strong> Happy Clients</div>
        <div class="hs-pill"><i class="fas fa-graduation-cap"></i> <strong><span class="counter" data-count="200">200</span>+</strong> Students</div>
        <div class="hs-pill"><i class="fas fa-star"></i> <strong>Trusted</strong> by 500+ Members</div>
      </div>
    </div>
  </div>'''

html = html.replace(old_cta, new_cta)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Hero layout updated!")
