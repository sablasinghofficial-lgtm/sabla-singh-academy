# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

extra_css = """
/* Hero Slideshow CSS */
.hero { background: transparent !important; } /* override old bg */
.hero-slideshow {
  position: absolute; inset: 0; z-index: 0;
  width: 100%; height: 100%; overflow: hidden;
}
.hero-slide {
  position: absolute; inset: 0;
  width: 100%; height: 100%;
  background-size: cover;
  background-position: center top;
  opacity: 0;
  animation: heroFade 15s infinite;
}
.hero-slide.slide-1 {
  background-image: url('gal16.jpg'); /* Beautiful orange lehenga */
  animation-delay: 0s;
}
.hero-slide.slide-2 {
  background-image: url('gal7.jpg'); /* Full bridal maroon */
  animation-delay: 5s;
}
.hero-slide.slide-3 {
  background-image: url('gal17.jpg'); /* Bridal eyes closed */
  animation-delay: 10s;
}

@keyframes heroFade {
  0% { opacity: 0; transform: scale(1.05); }
  10% { opacity: 1; transform: scale(1); }
  33% { opacity: 1; transform: scale(1); }
  43% { opacity: 0; transform: scale(1.05); }
  100% { opacity: 0; transform: scale(1.05); }
}

.hero-overlay { z-index: 1; }
"""

# Let's also make sure global font size wasn't accidentally shrunk.
# I'll just append html, body { font-size: 16px !important; } to guarantee it.
# Actually, rem values are based on html font-size. Browsers default to 16px. 
# If someone pressed Ctrl+Minus, the browser shrinks it. We can't override browser zoom,
# but we can ensure it's standard 16px.
extra_css += """
html { font-size: 16px; }
"""

css = css + "\n" + extra_css

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Hero CSS and Slider added!")
