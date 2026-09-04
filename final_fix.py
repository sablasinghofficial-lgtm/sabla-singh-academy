with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# The new hero got appended AFTER </html> - we need to cut it out and put it in the right place

# Find where body ends (before scripts)
scripts_start = content.find('<script src="https://cdn.jsdelivr.net/npm/swiper')

# Find where the misplaced hero starts (after </html>)
hero_block_start = content.find("</html>") 
hero_block = content[hero_block_start + len("</html>"):]  # Everything after </html>

# Clean body content (before </html>)
body_before_close = content[:hero_block_start]

# Find the SIDE BUTTONS section end in body to know where to insert hero
side_btns_end = body_before_close.rfind("</div>\n\n<!-- --- COURSES")
if side_btns_end == -1:
    side_btns_end = body_before_close.rfind("</div>\n<!-- --- COURSES")
if side_btns_end == -1:
    side_btns_end = body_before_close.rfind("</div>\n\n<!-- --- COURSES")

# Find where courses section starts
courses_idx = body_before_close.find("<!-- --- COURSES FULL --- -->")
if courses_idx == -1:
    courses_idx = body_before_close.find("<!-- --- COURSES")

print(f"side_btns_end={side_btns_end}, courses_idx={courses_idx}")
print(f"hero_block length={len(hero_block)}")

# Strategy: insert hero_block BEFORE courses section
side_div_close = body_before_close.rfind("</div>", 0, courses_idx)

new_content = (
    body_before_close[:side_div_close + 6] + "\n\n" +
    hero_block +
    "\n" +
    body_before_close[side_div_close + 6:] +
    "\n</html>"
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done!")
