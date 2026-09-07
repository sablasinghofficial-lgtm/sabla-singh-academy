with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Fix ticker years counter - both occurrences
    if 'data-count="5"' in line and 'Years Excellence' in line:
        line = line.replace('data-count="5"', 'data-count="20"')
        line = line.replace('>5<', '>20<')
    # Fix stat box years counter (line 239 area)
    if 'data-count="5"' in line and 'Years of Excellence' in line:
        line = line.replace('data-count="5"', 'data-count="20"')
    # Fix general data-count="5" that could be years
    if 'data-count="5"' in line and '>5<' in line:
        line = line.replace('data-count="5"', 'data-count="20"')
        line = line.replace('>5<', '>20<')
    # Fix Happy Clients display value 500 -> 2500
    if 'data-count="2500"' in line and '>500<' in line:
        line = line.replace('>500<', '>2500<')
    new_lines.append(line)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed!")
