import glob

new_courses_html = '''<!-- --- COURSES FULL --- -->
<section class="courses-full" id="courses">
<div class="container">
  <div class="sec-title" data-aos="fade-up">
    <h2>Our Professional <span>Courses</span></h2>
    <div class="deco"><div class="line"></div><i class="fas fa-diamond"></i><div class="line"></div></div>
    <p>Master the art of beauty with our expert-led professional training. 100% Practical Training & Placement Assistance.</p>
  </div>
  <div class="crs-grid-full">
    
    <!-- Course 1 -->
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="100">
      <div class="crs-card-img">
        <div class="crs-tag">MOST POPULAR</div>
        <img src="https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?w=500&q=80" alt="Makeup Course">
      </div>
      <div class="crs-body-premium">
        <h4>Professional Makeup</h4>
        <div class="specialist-badge"><i class="fas fa-star"></i> Specialist in Bridal HD & Airbrush Makeup</div>
        <p class="dur"><i class="fas fa-clock"></i> Duration: 3-6 Months</p>
        <ul class="crs-list">
          <li><i class="fas fa-check-circle"></i> Complete Color & Skin Theory</li>
          <li><i class="fas fa-check-circle"></i> Advanced Bridal & HD Makeup</li>
          <li><i class="fas fa-check-circle"></i> Signature Airbrush Techniques</li>
          <li><i class="fas fa-check-circle"></i> Party, Engagement & Editorial Looks</li>
        </ul>
        <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20and%20syllabus%20for%20the%20Makeup%20Artistry%20Course." target="_blank" class="crs-wa-btn">
          <i class="fab fa-whatsapp"></i> WhatsApp for Syllabus
        </a>
      </div>
    </div>

    <!-- Course 2 -->
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="200">
      <div class="crs-card-img">
        <img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?w=500&q=80" alt="Hair Course">
      </div>
      <div class="crs-body-premium">
        <h4>Hair Styling Mastery</h4>
        <div class="specialist-badge"><i class="fas fa-cut"></i> Advanced Cuts, Spa & Chemicals</div>
        <p class="dur"><i class="fas fa-clock"></i> Duration: 2-4 Months</p>
        <ul class="crs-list">
          <li><i class="fas fa-check-circle"></i> Hair Science & Deep Treatments</li>
          <li><i class="fas fa-check-circle"></i> Chemical Work (Keratin, Smoothening)</li>
          <li><i class="fas fa-check-circle"></i> Global Hair Coloring & Highlights</li>
          <li><i class="fas fa-check-circle"></i> Premium Bridal Updos & Styling</li>
        </ul>
        <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20and%20syllabus%20for%20the%20Hair%20Styling%20Course." target="_blank" class="crs-wa-btn">
          <i class="fab fa-whatsapp"></i> WhatsApp for Syllabus
        </a>
      </div>
    </div>

    <!-- Course 3 -->
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="300">
      <div class="crs-card-img">
        <div class="crs-tag" style="background:var(--gold);color:var(--black);">ALL-IN-ONE</div>
        <img src="https://images.unsplash.com/photo-1560066984-138dadb4c035?w=800&q=80" alt="Cosmetology Course">
      </div>
      <div class="crs-body-premium">
        <h4>Cosmetology Diploma</h4>
        <div class="specialist-badge"><i class="fas fa-spa"></i> Complete Hair, Skin & Nails Training</div>
        <p class="dur"><i class="fas fa-clock"></i> Duration: 6-12 Months</p>
        <ul class="crs-list">
          <li><i class="fas fa-check-circle"></i> Advanced Skin Aesthetics & Facials</li>
          <li><i class="fas fa-check-circle"></i> Complete Hair Cutting & Chemical Work</li>
          <li><i class="fas fa-check-circle"></i> Nail Art, Extensions & Acrylics</li>
          <li><i class="fas fa-check-circle"></i> Salon Management & Client Handling</li>
        </ul>
        <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20and%20syllabus%20for%20the%20Cosmetology%20Course." target="_blank" class="crs-wa-btn">
          <i class="fab fa-whatsapp"></i> WhatsApp for Syllabus
        </a>
      </div>
    </div>
    
  </div>
</div>
</section>'''

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    start_idx = html.find('<!-- --- COURSES FULL --- -->')
    if start_idx != -1:
        end_idx = html.find('</section>', start_idx) + 10
        old_block = html[start_idx:end_idx]
        html = html.replace(old_block, new_courses_html)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)

new_css = '''
/* --- PREMIUM COURSE DETAILS --- */
.crs-card-img { position: relative; }
.crs-tag {
  position: absolute; top: 15px; left: 15px; background: #E50914; color: #fff;
  font-size: 0.65rem; font-weight: 800; letter-spacing: 1px; padding: 5px 12px;
  border-radius: 4px; z-index: 10; box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
.crs-body-premium { padding: 26px; }
.crs-body-premium h4 { font-family: var(--hd); font-size: 1.6rem; color: var(--gold); margin-bottom: 6px; }
.specialist-badge {
  display: inline-block; background: rgba(201,149,26,0.1); border: 1px solid rgba(201,149,26,0.3);
  color: var(--gold); font-size: 0.72rem; font-weight: 600; padding: 6px 12px; border-radius: 6px;
  margin-bottom: 12px; letter-spacing: 0.5px;
}
.specialist-badge i { margin-right: 5px; }
.crs-body-premium .dur { color: var(--white); font-weight: 600; font-size: 0.8rem; margin-bottom: 16px; display: flex; align-items: center; gap: 6px; }
.crs-body-premium .dur i { color: var(--gold); }
.crs-list { font-size: 0.8rem; color: rgba(255,255,255,0.75); line-height: 1.8; margin-bottom: 24px; }
.crs-list li { margin-bottom: 6px; display: flex; align-items: flex-start; gap: 8px; }
.crs-list li i { color: var(--gold); margin-top: 4px; font-size: 0.8rem; }
.crs-wa-btn {
  display: block; text-align: center; background: linear-gradient(135deg, #25D366, #128C7E);
  color: #fff; padding: 14px; border-radius: 8px; font-weight: 700; font-size: 0.75rem;
  letter-spacing: 1px; text-transform: uppercase; transition: all 0.3s; box-shadow: 0 4px 15px rgba(37,211,102,0.3);
}
.crs-wa-btn:hover {
  transform: translateY(-2px); box-shadow: 0 8px 25px rgba(37,211,102,0.5); color: #fff;
}
.crs-wa-btn i { font-size: 1.1rem; margin-right: 6px; vertical-align: middle; }
'''

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()
css += new_css
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated with premium look!")
