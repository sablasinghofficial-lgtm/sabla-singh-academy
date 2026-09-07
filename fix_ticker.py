content = open('index.html', 'r', encoding='utf-8').read()

# Fix counter data-count from 5 to 20 for Years Excellence
content = content.replace('data-count="5">5</span>+ Years Excellence', 'data-count="20">20</span>+ Years Excellence')

# Fix "by 500+ Members" to "by 2500+ Members"
content = content.replace('by 500+ Members', 'by 2500+ Members')

# Fix any remaining "5+ Years" plain text
content = content.replace('>5+</strong> Years Excellence', '>20+</strong> Years Excellence')
content = content.replace('5+ Years Excellence', '20+ Years Excellence')
content = content.replace('5+ years', '20+ years')
content = content.replace('5+ Years', '20+ Years')

open('index.html', 'w', encoding='utf-8').write(content)
print("Done! All updated.")
