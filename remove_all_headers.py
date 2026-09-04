# -*- coding: utf-8 -*-
import glob
import re

for fname in glob.glob("*.html"):
    if fname == "index.html":
        continue
        
    with open(fname, "r", encoding="utf-8") as f:
        html = f.read()

    # Find page-header section
    start_idx = html.find('<section class="page-header">')
    
    # Also check if there's a comment right before it
    if start_idx != -1:
        # Find the end of this section
        end_idx = html.find('</section>', start_idx)
        if end_idx != -1:
            end_idx += 10 # length of </section>
            
            # Check if there is a comment right before it like <!-- === PAGE HEADER === -->
            comment_start = html.rfind('<!--', 0, start_idx)
            if comment_start != -1 and "PAGE HEADER" in html[comment_start:start_idx]:
                start_idx = comment_start
                
            # Remove the block
            html = html[:start_idx] + html[end_idx:]
            
            with open(fname, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Removed page-header from {fname}")
