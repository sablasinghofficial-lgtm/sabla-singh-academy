from PIL import Image

img = Image.open('logo.png')
img = img.convert('RGBA')
data = img.getdata()

dark_pixels = 0
gold_pixels = 0
for item in data:
    if item[3] > 0: # not transparent
        r, g, b = item[:3]
        if r < 100 and g < 100 and b < 100:
            dark_pixels += 1
        elif r > 150 and g > 100 and b < 100:
            gold_pixels += 1

print(f"Dark pixels: {dark_pixels}, Gold pixels: {gold_pixels}")
