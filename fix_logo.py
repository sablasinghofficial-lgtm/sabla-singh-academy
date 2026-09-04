import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('logo.jpg', 'logo.png')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Logo updated to .png in HTML files")
