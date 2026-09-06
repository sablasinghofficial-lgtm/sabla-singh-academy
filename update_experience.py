import glob

files = ['index.html', 'courses.html', 'about.html', 'services.html', 'contact.html', 'gallery.html', 'vlogs.html']

for fname in files:
    try:
        content = open(fname, 'r', encoding='utf-8').read()
        updated = content.replace('5+ Years Experience', '20+ Years Experience')
        updated = updated.replace('5+ years of excellence', '20+ years of excellence')
        updated = updated.replace('5+ years of industry secrets', '20+ years of industry secrets')
        updated = updated.replace('5+ years of experience', '20+ years of experience')
        if updated != content:
            open(fname, 'w', encoding='utf-8').write(updated)
            print(f"Updated: {fname}")
        else:
            print(f"No change: {fname}")
    except FileNotFoundError:
        print(f"Not found: {fname}")

print("Done!")
