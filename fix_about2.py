# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8", errors="replace") as f:
    html = f.read()

new_about_content = """<!-- --- ABOUT FULL PREMIUM --- -->
<section class="about-premium" id="about">
  <div class="about-pm-inner">

    <!-- Left: Image with overlays -->
    <div class="apm-left" data-aos="fade-right" data-aos-duration="900">
      <div class="apm-img-wrap">
        <img src="gal10.jpg" alt="Sabla Singh - Founder">
        <div class="apm-corner apm-tl"></div>
        <div class="apm-corner apm-br"></div>
        <div class="apm-exp-badge">
          <span class="apm-exp-num">5<sup>+</sup></span>
          <span class="apm-exp-lbl">Years of<br>Excellence</span>
        </div>
      </div>
      <div class="apm-mini-stats">
        <div class="apm-mstat"><span class="apm-ms-num">500+</span><span class="apm-ms-lbl">Happy Clients</span></div>
        <div class="apm-divider"></div>
        <div class="apm-mstat"><span class="apm-ms-num">200+</span><span class="apm-ms-lbl">Students</span></div>
        <div class="apm-divider"></div>
        <div class="apm-mstat"><span class="apm-ms-num">10+</span><span class="apm-ms-lbl">Masterclasses</span></div>
      </div>
    </div>

    <!-- Right: Content -->
    <div class="apm-right" data-aos="fade-left" data-aos-duration="900" data-aos-delay="100">
      <div class="apm-tag">Meet The Founder</div>
      <h2 class="apm-heading">
        Sabla <em>Singh</em>
      </h2>
      <div class="apm-gold-line"><span></span></div>
      
      <p class="apm-desc">
        Welcome to <strong>Sabla Singh Academy</strong>, Ranchi's premier destination for luxury beauty services and professional academy training. Founded by <strong>Sabla Singh</strong>, a highly acclaimed makeup artist and beauty visionary, the academy was established with a mission to empower aspiring artists and enhance natural beauty. 
      </p>
      <p class="apm-desc">
        With over <strong>5+ years of industry excellence</strong>, Sabla Singh brings international standards of HD & Airbrush makeup, hair styling, and skin treatments directly to Ranchi. Her hands-on teaching approach has successfully shaped the careers of hundreds of students.
      </p>

      <div class="apm-courses-box" style="margin: 25px 0; padding: 25px; background: rgba(201,149,26,0.05); border-left: 4px solid var(--gold); border-radius: 4px;">
        <h4 style="font-size: 1.5rem; color: var(--gold); margin-bottom: 16px; font-family: var(--hd);">Our Professional Courses:</h4>
        <div class="apm-features" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
          <div class="apm-feat" style="display: flex; gap: 10px; align-items: flex-start;"><i class="fas fa-palette" style="color: var(--gold); font-size: 1.2rem; margin-top: 4px;"></i><span style="font-size:1.15rem; line-height: 1.4;"><strong>Makeup Artistry</strong><br><small style="color:#aaa; font-size:0.95rem;">Bridal, HD & Airbrush</small></span></div>
          <div class="apm-feat" style="display: flex; gap: 10px; align-items: flex-start;"><i class="fas fa-scissors" style="color: var(--gold); font-size: 1.2rem; margin-top: 4px;"></i><span style="font-size:1.15rem; line-height: 1.4;"><strong>Hair Designing</strong><br><small style="color:#aaa; font-size:0.95rem;">Styling & Chemical Work</small></span></div>
          <div class="apm-feat" style="display: flex; gap: 10px; align-items: flex-start;"><i class="fas fa-spa" style="color: var(--gold); font-size: 1.2rem; margin-top: 4px;"></i><span style="font-size:1.15rem; line-height: 1.4;"><strong>Cosmetology</strong><br><small style="color:#aaa; font-size:0.95rem;">Skin & Hair Treatments</small></span></div>
          <div class="apm-feat" style="display: flex; gap: 10px; align-items: flex-start;"><i class="fas fa-hand-sparkles" style="color: var(--gold); font-size: 1.2rem; margin-top: 4px;"></i><span style="font-size:1.15rem; line-height: 1.4;"><strong>Nail & Lash Art</strong><br><small style="color:#aaa; font-size:0.95rem;">Extensions & Styling</small></span></div>
        </div>
      </div>

      <div class="apm-signature">
        <div class="apm-sig-line"></div>
        <div>
          <div class="apm-sig-name" style="font-size: 1.6rem;">Sabla Singh</div>
          <div class="apm-sig-role" style="font-size: 1rem;">Founder & Director, Sabla Singh Academy</div>
        </div>
      </div>
    </div>

  </div>
</section>"""

# Find the start and end of the block
start_idx = html.find("<!-- --- ABOUT FULL PREMIUM --- -->")
if start_idx != -1:
    end_tag = "</section>"
    end_idx = html.find(end_tag, start_idx) + len(end_tag)
    html = html[:start_idx] + new_about_content + html[end_idx:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("About section updated successfully!")
else:
    print("Could not find the About block!")
