css = open("style.css", "r", encoding="utf-8", errors="replace").read()

css = css.replace(
    ".navbar{background:var(--bg2);position:sticky;top:0;z-index:1000;border-bottom:1px solid rgba(201,149,26,.15)}",
    ".navbar{background:#fff;position:sticky;top:0;z-index:1000;border-bottom:1px solid rgba(201,149,26,.18);box-shadow:0 2px 10px rgba(0,0,0,.06)}"
)
css = css.replace(
    ".navbar{background:var(--bg);position:sticky;top:0;z-index:1000;border-bottom:1px solid rgba(201,149,26,.2)}",
    ".navbar{background:#fff;position:sticky;top:0;z-index:1000;border-bottom:1px solid rgba(201,149,26,.18);box-shadow:0 2px 10px rgba(0,0,0,.06)}"
)

open("style.css", "w", encoding="utf-8").write(css)
print("Navbar white done!")
