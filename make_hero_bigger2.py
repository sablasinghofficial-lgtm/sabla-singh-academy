# -*- coding: utf-8 -*-
with open("style.css", "r", encoding="utf-8", errors="replace") as f:
    css = f.read()

# Remove the bad overrides
css = css.replace("""/* Hero text overrides to make it HUGE */
.hero-sub { font-size: 4.5rem !important; margin-bottom: -15px !important; }
.hero-main { font-size: clamp(4.5rem, 8vw, 7.5rem) !important; line-height: 1.1 !important; }
.hero-meet { font-size: 3.5rem !important; }
.hero-desc { font-size: 1.15rem !important; max-width: 600px !important; line-height: 1.8 !important; }
""", "")

better_extra = """
/* Proper responsive hero sizing */
@media (min-width: 992px) {
    .hero-content { max-width: 750px !important; }
    .hero-sub { font-size: 4.5rem !important; margin-bottom: -15px !important; }
    .hero-main { font-size: 7.5rem !important; line-height: 1.1 !important; }
    .hero-meet { font-size: 3.5rem !important; }
    .hero-desc { font-size: 1.15rem !important; max-width: 650px !important; line-height: 1.8 !important; }
}
@media (min-width: 601px) and (max-width: 991px) {
    .hero-sub { font-size: 3.5rem !important; }
    .hero-main { font-size: 5rem !important; }
    .hero-meet { font-size: 2.8rem !important; }
}
"""

css = css + "\n" + better_extra

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Responsive hero size fixed!")
