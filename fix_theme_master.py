import re

# 1. Update CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace root variables entirely
old_root = re.search(r':root\{.*?\}', css, re.DOTALL)
if old_root:
    new_root = '''
:root{
  --gold:#C9951A;--gold-h:#B5840F;--gold-l:#FCEFB4;--gold-bg:rgba(201,149,26,.06);
  --black:#ffffff;--black2:#fdfbf7;--black3:#ffffff;--black4:#f0f0f0;--black5:#e0e0e0;
  --white:#222222;--off:#222222;--cream:#FFF9ED;
  --gray:#666;--gray-d:#333;--gray-l:#999;
  --hd:'Cormorant Garamond',serif;--bd:'Montserrat',sans-serif;--sc:'Great Vibes',cursive;
  --tr:all .35s ease;--sh:0 8px 30px rgba(0,0,0,.08);
}
'''
    css = css.replace(old_root.group(0), new_root.strip())

# Fix dark text for light theme
css = css.replace('color:#fff', 'color:var(--white)')
css = css.replace('color:#ffffff', 'color:var(--white)')
css = css.replace('color:rgba(255,255,255,.75)', 'color:rgba(0,0,0,.8)')
css = css.replace('color:rgba(255,255,255,.7)', 'color:rgba(0,0,0,.7)')
css = css.replace('background:#000', 'background:#fff')

# Hero section background image
hero_css_match = re.search(r'\.hero\{.*?\}', css, re.DOTALL)
if hero_css_match:
    new_hero_css = '.hero{position:relative;min-height:100vh;display:flex;align-items:center;background:url("https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=1600&q=80") center/cover no-repeat;padding:120px 0 60px;overflow:hidden;}'
    css = css.replace(hero_css_match.group(0), new_hero_css)

# Add overlay for hero
if '.hero::before' not in css:
    css += '\n.hero::before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;background:linear-gradient(to right, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.7) 50%, rgba(255,255,255,0.2) 100%);z-index:1;}\n'
    css += '.hero .container{position:relative;z-index:2;}\n'
    css += '.hero-right{display:none;}\n'

# Fix navbar
css = css.replace('.navbar{position:fixed;top:38px', '.navbar{position:fixed;top:38px;background:rgba(255,255,255,0.95);box-shadow:0 4px 15px rgba(0,0,0,0.05)')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update HTML Hero Section
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find hero section bounds
h_start = html.find('<section class="hero" id="home">')
h_end = html.find('</section>', h_start) + 10

if h_start != -1:
    new_hero = '''<section class="hero" id="home">
<div class="container" style="display:block;">
  <div class="hero-left" data-aos="fade-right" data-aos-duration="1000" style="max-width: 650px; margin-top: 20px;">
    
    <h3 style="font-family: var(--sc); font-size: 2.8rem; color: #555; margin-bottom: 5px; font-weight: normal;">Unleash Your Beauty</h3>
    <h1 style="font-family: var(--hd); font-size: 4.5rem; color: #111; line-height: 1.1; margin-bottom: 15px; text-transform: uppercase;">Empower<br><span style="color: var(--gold);">Your Future</span></h1>
    
    <p style="font-size: 1.1rem; color: #333; font-weight: 700; letter-spacing: 1px; margin-bottom: 15px; text-transform: uppercase;">Premium Beauty & Training Academy in Ranchi</p>
    
    <p style="font-size: 0.95rem; color: #666; margin-bottom: 30px; letter-spacing: 2px;">MAKEUP | SKIN | HAIR | NAILS | LASHES</p>
    
    <div class="hero-btns" style="display: flex; gap: 15px;">
      <a href="services.html" class="hbtn" style="background: var(--gold); color: #fff; padding: 15px 30px; border-radius: 4px; text-transform: uppercase; font-weight: 700; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(201,149,26,0.3);">Our Services <i class="fas fa-arrow-right"></i></a>
      <a href="courses.html" class="hbtn" style="background: transparent; color: #222; border: 2px solid var(--gold); padding: 13px 30px; border-radius: 4px; text-transform: uppercase; font-weight: 700; letter-spacing: 1px;">Our Courses <i class="fas fa-arrow-right"></i></a>
    </div>

  </div>
</div>
</section>'''
    
    old_hero = html[h_start:h_end]
    html = html.replace(old_hero, new_hero)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("Theme and Hero applied!")
