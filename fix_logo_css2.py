# -*- coding: utf-8 -*-
css = open("style.css", "r", encoding="utf-8", errors="replace").read()

extra = """
/* Override for Logo + Text Balance */
.nav-brand { gap: 8px !important; }
.nav-brand img { height: 50px !important; margin-right: 2px; }
.brand-title { font-size: 1.6rem !important; color: var(--gold-h) !important; font-weight: 600 !important; }
.brand-sub { color: #555 !important; font-size: 0.55rem !important; letter-spacing: 3.5px !important; font-weight: 700 !important; }
"""

css = css + "\n" + extra
open("style.css", "w", encoding="utf-8").write(css)
print("Logo text CSS added safely!")
