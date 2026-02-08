import base64
import os
import re

def pdf_to_base64(pdf_path):
    """Convert PDF file to base64 string"""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            encoded = base64.b64encode(pdf_file.read()).decode('utf-8')
            return f"data:application/pdf;base64,{encoded}"
    except Exception as e:
        print(f"Error encoding {pdf_path}: {e}")
        return None

def embed_pdfs_in_html(html_file):
    """Read HTML file, find all PDF references, and embed them as base64"""
    print(f"\nProcessing {html_file}...")
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all PDF references in iframe src and other src attributes
    pdf_pattern = r'src=["\']([^"\']+\.pdf)["\']'
    matches = re.findall(pdf_pattern, content, re.IGNORECASE)
    
    if not matches:
        print(f"No PDFs found in {html_file}")
        return
    
    # Remove duplicates
    unique_pdfs = list(set(matches))
    print(f"Found {len(unique_pdfs)} unique PDF references")
    
    base_dir = os.path.dirname(html_file)
    if not base_dir:
        base_dir = os.getcwd()
    
    replacements = {}
    
    for pdf_path in unique_pdfs:
        # Skip if already base64
        if pdf_path.startswith('data:'):
            continue
        
        # Construct full path
        full_path = os.path.join(base_dir, pdf_path.replace('/', os.sep))
        full_path = os.path.normpath(full_path)
        
        if os.path.exists(full_path):
            file_size = os.path.getsize(full_path) / 1024  # KB
            print(f"  Encoding: {pdf_path} ({file_size:.1f} KB)")
            base64_data = pdf_to_base64(full_path)
            if base64_data:
                replacements[pdf_path] = base64_data
        else:
            print(f"  WARNING: File not found: {full_path}")
    
    # Replace all PDF paths with base64
    for original, base64_data in replacements.items():
        # Escape special regex characters in the path
        escaped = re.escape(original)
        content = re.sub(
            f'src=["\']({escaped})["\']',
            f'src="{base64_data}"',
            content,
            flags=re.IGNORECASE
        )
    
    # Write back to file (overwrite the optimized file)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated: {html_file}")
    print(f"  Embedded {len(replacements)} PDFs")
    
    # Show file size
    size_mb = os.path.getsize(html_file) / (1024 * 1024)
    print(f"  New file size: {size_mb:.1f} MB")

if __name__ == '__main__':
    # Process the optimized HTML files
    html_files = [
        'final_presentation_optimized.html',
        'professional_renovation_plan_optimized.html',
    ]
    
    base_dir = os.getcwd()
    
    print("=" * 70)
    print("Embedding PDFs into optimized HTML files")
    print("=" * 70)
    
    for html_file in html_files:
        full_path = os.path.join(base_dir, html_file)
        full_path = os.path.normpath(full_path)
        if os.path.exists(full_path):
            embed_pdfs_in_html(full_path)
        else:
            print(f"File not found: {full_path}")
    
    print("\n" + "=" * 70)
    print("✓ All done! PDFs are now embedded in the HTML files")
    print("=" * 70)
    print("\n📄 The HTML files now include:")
    print("   - All before/after images (embedded)")
    print("   - All PDF documents (embedded)")
    print("   - Completely standalone - no external files needed!")
    print("   - Ready to share via email, WhatsApp, or any platform")
