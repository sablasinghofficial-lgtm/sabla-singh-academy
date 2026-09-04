import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace "WhatsApp for Syllabus" with "WhatsApp"
    new_html = html.replace('WhatsApp for Syllabus', 'WhatsApp')

    if html != new_html:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Updated {file}")

print("Done!")
