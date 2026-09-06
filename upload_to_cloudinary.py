import os
import requests
import json

cloud_name = "iqlwz76c"
upload_preset = "ml_default"
upload_url = f"https://api.cloudinary.com/v1_1/{cloud_name}/auto/upload"

files_to_upload = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith(('.jpg', '.png', '.mp4')):
            files_to_upload.append(os.path.join(root, file))

results = {}
for path in files_to_upload:
    print(f"Uploading {path}...")
    try:
        with open(path, 'rb') as f:
            response = requests.post(
                upload_url,
                data={'upload_preset': upload_preset},
                files={'file': f}
            )
            data = response.json()
            if 'secure_url' in data:
                results[path] = data['secure_url']
                print(f"Success: {data['secure_url']}")
            else:
                print(f"Error for {path}: {data}")
    except Exception as e:
        print(f"Failed {path}: {e}")

with open('cloudinary_urls.json', 'w') as f:
    json.dump(results, f, indent=4)
print("Finished uploading!")
