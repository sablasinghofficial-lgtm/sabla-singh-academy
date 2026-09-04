from PIL import Image
import numpy as np

src = "C:/Users/mathu/.gemini/antigravity/brain/b8b47f7a-f90b-44bf-8cc4-ec63857eecd5/.user_uploaded/media_1788438157942.png"
img = Image.open(src).convert("RGBA")
data = np.array(img)

r = data[:,:,0].astype(float)
g = data[:,:,1].astype(float)
b = data[:,:,2].astype(float)

# Background navy = (10-14, 27-30, 63-66)
bg_r, bg_g, bg_b = 12, 28, 64
dist = np.sqrt((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)

# Only remove pixels very close to the navy BG color (tight threshold=28)
# Keep all pixels that are part of logo artwork
strict_bg = dist < 28

result = data.copy()
result[strict_bg, 3] = 0   # Make background transparent

out = Image.fromarray(result)
out.save("logo.png", "PNG")

# Verify - sample the logo gold area  
out2 = Image.open("logo.png").convert("RGBA")
# Sample bottom text area (SABLA SINGH ACADEMY is around 75% down)
h, w = out2.size[1], out2.size[0]
sample = out2.getpixel((w//2, int(h*0.78)))
print(f"Logo text area pixel: {sample}")
print(f"Tight bg removal done. transparent={strict_bg.sum()} of {data.shape[0]*data.shape[1]}")
