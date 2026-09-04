# -*- coding: utf-8 -*-
# Read the full multi-page website content from other files to understand the shared structure
# Then rebuild index.html cleanly with the new hero

with open("courses.html", "r", encoding="utf-8") as f:
    courses = f.read()

# Extract header section (everything before <div class="page-header">)
header_end = courses.find('<div class="page-header">')
header_html = courses[:header_end]

# Extract footer section (from <footer to end)
footer_start = courses.find('<footer class="footer">')
footer_html = courses[footer_start:]

# Build fresh index.html
index_html = header_html.replace('<link rel="canonical" href="courses.html">', '<link rel="canonical" href="index.html">') if '<link rel="canonical"' in header_html else header_html

# Fix title and active link in index
index_html = index_html.replace(
    '<title>Sabla Singh Academy � Our Professional Courses | Ranchi</title>',
    '<title>Sabla Singh Academy � Premium Bridal HD & Airbrush Makeup Academy | Ranchi</title>'
)
index_html = index_html.replace(
    '<a href="courses.html" class="active">',
    '<a href="courses.html">'
).replace(
    '<a href="index.html">Home</a>',
    '<a href="index.html" class="active">Home</a>'
)

# Build body content
body_content = """
<!-- --- HERO --- -->
<section class="hero" id="home">
  <div class="hero-overlay"></div>
  <div class="hero-content" data-aos="fade-right" data-aos-duration="1000">
    <p class="hero-tagline">? Ranchi's Most Trusted Beauty &amp; Academy ?</p>
    <h3 class="hero-sub">Where Beauty Meets</h3>
    <h1 class="hero-main"><span class="typewriter-wrap" id="typewriter">CONFIDENCE</span></h1>
    <h2 class="hero-meet">Meets <em>Career</em></h2>
    <div class="hero-academy-name">SABLA SINGH ACADEMY</div>
    <p class="hero-brief">Your Premier Destination for Beauty,<br>Wellness &amp; Professional Training</p>
    <div class="hero-trust">
      <div class="trust-icon"><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i></div>
      <p class="trust-text">Trusted by <strong>500+</strong> Happy Members</p>
    </div>
    <div class="hero-cta-row">
      <a href="https://wa.me/918603388406" target="_blank" class="hero-btn-wa"><i class="fab fa-whatsapp"></i> Book Now on WhatsApp</a>
      <a href="courses.html" class="hero-btn-outline">Explore Courses <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
  <div class="hero-img-panel" data-aos="fade-left" data-aos-duration="1100">
    <div class="hero-mini-stats">
      <div class="mini-stat"><i class="fas fa-award"></i><span class="mini-num"><span class="counter" data-count="5">0</span>+ Yrs</span><span class="mini-lbl">Excellence</span></div>
      <div class="mini-stat"><i class="fas fa-heart"></i><span class="mini-num"><span class="counter" data-count="500">0</span>+</span><span class="mini-lbl">Happy Clients</span></div>
      <div class="mini-stat"><i class="fas fa-graduation-cap"></i><span class="mini-num"><span class="counter" data-count="200">0</span>+</span><span class="mini-lbl">Students</span></div>
    </div>
  </div>
</section>

<!-- --- MARQUEE SERVICES --- -->
<div class="marquee-bar">
  <div class="marquee-track">
    <span><i class="fas fa-diamond"></i> Bridal Makeup</span>
    <span><i class="fas fa-diamond"></i> HD Makeup</span>
    <span><i class="fas fa-diamond"></i> Airbrush Makeup</span>
    <span><i class="fas fa-diamond"></i> Party Makeup</span>
    <span><i class="fas fa-diamond"></i> Skin Facial</span>
    <span><i class="fas fa-diamond"></i> Skin Cleanup</span>
    <span><i class="fas fa-diamond"></i> Hair Cut</span>
    <span><i class="fas fa-diamond"></i> Hair Spa</span>
    <span><i class="fas fa-diamond"></i> Chemical Work</span>
    <span><i class="fas fa-diamond"></i> Nail Art</span>
    <span><i class="fas fa-diamond"></i> Nail Extension</span>
    <span><i class="fas fa-diamond"></i> Manicure &amp; Pedicure</span>
    <span><i class="fas fa-diamond"></i> Lash Extension</span>
    <span><i class="fas fa-diamond"></i> Makeup Course</span>
    <span><i class="fas fa-diamond"></i> Hair Styling Course</span>
    <span><i class="fas fa-diamond"></i> Cosmetology Diploma</span>
    <span><i class="fas fa-diamond"></i> Bridal Makeup</span>
    <span><i class="fas fa-diamond"></i> HD Makeup</span>
    <span><i class="fas fa-diamond"></i> Airbrush Makeup</span>
    <span><i class="fas fa-diamond"></i> Nail Art</span>
    <span><i class="fas fa-diamond"></i> Lash Extension</span>
  </div>
</div>

<!-- --- COURSES FULL --- -->
<section class="courses-full" id="courses">
<div class="container">
  <div class="sec-title" data-aos="fade-up">
    <h2>Our Professional <span>Courses</span></h2>
    <div class="deco"><div class="line"></div><i class="fas fa-diamond"></i><div class="line"></div></div>
    <p>Master the art of beauty with our expert-led professional training. 100% Practical Training &amp; Placement Assistance.</p>
  </div>
  <div class="crs-grid-full">
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="100">
      <div class="crs-card-img"><div class="crs-tag">MOST POPULAR</div><img src="https://images.unsplash.com/photo-1487412947147-5cebf100ffc2?w=500&q=80" alt="Makeup Course"></div>
      <div class="crs-body-premium">
        <h4>Professional Makeup</h4>
        <div class="specialist-badge"><i class="fas fa-star"></i> Specialist in Bridal HD &amp; Airbrush Makeup</div>
        <p class="dur"><i class="fas fa-clock"></i> Duration: 3-6 Months</p>
        <ul class="crs-list">
          <li><i class="fas fa-check-circle"></i> Complete Color &amp; Skin Theory</li>
          <li><i class="fas fa-check-circle"></i> Advanced Bridal &amp; HD Makeup</li>
          <li><i class="fas fa-check-circle"></i> Signature Airbrush Techniques</li>
          <li><i class="fas fa-check-circle"></i> Party, Engagement &amp; Editorial Looks</li>
        </ul>
        <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20for%20the%20Makeup%20Artistry%20Course." target="_blank" class="crs-wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp</a>
      </div>
    </div>
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="200">
      <div class="crs-card-img"><img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?w=500&q=80" alt="Hair Course"></div>
      <div class="crs-body-premium">
        <h4>Hair Styling Mastery</h4>
        <div class="specialist-badge"><i class="fas fa-cut"></i> Advanced Cuts, Spa &amp; Chemicals</div>
        <p class="dur"><i class="fas fa-clock"></i> Duration: 2-4 Months</p>
        <ul class="crs-list">
          <li><i class="fas fa-check-circle"></i> Hair Science &amp; Deep Treatments</li>
          <li><i class="fas fa-check-circle"></i> Chemical Work (Keratin, Smoothening)</li>
          <li><i class="fas fa-check-circle"></i> Global Hair Coloring &amp; Highlights</li>
          <li><i class="fas fa-check-circle"></i> Premium Bridal Updos &amp; Styling</li>
        </ul>
        <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20for%20the%20Hair%20Styling%20Course." target="_blank" class="crs-wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp</a>
      </div>
    </div>
    <div class="crs-card-3d" data-aos="fade-up" data-aos-delay="300">
      <div class="crs-card-img"><div class="crs-tag" style="background:var(--gold);color:#111;">ALL-IN-ONE</div><img src="https://images.unsplash.com/photo-1560066984-138dadb4c035?w=800&q=80" alt="Cosmetology Course"></div>
      <div class="crs-body-premium">
        <h4>Cosmetology Diploma</h4>
        <div class="specialist-badge"><i class="fas fa-spa"></i> Complete Hair, Skin &amp; Nails Training</div>
        <p class="dur"><i class="fas fa-clock"></i> Duration: 6-12 Months</p>
        <ul class="crs-list">
          <li><i class="fas fa-check-circle"></i> Advanced Skin Aesthetics &amp; Facials</li>
          <li><i class="fas fa-check-circle"></i> Complete Hair Cutting &amp; Chemical Work</li>
          <li><i class="fas fa-check-circle"></i> Nail Art, Extensions &amp; Acrylics</li>
          <li><i class="fas fa-check-circle"></i> Salon Management &amp; Client Handling</li>
        </ul>
        <a href="https://wa.me/918603388406?text=Hi%2C%20I%20want%20details%20for%20the%20Cosmetology%20Course." target="_blank" class="crs-wa-btn"><i class="fab fa-whatsapp"></i> WhatsApp</a>
      </div>
    </div>
  </div>
</div>
</section>

<!-- --- ABOUT FULL 3D --- -->
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
</section>

<!-- --- SERVICES --- -->
<section class="services" id="services">
<div class="container">
  <div class="sec-title">
    <h2>Our Premium <span>Services</span></h2>
    <div class="deco"><div class="line"></div><i class="fas fa-diamond"></i><div class="line"></div></div>
    <p>From stunning bridal transformations to rejuvenating skin therapies � experience luxury beauty services at Studio S.</p>
  </div>
  <div class="srv-grid">
    <div class="srv-card" data-aos="fade-up" data-aos-delay="50"><div class="srv-img"><img src="https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=300&q=80" alt="Bridal Makeup"></div><h4>Bridal Makeup</h4><p>HD, Airbrush &amp; Party</p></div>
    <div class="srv-card" data-aos="fade-up" data-aos-delay="100"><div class="srv-img"><img src="https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=300&q=80" alt="Skin Care"></div><h4>Skin Care</h4><p>Facial, Cleanup &amp; Treatments</p></div>
    <div class="srv-card" data-aos="fade-up" data-aos-delay="150"><div class="srv-img"><img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?w=300&q=80" alt="Hair"></div><h4>Hair Styling</h4><p>Haircut, Spa &amp; Chemical Work</p></div>
    <div class="srv-card" data-aos="fade-up" data-aos-delay="200"><div class="srv-img"><img src="https://images.unsplash.com/photo-1604654894610-df63bc536371?w=300&q=80" alt="Nails"></div><h4>Nails</h4><p>Manicure, Pedicure, Nail Art &amp; Extension</p></div>
    <div class="srv-card" data-aos="fade-up" data-aos-delay="250"><div class="srv-img"><img src="https://images.unsplash.com/photo-1583001931096-959e9a854654?w=300&q=80" alt="Lashes"></div><h4>Lash Extensions</h4><p>Professional Eyelash Extensions</p></div>
  </div>
</div>
</section>

<!-- --- WHY CHOOSE US --- -->
<section class="why">
<div class="container">
  <div class="why-grid">
    <div class="why-img" data-aos="fade-right"><img src="https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=700&q=80" alt="Sabla Singh Academy"></div>
    <div class="why-content" data-aos="fade-left" data-aos-delay="100">
      <h2>Why Choose <span>Sabla Singh Academy?</span></h2>
      <p>With 5+ years of excellence, we are Jharkhand's premier beauty destination. Whether you're a bride-to-be or an aspiring makeup artist, we deliver nothing but perfection.</p>
      <div class="why-list">
        <div class="why-item"><div class="why-icon"><i class="fas fa-award"></i></div><p><strong>5+ Years Experience</strong>Trusted by thousands of brides</p></div>
        <div class="why-item"><div class="why-icon"><i class="fas fa-certificate"></i></div><p><strong>Certified Courses</strong>Industry-recognized certificates</p></div>
        <div class="why-item"><div class="why-icon"><i class="fas fa-users"></i></div><p><strong>Expert Trainers</strong>Learn from industry professionals</p></div>
        <div class="why-item"><div class="why-icon"><i class="fas fa-star"></i></div><p><strong>Premium Products</strong>Top-tier international brands only</p></div>
      </div>
      <a href="contact.html" class="ab-btn">Enquire Now <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>
</div>
</section>

<!-- --- STATS BAR --- -->
<section class="stats">
<div class="container">
  <div class="stat-box" data-aos="zoom-in" data-aos-delay="50"><div class="number"><span class="counter" data-count="5">0</span><sup>+</sup></div><div class="text">Years of Excellence</div></div>
  <div class="stat-box" data-aos="zoom-in" data-aos-delay="100"><div class="number"><span class="counter" data-count="500">0</span><sup>+</sup></div><div class="text">Happy Customers</div></div>
  <div class="stat-box" data-aos="zoom-in" data-aos-delay="150"><div class="number"><span class="counter" data-count="200">0</span><sup>+</sup></div><div class="text">Students Enrolled</div></div>
  <div class="stat-box" data-aos="zoom-in" data-aos-delay="200"><div class="number"><span class="counter" data-count="15">0</span><sup>+</sup></div><div class="text">Expert Trainers</div></div>
</div>
</section>

<!-- --- CTA --- -->
<section class="cta">
<div class="container">
  <div class="cta-left"><h2>Ready to Transform<br>Your Beauty or<br>Build Your Career?</h2></div>
  <p class="cta-mid">Book your appointment or enroll in our professional beauty courses today!</p>
  <div class="cta-btns">
    <a href="https://wa.me/918603388406" target="_blank" class="cta-btn cta-btn-gold">Book Appointment</a>
    <a href="contact.html" class="cta-btn cta-btn-outline">Enquire Now <i class="fas fa-arrow-right" style="margin-left:5px"></i></a>
  </div>
</div>
</section>
"""

# Extract the footer part from footer_html
# Build complete index
index_final = index_html + "\n<body>\n" + body_content + "\n" + footer_html

# Actually, courses.html already has a complete structure, let me just replace the body content
# Extract from after <body> to before <footer in courses.html
body_start_tag = courses.find("<body>") + 6
body_before_footer = courses[:footer_start]
after_body_start = courses[body_start_tag:footer_start]

# Get the topbar+navbar+mobile menu+side buttons from courses.html
# These should be the first elements
side_btns_end = after_body_start.find("</div>", after_body_start.find("side-btns")) + 6

header_nav_part = after_body_start[:side_btns_end]

# Build index.html
final_index = courses[:courses.find("<body>") + 6] + "\n" + header_nav_part + "\n" + body_content + "\n" + footer_html

with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_index)

print("index.html rebuilt cleanly!")

