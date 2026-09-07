files = ['index.html', 'courses.html', 'services.html', 'about.html', 'gallery.html', 'vlogs.html', 'contact.html']

for fname in files:
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace ALL logo.png references with logo_transparent.png
        content = content.replace('src="logo.png"', 'src="logo_transparent.png"')
        content = content.replace("src='logo.png'", "src='logo_transparent.png'")
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {fname}")
    except Exception as e:
        print(f"Error {fname}: {e}")

print("All done!")
