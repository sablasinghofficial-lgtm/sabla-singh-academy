# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# 1. FIX THE MARQUEE BAR SIZING & FULL-WIDTH LOCK
marquee_css = """
/* ==== MARQUEE FIX ==== */
.marquee-bar { 
    padding: 22px 0 !important; 
    width: 100vw !important; 
    margin-left: calc(-50vw + 50%) !important; /* Forces edge-to-edge lock */
    background: var(--gold) !important; 
    border-top: 3px solid #000 !important;
    border-bottom: 3px solid #000 !important;
}
.marquee-track span { 
    font-size: 1.25rem !important; 
    font-weight: 800 !important; 
    padding: 0 45px !important; 
    color: #111 !important; 
    letter-spacing: 2.5px !important;
}
.marquee-track span i { 
    font-size: 0.8rem !important; 
    color: var(--green) !important; /* Make the little diamonds green for theme consistency */
}
"""

css = css + "\n" + marquee_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

# 2. FIX ABOUT.HTML TO MATCH THE PREMIUM OWNER PROFILE
with open("about.html", "r", encoding="utf-8", errors="replace") as f:
    about_html = f.read()

# We will replace whatever is inside <section class="about-page">... </section>
# with the premium layout from index.html (but adapted for the standalone page).

import re

premium_about_page_content = """<section class="about-page" style="padding-top: 80px;">
  <div class="container">
    <div class="about-pm-inner" style="display: grid; grid-template-columns: 1fr 1fr; gap: 70px; align-items: center;">

      <!-- Left: Founder Photo -->
      <div class="apm-left" data-aos="fade-right" data-aos-duration="900" style="position: relative;">
        <div class="apm-img-wrap" style="position: relative; border-radius: 12px; overflow: hidden; border: 3px solid var(--gold); box-shadow: 0 20px 50px rgba(6,78,35,0.4);">
          <img src="gal10.jpg" alt="Sabla Singh - Founder" style="width: 100%; display: block;">
        </div>
        <!-- Stats -->
        <div class="apm-mini-stats" style="display: flex; align-items: center; justify-content: center; gap: 20px; background: var(--green); padding: 25px; border-radius: 12px; position: relative; margin-top: -40px; width: 90%; margin-left: auto; margin-right: auto; box-shadow: 0 10px 30px rgba(0,0,0,0.5); z-index: 5; border: 1px solid var(--gold);">
          <div style="text-align: center;"><span style="display: block; font-size: 1.8rem; font-weight: 700; color: var(--gold);">5+</span><span style="font-size: 0.85rem; color: #fff; text-transform: uppercase; letter-spacing: 1px;">Years Exp</span></div>
          <div style="width: 2px; height: 40px; background: rgba(245,199,26,0.3);"></div>
          <div style="text-align: center;"><span style="display: block; font-size: 1.8rem; font-weight: 700; color: var(--gold);">500+</span><span style="font-size: 0.85rem; color: #fff; text-transform: uppercase; letter-spacing: 1px;">Happy Clients</span></div>
          <div style="width: 2px; height: 40px; background: rgba(245,199,26,0.3);"></div>
          <div style="text-align: center;"><span style="display: block; font-size: 1.8rem; font-weight: 700; color: var(--gold);">200+</span><span style="font-size: 0.85rem; color: #fff; text-transform: uppercase; letter-spacing: 1px;">Students</span></div>
        </div>
      </div>

      <!-- Right: Content & Message -->
      <div class="apm-right" data-aos="fade-left" data-aos-duration="900" data-aos-delay="100">
        <div class="apm-tag" style="color: var(--gold); font-weight: 700; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 10px; font-size: 1.1rem;">Meet The Founder</div>
        <h2 class="apm-heading" style="font-size: 3.5rem; font-family: var(--hd); line-height: 1.1; margin-bottom: 25px; color: #fff;">
          Sabla <em style="color: var(--green); text-shadow: 0 0 2px rgba(255,255,255,0.2);">Singh</em>
        </h2>
        
        <div style="font-size: 1.25rem; line-height: 1.8; color: #ccc; margin-bottom: 30px;">
          <p style="margin-bottom: 20px;">
            "My vision has always been simple: To reveal the true, natural beauty of every client while empowering the next generation of artists with world-class skills."
          </p>
          <p>
            Welcome to <strong>Sabla Singh Academy</strong>. As Ranchi's premier destination for luxury bridal makeup and professional cosmetology training, we bring over 5 years of international-level expertise directly to you. Whether you're a bride dreaming of the perfect wedding day look or a passionate student ready to build a successful career, my team and I are dedicated to making your vision a reality.
          </p>
        </div>

        <div style="background: rgba(245,199,26,0.05); padding: 30px; border-left: 5px solid var(--gold); border-radius: 8px; margin-bottom: 40px;">
          <h4 style="font-size: 1.6rem; color: var(--gold); font-family: var(--hd); margin-bottom: 20px;">Why Choose Us?</h4>
          <ul style="list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <li style="display: flex; gap: 12px; font-size: 1.15rem; align-items: center;"><i class="fas fa-gem" style="color: var(--gold); font-size: 1.3rem;"></i> Premium Products</li>
            <li style="display: flex; gap: 12px; font-size: 1.15rem; align-items: center;"><i class="fas fa-user-graduate" style="color: var(--gold); font-size: 1.3rem;"></i> 100% Practical Training</li>
            <li style="display: flex; gap: 12px; font-size: 1.15rem; align-items: center;"><i class="fas fa-award" style="color: var(--gold); font-size: 1.3rem;"></i> ISO Certified Academy</li>
            <li style="display: flex; gap: 12px; font-size: 1.15rem; align-items: center;"><i class="fas fa-star" style="color: var(--gold); font-size: 1.3rem;"></i> 5-Star Rated Service</li>
          </ul>
        </div>

        <div style="display: flex; align-items: center; gap: 25px;">
          <a href="courses.html" class="crs-btn" style="text-decoration: none; display: inline-block;">Explore Courses</a>
          <div style="display: flex; flex-direction: column;">
            <span style="font-size: 1.6rem; font-family: var(--sc); color: #fff;">Sabla Singh</span>
            <span style="font-size: 0.85rem; color: var(--gold); letter-spacing: 2px; text-transform: uppercase; font-weight: 700;">Founder & Director</span>
          </div>
        </div>

      </div>

    </div>
  </div>
</section>"""

# Find the generic about section and replace its content
# It likely looks like <section class="about-page"> ... </section>
# I'll use regex to replace everything inside it, or just replace the whole section.
new_html = re.sub(r'<section class="about-page.*?</section>', premium_about_page_content, about_html, flags=re.DOTALL)

with open("about.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Marquee and About Page fixed successfully!")
