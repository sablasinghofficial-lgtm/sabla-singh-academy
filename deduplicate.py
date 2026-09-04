import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the split block
a_start = html.find('<!--', html.find('ABOUT + COURSES SPLIT'))
if a_start == -1: 
    a_start = html.find('<!--', html.find('SPLIT'))
a_end = html.find('</section>', a_start) + 10
split_chunk = html[a_start:a_end]

# Remove all occurrences of the split block
html_no_chunks = html.replace(split_chunk, '')

# Re-insert just ONE occurrence at the right place (after HERO)
hero_end = html_no_chunks.find('</section>', html_no_chunks.find('HERO')) + 10
new_html = html_no_chunks[:hero_end] + '\n\n' + split_chunk + html_no_chunks[hero_end:]

# Let's also check if services is duplicated just in case
s_start = new_html.find('<!--', new_html.find('SERVICES'))
if s_start != -1:
    s_end = new_html.find('</section>', s_start) + 10
    services_chunk = new_html[s_start:s_end]
    # If it appears more than once, replace all with '' and reinsert once
    if new_html.count(services_chunk) > 1:
        new_html = new_html.replace(services_chunk, '')
        split_end = new_html.find('</section>', new_html.find('SPLIT')) + 10
        new_html = new_html[:split_end] + '\n\n' + services_chunk + new_html[split_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Deduplicated!")
