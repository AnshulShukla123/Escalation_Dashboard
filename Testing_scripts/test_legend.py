from app import app
from collections import Counter

with app.app_context():
    # Simulate what the template will receive
    closing_reason_labels = ['Bug', 'Network issue', 'Config issue', 'Infra issue', 'Serviceability issue', 'Location/AP/SDA', 'Routing', 'Documentation']
    closing_reason_data = [2, 1, 3, 0, 1, 1, 2, 1]
    colors = ['#f1c40f', '#3498db', '#9b59b6', '#27ae60', '#e74c3c', '#ff6b6b', '#4ecdc4', '#45b7d1']
    
    print("Dynamic legend will show:")
    total = sum(closing_reason_data)
    for i, (label, data) in enumerate(zip(closing_reason_labels, closing_reason_data)):
        if data > 0:
            percentage = round((data / total * 100) if total > 0 else 0, 1)
            print(f"  {label}: {data} ({percentage}%) - Color: {colors[i]}")
    
    print(f"\nTotal escalations with closing reasons: {total}")
    print("Categories that won't show (data = 0):")
    for i, (label, data) in enumerate(zip(closing_reason_labels, closing_reason_data)):
        if data == 0:
            print(f"  {label}: {data}")