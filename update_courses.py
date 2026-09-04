import glob
import re

new_courses_html = '''<!-- --- COURSES FULL --- -->
<section class="courses-full" id="courses">
<div class="container">
  <div class="sec-title" data-aos="fade-up">
    <h2>Our Professional <span>Courses</span></h2>
    <div class="deco"><div class="line"></div><i class="fas fa-diamond"></i><div class="line"></div></div>
    <p>Master the art of beauty with our expert-led professional courses. 100% Practical Training & Placement Assistance.</p>
  </div>
  <div class="crs-grid-full">
    
    <!-- Course 1 -->
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="100">
      <div class="crs-card-img"><img src="https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?w=500&q=80" alt="Makeup Course"></div>
      <div class="crs-card-body" style="padding: 24px;">
        <h4 style="font-family:var(--hd);font-size:1.4rem;color:var(--gold);margin-bottom:8px;">Professional Makeup Artistry</h4>
        <p class="dur" style="color:var(--white);font-weight:600;margin-bottom:12px;font-size:0.8rem;"><i class="fas fa-clock" style="color:var(--gold);"></i> Duration: 3-6 Months</p>
        <p style="font-size:0.8rem;color:var(--gray);line-height:1.7;margin-bottom:16px;">Step-by-step masterclass from basics to advanced techniques.</p>
        <ul style="font-size:0.75rem;color:rgba(255,255,255,0.7);line-height:1.8;margin-bottom:20px;padding-left:0;">
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Color Theory & Skin Science</li>
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Bridal & HD Makeup</li>
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Advanced Airbrush Techniques</li>
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Party & Editorial Looks</li>
        </ul>
        <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20and%20syllabus%20for%20the%20Makeup%20Artistry%20Course." target="_blank" style="display:block;text-align:center;background:#25D366;color:#fff;padding:12px;border-radius:8px;font-weight:700;font-size:0.75rem;letter-spacing:1px;text-transform:uppercase;transition:all 0.3s;"><i class="fab fa-whatsapp" style="font-size:1rem;margin-right:5px;vertical-align:middle;"></i> WhatsApp for Syllabus</a>
      </div>
    </div>

    <!-- Course 2 -->
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="200">
      <div class="crs-card-img"><img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?w=500&q=80" alt="Hair Course"></div>
      <div class="crs-card-body" style="padding: 24px;">
        <h4 style="font-family:var(--hd);font-size:1.4rem;color:var(--gold);margin-bottom:8px;">Master in Hair Styling</h4>
        <p class="dur" style="color:var(--white);font-weight:600;margin-bottom:12px;font-size:0.8rem;"><i class="fas fa-clock" style="color:var(--gold);"></i> Duration: 2-4 Months</p>
        <p style="font-size:0.8rem;color:var(--gray);line-height:1.7;margin-bottom:16px;">Become a professional hairstylist with hands-on practical training.</p>
        <ul style="font-size:0.75rem;color:rgba(255,255,255,0.7);line-height:1.8;margin-bottom:20px;padding-left:0;">
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Hair Anatomy & Treatments</li>
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Advanced Chemical Work (Keratin)</li>
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Global Coloring & Highlights</li>
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Bridal Updos & Styling</li>
        </ul>
        <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20and%20syllabus%20for%20the%20Hair%20Styling%20Course." target="_blank" style="display:block;text-align:center;background:#25D366;color:#fff;padding:12px;border-radius:8px;font-weight:700;font-size:0.75rem;letter-spacing:1px;text-transform:uppercase;transition:all 0.3s;"><i class="fab fa-whatsapp" style="font-size:1rem;margin-right:5px;vertical-align:middle;"></i> WhatsApp for Syllabus</a>
      </div>
    </div>

    <!-- Course 3 -->
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="300">
      <div class="crs-card-img"><img src="https://images.unsplash.com/photo-1560066984-138dadb4c035?w=800&q=80" alt="Cosmetology Course"></div>
      <div class="crs-card-body" style="padding: 24px;">
        <h4 style="font-family:var(--hd);font-size:1.4rem;color:var(--gold);margin-bottom:8px;">Diploma in Cosmetology</h4>
        <p class="dur" style="color:var(--white);font-weight:600;margin-bottom:12px;font-size:0.8rem;"><i class="fas fa-clock" style="color:var(--gold);"></i> Duration: 6-12 Months</p>
        <p style="font-size:0.8rem;color:var(--gray);line-height:1.7;margin-bottom:16px;">The ultimate all-in-one mastery course to open your own salon.</p>
        <ul style="font-size:0.75rem;color:rgba(255,255,255,0.7);line-height:1.8;margin-bottom:20px;padding-left:0;">
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Complete Hair & Skin Science</li>
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Advanced Facials & Aesthetics</li>
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Nail Art, Extension & Acrylics</li>
          <li><i class="fas fa-check" style="color:var(--gold);margin-right:6px;"></i> Salon Management & Setup</li>
        </ul>
        <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20and%20syllabus%20for%20the%20Cosmetology%20Course." target="_blank" style="display:block;text-align:center;background:#25D366;color:#fff;padding:12px;border-radius:8px;font-weight:700;font-size:0.75rem;letter-spacing:1px;text-transform:uppercase;transition:all 0.3s;"><i class="fab fa-whatsapp" style="font-size:1rem;margin-right:5px;vertical-align:middle;"></i> WhatsApp for Syllabus</a>
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
        print(f"Updated Courses in {file}")

