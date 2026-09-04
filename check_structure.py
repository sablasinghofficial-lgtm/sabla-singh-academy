with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Check key markers in order
markers = [
    "<nav class=",
    "<div class=\"side-btns\"",
    "class=\"hero\"",
    "marquee-bar",
    "courses-full",
    "about-full",
    "</body>",
    "</html>"
]

for m in markers:
    pos = content.find(m)
    print(f"{pos:6d} | {m}")
