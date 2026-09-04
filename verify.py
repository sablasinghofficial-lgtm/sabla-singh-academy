with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

markers = [
    ("<nav class=", "Navbar"),
    ("side-btns", "Side Buttons"),
    ("class=\"hero\"", "Hero"),
    ("hero-overlay", "Hero Overlay"),
    ("typewriter", "Typewriter"),
    ("marquee-bar", "Marquee"),
    ("courses-full", "Courses"),
    ("about-full", "About"),
    ("class=\"services\"", "Services"),
    ("class=\"stats\"", "Stats"),
    ("class=\"footer\"", "Footer"),
    ("</html>", "HTML End"),
]
for pattern, name in markers:
    pos = html.find(pattern)
    print(f"  {pos:6d} | {name}")
