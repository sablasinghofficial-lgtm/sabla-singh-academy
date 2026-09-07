with open('courses.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace course 1 image (Makeup Artistry) - currently uses gal15 or similar
import re

# Replace the first course card image (Advanced Makeup Artistry)
content = re.sub(
    r'(<div class="crs-card-3d"[^>]*>[\s\S]*?MOST POPULAR[\s\S]*?<img src=")[^"]*(")',
    r'\1course_makeup.jpg\2',
    content, count=1
)

# Replace the cosmetology course image (gal15)
content = content.replace('<img src="gal15.jpg" alt="Cosmetology Course">', '<img src="course_cosmetology.jpg" alt="Cosmetology Course">')

with open('courses.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Updated course images.")
