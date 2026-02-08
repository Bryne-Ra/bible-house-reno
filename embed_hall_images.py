import base64
import os
from pathlib import Path

def image_to_base64(image_path):
    """Convert image file to base64 string"""
    with open(image_path, 'rb') as img_file:
        encoded = base64.b64encode(img_file.read()).decode('utf-8')
        ext = os.path.splitext(image_path)[1].lower()
        mime = 'image/jpeg' if ext in ['.jpg', '.jpeg'] else 'image/png'
        return f"data:{mime};base64,{encoded}"

# Image paths
images = {
    'before and after pictures/inside_hall_before.jpeg': None,
    'before and after pictures/inside_hall_after.png': None,
    'before and after pictures/outside_hall_before.jpeg': None,
    'before and after pictures/outside_hall_after.png': None
}

print("Embedding hall images in quotes.html...")

# Encode images
for img_path in images.keys():
    if os.path.exists(img_path):
        print(f"  Encoding: {img_path}")
        images[img_path] = image_to_base64(img_path)
    else:
        print(f"  ERROR: Not found: {img_path}")

# Read quotes.html
with open('quotes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace image paths with base64
for original, base64_data in images.items():
    if base64_data:
        content = content.replace(f'src="{original}"', f'src="{base64_data}"')

# Write updated quotes.html
with open('quotes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Hall images embedded in quotes.html!")
print("  The file is now standalone and doesn't need the image files.")
