import re

# 1. Update style.css colors and add typewriter CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update colors
css = css.replace('--gold: #C9951A;', '--gold: #D4AF37; /* Brighter premium yellow-gold */')
css = css.replace('--gold-l: #E8B946;', '--gold-l: #FCEFB4; /* Lighter bright gold */')
css = css.replace('--black: #0a0a0a;', '--black: #050505;')
css = css.replace('--black2: #111111;', '--black2: #0a0a0a;')
css = css.replace('--black3: #1a1a1a;', '--black3: #141414;')

# Make Stats section white!
css = re.sub(
    r'\.stats \{[^\}]+\}',
    '.stats { background: #FFFFFF; padding: 60px 0; border-top: 2px solid var(--gold); border-bottom: 2px solid var(--gold); position: relative; z-index: 10; }',
    css
)
css = re.sub(
    r'\.stat-box \{[^\}]+\}',
    '.stat-box { flex: 1; text-align: center; border-right: 1px solid rgba(212,175,55,0.3); padding: 0 20px; }\n.stat-box:last-child { border: none; }',
    css
)
css = re.sub(
    r'\.stat-num \{[^\}]+\}',
    '.stat-num { font-family: var(--hd); font-size: 3.5rem; font-weight: 700; color: #111; line-height: 1; margin-bottom: 10px; }\n.stat-num sup { color: var(--gold); }',
    css
)
css = re.sub(
    r'\.stat-lbl \{[^\}]+\}',
    '.stat-lbl { font-size: 0.8rem; font-weight: 600; color: #555; text-transform: uppercase; letter-spacing: 2px; }',
    css
)

# Add Typewriter CSS
if '.typewriter' not in css:
    css += '''
/* Typewriter Effect */
.typewriter {
    color: var(--gold);
    font-family: var(--sc);
    font-weight: normal;
    border-right: 3px solid var(--gold);
    padding-right: 5px;
    animation: blink 0.75s step-end infinite;
}
@keyframes blink { 50% { border-color: transparent; } }

/* Make hero text a bit higher */
.hero-left { margin-top: -40px; }
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html for Typewriter and Stats structure
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Hero H1
old_h1 = '<h1>Where Beauty<br>Meets <span style="font-family: var(--sc); font-weight: normal;">Excellence</span></h1>'
new_h1 = '<h1>Where Beauty<br>Meets <span class="typewriter" id="typewriter"></span></h1>'
html = html.replace(old_h1, new_h1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("CSS and HTML updated for Theme and Typewriter")
