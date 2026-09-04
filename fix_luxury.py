with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add body fade in animation
if '@keyframes fadeIn' not in css:
    css = 'body { animation: fadeIn 0.8s ease-in-out; }\n@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }\n' + css

# Add parallax to page-header
if 'background-attachment: fixed;' not in css:
    css = css.replace('.page-header {\n  padding: 120px 0 80px;', '.page-header {\n  padding: 120px 0 80px;\n  background-attachment: fixed !important;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Luxury touches added!")
