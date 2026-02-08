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
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            
            if img.width > max_width:
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            buffer = io.BytesIO()
            img.save(buffer, format='JPEG', quality=quality, optimize=True)
            buffer.seek(0)
            
            encoded = base64.b64encode(buffer.read()).decode('utf-8')
            return f"data:image/jpeg;base64,{encoded}"
    except Exception as e:
        print(f"Error encoding {image_path}: {e}")
        return None

def pdf_to_base64(pdf_path):
    """Convert PDF file to base64 string"""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            encoded = base64.b64encode(pdf_file.read()).decode('utf-8')
            return f"data:application/pdf;base64,{encoded}"
    except Exception as e:
        print(f"Error encoding {pdf_path}: {e}")
        return None

def embed_all_in_html(html_file, exclude_scan_pdfs=False):
    """Embed both images and PDFs in HTML file"""
    print(f"\nProcessing {html_file}...")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    base_dir = os.path.dirname(html_file)
    if not base_dir:
        base_dir = os.getcwd()
    
    # Find and embed images
    patterns = [
        r'src=["\']([^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',
        r'before:\s*["\']([^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',
        r'after:\s*["\']([^"\']+\.(?:jpg|jpeg|png|JPG|JPEG|PNG))["\']',
    ]
    
    all_images = []
    for pattern in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        all_images.extend(matches)
    
    unique_images = list(set(all_images))
    print(f"Found {len(unique_images)} unique images")
    
    for img_path in unique_images:
        if img_path.startswith('data:'):
            continue
        
        full_path = os.path.join(base_dir, img_path.replace('/', os.sep))
        full_path = os.path.normpath(full_path)
        
        if os.path.exists(full_path):
            print(f"  Encoding image: {os.path.basename(img_path)}")
            base64_data = compress_and_encode_image(full_path, max_width=1200, quality=85)
            if base64_data:
                escaped = re.escape(img_path)
                content = re.sub(f'(["\'])({escaped})(["\'])', f'\\1{base64_data}\\3', content)
    
    # Find and embed PDFs
    pdf_pattern = r'src=["\']([^"\']+\.pdf)["\']'
    pdf_matches = re.findall(pdf_pattern, content, re.IGNORECASE)
    unique_pdfs = list(set(pdf_matches))
    
    if exclude_scan_pdfs:
        # Only embed main estimate PDFs, skip large scan PDFs
        unique_pdfs = [p for p in unique_pdfs if 'scan_' not in p.lower()]
        print(f"Found {len(unique_pdfs)} PDFs (excluding large scan files)")
    else:
        print(f"Found {len(unique_pdfs)} PDFs")
    
    for pdf_path in unique_pdfs:
        if pdf_path.startswith('data:'):
            continue
        
        full_path = os.path.join(base_dir, pdf_path.replace('/', os.sep))
        full_path = os.path.normpath(full_path)
        
        if os.path.exists(full_path):
            file_size = os.path.getsize(full_path) / 1024
            print(f"  Encoding PDF: {os.path.basename(pdf_path)} ({file_size:.1f} KB)")
            base64_data = pdf_to_base64(full_path)
            if base64_data:
                escaped = re.escape(pdf_path)
                content = re.sub(f'src=["\']({escaped})["\']', f'src="{base64_data}"', content, flags=re.IGNORECASE)
    
    return content

if __name__ == '__main__':
    base_dir = os.getcwd()
    
    print("=" * 70)
    print("Creating COMPLETE STANDALONE versions")
    print("=" * 70)
    
    # Create light version without large scan PDFs
    print("\n📦 Creating LIGHT version (without property scans)...")
    source = os.path.join(base_dir, 'final_presentation.html')
    if os.path.exists(source):
        content = embed_all_in_html(source, exclude_scan_pdfs=True)
        output = os.path.join(base_dir, 'final_presentation_complete_light.html')
        with open(output, 'w', encoding='utf-8') as f:
            f.write(content)
        size_mb = os.path.getsize(output) / (1024 * 1024)
        print(f"✓ Created: final_presentation_complete_light.html ({size_mb:.1f} MB)")
    
    # Professional plan (already has only main PDFs)
    print("\n📦 Creating professional plan complete version...")
    source = os.path.join(base_dir, 'professional_renovation_plan.html')
    if os.path.exists(source):
        content = embed_all_in_html(source, exclude_scan_pdfs=False)
        output = os.path.join(base_dir, 'professional_renovation_plan_complete.html')
        with open(output, 'w', encoding='utf-8') as f:
            f.write(content)
        size_mb = os.path.getsize(output) / (1024 * 1024)
        print(f"✓ Created: professional_renovation_plan_complete.html ({size_mb:.1f} MB)")
    
    print("\n" + "=" * 70)
    print("✓ All complete standalone versions created!")
    print("=" * 70)
    print("\n📧 RECOMMENDED FOR SHARING:")
    print("   • final_presentation_complete_light.html (~5-6 MB)")
    print("     - All images + main estimate PDFs")
    print("     - NO large property scan PDFs (33 MB saved)")
    print("     - Perfect for email/WhatsApp")
    print("\n   • professional_renovation_plan_complete.html (~5-6 MB)")
    print("     - All images + 3 estimate PDFs")
    print("     - Professional project view")
    print("\n💡 If you need property scans, use:")
    print("   • final_presentation_optimized.html (49 MB)")
    print("     - Includes all 6 PDFs including property scans")
