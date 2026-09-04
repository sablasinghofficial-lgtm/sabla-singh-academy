import glob
import re

# Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace old side-btns css
old_css_pattern = r'/\* Side buttons \*/.*?\.sb-enq\{.*?\}'
new_css = '''/* --- PREMIUM SIDE BUTTONS --- */
.side-btns { position:fixed; right:0; top:50%; transform:translateY(-50%); z-index:900; display:flex; flex-direction:column; gap:12px; }
.side-btn {
  display:flex; align-items:center; gap:12px; padding:12px 20px 12px 16px; border-radius:12px 0 0 12px;
  font-size:0.75rem; font-weight:700; letter-spacing:1px; text-transform:uppercase; transition:all 0.3s ease;
  cursor:pointer; box-shadow:-5px 5px 20px rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.1);
  border-right:none; backdrop-filter:blur(10px); -webkit-backdrop-filter:blur(10px);
}
.side-btn:hover { transform:translateX(-5px); padding-right:25px; }
.side-btn i { font-size:1.2rem; }
.sb-wa { background:rgba(37,211,102,0.9); color:#fff; border-color:rgba(255,255,255,0.2); }
.sb-wa:hover { background:#25D366; box-shadow:-5px 5px 25px rgba(37,211,102,0.5); }
.sb-call { background:rgba(201,149,26,0.9); color:var(--black); border-color:rgba(201,149,26,0.4); }
.sb-call:hover { background:var(--gold); box-shadow:-5px 5px 25px rgba(201,149,26,0.5); }
.sb-enq { background:rgba(15,15,15,0.95); color:var(--gold); border-color:var(--gold); }
.sb-enq:hover { background:var(--black); box-shadow:-5px 5px 25px rgba(201,149,26,0.3); }
'''

if '/* Side buttons */' in css:
    css = re.sub(old_css_pattern, new_css, css, flags=re.DOTALL)
else:
    css += '\n' + new_css

# Also remove wa-fl css
css = re.sub(r'/\* --- FLOATS --- \*/.*?(?=\.back-top)', '', css, flags=re.DOTALL)
css = re.sub(r'\.wa-fl\{.*?\}.*?@keyframes waP\{.*?\}', '', css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Remove wa-fl from all HTML files
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove the floating WA button
    html = re.sub(r'<a href="https://wa\.me/[^>]*class="wa-fl".*?</a>', '', html, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed!")
