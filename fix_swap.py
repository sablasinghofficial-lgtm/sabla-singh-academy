import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will find the precise chunks using string operations to be totally safe
s_start = html.find('<!--', html.find('SERVICES'))
s_end = html.find('</section>', s_start) + 10
services_chunk = html[s_start:s_end]

a_start = html.find('<!--', html.find('ABOUT + COURSES SPLIT'))
if a_start == -1: # Due to unicode garble
    a_start = html.find('<!--', html.find('SPLIT'))
a_end = html.find('</section>', a_start) + 10
split_chunk = html[a_start:a_end]

if s_start != -1 and a_start != -1:
    # Remove both chunks
    html_no_chunks = html.replace(services_chunk, '').replace(split_chunk, '')
    
    # We want SPLIT to go where SERVICES originally started (right after HERO)
    # HERO ends at </section> right before SERVICES.
    hero_end = html_no_chunks.find('</section>', html_no_chunks.find('HERO')) + 10
    
    # Insert SPLIT then SERVICES
    new_html = html_no_chunks[:hero_end] + '\n\n' + split_chunk + '\n\n' + services_chunk + html_no_chunks[hero_end:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Properly swapped!")
else:
    print("Could not find chunks")
