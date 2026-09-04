with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Check where the side-btns section ends and where hero starts
side_end = content.find("</div>\n\n<!-- --- HERO --- -->")
if side_end == -1:
    side_end = content.find("</div>\n<!-- --- HERO --- -->")

hero_start = content.find("<!-- --- HERO --- -->")
courses_start = content.find("<!-- --- ABOUT + COURSES SPLIT --- -->")
if courses_start == -1:
    courses_start = content.find("<!-- --- COURSES FULL --- -->")

print(f"hero_start={hero_start}, courses_start={courses_start}")
print("Around hero_start:", repr(content[hero_start-50:hero_start+100]))
