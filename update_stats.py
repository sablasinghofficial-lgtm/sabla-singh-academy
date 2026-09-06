content = open('index.html', 'r', encoding='utf-8').read()

# Change Happy Customers count from 500 to 2500
content = content.replace('data-count="500"', 'data-count="2500"')

# Change 'luxury beauty' to 'luxury makeup' in the about description
content = content.replace('destination for luxury beauty and professional training', 'destination for luxury makeup and professional training')

open('index.html', 'w', encoding='utf-8').write(content)
print('Done! Updated Happy Customers to 2500+ and beauty to makeup.')
