from PIL import Image

img = Image.open('logo.png')
img = img.convert('RGBA')
data = img.getdata()

new_data = []
for item in data:
    if item[3] > 0: # not transparent
        r, g, b, a = item
        # If it's a dark pixel, invert it to white/off-white
        if r < 80 and g < 80 and b < 80:
            new_data.append((255, 255, 255, a))
        # If it's somewhat dark (anti-aliasing edges of the black text)
        elif r < 130 and g < 130 and b < 130:
            new_data.append((220, 220, 220, a))
        else:
            new_data.append(item)
    else:
        new_data.append(item)
        
img.putdata(new_data)
img.save('logo.png', 'PNG')
print("Dark pixels converted to white for dark theme!")
