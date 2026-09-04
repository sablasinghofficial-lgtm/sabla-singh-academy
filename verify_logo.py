from PIL import Image
img = Image.open("logo.png").convert("RGBA")
data = list(img.getdata())
transparent = sum(1 for p in data if p[3] == 0)
opaque = sum(1 for p in data if p[3] > 200)
print(f"Image size: {img.size}")
print(f"Transparent pixels: {transparent} ({transparent*100//len(data)}%)")
print(f"Opaque pixels: {opaque} ({opaque*100//len(data)}%)")
# Sample a gold pixel and magenta pixel
# center of image should have gold
cx, cy = img.size[0]//2, img.size[1]//3
print(f"Center-top pixel (should be gold): {img.getpixel((cx, cy))}")
