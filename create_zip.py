import os
import zipfile

zip_filename = 'sabla-singh-academy-source.zip'
exclude_dirs = {'.git', 'node_modules', '.firebase'}

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk('.'):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file == zip_filename:
                continue
            file_path = os.path.join(root, file)
            zipf.write(file_path, os.path.relpath(file_path, '.'))

print(f"Created {zip_filename}")
