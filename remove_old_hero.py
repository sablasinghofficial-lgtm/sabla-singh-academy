with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# There are 2 hero sections - line 88 is old, line 111 is new
# Find the first one (old) and remove it
first_hero = content.find('<section class="hero" id="home">')
second_hero = content.find('<section class="hero" id="home">', first_hero + 10)

print(f"First hero at: {first_hero}, Second hero at: {second_hero}")

if second_hero != -1:
    # Remove from first_hero to just before second_hero
    # But we need to remove the entire first section including </section>
    first_section_end = content.find("</section>", first_hero) + 10
    print(f"First section ends at: {first_section_end}")
    print("First section content:", repr(content[first_hero:first_section_end]))
    
    # Remove first hero
    content = content[:first_hero] + "\n" + content[first_section_end:]
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Old hero removed!")
else:
    print("No duplicate found")
