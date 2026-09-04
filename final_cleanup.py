with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Find the new hero section (the full premium one with hero-overlay)  
hero_start = content.find("<!-- --- HERO --- -->")
if hero_start == -1:
    hero_start = content.find("<!-- --- HERO --- -->")

print(f"Premium hero found at: {hero_start}")
print("Around it:", repr(content[hero_start:hero_start+100]))

# Check marquee
mq = content.find("marquee-bar")
print(f"Marquee at: {mq}")

# Check side-btns end
sb_end = content.find("</div>", content.find("class=\"side-btns\""))
print(f"Side-btns </div> at: {sb_end}")

# Get content before side-btns end (navbar+topbar+side-btns)
pre_hero = content[:sb_end + 6]
# Get everything from hero onwards
at_hero = content[hero_start:]

new_content = pre_hero + "\n\n" + at_hero

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Done!")
