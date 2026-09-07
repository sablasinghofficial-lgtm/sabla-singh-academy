import os
import re

files = ['index.html', 'courses.html', 'services.html', 'about.html', 'gallery.html', 'vlogs.html', 'contact.html']

for fname in files:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace 5+ Years Excellence -> 20+ Years Excellence
        content = content.replace('5+ Years Excellence', '20+ Years Excellence')
        
        # Replace 5+ Years Experience -> 20+ Years Experience
        content = content.replace('5+ Years Experience', '20+ Years Experience')
        
        # Replace Trusted by 500+ -> Trusted by 2500+ (in the ticker)
        content = content.replace('Trusted by 500+', 'Trusted by 2500+')
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname}")

print("All done!")
