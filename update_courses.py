import re

with open('courses.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Elite Hair Design duration: 2-4 Months -> 60 Days
content = content.replace('Duration: 2-4 Months', 'Duration: 60 Days')

# 2. Update Elite Hair Design image: gal8.jpg -> course_hair.jpg
content = content.replace('<img src="gal8.jpg" alt="Hair Course">', '<img src="course_hair.jpg" alt="Hair Course" style="width:100%;height:100%;object-fit:cover;">')

# 3. Find where the cosmetology course starts and insert Nails & Lashes before it
nails_lashes_card = '''
    <!-- Nails & Lash Extension Course -->
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="250">
      <div class="crs-card-img">
        <div class="crs-tag" style="background:#b5868a;color:#fff;">SPECIALTY</div>
        <img src="course_lashes.jpg" alt="Nails and Lash Extension Course" style="width:100%;height:100%;object-fit:cover;">
      </div>
      <div class="crs-body-premium">
        <h4>Nail Art &amp; Lash Extension</h4>
        <div class="specialist-badge"><i class="fas fa-spa"></i> Nails &amp; Lash Expert</div>
        <p class="dur"><i class="fas fa-clock"></i> Duration: 30 Days</p>
        <p class="crs-desc">Master stunning nail art designs and professional lash extension techniques — the most in-demand beauty skills in salons today.</p>
        <ul class="crs-list-premium">
          <li><i class="fas fa-check"></i> Gel Nails &amp; Nail Art Designs</li>
          <li><i class="fas fa-check"></i> Acrylic &amp; Extension Techniques</li>
          <li><i class="fas fa-check"></i> Classic, Volume &amp; Hybrid Lash Extensions</li>
        </ul>
        <div class="crs-action-btns">
          <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20for%20the%20Nail%20Art%20and%20Lash%20Extension%20Course." target="_blank" class="crs-btn crs-wa"><i class="fab fa-whatsapp"></i> WhatsApp</a>
          <a href="tel:+918603388406" class="crs-btn crs-call"><i class="fas fa-phone-alt"></i> Call Now</a>
        </div>
      </div>
    </div>

'''

# Insert the new card before the Cosmetology course (Course 3 - identified by ALL-IN-ONE tag)
content = content.replace('    <!-- Course 3 -->', nails_lashes_card + '    <!-- Course 3 -->')

with open('courses.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Updated Hair duration, image, and added Nails & Lashes course.")
