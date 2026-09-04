# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

old_about = """<!-- --- ABOUT FULL 3D --- -->
<section class="about-full" id="about">
<div class="container">
  <div class="about-3d-box" data-aos="zoom-in" data-aos-duration="1000">
    <div class="ab-3d-img">
      <img src="https://images.unsplash.com/photo-1595959183082-7b570b7e08e2?w=600&q=80" alt="Sabla Singh Academy">
      <div class="ab-yrs-3d"><div class="big">5<sup>+</sup></div><div class="sub">Years of Excellence</div></div>
    </div>
    <div class="ab-3d-content">
      <div style="border:1.5px solid var(--gold);color:var(--gold);padding:5px 14px;border-radius:20px;font-size:.62rem;font-weight:600;letter-spacing:2px;text-transform:uppercase;margin-bottom:18px;width:fit-content;">About Us</div>
      <h2 style="font-family:var(--hd);font-size:2.5rem;font-weight:600;color:#fff;line-height:1.2;margin-bottom:18px;">Empowering Beauty.<br><em style="color:var(--gold);font-style:italic;">Inspiring</em> Confidence.</h2>
      <p style="font-size:.85rem;color:rgba(255,255,255,.65);line-height:1.85;margin-bottom:22px;">Sabla Singh Academy has been a pioneer in the beauty industry in Ranchi, shaping thousands of successful careers and enhancing natural beauty for over 5 successful years. Led by founder <strong style="color:var(--gold)">Sabla Singh</strong>, our academy delivers world-class training and premium beauty services.</p>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:26px;">
        <div style="font-size:.8rem;font-weight:500;color:rgba(255,255,255,.8);"><i class="fas fa-check" style="color:var(--gold);margin-right:8px;"></i> Industry Expert Trainers</div>
        <div style="font-size:.8rem;font-weight:500;color:rgba(255,255,255,.8);"><i class="fas fa-check" style="color:var(--gold);margin-right:8px;"></i> Advanced HD &amp; Airbrush</div>
        <div style="font-size:.8rem;font-weight:500;color:rgba(255,255,255,.8);"><i class="fas fa-check" style="color:var(--gold);margin-right:8px;"></i> Personalized Training</div>
        <div style="font-size:.8rem;font-weight:500;color:rgba(255,255,255,.8);"><i class="fas fa-check" style="color:var(--gold);margin-right:8px;"></i> International Products</div>
      </div>
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:22px;">
        <div style="width:30px;height:1.5px;background:var(--gold);"></div>
        <div><div style="font-family:var(--sc);font-size:2rem;color:var(--gold);">Sabla Singh</div><div style="font-size:.62rem;color:rgba(255,255,255,.45);letter-spacing:1px;text-transform:uppercase;">Founder &amp; Director</div></div>
      </div>
      <a href="about.html" class="ab-btn">Know More About Us <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</div>
</section>"""

new_about = """<!-- --- ABOUT FULL PREMIUM --- -->
<section class="about-premium" id="about">
  <div class="about-pm-inner">

    <!-- Left: Image with overlays -->
    <div class="apm-left" data-aos="fade-right" data-aos-duration="900">
      <div class="apm-img-wrap">
        <img src="https://images.unsplash.com/photo-1552374196-c4e7ffc6e126?w=700&q=85" alt="Sabla Singh - Founder">
        <!-- Gold frame corners -->
        <div class="apm-corner apm-tl"></div>
        <div class="apm-corner apm-br"></div>
        <!-- Experience badge -->
        <div class="apm-exp-badge">
          <span class="apm-exp-num">5<sup>+</sup></span>
          <span class="apm-exp-lbl">Years of<br>Excellence</span>
        </div>
      </div>
      <!-- Small floating stats below image -->
      <div class="apm-mini-stats">
        <div class="apm-mstat"><span class="apm-ms-num">500+</span><span class="apm-ms-lbl">Happy Clients</span></div>
        <div class="apm-divider"></div>
        <div class="apm-mstat"><span class="apm-ms-num">200+</span><span class="apm-ms-lbl">Students</span></div>
        <div class="apm-divider"></div>
        <div class="apm-mstat"><span class="apm-ms-num">3</span><span class="apm-ms-lbl">Courses</span></div>
      </div>
    </div>

    <!-- Right: Content -->
    <div class="apm-right" data-aos="fade-left" data-aos-duration="900" data-aos-delay="100">
      <div class="apm-tag">About Us</div>
      <h2 class="apm-heading">
        Empowering Beauty.<br>
        <em>Inspiring</em> Confidence.
      </h2>
      <div class="apm-gold-line"><span></span></div>
      <p class="apm-desc">
        Sabla Singh Academy has been a pioneer in the beauty industry in Ranchi, shaping thousands of successful careers and enhancing natural beauty for over 5 successful years. Led by founder <strong>Sabla Singh</strong>, our academy delivers world-class training and premium beauty services using the finest international products.
      </p>
      <div class="apm-features">
        <div class="apm-feat"><i class="fas fa-check-circle"></i><span>Industry Expert Trainers</span></div>
        <div class="apm-feat"><i class="fas fa-check-circle"></i><span>Advanced HD &amp; Airbrush</span></div>
        <div class="apm-feat"><i class="fas fa-check-circle"></i><span>Personalized Training</span></div>
        <div class="apm-feat"><i class="fas fa-check-circle"></i><span>International Products</span></div>
        <div class="apm-feat"><i class="fas fa-check-circle"></i><span>Certified Courses</span></div>
        <div class="apm-feat"><i class="fas fa-check-circle"></i><span>Specialist in Bridal Makeup</span></div>
      </div>
      <div class="apm-signature">
        <div class="apm-sig-line"></div>
        <div>
          <div class="apm-sig-name">Sabla Singh</div>
          <div class="apm-sig-role">Founder &amp; Director, Sabla Singh Academy</div>
        </div>
      </div>
      <a href="about.html" class="apm-btn">Know More About Us <i class="fas fa-arrow-right"></i></a>
    </div>

  </div>
</section>"""

html = html.replace(old_about, new_about)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("About section upgraded!" if old_about in open("index.html","r",encoding="utf-8").read() == False else "About upgraded!")
