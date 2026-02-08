import os
import base64
from pathlib import Path

# Directory setup
base_dir = Path(__file__).parent
images_dir = base_dir / "before and after pictures"

# Image pairs for before/after
image_pairs = [
    ("pic1b4.jpg.jpg", "pic1after.jpg.png", "View 1"),
    ("pic1b4.jpg.jpg", "pic1after2.jpg.png", "View 2"),
    ("pic2b4.jpg.jpg", "pic2after.jpg.png", "View 3"),
    ("pic2b4.jpg.jpg", "pic2after2.jpg.png", "View 4"),
    ("pic3b4.jpg.jpg", "pic3after.jpg.png", "View 5"),
    ("pic3b42.jpg.jpg", "pic3after.jpg.png", "View 6"),
    ("pic4b4.jpg.jpg", "pic4after.jpg.png", "View 7"),
    ("pic4b42.jpg.jpg", "pic4after.jpg.png", "View 8"),
    ("pic4b4.jpg.jpg", "pic5after.jpg.png", "View 9"),
    ("pic6b4.jpg.jpg", "pic6after.jpg.png", "View 10"),
    ("pic6b42.jpg.jpg", "pic6after.jpg.png", "View 11"),
    ("pic6b43.jpg.jpg", "pic6after.jpg.png", "View 12"),
    ("pic7b4.jpg.jpg", "pic7after.jpg.png", "View 13"),
    ("pic8b4.jpg.jpg", "pic8after.jpg.png", "View 14"),
    ("pic8b42.jpg.jpg", "pic8after.jpg.png", "View 15"),
    ("junglegym1.jpg.jpg", "pic8after.jpg.png", "View 16"),
]

def image_to_base64(image_path):
    """Convert image to base64 string"""
    try:
        with open(image_path, 'rb') as img_file:
            encoded = base64.b64encode(img_file.read()).decode('utf-8')
            ext = image_path.suffix.lower()
            if ext in ['.jpg', '.jpeg']:
                return f"data:image/jpeg;base64,{encoded}"
            elif ext == '.png':
                return f"data:image/png;base64,{encoded}"
    except FileNotFoundError:
        return None

# Encode images
print("Encoding before/after images...")
encoded_images = []
for before, after, title in image_pairs:
    before_path = images_dir / before
    after_path = images_dir / after
    
    before_b64 = image_to_base64(before_path)
    after_b64 = image_to_base64(after_path)
    
    if before_b64 and after_b64:
        encoded_images.append({
            'title': title,
            'before': before_b64,
            'after': after_b64
        })
        print(f"✓ Encoded {title}")

print(f"\n✓ Encoded {len(encoded_images)} image pairs")

# Shared CSS and navigation
def get_shared_styles():
    return """
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        
        .progress-bar {
            background: rgba(255,255,255,0.2);
            height: 8px;
            border-radius: 10px;
            margin-top: 20px;
            overflow: hidden;
        }
        
        .progress-fill {
            background: #4caf50;
            height: 100%;
            border-radius: 10px;
            transition: width 0.3s;
        }
        
        .navigation {
            display: flex;
            justify-content: space-between;
            padding: 20px 40px;
            background: #f9f9f9;
            border-bottom: 2px solid #eee;
        }
        
        .nav-button {
            padding: 12px 24px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .nav-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }
        
        .nav-button.disabled {
            background: #ccc;
            cursor: not-allowed;
            pointer-events: none;
        }
        
        .content {
            padding: 40px;
        }
        
        .section {
            margin-bottom: 30px;
        }
        
        .section h2 {
            color: #667eea;
            margin-bottom: 20px;
            font-size: 2em;
        }
        
        .section h3 {
            color: #764ba2;
            margin: 20px 0 10px;
            font-size: 1.4em;
        }
        
        .info-box {
            background: #e3f2fd;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 4px solid #2196f3;
        }
        
        .success-box {
            background: #e8f5e9;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 4px solid #4caf50;
        }
        
        .warning-box {
            background: #fff3e0;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 4px solid #ff9800;
        }
        
        .cost-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .cost-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-top: 3px solid #667eea;
        }
        
        .cost-card h3 {
            color: #667eea;
            margin-bottom: 15px;
        }
        
        .cost-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }
        
        .cost-item:last-child {
            border-bottom: none;
            font-weight: bold;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }
        
        th {
            background: #667eea;
            color: white;
            font-weight: 600;
        }
        
        tr:hover {
            background: #f5f5f5;
        }
        
        ul, ol {
            margin-left: 20px;
            margin-top: 10px;
        }
        
        li {
            margin-bottom: 8px;
            line-height: 1.6;
        }
        
        .comparison-container {
            position: relative;
            width: 100%;
            max-width: 800px;
            margin: 30px auto;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        }
        
        .comparison-images {
            position: relative;
            width: 100%;
            height: 500px;
        }
        
        .comparison-before, .comparison-after {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }
        
        .comparison-after {
            clip-path: inset(0 50% 0 0);
        }
        
        .comparison-before img, .comparison-after img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        
        .comparison-slider {
            position: absolute;
            width: 4px;
            height: 100%;
            background: white;
            left: 50%;
            top: 0;
            cursor: ew-resize;
            box-shadow: 0 0 10px rgba(0,0,0,0.5);
        }
        
        .comparison-slider::before {
            content: '⟨ ⟩';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 10px 15px;
            border-radius: 50px;
            font-weight: bold;
            color: #667eea;
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        
        .comparison-labels {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
            font-size: 0.9em;
            color: #666;
        }
        
        /* Mobile Responsive */
        @media screen and (max-width: 768px) {
            .container {
                border-radius: 0;
            }
            
            .header h1 {
                font-size: 1.8em;
            }
            
            .navigation {
                flex-direction: column;
                gap: 10px;
            }
            
            .content {
                padding: 20px;
            }
            
            .cost-grid {
                grid-template-columns: 1fr;
            }
            
            .comparison-images {
                height: 300px;
            }
            
            table {
                font-size: 0.85em;
            }
            
            th, td {
                padding: 10px 8px;
            }
        }
        
        @media screen and (max-width: 480px) {
            .header h1 {
                font-size: 1.5em;
            }
            
            .content {
                padding: 15px;
            }
            
            .section h2 {
                font-size: 1.5em;
            }
            
            .comparison-images {
                height: 250px;
            }
        }
    </style>
"""

def get_navigation(current_page, total_pages, prev_page=None, next_page=None):
    prev_button = f'<a href="{prev_page}" class="nav-button">← Previous</a>' if prev_page else '<span class="nav-button disabled">← Previous</span>'
    next_button = f'<a href="{next_page}" class="nav-button">Next →</a>' if next_page else '<span class="nav-button disabled">Next →</span>'
    
    progress_percent = (current_page / total_pages) * 100
    
    return f"""
    <div class="navigation">
        {prev_button}
        <div style="text-align: center; flex: 1;">
            <div style="font-weight: 600; color: #667eea;">Step {current_page} of {total_pages}</div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: {progress_percent}%"></div>
            </div>
        </div>
        {next_button}
    </div>
"""

def get_comparison_script():
    return """
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const containers = document.querySelectorAll('.comparison-container');
            
            containers.forEach(container => {
                const slider = container.querySelector('.comparison-slider');
                const afterImage = container.querySelector('.comparison-after');
                let isDragging = false;
                
                function updatePosition(e) {
                    const rect = container.getBoundingClientRect();
                    const x = (e.clientX || e.touches[0].clientX) - rect.left;
                    const percentage = Math.max(0, Math.min(100, (x / rect.width) * 100));
                    
                    afterImage.style.clipPath = `inset(0 ${100 - percentage}% 0 0)`;
                    slider.style.left = percentage + '%';
                }
                
                slider.addEventListener('mousedown', () => isDragging = true);
                slider.addEventListener('touchstart', () => isDragging = true);
                
                document.addEventListener('mousemove', (e) => {
                    if (isDragging) updatePosition(e);
                });
                
                document.addEventListener('touchmove', (e) => {
                    if (isDragging) updatePosition(e);
                });
                
                document.addEventListener('mouseup', () => isDragging = false);
                document.addEventListener('touchend', () => isDragging = false);
                
                container.addEventListener('click', updatePosition);
            });
        });
    </script>
"""

# Page 1: Overview
page1_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible House Renovation - Overview</title>
    {get_shared_styles()}
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏠 Bible House Renovation Project</h1>
            <p>Step 1: Project Overview</p>
        </div>
        
        {get_navigation(1, 7, None, 'costs.html')}
        
        <div class="content">
            <div class="section">
                <h2>⛪ Church Expansion & Renewal Vision</h2>
                <div class="info-box">
                    <h3>📊 Project Scope</h3>
                    <p><strong>Total Investment:</strong> R 730,900</p>
                    <p><strong>Project Type:</strong> Church Expansion & Sacred Space Enhancement</p>
                    <p><strong>Location:</strong> Bible House</p>
                    <p><strong>Timeline:</strong> 8-12 weeks (estimated)</p>
                    <p><strong>Mission:</strong> Building a sanctuary that welcomes all, sustains worship, and nurtures spiritual growth</p>
                </div>
                
                <h3>🎯 Church-Centered Objectives</h3>
                <ul>
                    <li><strong>Extending the Main Hall:</strong> Expanding worship space to welcome larger congregations and facilitate community growth</li>
                    <li><strong>Emergency Worship System:</strong> Ensuring uninterrupted services during power outages through solar backup systems (2x 200L geysers)</li>
                    <li><strong>Sacred Space Enhancement:</strong> Creating dedicated prayer rooms and improving facilities for spiritual activities</li>
                    <li><strong>Infrastructure Renewal:</strong> Upgrading electrical, plumbing, and structural systems to support continuous ministry operations</li>
                    <li><strong>Atmosphere of Worship:</strong> Professional finishing (ceilings, painting, tiling) to create an environment conducive to prayer and spiritual growth</li>
                    <li><strong>Security & Accessibility:</strong> New doors and hardware ensuring safe, welcoming access for all congregation members</li>
                </ul>
                
                <h3>📋 Ministry-Focused Implementation Phases</h3>
                <ol>
                    <li><strong>Phase 1:</strong> Protecting God's House (Weeks 1-4)
                        <ul>
                            <li>Roof waterproofing - ensuring weatherproof sanctuary for year-round worship</li>
                            <li>Exterior renewal - creating welcoming first impressions for visitors and members</li>
                        </ul>
                    </li>
                    <li><strong>Phase 2:</strong> Emergency Worship System & Infrastructure (Weeks 3-6)
                        <ul>
                            <li>Electrical system upgrade - reliable power for services and ministry activities</li>
                            <li>Solar geysers installation (2x 200L) - blackout support for uninterrupted worship</li>
                            <li>Plumbing modernization - supporting fellowship meals and congregation needs</li>
                        </ul>
                    </li>
                    <li><strong>Phase 3:</strong> Enhancing Sacred Spaces (Weeks 5-9)
                        <ul>
                            <li>Ceiling installation - improved acoustics for worship and teaching</li>
                            <li>Wall preparation and painting - creating peaceful atmosphere for prayer</li>
                            <li>Floor tiling - durable, clean surfaces for active ministry use</li>
                        </ul>
                    </li>
                    <li><strong>Phase 4:</strong> Completing the Sanctuary (Weeks 9-12)
                        <ul>
                            <li>Door installation - security and privacy for prayer rooms and offices</li>
                            <li>Final touches - polish and excellence worthy of God's house</li>
                            <li>Dedication and blessing preparation</li>
                        </ul>
                    </li>
                </ol>
                
                <div class="success-box">
                    <h3>✨ Kingdom Impact & Expected Outcomes</h3>
                    <ul>
                        <li><strong>Larger Congregations:</strong> Expanded hall space welcoming more families to worship together</li>
                        <li><strong>Uninterrupted Ministry:</strong> Emergency power ensuring services continue during blackouts</li>
                        <li><strong>Sacred Prayer Spaces:</strong> Dedicated rooms for personal communion with God and meditation</li>
                        <li><strong>Enhanced Worship Atmosphere:</strong> Professional finishes creating environment conducive to spiritual growth</li>
                        <li><strong>Safe & Welcoming:</strong> Modern infrastructure supporting all ministry activities safely</li>
                        <li><strong>Generational Legacy:</strong> Building a sanctuary that will serve God's people for years to come</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

# Save Page 1
with open(base_dir / 'overview.html', 'w', encoding='utf-8') as f:
    f.write(page1_content)
print("✓ Created overview.html")

# Page 2: Costs
page2_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible House Renovation - Cost Breakdown</title>
    {get_shared_styles()}
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>💰 Cost Breakdown</h1>
            <p>Step 2: Detailed Budget Analysis</p>
        </div>
        
        {get_navigation(2, 7, 'overview.html', 'materials.html')}
        
        <div class="content">
            <div class="section">
                <h2>Complete Cost Analysis</h2>
                
                <div class="cost-grid">
                    <div class="cost-card">
                        <h3>🏗️ Roof Waterproofing</h3>
                        <p style="color: #666; font-size: 0.9em; margin-bottom: 10px;"><em>Protecting God's house from the elements</em></p>
                        <div class="cost-item"><span>Labor & Materials</span><span>R 80,000.00</span></div>
                    </div>
                    
                    <div class="cost-card">
                        <h3>⚡ Electrical System</h3>
                        <p style="color: #666; font-size: 0.9em; margin-bottom: 10px;"><em>Reliable power for services & ministry</em></p>
                        <div class="cost-item"><span>Material</span><span>R 80,000.00</span></div>
                        <div class="cost-item"><span>Labor</span><span>R 40,000.00</span></div>
                        <div class="cost-item"><span><strong>Subtotal</strong></span><span><strong>R 120,000.00</strong></span></div>
                    </div>
                    
                    <div class="cost-card">
                        <h3>⚡ Emergency Worship System</h3>
                        <p style="color: #666; font-size: 0.9em; margin-bottom: 10px;"><em>Ensuring uninterrupted worship during blackouts</em></p>
                        <div class="cost-item"><span>Material</span><span>R 95,000.00</span></div>
                        <div class="cost-item"><span>Labor</span><span>R 8,500.00</span></div>
                        <div class="cost-item"><span>Solar Geysers (2x 200L)</span><span>R 35,000.00</span></div>
                        <div class="cost-item"><span><strong>Subtotal</strong></span><span><strong>R 138,500.00</strong></span></div>
                    </div>
                    
                    <div class="cost-card">
                        <h3>🏢 Main Hall Extension</h3>
                        <p style="color: #666; font-size: 0.9em; margin-bottom: 10px;"><em>Welcoming larger congregations</em></p>
                        <div class="cost-item"><span>Material (Ceiling Boards)</span><span>R 96,000.00</span></div>
                        <div class="cost-item"><span>Labor</span><span>R 24,000.00</span></div>
                        <div class="cost-item"><span><strong>Subtotal</strong></span><span><strong>R 120,000.00</strong></span></div>
                    </div>
                    
                    <div class="cost-card">
                        <h3>🎨 Sacred Space Atmosphere</h3>
                        <p style="color: #666; font-size: 0.9em; margin-bottom: 10px;"><em>Creating conducive worship environment</em></p>
                        <div class="cost-item"><span>Paint Material</span><span>R 32,000.00</span></div>
                        <div class="cost-item"><span>Professional Labor</span><span>R 48,000.00</span></div>
                        <div class="cost-item"><span><strong>Subtotal</strong></span><span><strong>R 80,000.00</strong></span></div>
                    </div>
                    
                    <div class="cost-card">
                        <h3>🔲 Sanctuary Flooring</h3>
                        <p style="color: #666; font-size: 0.9em; margin-bottom: 10px;"><em>Durable surfaces for active ministry</em></p>
                        <div class="cost-item"><span>Tiles Material</span><span>R 64,000.00</span></div>
                        <div class="cost-item"><span>Installation Labor</span><span>R 36,000.00</span></div>
                        <div class="cost-item"><span><strong>Subtotal</strong></span><span><strong>R 100,000.00</strong></span></div>
                    </div>
                    
                    <div class="cost-card">
                        <h3>🚪 Prayer Rooms & Access</h3>
                        <p style="color: #666; font-size: 0.9em; margin-bottom: 10px;"><em>Privacy for prayer & secure access</em></p>
                        <div class="cost-item"><span>Doors Material</span><span>R 11,840.00</span></div>
                        <div class="cost-item"><span>Installation Labor</span><span>R 6,600.00</span></div>
                        <div class="cost-item"><span><strong>Subtotal</strong></span><span><strong>R 18,440.00</strong></span></div>
                    </div>
                    
                    <div class="cost-card">
                        <h3>🔧 Supporting Infrastructure</h3>
                        <p style="color: #666; font-size: 0.9em; margin-bottom: 10px;"><em>Windows, demolition & finishing touches</em></p>
                        <div class="cost-item"><span>Window Installation</span><span>R 16,000.00</span></div>
                        <div class="cost-item"><span>Demolition Work</span><span>R 20,000.00</span></div>
                        <div class="cost-item"><span>Sundries & Materials</span><span>R 24,000.00</span></div>
                        <div class="cost-item"><span>VAT (15%)</span><span>R 13,960.88</span></div>
                        <div class="cost-item"><span><strong>Subtotal</strong></span><span><strong>R 93,960.88</strong></span></div>
                    </div>
                </div>
                
                <div class="success-box" style="margin-top: 30px; text-align: center;">
                    <h3>💒 Total Investment in God's House</h3>
                    <h2 style="color: #4caf50; font-size: 2.5em;">R 730,900.00</h2>
                    <p style="margin-top: 15px; font-size: 1.1em;"><em>Building a sanctuary that welcomes all, sustains worship, and nurtures spiritual growth for generations to come</em></p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

with open(base_dir / 'costs.html', 'w', encoding='utf-8') as f:
    f.write(page2_content)
print("✓ Created costs.html")

# Page 3: Materials
page3_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible House Renovation - Materials & Specifications</title>
    {get_shared_styles()}
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🛠️ Materials & Specifications</h1>
            <p>Step 3: Detailed Material Requirements</p>
        </div>
        
        {get_navigation(3, 7, 'costs.html', 'timeline.html')}
        
        <div class="content">
            <div class="section">
                <h2>Material Specifications</h2>
                <p style="text-align: center; color: #666; margin-bottom: 30px; font-size: 1.1em;">
                    <em>Quality materials for a sanctuary that will serve generations</em>
                </p>
                
                <h3>🏗️ Roofing Materials - Protecting God's House</h3>
                <p style="color: #666; margin-bottom: 15px;"><em>Weatherproofing to ensure year-round worship without interruption</em></p>
                <table>
                    <tr>
                        <th>Item</th>
                        <th>Specification</th>
                        <th>Quantity</th>
                    </tr>
                    <tr>
                        <td>Waterproofing Membrane</td>
                        <td>Torch-on waterproofing, 4mm thickness</td>
                        <td>As per roof area</td>
                    </tr>
                    <tr>
                        <td>Roof Coating</td>
                        <td>Elastomeric acrylic coating</td>
                        <td>2 coats</td>
                    </tr>
                </table>
                
                <h3>⚡ Electrical Materials - Reliable Power for Ministry</h3>
                <p style="color: #666; margin-bottom: 15px;"><em>Supporting worship services with consistent, safe power infrastructure</em></p>
                <table>
                    <tr>
                        <th>Item</th>
                        <th>Specification</th>
                        <th>Notes</th>
                    </tr>
                    <tr>
                        <td>Distribution Board</td>
                        <td>18-way, SANS compliant</td>
                        <td>With surge protection</td>
                    </tr>
                    <tr>
                        <td>Cables</td>
                        <td>2.5mm² & 4mm² PVC insulated</td>
                        <td>Color coded as per regulations</td>
                    </tr>
                    <tr>
                        <td>Light Fittings</td>
                        <td>LED downlights, 9W</td>
                        <td>Energy efficient</td>
                    </tr>
                    <tr>
                        <td>Plugs & Switches</td>
                        <td>16A, modular design</td>
                        <td>White finish</td>
                    </tr>
                </table>
                
                <h3>🚰 Emergency Worship System - Blackout Support</h3>
                <p style="color: #666; margin-bottom: 15px;"><em>Solar geysers ensuring continuous hot water during power outages</em></p>
                <table>
                    <tr>
                        <th>Item</th>
                        <th>Specification</th>
                        <th>Quantity</th>
                    </tr>
                    <tr>
                        <td>Solar Geysers</td>
                        <td>200L high-pressure, stainless steel</td>
                        <td>2 units</td>
                    </tr>
                    <tr>
                        <td>Pipes</td>
                        <td>Class 12 UPVC, 110mm & 50mm</td>
                        <td>As required</td>
                    </tr>
                    <tr>
                        <td>Taps & Mixers</td>
                        <td>Chrome finish, water-saving aerators</td>
                        <td>As per layout</td>
                    </tr>
                </table>
                
                <h3>🏢 Ceiling Materials - Main Hall Extension</h3>
                <p style="color: #666; margin-bottom: 15px;"><em>Expanding worship space to welcome larger congregations with quality acoustics</em></p>
                <table>
                    <tr>
                        <th>Item</th>
                        <th>Specification</th>
                        <th>Coverage</th>
                    </tr>
                    <tr>
                        <td>Ceiling Boards</td>
                        <td>9mm Rhino board</td>
                        <td>All rooms</td>
                    </tr>
                    <tr>
                        <td>Steel Framework</td>
                        <td>38mm x 12mm galvanized</td>
                        <td>As required</td>
                    </tr>
                    <tr>
                        <td>Cornices</td>
                        <td>80mm polystyrene</td>
                        <td>All perimeters</td>
                    </tr>
                </table>
                
                <h3>🎨 Paint Specifications - Creating Sacred Atmosphere</h3>
                <p style="color: #666; margin-bottom: 15px;"><em>Peaceful colors and durable finishes for prayer rooms and worship halls</em></p>
                <table>
                    <tr>
                        <th>Area</th>
                        <th>Product</th>
                        <th>Coats</th>
                    </tr>
                    <tr>
                        <td>Interior Walls</td>
                        <td>Plascon Double Velvet</td>
                        <td>2 coats</td>
                    </tr>
                    <tr>
                        <td>Ceilings</td>
                        <td>Plascon Ceiling White</td>
                        <td>2 coats</td>
                    </tr>
                    <tr>
                        <td>Exterior</td>
                        <td>Plascon Exteriorwall</td>
                        <td>2 coats</td>
                    </tr>
                </table>
                
                <h3>🔲 Tiling Materials - Durable Sanctuary Flooring</h3>
                <p style="color: #666; margin-bottom: 15px;"><em>Long-lasting surfaces for active ministry and fellowship gatherings</em></p>
                <table>
                    <tr>
                        <th>Item</th>
                        <th>Specification</th>
                        <th>Area</th>
                    </tr>
                    <tr>
                        <td>Floor Tiles</td>
                        <td>600x600mm porcelain</td>
                        <td>As per floor plan</td>
                    </tr>
                    <tr>
                        <td>Tile Adhesive</td>
                        <td>Flexible, polymer-modified</td>
                        <td>As required</td>
                    </tr>
                    <tr>
                        <td>Grout</td>
                        <td>Epoxy grout, stain resistant</td>
                        <td>Matching color</td>
                    </tr>
                </table>
                
                <h3>🚪 Door Specifications - Prayer Room Privacy</h3>
                <p style="color: #666; margin-bottom: 15px;"><em>Secure and private access to sacred spaces</em></p>
                <table>
                    <tr>
                        <th>Type</th>
                        <th>Specification</th>
                        <th>Hardware</th>
                    </tr>
                    <tr>
                        <td>Interior Doors</td>
                        <td>Hollow core, 813mm x 2032mm</td>
                        <td>Lever handles, hinges</td>
                    </tr>
                    <tr>
                        <td>Frames</td>
                        <td>Pre-hung, pine wood</td>
                        <td>Primed and ready to paint</td>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</body>
</html>"""

with open(base_dir / 'materials.html', 'w', encoding='utf-8') as f:
    f.write(page3_content)
print("✓ Created materials.html")

# Page 4: Timeline
page4_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible House Renovation - Timeline</title>
    {get_shared_styles()}
    <style>
        .timeline-item {{
            position: relative;
            padding-left: 40px;
            padding: 20px;
            background: white;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            border-left: 4px solid #667eea;
        }}
        
        .timeline-item h4 {{
            color: #667eea;
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📅 Project Timeline</h1>
            <p>Step 4: Detailed Schedule & Phases</p>
        </div>
        
        {get_navigation(4, 7, 'materials.html', 'beforeafter.html')}
        
        <div class="content">
            <div class="section">
                <h2>8-12 Week Construction Timeline</h2>
                <p style="text-align: center; color: #666; margin-bottom: 30px; font-size: 1.1em;">
                    <em>Phased approach to minimize worship disruptions</em>
                </p>
                
                <div class="timeline-item">
                    <h4>Week 1-2: Protecting God's House</h4>
                    <p style="color: #666; margin-bottom: 10px;"><em>Weatherproofing the sanctuary</em></p>
                    <ul>
                        <li>Site preparation and protection</li>
                        <li>Roof inspection and repairs</li>
                        <li>Waterproofing application for year-round worship</li>
                        <li>First coat of roof sealing</li>
                    </ul>
                </div>
                
                <div class="timeline-item">
                    <h4>Week 2-3: Power for Ministry</h4>
                    <p style="color: #666; margin-bottom: 10px;"><em>Installing reliable electrical infrastructure</em></p>
                    <ul>
                        <li>Electrical conduit installation</li>
                        <li>Distribution board setup for worship services</li>
                        <li>Cable pulling and routing</li>
                        <li>First safety inspection</li>
                    </ul>
                </div>
                
                <div class="timeline-item">
                    <h4>Week 3-4: Emergency Worship System</h4>
                    <p style="color: #666; margin-bottom: 10px;"><em>Blackout support installation</em></p>
                    <ul>
                        <li>Plumbing pipe installation</li>
                        <li>Solar geyser mounting (2 x 200L units)</li>
                        <li>Connection of hot water lines for fellowship meal support</li>
                        <li>Pressure testing and certification</li>
                    </ul>
                </div>
                
                <div class="timeline-item">
                    <h4>Week 4-6: Extending the Main Hall</h4>
                    <p style="color: #666; margin-bottom: 10px;"><em>Creating space for larger congregations</em></p>
                    <ul>
                        <li>Steel framework for hall expansion</li>
                        <li>Ceiling board mounting for worship acoustics</li>
                        <li>Cornice installation for finished appearance</li>
                        <li>Ceiling finishing and sanding</li>
                    </ul>
                </div>
                
                <div class="timeline-item">
                    <h4>Week 6-7: Lighting for Worship</h4>
                    <p style="color: #666; margin-bottom: 10px;"><em>Completing electrical and lighting systems</em></p>
                    <ul>
                        <li>Energy-efficient LED light fitting installation</li>
                        <li>Plug and switch installation for ministry equipment</li>
                        <li>Testing and certification</li>
                        <li>Final electrical inspection</li>
                    </ul>
                </div>
                
                <div class="timeline-item">
                    <h4>Week 7-9: Durable Sanctuary Flooring</h4>
                    <p style="color: #666; margin-bottom: 10px;"><em>Long-lasting surfaces for active ministry</em></p>
                    <ul>
                        <li>Floor preparation and leveling</li>
                        <li>Tile laying and alignment throughout sanctuary</li>
                        <li>Grouting and sealing for easy maintenance</li>
                        <li>Cleaning and protection</li>
                    </ul>
                </div>
                
                <div class="timeline-item">
                    <h4>Week 8-10: Sacred Space Atmosphere</h4>
                    <p style="color: #666; margin-bottom: 10px;"><em>Creating peaceful worship environment</em></p>
                    <ul>
                        <li>Wall preparation and priming</li>
                        <li>Interior wall painting in peaceful colors (2 coats)</li>
                        <li>Ceiling painting for brightness (2 coats)</li>
                        <li>Exterior painting for welcoming appearance (2 coats)</li>
                    </ul>
                </div>
                
                <div class="timeline-item">
                    <h4>Week 10-11: Prayer Room Privacy</h4>
                    <p style="color: #666; margin-bottom: 10px;"><em>Securing sacred spaces for contemplation</em></p>
                    <ul>
                        <li>Door frame installation for prayer rooms</li>
                        <li>Door hanging and adjustment for privacy</li>
                        <li>Hardware installation (locks for security)</li>
                        <li>Final adjustments</li>
                    </ul>
                </div>
                
                <div class="timeline-item">
                    <h4>Week 11-12: Dedication Preparation</h4>
                    <p style="color: #666; margin-bottom: 10px;"><em>Completing the sanctuary for blessing</em></p>
                    <ul>
                        <li>Touch-up painting throughout</li>
                        <li>Plumbing fixture installation (taps, fittings)</li>
                        <li>Final deep cleaning and consecration preparation</li>
                        <li>Inspection and handover for worship services</li>
                    </ul>
                </div>
                
                <div class="warning-box">
                    <h3>⚠️ Important Notes</h3>
                    <ul>
                        <li>Timeline designed to minimize worship disruptions</li>
                        <li>Some phases overlap for faster completion</li>
                        <li>Weather conditions may affect outdoor work</li>
                        <li>Regular updates to church leadership recommended</li>
                        <li>Flexible scheduling to accommodate special services</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

with open(base_dir / 'timeline.html', 'w', encoding='utf-8') as f:
    f.write(page4_content)
print("✓ Created timeline.html")

# Page 5: Before & After (with images)
comparisons_html = ""
for img in encoded_images[:8]:  # First 8 images
    comparisons_html += f"""
                <h3>{img['title']}</h3>
                <div class="comparison-container">
                    <div class="comparison-images">
                        <div class="comparison-before">
                            <img src="{img['before']}" alt="{img['title']} - Before">
                        </div>
                        <div class="comparison-after">
                            <img src="{img['after']}" alt="{img['title']} - After">
                        </div>
                        <div class="comparison-slider"></div>
                    </div>
                    <div class="comparison-labels">
                        <span>← Before</span>
                        <span>After →</span>
                    </div>
                </div>
"""

page5_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible House Renovation - Before & After</title>
    {get_shared_styles()}
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📸 Before & After Comparisons</h1>
            <p>Step 5: Visual Transformation (Part 1 of 2)</p>
        </div>
        
        {get_navigation(5, 7, 'timeline.html', 'beforeafter2.html')}
        
        <div class="content">
            <div class="section">
                <h2>Interactive Image Comparisons</h2>
                <p style="text-align: center; color: #666; margin-bottom: 30px;">
                    <em>Drag the slider or click to compare before and after</em>
                </p>
                
                {comparisons_html}
            </div>
        </div>
    </div>
    {get_comparison_script()}
</body>
</html>"""

with open(base_dir / 'beforeafter.html', 'w', encoding='utf-8') as f:
    f.write(page5_content)
print("✓ Created beforeafter.html")

# Page 6: Before & After Part 2
comparisons_html2 = ""
for img in encoded_images[8:]:  # Remaining images
    comparisons_html2 += f"""
                <h3>{img['title']}</h3>
                <div class="comparison-container">
                    <div class="comparison-images">
                        <div class="comparison-before">
                            <img src="{img['before']}" alt="{img['title']} - Before">
                        </div>
                        <div class="comparison-after">
                            <img src="{img['after']}" alt="{img['title']} - After">
                        </div>
                        <div class="comparison-slider"></div>
                    </div>
                    <div class="comparison-labels">
                        <span>← Before</span>
                        <span>After →</span>
                    </div>
                </div>
"""

page6_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible House Renovation - Before & After (Part 2)</title>
    {get_shared_styles()}
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📸 Before & After Comparisons</h1>
            <p>Step 6: Visual Transformation (Part 2 of 2)</p>
        </div>
        
        {get_navigation(6, 7, 'beforeafter.html', 'prioritization.html')}
        
        <div class="content">
            <div class="section">
                <h2>Interactive Image Comparisons (Continued)</h2>
                <p style="text-align: center; color: #666; margin-bottom: 30px;">
                    <em>Drag the slider or click to compare before and after</em>
                </p>
                
                {comparisons_html2}
            </div>
        </div>
    </div>
    {get_comparison_script()}
</body>
</html>"""

with open(base_dir / 'beforeafter2.html', 'w', encoding='utf-8') as f:
    f.write(page6_content)
print("✓ Created beforeafter2.html")

# Page 7: Prioritization
page7_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible House Renovation - Prioritization</title>
    {get_shared_styles()}
    <style>
        .priority-high {{ border-left-color: #f44336; }}
        .priority-medium {{ border-left-color: #ff9800; }}
        .priority-low {{ border-left-color: #4caf50; }}
        .priority-badge {{
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .badge-high {{ background: #ffebee; color: #f44336; }}
        .badge-medium {{ background: #fff3e0; color: #ff9800; }}
        .badge-low {{ background: #e8f5e9; color: #4caf50; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>⭐ Project Prioritization</h1>
            <p>Step 7: Recommended Implementation Order</p>
        </div>
        
        {get_navigation(7, 7, 'beforeafter2.html', None)}
        
        <div class="content">
            <div class="section">
                <h2>Priority-Based Implementation Plan</h2>
                <p style="text-align: center; color: #666; margin-bottom: 30px; font-size: 1.1em;">
                    <em>Prioritized by kingdom impact and worship continuity</em>
                </p>
                
                <div class="info-box priority-high">
                    <span class="priority-badge badge-high">🔴 HIGH PRIORITY</span>
                    <h3>Phase 1: Protecting & Welcoming (Weeks 1-4)</h3>
                    <p><strong>Ministry Investment:</strong> R 200,000</p>
                    <p style="color: #666;"><em>Foundation for year-round worship and safe gatherings</em></p>
                    <ul>
                        <li><strong>Roof Waterproofing (R 80,000)</strong>
                            <ul>
                                <li>Protects sanctuary from weather - enables year-round worship</li>
                                <li>Prevents damage to prayer spaces and fellowship areas</li>
                                <li>Must be completed before rainy season disrupts services</li>
                            </ul>
                        </li>
                        <li><strong>Electrical System Upgrade (R 120,000)</strong>
                            <ul>
                                <li>Reliable power for worship services, lighting, sound systems</li>
                                <li>Safety critical - protects congregation and equipment</li>
                                <li>Required for all ministry activities and events</li>
                            </ul>
                        </li>
                    </ul>
                </div>
                
                <div class="info-box priority-medium">
                    <span class="priority-badge badge-medium">🟡 MEDIUM PRIORITY</span>
                    <h3>Phase 2: Expanding & Sustaining (Weeks 3-7)</h3>
                    <p><strong>Ministry Investment:</strong> R 258,500</p>
                    <p style="color: #666;"><em>Ensuring uninterrupted ministry and welcoming larger congregations</em></p>
                    <ul>
                        <li><strong>Emergency Worship System & Plumbing (R 138,500)</strong>
                            <ul>
                                <li>Solar geysers ensure hot water during blackouts (fellowship meals, baptisms)</li>
                                <li>Uninterrupted worship services regardless of power outages</li>
                                <li>Long-term cost savings for ministry funds</li>
                            </ul>
                        </li>
                        <li><strong>Main Hall Extension - Ceilings (R 120,000)</strong>
                            <ul>
                                <li>Expanding capacity to welcome larger congregations</li>
                                <li>Improved acoustics for worship music and preaching</li>
                                <li>Creates inviting atmosphere for new visitors</li>
                            </ul>
                        </li>
                    </ul>
                </div>
                
                <div class="info-box priority-low">
                    <span class="priority-badge badge-low">🟢 STANDARD PRIORITY</span>
                    <h3>Phase 3: Enhancing Sacred Spaces (Weeks 7-12)</h3>
                    <p><strong>Ministry Investment:</strong> R 272,400</p>
                    <p style="color: #666;"><em>Creating beautiful, durable spaces for prayer and fellowship</em></p>
                    <ul>
                        <li><strong>Sacred Space Atmosphere - Painting (R 80,000)</strong>
                            <ul>
                                <li>Peaceful colors enhancing worship and prayer environment</li>
                                <li>Welcoming exterior inviting community participation</li>
                                <li>Can be phased by room priority if needed</li>
                            </ul>
                        </li>
                        <li><strong>Durable Sanctuary Flooring - Tiling (R 100,000)</strong>
                            <ul>
                                <li>Long-lasting surfaces for active ministry and fellowship</li>
                                <li>Easy maintenance for volunteer cleaning teams</li>
                                <li>Can prioritize high-traffic worship areas first</li>
                            </ul>
                        </li>
                        <li><strong>Prayer Room Privacy - Doors (R 18,440)</strong>
                            <ul>
                                <li>Secure, private spaces for personal prayer and counseling</li>
                                <li>Enhanced security for sacred spaces</li>
                                <li>Can install in phases as budget allows</li>
                            </ul>
                        </li>
                        <li><strong>Supporting Infrastructure (R 73,960.88)</strong>
                            <ul>
                                <li>Windows for natural light in prayer spaces</li>
                                <li>Demolition for hall expansion</li>
                                <li>Finishing touches for dedication</li>
                            </ul>
                        </li>
                    </ul>
                </div>
                
                <div class="success-box">
                    <h3>💡 Budget Flexibility Options</h3>
                    <p style="color: #666; margin-bottom: 20px;"><em>Phased approach for stewardship and financial planning</em></p>
                    
                    <h4>If Budget Constraints Exist:</h4>
                    <ol>
                        <li><strong>Minimum Viable Sanctuary (R 320,000)</strong>
                            <ul>
                                <li>Roof waterproofing - protects from weather</li>
                                <li>Electrical upgrade - safe, reliable power for services</li>
                                <li>Basic plumbing (without solar geysers initially)</li>
                                <li>Essential ceilings for main worship hall</li>
                                <li><em>Enables continued worship services with foundational improvements</em></li>
                            </ul>
                        </li>
                        <li><strong>Phase 2 Expansion (+R 218,500)</strong>
                            <ul>
                                <li>Add solar geysers for blackout resilience</li>
                                <li>Complete hall ceiling extension for larger congregations</li>
                                <li>Basic painting for welcoming atmosphere</li>
                                <li><em>Enhances capacity and ensures uninterrupted ministry</em></li>
                            </ul>
                        </li>
                        <li><strong>Phase 3 Completion (+R 192,400)</strong>
                            <ul>
                                <li>Full painting for peaceful sacred atmosphere</li>
                                <li>Complete tiling for durable ministry spaces</li>
                                <li>Doors for prayer room privacy and security</li>
                                <li>Final touches for dedication and blessing ceremony</li>
                                <li><em>Creates beautiful, lasting sanctuary for generations</em></li>
                            </ul>
                        </li>
                    </ol>
                </div>
                
                <div class="warning-box">
                    <h3>⚠️ Critical Considerations</h3>
                    <ul>
                        <li><strong>Don't compromise on:</strong> Roof waterproofing (protects year-round worship) and electrical safety (protects congregation)</li>
                        <li><strong>Best stewardship ROI:</strong> Solar geysers pay for themselves in 3-5 years, freeing funds for ministry</li>
                        <li><strong>Weather dependent:</strong> Complete roofing before rainy season to avoid worship disruptions</li>
                        <li><strong>Code compliance:</strong> All electrical and plumbing certified for congregation safety</li>
                        <li><strong>Ministry sequence:</strong> Phased to minimize service interruptions and maintain weekly worship</li>
                        <li><strong>Kingdom impact:</strong> Investment creates generational blessing for community</li>
                    </ul>
                </div>
                
                <div style="text-align: center; margin-top: 40px;">
                    <a href="overview.html" class="nav-button">🔄 Start Over</a>
                    <a href="index.html" class="nav-button">🏠 Home</a>
                </div>
            </div>
        </div>
    </div>
</body>
</html>"""

with open(base_dir / 'prioritization.html', 'w', encoding='utf-8') as f:
    f.write(page7_content)
print("✓ Created prioritization.html")

# Update index.html for multipage site
index_multipage = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible House Renovation - Home</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            max-width: 900px;
            margin: 20px;
            background: white;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
        }
        h1 {
            color: #667eea;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        .info-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        .info-card {
            background: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            border-top: 3px solid #667eea;
        }
        .info-card h3 {
            color: #667eea;
            margin: 0 0 10px 0;
            font-size: 1.1em;
        }
        .info-card p {
            margin: 0;
            color: #333;
            font-size: 1.3em;
            font-weight: bold;
        }
        .nav-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
            margin-top: 30px;
        }
        .nav-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            padding: 25px;
            border-radius: 10px;
            transition: transform 0.3s, box-shadow 0.3s;
            text-align: center;
        }
        .nav-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
        }
        .nav-card h3 {
            margin: 0 0 10px 0;
            font-size: 1.3em;
        }
        .nav-card p {
            margin: 0;
            font-size: 0.9em;
            opacity: 0.9;
        }
        .version-toggle {
            text-align: center;
            margin: 30px 0;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 10px;
        }
        .version-toggle a {
            display: inline-block;
            margin: 10px;
            padding: 12px 25px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: all 0.3s;
        }
        .version-toggle a:hover {
            background: #764ba2;
        }
        @media screen and (max-width: 768px) {
            .container {
                padding: 20px;
                margin: 10px;
            }
            .nav-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏠 Bible House Renovation Project</h1>
        <p class="subtitle">Complete Professional Project Documentation</p>
        
        <div class="info-grid">
            <div class="info-card">
                <h3>Total Budget</h3>
                <p>R 730,900</p>
            </div>
            <div class="info-card">
                <h3>Timeline</h3>
                <p>8-12 weeks</p>
            </div>
            <div class="info-card">
                <h3>Categories</h3>
                <p>8 Major</p>
            </div>
            <div class="info-card">
                <h3>B/A Images</h3>
                <p>32 Total</p>
            </div>
        </div>

        <h2 style="color: #667eea; text-align: center; margin: 30px 0 20px;">📚 Step-by-Step Guide</h2>
        
        <div class="nav-grid">
            <a href="overview.html" class="nav-card">
                <h3>1️⃣ Overview</h3>
                <p>Project scope and objectives</p>
            </a>
            
            <a href="costs.html" class="nav-card">
                <h3>2️⃣ Costs</h3>
                <p>Complete budget breakdown</p>
            </a>
            
            <a href="materials.html" class="nav-card">
                <h3>3️⃣ Materials</h3>
                <p>Specifications & requirements</p>
            </a>
            
            <a href="timeline.html" class="nav-card">
                <h3>4️⃣ Timeline</h3>
                <p>Week-by-week schedule</p>
            </a>
            
            <a href="beforeafter.html" class="nav-card">
                <h3>5️⃣ Before & After (1)</h3>
                <p>Visual comparisons 1-8</p>
            </a>
            
            <a href="beforeafter2.html" class="nav-card">
                <h3>6️⃣ Before & After (2)</h3>
                <p>Visual comparisons 9-16</p>
            </a>
            
            <a href="prioritization.html" class="nav-card">
                <h3>7️⃣ Prioritization</h3>
                <p>Implementation recommendations</p>
            </a>
        </div>

        <div class="version-toggle">
            <h3 style="color: #667eea;">Choose Your View:</h3>
            <p style="margin-bottom: 15px;">Multi-page version (fast loading) or single-page version (all content at once)</p>
            <a href="overview.html">📚 Start Step-by-Step Guide</a>
            <a href="professional_renovation_plan_complete.html">📄 View Complete Single Page</a>
        </div>

        <div style="text-align: center; margin-top: 30px; color: #666; font-size: 0.9em;">
            <p><em>Last Updated: January 2026</em></p>
        </div>
    </div>
</body>
</html>"""

with open(base_dir / 'index.html', 'w', encoding='utf-8') as f:
    f.write(index_multipage)
print("✓ Updated index.html")

print(f"\n{'='*60}")
print("✅ Multi-page site created successfully!")
print(f"{'='*60}")
print(f"\nCreated 8 optimized pages:")
print("  1. index.html - Landing page with navigation")
print("  2. overview.html - Project overview (Step 1)")
print("  3. costs.html - Budget breakdown (Step 2)")
print("  4. materials.html - Materials & specs (Step 3)")
print("  5. timeline.html - Project timeline (Step 4)")
print("  6. beforeafter.html - Images 1-8 (Step 5)")
print("  7. beforeafter2.html - Images 9-16 (Step 6)")
print("  8. prioritization.html - Recommendations (Step 7)")
print(f"\n📊 File sizes significantly reduced:")
print("  • Each page: ~2-8 MB (vs 56MB single page)")
print("  • Faster loading on mobile")
print("  • Better navigation flow")
print(f"\n🚀 Ready to deploy to GitHub!")
