# -*- coding: utf-8 -*-
import glob
import re

# 1. Clean up the messy inline styles from the HTML files for the About section
for html_file in ["index.html", "about.html"]:
    with open(html_file, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()

    # Remove inline styles from apm-courses-box and its children
    html = re.sub(r'<div class="apm-courses-box" style="[^"]+">', r'<div class="apm-courses-box">', html)
    html = re.sub(r'<h4 style="[^"]+">Our Professional Courses:</h4>', r'<h4>Our Professional Courses:</h4>', html)
    html = re.sub(r'<div class="apm-features" style="[^"]+">', r'<div class="apm-features">', html)
    html = re.sub(r'<div class="apm-feat" style="[^"]+">', r'<div class="apm-feat">', html)
    html = re.sub(r'<i class="fas([^"]+)" style="[^"]+"></i>', r'<i class="fas\1"></i>', html)
    html = re.sub(r'<span style="[^"]+"><strong>(.*?)</strong><br><small style="[^"]+">(.*?)</small></span>', r'<span><strong>\1</strong><br><small>\2</small></span>', html)
    
    # Signature inline fix
    html = re.sub(r'<div class="apm-sig-name" style="[^"]+">Sabla Singh</div>', r'<div class="apm-sig-name">Sabla Singh</div>', html)
    html = re.sub(r'<div class="apm-sig-role" style="[^"]+">Founder & Director.*?</div>', r'<div class="apm-sig-role">Founder & Director, Sabla Singh Academy</div>', html)

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)

print("HTML inline styles cleaned up!")
