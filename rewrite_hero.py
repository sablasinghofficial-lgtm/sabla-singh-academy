with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find and replace the hero section completely
start = html.find("<!-- --- HERO --- -->")
end = html.find("<!-- --- ABOUT + COURSES SPLIT --- -->")
if start == -1:
    start = html.find("<!-- --- COURSES FULL --- -->")
    end = start

hero_new = """<!-- --- HERO --- -->
<section class="hero" id="home">
<div class="container">
  <div class="hero-left" data-aos="fade-right" data-aos-duration="1000">
    <div class="hero-badge">? Ranchi's Most Trusted Beauty &amp; Academy</div>
    <span class="hero-script">Unleash Your Beauty</span>
    <h1>Empower<br><span>Your Future</span></h1>
    <p class="hero-desc">Specialist in <strong style="color:var(--gold)">Bridal HD &amp; Airbrush Makeup</strong>. Offering premium beauty services &amp; professional courses in Ranchi.</p>
    <div class="hero-services-row">
      <span>Makeup</span><span>Skin</span><span>Hair</span><span>Nails</span><span>Lashes</span>
    </div>
    <div class="hero-btns">
      <a href="https://wa.me/918603388406" target="_blank" class="hbtn hbtn-wa"><i class="fab fa-whatsapp"></i> WhatsApp Us</a>
      <a href="courses.html" class="hbtn hbtn-outline">Explore Courses <i class="fas fa-arrow-right"></i></a>
    </div>
    <div class="hero-stats">
      <div class="h-stat"><div class="icon"><i class="fas fa-award"></i></div><div class="num"><span class="counter" data-count="5">0</span><sup>+</sup></div><div class="lbl">Years of Excellence</div></div>
      <div class="h-stat"><div class="icon"><i class="fas fa-heart"></i></div><div class="num"><span class="counter" data-count="500">0</span><sup>+</sup></div><div class="lbl">Happy Customers</div></div>
      <div class="h-stat"><div class="icon"><i class="fas fa-graduation-cap"></i></div><div class="num"><span class="counter" data-count="200">0</span><sup>+</sup></div><div class="lbl">Students Enrolled</div></div>
    </div>
  </div>
</div>
</section>

"""

end2 = html.find("<!-- --- ABOUT + COURSES SPLIT --- -->")
if end2 == -1:
    end2 = html.find("<!-- --- COURSES FULL --- -->")

if start != -1 and end2 != -1:
    html = html[:start] + hero_new + html[end2:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Hero rewritten!")
else:
    print("Could not find boundaries: start=%d, end=%d" % (start, end2))
