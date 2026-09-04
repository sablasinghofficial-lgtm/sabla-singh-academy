from PIL import Image

img = Image.open('logo.png')
img = img.convert('RGBA')
data = img.getdata()

new_data = []
for item in data:
    r, g, b, a = item
    # If pixel is very dark (almost black), make it transparent
    if r < 30 and g < 30 and b < 30:
        new_data.append((0, 0, 0, 0))
    else:
        new_data.append(item)
        
img.putdata(new_data)
img.save('logo.png', 'PNG')
print("Black background removed successfully!")
