css = open("style.css", "r", encoding="utf-8", errors="replace").read()

# Add upgraded CSS at end - clean navbar + hero layout fix
extra = """

/* ==== NAVBAR - Clean White Premium ==== */
.navbar {
  background: #ffffff !important;
  position: sticky; top: 0; z-index: 1000;
  border-bottom: 2px solid rgba(201,149,26,.2);
  box-shadow: 0 2px 16px rgba(0,0,0,.06);
}
.nav-links > a, .dd > a {
  color: #333 !important;
  font-size: .73rem; font-weight: 700; letter-spacing: 1.2px;
  text-transform: uppercase; transition: color .3s; position: relative; padding: 6px 0;
}
.nav-links > a.active, .nav-links > a:hover, .dd:hover > a { color: var(--gold) !important; }
.nav-links > a.active::after { content: ''; position: absolute; bottom: 0; left: 0; right: 0; height: 2px; background: var(--gold); }
.dd-menu {
  background: #fff !important;
  box-shadow: 0 8px 28px rgba(0,0,0,.1) !important;
  border: 1px solid rgba(201,149,26,.15) !important;
}
.dd-menu a { color: #555 !important; }
.dd-menu a:hover { color: var(--gold) !important; background: rgba(201,149,26,.07) !important; }

/* ==== SIDE BUTTONS - No Black ==== */
.sb-enq {
  background: linear-gradient(135deg, #8B1A4A, #C9386A) !important;
  color: #fff !important; border: none !important;
}
.sb-enq:hover { background: linear-gradient(135deg, #C9386A, #8B1A4A) !important; box-shadow: -4px 4px 20px rgba(139,26,74,.5) !important; }

/* ==== MINI STATS - Dont overlap side buttons ==== */
.hero-img-panel { padding-right: 100px !important; }
.mini-stat {
  background: rgba(255,255,255,0.12) !important;
  backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255,255,255,0.2) !important;
  border-radius: 14px; padding: 18px 20px !important;
  min-width: 115px !important;
}
.mini-stat:hover { background: rgba(201,149,26,.2) !important; border-color: var(--gold) !important; }

/* ==== HERO PADDING ==== */
.hero { padding: 90px 24px 60px !important; }
"""

css = css.rstrip() + "\n" + extra
open("style.css", "w", encoding="utf-8").write(css)
print("Nav and hero fully fixed!")
