with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# There are 2 hero sections - remove the old one between lines 88-102
# The old one starts at the first <section class="hero" id="home">
# The new correct one starts with our new content
# Find first hero and second hero
first = html.find('<section class="hero" id="home">')
second = html.find('<section class="hero" id="home">', first + 10)

if second != -1:
    # The old hero goes from first to just before second
    # Remove from first to second (exclusive), keeping content from second onwards
    old_section_end = html.rfind('\n', 0, second)
    html = html[:first] + html[second:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Duplicate hero removed!")
else:
    print("No duplicate found")
