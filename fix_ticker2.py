content = open('index.html', 'r', encoding='utf-8').read()

# Fix counter span - data-count 5 -> 20, inner text 5 -> 20
content = content.replace(
    'data-count="5">5</span>+ Years Excellence',
    'data-count="20">20</span>+ Years Excellence'
)

# Fix Happy Clients counter display (shows 500 but should show 2500 initially or just static)
content = content.replace(
    'data-count="2500">500</span>+ Happy Clients',
    'data-count="2500">2500</span>+ Happy Clients'
)

open('index.html', 'w', encoding='utf-8').write(content)
print("Done!")
