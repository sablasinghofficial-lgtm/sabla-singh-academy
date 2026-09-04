import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix nav link color
css = css.replace('color:rgba(255,255,255,.75)', 'color:#333')
css = css.replace('color:rgba(255,255,255,.7)', 'color:#444')

# Fix footer text colors
css = css.replace('color:rgba(255,255,255,.6)', 'color:#666')
css = css.replace('color:rgba(255,255,255,.45)', 'color:#777')
css = css.replace('color:rgba(255,255,255,.85)', 'color:#333')

# Check mobile menu background
if '.mob-menu{position:fixed;top:0;right:-100%;width:320px;height:100vh;background:var(--black2)' in css:
    pass # it's fine, black2 is now cream

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Nav fixed")
