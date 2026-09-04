with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find the OLD hero at top of body (should be after navbar)
hero_old_start = html.find("<!-- --- HERO --- -->", 0, 5000)  # Only look in first 5000 chars
marquee_old_start = html.find("<!-- --- MARQUEE SERVICES --- -->", 0, 5000)

# Find the DUPLICATED hero sections lower in the file
hero_new_start = html.find("<!-- --- HERO --- -->", 300)  # Second occurrence
marquee_new_start = html.find("<!-- --- MARQUEE SERVICES --- -->", 300)

print(f"Hero positions: first={hero_old_start}, second={hero_new_start}")
print(f"Marquee positions: first={marquee_old_start}, second={marquee_new_start}")

# Check what we are working with
print("First 200 chars after first hero:", repr(html[hero_old_start:hero_old_start+200]))
