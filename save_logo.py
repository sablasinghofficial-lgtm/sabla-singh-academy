from PIL import Image
import numpy as np

src = "C:/Users/mathu/.gemini/antigravity/brain/b8b47f7a-f90b-44bf-8cc4-ec63857eecd5/sa_logo_new_1788439085143.jpg"
img = Image.open(src).convert("RGBA")
data = np.array(img)

r = data[:,:,0].astype(float)
g = data[:,:,1].astype(float)
b = data[:,:,2].astype(float)

# White background removal - pixels close to white (>230,>230,>230)
is_white_bg = (r > 230) & (g > 230) & (b > 230)
# Semi-white edge (anti-aliasing)
is_near_white = (r > 210) & (g > 210) & (b > 210) & ~is_white_bg

result = data.copy()
result[is_white_bg, 3] = 0
result[is_near_white, 3] = (result[is_near_white, 3] * 0.3).astype(np.uint8)

out = Image.fromarray(result)
out.save("logo.png", "PNG")
print(f"New logo saved! Transparent: {is_white_bg.sum()} pixels")
