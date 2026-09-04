css = open("style.css", "r", encoding="utf-8", errors="replace").read()

# 1. Fix Enquiry button - remove black, make it elegant gold/wine
old_enq = ".sb-enq { background: var(--bg3); color: var(--gold); border: 1px solid rgba(201,149,26,.3); border-right: none; }\n.sb-enq:hover { background: var(--gold); color: #111; }"
new_enq = ".sb-enq { background: linear-gradient(135deg,#8B1A4A,#C9386A); color: #fff; border: none; }\n.sb-enq:hover { background: linear-gradient(135deg,#C9386A,#8B1A4A); box-shadow: -4px 4px 20px rgba(139,26,74,.5); }"
css = css.replace(old_enq, new_enq)

# Also fix the compact version
css = css.replace(
    ".sb-enq{background:var(--bg3);color:var(--gold);border:1px solid rgba(201,149,26,.3);border-right:none}",
    ".sb-enq{background:linear-gradient(135deg,#8B1A4A,#C9386A);color:#fff;border:none}"
)
css = css.replace(
    ".sb-enq:hover{background:var(--gold);color:#111}",
    ".sb-enq:hover{background:linear-gradient(135deg,#C9386A,#8B1A4A);box-shadow:-4px 4px 20px rgba(139,26,74,.5)}"
)

# 2. Fix mini stats - move them left so they don't overlap side buttons
# Give mini-stat cards some right margin / max-width constraint
old_mini = ".hero-img-panel {\n  position: relative; z-index: 2; flex: 0 0 40%;\n  display: flex; align-items: center; gap: 20px;\n  justify-content: flex-end;\n}"
new_mini = ".hero-img-panel {\n  position: relative; z-index: 2; flex: 0 0 35%;\n  display: flex; align-items: center; gap: 20px;\n  justify-content: center;\n  padding-right: 80px;\n}"
css = css.replace(old_mini, new_mini)

# 3. Fix hero content max-width to give more room
old_hc = ".hero-content {\n  position: relative; z-index: 2;\n  flex: 0 0 52%;\n  max-width: 600px;\n}"
new_hc = ".hero-content {\n  position: relative; z-index: 2;\n  flex: 0 0 55%;\n  max-width: 620px;\n}"
css = css.replace(old_hc, new_hc)

# 4. Keep side-btns at top: 45% so they are clearly visible and not clashing 
old_side = ".side-btns { position: fixed; right: 0; top: 50%; transform: translateY(-50%); z-index: 900; display: flex; flex-direction: column; gap: 10px; }"
new_side = ".side-btns { position: fixed; right: 0; top: 42%; transform: translateY(-50%); z-index: 900; display: flex; flex-direction: column; gap: 8px; }"
css = css.replace(old_side, new_side)

open("style.css", "w", encoding="utf-8").write(css)
print("Overlap fixed!")
