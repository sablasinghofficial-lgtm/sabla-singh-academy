# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

css = css.replace(".tb-right span{font-weight:600}", 
                  ".tb-right span{font-weight:600; font-size: 0.9rem;}")

css = css.replace(".tb-right a{width:22px;height:22px;border-radius:50%;background:rgba(0,0,0,.08);display:flex;align-items:center;justify-content:center;font-size:.65rem;", 
                  ".tb-right a{width:28px;height:28px;border-radius:50%;background:rgba(0,0,0,.08);display:flex;align-items:center;justify-content:center;font-size:0.9rem;")

# Fix logo height to be truly prominent since the container is min-height 95px now.
css = css.replace("height: 85px !important; min-width: 85px !important;", "height: 75px !important; min-width: 75px !important;")
# Let's make brand text a bit bigger too
css = css.replace(".brand-title { font-size: 1.8rem !important; }", ".brand-title { font-size: 2.1rem !important; margin-bottom: 2px !important; }")
css = css.replace(".brand-sub { font-size: 0.6rem !important; letter-spacing: 4px !important; }", ".brand-sub { font-size: 0.75rem !important; letter-spacing: 5px !important; }")

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("More header size fixes!")
