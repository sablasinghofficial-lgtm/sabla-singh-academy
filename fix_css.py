import re

css = open('style.css', 'r', encoding='utf-8').read()

# Fix root variables - restore proper dark theme
old_root = """:root{
  --gold:#C9951A;--gold-h:#B5840F;--gold-l:#FCEFB4;--gold-bg:rgba(201,149,26,.06);
  --black:#ffffff;--black2:#fdfbf7;--black3:#ffffff;--black4:#f0f0f0;--black5:#e0e0e0;
  --white:#222222;--off:#222222;--cream:#FFF9ED;
  --gray:#666;--gray-d:#333;--gray-l:#999;
  --hd:'Cormorant Garamond',serif;--bd:'Montserrat',sans-serif;--sc:'Great Vibes',cursive;
  --tr:all .35s ease;--sh:0 8px 30px rgba(0,0,0,.08);
}"""
new_root = """:root{
  --gold:#C9951A;--gold-h:#B5840F;--gold-l:#F0CD6A;--gold-bg:rgba(201,149,26,.08);
  --bg:#0A0A0A;--bg2:#111111;--bg3:#1A1A1A;--bg4:#222222;
  --txt:#FFFFFF;--txt2:#BBBBBB;--gray:#888888;
  --hd:'Cormorant Garamond',serif;--bd:'Montserrat',sans-serif;--sc:'Great Vibes',cursive;
  --tr:all .3s ease;
}"""
css = css.replace(old_root, new_root)

# Fix all --black and --white references
pairs = [
    ('var(--black2)', 'var(--bg2)'),
    ('var(--black3)', 'var(--bg3)'),
    ('var(--black4)', 'var(--bg4)'),
    ('var(--black)', 'var(--bg)'),
    ('var(--white)', 'var(--txt)'),
    ('color:var(--txt)', 'color:#fff'),  # will be wrong in topbar etc, but selective below
]
# Only replace background references for bg vars
css = re.sub(r'background:var\(--black(\d?)\)', lambda m: 'background:var(--bg' + m.group(1) + ')', css)
css = re.sub(r'background: var\(--black(\d?)\)', lambda m: 'background:var(--bg' + m.group(1) + ')', css)
# Replace text colors
css = css.replace('color:var(--white)', 'color:var(--txt)')
css = css.replace('color: var(--white)', 'color:var(--txt)')
# Replace remaining var(--black) in non-background contexts (border, color on gold bg)
css = re.sub(r'color:var\(--black\)', 'color:#111', css)
css = re.sub(r'color: var\(--black\)', 'color:#111', css)

# Fix hero section CSS - replace old hero with full bg image hero
old_hero_line = '.hero{position:relative;min-height:100vh;display:flex;align-items:center;background:url("https://images.unsplash.com/photo-1596755389378-c31d21fd1273?w=1600&q=80") center/cover no-repeat;padding:120px 0 60px;overflow:hidden;}'
new_hero_line = '.hero{position:relative;min-height:100vh;display:flex;align-items:center;background:url("https://images.unsplash.com/photo-1519340241574-2cec6aef0c01?w=1800&q=85") center/cover no-repeat;padding:80px 0 60px;overflow:hidden}'
css = css.replace(old_hero_line, new_hero_line)

# Fix hero::before - remove white overlay, add dark overlay
old_before = '.hero::before{content:"";position:absolute;top:0;left:0;width:100%;height:100%;background:linear-gradient(to right, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.7) 50%, rgba(255,255,255,0.2) 100%);z-index:1;}'
new_before = '.hero::before{content:"";position:absolute;inset:0;background:linear-gradient(105deg,rgba(10,10,10,0.93) 0%,rgba(10,10,10,0.72) 55%,rgba(10,10,10,0.25) 100%);z-index:1}'
css = css.replace(old_before, new_before)

# Remove the duplicate broken hero lines appended at end
css = css.replace('\\n.hero-right { display: none; } /* Hide the floating image since we have a full background */\\n', '')
css = css.replace('.hero .container{position:relative;z-index:2;}\n.hero-right{display:none;}\n', '.hero .container{position:relative;z-index:2}\n.hero-right{display:none}\n')

# Fix WhatsApp nav button (change from gold to green)
css = css.replace('.nav-book{background:var(--gold);color:#111;padding:11px 24px;border-radius:6px;font-size:.72rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;transition:var(--tr);box-shadow:0 4px 15px rgba(200,148,26,.3);white-space:nowrap}',
    '.nav-book{background:#25D366;color:#fff;padding:11px 22px;border-radius:6px;font-size:.72rem;font-weight:700;letter-spacing:1px;text-transform:uppercase;transition:var(--tr);box-shadow:0 4px 15px rgba(37,211,102,.3);white-space:nowrap;display:flex;align-items:center;gap:7px}')
css = css.replace('.nav-book:hover{background:var(--gold-h);transform:translateY(-1px);box-shadow:0 6px 20px rgba(200,148,26,.5)}',
    '.nav-book:hover{background:#20bc5a;transform:translateY(-1px);box-shadow:0 6px 20px rgba(37,211,102,.5)}')

# Fix hero text (it was set to var(--white) which is now dark)
css = css.replace('.hero h1{font-family:var(--hd);font-size:clamp(2.4rem,4.5vw,3.8rem);font-weight:700;color:var(--txt);',
    '.hero h1{font-family:var(--hd);font-size:clamp(2.8rem,5vw,4.5rem);font-weight:700;color:#fff;')
css = css.replace('.h-stat .num{font-family:var(--hd);font-size:1.9rem;font-weight:700;color:var(--txt);',
    '.h-stat .num{font-family:var(--hd);font-size:2rem;font-weight:700;color:#fff;')

# Fix crs-list text (was changed to dark by accident)
css = css.replace('color: rgba(0,0,0,0.75)', 'color:var(--txt2)')

# Fix cta-mid (was white -> now dark, but on dark background needs to be light)
css = css.replace('.cta-mid{font-size:.82rem;color:rgba(255,255,255,.65)', '.cta-mid{font-size:.82rem;color:var(--gray)')

# Fix footer bottom text
css = css.replace('.ft-bottom p{font-size:.75rem;color:rgba(255,255,255,.3)}', '.ft-bottom p{font-size:.75rem;color:var(--gray)}')

open('style.css', 'w', encoding='utf-8').write(css)
print('All CSS fixed!')
