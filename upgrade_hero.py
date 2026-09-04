with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find hero section and replace completely
start = html.find("<!-- --- HERO --- -->")
end = html.find("<!-- --- ABOUT + COURSES SPLIT --- -->")
if end == -1:
    end = html.find("<!-- --- COURSES FULL --- -->")

new_hero = """<!-- --- HERO --- -->
<section class="hero" id="home">
  <!-- Background overlay for readability -->
  <div class="hero-overlay"></div>
  
  <!-- Left Text Content -->
  <div class="hero-content" data-aos="fade-right" data-aos-duration="1000">
    <p class="hero-tagline">? Ranchi's Most Trusted Beauty &amp; Academy ?</p>
    <h3 class="hero-sub">Where Beauty Meets</h3>
    <h1 class="hero-main">
      <span class="typewriter-wrap" id="typewriter">CONFIDENCE</span>
    </h1>
    <h2 class="hero-meet">Meets <em>Career</em></h2>
    <div class="hero-academy-name">SABLA SINGH ACADEMY</div>
    <p class="hero-brief">Your Premier Destination for Beauty,<br>Wellness &amp; Professional Training</p>
    <div class="hero-trust">
      <div class="trust-icon">
        <i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i><i class="fas fa-star"></i>
      </div>
      <p class="trust-text">Trusted by <strong>500+</strong> Happy Members</p>
    </div>
    <div class="hero-cta-row">
      <a href="https://wa.me/918603388406" target="_blank" class="hero-btn-wa"><i class="fab fa-whatsapp"></i> Book Now on WhatsApp</a>
      <a href="courses.html" class="hero-btn-outline">Explore Courses <i class="fas fa-arrow-right"></i></a>
    </div>
  </div>

  <!-- Right Image Panel -->
  <div class="hero-img-panel" data-aos="fade-left" data-aos-duration="1100">
    <div class="hero-img-frame">
      <div class="hero-badge-float">5<sup>+</sup><span>Yrs</span></div>
    </div>
    <!-- Mini stats column -->
    <div class="hero-mini-stats">
      <div class="mini-stat">
        <i class="fas fa-award"></i>
        <span class="mini-num"><span class="counter" data-count="5">0</span>+ Years</span>
        <span class="mini-lbl">Excellence</span>
      </div>
      <div class="mini-stat">
        <i class="fas fa-heart"></i>
        <span class="mini-num"><span class="counter" data-count="500">0</span>+</span>
        <span class="mini-lbl">Happy Clients</span>
      </div>
      <div class="mini-stat">
        <i class="fas fa-graduation-cap"></i>
        <span class="mini-num"><span class="counter" data-count="200">0</span>+</span>
        <span class="mini-lbl">Students</span>
      </div>
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
    <span><i class="fas fa-diamond"></i> Manicure</span>
    <span><i class="fas fa-diamond"></i> Pedicure</span>
    <span><i class="fas fa-diamond"></i> Lash Extension</span>
    <span><i class="fas fa-diamond"></i> Makeup Course</span>
    <span><i class="fas fa-diamond"></i> Hair Styling Course</span>
    <span><i class="fas fa-diamond"></i> Cosmetology Diploma</span>
    <!-- Duplicate for seamless loop -->
    <span><i class="fas fa-diamond"></i> Bridal Makeup</span>
    <span><i class="fas fa-diamond"></i> HD Makeup</span>
    <span><i class="fas fa-diamond"></i> Airbrush Makeup</span>
    <span><i class="fas fa-diamond"></i> Party Makeup</span>
    <span><i class="fas fa-diamond"></i> Skin Facial</span>
    <span><i class="fas fa-diamond"></i> Hair Spa</span>
    <span><i class="fas fa-diamond"></i> Nail Art</span>
    <span><i class="fas fa-diamond"></i> Lash Extension</span>
  </div>
</div>

"""

html = html[:start] + new_hero + html[end:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Hero upgraded!")
