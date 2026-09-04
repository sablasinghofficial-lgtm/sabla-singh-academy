# -*- coding: utf-8 -*-
import glob

for html_file in glob.glob("*.html"):
    with open(html_file, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()

    # Add ft-contact class to contact column in footer
    html = html.replace('<div class="ft-col">\n      <h4>Contact Info</h4>', '<div class="ft-col ft-contact">\n      <h4>Contact Info</h4>')
    html = html.replace('<div class="ft-col">\n      <h4>Contact Info', '<div class="ft-col ft-contact">\n      <h4>Contact Info')
    
    # Add ft-brand class to the brand column
    html = html.replace('<div class="ft-col">\n      <img src="logo.png"', '<div class="ft-col ft-brand">\n      <img src="logo.png"')

    # Ensure ft-bottom is a child of footer, not inside ft-grid
    # Also ensure social icons in footer have the right class

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)

print("Footer HTML fixed for all pages!")
