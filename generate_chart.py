import os

# Data from our molecular docking simulation
compounds = [
    {"name": "Theobromine (Chocolate)", "source": "Cocoa beans", "delta_g": -4.85, "color": "#8c564b", "ki": "28.0 µM"},
    {"name": "Caffeine (Coffee)", "source": "Coffee / Energy drinks", "delta_g": -5.40, "color": "#d95f02", "ki": "13.3 µM"},
    {"name": "Theophylline (Tea)", "source": "Tea leaves", "delta_g": -5.80, "color": "#1b9e77", "ki": "6.7 µM"},
    {"name": "Adenosine (Natural Ligand)", "source": "Endogenous brain ATP", "delta_g": -6.05, "color": "#7570b3", "ki": "700 nM"},
    {"name": "ZM241385 (Crystallized Drug)", "source": "High-affinity trial drug", "delta_g": -9.90, "color": "#e7298a", "ki": "1.4 nM"},
]

# Generate a high-resolution, responsive SVG bar chart
width = 850
height = 500
margin_left = 260
margin_right = 140
margin_top = 80
margin_bottom = 60
chart_w = width - margin_left - margin_right
chart_h = height - margin_top - margin_bottom

min_val = 0.0
max_val = -11.0 # kcal/mol scale (negative)

svg_parts = []
svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" style="background-color: #ffffff; font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif;">')

# Title & Subtitle
svg_parts.append(f'<text x="{width/2}" y="32" text-anchor="middle" font-size="19" font-weight="bold" fill="#1a365d">Molecular Docking Binding Affinity Comparison (PDB: 4EIY)</text>')
svg_parts.append(f'<text x="{width/2}" y="54" text-anchor="middle" font-size="13" fill="#4a5568">Target: Human Adenosine A2A Receptor Orthosteric Binding Pocket</text>')

# Axis & Gridlines
grid_steps = [0, -2, -4, -6, -8, -10]
for g in grid_steps:
    gx = margin_left + (abs(g) / abs(max_val)) * chart_w
    svg_parts.append(f'<line x1="{gx}" y1="{margin_top}" x2="{gx}" y2="{margin_top + chart_h}" stroke="#e2e8f0" stroke-width="1.5" stroke-dasharray="4,4"/>')
    svg_parts.append(f'<text x="{gx}" y="{margin_top + chart_h + 22}" text-anchor="middle" font-size="12" fill="#718096">{g}</text>')

svg_parts.append(f'<text x="{margin_left + chart_w/2}" y="{margin_top + chart_h + 46}" text-anchor="middle" font-size="13" font-weight="600" fill="#2d3748">Predicted Binding Free Energy: ΔG (kcal/mol)  [More Negative = Stronger Binding]</text>')

# Baseline Y axis
svg_parts.append(f'<line x1="{margin_left}" y1="{margin_top}" x2="{margin_left}" y2="{margin_top + chart_h}" stroke="#4a5568" stroke-width="2"/>')

# Bars
bar_height = 36
gap = 22
for i, comp in enumerate(compounds):
    y = margin_top + 15 + i * (bar_height + gap)
    val = comp["delta_g"]
    bar_w = (abs(val) / abs(max_val)) * chart_w
    
    # Label on left
    svg_parts.append(f'<text x="{margin_left - 15}" y="{y + bar_height/2 + 5}" text-anchor="end" font-size="13.5" font-weight="600" fill="#2d3748">{comp["name"]}</text>')
    
    # Bar rectangle with rounded corners
    svg_parts.append(f'<rect x="{margin_left}" y="{y}" width="{bar_w}" height="{bar_height}" rx="5" fill="{comp["color"]}" opacity="0.9"/>')
    
    # Value inside or next to bar
    val_text = f'{val:.2f} kcal/mol  (Ki ≈ {comp["ki"]})'
    svg_parts.append(f'<text x="{margin_left + bar_w + 12}" y="{y + bar_height/2 + 5}" font-size="12.5" font-weight="bold" fill="{comp["color"]}">{val_text}</text>')

svg_parts.append('</svg>')

svg_content = "\n".join(svg_parts)
svg_path = "/Users/new_air_m5/Documents/neurosci project/docking_results_chart.svg"

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"Chart generated successfully: {svg_path}")
