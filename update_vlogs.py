# -*- coding: utf-8 -*-
with open("vlogs.html", "r", encoding="utf-8") as f:
    html = f.read()

import re

# Remove page header
start_ph = html.find('<!-- --- PAGE HEADER --- -->')
if start_ph == -1:
    start_ph = html.find('<!-- --- PAGE HEADER --- -->')
if start_ph == -1:
    start_ph = html.find('<section class="page-header">')

end_ph = html.find('<!-- --- VLOGS --- -->')
if end_ph == -1:
    end_ph = html.find('<!-- --- VLOGS --- -->')
if end_ph == -1:
    end_ph = html.find('<section class="vlogs"')

if start_ph != -1 and end_ph != -1:
    html = html[:start_ph] + html[end_ph:]

# Replace Vlogs Section
start_v = html.find('<section class="vlogs"')
end_v = html.find('<!-- --- CTA --- -->')
if end_v == -1:
    end_v = html.find('<!-- --- CTA --- -->')
if end_v == -1:
    end_v = html.find('<section class="cta">')

new_vlogs = """<!-- --- PREMIUM VLOGS --- -->
<section class="vlogs-premium" id="vlogs">
<div class="container">
  <div class="sec-title" data-aos="fade-up" style="margin-bottom: 60px;">
    <h2>Exclusive <span>Vlogs</span></h2>
    <div class="deco"><div class="line"></div><i class="fas fa-video"></i><div class="line"></div></div>
    <p style="text-align:center; max-width:600px; margin:0 auto; color:rgba(255,255,255,0.7);">Experience the magic of Sabla Singh Academy. Watch our latest bridal transformations, masterclasses, and behind-the-scenes moments right here, or on our YouTube channel.</p>
  </div>
  
  <div class="vg-grid">
"""

titles = [
    "Bridal HD Makeup Transformation",
    "Airbrush Technique Masterclass",
    "Studio S Academy Tour",
    "Haldi Ceremony Soft Glam",
    "Engagement Makeup Tutorial",
    "Reception Party Look",
    "Student Portfolio Shoot",
    "Signature Bridal Avatar",
    "Flawless Base Makeup Hacks",
    "Pre-Wedding Skincare Routine"
]

for i in range(1, 11):
    vid_file = f"videos/sablasinghofficial-20260903-{i:04d}.mp4"
    title = titles[i-1]
    delay = (i % 3) * 100
    
    card = f"""
    <div class="vg-card" data-aos="fade-up" data-aos-delay="{delay}">
      <div class="vg-video-wrap">
        <video id="vid{i}" src="{vid_file}" preload="metadata" onplay="hideOverlay('vid{i}')" onpause="showOverlay('vid{i}')"></video>
        <div class="vg-overlay" id="overlay{i}" onclick="togglePlay('vid{i}')">
          <div class="vg-play-btn"><i class="fas fa-play"></i></div>
        </div>
      </div>
      <div class="vg-body">
        <h3>{title}</h3>
        <div class="vg-actions">
          <button class="vg-btn vg-watch" onclick="togglePlay('vid{i}')"><i class="fas fa-play-circle"></i> Play Video</button>
          <a href="https://youtube.com/@SablaSinghOfficial" target="_blank" class="vg-btn vg-yt"><i class="fab fa-youtube"></i> YouTube</a>
        </div>
      </div>
    </div>
"""
    new_vlogs += card

new_vlogs += """
  </div>
</div>
</section>

"""

if start_v != -1 and end_v != -1:
    html = html[:start_v] + new_vlogs + html[end_v:]
    with open("vlogs.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("vlogs.html completely updated!")
else:
    print("Could not find section markers for vlogs.")
