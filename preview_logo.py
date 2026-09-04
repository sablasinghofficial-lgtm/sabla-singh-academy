from PIL import Image, ImageDraw
import numpy as np

# Create a white preview and a dark preview to check transparency
logo = Image.open("logo.png").convert("RGBA")

# White background preview
white_bg = Image.new("RGBA", logo.size, (255,255,255,255))
white_preview = Image.alpha_composite(white_bg, logo)
white_preview.convert("RGB").save("logo_preview_white.jpg", "JPEG", quality=92)

# Gold/cream background preview  
cream_bg = Image.new("RGBA", logo.size, (245,235,210,255))
cream_preview = Image.alpha_composite(cream_bg, logo)
cream_preview.convert("RGB").save("logo_preview_cream.jpg", "JPEG", quality=92)

print("Preview images saved!")
print(f"Logo size: {logo.size}")
