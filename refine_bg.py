from PIL import Image
import numpy as np
from scipy.ndimage import binary_dilation, binary_erosion

# Start fresh from uploaded original
src = "C:/Users/mathu/.gemini/antigravity/brain/b8b47f7a-f90b-44bf-8cc4-ec63857eecd5/.user_uploaded/media_1788438157942.png"
img = Image.open(src).convert("RGBA")
data = np.array(img)

r = data[:,:,0].astype(float)
g = data[:,:,1].astype(float)
b = data[:,:,2].astype(float)

# Background is (10,28,64) navy - detect all similar pixels
# Use Euclidean distance from background color
bg_r, bg_g, bg_b = 12, 28, 64
dist = np.sqrt((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)

# Strict background: very close to navy (threshold=35)
strict_bg = dist < 35
# Medium background: somewhat close (threshold=55) - these become semi-transparent
medium_bg = (dist >= 35) & (dist < 60)

result = data.copy()
result[strict_bg, 3] = 0          # Fully transparent
result[medium_bg, 3] = (result[medium_bg, 3] * 0.25).astype(np.uint8)  # Very faint

out = Image.fromarray(result)
out.save("logo.png", "PNG")
print("Logo background removed precisely!")
print(f"Total pixels: {data.shape[0]*data.shape[1]}")
print(f"Transparent pixels: {strict_bg.sum()}")
