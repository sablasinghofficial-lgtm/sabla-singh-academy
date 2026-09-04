import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update text mentions
    html = html.replace('20+ years', '5+ years')
    html = html.replace('20+ Years', '5+ Years')
    html = html.replace('two decades', '5 successful years')
    html = html.replace('data-count="20"', 'data-count="5"')
    html = html.replace('data-count="5000"', 'data-count="500"')
    html = html.replace('data-count="1000"', 'data-count="200"')
    html = html.replace('Happy Clients', 'Happy Customers')
    html = html.replace('Students Trained', 'Students Enrolled')
    
    # Update the big badge in about section
    html = html.replace('<div class="big">20<sup>+</sup></div>', '<div class="big">5<sup>+</sup></div>')

    # 2. Remove Placement Support stat blocks
    # In hero section stats
    html = re.sub(r'<div class="h-stat"><div class="icon"><i class="fas fa-thumbs-up"></i></div><div class="num"><span class="counter" data-count="100">0</span><sup>%</sup></div><div class="lbl">Placement Support</div></div>', '', html)
    
    # In stats bar section
    html = re.sub(r'<div class="stat-box" [^>]+><div class="number"><span class="counter" data-count="100">0</span><sup>%</sup></div><div class="text">Placement Support</div></div>', '', html)

    # 3. Remove Placement support from features/why choose us
    html = re.sub(r'<div class="ab-check"><i class="fas fa-check"></i> 100% Placement Assistance</div>', '', html)
    html = re.sub(r'<div class="why-item"><div class="why-icon"><i class="fas fa-briefcase"></i></div><p><strong>Placement Support</strong>100% job placement assistance</p></div>', '', html)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Stats updated successfully!")
