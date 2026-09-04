with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix inline style color references in about-full section
html = html.replace('color:var(--white);line-height:1.2', 'color:#fff;line-height:1.2')
html = html.replace('color:rgba(255,255,255,.6)', 'color:rgba(255,255,255,.65)')
html = html.replace('color:rgba(255,255,255,.85)', 'color:rgba(255,255,255,.8)')
html = html.replace('color:rgba(255,255,255,.45)', 'color:rgba(255,255,255,.5)')
html = html.replace('background:var(--gold);color:var(--black);padding:13px', 'background:var(--gold);color:#111;padding:13px')
html = html.replace('style="background:var(--gold);color:var(--black);', 'style="background:var(--gold);color:#111;')
html = html.replace('"background:var(--gold);color:var(--black)', '"background:var(--gold);color:#111')
# crs-tag color fix
html = html.replace('color:var(--black);"', 'color:#111;"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Also fix same inline color issues in all other html files
import glob
for fname in glob.glob("*.html"):
    if fname == "index.html":
        continue
    with open(fname, "r", encoding="utf-8") as f:
        h = f.read()
    h = h.replace('color:var(--white)', 'color:#fff')
    h = h.replace('color:var(--black)', 'color:#111')
    h = h.replace('background:var(--black);', 'background:#0a0a0a;')
    h = h.replace('background:var(--black2);', 'background:#111;')
    with open(fname, "w", encoding="utf-8") as f:
        f.write(h)

print("Inline styles fixed!")
