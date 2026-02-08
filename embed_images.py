import base64
import os
import re
from pathlib import Path

def image_to_base64(image_path):
    """Convert image file to base64 string"""
    try:
        with open(image_path, 'rb') as img_file:
            encoded = base64.b64encode(img_file.read()).decode('utf-8')
            # Determine mime type
            ext = os.path.splitext(image_path)[1].lower()
            if ext in ['.jpg', '.jpeg']:
                mime = 'image/jpeg'
            elif ext == '.png':
                mime = 'image/png'
            else:
                mime = 'image/jpeg'
            return f"data:{mime};base64,{encoded}"
    except Exception as e:
        print(f"Error encoding {image_path}: {e}")
        return None

def embed_images_in_html(html_file):
    """Read HTML file, find all image references, and embed them as base64"""
    print(f"\nProcessing {html_file}...")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all image references (in src attributes and JavaScript strings)
    patterns = [
        r'src=["\']([^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',  # HTML src
        r'before:\s*["\']([^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',  # JS before
        r'after:\s*["\']([^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',   # JS after
    ]
    
    all_matches = []
    for pattern in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        all_matches.extend(matches)
    
    if not all_matches:
        print(f"No images found in {html_file}")
        return
    
    # Remove duplicates
    unique_images = list(set(all_matches))
    print(f"Found {len(unique_images)} unique image references")
    
    base_dir = os.path.dirname(html_file)
    replacements = {}
    
    for img_path in unique_images:
        # Skip if already base64
        if img_path.startswith('data:'):
            continue
            
        # Construct full path
        full_path = os.path.join(base_dir, img_path.replace('/', os.sep))
        full_path = os.path.normpath(full_path)
        
        if os.path.exists(full_path):
            print(f"  Encoding: {img_path}")
            base64_data = image_to_base64(full_path)
            if base64_data:
                replacements[img_path] = base64_data
        else:
            print(f"  WARNING: File not found: {full_path}")
    
    # Replace all image paths with base64
    for original, base64_data in replacements.items():
        # Escape special regex characters in the path
        escaped = re.escape(original)
        # Replace in both HTML src and JavaScript strings
        content = re.sub(
            f'(["\'])({escaped})(["\'])',
            f'\\1{base64_data}\\3',
            content
        )
    
    # Write back to file
    output_file = html_file.replace('.html', '_embedded.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Created: {output_file}")
    print(f"  Embedded {len(replacements)} images")

if __name__ == '__main__':
    # Process all HTML files
    html_files = [
        'final_presentation.html',
        'professional_renovation_plan.html',
        'presentation/comparison.html'
    ]
    
    # Use current directory
    base_dir = os.getcwd()
    
    for html_file in html_files:
        full_path = os.path.join(base_dir, html_file)
        # Normalize path separators
        full_path = os.path.normpath(full_path)
        if os.path.exists(full_path):
            embed_images_in_html(full_path)
        else:
            print(f"File not found: {full_path}")
    
    print("\n✓ All done! Embedded versions created with '_embedded.html' suffix")
    print("These files are now completely standalone and portable!")
