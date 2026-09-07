from PIL import Image
import numpy as np

img = Image.open('logo_new.png').convert('RGBA')
data = np.array(img)

# Get RGB values
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

# Pixels that are near-black (background) -> make transparent
# Black background is roughly r<40, g<40, b<40
black_mask = (r < 50) & (g < 50) & (b < 50)

# Also remove very dark pixels near edges
data[black_mask, 3] = 0  # Set alpha to 0 (transparent)

result = Image.fromarray(data)
result.save('logo_transparent.png')
print("Done! Black background removed.")
