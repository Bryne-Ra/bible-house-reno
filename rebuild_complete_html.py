import os
import base64
import json

# Get base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define image paths for materials
materials_images = {
    "ceiling": os.path.join(base_dir, "materials_and_spce", "ceilingwood_20250116_110824_0000.png"),
    "roof_paint": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0005.jpg"),
    "wall_paint": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0006.jpg"),
    "floor_tiles": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0007.jpg"),
    "solar1": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0008.jpg"),
    "solar2": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0009.jpg"),
    "water_tank": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0010.jpg"),
    "pump": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0011.jpg"),
    "jungle_gym1": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0012.jpg"),
    "jungle_gym2": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0013.jpg"),
    "benches": os.path.join(base_dir, "materials_and_spce", "IMG-20250116-WA0014.jpg")
}

# Define before/after image pairs - ALL available images
beforeafter_pairs = [
    {"before": "pic1b4.jpg.jpg", "after": "pic1after.jpg.png", "title": "Exterior Front View - Option 1"},
    {"before": "pic1b4.jpg.jpg", "after": "pic1after2.jpg.png", "title": "Exterior Front View - Option 2"},
    {"before": "pic2b4.jpg.jpg", "after": "pic2after.jpg.png", "title": "Side Entrance - Option 1"},
    {"before": "pic2b4.jpg.jpg", "after": "pic2after2.jpg.png", "title": "Side Entrance - Option 2"},
    {"before": "pic3b4.jpg.jpg", "after": "pic3after.jpg.png", "title": "Garden Area"},
    {"before": "pic3b42.jpg.jpg", "after": "pic3after.jpg.png", "title": "Garden Area - Alternate View"},
    {"before": "pic4b4.jpg.jpg", "after": "pic4after.jpg.png", "title": "Back Exterior"},
    {"before": "pic4b42.jpg.jpg", "after": "pic4after.jpg.png", "title": "Back Exterior - Alternate View"},
    {"before": "pic6b4.jpg.jpg", "after": "pic5after.jpg.png", "title": "Parking Area"},
    {"before": "pic6b42.jpg.jpg", "after": "pic5after.jpg.png", "title": "Parking Area - View 2"},
    {"before": "pic6b43.jpg.jpg", "after": "pic5after.jpg.png", "title": "Parking Area - View 3"},
    {"before": "pic6b4.jpg.jpg", "after": "pic6after.jpg.png", "title": "Entrance Walkway"},
    {"before": "pic7b4.jpg.jpg", "after": "pic7after.jpg.png", "title": "Roof & Structure"},
    {"before": "pic8b4.jpg.jpg", "after": "pic8after.jpg.png", "title": "Building Exterior"},
    {"before": "pic8b42.jpg.jpg", "after": "pic8after.jpg.png", "title": "Building Exterior - Alternate"},
    {"before": "junglegym1.jpg.jpg", "after": "junglegym2.jpg.jpg", "title": "Play Area Equipment"}
]

def get_mime_type(filename):
    """Determine MIME type from file extension"""
    ext = filename.lower().split('.')[-1]
    if ext in ['jpg', 'jpeg']:
        return 'image/jpeg'
    elif ext == 'png':
        return 'image/png'
    return 'image/jpeg'

def image_to_base64(image_path):
    """Convert image to base64 data URI"""
    try:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()
            b64_data = base64.b64encode(img_data).decode('utf-8')
            mime_type = get_mime_type(image_path)
            return f"data:{mime_type};base64,{b64_data}"
    except Exception as e:
        print(f"Error encoding {image_path}: {e}")
        return None

print("Encoding materials images...")
materials_encoded = {}
for key, path in materials_images.items():
    if os.path.exists(path):
        encoded = image_to_base64(path)
        if encoded:
            materials_encoded[key] = encoded
            print(f"✓ Encoded {key}")
    else:
        print(f"✗ Not found: {path}")

print(f"\nEncoding before/after images...")
beforeafter_encoded = []
ba_folder = os.path.join(base_dir, "before and after pictures")
for pair in beforeafter_pairs:
    before_path = os.path.join(ba_folder, pair["before"])
    after_path = os.path.join(ba_folder, pair["after"])
    
    if os.path.exists(before_path) and os.path.exists(after_path):
        before_data = image_to_base64(before_path)
        after_data = image_to_base64(after_path)
        if before_data and after_data:
            beforeafter_encoded.append({
                "title": pair["title"],
                "before": before_data,
                "after": after_data
            })
            print(f"✓ Encoded {pair['title']}")
    else:
        print(f"✗ Missing: {pair['title']}")

print(f"\n✓ Encoded {len(materials_encoded)} materials images")
print(f"✓ Encoded {len(beforeafter_encoded)} before/after pairs")

# Now create the complete HTML
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bible House Renovation - Professional Project Plan</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
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
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }
        
        .tabs {
            display: flex;
            background: #f5f5f5;
            padding: 0;
            overflow-x: auto;
            border-bottom: 3px solid #667eea;
        }
        
        .tab-button {
            flex: 1;
            min-width: 150px;
            padding: 20px;
            background: #f5f5f5;
            border: none;
            cursor: pointer;
            font-size: 1em;
            font-weight: 600;
            transition: all 0.3s;
            border-bottom: 3px solid transparent;
            color: #666;
        }
        
        .tab-button:hover {
            background: #e0e0e0;
            color: #333;
        }
        
        .tab-button.active {
            background: white;
            color: #667eea;
            border-bottom: 3px solid #667eea;
        }
        
        .tab-content {
            display: none;
            padding: 40px;
            animation: fadeIn 0.5s;
        }
        
        .tab-content.active {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .section {
            margin-bottom: 30px;
            padding: 25px;
            background: #f9f9f9;
            border-radius: 10px;
            border-left: 4px solid #667eea;
        }
        
        .section h2 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.8em;
        }
        
        .section h3 {
            color: #764ba2;
            margin-top: 20px;
            margin-bottom: 10px;
            font-size: 1.3em;
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
        
        .cost-card h4 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.2em;
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
            color: #764ba2;
            font-size: 1.1em;
        }
        
        .timeline {
            position: relative;
            padding-left: 30px;
        }
        
        .timeline-item {
            position: relative;
            padding: 20px;
            background: white;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -30px;
            top: 25px;
            width: 15px;
            height: 15px;
            background: #667eea;
            border-radius: 50%;
            box-shadow: 0 0 0 4px white, 0 0 0 6px #667eea;
        }
        
        .timeline-item h4 {
            color: #667eea;
            margin-bottom: 10px;
        }
        
        .info-box {
            background: #e3f2fd;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 4px solid #2196f3;
        }
        
        .warning-box {
            background: #fff3e0;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 4px solid #ff9800;
        }
        
        .success-box {
            background: #e8f5e9;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 4px solid #4caf50;
        }
        
        ul, ol {
            margin-left: 20px;
            margin-top: 10px;
        }
        
        li {
            margin-bottom: 8px;
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
        
        .highlight {
            background: #fff59d;
            padding: 2px 6px;
            border-radius: 3px;
        }
        
        /* Mobile Responsive Styles */
        @media screen and (max-width: 768px) {
            .container {
                padding: 10px;
            }
            
            .header h1 {
                font-size: 1.8em;
            }
            
            .header p {
                font-size: 0.9em;
            }
            
            .tabs {
                overflow-x: auto;
                white-space: nowrap;
                -webkit-overflow-scrolling: touch;
            }
            
            .tab-button {
                padding: 10px 15px;
                font-size: 0.85em;
            }
            
            .cost-grid {
                grid-template-columns: 1fr;
            }
            
            table {
                font-size: 0.85em;
            }
            
            th, td {
                padding: 10px 8px;
            }
            
            .comparison-container {
                height: 400px;
            }
            
            .success-box h2 {
                font-size: 1.8em !important;
            }
            
            .section {
                padding: 15px;
            }
        }
        
        @media screen and (max-width: 480px) {
            .header h1 {
                font-size: 1.5em;
            }
            
            .tab-button {
                padding: 8px 12px;
                font-size: 0.8em;
            }
            
            .section h2 {
                font-size: 1.5em;
            }
            
            .section h3 {
                font-size: 1.2em;
            }
            
            table {
                font-size: 0.75em;
            }
            
            th, td {
                padding: 8px 5px;
            }
            
            .comparison-container {
                height: 300px;
            }
            
            .success-box h2 {
                font-size: 1.5em !important;
            }
            
            .cost-item {
                font-size: 0.9em;
            }
            
            .section {
                padding: 10px;
            }
        }
        
        .materials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .material-card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        
        .material-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
        }
        
        .material-card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        
        .material-card-content {
            padding: 15px;
        }
        
        .material-card h4 {
            color: #667eea;
            margin-bottom: 10px;
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
        
        .comparison-container img {
            display: block;
            width: 100%;
            height: auto;
        }
        
        .comparison-before {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
        }
        
        .comparison-after {
            position: absolute;
            width: 50%;
            height: 100%;
            top: 0;
            left: 0;
            overflow: hidden;
        }
        
        .comparison-slider {
            position: absolute;
            width: 4px;
            height: 100%;
            background: #667eea;
            left: 50%;
            top: 0;
            cursor: ew-resize;
            z-index: 10;
        }
        
        .comparison-slider::before {
            content: '';
            position: absolute;
            width: 40px;
            height: 40px;
            background: white;
            border: 3px solid #667eea;
            border-radius: 50%;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }
        
        .comparison-label {
            position: absolute;
            top: 20px;
            padding: 8px 16px;
            background: rgba(0,0,0,0.7);
            color: white;
            font-weight: bold;
            border-radius: 5px;
            z-index: 5;
        }
        
        .comparison-label.before {
            left: 20px;
        }
        
        .comparison-label.after {
            right: 20px;
        }
        
        .comparison-info {
            text-align: center;
            margin-top: 15px;
            padding: 15px;
            background: #f5f5f5;
            border-radius: 10px;
        }
        
        .comparison-info h4 {
            color: #667eea;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏠 Bible House Renovation Project</h1>
            <p>Complete Professional Project Plan & Budget Breakdown</p>
            <p style="font-size: 0.9em; margin-top: 10px;">Total Budget: R 730,900</p>
        </div>
        
        <div class="tabs">
            <button class="tab-button active" onclick="showTab(event, 'overview')">📋 Overview</button>
            <button class="tab-button" onclick="showTab(event, 'costs')">💰 Costs</button>
            <button class="tab-button" onclick="showTab(event, 'materials')">🛠️ Materials & Specs</button>
            <button class="tab-button" onclick="showTab(event, 'timeline')">📅 Timeline</button>
            <button class="tab-button" onclick="showTab(event, 'beforeafter')">📸 Before & After</button>
            <button class="tab-button" onclick="showTab(event, 'documents')">📄 Documents</button>
            <button class="tab-button" onclick="showTab(event, 'prioritization')">⭐ Prioritization</button>
        </div>
        
        <div id="overview" class="tab-content active">
            <div class="section">
                <h2>Project Overview</h2>
                <div class="info-box">
                    <h3>📊 Project Scope</h3>
                    <p><strong>Total Budget:</strong> R 730,900</p>
                    <p><strong>Project Type:</strong> Comprehensive Building Renovation</p>
                    <p><strong>Location:</strong> Bible House</p>
                    <p><strong>Timeline:</strong> 8-12 weeks (estimated)</p>
                </div>
                
                <h3>🎯 Key Objectives</h3>
                <ul>
                    <li>Complete roof replacement and waterproofing</li>
                    <li>Full electrical system upgrade</li>
                    <li>Plumbing system modernization</li>
                    <li>Interior renovations (ceilings, walls, floors)</li>
                    <li>Solar power installation</li>
                    <li>Outdoor improvements and landscaping</li>
                </ul>
                
                <h3>📦 Major Work Categories</h3>
                <div class="cost-grid">
                    <div class="cost-card">
                        <h4>🏗️ Structural Work</h4>
                        <p>Roof, ceilings, walls, and foundational repairs</p>
                        <p><strong>Budget: ~R 280,000</strong></p>
                    </div>
                    <div class="cost-card">
                        <h4>⚡ Electrical Systems</h4>
                        <p>Complete rewiring, solar installation, and lighting</p>
                        <p><strong>Budget: ~R 180,000</strong></p>
                    </div>
                    <div class="cost-card">
                        <h4>💧 Plumbing Systems</h4>
                        <p>Water tanks, pumps, pipes, and fixtures</p>
                        <p><strong>Budget: ~R 120,000</strong></p>
                    </div>
                    <div class="cost-card">
                        <h4>🎨 Finishes</h4>
                        <p>Painting, tiling, flooring, and aesthetics</p>
                        <p><strong>Budget: ~R 90,000</strong></p>
                    </div>
                </div>
            </div>
        </div>
        
        <div id="costs" class="tab-content">
            <div class="section">
                <h2>💰 Detailed Cost Breakdown</h2>
                
                <h3>Roof & Ceiling Work</h3>
                <div class="cost-card">
                    <div class="cost-item">
                        <span>IBR Sheeting (26 sheets)</span>
                        <span>R 14,664.60</span>
                    </div>
                    <div class="cost-item">
                        <span>Ridge Caps (13 units)</span>
                        <span>R 1,274.52</span>
                    </div>
                    <div class="cost-item">
                        <span>Timber & Purlins</span>
                        <span>R 8,500.00</span>
                    </div>
                    <div class="cost-item">
                        <span>PVC Ceiling Boards (70 sq m)</span>
                        <span>R 21,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Ceiling Installation</span>
                        <span>R 35,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span><strong>Subtotal</strong></span>
                        <span><strong>R 80,439.12</strong></span>
                    </div>
                </div>
                
                <h3>Electrical Systems</h3>
                <div class="cost-card">
                    <div class="cost-item">
                        <span>Solar Panels (8x 550W)</span>
                        <span>R 60,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>5kW Inverter</span>
                        <span>R 45,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Battery Storage (10kWh)</span>
                        <span>R 55,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Electrical Wiring & Fittings</span>
                        <span>R 35,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Light Fixtures</span>
                        <span>R 15,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span><strong>Subtotal</strong></span>
                        <span><strong>R 210,000.00</strong></span>
                    </div>
                </div>
                
                <h3>Plumbing & Water Systems</h3>
                <div class="cost-card">
                    <div class="cost-item">
                        <span>Water Tanks (2x 5000L)</span>
                        <span>R 28,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Water Pump System</span>
                        <span>R 18,500.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Pipes & Fittings</span>
                        <span>R 22,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Plumbing Installation</span>
                        <span>R 35,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span><strong>Subtotal</strong></span>
                        <span><strong>R 103,500.00</strong></span>
                    </div>
                </div>
                
                <h3>Painting & Finishing</h3>
                <div class="cost-card">
                    <div class="cost-item">
                        <span>Interior Paint (200L)</span>
                        <span>R 18,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Exterior Paint (150L)</span>
                        <span>R 25,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Floor Tiles (80 sq m)</span>
                        <span>R 32,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Painting Labour</span>
                        <span>R 45,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span><strong>Subtotal</strong></span>
                        <span><strong>R 120,000.00</strong></span>
                    </div>
                </div>
                
                <h3>Outdoor & Recreation</h3>
                <div class="cost-card">
                    <div class="cost-item">
                        <span>Jungle Gym Equipment (2 units)</span>
                        <span>R 45,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Outdoor Benches (6 units)</span>
                        <span>R 18,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Landscaping</span>
                        <span>R 25,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span><strong>Subtotal</strong></span>
                        <span><strong>R 88,000.00</strong></span>
                    </div>
                </div>
                
                <h3>Labour & Miscellaneous</h3>
                <div class="cost-card">
                    <div class="cost-item">
                        <span>General Labour</span>
                        <span>R 60,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Project Management</span>
                        <span>R 20,000.00</span>
                    </div>
                    <div class="cost-item">
                        <span>Contingency (2%)</span>
                        <span>R 13,960.88</span>
                    </div>
                    <div class="cost-item">
                        <span><strong>Subtotal</strong></span>
                        <span><strong>R 93,960.88</strong></span>
                    </div>
                </div>
                
                <div class="success-box" style="margin-top: 30px;">
                    <h3>💵 GRAND TOTAL</h3>
                    <h2 style="color: #4caf50; font-size: 2.5em;">R 730,900.00</h2>
                </div>
            </div>
        </div>
        
        <div id="materials" class="tab-content">
            <div class="section">
                <h2>🛠️ Materials & Specifications</h2>
                
                <div class="info-box">
                    <h3>📦 Material Categories</h3>
                    <p>All materials have been carefully selected for quality, durability, and cost-effectiveness.</p>
                </div>
                
                <h3>Featured Materials</h3>
                <div class="materials-grid">
'''

# Add materials images
for key, title in [
    ("ceiling", "PVC Ceiling Boards"),
    ("roof_paint", "Roof Paint"),
    ("wall_paint", "Wall Paint"),
    ("floor_tiles", "Floor Tiles"),
    ("solar1", "Solar Panel System"),
    ("solar2", "Solar Installation"),
    ("water_tank", "Water Tank"),
    ("pump", "Water Pump"),
    ("jungle_gym1", "Jungle Gym - Type 1"),
    ("jungle_gym2", "Jungle Gym - Type 2"),
    ("benches", "Outdoor Benches")
]:
    if key in materials_encoded:
        html_content += f'''
                    <div class="material-card">
                        <img src="{materials_encoded[key]}" alt="{title}">
                        <div class="material-card-content">
                            <h4>{title}</h4>
                            <p>Professional grade material</p>
                        </div>
                    </div>
'''

html_content += '''
                </div>
                
                <h3>📋 Complete Materials List</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Category</th>
                            <th>Item</th>
                            <th>Quantity</th>
                            <th>Specifications</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Roofing</td>
                            <td>IBR Sheeting</td>
                            <td>26 sheets</td>
                            <td>0.45mm gauge, Colorbon finish</td>
                        </tr>
                        <tr>
                            <td>Roofing</td>
                            <td>Ridge Caps</td>
                            <td>13 units</td>
                            <td>3m length, matching profile</td>
                        </tr>
                        <tr>
                            <td>Ceiling</td>
                            <td>PVC Ceiling Boards</td>
                            <td>70 sq m</td>
                            <td>White wood pattern, 250mm width</td>
                        </tr>
                        <tr>
                            <td>Electrical</td>
                            <td>Solar Panels</td>
                            <td>8 panels</td>
                            <td>550W monocrystalline, 25yr warranty</td>
                        </tr>
                        <tr>
                            <td>Electrical</td>
                            <td>Inverter</td>
                            <td>1 unit</td>
                            <td>5kW hybrid inverter</td>
                        </tr>
                        <tr>
                            <td>Electrical</td>
                            <td>Battery Storage</td>
                            <td>1 system</td>
                            <td>10kWh lithium battery</td>
                        </tr>
                        <tr>
                            <td>Plumbing</td>
                            <td>Water Tanks</td>
                            <td>2 tanks</td>
                            <td>5000L JOJO tanks</td>
                        </tr>
                        <tr>
                            <td>Plumbing</td>
                            <td>Water Pump</td>
                            <td>1 unit</td>
                            <td>1.5HP pressure pump</td>
                        </tr>
                        <tr>
                            <td>Paint</td>
                            <td>Interior Paint</td>
                            <td>200L</td>
                            <td>Dulux washable PVA</td>
                        </tr>
                        <tr>
                            <td>Paint</td>
                            <td>Exterior Paint</td>
                            <td>150L</td>
                            <td>Weatherguard acrylic</td>
                        </tr>
                        <tr>
                            <td>Flooring</td>
                            <td>Floor Tiles</td>
                            <td>80 sq m</td>
                            <td>600x600mm porcelain</td>
                        </tr>
                        <tr>
                            <td>Outdoor</td>
                            <td>Jungle Gyms</td>
                            <td>2 units</td>
                            <td>Commercial grade, 5-12 years</td>
                        </tr>
                        <tr>
                            <td>Outdoor</td>
                            <td>Benches</td>
                            <td>6 units</td>
                            <td>Treated timber, 1.8m length</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        
        <div id="timeline" class="tab-content">
            <div class="section">
                <h2>📅 Project Timeline</h2>
                
                <div class="info-box">
                    <h3>⏱️ Estimated Duration: 8-12 weeks</h3>
                    <p>Timeline may vary based on weather conditions, material availability, and unforeseen circumstances.</p>
                </div>
                
                <div class="timeline">
                    <div class="timeline-item">
                        <h4>Week 1-2: Preparation & Demolition</h4>
                        <ul>
                            <li>Site preparation and protection</li>
                            <li>Removal of old roofing materials</li>
                            <li>Structural assessment and repairs</li>
                            <li>Material procurement begins</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Week 3-4: Structural Work</h4>
                        <ul>
                            <li>Roof installation (IBR sheeting)</li>
                            <li>Timber and purlin installation</li>
                            <li>Waterproofing and sealing</li>
                            <li>Ceiling framework setup</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Week 5-6: Systems Installation</h4>
                        <ul>
                            <li>Electrical rewiring</li>
                            <li>Solar panel installation</li>
                            <li>Plumbing system upgrade</li>
                            <li>Water tank installation</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Week 7-8: Interior Finishing</h4>
                        <ul>
                            <li>Ceiling board installation</li>
                            <li>Interior painting</li>
                            <li>Floor tiling</li>
                            <li>Fixture installation</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Week 9-10: Exterior Work</h4>
                        <ul>
                            <li>Exterior painting</li>
                            <li>Landscaping</li>
                            <li>Outdoor equipment installation</li>
                            <li>Jungle gym assembly</li>
                        </ul>
                    </div>
                    
                    <div class="timeline-item">
                        <h4>Week 11-12: Final Touches</h4>
                        <ul>
                            <li>Quality inspections</li>
                            <li>Touch-ups and corrections</li>
                            <li>System testing</li>
                            <li>Final walkthrough and handover</li>
                        </ul>
                    </div>
                </div>
                
                <div class="warning-box">
                    <h3>⚠️ Important Notes</h3>
                    <ul>
                        <li>Weather-dependent activities may cause delays</li>
                        <li>Material delivery schedules must be coordinated</li>
                        <li>Some phases may overlap for efficiency</li>
                        <li>Regular progress meetings recommended weekly</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div id="beforeafter" class="tab-content">
            <div class="section">
                <h2>📸 Before & After Comparisons</h2>
                
                <div class="info-box">
                    <h3>🔄 Interactive Comparisons</h3>
                    <p>Drag the slider to compare before and after images. These visualizations show the transformation planned for Bible House.</p>
                </div>
'''

# Add before/after comparisons
for pair in beforeafter_encoded:
    html_content += f'''
                <div class="comparison-container">
                    <div class="comparison-label before">BEFORE</div>
                    <div class="comparison-label after">AFTER</div>
                    
                    <!-- Before Image -->
                    <img src="{pair['before']}" alt="{pair['title']} - Before" 
                         style="position: absolute; width: 100%; height: 100%; object-fit: cover; left: 0; top: 0;">
                    
                    <!-- After Image with slider -->
                    <div class="comparison-after">
                        <img src="{pair['after']}" alt="{pair['title']} - After" 
                             style="width: 100%; height: 100%; object-fit: cover;">
                    </div>
                    
                    <div class="comparison-slider"></div>
                    
                    <div class="comparison-info">
                        <h4>{pair['title']}</h4>
                    </div>
                </div>
'''

html_content += '''
            </div>
        </div>
        
        <div id="documents" class="tab-content">
            <div class="section">
                <h2>📄 Project Documents</h2>
                
                <h3>Available Documents</h3>
                <ul>
                    <li>📋 Detailed Cost Estimate (PDF)</li>
                    <li>📐 Architectural Plans</li>
                    <li>🔧 Technical Specifications</li>
                    <li>📝 Material Purchase Orders</li>
                    <li>✅ Quality Assurance Checklist</li>
                    <li>📊 Progress Reports Template</li>
                </ul>
                
                <div class="info-box">
                    <h3>📁 Document Management</h3>
                    <p>All project documents are maintained in the project folder structure:</p>
                    <ul>
                        <li><strong>ocr/</strong> - Scanned estimates and invoices</li>
                        <li><strong>materials_and_spce/</strong> - Material specifications</li>
                        <li><strong>before and after pictures/</strong> - Visual documentation</li>
                        <li><strong>presentation/</strong> - Client presentation materials</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div id="prioritization" class="tab-content">
            <div class="section">
                <h2>⭐ Work Prioritization</h2>
                
                <div class="success-box">
                    <h3>🎯 Critical Priority (Must Complete First)</h3>
                    <ol>
                        <li><strong>Roof Replacement</strong> - Prevents water damage</li>
                        <li><strong>Structural Repairs</strong> - Ensures building safety</li>
                        <li><strong>Electrical Safety</strong> - Prevents hazards</li>
                        <li><strong>Plumbing Basics</strong> - Ensures water supply</li>
                    </ol>
                </div>
                
                <div class="warning-box">
                    <h3>⚠️ High Priority (Complete Early)</h3>
                    <ol>
                        <li>Solar panel installation</li>
                        <li>Water tank setup</li>
                        <li>Ceiling installation</li>
                        <li>Interior painting</li>
                    </ol>
                </div>
                
                <div class="info-box">
                    <h3>📋 Medium Priority (Mid-Project)</h3>
                    <ol>
                        <li>Floor tiling</li>
                        <li>Exterior painting</li>
                        <li>Landscaping basics</li>
                        <li>Lighting fixtures</li>
                    </ol>
                </div>
                
                <div style="background: #f5f5f5; padding: 20px; border-radius: 10px; margin-top: 20px;">
                    <h3>✨ Lower Priority (Final Phase)</h3>
                    <ol>
                        <li>Jungle gym installation</li>
                        <li>Bench placement</li>
                        <li>Decorative elements</li>
                        <li>Final landscaping touches</li>
                    </ol>
                </div>
                
                <div class="info-box" style="margin-top: 30px;">
                    <h3>💡 Optimization Tips</h3>
                    <ul>
                        <li>Weather-dependent tasks should be scheduled during favorable conditions</li>
                        <li>Material deliveries should align with installation schedules</li>
                        <li>Interior work can proceed while exterior work is ongoing</li>
                        <li>Some tasks can be parallelized to reduce overall timeline</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        function showTab(event, tabName) {
            // Hide all tab contents
            const tabContents = document.getElementsByClassName('tab-content');
            for (let i = 0; i < tabContents.length; i++) {
                tabContents[i].classList.remove('active');
            }
            
            // Remove active class from all buttons
            const tabButtons = document.getElementsByClassName('tab-button');
            for (let i = 0; i < tabButtons.length; i++) {
                tabButtons[i].classList.remove('active');
            }
            
            // Show the selected tab and mark button as active
            document.getElementById(tabName).classList.add('active');
            event.currentTarget.classList.add('active');
        }
        
        // Before/After slider functionality
        document.addEventListener('DOMContentLoaded', function() {
            const containers = document.querySelectorAll('.comparison-container');
            
            containers.forEach(container => {
                const slider = container.querySelector('.comparison-slider');
                const afterDiv = container.querySelector('.comparison-after');
                let isDragging = false;
                
                function updateSlider(x) {
                    const rect = container.getBoundingClientRect();
                    const position = ((x - rect.left) / rect.width) * 100;
                    const clampedPosition = Math.max(0, Math.min(100, position));
                    
                    afterDiv.style.width = clampedPosition + '%';
                    slider.style.left = clampedPosition + '%';
                }
                
                slider.addEventListener('mousedown', () => isDragging = true);
                
                container.addEventListener('mousemove', (e) => {
                    if (isDragging) updateSlider(e.clientX);
                });
                
                document.addEventListener('mouseup', () => isDragging = false);
                
                container.addEventListener('touchstart', () => isDragging = true);
                
                container.addEventListener('touchmove', (e) => {
                    if (isDragging) {
                        e.preventDefault();
                        updateSlider(e.touches[0].clientX);
                    }
                });
                
                document.addEventListener('touchend', () => isDragging = false);
            });
        });
    </script>
</body>
</html>
'''

# Write the HTML file
output_path = os.path.join(base_dir, "professional_renovation_plan_complete.html")
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

file_size = os.path.getsize(output_path)
print(f"\n✅ HTML file created successfully!")
print(f"📁 Location: {output_path}")
print(f"📊 File size: {file_size:,} bytes ({file_size/1024/1024:.1f} MB)")
print(f"🖼️  Total embedded images: {len(materials_encoded) + len(beforeafter_encoded) * 2}")
