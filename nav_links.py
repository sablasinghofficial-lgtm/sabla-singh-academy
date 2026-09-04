css = open("style.css", "r", encoding="utf-8", errors="replace").read()

# Nav link text colors - dark for white background
old = "text-transform:uppercase;color:rgba(0,0,0,.8);transition:color .3s;position:relative;padding:6px 0"
new = "text-transform:uppercase;color:#444;transition:color .3s;position:relative;padding:6px 0"
css = css.replace(old, new)

# Also try the pattern from the appended upgraded hero CSS at end
old2 = "text-transform:uppercase;color:var(--txt2);transition:color .3s;position:relative;padding:6px 0"
new2 = "text-transform:uppercase;color:#444;transition:color .3s;position:relative;padding:6px 0"
css = css.replace(old2, new2)

# Also fix hamburger span for white navbar - keep gold
# Mobile menu background stays dark (black) - thats fine

# Dropdown - white background, light shadow
old3 = "background:var(--bg3);min-width:220px;border-radius:8px;box-shadow:0 12px 40px rgba(0,0,0,.7);"
new3 = "background:#fff;min-width:220px;border-radius:8px;box-shadow:0 8px 24px rgba(0,0,0,.1);"
css = css.replace(old3, new3)

# Dropdown link color
old4 = "padding:10px 22px;font-size:.78rem;font-weight:500;color:var(--txt2);transition"
new4 = "padding:10px 22px;font-size:.78rem;font-weight:500;color:#555;transition"
css = css.replace(old4, new4)

open("style.css", "w", encoding="utf-8").write(css)
print("Nav links dark done!")
