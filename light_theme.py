import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update CSS variables for Light Theme
new_vars = '''
:root {
  --gold: #C9951A; /* Classic luxury gold */
  --gold-l: #E8B946;
  --black: #ffffff; /* We swap black to white for backgrounds */
  --black2: #f9f7f2; /* Cream/off-white for secondary backgrounds */
  --black3: #ffffff; /* White for cards */
  --white: #222222; /* We swap white to dark grey for text */
  --gray: #666666;
  --hd: 'Playfair Display', serif;
  --sc: 'Great Vibes', cursive;
  --bd: 'Montserrat', sans-serif;
}
'''
css = re.sub(r':root \{[^\}]+\}', new_vars.strip(), css)

# Fix specific color issues caused by the swap
css = css.replace('color: #fff;', 'color: var(--white);')
css = css.replace('color: #ffffff;', 'color: var(--white);')
css = css.replace('color: rgba(255,255,255,', 'color: rgba(0,0,0,')
css = css.replace('background: #000;', 'background: #fff;')

# 2. Add Background Image to Hero Section
# The user said "background m image dalo or black colour k jagha koi acha photo dalo"
# Let's make the Hero section have a beautiful bridal background image with a light overlay

hero_css = '''
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  background: url('https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=1600&q=80') center/cover no-repeat;
  padding: 120px 0 60px;
  overflow: hidden;
}
/* Light overlay so text is readable */
.hero::before {
  content: '';
  position: absolute;
  top:0; left:0; width:100%; height:100%;
  background: linear-gradient(to right, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.8) 50%, rgba(255,255,255,0.3) 100%);
  z-index: 1;
}
.hero .container { position: relative; z-index: 2; }
'''
css = re.sub(r'\.hero \{[^\}]+\}', hero_css.strip(), css)
css = re.sub(r'\.hero::before \{[^\}]+\}', '', css) # remove old before if any

# We also need to hide the right-side image if we are using a background image, 
# OR we can keep the right side image and just have a soft pattern background.
# Since the user specifically said "background m image dalo", making the whole hero a background image is best.
css += '\\n.hero-right { display: none; } /* Hide the floating image since we have a full background */\\n'

# 3. Fix navbar for light theme
css = css.replace('.navbar { position: fixed;', '.navbar { position: fixed; background: rgba(255,255,255,0.95) !important; box-shadow: 0 4px 20px rgba(0,0,0,0.05);')
css = css.replace('.nav-links a { color: var(--white);', '.nav-links a { color: #222; font-weight: 600;')

# 4. Update the "Stats" section to look good on light theme
# It's currently forced to #FFFFFF, which is fine, but text should be dark.
css = css.replace('.stats { background: #FFFFFF;', '.stats { background: #fdfbf7;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Light Luxury Theme CSS applied!")
