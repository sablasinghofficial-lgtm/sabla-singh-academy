# -*- coding: utf-8 -*-
with open("gallery.html", "r", encoding="utf-8") as f:
    html = f.read()

# Locate the entire sec-title block and remove it
import re
start_marker = '<div class="sec-title" data-aos="fade-up">'
end_marker = '</div>' # The closing div for sec-title

start_idx = html.find(start_marker)
if start_idx != -1:
    # Need to find the correct closing div for sec-title
    # It contains <h2>...</h2> \n <div class="deco">...</div>
    # A simple regex or string replacement will work since we know the structure
    block_to_remove = """<div class="sec-title" data-aos="fade-up">
    <h2>Our <span>Portfolio</span></h2>
    <div class="deco"><div class="line"></div><i class="fas fa-camera"></i><div class="line"></div></div>
    
  </div>"""
    
    html = html.replace(block_to_remove, "")
    
    with open("gallery.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Portfolio title removed successfully!")
else:
    print("Could not find sec-title")
