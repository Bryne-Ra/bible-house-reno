import base64
import os
import re
from pathlib import Path
from PIL import Image
import io

def compress_and_encode_image(image_path, max_width=1200, quality=85):
    """Compress image and convert to base64 string"""
    try:
        with Image.open(image_path) as img:
            # Convert RGBA to RGB if necessary
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            
            # Resize if too large
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Compress to bytes
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=quality, optimize=True)
            buffer.seek(0)
            
            # Encode to base64
            encoded = base64.b64encode(buffer.read()).decode('utf-8')
            return f"data:image/jpeg;base64,{encoded}"
    except Exception as e:
        print(f"Error encoding {image_path}: {e}")
        return None

def embed_images_in_html(html_file, compress=True):
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
            if compress:
                base64_data = compress_and_encode_image(full_path, max_width=1200, quality=85)
            else:
                base64_data = compress_and_encode_image(full_path, max_width=3000, quality=95)
            
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
    suffix = '_optimized.html' if compress else '_highres.html'
    output_file = html_file.replace('.html', suffix)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Created: {output_file}")
    print(f"  Embedded {len(replacements)} images")
    
    # Show file size
    size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"  File size: {size_mb:.1f} MB")

if __name__ == '__main__':
    # Process all HTML files
    html_files = [
        'final_presentation.html',
        'professional_renovation_plan.html',
        'presentation/comparison.html'
    ]
    
    # Use current directory
    base_dir = os.getcwd()
    
    print("=" * 60)
    print("Creating OPTIMIZED versions (smaller, faster loading)")
    print("=" * 60)
    
    for html_file in html_files:
        full_path = os.path.join(base_dir, html_file)
        full_path = os.path.normpath(full_path)
        if os.path.exists(full_path):
            embed_images_in_html(full_path, compress=True)
        else:
            print(f"File not found: {full_path}")
    
    print("\n" + "=" * 60)
    print("✓ All done!")
    print("=" * 60)
    print("\n📱 OPTIMIZED versions (_optimized.html):")
    print("   - Compressed images (1200px max width, 85% quality)")
    print("   - Perfect for sharing via email or WhatsApp")
    print("   - Works on all devices without internet")
    print("   - Smaller file size for faster loading")
