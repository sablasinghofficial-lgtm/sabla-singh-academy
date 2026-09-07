content = open('index.html','r',encoding='utf-8').read()

# Fix lash image - replace Unsplash URL with local image
content = content.replace(
    'https://images.unsplash.com/photo-1512496015851-a1fb92f5e3e2?w=300&q=80',
    'service_lash.jpg'
)

open('index.html','w',encoding='utf-8').write(content)
print('Lash image updated!')
