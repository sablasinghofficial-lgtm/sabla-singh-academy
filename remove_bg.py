from PIL import Image
import numpy as np

# Reload original uploaded file
img = Image.open("logo.png").convert("RGBA")
data = np.array(img, dtype=np.float64)

r = data[:,:,0]
g = data[:,:,1]  
b = data[:,:,2]

# Navy blue background is approx (10-40, 20-55, 80-130)
# Use flood-fill style: detect bg color from corners
# Sample corner pixels to get exact bg color
corners = [
    img.getpixel((0, 0)),
    img.getpixel((10, 10)),
    img.getpixel((img.width-1, 0)),
    img.getpixel((0, img.height-1)),
    img.getpixel((img.width-1, img.height-1)),
]
print("Corner colors:", corners)

# Target bg: dark navy blue range
# Make mask: pixels similar to navy background
# Navy: R~15-45, G~25-60, B~80-130
mask = (
    (r < 65) & (g < 75) & (b > 65) & (b < 145) |  # Navy blue range
    (r < 20) & (g < 20) & (b < 50)  # Very dark / near black
)

# Apply with smooth edges using alpha feathering
data_uint8 = np.array(img)
data_uint8[mask, 3] = 0  # Fully transparent

# Also semi-transparent edge pixels (anti-aliasing)
# Find edge pixels - neighbors of mask
from scipy.ndimage import binary_dilation
dilated = binary_dilation(mask, iterations=2)
edge_mask = dilated & ~mask
# Make edge pixels semi-transparent for smooth look
data_uint8[edge_mask, 3] = (data_uint8[edge_mask, 3] * 0.3).astype(np.uint8)

result = Image.fromarray(data_uint8)
result.save("logo.png", "PNG")
print("Transparency done with smooth edges!")
