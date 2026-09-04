# -*- coding: utf-8 -*-
with open("contact.html", "r", encoding="utf-8") as f:
    html = f.read()

# Using find and replace based on the actual file content to be safe against encoding issues
start = html.find("<!--")
start = html.find("PAGE HEADER", start)
if start != -1:
    # Find the beginning of this comment line
    start = html.rfind("<!--", 0, start)
    
    # Find the end of the section
    end = html.find("</section>", start)
    if end != -1:
        end += 10 # length of </section>
        # Remove the block
        html = html[:start] + html[end:]
        with open("contact.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Page header removed successfully!")
    else:
        print("Could not find </section>")
else:
    print("Could not find PAGE HEADER")
