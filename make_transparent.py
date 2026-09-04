from PIL import Image
import numpy as np

img = Image.open("logo.png").convert("RGBA")
data = np.array(img)

r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

# The background is dark navy blue: approx R<50, G<60, B>90 (dark blue range)
dark_blue_mask = (r < 60) & (g < 70) & (b > 70) & (b < 180)

# Also catch near-black pixels that are part of background
very_dark_mask = (r < 30) & (g < 30) & (b < 60)

# Combine masks
bg_mask = dark_blue_mask | very_dark_mask

# Make background fully transparent
data[bg_mask, 3] = 0

result = Image.fromarray(data)
result.save("logo.png", "PNG")
print("Background removed! Transparent PNG saved.")
