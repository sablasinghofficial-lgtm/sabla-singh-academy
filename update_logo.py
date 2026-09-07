import re

files = ['index.html', 'courses.html', 'services.html', 'about.html', 'gallery.html', 'vlogs.html', 'contact.html']

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace logo in navbar nav-brand
        content = re.sub(
            r'(<a [^>]*class="nav-brand"[^>]*>[\s\S]*?<img src=")[^"]*(")',
            r'\1logo_new.png\2',
            content, count=1
        )

        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated logo in {fname}")
    except FileNotFoundError:
        print(f"Not found: {fname}")

print("All done!")
