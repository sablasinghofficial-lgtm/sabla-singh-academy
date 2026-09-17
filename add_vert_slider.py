import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The block to replace
old_block = """      <div class="apm-img-wrap">
        <img src="founder.jpg" alt="Sabla Singh - Founder & Director">
        <div class="apm-corner apm-tl"></div>
        <div class="apm-corner apm-br"></div>
        
      </div>"""

new_block = """      <div class="apm-img-wrap swiper about-vert-slider" style="overflow: hidden; width: 100%; height: 100%;">
        <div class="swiper-wrapper">
          <div class="swiper-slide"><img src="gal16.jpg" alt="Makeup Academy" style="object-fit: cover; width: 100%; height: 100%;"></div>
          <div class="swiper-slide"><img src="gal14.jpg" alt="Bridal Makeup" style="object-fit: cover; width: 100%; height: 100%;"></div>
          <div class="swiper-slide"><img src="gal8.jpg" alt="Hair Styling" style="object-fit: cover; width: 100%; height: 100%;"></div>
          <div class="swiper-slide"><img src="gal9.jpg" alt="Cosmetology" style="object-fit: cover; width: 100%; height: 100%;"></div>
          <div class="swiper-slide"><img src="gal17.jpg" alt="Academy Class" style="object-fit: cover; width: 100%; height: 100%;"></div>
        </div>
        <div class="apm-corner apm-tl"></div>
        <div class="apm-corner apm-br"></div>
      </div>
      
      <script>
        document.addEventListener('DOMContentLoaded', function() {
          new Swiper('.about-vert-slider', {
            direction: 'vertical',
            loop: true,
            autoplay: {
              delay: 2000,
              disableOnInteraction: false,
            },
            effect: 'slide',
            speed: 800
          });
        });
      </script>"""

content = content.replace(old_block, new_block)

# Just in case there are subtle whitespace differences, try regex if not replaced
if old_block not in content and 'about-vert-slider' not in content:
    pattern = r'<div class="apm-img-wrap">\s*<img src="founder.jpg" alt="Sabla Singh - Founder & Director">\s*<div class="apm-corner apm-tl"></div>\s*<div class="apm-corner apm-br"></div>\s*</div>'
    content = re.sub(pattern, new_block, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html")
