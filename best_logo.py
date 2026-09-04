from PIL import Image
import numpy as np

src = "C:/Users/mathu/.gemini/antigravity/brain/b8b47f7a-f90b-44bf-8cc4-ec63857eecd5/.user_uploaded/media_1788438157942.png"
img = Image.open(src).convert("RGBA")
data = np.array(img)

r = data[:,:,0].astype(float)
g = data[:,:,1].astype(float)
b = data[:,:,2].astype(float)

bg_r, bg_g, bg_b = 12, 28, 64

# The issue: logo artwork also has dark colors (navy shades near bg)
# So we keep pixels that are:
# - Gold/yellow tones: r>100, g>80, b<80
# - Magenta/pink tones: r>80, b>50, g<60
# - White/bright text: r>150, g>150, b>150
# Everything else close to bg -> transparent

dist = np.sqrt((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)

# "Logo" pixels: gold, magenta, bright
is_gold = (r > 120) & (g > 90) & (b < 90)
is_magenta = (r > 100) & (b > 60) & (g < r - 20)
is_bright = (r > 140) & (g > 140) & (b > 120)
is_logo = is_gold | is_magenta | is_bright

# Background = not logo AND close to navy
is_bg = ~is_logo & (dist < 55)

result = data.copy()
result[is_bg, 3] = 0

out = Image.fromarray(result)
out.save("logo.png", "PNG")
data2 = np.array(out)
transparent = (data2[:,:,3] == 0).sum()
opaque = (data2[:,:,3] > 200).sum()
print(f"Transparent: {transparent} ({transparent*100//(1024*1024)}%)")
print(f"Opaque logo pixels: {opaque} ({opaque*100//(1024*1024)}%)")
print("Done!")
